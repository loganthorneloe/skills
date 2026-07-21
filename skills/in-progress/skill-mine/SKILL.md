---
name: skill-mine
description: "Mine repeated multi-step workflows from trajectories that lack a skill; propose new skill candidates. Use when user wants new skills from habits, skill forge, or evolve mine."
disable-model-invocation: true
metadata:
  internal: true
  opencode/slash: "true"
---

# Skill mine

1. Run `skill-sessions`
2. Coarse-step sequences (build, test, commit, review, deploy, …)
3. Repeated n-grams (~3–7 steps), default ≥8 hits across sessions
4. Drop explore-only noise; skip patterns already covered by a skill
5. Write candidates → `.scratch/skill-evolution/YYYY-MM-DD-mine-<slug>.md`
   - name, description draft, steps, evidence session ids
6. Gate outline with `skill-quality`

No `SKILL.md` until user accepts → `skill-apply` or hand-author.
