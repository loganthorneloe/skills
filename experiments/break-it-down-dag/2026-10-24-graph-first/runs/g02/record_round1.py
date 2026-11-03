import json,pathlib
r=pathlib.Path(__file__).parent;p=r/'dag.json';g=json.loads(p.read_text())
loc={'weighted_sum':'lines 76–90','hidden':'lines 91–95','sensitivity':'lines 25–36','add_rule':'lines 37–40','multiply_rule':'lines 25–33','chain':'lines 44–69','label':'lines 37–42','gradient':'lines 45–57'}
for n in g['nodes']:
 if n['id'] in loc:
  n['status']='supported';n['evidence'][0]['locator'] += '; HTML '+loc[n['id']];n['evidence'][0]['basis']='supplied packet plus full relevant HTML passage read'
 if n['id']=='gradient':
  n['answer']='The collection of loss sensitivities, one per adjustable parameter, evaluated at the present values.'
  n['evidence'][0]['exact_claim']=n['answer']
g['revisions'].append({'round':1,'gaps_before':['Full-passage reconciliation','Exact derivative definition','ReLU rules','Local descent limits','Numerical trace'], 'research':[{'action':'opened','url':u,'result':'Readable HTML; opening relevant sections returned'} for u in ['https://cs231n.github.io/optimization-2/','https://developers.google.com/machine-learning/crash-course/neural-networks/nodes-hidden-layers','https://www.3blue1brown.com/lessons/backpropagation/']], 'changes':{'supported_nodes':list(loc),'edited_answers':['gradient: restrict to parameter sensitivities; historical-credit caveat remains in scope'], 'edges':'unchanged'},'gaps_after':['Need later CS231n sections on saving and accumulation','Need later Sanderson sections on example averaging','Need ReLU definition and zero boundary','Need exact update formula and descent reasoning','Need numerical trace']})
p.write_text(json.dumps(g,indent=2)+'\n');(r/'history'/'01-passages.json').write_text(p.read_text())
