---
name: skill-health
description: "Score installed skills from recent trajectories: uses, retries, corrections, unused, trends. Use when user asks skill health, which skills fail, or evolve health."
disable-model-invocation: true
metadata:
  internal: true
  opencode/slash: "true"
---

# Skill health

1. Run `skill-sessions`
2. Per skill: uses, success-ish rate, retries, corrections, last used
3. Flag: high_failure, excessive_retries, frequent_corrections, unused
4. Tight table + top issues

No patches. Fixes → `skill-diagnose` / `skill-propose`.
