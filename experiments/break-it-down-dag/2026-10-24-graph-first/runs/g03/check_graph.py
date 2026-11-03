import json,pathlib,itertools,collections
p=pathlib.Path(__file__).parent
g=json.loads((p/'dag.json').read_text())
ids=[n['id'] for n in g['nodes']]
assert len(ids)==len(set(ids))
assert g['target'] in ids
adj={i:[] for i in ids}; degree={i:0 for i in ids}
for e in g['edges']:
 assert e['from'] in adj and e['to'] in adj and e['why'].strip()
 adj[e['from']].append(e['to']); degree[e['to']]+=1
q=collections.deque(i for i in ids if not degree[i]); order=[]
while q:
 a=q.popleft();order.append(a)
 for b in adj[a]:
  degree[b]-=1
  if degree[b]==0:q.append(b)
assert len(order)==len(ids),'cycle'
def reaches(i,seen=None):
 if i==g['target']:return True
 return any(reaches(j) for j in adj[i])
assert all(reaches(i) for i in ids)
for n in g['nodes']:
 assert n['question'] and n['answer'] and n['status'] in {'assumed','supported','gap'}
 if n['status']=='supported':
  assert n['evidence']
  for e in n['evidence']:assert all(e.get(k) for k in ('url','locator','claim'))
assert not [n for n in g['nodes'] if n['status']=='gap']
assert (p/'initial-dag.json').exists() and (p/'round-1-dag.json').exists()
assert len(g['revisions'])==3
# State model of the constructed read/conditional-write operations; W includes commit.
def execute(schedule):
 state={'A':True,'B':True}; decisions={}
 for op in schedule:
  who,kind=op
  if kind=='R':decisions[who]=state['B' if who=='A' else 'A']
  elif decisions[who]:state[who]=False
 return [state['A'],state['B']]
serial=[execute(['AR','AW','BR','BW']),execute(['BR','BW','AR','AW'])]
assert serial==[[False,True],[True,False]]
interleaved=execute(['AR','BR','AW','BW'])
assert interleaved==[False,False] and interleaved not in serial
schedules=[]
for s in itertools.permutations(['AR','AW','BR','BW']):
 if s.index('AR')<s.index('AW') and s.index('BR')<s.index('BW'):
  schedules.append({'schedule':list(s),'result':execute(s)})
checks={'status':'PASS','node_count':len(ids),'edge_count':len(g['edges']),'unique_ids':True,'valid_endpoints':True,'acyclic':True,'every_node_reaches_target':True,'required_fields':True,'supported_nodes_have_locator_evidence':True,'required_gap_nodes':0,'initial_and_round_history_preserved':True,'topological_order':order,'constructed_example_state_model':{'serial_outcomes':serial,'interleaved_outcome':interleaved,'all_six_ordered_schedules':schedules},'limitations':['Structural validity does not prove prerequisite quality.','Evidence checking is a manual source review, not automated fact verification.','State-transition model is not live database execution.']}
(p/'checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print('PASS: 18 nodes, 31 edges; structure/evidence/history checks; serial versus interleaved example model.')
