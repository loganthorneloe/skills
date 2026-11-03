"""Observe valid graph writes without changing workers' files."""
import hashlib,json,time
from pathlib import Path
from datetime import datetime,timezone
root=Path(__file__).parent
out=root/'observed';out.mkdir(exist_ok=True)
seen={}
while not (root/'STOP_WATCHING').exists():
    for p in sorted((root/'runs').glob('*/dag*.json')):
        try:
            raw=p.read_bytes();g=json.loads(raw)
            if not isinstance(g,dict) or not g.get('nodes'):continue
        except (OSError,ValueError):continue
        key=str(p.relative_to(root));sha=hashlib.sha256(raw).hexdigest()
        if seen.get(key)==sha:continue
        seen[key]=sha;run=p.parent.name;d=out/run;d.mkdir(exist_ok=True)
        snapshot=d/f'{p.stem}-{sha[:12]}.json'
        if not snapshot.exists():snapshot.write_bytes(raw)
        with (out/'events.jsonl').open('a') as f:
            f.write(json.dumps({'time':datetime.now(timezone.utc).isoformat(),'file':key,'sha256':sha,'snapshot':str(snapshot.relative_to(root)),'nodes':len(g['nodes']),'edges':len(g.get('edges',[]))})+'\n')
    time.sleep(2)
