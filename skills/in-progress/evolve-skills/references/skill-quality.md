# Skill quality

Root virtue: **predictable process**, not identical output. Read this file before every proposal or apply. Load [skill-quality-glossary.md](skill-quality-glossary.md) only when one of its terms needs depth.

## Routing

- Description is routing context, not documentation. Start `Load when...` and quote phrases users type.
- Model-invoked disciplines remain discoverable; slash-only orchestrators use the harness's disable-model-invocation field.
- One router owns internal steps; worker files do not get extra `SKILL.md` entrypoints.

## Workflow design

1. Ordered actions; every risky step ends in checkable evidence.
2. One prescribed default; alternatives only for materially different constraints.
3. Always-needed rules inline; branch-only/heavy material behind links with explicit load conditions.
4. Domain anomalies centralized in one gotchas section/reference and required before the affected action.
5. Likely shortcuts get nearby rebuttals; completion requires a concrete test, artifact, or log.

Use scripts for portable deterministic work. Keep project memory in project rules/ADRs, not portable skills.

## Prune before adding

| Failure | Response |
|---|---|
| No-op or generic exhortation | delete |
| Duplicate rule | keep one source of truth |
| Stale sediment | delete or replace |
| Reference dump | convert to workflow; disclose detail |
| Premature completion | add observable criterion |
| Multiple equal paths | choose one default |

Prefer delete → sharpen → reorder → extract → add. Target `SKILL.md` at ~1,500 tokens maximum; required detail may live in linked files.

## Gate — all pass

- [ ] Routing description uses exact user language
- [ ] Invocation type is intentional
- [ ] Default workflow is ordered and checkable
- [ ] References have explicit load conditions
- [ ] Gotchas and shortcut rebuttals are centralized
- [ ] No no-op, duplication, sediment, or unresolved menu
- [ ] Portable; metadata/path valid
- [ ] `SKILL.md` ≤~1,500 tokens
- [ ] Target validator/tests and one representative pressure scenario pass

“The existing skill works” and “there are no tests” do not waive the gate. Failed proof means reject/revert, not success.
