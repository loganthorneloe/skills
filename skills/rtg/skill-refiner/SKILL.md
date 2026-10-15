---
name: skill-refiner
description: Creates and refines agent skills for reliable discovery and execution. Use when creating a skill, improving a SKILL.md, or refining existing skills.
metadata:
  opencode/slash: "true"
---

# Skill refiner

Create or edit the target skill in place. Default to implementation, not a review memo. Preserve the user's intended behavior; improve how reliably an agent reaches it.

## 1. Establish the contract

1. Resolve the target skill and read its `SKILL.md`, applicable repository instructions, linked always-required files, scripts, and tests. For a new skill, resolve its source location and repository tier first.
2. Write a compact internal contract: representative user utterances, required output/action, constraints, and observable completion evidence.
3. Read [references/gotchas.md](references/gotchas.md) completely before editing. List which gotchas apply. Familiarity is not a substitute for reading it.
4. Identify observed failures before adding instructions. For substantial behavior changes, consider defining three representative requests and expected results before drafting, then comparing outcomes with and without the skill. These behavioral evaluations are recommended, not a mandatory suite for every skill; the checks in step 5 remain required.

Criterion: target, intent, invocation type, and proof of completion are unambiguous. Ask only if ambiguity would materially change them.

## 2. Diagnose before adding

Check the current draft against this order:

1. **Routing:** description states what the skill does and when to use it, in third person, with specific task terms and contexts. Keep implementation details in the body. No required opening phrase or quoted triggers.
2. **Cohesion:** one skill teaches one cohesive capability. Separate independently invocable outcomes; keep internal workflow steps in the parent skill.
3. **Workflow:** ordered actions replace reference-dump prose. Match specificity to fragility: allow judgment for open-ended work; prescribe exact sequences for error-prone operations. Each risky step ends in observable evidence.
4. **One default:** prescribe the best normal path. Add alternatives only for materially different constraints.
5. **Progressive disclosure:** keep always-needed rules in `SKILL.md`; move branch-specific or heavy detail into clearly linked files with explicit load conditions.
6. **Consistency:** resolve contradictory instructions, competing defaults, and duplicated sources of truth within the target materials.
7. **Examples:** add a concrete command or input/output pair only when it clarifies a non-obvious decision or expected result. Derive it from the task contract or verified behavior; keep it consistent with the rules. Omit examples that add no value or require inventing requirements.
8. **Defensive design:** identify likely shortcuts, place direct rebuttals near them, and make verification a hard exit gate.
9. **Directness:** remove filler, motivational language, obvious reminders, duplication, and empty quality imperatives.
10. **Size:** keep `SKILL.md` within the local 2,000-token default budget; this is a ceiling, not a target. Shorten first; then disclose detail. Do not omit necessary constraints merely to hit the number.

Criterion: every retained instruction changes routing, decisions, actions, or verification.

## 3. Design the patch

- Keep one thin `SKILL.md`: trigger, default workflow, decisions needed every run, hard gates.
- Put optional detail under `references/`; portable deterministic operations under `scripts/`.
- Consolidate domain anomalies into one `## Gotchas` section or one gotchas reference. Explicitly require reading it before the affected step.
- Link reference files directly from `SKILL.md` and state when each must load. Avoid chains of references. Add a contents list to references longer than 100 lines.
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

Fix failures and rerun affected checks. Structural `PASS` does not prove behavioral quality: manually review description relevance and observe whether the dry run loads the right references and follows the intended workflow. When broader evaluations are useful, check appropriate activation, output correctness, and known failure cases; compare against the baseline and test intended models when available. Report any untested coverage without making optional evaluations a completion gate.

## Anti-rationalization

- **“The old skill already works.”** Then evidence will pass; run it.
- **“There are no tests.”** The validator and representative dry run are still required.
- **“Everything must stay inline.”** Branch-only detail is not always-needed context; extract it and link the load condition.
- **“Several options are more helpful.”** Options transfer unresolved decisions to the agent; prescribe one default.
- **“A warning is close enough.”** Resolve it or report blocked; do not relabel it success.
- **“I know the gotchas.”** Memory drifts; read the canonical file.
- **“Triggers alone explain the skill.”** Describe the capability and its use conditions; reserve implementation details for the body.

## Report

Return: changed paths, major deletions/extractions, validator and test commands with results, approximate token count, dry-run result, and any blocker. Distinguish structural checks from behavioral evidence. Keep it brief.

Authoring reference: [Anthropic's best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices). Consult when reassessing guidance; the token budget and completion gates above are local conventions.
