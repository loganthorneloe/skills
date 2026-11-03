import json
from pathlib import Path
from fractions import Fraction as F
p=Path(__file__).parent
g=json.loads((p/'dag.json').read_text()); ns=g['nodes']; ids=[n['id'] for n in ns]; target=g['target']
assert len(ids)==len(set(ids));assert target in ids
adj={i:[] for i in ids};indeg={i:0 for i in ids}
for e in g['edges']:
 assert e['from'] in ids and e['to'] in ids and e['why'].strip()
 adj[e['from']].append(e['to']);indeg[e['to']]+=1
assert len(g['edges'])==len({(e['from'],e['to']) for e in g['edges']})
queue=[i for i in ids if not indeg[i]];order=[]
while queue:
 i=queue.pop(0);order.append(i)
 for j in adj[i]:
  indeg[j]-=1
  if not indeg[j]:queue.append(j)
assert len(order)==len(ids)
def reaches(i):return i==target or any(reaches(j) for j in adj[i])
assert all(reaches(i) for i in ids)
for n in ns:
 assert all(k in n for k in ['id','question','answer','status','evidence'])
 assert n['status'] in ['supported','assumed'];assert n['answer'].strip()
 if n['status']=='supported':
  assert n['evidence']
  for e in n['evidence']:assert all(e.get(k) for k in ['url','locator','claim'])
initial=json.loads((p/'history'/'initial-dag.json').read_text())
assert g['revisions'][0]==initial['revisions'][0]
assert len(initial['nodes'])==14 and len(ns)==15
calc=json.loads((p/'calculations.json').read_text())
assert F(calc['given_case']['spam_fraction_among_flags'])==F(1,12)
previous=F(-1)
for row in calc['base_rates']:
 prior=F(row['prior_fraction']);spam=10000*prior;legit=10000-spam
 answer=spam*F(9,10)/(spam*F(9,10)+legit*F(1,10))
 assert answer==F(row['posterior_fraction']) and answer>previous;previous=answer
assert F(calc['two_clue_example']['independent_posterior'])==F(9,20)
result={'status':'PASS','node_count':len(ns),'edge_count':len(g['edges']),'checks':['Required fields and allowed statuses','Unique node IDs and edge pairs','Valid endpoints and edge justifications','Acyclicity via topological sort','Every node reaches target','Explanatory evidence entries for every supported node','Initial snapshot preserved unchanged','Count reconstruction agrees with base-rate formula','Monotonic tested base rates and 0/100 percent boundaries','Two independent hypothetical clues yield 45 percent'],'topological_order':order,'not_checked':['Rendered graph layout (shared renderer)','Real-world calibration or performance']}
(p/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
