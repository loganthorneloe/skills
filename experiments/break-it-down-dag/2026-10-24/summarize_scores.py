"""Unblind frozen scores and summarize; no inferential statistics."""
from pathlib import Path
import json

root=Path(__file__).parent
key=json.loads((root/'inputs/blind-key.json').read_text())
assignments={x['id']:x for x in json.loads((root/'inputs/assignments.json').read_text())}
rows=[]
for topic in ('evals','causal','encryption','isolation'):
    raw=json.loads((root/'evaluation'/f'{topic}-scores.json').read_text())
    row={'topic':topic,'winner':'tie' if raw['winner']=='tie' else assignments[key[f"{topic}/{raw['winner']}"]['run']]['skill'],'rationale':raw['rationale']}
    for label in ('A','B'):
        condition=assignments[key[f'{topic}/{label}']['run']]['skill']
        row[condition]={'label':label,**raw[label],'total':sum(raw[label]['scores'].values())}
    rows.append(row)
dimensions={d:{condition:sum(row[condition]['scores'][d] for row in rows)/len(rows) for condition in ('baseline','variant')} for d in rows[0]['baseline']['scores']}
for values in dimensions.values():values['delta']=values['variant']-values['baseline']
result={'topics':rows,'dimension_means':dimensions,'totals':{c:sum(row[c]['total'] for row in rows) for c in ('baseline','variant')},'note':'Descriptive ordinal scores only; one evaluator, one generation per cell, four topics.'}
(root/'scores-unblinded.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
