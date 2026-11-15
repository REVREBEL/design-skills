#!/usr/bin/env python3
from pathlib import Path
import json,sys,math
sys.path.insert(0,str(Path(__file__).parent))
from metrics import metrics, net_after_acquisition, revpar_effects, pace
root=Path(__file__).resolve().parents[1]
records=json.loads((root/'evals/metric-fixtures.json').read_text())['fixtures']
fail=[]
for rec in records:
    k=rec['kind']; a=rec['input']
    if k=='metrics': out=metrics(**a)
    elif k=='net': out=net_after_acquisition(**a)
    elif k=='attribution': out=revpar_effects(**a)
    elif k=='pace': out={'paceVariance':pace(**a)}
    else: raise ValueError(k)
    for field,expected in rec['expected'].items():
        actual=out.get(field)
        if not ((expected is None and actual is None) or (isinstance(expected,(int,float)) and isinstance(actual,(int,float)) and math.isclose(actual,expected,rel_tol=1e-9,abs_tol=1e-9))):
            fail.append(f"{rec['id']}.{field}: {actual!r} != {expected!r}")
    print(('FAIL' if any(x.startswith(rec['id']+'.') for x in fail) else 'PASS'),rec['id'])
if fail:
    print('\n'.join(fail));sys.exit(1)
print(f"PASS: {len(records)} metric fixtures")
