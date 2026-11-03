"""Shared, offline, fixed-font DAG renderer for both experimental arms."""
from pathlib import Path
from collections import defaultdict,deque
from urllib.parse import urlsplit
import html,json,textwrap,sys


def esc(v):return html.escape(str(v))
def detail(v):
    if isinstance(v,list):return '<ul>'+''.join('<li>'+detail(x)+'</li>' for x in v)+'</ul>'
    if isinstance(v,dict):return '<dl>'+''.join('<dt>'+esc(k)+'</dt><dd>'+detail(x)+'</dd>' for k,x in v.items())+'</dl>'
    if isinstance(v,str) and urlsplit(v).scheme in ('https','http'):
        return '<a href="'+esc(v)+'">'+esc(v)+'</a>'
    return esc(v)

def render(source):
    g=json.loads(source.read_text());nodes=g['nodes'];edges=g['edges'];ids=[n['id'] for n in nodes];lookup={n['id']:n for n in nodes}
    outgoing=defaultdict(list);parents=defaultdict(list);degree={i:0 for i in ids};level={i:0 for i in ids}
    for e in edges:
        a,b=e['from'],e['to']
        if a not in degree or b not in degree:raise ValueError('Unknown endpoint')
        outgoing[a].append(b);parents[b].append(a);degree[b]+=1
    ready=deque(i for i in ids if degree[i]==0);order=[]
    while ready:
        a=ready.popleft();order.append(a)
        for b in outgoing[a]:
            level[b]=max(level[b],level[a]+1);degree[b]-=1
            if degree[b]==0:ready.append(b)
    if len(order)!=len(ids):raise ValueError('Cycle or duplicate IDs')
    layers=defaultdict(list)
    for i in order:layers[level[i]].append(i)
    positions={};maxrow=max(map(len,layers.values()),default=1)
    for depth,row in sorted(layers.items()):
        row.sort(key=lambda i:sum(positions[p][0] for p in parents[i])/len(parents[i]) if parents[i] else ids.index(i)*310)
        for col,i in enumerate(row):positions[i]=(24+col*310,30+depth*190)
    long=[e for e in edges if level[e['to']]-level[e['from']]>1]
    width=max(650,maxrow*310+80+len(long)*12);height=max(250,(max(level.values(),default=0)+1)*190)
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" role="img" aria-label="Prerequisite graph; arrows point to the dependent concept"><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8Z" fill="#646c77"/></marker></defs>']
    lane=0
    for number,e in enumerate(edges,1):
        a,b=e['from'],e['to'];x,y=positions[a];xx,yy=positions[b];x+=135;xx+=135;y+=135
        if level[b]-level[a]>1:
            rail=maxrow*310+28+lane*12;lane+=1
            path=f'M{x},{y} L{x},{y+20} L{rail},{y+20} L{rail},{yy-16} L{xx},{yy-16} L{xx},{yy}'
        else:path=f'M{x},{y} C{x},{y+27} {xx},{yy-27} {xx},{yy}'
        svg.append(f'<a href="#edge-{number}"><path d="{path}" fill="none" stroke="#646c77" stroke-width="1.3" marker-end="url(#arrow)"/><title>{esc(a)} → {esc(b)}: {esc(e.get("why",""))}</title></a>')
    colors={'supported':'#46734d','assumed':'#646c77','partial':'#8a5b00','gap':'#bf3030'}
    for n in nodes:
        i=n['id'];x,y=positions[i];lines=textwrap.wrap(n['question'],width=31)[:4];status=n.get('status','unknown')
        svg.append(f'<a href="#node-{esc(i)}"><rect x="{x}" y="{y}" width="270" height="135" fill="white" stroke="#cbd0d3"/><text x="{x+12}" y="{y+21}" fill="{colors.get(status,"#646c77")}" font-size="12">{esc(i)} · {esc(status)}</text>')
        for j,line in enumerate(lines):svg.append(f'<text x="{x+12}" y="{y+47+j*20}" font-size="15" fill="#101527">{esc(line)}</text>')
        svg.append('</a>')
    svg.append('</svg>');svg=''.join(svg)
    text=['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Prerequisite graph</title><style>*{box-sizing:border-box}body{margin:0;background:#f5f4f0;color:#101527;font:16px/1.65 system-ui,sans-serif}main{max-width:1200px;margin:auto;padding:28px 22px}h1{letter-spacing:-.03em;line-height:1.15}h2{margin-top:36px}h3{font-size:1.2rem}a{color:#2f6c9e;overflow-wrap:anywhere}a:hover{color:#bf3030}:focus-visible{outline:3px solid #bf3030;outline-offset:3px}.graph{overflow:auto;border:1px solid #cbd0d3;max-height:700px;background:#fafafa}.graph svg{display:block;font-family:system-ui,sans-serif;flex-shrink:0}article{border-top:1px solid #cbd0d3;padding:12px 0}dt{font-weight:600}dd{margin:0 0 12px;overflow-wrap:anywhere}code{font-size:.9em}ul{padding-left:24px}li{margin:8px 0}.status{font-weight:600}p{max-width:850px}@media(max-width:600px){main{padding:24px 20px}.graph{max-height:500px}}</style></head><body><main><h1>Prerequisite graph</h1><p>Arrows point from a prerequisite to the concept that needs it. Scroll horizontally and vertically to inspect the diagram; labels retain their size on narrow screens. Select a node for its full answer below.</p><p><a href="dag.json">Raw graph and history</a> · <a href="#nodes">Node answers and evidence</a> · <a href="#edges">Dependency reasons</a></p><div class="graph" tabindex="0" role="region" aria-label="Scrollable prerequisite diagram">',svg,'</div><h2>Reader and scope</h2>']
    for k in ['reader_assumptions','assumptions','reader','target','target_id','scope','scope_notes','optional','optional_material','non_prerequisites','unresolved_gaps']:
        if k in g:text.append('<h3>'+esc(k.replace('_',' ').capitalize())+'</h3>'+detail(g[k]))
    text.append('<h2 id="nodes">Node answers and evidence</h2>')
    for n in nodes:
        text.append(f'<article id="node-{esc(n["id"])}"><h3>{esc(n["id"])} — {esc(n["question"])}</h3><p class="status">{esc(n.get("status"))}</p><p>{esc(n.get("answer",""))}</p>')
        for k,v in n.items():
            if k not in ('id','question','answer','status'):text.append('<h4>'+esc(k.replace('_',' ').capitalize())+'</h4>'+detail(v))
        text.append('</article>')
    text.append('<h2 id="edges">Dependency reasons</h2>')
    for j,e in enumerate(edges,1):text.append(f'<article id="edge-{j}"><h3>{esc(e["from"])} → {esc(e["to"])}</h3>'+detail({k:v for k,v in e.items() if k not in ('from','to')})+'</article>')
    text.append('</main></body></html>');source.with_name('dag.html').write_text(''.join(text));source.with_name('dag.svg').write_text(svg)
    return {'file':str(source),'nodes':len(nodes),'edges':len(edges),'topological_order':order,'min_diagram_label_px':15}

if __name__=='__main__':
    for name in sys.argv[1:]:print(json.dumps(render(Path(name))))
