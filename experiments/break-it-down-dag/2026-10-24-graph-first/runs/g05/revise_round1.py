import json,copy
from pathlib import Path
p=Path(__file__).parent
g=json.loads((p/'dag.json').read_text()); before=copy.deepcopy(g)
n={x['id']:x for x in g['nodes']}
u='https://developers.openai.com/api/docs/guides/evaluation-best-practices'
def ev(locator,claim):return dict(url=u,locator=locator,exact_claim=claim,basis='Directly read relevant official HTML sections; paraphrase, not quotation')
n['objective']['answer']='Specify the support task and observable success criteria using domain expertise. For order support, criteria can distinguish providing the required order details from providing correct details. Exact criteria depend on the service.'
n['objective']['status']='supported'; n['objective']['evidence'].append(ev('Workflow architectures, lines 1093–1101','Support evaluation distinguishes required response fields from correct field values.'))
n['case']['answer']='A test case records an input and the information needed to judge its output. Support cases may need conversation history and external information, such as order details, as well as the request and expected behavior.'
n['case']['status']='supported';n['case']['evidence'].append(ev('Workflow architectures, lines 1087–1101; Contextual complexity, lines 1202–1213','Order support depends on fetched order details; context and conversation history affect responses.'))
n['target']['evidence']=[ev('Design your eval process, lines 1012–1019','Define the objective, collect data, define measurements, run comparisons, and continuously evaluate.')]
n['target']['synthesis_note']='Workflow is an application of the cited process to the reader’s support task, not a measured result or a universal deployment standard.'
r=dict(round=1,kind='supplemental_research',gaps_before=before['revisions'][0]['gaps'],searches=[],opened=[u,'https://developers.openai.com/api/docs/guides/graders'],navigation=['find customer / Design / variable / Overview','read best-practices lines 1000–1213 and graders lines 957–1086'],findings=['Order-support examples separate response completeness from correct facts.','Conversation history and fetched data belong in relevant support cases.','Grader documentation is explicitly deprecated; conceptual usage only.'],changes=[dict(id=k,before=next(x for x in before['nodes'] if x['id']==k),after=n[k]) for k in ['objective','case','target']],gaps_remaining=['Aggregation calculation and grouped failure interpretation','Controlled comparisons and small-difference uncertainty','Final target synthesis reconciliation'])
g['revisions'].append({k:v for k,v in r.items() if k!='changes'})
(p/'dag.json').write_text(json.dumps(g,indent=2)+'\n');(p/'history/round-01.json').write_text(json.dumps(r,indent=2)+'\n');(p/'history/after-round-01.json').write_text(json.dumps(g,indent=2)+'\n')
print('Round 1 preserved; two partial nodes now supported.')
