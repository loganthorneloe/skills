# Development Skills for AI Coding Agents

Public skills for AI coding agents (Claude Code, Codex, Cursor, OpenCode, pi, etc.).

Install with Vercel’s `npx skills` CLI. Layout and stability rules: [`AGENTS.md`](AGENTS.md).

## Available Skills

RTG (completed). Safe default install.

| Skill | Description |
| --- | --- |
| [`commit-and-push`](skills/rtg/commit-and-push/SKILL.md) | Update affected READMEs, commit, push (conventional commits). |
| [`cost`](skills/rtg/cost/SKILL.md) | Session token usage and recorded cost when available across harnesses. |
| [`edit`](skills/rtg/edit/SKILL.md) | Diagnose prose rigorously, then apply only approved minimal corrections. |
| [`setup-lat`](skills/rtg/setup-lat/SKILL.md) | LAT prefs, secure Readwise Reader MCP setup, and branded visual tooling with `/brand` and Bento Slides. |
| [`skill-refiner`](skills/rtg/skill-refiner/SKILL.md) | Create or refine skills with routing, workflow, disclosure, and proof gates. |

## In progress

Workshop only. `metadata.internal: true` — omitted from default `npx skills` list/install.

| Skill | Description |
| --- | --- |
| [`brand`](skills/in-progress/brand/SKILL.md) | Apply the AI for Software Engineers brand to slides, videos, diagrams, thumbnails, and illustrations. |
| [`deep-research`](skills/in-progress/deep-research/SKILL.md) | Source-gated web and connected Reader archive/later research saved as a concise cited report; Reddit prohibited. |
| [`evolve-skills`](skills/in-progress/evolve-skills/SKILL.md) | Trajectory → health/mine/diagnose/propose/apply. One slash entry; steps internal. |

```bash
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --list
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill brand
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill deep-research
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill evolve-skills
```

## Repository Structure

```text
skills/
├── README.md
├── AGENTS.md
└── skills/
    ├── rtg/
    │   └── <completed-skill>/SKILL.md
    └── in-progress/
        ├── README.md
        └── evolve-skills/
            ├── SKILL.md          # user entry only
            ├── steps/            # loaded on demand (not separate skills)
            └── references/
```

## Install

```bash
npx skills add loganthorneloe/skills
npx skills add loganthorneloe/skills --skill commit-and-push
npx skills add loganthorneloe/skills --list

INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills
```

Local dev: symlink `skills/rtg/<name>` or `skills/in-progress/<name>` into the harness skills directory.
