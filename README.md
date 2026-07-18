# Development Skills for Antigravity

A collection of public, custom AI skills designed for development workflows using the Google Antigravity platform.

Each subdirectory in this repository represents a distinct skill that can be loaded into Antigravity to extend its capabilities with specialized instructions, context, scripts, and references.

## Repository Structure

This is a multi-skill repository organized as follows:

```text
skills/ (repository root)
├── README.md                 # Repository overview and guidelines
├── .gitignore                # Git ignore rules for node/python/etc.
└── skills/                   # Folder housing all skills (for Vercel CLI)
    └── [skill-name]/         # Individual custom skill folder
        ├── SKILL.md          # Main instructions & metadata (required)
        ├── scripts/          # Helper scripts (TypeScript or Python)
        ├── references/       # Local markdown files containing reference docs
        ├── examples/         # Reference implementations and examples
        └── resources/        # External templates or static assets
```

## Skill Specification (`SKILL.md`)

Every skill folder must contain a `SKILL.md` file at its root with the following YAML frontmatter:

```yaml
---
name: skill-name-kebab-case
description: A short, clear description of what this skill does and when it should be used.
---

# Instructions for the Skill

Detailed guidelines, rules, and procedures for the AI agent to follow when this skill is active.
```

### Guidelines for Scripts
To maintain a high-quality codebase, we follow these strict rules for helper scripts within the `scripts/` directory:
- **Languages**: Use **TypeScript** or **Python** only. Do not write scripts in plain JavaScript.
- **Documentation**: Keep helper script code clean, modular, and self-documenting.

## Installing and Activating Skills

This repository is compatible with Vercel's `skills` package manager CLI. You or others can install the skills from this repository directly using `npx skills`:

### Install all skills from this repository
```bash
npx skills add loganthorneloe/skills
```

### Install a specific skill from this repository
```bash
npx skills add loganthorneloe/skills --skill template-skill
```

### List skills available in this repository before adding
```bash
npx skills add loganthorneloe/skills --list
```


Once installed, the skill will be automatically loaded by your AI agent.
