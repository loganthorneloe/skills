"""Copy reports into anonymized folders. Key saved to inputs/blind-key.json (evaluators must not read it)."""
import json,random,shutil,sys
from pathlib import Path
E=Path(__file__).parent;topic,prefix=sys.argv[1],sys.argv[2]
runs=[d for d in sorted((E/'runs').iterdir()) if d.name.startswith(prefix) and (d/'report.html').exists()]
items=[(d,'report.html') for d in runs]+([] if len(sys.argv)>3 else [(d,'draft.html') for d in runs if (d/'draft.html').exists()])
random.seed(f'{topic}-2026-11-03');random.shuffle(items)
keyf=E/'inputs/blind-key.json';key=json.loads(keyf.read_text()) if keyf.exists() else {}
out=E/'blind'/topic;shutil.rmtree(out,ignore_errors=True)
for i,(d,f) in enumerate(items):
    L=chr(65+i);t=out/L;t.mkdir(parents=True)
    shutil.copy(d/f,t/'report.html')
    if (d/'assets').exists():shutil.copytree(d/'assets',t/'assets')
    key[f'{topic}/{L}']=f'{d.name}/{f}'
keyf.write_text(json.dumps(key,indent=1));print({k:v for k,v in key.items() if k.startswith(topic)})
