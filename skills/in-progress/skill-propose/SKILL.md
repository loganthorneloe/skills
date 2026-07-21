---
name: skill-propose
description: "Turn trajectory evidence into skill patch or new-skill proposals; gate with skill-quality. Use when evolve propose, or after skill-diagnose / skill-mine / skill-health."
disable-model-invocation: true
metadata:
  internal: true
  opencode/slash: "true"
---

# Skill propose

**Propose only — never edit SKILL.md.**

1. Evidence from `skill-diagnose` / `skill-mine` / `.scratch/skill-evolution/*` — else run those first
2. k≥3 sessions per change (unless user `k=1`)
3. Project-only lesson → CONTEXT.md/ADR/rules, not portable skill
4. Lever: [references/failure-levers.md](references/failure-levers.md)
5. Draft patch — prefer sharpen/split/delete over append
6. Must pass `skill-quality` gate — fail = no file
7. Write `.scratch/skill-evolution/YYYY-MM-DD-propose-<slug>.md` per [references/proposal-format.md](references/proposal-format.md)
8. Reject: sediment, sprawl, no-ops, append-only lessons, vendor in-place edits

One concern per file. Accept → `skill-apply`.
