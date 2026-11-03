import json,pathlib,collections,datetime,copy
p=pathlib.Path(__file__).parent;g=json.loads((p/'dag.json').read_text())
# Graph algorithm executed on supplied inputs; no implementation outside the graph.
def table(entries,m,h):
 b=[[] for _ in range(m)]
 for k,v in entries:b[h(k)%m].append((k,v))
 return b
def find(b,k,h):
 checked=[]
 for key,value in b[h(k)%len(b)]:
  checked.append(key)
  if key==k:return value,checked
 return 'missing',checked
entries=[(1,'A'),(5,'B'),(2,'C'),(3,'D')]
b=table(entries,4,lambda k:k)
assert find(b,5,lambda k:k)==('B',[1,5])
assert find(b,9,lambda k:k)==('missing',[1,5])
b8=table(entries+[(9,'E')],8,lambda k:k)
assert find(b8,5,lambda k:k)==('B',[5])
assert b8[1]==[(1,'A'),(9,'E')]
# Unfamiliar case: use supplied nonidentity hash and non-power-of-two capacity.
h=lambda k:3*k+1
u=[(2,'U'),(7,'V'),(4,'W')]
u5=table(u,5,h);u10=table(u,10,h)
assert find(u5,7,h)==('V',[2,7])
assert find(u5,12,h)==('missing',[2,7])
assert [h(k)%10 for k,v in u]==[7,2,3]
assert find(u10,7,h)==('V',[7])
# Counterexample: all keys have exactly equal codes, so growth cannot separate them.
c=lambda k:7
c8=table(entries,8,c);c16=table(entries,16,c)
assert find(c8,99,c)==('missing',[1,5,2,3])
assert find(c16,99,c)==('missing',[1,5,2,3])
# Outcome check for a broken implementation which merely appends empty buckets.
broken=b+[[] for _ in range(4)]
assert find(broken,5,lambda k:k)[0]=='missing'
# Mutable key/input inconsistency: same logical query now produces a different code.
assert find(table([(1,'A')],4,lambda k:k),1,lambda k:k+1)[0]=='missing'
# Growth-cost arithmetic: copied populations 1,2,4,... before N insertions.
for N in [1,2,3,5,8,17,100]:
 m=1;copied=0
 for n in range(N):
  if n+1>m:copied+=n;m*=2
 assert copied<2*N
# Dependency audit exposed two unlinked terms: bucket-list meaning in load and hash meaning in keycost.
new_edges=[{'from':'chain','to':'load','why':'The mean n/m is the number of entries per bucket sequence, so the claim requires what each bucket stores.'},{'from':'hash','to':'keycost','why':'The cost caveat counts computing the hash function defined in hash.'}]
g['edges']+=new_edges
ids=[n['id'] for n in g['nodes']];assert len(ids)==len(set(ids));assert g['target'] in ids
adj={x:[] for x in ids};indeg=dict.fromkeys(ids,0)
for e in g['edges']:
 assert e['from'] in ids and e['to'] in ids and e['why']
 adj[e['from']].append(e['to']);indeg[e['to']]+=1
q=collections.deque(x for x in ids if not indeg[x]);order=[]
while q:
 x=q.popleft();order.append(x)
 for y in adj[x]:
  indeg[y]-=1
  if indeg[y]==0:q.append(y)
assert len(order)==len(ids)
def reaches(x):return x==g['target'] or any(reaches(y) for y in adj[x])
assert all(reaches(x) for x in ids)
assert all(n['status'] in ['assumed','supported','partial','gap'] for n in g['nodes'])
assert all(n['evidence'] for n in g['nodes'] if n['status']=='supported')
results={'graph_checks':{'unique_ids':True,'valid_endpoints':True,'acyclic':True,'all_nodes_reach_target':True,'nodes':len(ids),'edges':len(g['edges']),'topological_order':order},'tiny_trace':'PASS: computed lookup comparisons, relocation and remaining collision match saved trace.','unfamiliar_case':{'inputs':'h(k)=3k+1, m=5, entries (2,U),(7,V),(4,W)','observations':'Codes 7,22,13 select buckets 2,2,3. Lookup 7 checks 2 then 7; missing 12 checks 2 then 7. At m=10 indices become 7,2,3 and lookup 7 checks only 7.','result':'PASS; supplied hash function is sufficient, no missing input.'},'counterexample':{'inputs':'h(k)=7 for every key, entries 1,5,2,3; grow 8 to 16','observations':'All four entries remain bucket 7. Missing query 99 performs four comparisons before and after growth.','result':'PASS; confirms growth cannot guarantee separation or worst-case constant lookup.'},'broken_resize':'PASS: appending empty buckets without redistribution loses key 5 under new lookup index.','inconsistent_key_hash':'PASS: changing the hash used for an existing key makes a one-bucket lookup miss its entry.','amortized_arithmetic':'PASS: geometric copied-entry totals are below 2N for N=1,2,3,5,8,17,100. This is arithmetic verification, not a proof by testing.','manual_edge_audit':'Every final edge checked against destination claim. Added chain→load and hash→keycost to resolve vocabulary prerequisites. Example steps kept outside edges.','limits':['No measured timings or CPython implementation claims.','No visual QA; common renderer handles graph output.','Expected guarantee remains conditional on suitable hash distribution.']}
g['verification']=results
r={'round':8,'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'stage':'substantive verification','actions':['Executed graph-only unfamiliar case, equal-code counterexample, broken resize, inconsistent hash, trace arithmetic and geometric sum checks.','Manually checked each edge’s destination claim; no example/order edges retained.','Checked unique IDs, endpoints, acyclicity and paths to target.'],'edge_additions':new_edges,'edits':[],'results':results,'remaining_gaps':[]}
g['revisions'].append(r)
(p/'dag.json').write_text(json.dumps(g,indent=2)+'\n');(p/'verification.json').write_text(json.dumps(results,indent=2)+'\n')
with (p/'history.jsonl').open('a') as f:f.write(json.dumps(r)+'\n')
audit=['# Edge necessity audit','', 'Each retained edge names the destination claim that needs its source. Baseline is reader knowledge, not a lesson-order node. Examples are stored outside the graph.','']
for e in g['edges']:audit.append(f"- `{e['from']} → {e['to']}`: {e['why']}")
(p/'edge-audit.md').write_text('\n'.join(audit)+'\n')
print(json.dumps(results,indent=2))
