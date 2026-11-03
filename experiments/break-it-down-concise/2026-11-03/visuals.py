"""Count visual elements per report (decorative aria-hidden svgs excluded)."""
import re,json,sys
from pathlib import Path
from measure import measure
def v(p):
    s=Path(p).read_text();body=re.sub(r'(?s)<(style|script)\b.*?</\1>','',s)
    svgs=[m for m in re.findall(r'(?s)<svg\b[^>]*>',body) if 'aria-hidden' not in m]
    return dict(img=len(re.findall(r'<img\b',body)),svg=len(svgs),canvas=body.count('<canvas'),controls=len(re.findall(r'<(input|select)\b',body)),tables=body.count('<table'),figures=body.count('<figure'))
E=Path(__file__).parent;rows={}
for d in sorted((E/'runs').glob('t-*')):
    for f in ('draft.html','report.html'):
        if (d/f).exists():rows[f'{d.name}/{f}']=dict(words=measure(d/f)['words'],**v(d/f))
json.dump(rows,open(E/'evaluation/topics-visuals.json','w'),indent=1)
for k,r in rows.items():print(f"{k:32}",r)
