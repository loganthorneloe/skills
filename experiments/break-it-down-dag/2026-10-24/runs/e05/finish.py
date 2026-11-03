from pathlib import Path
from PIL import Image
from bs4 import BeautifulSoup
import json,html,copy
p=Path(__file__).parent
Image.open(p/'source-page-2-hi.png').crop((400,260,1920,1286)).save(p/'tau-figure-1.png')
Image.open(p/'source-page-7-hi.png').crop((1150,624,1910,1052)).save(p/'tau-figure-4.png')
exec((p/'build_report.py').read_text())
s=BeautifulSoup((p/'report.html').read_text(),'html.parser')
for a in s.select('a[href^="http"]'):
 if 'image-link' not in a.get('class',[]):
  span=s.new_tag('span');span['aria-hidden']='true';span['class']='external';span.string=' ↗';a.append(span)
s.style.string=s.style.string.replace('a[href^="http"]:after{content:" ↗";color:#bf3030;font-size:.8em}', '.external{color:#bf3030;font-size:.8em}')
(p/'report.html').write_text(str(s))
g=json.loads((p/'dag.json').read_text()); ev=g['revisions'][1]['evidence']
answers={'variation':('A fluent response can violate policy or describe an action that never occurred; repeated model executions can differ.',[ev[0],ev[1]]),'goal':('Define observable behavior from the support policy, including eligible, ineligible and missing-information situations.',[ev[1],ev[2]]),'case':('Record inputs and starting conditions separately from expected behavior; supply only task context to the application.',[ev[0],ev[1]]),'grader':('Use exact checks for records and explicit human criteria for prose; calibrate automated judges with human judgments.',[ev[0],ev[1]]),'sample':('A result describes sampled attempts; case mix, variability, sampling uncertainty, and grading error limit generalization.',[ev[0],ev[2],ev[3]]),'compare':('Keep cases and grading fixed while comparing baseline and candidate, inspect regressions and reserve independent checks.',[ev[1],ev[2]]),'workflow':('Define one support job, collect cases, run the application, review judgments, compare a controlled change, then maintain cases from real failures.',[ev[1],ev[2]])}
for n in g['nodes']:
 if n['id'] in answers:n['answer'],n['evidence']=answers[n['id']];n['status']='supported'
g['revisions'].append({'round':2,'gaps':[],'searches':['Read tau PDF figure 1 and figure 4, full §§3,5,6','Read NIST confidence intervals','Read Anthropic grader and zero-to-one sections'],'evidence':[ev[0],ev[3]],'changes':['Explained outcome-versus-authorization distinction in report','Added population assumptions and zero-failure calculation','Selected original setup and reliability figures; rejected current-model rankings as out of scope'],'graph':{'nodes':copy.deepcopy(g['nodes']),'edges':copy.deepcopy(g['edges'])}})
ids=[n['id'] for n in g['nodes']];assert len(ids)==len(set(ids));adj={x:[] for x in ids};ind={x:0 for x in ids}
for e in g['edges']:
 assert e['from'] in ids and e['to'] in ids;adj[e['from']].append(e['to']);ind[e['to']]+=1
order=[];q=[x for x in ids if not ind[x]]
while q:
 x=q.pop(0);order.append(x)
 for v in adj[x]:
  ind[v]-=1
  if not ind[v]:q.append(v)
assert len(order)==len(ids)
def reaches(x):return x==g['target_id'] or any(reaches(v) for v in adj[x])
assert all(reaches(x) for x in ids)
g['verification']={'unique_ids':True,'valid_endpoints':True,'acyclic':True,'all_nodes_reach_target':True,'topological_order':order,'semantic_check':'Each edge reviewed against the prose; source evidence does not by itself prove dependency necessity.'}
(p/'dag.json').write_text(json.dumps(g,indent=2))
y={x:70+i*120 for i,x in enumerate(order)};height=120*len(order)+60
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1050" height="{height}" viewBox="0 0 1050 {height}" role="img" aria-labelledby="title"><title id="title">Prerequisites for evaluating a support assistant</title><defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6" fill="#2f6c9e"/></marker></defs><rect width="100%" height="100%" fill="#f5f4f0"/>']
for i,e in enumerate(g['edges']):
 x=710+i*21;ya=y[e['from']]+30;yb=y[e['to']]+30
 svg.append(f'<path d="M680 {ya} H{x} V{yb} H685" fill="none" stroke="#2f6c9e" stroke-width="1.3" marker-end="url(#arrow)"><title>{html.escape(e["why"])}</title></path>')
for x in order:
 n=next(n for n in g['nodes'] if n['id']==x);svg.append(f'<rect x="25" y="{y[x]}" width="655" height="78" fill="white" stroke="#cbd0d3"/><text x="42" y="{y[x]+25}" font-family="sans-serif" font-size="16">{html.escape(x)} · {n["status"]}</text><text x="42" y="{y[x]+53}" font-family="sans-serif" font-size="14">{html.escape(n["question"])}</text>')
svg.append('</svg>');(p/'dag.svg').write_text(''.join(svg))
(p/'dag.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Evaluation prerequisites</title><body style="font-family:system-ui;background:#f5f4f0;max-width:1080px;margin:auto;padding:20px"><h1>Evaluation prerequisites</h1><p>An arrow A → B means understanding B requires A. The initial graph and research history are preserved in <a href="dag.json">dag.json</a>.</p><object type="image/svg+xml" data="dag.svg" style="width:100%"></object><h2>Why each dependency exists</h2><ul>'+''.join('<li><strong>'+html.escape(e['from']+' → '+e['to'])+'</strong>: '+html.escape(e['why'])+'</li>' for e in g['edges'])+'</ul></body></html>')
print('Graph structural checks PASS; report built')
