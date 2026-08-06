---
name: skill-refiner
description: 'Load when the user says "create a skill", "refine this skill", "refine all skills", "improve this SKILL.md", or "make this skill more reliable".'
metadata:
  opencode/slash: "true"
---

# Skill refiner

Create or edit the target skill in place. Default to implementation, not a review memo. Preserve the user's intended behavior; improve how reliably an agent reaches it.

## 1. Establish the contract

1. Resolve the target skill and read its `SKILL.md`, applicable repository instructions, linked always-required files, scripts, and tests. For a new skill, resolve its source location and repository tier first.
2. Write a compact internal contract: representative user utterances, required output/action, constraints, and observable completion evidence.
3. Read [references/gotchas.md](references/gotchas.md) completely before editing. List which gotchas apply. Familiarity is not a substitute for reading it.

Criterion: target, intent, invocation type, and proof of completion are unambiguous. Ask only if ambiguity would materially change them.

## 2. Diagnose before adding

Check the current draft against this order:

1. **Routing:** description starts `Load when...` and contains quoted phrases users actually type. It triggers loading; it does not summarize internals.
2. **Cohesion:** one skill teaches one cohesive capability. Separate independently invocable outcomes; keep internal workflow steps in the parent skill.
3. **Workflow:** ordered actions replace reference-dump prose. Each risky step ends in observable evidence.
4. **One default:** prescribe the best normal path. Add alternatives only for materially different constraints.
5. **Progressive disclosure:** keep always-needed rules in `SKILL.md`; move branch-specific or heavy detail into clearly linked files with explicit load conditions.
6. **Consistency:** resolve contradictory instructions, competing defaults, and duplicated sources of truth within the target materials.
7. **Examples:** flag non-obvious commands, arguments, or expected outputs where a concrete example would materially reduce reasoning. Report the opportunity instead of changing the target; add one only after the user explicitly approves that example.
8. **Defensive design:** identify likely shortcuts, place direct rebuttals near them, and make verification a hard exit gate.
9. **Directness:** remove filler, motivational language, obvious reminders, duplication, and empty quality imperatives.
10. **Size:** target about 1,500 tokens maximum. Shorten first; then disclose detail. Do not omit necessary constraints merely to hit the number.

Criterion: every retained instruction changes routing, decisions, actions, or verification; unresolved example opportunities are recorded for the report.

## 3. Design the patch

- Keep one thin `SKILL.md`: trigger, default workflow, decisions needed every run, hard gates.
- Put optional detail under `references/`; portable deterministic operations under `scripts/`.
- Consolidate domain anomalies into one `## Gotchas` section or one gotchas reference. Explicitly require reading it before the affected step.
- Use local links and state exactly when each linked file must load. Never say only “see references.”
- Preserve valid name/path, invocation, compatibility, and release-tier metadata unless the task requires changing them.
- Prefer delete → sharpen → reorder → extract → add, in that order.

Criterion: proposed structure has no competing default paths or duplicated source of truth.

## 4. Edit

Apply the smallest coherent rewrite. For a new skill, scaffold only files the workflow uses. Do not create top-level worker skills for internal steps; use `steps/` or `references/` without additional `SKILL.md` files.

Criterion: all local links resolve and the default workflow can be followed without loading optional material.

## 5. Prove it

Resolve this skill's directory, then run:

```bash
python3 <skill-refiner-dir>/scripts/validate_skill.py <target-skill-dir>
```

Also run:

1. target-provided tests or checks;
2. the harness's native skill validator/discovery check when available;
3. `git diff --check` in a Git worktree;
4. one representative dry-run trace from trigger to exit. If behavior is executable, run it instead of merely tracing it.

Hard exit: validator prints `PASS`, every available target check passes, and the dry run reaches the promised artifact/action. If an external blocker prevents proof, report **blocked**, not complete.

## Anti-rationalization

- **“The old skill already works.”** Then evidence will pass; run it.
- **“There are no tests.”** The validator and representative dry run are still required.
- **“Everything must stay inline.”** Branch-only detail is not always-needed context; extract it and link the load condition.
- **“Several options are more helpful.”** Options transfer unresolved decisions to the agent; prescribe one default.
- **“A warning is close enough.”** Resolve it or report blocked; do not relabel it success.
- **“I know the gotchas.”** Memory drifts; read the canonical file.
- **“The description should explain the skill.”** It is routing context; body explains the skill.

## Report

Return: changed paths, major deletions/extractions, validator and test commands with results, approximate token count, dry-run result, unresolved example opportunities, and any blocker. Keep it brief.
