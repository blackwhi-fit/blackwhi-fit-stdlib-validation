#!/usr/bin/env python3
"""Execute all specification cases against the genuine BlackWhi Rust/Starlark worker.

No mocks and no Python reimplementation of FIT predicates. The only Python-side
logic generates the fixture, invokes the actual worker and checks JSON outcomes.
"""
from __future__ import annotations
import argparse, json, os, shutil, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--engine', type=Path, required=True, help='Path to blackwhi-fit-engine executable')
    args = parser.parse_args()
    if not args.engine.is_file():
        print('[BLOCK] Actual FIT engine not found:',args.engine);return 2
    cases = json.loads((ROOT/'tests/cases.json').read_text(encoding='utf-8'))['cases']
    names = 'is_string is_integer is_number is_boolean is_list is_tuple is_dict is_none is_scalar is_collection is_json_value type_is'.split()
    setup = [
        'def make_deep(n):', '    value = 0', '    for _ in range(n):', '        value = [value]', '    return value',
        'deep_33 = make_deep(33)', 'deep_32 = make_deep(32)', 'deep_31 = make_deep(31)',
        'many_1024 = [0 for _ in range(1024)]',
        'many_1023 = [0 for _ in range(1023)]',
        'many_8192 = [0 for _ in range(8192)]',
        'dict_many_1024 = {str(i): i for i in range(1024)}',
        'cycle = []','cycle.append(cycle)',
        'stable = {"x": [1, 2]}',
    ]
    lines = ['load("modules/types.fit", '+', '.join(json.dumps(x) for x in names)+')', *setup,
             '[', *('    '+c['expr']+',' for c in cases), ']']
    with tempfile.TemporaryDirectory(prefix='blackwhi-stdlib-validation-test-') as folder:
        tmp=Path(folder); (tmp/'modules').mkdir()
        shutil.copyfile(ROOT/'packages/core/modules/types.fit',tmp/'modules/types.fit')
        script=tmp/'test.fit';script.write_text('\n'.join(lines)+'\n',encoding='utf-8')
        for action in ('validate','run-secure'):
            try:
                result=subprocess.run([str(args.engine.resolve()),action,str(script)],cwd=tmp,
                    capture_output=True,text=True,timeout=25,env={'PATH':os.environ.get('PATH','/usr/bin:/bin'),'LANG':'C.UTF-8'})
                payload=json.loads(result.stdout)
            except (subprocess.TimeoutExpired,ValueError,OSError) as exc:
                print('[FAIL]',action,type(exc).__name__);return 1
            if result.returncode or payload.get('ok') is not True or payload.get('protocol')!=1:
                print('[FAIL]',action,result.stderr[:500],result.stdout[:1000]);return 1
            data=payload['data']
            if action=='validate':
                if data.get('executed') is not False: print('[FAIL] validate executed script');return 1
            else:
                if data.get('native_capabilities') is not False or data['result'].get('capabilities')!=[]:
                    print('[FAIL] secure engine was not capability-free');return 1
                output=data['result']['value']
                if len(output)!=len(cases):
                    print('[FAIL] Expected',len(cases),'outcomes, got',len(output));return 1
                failures=[(c['id'],c['expr'],c['expected'],got)
                          for c,got in zip(cases,output) if type(got) is not bool or got != c['expected']]
                for case in failures[:20]:print('[FAIL]',case)
                if failures: print('[FAIL]',len(failures),'/',len(cases));return 1
                print('[PASS]',len(cases),'real FIT/Starlark cases; no native capabilities')
    return 0

if __name__=='__main__':raise SystemExit(main())
