import json,pathlib,collections
p=pathlib.Path(__file__).parent
d=json.loads((p/'dag.json').read_text())
ids=[n['id'] for n in d['nodes']]; lookup={n['id']:n for n in d['nodes']}
assert len(ids)==len(set(ids))
adj={i:[] for i in ids}; indeg={i:0 for i in ids}
for e in d['edges']:
 assert e['from'] in adj and e['to'] in adj and e['why']
 adj[e['from']].append(e['to']);indeg[e['to']]+=1
q=collections.deque(i for i in ids if not indeg[i]);order=[]
while q:
 i=q.popleft();order.append(i)
 for j in adj[i]:
  indeg[j]-=1
  if not indeg[j]:q.append(j)
assert len(order)==len(ids)
def reachable(a,b):
 todo=[a]; seen=set()
 while todo:
  c=todo.pop()
  if c==b:return True
  if c not in seen:seen.add(c);todo+=adj[c]
 return False
assert all(reachable(i,d['target']) for i in ids)
for n in d['nodes']:
 assert all(k in n for k in ['id','question','answer','status','evidence'])
 assert n['status'] in ['assumed','supported','partial','gap']
 assert n['evidence']
 if n['status']!='assumed':
  assert all(e['url'] and e['locator'] and e['exact_claim'] for e in n['evidence'])
# Model only the stated arithmetic and schedule, not database behavior.
def serial(first):
 values=[100,100]
 for i in [first,1-first]:
  if sum(values)>=150:values[i]-=150
 return values
concurrent=[100-150,100-150]
assert sum(concurrent)==-100
assert serial(0)==[-50,100] and serial(1)==[100,-50]
assert concurrent!=serial(0) and concurrent!=serial(1)
initial=json.loads((p/'history/initial.json').read_text())
assert initial['revisions']==[json.loads((p/'history/round-0.json').read_text())]
assert len(initial['nodes'])==22 and initial['nodes']!=d['nodes']
checks={'status':'PASS','node_count':len(ids),'edge_count':len(d['edges']),'checks':['Unique node IDs','All edge endpoints exist and have rationale','Acyclic graph','Every prerequisite has a path to target','Required node fields and status values','Evidence URL, locator, exact claim present for all supported nodes','Constructed withdrawal arithmetic and both serial orders','Initial snapshot preserved and distinct from final'],'topological_order':order,'not_checked':['Live database execution','HTML or SVG rendering (shared renderer responsibility)','Formal proof that every pedagogical edge is necessary'],'manual_review':'Read each answer and edge against located passages. Removed invariant-to-atomicity motivation, concurrency-to-serial order, level-to-implementation dependencies, and optional choice branch. Product-specific semantics retain labels; snapshot example explicitly assumes distinct-row updates and no extra enforcement.'}
(p/'checks.json').write_text(json.dumps(checks,indent=2)+'\n')
r={'round':2,'type':'Verification; no further research','gaps_before':[],'searches':[],'evidence':[],'changes':'No node or edge changes. Ran check.py and manual source/edge review. Recorded checks.json.','remaining_gaps':[],'limits':checks['not_checked']}
d['revisions'].append(r)
d['verification']=checks
(p/'history/round-2.json').write_text(json.dumps(r,indent=2)+'\n')
(p/'dag.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps({'status':'PASS','nodes':len(ids),'edges':len(d['edges']),'partial_or_gap_nodes':[n['id'] for n in d['nodes'] if n['status'] in ['partial','gap']]}))
