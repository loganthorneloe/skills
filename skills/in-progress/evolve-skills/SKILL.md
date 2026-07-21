---
name: evolve-skills
description: "Mine agent trajectories and improve skills: health, mine new skills, diagnose, propose gated patches, apply after approval. Use when user says evolve skills, skill health, improve skills from history, or skill dojo."
disable-model-invocation: true
metadata:
  internal: true
  opencode/slash: "true"
---

# Evolve skills

**You only enter here.** Steps below are files in this skill — load with `read`, do not expect separate slash skills.

Quality law: read [references/skill-quality.md](references/skill-quality.md) before any proposal/apply. Do not restate it.

**Default: propose only.** Edit real SKILL.md only in the apply step after explicit user OK.

## Modes

| Arg / intent | Load and run |
|--------------|----------------|
| (default) / full | [steps/default.md](steps/default.md) |
| `health` | [steps/health.md](steps/health.md) |
| `mine` | [steps/mine.md](steps/mine.md) |
| `diagnose [name]` | [steps/diagnose.md](steps/diagnose.md) |
| `propose` | [steps/propose.md](steps/propose.md) |
| `apply [proposal]` | [steps/apply.md](steps/apply.md) |
| sessions only | [steps/sessions.md](steps/sessions.md) |

Shared: always start heavy work with [steps/sessions.md](steps/sessions.md) ingest unless evidence already in-hand.

## Hard limits

- k≥3 sessions per change (unless user sets `k=1`)
- One concern per proposal
- No vendor/plugin in-place edits
- Prefer sharpen/split/delete over append
- Artifacts → `.scratch/skill-evolution/`
