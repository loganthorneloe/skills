"""Copy reports with neutral labels; preserve bytes and local linked assets."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import json
import shutil

ROOT=Path(__file__).parent
MAPPING={'evals': {'A':'e05','B':'e01'}, 'causal': {'A':'e03','B':'e07'}, 'encryption': {'A':'e06','B':'e02'}, 'isolation': {'A':'e04','B':'e08'}}
class Links(HTMLParser):
    def __init__(self): super().__init__(); self.paths=set()
    def handle_starttag(self,tag,attrs):
        for key,value in attrs:
            if key not in ('href','src') or not value: continue
            part=urlsplit(value)
            if not part.scheme and not part.netloc and part.path:
                self.paths.add(unquote(part.path))

manifest={}
completed=json.loads((ROOT/"completed-runs.json").read_text())
for topic,labels in MAPPING.items():
    target=ROOT/'blind'/topic
    target.mkdir(parents=True,exist_ok=True)
    for label,run in labels.items():
        source=ROOT/'runs'/run
        output=target/label
        output.mkdir(exist_ok=True)
        report=source/'report.html'
        if not report.exists() or run not in completed: continue
        shutil.copy2(report,output/'report.html')
        parser=Links();parser.feed(report.read_text())
        for rel in parser.paths:
            src=(source/rel).resolve()
            if not src.is_relative_to(source.resolve()):
                raise ValueError(f'Outside source folder: {rel}')
            if src.is_file():
                dst=output/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
        shutil.copy2(source/'request.txt',target/'request.txt')
        manifest[f'{topic}/{label}']={'run':run,'sha256':hashlib.sha256(report.read_bytes()).hexdigest()}
(ROOT/'inputs/blind-key.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(f'{len(manifest)} reports copied')
