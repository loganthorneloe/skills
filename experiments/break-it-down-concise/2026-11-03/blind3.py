"""Blind exactly two runs (baseline + hyb3) for topic t as blind/<t>3/{A,B}."""
import json,random,shutil,sys
from pathlib import Path
E=Path(__file__).parent;t=sys.argv[1];T=f'{t}3'
runs=[E/'runs'/f't-{t}-base',E/'runs'/f't-{t}-hyb3']
random.seed(f'{T}-2026-11-03');random.shuffle(runs)
keyf=E/'inputs/blind-key.json';key=json.loads(keyf.read_text())
out=E/'blind'/T;shutil.rmtree(out,ignore_errors=True)
for i,d in enumerate(runs):
    L=chr(65+i);o=out/L;o.mkdir(parents=True);shutil.copy(d/'report.html',o/'report.html')
    for s in ('assets','records'):
        if (d/s).exists():shutil.copytree(d/s,o/s)
    key[f'{T}/{L}']=f'{d.name}/report.html'
keyf.write_text(json.dumps(key,indent=1))
