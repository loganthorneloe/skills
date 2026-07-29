---
name: evolve-skills
description: 'Load when the user invokes "/evolve-skills", says "evolve skills", "skill health", "skill dojo", or asks to improve skills from agent history.'
disable-model-invocation: true
metadata:
  internal: true
  opencode/slash: "true"
---

# Evolve skills

Use agent trajectories as evidence for skill changes. This is the only entrypoint; linked `steps/` files are internal workflow, not separate skills.

**Default: propose only.** Never edit a real `SKILL.md` until the user explicitly accepts a proposal and requests apply.

## Route

| Intent | Load and run |
|---|---|
| default/full | [steps/default.md](steps/default.md) |
| `health` | [steps/health.md](steps/health.md) |
| `mine` | [steps/mine.md](steps/mine.md) |
| `diagnose <name>` | [steps/diagnose.md](steps/diagnose.md) |
| `propose` | [steps/propose.md](steps/propose.md) |
| `apply <proposal>` | [steps/apply.md](steps/apply.md) |
| sessions only | [steps/sessions.md](steps/sessions.md) |

Before proposal or apply, read [references/skill-quality.md](references/skill-quality.md) completely. Heavy work begins with [steps/sessions.md](steps/sessions.md) unless current-session evidence is already in hand.

## Hard gates

- Default evidence: ≥3 independent sessions per proposed concern; only an explicit user `k=1` overrides it.
- One concern per proposal.
- Owned skills only; vendor/plugin skills require a fork.
- Prefer sharpen, split, or delete over append.
- Store artifacts under `.scratch/skill-evolution/`.
- Apply must pass the quality gate and a representative pressure scenario; failure reverts the patch.

## Gotchas

- Repeated text is not repeated evidence when sessions share one cause.
- “The pattern is obvious” does not waive session IDs and quotations.
- Health and diagnosis produce evidence, not patches.
- Proposal acceptance does not authorize unrelated improvements.

## Report

Return artifact paths, evidence count, mode reached, gate result, and next required user decision.
