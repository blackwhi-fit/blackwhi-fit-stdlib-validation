#!/usr/bin/env python3
"""Produce a real FIT-03 .fitpkg using the official BlackWhi packaging worker.

Only copies required BlackWhi tools into a private temporary workspace. This
script never modifies blackwhi-v2, Git history, or the user's existing apps.
"""
from __future__ import annotations
import argparse,hashlib,json,os,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
LIB='com.blackwhi.std.validation.core'
VER='0.1.0'

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--blackwhi-root',type=Path,default=ROOT.parent.parent/'blackwhi-v2')
    args=p.parse_args();bw=args.blackwhi_root.expanduser().resolve()
    required=['package.json','pnpm-workspace.yaml','apps/cli/package.json','apps/api/package.json',
             'crates/fit-engine/target/debug/blackwhi-fit-engine',
             'tools/fit/fit03_program_contract_v050.py','tools/fit/fit03_modules_v051.py',
             'tools/fit/fit03_packages_v052.py']
    for rel in required:
        pth=bw/rel
        if not pth.is_file() or pth.is_symlink():
            print('[BLOCK] Original BlackWhi contract missing:',pth);return 2
    # Assert expected identity before running the official worker.
    meta=json.loads((bw/'package.json').read_bytes())
    if meta.get('name')!='blackwhi':
        print('[BLOCK] Not a BlackWhi workspace');return 2
    subprocess.run([sys.executable,str(ROOT/'scripts/verify_source.py')],check=True)
    archive=f'{LIB}-{VER}.fitpkg'
    release=ROOT/'dist'/archive
    with tempfile.TemporaryDirectory(prefix='blackwhi-fit-stdlib-build-') as folder:
        stage=Path(folder)
        for rel in required:
            dest=stage/rel;dest.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(bw/rel,dest)
        library=stage/f'libraries/fit/{LIB}/{VER}'
        library.mkdir(parents=True)
        shutil.copy2(ROOT/'packages/core/fit-library.json',library/'fit-library.json')
        (library/'modules').mkdir()
        shutil.copy2(ROOT/'packages/core/modules/types.fit',library/'modules/types.fit')
        app=stage/'programs/fit/stdlib-validation-core';app.mkdir(parents=True)
        for fn in ['main.fit','fit-program.json','fit-lock.json']:
            shutil.copy2(ROOT/'packages/core'/fn,app/fn)
        official=stage/'tools/fit/fit03_packages_v052.py'
        common=[sys.executable,str(official),'--root',str(stage),'--json']
        pack='programs/fit/stdlib-validation-core/fit-program.json'
        for action,name in [('validate',pack),('pack',pack),('verify',f'programs/fit/stdlib-validation-core/{archive}'),('run',f'programs/fit/stdlib-validation-core/{archive}')]:
            result=subprocess.run([*common,action,name],capture_output=True,text=True,timeout=45)
            try: info=json.loads(result.stdout)
            except ValueError:print('[FAIL]',action,result.stderr[:400],result.stdout[:400]);return 1
            if result.returncode or info.get('status')!='PASS':
                print('[FAIL]',action,info);return 1
            print('[PASS] Official FIT-03',action)
            if action=='run':
                out=info.get('result')
                if not isinstance(out,dict) or out.get('smoke') is not True or out.get('rejects_boolean_as_integer') is not True:
                    print('[FAIL] Real package smoke did not pass:',out);return 1
        # A different FIT program must import the library through an exact-version lock.
        consumer=stage/'programs/fit/independent-consumer'
        consumer.mkdir(parents=True)
        consumer_code=(
            '# BlackWhi independent consumer integration proof.\n'
            'load("vendor/com.blackwhi.std.validation.core/0.1.0/modules/types.fit", '
            '"is_integer", "is_json_value", "type_is")\n'
            '{"external_consumer_pass": is_integer(42) and '
            'is_json_value({"name": "Fitness", "age": 42}) and '
            'type_is(None, "NoneType")}\n'
        )
        (consumer/'main.fit').write_text(consumer_code,encoding='utf-8')
        consumer_manifest=json.loads((ROOT/'packages/core/fit-program.json').read_bytes())
        consumer_manifest['id']='org.blackwhi.quality.validation-consumer'
        consumer_manifest['metadata']['title']='External FIT Validation consumer'
        consumer_manifest['source']['modules'][0]['sha256']=hashlib.sha256(consumer_code.encode()).hexdigest()
        manifest_raw=(json.dumps(consumer_manifest,sort_keys=True,indent=2,ensure_ascii=False)+'\n').encode()
        (consumer/'fit-program.json').write_bytes(manifest_raw)
        consumer_lock={'contract':'blackwhi.fit.lock.v1',
                       'program':{'id':consumer_manifest['id'],'version':consumer_manifest['version'],
                                  'manifest_sha256':hashlib.sha256(manifest_raw).hexdigest()},
                       'libraries':[{'id':LIB,'version':VER,
                                     'manifest_sha256':hashlib.sha256((library/'fit-library.json').read_bytes()).hexdigest()}]}
        (consumer/'fit-lock.json').write_text(json.dumps(consumer_lock,sort_keys=True,indent=2,ensure_ascii=False)+'\n')
        consumer_path='programs/fit/independent-consumer/fit-program.json'
        for action,name in [('validate',consumer_path),('pack',consumer_path),
                            ('verify',f'programs/fit/independent-consumer/{consumer_manifest["id"]}-{VER}.fitpkg'),
                            ('run',f'programs/fit/independent-consumer/{consumer_manifest["id"]}-{VER}.fitpkg')]:
            proc=subprocess.run([*common,action,name],capture_output=True,text=True,timeout=45)
            try: info=json.loads(proc.stdout)
            except ValueError: print('[FAIL] External consumer',action,proc.stdout[:200]);return 1
            if proc.returncode or info.get('status')!='PASS':
                print('[FAIL] External consumer',action,info);return 1
            if action=='run' and info.get('result',{}).get('external_consumer_pass') is not True:
                print('[FAIL] External consumer returned false:',info);return 1
            print('[PASS] Independent FIT consumer',action)
        content=(app/archive).read_bytes()
        release.parent.mkdir(parents=True,exist_ok=True)
        if release.exists() and release.read_bytes()!=content:
            print('[BLOCK] Existing artifact differs, refusing to overwrite:',release);return 2
        if not release.exists(): release.write_bytes(content)
        checksum=hashlib.sha256(content).hexdigest()
        sha_file=ROOT/'dist/SHA256SUMS.txt'
        line=f'{checksum}  {archive}\n'
        if sha_file.exists() and sha_file.read_text()!=line:
            print('[BLOCK] Existing SHA256SUMS differs');return 2
        sha_file.write_text(line)
        print('[PASS] Real verified .fitpkg:',release,'bytes:',len(content),'sha256:',checksum)
    return 0

if __name__=='__main__':raise SystemExit(main())
