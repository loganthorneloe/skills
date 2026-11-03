"""Descriptive size metrics for each report (not quality scores)."""
from html.parser import HTMLParser
from pathlib import Path
import json,re,sys
W=re.compile(r"\b[\w'-]+\b")
class P(HTMLParser):
    def __init__(s):
        super().__init__();s.skip=0;s.sec='(title)';s.secs={};s.inh=False;s.h='';s.imgs=0;s.tables=0;s.fig=0;s.capw=0;s.incap=0
    def handle_starttag(s,t,a):
        if t in('style','script','head','noscript'):s.skip+=1
        if t=='h2':s.inh=True;s.h=''
        if t=='img':s.imgs+=1
        if t=='table':s.tables+=1
        if t=='figure':s.fig+=1
        if t=='figcaption':s.incap+=1
    def handle_endtag(s,t):
        if t in('style','script','head','noscript'):s.skip-=1
        if t=='h2':s.inh=False;s.sec=' '.join(s.h.split())[:50]
        if t=='figcaption':s.incap-=1
    def handle_data(s,d):
        if s.skip:return
        n=len(W.findall(d))
        if s.inh:s.h+=d
        s.secs[s.sec]=s.secs.get(s.sec,0)+n
        if s.incap:s.capw+=n
def measure(p):
    x=P();x.feed(Path(p).read_text())
    tot=sum(x.secs.values())
    audit=sum(v for k,v in x.secs.items() if re.search(r'source|audit|evidence behind',k,re.I) and not re.search(r'notice|reuse',k,re.I))
    return dict(words=tot,minutes=round(tot/230,1),audit_words=audit,caption_words=x.capw,images=x.imgs,tables=x.tables,figures=x.fig,sections=x.secs)
if __name__=='__main__':
    E=Path(__file__).parent;rows={}
    for d in sorted((E/'runs').iterdir()):
        for f in ('report.html','draft.html'):
            if (d/f).exists():rows[f'{d.name}/{f}']=measure(d/f)
    (E/'evaluation/metrics.json').write_text(json.dumps(rows,indent=1))
    for k,v in rows.items():print(f"{k:28} {v['words']:5} words {v['minutes']:4} min audit {v['audit_words']:4} img {v['images']} tbl {v['tables']}")
