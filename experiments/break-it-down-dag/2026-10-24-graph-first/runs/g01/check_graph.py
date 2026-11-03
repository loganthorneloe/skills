import json,pathlib,collections
p=pathlib.Path(__file__).parent;g=json.loads((p/'dag.json').read_text())
nodes=g['nodes']; ids=[n['id'] for n in nodes];assert len(ids)==len(set(ids))
assert g['target'] in ids
adj={i:[] for i in ids};indeg={i:0 for i in ids}
for e in g['edges']:
 assert e['from'] in adj and e['to'] in adj and e['why'].strip()
 adj[e['from']].append(e['to']);indeg[e['to']]+=1
assert len(g['edges'])==len({(e['from'],e['to']) for e in g['edges']})
q=collections.deque(i for i in ids if not indeg[i]);order=[]
while q:
 i=q.popleft();order.append(i)
 for j in adj[i]:
  indeg[j]-=1
  if indeg[j]==0:q.append(j)
assert len(order)==len(ids),'cycle'
def reaches(i):return i==g['target'] or any(reaches(j) for j in adj[i])
assert all(reaches(i) for i in ids)
for n in nodes:
 assert all(k in n for k in ('id','question','answer','status','evidence'))
 assert n['status'] in ('assumed','supported','gap')
 if n['status']=='supported':assert n['evidence'],n['id']
 for e in n['evidence']:assert all(e.get(k) for k in ('url','locator','claim'))
initial=json.loads((p/'dag.initial.json').read_text());assert initial==g['revisions'][0]['graph']
r={'result':'PASS','nodes':len(ids),'edges':len(g['edges']),'checks':['Unique IDs','Unique edges','Valid target and edge endpoints','Acyclic graph','Every node reaches target','Node schema and evidence fields','Supported nodes have evidence','Initial snapshot equals preserved revision-zero graph'],'topological_order':order,'limits':'Structural validation cannot prove prerequisite necessity or source entailment. Those were reviewed manually; no application or renderer tested.'}
(p/'checks.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
