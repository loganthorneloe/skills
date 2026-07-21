# Development Skills for AI Coding Agents

Public skills for AI coding agents (Claude Code, Codex, Cursor, OpenCode, pi, etc.).

Install with Vercel’s `npx skills` CLI. Layout and stability rules: [`AGENTS.md`](AGENTS.md).

## Available Skills

Stable. Safe default install.

| Skill | Description |
| --- | --- |
| [`auto-loop`](skills/auto-loop/SKILL.md) | Autonomous continuous development loop until the goal is done. |
| [`commit-and-push`](skills/commit-and-push/SKILL.md) | Update affected READMEs, commit, push (conventional commits). |
| [`cost`](skills/cost/SKILL.md) | Session token usage and estimated cost across harnesses. |
| [`setup-lat`](skills/setup-lat/SKILL.md) | LAT prefs: conciseness, no memory, ask/plan/turbo, `/clear`=fresh session. |

## In progress

Workshop only. Marked `metadata.internal: true` — **omitted** from default `npx skills` list/install.

| Skill | Description |
| --- | --- |
| [`evolve-skills` pack](skills/in-progress/) | Trajectory → health/mine/diagnose/propose/apply (+ `skill-quality`). See [in-progress README](skills/in-progress/README.md). |

```bash
# list / install WIP
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --list
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill evolve-skills
```

## Repository Structure

```text
skills/                         # repo root
├── README.md
├── AGENTS.md                   # conventions for agents + humans
└── skills/
    ├── <stable-skill>/SKILL.md
    └── in-progress/
        ├── README.md
        └── <wip-skill>/SKILL.md   # metadata.internal: true
```

## Install

```bash
# stable only (default)
npx skills add loganthorneloe/skills
npx skills add loganthorneloe/skills --skill commit-and-push
npx skills add loganthorneloe/skills --list

# include in-progress
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills
```

Local dev: symlink `skills/<name>` or `skills/in-progress/<name>` into the harness skills directory.
