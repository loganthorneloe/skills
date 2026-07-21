---
name: skill-diagnose
description: "Build an evidence pack for one skill from trajectories: failures, corrections, retries. Use when debugging a skill, evolve diagnose, or before proposing a patch."
disable-model-invocation: true
metadata:
  internal: true
  opencode/slash: "true"
---

# Skill diagnose

Args: skill name or path (required).

1. Run `skill-sessions`
2. Filter to that skill
3. Cluster failures (early done, bad trigger, ignored section, thrash, user rewrite)
4. Map clusters → [references/failure-levers.md](references/failure-levers.md)
5. Write `.scratch/skill-evolution/YYYY-MM-DD-diagnose-<name>.md`
   - k per cluster, session ids, quotes, suggested lever — **no diff**

k<3 → note only unless user forces. Next: `skill-propose`.
