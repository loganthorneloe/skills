---
name: skill-quality
description: "Constitution for authoring/editing agent skills. Use when writing, reviewing, pruning, or evolving any SKILL.md — predictability, invocation, progressive disclosure, prune rules."
metadata:
  internal: true
  opencode/slash: "true"
---

# Skill quality (constitution)

Root virtue: **predictability of process** (same *way* every run), not identical output.

Load only this file unless a term needs the glossary → [GLOSSARY.md](GLOSSARY.md).

## Invocation

| Kind | When | Cost |
|------|------|------|
| **Model-invoked** | Agent must auto-fire or other skills call it | Always-on **description** = context load |
| **User-invoked** | Human types name only (`disable-model-invocation: true`) | Zero context load; human remembers it |

- Description = **triggers** only ("Use when…"). No body restatement.
- Many user-invoked skills → one **router** skill naming them.
- Orchestrators = user-invoked. Reusable disciplines = model-invoked.

## Content ladder (progressive disclosure)

1. **In-skill steps** — ordered actions; each ends on a **checkable** completion criterion
2. **In-skill reference** — short rules needed every run
3. **Linked file** — heavy detail; load only when pointer fires

Inline what every branch needs. Disclose what only some branches need.

## Write rules

- **Single source of truth** — one meaning, one place
- **Leading words** — pretrained hooks (`tracer bullet`, `red`, `seam`) over long restatements
- **Positive steering** — say what to do; avoid pure negation piles
- **Degrees of freedom** — fragile → tight steps/scripts; judgment → heuristics
- **Scripts** when step must be deterministic (parse/sort/check)
- **Portable skill** ≠ project memory — glossary/ADRs/CONTEXT stay in the repo, not global skills

## Prune (every edit)

Delete or sharpen:

| Failure | Cure |
|---------|------|
| **No-op** | Line model already obeys → cut |
| **Duplication** | Same meaning twice → one home |
| **Sediment** | Stale "lessons" layers → remove |
| **Sprawl** | Too long → disclose/split |
| **Premature completion** | Fuzzy done → sharper criterion or split steps |
| **Append-only rot** | New rule without deleting old → forbidden |

Prefer **sharpen / split / delete** over append.

## Gate checklist (pass/fail)

Before shipping any skill or patch:

- [ ] Process predictable without bloating tokens
- [ ] Invocation kind correct; description earns its load
- [ ] Steps have checkable completion criteria
- [ ] Heavy detail behind links, not dumped in SKILL.md
- [ ] No no-ops, dupes, sediment, sprawl
- [ ] Positive steering; no prohibition pile
- [ ] Project-specific stuff not shoved into portable skill
- [ ] SKILL.md stays thin (~≤150–200 lines body ideal)
