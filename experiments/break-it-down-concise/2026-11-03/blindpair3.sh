#!/bin/zsh
t=$1; E=$PWD; python3 blind3.py $t
find blind/${t}3 -path '*records*' -type f -exec sed -i '' -E 's/[Dd]istill(ed|ing|ation)?/final/g; s/[Dd]raft/earlier version/g' {} +
R=$(python3 -c "import json;print(json.load(open('inputs/topics.json'))['$t'])")
sed -e "s|<BLIND>|$E/blind/${t}3|g" -e "s|<E>|$E|g" -e "s|questions-<TOPIC>|questions-$t|g" -e "s|<TOPIC>|${t}3|g" -e "s|<OUT>|$E/evaluation/judge-${t}3.md|g" inputs/judge-pair-instructions.txt | python3 -c "import sys;print(sys.stdin.read().replace('<REQUEST>',sys.argv[1]))" "$R" > evaluation/prompts/judge-${t}3.txt
for f in $(grep -il "hybrid\|distill\|variant\|baseline" blind/${t}3/*/report.html blind/${t}3/*/records/* 2>/dev/null); do echo "== $f"; grep -oi ".\{40\}\(baseline\|hybrid\|distill\|variant\).\{30\}" $f | head -3; done
