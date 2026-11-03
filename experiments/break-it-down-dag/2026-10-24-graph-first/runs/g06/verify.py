import json,pathlib,math
r=pathlib.Path(__file__).parent
g=json.loads((r/'dag.json').read_text()); ids=[n['id'] for n in g['nodes']]
assert len(ids)==len(set(ids)); assert g['target'] in ids
adj={k:[] for k in ids};degree={k:0 for k in ids}
for e in g['edges']:
 assert e['from'] in adj and e['to'] in adj and e['why']
 adj[e['from']].append(e['to']);degree[e['to']]+=1
queue=[k for k in ids if not degree[k]]; order=[]
while queue:
 k=queue.pop(0);order.append(k)
 for t in adj[k]:
  degree[t]-=1
  if degree[t]==0:queue.append(t)
assert len(order)==len(ids)
def reaches(k):return k==g['target'] or any(reaches(t) for t in adj[k])
assert all(reaches(k) for k in ids)
assert all(n['status'] in ['supported','assumed','gap'] for n in g['nodes'])
assert all(n['evidence'] for n in g['nodes'] if n['status']=='supported')
assert not any(n['status']=='gap' for n in g['nodes'])
initial=json.loads((r/'dag.initial.json').read_text())
assert g['revisions'][0]==initial['revisions'][0]
def forward(t):
 w,b,v1,v2=t;h=max(0,w*2+b);p1=v1*h;p2=v2*h;L=((p1-1)**2+(p2-2)**2)/2
 return {'h':h,'p1':p1,'p2':p2,'loss':L}
t=[1,0,1,0.5];grad=[1,.5,2,-2];f=forward(t);assert f['loss']==1
checks=[]
for i,name in enumerate(['w','b','v1','v2']):
 eps=1e-6;plus=t.copy();minus=t.copy();plus[i]+=eps;minus[i]-=eps
 fd=(forward(plus)['loss']-forward(minus)['loss'])/(2*eps)
 assert abs(fd-grad[i])<1e-8
 checks.append({'parameter':name,'backprop':grad[i],'central_difference':fd,'absolute_error':abs(fd-grad[i]),'epsilon':eps})
new=[a-.1*b for a,b in zip(t,grad)];nf=forward(new)
assert math.isclose(nf['loss'],.3803125,abs_tol=1e-12);assert nf['loss']<f['loss']
report={'status':'PASS','structural_checks':['unique IDs','valid target/endpoints','acyclic','all nodes reach target','supported nodes have evidence','no unresolved gap nodes','initial revision preserved'],'node_count':len(ids),'edge_count':len(g['edges']),'topological_order':order,'trace_forward':f,'trace_backward':checks,'trace_update':{'parameters':new,'forward':nf,'local_predicted_loss_change':-.1*sum(v*v for v in grad),'actual_loss_change':nf['loss']-f['loss']},'not_checked':['Rendering (shared renderer handles this)','Framework autograd','General convergence or teaching effectiveness']}
(r/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
