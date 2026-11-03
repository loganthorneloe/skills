#!/bin/zsh
# usage: blindpair.sh <topic>  — blinds t-<topic>-base/hyb2 finals with records, writes judge prompt
t=$1; E=$PWD
python3 blind.py $t t-$t- nodrafts >/dev/null
for L in blind/$t/*; do id=$(python3 -c "import json;print(json.load(open('inputs/blind-key.json'))['$t/$(basename $L)'].split('/')[0])"); [ -d runs/$id/records ] && cp -R runs/$id/records $L/records; done
# scrub process words from records
find blind/$t -path '*records*' -type f -exec sed -i '' -E 's/[Dd]istill(ed|ing|ation)?/final/g; s/[Dd]raft/earlier version/g' {} +
R=$(python3 -c "import json;print(json.load(open('inputs/topics.json'))['$t'])")
sed -e "s|<BLIND>|$E/blind/$t|g" -e "s|<E>|$E|g" -e "s|<TOPIC>|$t|g" -e "s|<OUT>|$E/evaluation/judge-$t.md|g" inputs/judge-pair-instructions.txt | python3 -c "import sys;print(sys.stdin.read().replace('<REQUEST>',sys.argv[1]))" "$R" > evaluation/prompts/judge-$t.txt
grep -il "baseline\|hybrid\|distill\|variant" blind/$t/*/report.html blind/$t/*/records/* 2>/dev/null
ls blind/$t
