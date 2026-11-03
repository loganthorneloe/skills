"""Freeze anonymized graph packages. Never changes generated raw artifacts."""
from pathlib import Path
import json,hashlib,shutil,sys,re
ROOT=Path(__file__).parent
LABELS={'g01':'evals-B','g05':'evals-A','g03':'isolation-A','g07':'isolation-B','g06':'backpropagation-A','g02':'backpropagation-B','g04':'bayesian_spam-A','g08':'bayesian_spam-B'}
assignments={a['run']:a for a in json.loads((ROOT/'inputs/assignments.json').read_text())}
for run in sys.argv[1:]:
 src=ROOT/'runs'/run; label=LABELS[run]; dest=ROOT/'blind'/label
 if dest.exists():raise SystemExit(f'Already frozen: {label}')
 if not (src/'run-notes.md').exists():raise SystemExit(f'Not completed: {run}')
 dest.mkdir(parents=True)
 # Exclude construction scripts; preserve raw data and contemporaneous history.
 files=[p for p in src.rglob('*') if p.is_file() and p.suffix in ('.json','.jsonl','.md','.txt','.html','.svg')]
 manifest=[]
 for p in files:
  rel=p.relative_to(src);out=dest/rel;out.parent.mkdir(parents=True,exist_ok=True)
  raw=p.read_bytes();s=raw.decode()
  # Condition-neutral path aliases only; substantive graph content is unchanged.
  s=s.replace(str(src.resolve()),label).replace(str(src),label).replace('runs/'+run,label).replace('/'+run+'/', '/'+label+'/')
  s=re.sub(r'\b'+run+r'\b',label,s).replace('old-skill','assigned-skill').replace('new-skill','assigned-skill').replace('old skill','assigned skill').replace('new skill','assigned skill')
  out.write_text(s)
  manifest.append({'file':str(rel),'original_sha256':hashlib.sha256(raw).hexdigest(),'blind_sha256':hashlib.sha256(out.read_bytes()).hexdigest()})
 shutil.copyfile(ROOT/'inputs/sources'/assignments[run]['source_packet'],dest/'source-packet.json')
 events=[]
 for line in (ROOT/'observed/events.jsonl').read_text().splitlines():
  e=json.loads(line)
  if not e['file'].startswith('runs/'+run+'/'):continue
  original=ROOT/e['snapshot']; target=dest/'observed'/original.name;target.parent.mkdir(exist_ok=True)
  shutil.copyfile(original,target)
  events.append({**e,'file':e['file'].replace('runs/'+run,label),'snapshot':'observed/'+original.name})
 (dest/'observed-events.json').write_text(json.dumps(events,indent=2)+'\n')
 (dest/'artifact-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 print(label)
