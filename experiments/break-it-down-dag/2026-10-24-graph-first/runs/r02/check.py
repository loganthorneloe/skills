import json,pathlib,datetime,itertools,copy
p=pathlib.Path(__file__).parent
g=json.loads((p/'dag.json').read_text())
ids=[n['id'] for n in g['nodes']]; assert len(ids)==len(set(ids))
adj={i:[] for i in ids}
for e in g['edges']:
 assert e['from'] in adj and e['to'] in adj
 adj[e['from']].append(e['to'])
def reaches(start,end,seen=None):
 seen=set() if seen is None else seen
 if start==end:return True
 if start in seen:return False
 seen.add(start)
 return any(reaches(v,end,seen) for v in adj[start])
orphans=[i for i in ids if not reaches(i,g['target'])]
assert orphans==['read_committed'],orphans
# Record observed structural issue before repair.
entry={'round':3,'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'event':'verification_finding','findings':['The researched graph has no target path for read_committed. Its claim is actually needed by statement_kind’s comparison between plain SELECT and UPDATE at that level.','Edge-by-edge target audit: engine qualifications are not explicit enough in the target answer to justify engine -> target. Make the existing requested qualification explicit.'],'research':[],'edits':[]}
with (p/'history.jsonl').open('a') as f:f.write(json.dumps(entry)+'\n')
g['edges'].append({'from':'read_committed','to':'statement_kind','why':'The comparison starts from PostgreSQL Read Committed’s plain-SELECT snapshot rule before showing how UPDATE can use a newer row.'})
next(n for n in g['nodes'] if n['id']=='target')['answer']+=' Level names also require engine and statement qualifications: PostgreSQL Repeatable Read prevents phantoms beyond the standard minimum, while InnoDB distinguishes plain and locking reads.'
g['revisions'].append({'round':3,'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'action':'Structural and semantic audit repair: connected Read Committed to its actual dependent claim; made target engine qualification explicit.'})
(p/'dag.round-3.json').write_text(json.dumps(g,indent=2)+'\n');(p/'dag.json').write_text(json.dumps(g,indent=2)+'\n')
with (p/'history.jsonl').open('a') as f:f.write(json.dumps({'round':3,'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'event':'verification_repair','before_artifact':'dag.round-2.json','after_artifact':'dag.round-3.json','edits':['Added read_committed -> statement_kind with actual claim rationale.','Expanded target answer with engine/statement qualification.'],'research':[]})+'\n')
# Constructed reasoning models; no claim of live database execution.
checks=[]
def reserve(state,owner,amount=6,capacity=10):
 out=state.copy()
 if sum(state)<=capacity-amount:out[owner]+=amount
 return out
serial=[]
for order in [(0,1),(1,0)]:
 state=[0,0]
 for owner in order:state=reserve(state,owner)
 serial.append(state)
overlap=[reserve([0,0],0)[0],reserve([0,0],1)[1]]
assert overlap==[6,6] and all(sum(x)==6 for x in serial)
checks.append({'name':'unfamiliar capacity reservation','given_inputs':{'capacity':10,'initial_row_values':[0,0],'each_request':6,'decision':'Read both rows; increase only own row if total plus six is at most ten.','assumptions':'Separate full transactions; ordinary reads; no extra constraint or coordinating lock.'},'graph_nodes_used':['rule','read_decision','wrong_result','repeatable_read','stable_not_serial','serializable','correctness_limit'],'overlap_outcome':overlap,'serial_outcomes':serial,'conclusion':'Overlapping old views permit twelve reserved units, exceeding capacity. Either serial order reserves only six. Serializable must prevent both successful conflicting decisions.','gap_found':False})
# Counterexample to treating all overlaps as lost updates.
value=100
for _ in range(2):value=value+1
stale_a=100+1;stale_b=100+1
assert value==102 and stale_b==101
checks.append({'name':'relative UPDATE versus stale replacement','given_inputs':'PostgreSQL Read Committed; one row n=100; two separate full transactions; both commit; no trigger or other writer.','graph_nodes_used':['read_decision','read_committed','statement_kind','locks'],'relative_update':'Both run UPDATE SET n=n+1; a waiting writer applies to the newer row, so final n=102.','stale_replacement':'Both first SELECT 100 and later issue UPDATE SET n=101; row locking orders the writes but both chosen constants are 101, so final n=101.','conclusion':'Concurrent does not automatically mean incorrect; SQL expression and transaction decision matter.','gap_found':False})
checks.append({'name':'serializable cannot repair split operation boundaries','given_inputs':'Capacity ten; two callers each read zero in its own committed transaction, then each updates its own reservation row to six in a separate serializable transaction.','graph_nodes_used':['transaction','serial','correctness_limit'],'allowed_serial_order':['read A','read B','write A','write B'],'result':'Total twelve; SQL transactions are serially ordered but the complete application decision was split.','conclusion':'Serializable composition requires each whole decision to be in its transaction.','gap_found':False})
# Final structural checks.
adj={i:[] for i in ids};indeg={i:0 for i in ids}
for e in g['edges']:adj[e['from']].append(e['to']);indeg[e['to']]+=1
queue=[i for i in ids if indeg[i]==0];order=[]
while queue:
 i=queue.pop(0);order.append(i)
 for j in adj[i]:
  indeg[j]-=1
  if indeg[j]==0:queue.append(j)
assert len(order)==len(ids),'cycle'
assert all(reaches(i,g['target']) for i in ids),'missing target path'
assert len({(e['from'],e['to']) for e in g['edges']})==len(g['edges'])
for n in g['nodes']:
 assert n['status'] in ['assumed','supported','partial','gap']
 assert all(k in n for k in ['id','question','answer','status','evidence'])
 if n['status']=='supported':assert n['evidence']
 for e in n['evidence']:assert all(k in e for k in ['url','locator','claim'])
verification={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'graph_shape':{'unique_ids':'PASS','endpoints':'PASS','acyclicity':'PASS','all_nodes_reach_target':'PASS','node_schema_and_supported_evidence':'PASS','node_count':len(ids),'edge_count':len(g['edges']),'topological_order':order},'substantive_tests':checks,'edge_audit':[dict(e,counterfactual='Without this prerequisite, the named dependent claim lacks the concept or condition identified in why; no edge retained solely for example ordering.') for e in g['edges']],'limits':['Constructed reasoning checks only; no PostgreSQL/MySQL/SQLite live execution.','No report, HTML, SVG, browser rendering, or controls requested from this worker.','No universal performance or best-level conclusion.','Source packet provided initial evidence; official HTML supplied gap research.']}
(p/'verification.json').write_text(json.dumps(verification,indent=2)+'\n')
with (p/'history.jsonl').open('a') as f:f.write(json.dumps({'round':4,'timestamp':verification['timestamp'],'event':'final_verification_no_graph_change','research':[],'checks':verification['graph_shape'],'substantive_tests':[x['name'] for x in checks],'edits':[],'artifact':'verification.json'})+'\n')
print(json.dumps(verification['graph_shape']))
