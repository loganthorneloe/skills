# Skill gotchas

Read completely before creating or refining a skill. Apply only relevant domain notes; do not copy this file into every target.

## Routing and invocation

- `description` is always-loaded routing context. Start with `Load when...`; include quoted, natural phrases a user would type. Keep implementation details in the body.
- Automatic routing and slash-only invocation differ. Use the current harness's supported invocation fields. Do not hide a skill from model routing when automatic loading is intended.
- Internal pipeline steps are files inside one parent skill, not extra `SKILL.md` entrypoints. Extra entrypoints create slash-command and name noise.

## Structure and disclosure

- `SKILL.md` must stand alone for the default path. A reference cannot contain a rule needed before the agent knows to load it.
- Every reference link needs a load condition: always before step N, or only when branch X applies.
- Centralize legacy behavior, API inconsistencies, edge cases, and unsafe defaults in one `## Gotchas` section or reference. Require it before the affected action.
- Keep examples only when they resolve a real ambiguity. Examples can accidentally become a second specification.
- Scripts are for portable deterministic work. Do not package machine-local or single-harness configuration trees as skill scripts.

## Defensive design

- Models optimize for apparent completion. Replace “verify” with the exact command, expected signal, and failure behavior.
- Put rebuttals beside likely shortcuts; generic warnings at the end are easy to ignore.
- Missing tests do not justify no proof. Use a deterministic validator plus a representative dry run; executable behavior requires an execution test.
- A blocked dependency means `blocked`, not “complete with caveats.”

## Frontmatter and files

- Use `SKILL.md` with valid YAML frontmatter. Keep the frontmatter `name` lowercase, hyphenated, and matching the parent directory for cross-harness portability.
- Keep descriptions within the Agent Skills limit (1,024 characters) and names within 64 characters.
- Resolve relative links from the skill directory. Validate that referenced files exist after moves.
- Preserve compatibility, licensing, invocation, and package metadata unless there is evidence to change them.
- Audit discovered skill roots for duplicate frontmatter names after install-path changes.

## This repository

When refining `loganthorneloe/skills`:

- Source belongs under `skills/`, never only in a harness install directory.
- Completed skills belong in `skills/rtg/` and the root Available Skills table.
- WIP skills belong in `skills/wip/`, require `metadata.internal: true`, and belong in both WIP README listings—not the Available Skills table.
- Follow `AGENTS.md` for graduation, installation, and harness-agnostic rules.
