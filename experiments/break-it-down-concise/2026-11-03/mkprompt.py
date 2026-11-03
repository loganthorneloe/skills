import json,sys
from pathlib import Path
E=Path(__file__).parent
run,variant,topic,mode=sys.argv[1:5]
T=json.loads((E/'inputs/topics.json').read_text())
tpl=(E/f'inputs/{"e2e" if mode=="e2e" else "worker"}-instructions.txt').read_text()
extra="- After the full draft is complete and checked, save it as <RUN_DIR>/draft.html before distilling, so both versions exist." if variant in ('distill','hybrid','hybrid2') else ""
s=tpl.replace('<EXTRA>\n',extra+'\n' if extra else '').replace('<VARIANT_DIR>',str(E/'variants'/variant)).replace('<RESEARCH_DIR>',str(E/'research'/topic)).replace('<RUN_DIR>',str(E/'runs'/run)).replace('<REQUEST>',T[topic])
(E/'runs'/run).mkdir(parents=True,exist_ok=True)
print(s)
