# Skills

Reusable skills for AI agents.

## Available Skills

| Skill | Description |
| --- | --- |
| [break-it-down](skills/rtg/research/break-it-down/SKILL.md) | Explanations from first principles with original source evidence and HTML reports. Requires the other research skills. |
| [source-audit](skills/rtg/research/source-audit/SKILL.md) | Vet sources and return pass, conditional, or fail records. |
| [find-evidence](skills/rtg/research/find-evidence/SKILL.md) | Extract original figures, tables, quotes, and metrics that support claims. |
| [voice](skills/rtg/research/voice/SKILL.md) | Write plain, direct, connected explanatory prose. |
| [skill-refiner](skills/rtg/skill-refiner/SKILL.md) | Create and improve skills with validation. |

## Install

Research skills live in `skills/rtg/research/` and work separately; `break-it-down` loads the other three.

```bash
npx skills add loganthorneloe/skills
```
