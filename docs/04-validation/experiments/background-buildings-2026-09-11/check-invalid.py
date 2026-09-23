import json
from pathlib import Path
from generate import validate
cases=[{'width':0},{'width':21},{'width':float('nan')},{'depth':2},{'depth':17},{'floors':0},{'floors':9},{'floors':2.5},{'floors':True},{'palette':3},{'palette':-1}]
results=[]
for override in cases:
    p={'width':8,'depth':8,'floors':4,'palette':0,**override}
    try: validate(p); rejected=False
    except ValueError: rejected=True
    results.append({'override':repr(override),'rejected':rejected})
Path(__file__).with_name('invalid-results.json').write_text(json.dumps(results,indent=2))
assert all(x['rejected'] for x in results)
print(len(results),'invalid inputs rejected')
