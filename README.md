# Development Skills for AI Coding Agents

Public skills for AI coding agents (Claude Code, Codex, Cursor, OpenCode, pi, etc.).

Install with Vercel’s `npx skills` CLI. Layout and stability rules: [`AGENTS.md`](AGENTS.md).

## Available Skills

Stable. Safe default install.

| Skill | Description |
| --- | --- |
| [`commit-and-push`](skills/commit-and-push/SKILL.md) | Update affected READMEs, commit, push (conventional commits). |
| [`cost`](skills/cost/SKILL.md) | Session token usage and estimated cost across harnesses. |
| [`setup-lat`](skills/setup-lat/SKILL.md) | LAT prefs: conciseness, no memory, modes, `/clear`, autonomous `/goal`, compact Git status. |

## In progress

Workshop only. `metadata.internal: true` — omitted from default `npx skills` list/install.

| Skill | Description |
| --- | --- |
| [`deep-research`](skills/in-progress/deep-research/SKILL.md) | Iterative web research with primary-source verification, claim-level citations, and a full bibliography. |
| [`evolve-skills`](skills/in-progress/evolve-skills/SKILL.md) | Trajectory → health/mine/diagnose/propose/apply. One slash entry; steps internal. |
| [`send-to-email`](skills/in-progress/send-to-email/SKILL.md) | Preserve transient work as a durable email handoff; resolve context, preview, confirm, and send. |

```bash
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --list
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill deep-research
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill evolve-skills
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill send-to-email
```

## Repository Structure

```text
skills/
├── README.md
├── AGENTS.md
└── skills/
    ├── <stable-skill>/SKILL.md
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

Local dev: symlink `skills/<name>` or `skills/in-progress/<name>` into the harness skills directory.
