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

Install everything:

```bash
npx skills add loganthorneloe/skills
```

Or install specific skills with `--skill <name>`. The research skills in `skills/rtg/research/` each work on their own, but `break-it-down` requires the other three, so install them together:

```bash
npx skills add loganthorneloe/skills --skill break-it-down source-audit find-evidence voice
```
