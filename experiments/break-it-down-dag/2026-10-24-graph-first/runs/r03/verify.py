import json,pathlib,datetime
from fractions import Fraction as F
r=pathlib.Path(__file__).parent; g=json.loads((r/'dag.json').read_text())
ids=[n['id'] for n in g['nodes']]; assert len(ids)==len(set(ids)); assert g['target'] in ids
out={i:[] for i in ids}; indeg={i:0 for i in ids}; pairs=set()
for e in g['edges']:
 assert e['from'] in out and e['to'] in out and e['why'].strip()
 assert (e['from'],e['to']) not in pairs;pairs.add((e['from'],e['to']))
 out[e['from']].append(e['to']);indeg[e['to']]+=1
queue=[i for i in ids if not indeg[i]]; order=[]
while queue:
 i=queue.pop(0);order.append(i)
 for j in out[i]:
  indeg[j]-=1
  if not indeg[j]:queue.append(j)
assert len(order)==len(ids),'Cycle found'
def reach(i):return i==g['target'] or any(reach(j) for j in out[i])
assert all(reach(i) for i in ids),'Node without target path'
for n in g['nodes']:
 assert n['question'] and n['answer'] and n['status'] in ['assumed','supported','partial','gap']
 assert n['evidence'] or n['status'] in ['assumed','gap']
assert not [n for n in g['nodes'] if n['status'] in ['partial','gap']]
def p(prior,spam,legit):
 den=prior*spam+(1-prior)*legit
 return None if den==0 else prior*spam/den
assert 10000*F(1,100)*F(9,10)==90
assert 10000*F(99,100)*F(1,10)==990
assert F(90,1080)==F(1,12)
for prior,expected in [(F(1,1000),F(1,112)),(F(1,100),F(1,12)),(F(1,10),F(1,2)),(F(1,2),F(9,10)),(F(0),F(0)),(F(1),F(1))]:
 assert p(prior,F(9,10),F(1,10))==expected
assert p(F(1,5),F(2,5)*(1-F(3,4)),F(1,10)*(1-F(1,5)))==F(5,21)
assert p(F(1,100),F(1,2),F(1,10))==F(5,104)
assert p(F(1,100),F(1,2)**2,F(1,10)**2)==F(25,124)
assert p(F(1,100),F(1,5),F(1,5))==F(1,100)
assert p(F(1,100),F(9,10),F(0))==1
assert p(F(1,100),F(0),F(0)) is None
result={'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','nodes':len(ids),'edges':len(pairs),'structural_checks':['unique IDs','valid endpoints','unique directed edges','acyclic','all nodes reach target','supported nodes carry evidence locators'],'topological_order':order,'arithmetic_checks':['90 true flags and 990 false flags per 10,000','posterior 1/12','six base-rate cases including endpoints','independent present/absent word pattern gives 5/21','duplicated-word counterexample gives 5/104 actual vs 25/124 naive','equal clue rates preserve prior','zero false-positive rate gives certainty under positive prior and detection','zero evidence denominator undefined'],'semantic_checks':{'method':'Manual, not automated; recorded separately in graph edge_audit and worked_cases.','performed':['Reviewed every retained edge against destination claim','Separated rate estimation from application of given inputs','Replaced example-order dependency with generic multiplication and partition prerequisites','Split raw scores from normalized probability','Replayed unfamiliar absent-word case and dependent-word counterexample after repair'],'limits':'No independent human review or empirical model validation.'}}
(r/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
with (r/'history.jsonl').open('a') as f:f.write(json.dumps({'time':result['time'],'round':'verification-1','action':'Ran verify.py and final manual prerequisite review','result':'PASS','artifact':'verification.json','graph_edits':'none; repaired graph retained'})+'\n')
print(json.dumps(result,indent=2))
