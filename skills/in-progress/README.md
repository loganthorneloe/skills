# In progress

Workshop skills. Rough edges expected. **Not** in the RTG README table.

## Install

Hidden from default `npx skills` (`metadata.internal: true`).

```bash
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --list
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill brand
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill deep-research
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill prompt-refiner
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill skill-refiner
```

Local: symlink `skills/in-progress/<name>` → harness skills dir.

## Current

| Skill | Notes |
| --- | --- |
| [`brand`](brand/SKILL.md) | AI for Software Engineers visual identity; hidden from default installs. |
| [`deep-research`](deep-research/SKILL.md) | Source-gated web and connected Reader archive/later research saved as a concise cited report; Reddit prohibited. |
| [`prompt-refiner`](prompt-refiner/SKILL.md) | Compile a prompt for a fresh agent context while preserving semantics and excluding unapproved conversation context. |
| [`skill-refiner`](skill-refiner/SKILL.md) | Create or refine skills with routing, workflow, disclosure, and proof gates. |

## Graduate

1. Drop `metadata.internal`
2. `mv skills/in-progress/<name> skills/rtg/<name>`
3. Root README Available Skills row; remove its entry here
4. `feat(skills): graduate <name>`
