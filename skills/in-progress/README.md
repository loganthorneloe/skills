# In progress

Workshop skills. Rough edges expected. **Not** in the RTG README table.

## Install

Hidden from default `npx skills` (`metadata.internal: true`).

```bash
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --list
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill brand
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill deep-research
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill evolve-skills
```

Local: symlink `skills/in-progress/<name>` → harness skills dir.

## Current

| Skill | Notes |
| --- | --- |
| [`brand`](brand/SKILL.md) | AI for Software Engineers visual identity; hidden from default installs. |
| [`deep-research`](deep-research/SKILL.md) | Source-gated web research saved as a concise, cited Markdown report; Reddit prohibited. |
| [`evolve-skills`](evolve-skills/SKILL.md) | **Only** user-facing evolve entry. Steps under `steps/`; law under `references/`. |

Workers are **not** separate skills (no slash noise). Router loads `steps/*.md` via progressive disclosure.

## Graduate

1. Drop `metadata.internal`
2. `mv skills/in-progress/<name> skills/rtg/<name>`
3. Root README Available Skills row; remove its entry here
4. `feat(skills): graduate <name>`
