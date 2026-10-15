# Development Skills for AI Coding Agents

Public skills for AI coding agents (Claude Code, Codex, Cursor, OpenCode, pi, etc.).

Install with Vercel’s `npx skills` CLI. Layout and stability rules: [`AGENTS.md`](AGENTS.md).

## Available Skills

RTG (completed). Safe default install.

| Skill | Description |
| --- | --- |
| [`break-it-down`](skills/rtg/break-it-down/SKILL.md) | First-principles explanations grounded in authoritative sources, delivered as simple HTML reports with portable Logan styling. |
| [`skill-refiner`](skills/rtg/skill-refiner/SKILL.md) | Create or refine skills with routing, workflow, disclosure, and proof gates. |

## WIP

No WIP skills currently.

## Repository Structure

```text
skills/
├── README.md
├── AGENTS.md
└── skills/
    ├── rtg/
    │   └── <completed-skill>/SKILL.md
    └── wip/
        ├── README.md
        └── <workshop-skill>/SKILL.md
```

## Install

```bash
npx skills add loganthorneloe/skills
npx skills add loganthorneloe/skills --skill break-it-down
npx skills add loganthorneloe/skills --list

INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills
```

Local dev: symlink `skills/rtg/<name>` or `skills/wip/<name>` into the harness skills directory.

## Break It Down

Maintain `break-it-down` in `skills/rtg/break-it-down/`. It replaces the standalone `break-it-down` repository as the canonical source, including its latest portability and web-report guidance. Install or share the complete skill folder; the bundled reference makes it usable without a companion brand skill or local brand repository.
