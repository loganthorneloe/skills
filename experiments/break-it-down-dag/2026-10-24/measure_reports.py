"""Descriptive output size metrics; these are not quality scores."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import json
import re

class ReadingText(HTMLParser):
    def __init__(self):
        super().__init__();self.skip=0;self.parts=[];self.links=set();self.images=0
    def handle_starttag(self,tag,attrs):
        if tag in ('style','script','head'):self.skip+=1
        if tag=='img':self.images+=1
        if tag=='a':
            href=dict(attrs).get('href','');parsed=urlsplit(href)
            if parsed.scheme in ('http','https'):self.links.add(parsed._replace(fragment='').geturl())
    def handle_endtag(self,tag):
        if tag in ('style','script','head'):self.skip-=1
    def handle_data(self,data):
        if not self.skip:self.parts.append(data)

root=Path(__file__).parent
rows=[]
for job in json.loads((root/'inputs/assignments.json').read_text()):
    directory=root/'runs'/job['id'];p=directory/'report.html'
    if not p.exists():continue
    parser=ReadingText();parser.feed(p.read_text())
    row={**job,'reading_words':len(re.findall(r"\b[\w'-]+\b",' '.join(parser.parts))),'report_bytes':p.stat().st_size,'distinct_external_link_destinations':len(parser.links),'image_elements':parser.images}
    graph=directory/'dag.json'
    if graph.exists():
        g=json.loads(graph.read_text());row.update(graph_nodes=len(g.get('nodes',[])),graph_edges=len(g.get('edges',[])),graph_revision_entries=len(g.get('revisions',[])))
    rows.append(row)
(root/'output-metrics.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps(rows,indent=2))
