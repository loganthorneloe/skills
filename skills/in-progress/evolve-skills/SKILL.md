---
name: evolve-skills
description: "Router for skill evolution pack. Use when user says evolve skills, improve skills from history, skill dojo, or is unsure which skill-health/mine/diagnose/propose/apply to run."
disable-model-invocation: true
metadata:
  internal: true
  opencode/slash: "true"
---

# Evolve skills (router)

| Intent | Run |
|--------|-----|
| Ingest / where is history | `skill-sessions` |
| What fails / unused | `skill-health` |
| New skills from habits | `skill-mine` |
| Why this skill fails | `skill-diagnose <name>` |
| Write proposals | `skill-propose` |
| Land accepted proposal | `skill-apply <proposal>` |
| Quality law | `skill-quality` |

## Default "evolve skills"

1. `skill-health`
2. Worst → `skill-diagnose`
3. `skill-propose`
4. Stop. Show paths. Apply only if user asks.

Optional: `skill-mine` in parallel.

Rules: quality=`skill-quality`; evidence via `skill-sessions`; k≥3; propose default.
