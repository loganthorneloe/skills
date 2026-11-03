import json
from pathlib import Path
from collections import Counter,deque
p=Path(__file__).parent;g=json.loads((p/'dag.json').read_text())
ids=[n['id'] for n in g['nodes']]; assert len(ids)==len(set(ids)); by={n['id']:n for n in g['nodes']}
assert g['target_id'] in by
adj={x:[] for x in ids};rev={x:[] for x in ids}; deg={x:0 for x in ids}
assert len({(e['from'],e['to']) for e in g['edges']})==len(g['edges'])
for e in g['edges']:
 assert e['from'] in by and e['to'] in by and e['why'].strip()
 adj[e['from']].append(e['to']);rev[e['to']].append(e['from']);deg[e['to']]+=1
q=deque(x for x in ids if deg[x]==0);order=[]
while q:
 x=q.popleft();order.append(x)
 for y in adj[x]:
  deg[y]-=1
  if deg[y]==0:q.append(y)
assert len(order)==len(ids),'cycle'
for x in ids:
 seen=set();todo=[x]
 while todo:
  z=todo.pop()
  if z not in seen:seen.add(z);todo+=adj[z]
 assert g['target_id'] in seen,f'{x} no target path'
for n in g['nodes']:
 assert all(k in n for k in ['id','question','answer','status','evidence'])
 assert n['status'] in ['assumed','supported','partial','gap']
 if n['status']=='supported':
  assert n['evidence']
  for e in n['evidence']:assert all(e[k] for k in ['url','locator','exact_claim'])
for x in ids:
 if not rev[x]:assert by[x]['status']=='assumed',f'unexplained root {x}'
# Check saved history has actual starting state and reconstructable node/edge changes.
initial=json.loads((p/'history/initial.json').read_text()); replay=json.loads(json.dumps(initial))
for i in [1,2]:
 r=json.loads((p/f'history/round-{i:02}.json').read_text())
 for ch in r['changes']:
  old=next((n for n in replay['nodes'] if n['id']==ch['id']),None);assert old==ch['before']
  if old is None:replay['nodes'].append(ch['after'])
  else:replay['nodes'][replay['nodes'].index(old)]=ch['after']
 if 'edges_after' in r:replay['edges']=r['edges_after']
assert replay['nodes']==g['nodes'] and replay['edges']==g['edges']
result=dict(result='PASS',node_count=len(ids),edge_count=len(g['edges']),status_counts=dict(Counter(n['status'] for n in g['nodes'])),checks=['unique IDs','valid target','valid edge endpoints','no duplicate edges','nonempty edge necessity rationales','acyclic','all nodes reach target','all roots reader-assumed','required node fields','supported evidence fields present','initial and actual rounds reconstruct final nodes/edges'],topological_order=order,limits=['Structural checks do not establish prerequisite quality or evidence truth.','Evidence/edge semantic review performed manually; no live assistant evaluation or rendering performed.'])
(p/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
