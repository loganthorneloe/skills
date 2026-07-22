# In progress

Workshop skills. Rough edges expected. **Not** in the stable README table.

## Install

Hidden from default `npx skills` (`metadata.internal: true`).

```bash
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --list
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill deep-research
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill evolve-skills
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill send-to-email
```

Local: symlink `skills/in-progress/<name>` → harness skills dir.

## Current

| Skill | Notes |
| --- | --- |
| [`deep-research`](deep-research/SKILL.md) | Evidence-backed internet research with claim-level citations and a full bibliography. |
| [`evolve-skills`](evolve-skills/SKILL.md) | **Only** user-facing evolve entry. Steps under `steps/`; law under `references/`. |
| [`send-to-email`](send-to-email/SKILL.md) | Preserve transient work as a durable email handoff; explicit invocation authorizes one immediate send with readable HTML rendering. |

Workers are **not** separate skills (no slash noise). Router loads `steps/*.md` via progressive disclosure.

## Graduate

1. Drop `metadata.internal`
2. `mv skills/in-progress/<name> skills/<name>`
3. Root README Available Skills row; remove its entry here
4. `feat(skills): graduate <name>`
