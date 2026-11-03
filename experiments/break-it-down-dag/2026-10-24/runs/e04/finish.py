from pathlib import Path
import json,copy,html,time
p=Path(__file__).parent;g=json.loads((p/'dag.json').read_text())
u='https://www.postgresql.org/docs/18/'
def ev(page,loc,claim):return {'URL':u+page,'locator':loc,'claim':claim}
answers={
 'transaction':('A transaction groups database statements into one commit-or-rollback unit; atomicity does not by itself prevent concurrent decision conflicts.',ev('tutorial-transactions.html','§3.4','BEGIN, COMMIT, ROLLBACK and implicit statement transactions')),
 'interleave':('Transactions overlap when their steps interleave. A previously read value can become stale before a dependent write.',ev('transaction-iso.html','§13.2.1','Read Committed gives successive statements different views; updates can use rows changed by concurrent transactions')),
 'snapshot':('A snapshot chooses visible committed row versions. MVCC lets reads use older versions while updates proceed.',ev('mvcc-intro.html','§13.1','MVCC provides snapshot visibility without ordinary reader/writer blocking')),
 'anomalies':('Dirty reads use uncommitted data; nonrepeatable reads change observed values; phantoms change result membership. Lost updates and write skew expose additional decision failures.',ev('transaction-iso.html','§13.2 definitions, Table 13.1','Read anomalies and serialization anomalies are distinct')),
 'levels':('The four levels exclude progressively stronger classes of outcomes, with vendor-specific stronger guarantees possible.',ev('transaction-iso.html','Table 13.1 and following paragraphs','PostgreSQL maps RU to RC and prevents phantoms in RR')),
 'serial':('Serializable requires equivalence to some serial ordering of all successfully committed transactions; concurrent execution is still possible.',ev('sql-set-transaction.html','Description: SERIALIZABLE','Read/write patterns inconsistent with a serial ordering cause a serialization failure')),
 'practice':('Protect the read-to-write dependency using a suitable atomic conditional statement, locking protocol, or Serializable transactions with whole-operation retries.',ev('explicit-locking.html','§13.3.2; §13.3.4','FOR UPDATE locks rows; lock waits can deadlock')),
 'target':('Individually correct operations can make decisions using shared data that another operation changes; isolation limits observations and successful joint outcomes.',ev('transaction-iso.html','§13.2.1–13.2.3','Weaker levels allow outcomes that serializable excludes'))}
for n in g['nodes']:
 if n['id'] in answers:n['answer'],e=answers[n['id']];n['status']='supported';n['evidence']=[e]
g['revisions'].append({'round':1,'gaps':['transaction','interleave','snapshot','anomalies','levels','serial','practice','target'],'searches':['PostgreSQL 18 transaction isolation','PostgreSQL tutorial transactions MVCC introduction'],'evidence':[v[1] for v in answers.values()],'changes':['Added explanatory evidence and identified missing prerequisites: explicit correctness rule, difference between row-write conflict and multirow decision conflict, and complete retries.'],'graph':copy.deepcopy({k:g[k] for k in ['nodes','edges']})})
new=[('rule','What makes an outcome incorrect?','An invariant is a stated rule that must hold; storing legal values is insufficient to preserve every application rule.',ev('ddl-constraints.html','§5.5; §5.5.1 note','Declared constraints enforce particular rules, and CHECK cannot depend on other rows')),
('skew','Why can a stable snapshot still violate a multirow rule?','Two transactions can read the same initial rows and modify different rows; both local decisions pass while their joint result violates the rule.',{'URL':'https://arxiv.org/pdf/1208.4179','locator':'§2.1.1, Figure 1, p.1851','claim':'Two doctors each remove themselves based on the other remaining; snapshot isolation allows both.'}),
('locks','How does locking change concurrent progress?','A conflicting updater waits for a held row lock; locks on selected rows do not automatically protect absent rows or every multirow condition.',ev('explicit-locking.html','§13.3.2–13.3.4','FOR UPDATE prevents concurrent modification until transaction end; conflicts can deadlock')),
('retry','What must happen after a serialization failure?','Start the complete transaction again, including application decisions and values; retrying only the previous UPDATE retains stale reasoning.',ev('mvcc-serialization-failure-handling.html','§13.5','Retry the entire transaction; repeated conflicts may require multiple attempts'))]
for i,q,a,e in new:g['nodes'].append({'id':i,'question':q,'answer':a,'status':'supported','evidence':[e]})
g['edges']=[e for e in g['edges'] if not (e['from']=='levels' and e['to']=='serial')]
for a,b,why in [('transaction','rule','Must define the unit of changes whose correctness is assessed.'),('rule','interleave','Need a rule to distinguish an invalid joint result from merely a different result.'),('snapshot','skew','Stable visibility explains how both transactions retain the initial premise.'),('rule','skew','A multirow invariant defines why the two locally allowed changes are invalid together.'),('skew','serial','The counterexample shows why stable reads are weaker than serial equivalence.'),('levels','serial','Compare named level guarantees before establishing the strongest level.'),('transaction','locks','Lock lifetime follows transaction lifetime.'),('locks','practice','A correct explicit-lock strategy requires understanding conflict scope.'),('serial','retry','Serialization rejection requires a fresh decision.'),('retry','practice','A usable isolation strategy includes transaction restart behavior.')]:g['edges'].append({'from':a,'to':b,'why':why})
g['revisions'].append({'round':2,'gaps':['rule','skew','locks','retry'],'searches':['Serializable Snapshot Isolation in PostgreSQL paper full PDF','PostgreSQL explicit locking','PostgreSQL serialization failure handling','PostgreSQL constraints'],'evidence':[x[3] for x in new],'changes':['Added rule, skew, locks, retry nodes to make implicit prerequisites explicit.','Retained initial graph and first evidence round.','Pruned implementation details (lock compatibility matrix, SSI serialization graphs, benchmark timings) unnecessary for the target.'],'graph':copy.deepcopy({k:g[k] for k in ['nodes','edges']})})
ids=[n['id'] for n in g['nodes']];assert len(ids)==len(set(ids));adj={i:[] for i in ids}
for e in g['edges']:assert e['from'] in ids and e['to'] in ids;adj[e['from']].append(e['to'])
visited=set();active=set();order=[]
def visit(i):
 assert i not in active,'cycle'
 if i in visited:return
 active.add(i)
 for j in adj[i]:visit(j)
 active.remove(i);visited.add(i);order.append(i)
