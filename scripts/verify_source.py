#!/usr/bin/env python3
"""Check first-party manifests and specification consistency without executing FIT."""
from __future__ import annotations
import hashlib,json,sys

def require(condition,detail):
    if not condition: raise SystemExit('[FAIL] '+detail)
from pathlib import Path
r=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
lib=json.loads((r/'packages/core/fit-library.json').read_bytes())
prog=json.loads((r/'packages/core/fit-program.json').read_bytes())
lock=json.loads((r/'packages/core/fit-lock.json').read_bytes())
require(lib['id']=='com.blackwhi.std.validation.core' and lib['version']=='0.1.0', 'library identity')
require(prog['contract']=='blackwhi.fit.program.v2', 'program schema')
require(sha((r/'packages/core/modules/types.fit').read_bytes())==lib['modules'][0]['sha256'], 'FIT library SHA-256')
require(sha((r/'packages/core/main.fit').read_bytes())==prog['source']['modules'][0]['sha256'], 'main.fit SHA-256')
require(lock['libraries'][0]['manifest_sha256']==sha((r/'packages/core/fit-library.json').read_bytes()), 'library manifest lock')
require(lock['program']['manifest_sha256']==sha((r/'packages/core/fit-program.json').read_bytes()), 'program manifest lock')
cat=json.loads((r/'docs/specifications/validation/v0.1.0/CATALOG.PROPOSAL.json').read_bytes())
require(cat['validator_count']==298 and cat['families']==21 and len(cat['items'])==298, 'catalog 298/21')
cases=json.loads((r/'tests/cases.json').read_bytes())['cases']
require(len(cases)>=80 and len({x['id'] for x in cases})==len(cases), 'test inventory')
required='is_string is_integer is_number is_boolean is_list is_tuple is_dict is_none is_scalar is_collection is_json_value type_is'.split()
source=(r/'packages/core/modules/types.fit').read_text()
for name in required: require(f'def {name}(' in source, 'missing API '+name)
print(f'[PASS] Manifests SHA-256, catalog 298/21, {len(cases)} test definitions, 12 APIs')
