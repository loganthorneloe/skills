import json,pathlib,collections
r=pathlib.Path(__file__).parent;g=json.loads((r/'dag.json').read_text());ids=[n['id'] for n in g['nodes']];assert len(ids)==len(set(ids));assert g['target'] in ids
adj={i:[] for i in ids};ind={i:0 for i in ids}
for e in g['edges']:
 assert e['from'] in ids and e['to'] in ids and e['why'];adj[e['from']].append(e['to']);ind[e['to']]+=1
q=collections.deque(i for i in ids if ind[i]==0);order=[]
while q:
 i=q.popleft();order.append(i)
 for j in adj[i]:
  ind[j]-=1
  if ind[j]==0:q.append(j)
assert len(order)==len(ids)
def reaches(i):return i==g['target'] or any(reaches(j) for j in adj[i])
assert all(reaches(i) for i in ids)
for n in g['nodes']:
 assert n['status'] in ['assumed','supported','partial','gap']
 assert all(k in n for k in ['id','question','answer','status','evidence'])
 if n['status']=='supported':assert n['evidence'] and all(all(e.get(k) for k in ['url','locator','exact_claim']) for e in n['evidence'])
initial=json.loads((r/'history'/'00-initial.json').read_text());assert len(initial['revisions'])==1 and len(g['revisions'])==5
result={'pass':True,'nodes':len(ids),'edges':len(g['edges']),'unique_ids':True,'endpoints':True,'acyclic':True,'all_nodes_reach_target':True,'supported_nodes_have_evidence':True,'topological_order':order,'status_counts':dict(collections.Counter(n['status'] for n in g['nodes'])),'history_snapshots':5,'limits':'Structural validity does not prove prerequisite quality; edge necessity manually audited in round 4.'}
(r/'graph-checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