for i in ids:visit(i)
def reaches(i):return i==g['target'] or any(reaches(j) for j in adj[i])
assert all(reaches(i) for i in ids)
g['validation']={'unique_IDs':True,'valid_endpoints':True,'acyclic':True,'all_nodes_reach_target':True,'topological_order':list(reversed(order)),'limitations':'Structural validity does not prove pedagogical necessity; edges manually reviewed against report.'}
(p/'dag.json').write_text(json.dumps(g,indent=2))
# Render a vertical, readable graph with separately listed edge reasons.
order=list(reversed(order));pos={i:(240,55+n*104) for n,i in enumerate(order)};height=104*len(order)+20
s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 {height}" role="img" aria-label="Prerequisite research graph"><defs><marker id="a" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7" fill="#2f6c9e"/></marker></defs><rect width="850" height="{height}" fill="#f5f4f0"/>']
for k,e in enumerate(g['edges']):
 x,y=pos[e['from']];xx,yy=pos[e['to']];r=50+(k%6)*24
 s.append(f'<path d="M{x+350},{y+25} C{650+r},{y+25} {650+r},{yy+25} {xx+350},{yy+25}" fill="none" stroke="#2f6c9e" stroke-width="1.2" marker-end="url(#a)"/>')
for i in order:
 x,y=pos[i];s.append(f'<rect x="{x}" y="{y}" width="350" height="50" fill="white" stroke="#cbd0d3"/><text x="{x+16}" y="{y+31}" font-family="Arial" font-size="19">{html.escape(i)}</text>')
s.append('</svg>');(p/'dag.svg').write_text(''.join(s))
(p/'dag.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>Research dependencies</title><style>body{max-width:950px;margin:40px auto;padding:20px;font:17px/1.6 Arial;background:#f5f4f0;color:#101527}img{width:100%}li{margin-bottom:14px}</style><h1>Prerequisite graph</h1><p>A → B means understanding B requires A. This is an explanation graph, not the database conflict graph.</p><img src="dag.svg" alt="Directed prerequisite graph"><h2>Questions and answers</h2>'+''.join('<h3>'+html.escape(n['question'])+'</h3><p>'+html.escape(n['answer'])+'</p>' for n in g['nodes'])+'<h2>Dependency reasons</h2><ul>'+''.join('<li>'+html.escape(e['from']+' → '+e['to']+': '+e['why'])+'</li>' for e in g['edges'])+'</ul><p>Validation: 13 unique nodes, valid endpoints, acyclic, every node reaches target.</p></html>')
print(json.dumps(g['validation'],indent=2))
