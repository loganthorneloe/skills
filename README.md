# Development Skills for AI Coding Agents

A collection of public, custom AI skills designed for development workflows across modern AI agent harnesses (Antigravity, Claude Code, Cursor, Codex, OpenCode).

Each subdirectory in `skills/` represents a distinct skill that can be loaded into any supported AI harness via Vercel's `npx skills` CLI.

## Available Skills

| Skill | Description |
| --- | --- |
| [`auto-loop`](skills/auto-loop/SKILL.md) | Autonomous continuous development loop (plan, implement, test, debug, verify) until 100% complete. |
| [`commit-and-push`](skills/commit-and-push/SKILL.md) | Inspects and updates affected READMEs, stages, commits, and pushes changes with conventional commit messages. |
| [`cost`](skills/cost/SKILL.md) | Calculates session token usage and estimated cost ($) across AI harnesses. |

## Repository Structure

```text
skills/ (repository root)
├── README.md                 # Repository overview and guidelines
├── AGENTS.md                 # Agent guidelines for this repository
├── .gitignore                # Git ignore rules
└── skills/                   # Folder housing all skills (for Vercel CLI)
    └── [skill-name]/         # Individual custom skill folder
        ├── SKILL.md          # Main instructions & metadata (required)
        └── scripts/          # Helper scripts (TypeScript or Python)
```

## Installing and Activating Skills

This repository is compatible with Vercel's `skills` CLI. Install skills directly into any agent harness:

### Install all skills from this repository
```bash
npx skills add loganthorneloe/skills
```

### Install a specific skill from this repository
```bash
npx skills add loganthorneloe/skills --skill commit-and-push
```

### List skills available in this repository
```bash
npx skills add loganthorneloe/skills --list
```

Once installed, the skills will be automatically loaded by your AI agent.
