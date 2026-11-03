"""Structural checks and observed-write inventory; semantic judgment is separate."""
from pathlib import Path
from collections import defaultdict,deque,Counter
import json,hashlib,sys

ROOT=Path(__file__).parent

def check(p):
    errors=[];g=json.loads(p.read_text());nodes=g.get('nodes',[]);edges=g.get('edges',[]);ids=[n.get('id') for n in nodes];target=g.get('target',g.get('target_id'))
    if isinstance(target,dict):target=target.get('id')
    if not ids or any(not isinstance(i,str) or not i for i in ids):errors.append('Missing/invalid IDs')
    if len(set(ids))!=len(ids):errors.append('Duplicate IDs')
    if target not in ids:errors.append('Target not in graph')
    outgoing=defaultdict(list);parents=defaultdict(list);degree={i:0 for i in ids}
    for e in edges:
        a,b=e.get('from'),e.get('to')
        if a not in degree or b not in degree:errors.append(f'Unresolved endpoint: {a}->{b}');continue
        outgoing[a].append(b);parents[b].append(a);degree[b]+=1
    ready=deque(i for i in degree if degree[i]==0);order=[]
    while ready:
        a=ready.popleft();order.append(a)
        for b in outgoing[a]:
            degree[b]-=1
            if degree[b]==0:ready.append(b)
    if len(order)!=len(set(ids)):errors.append('Cycle')
    ancestors=set();queue=[target] if target in ids else []
    while queue:
        a=queue.pop()
        if a not in ancestors:ancestors.add(a);queue.extend(parents[a])
    events=[];log=ROOT/'observed/events.jsonl'
    if log.exists():events=[e for line in log.read_text().splitlines() if (e:=json.loads(line))['file'].startswith('runs/'+p.parent.name+'/')]
    return {'run':p.parent.name,'structural_status':'PASS' if not errors else 'FAIL','nodes':len(nodes),'edges':len(edges),'target':target,'topological_order':order,'errors':errors,'nodes_without_path_to_target':sorted(set(ids)-ancestors),'support_status_counts':dict(Counter(n.get('status','absent') for n in nodes)),'declared_revision_count':len(g.get('revisions',[])),'observed_graph_writes':len(events),'distinct_observed_snapshots':len(set(e['sha256'] for e in events)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'limit':'Structure and file observations only; not proof of prerequisite correctness, source entailment, or thought chronology.'}

if __name__=='__main__':
    paths=[Path(p) for p in sys.argv[1:]] or sorted((ROOT/'runs').glob('*/dag.json'))
    results=[]
    for p in paths:
        try:results.append(check(p))
        except (ValueError,TypeError,KeyError) as e:results.append({'run':p.parent.name,'structural_status':'FAIL','errors':[str(e)]})
    (ROOT/'structural-checks.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2))
    raise SystemExit(0 if results and all(r['structural_status']=='PASS' for r in results) else 1)
