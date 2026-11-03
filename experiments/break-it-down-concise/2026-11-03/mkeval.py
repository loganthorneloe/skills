import json,sys
from pathlib import Path
E=Path(__file__).parent;topic=sys.argv[1];T=json.loads((E/'inputs/topics.json').read_text())[topic]
key=json.loads((E/'inputs/blind-key.json').read_text())
letters=sorted(L.split('/')[1] for L in key if L.startswith(topic+'/'))
finals=[L for L in letters if 'draft' not in key[f'{topic}/{L}']]
g=(E/'inputs/grader-instructions.txt').read_text()
for L in letters:
    s=g.replace('<REPORT>',str(E/f'blind/{topic}/{L}/report.html')).replace('<QUESTIONS>',str(E/f'inputs/questions-{topic}.md')).replace('<REQUEST>',T).replace('<OUT>',str(E/f'evaluation/coverage/{topic}-{L}.md'))
    (E/f'evaluation/prompts/grade-{topic}-{L}.txt').write_text(s)
j=(E/'inputs/judge-instructions.txt').read_text().replace('<BLIND_DIR>',str(E/f'blind/{topic}')).replace('<LETTERS>','{'+','.join(finals)+'}').replace('<RESEARCH_DIR>',str(E/f'research/{topic}')).replace('<RUBRIC>',str(E/'inputs/prior-report-rubric.txt')).replace('<QUESTIONS>',str(E/f'inputs/questions-{topic}.md')).replace('<REQUEST>',T).replace('<OUT>',str(E/f'evaluation/judge-{topic}.md'))
(E/f'evaluation/prompts/judge-{topic}.txt').write_text(j);print(letters,finals)
