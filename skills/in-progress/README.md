# In progress

Workshop skills. Rough edges expected. **Not** in the stable README table.

## Install

Hidden from default `npx skills` (`metadata.internal: true`).

```bash
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --list
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill evolve-skills
```

Local: symlink `skills/in-progress/evolve-skills` → harness skills dir.

## Current

| Skill | Notes |
| --- | --- |
| [`evolve-skills`](evolve-skills/SKILL.md) | **Only** user-facing evolve entry. Steps under `steps/`; law under `references/`. |

Workers are **not** separate skills (no slash noise). Router loads `steps/*.md` via progressive disclosure.

## Graduate

1. Drop `metadata.internal`
2. `mv skills/in-progress/evolve-skills skills/evolve-skills`
3. Root README Available Skills row; trim this file
4. `feat(skills): graduate evolve-skills`
