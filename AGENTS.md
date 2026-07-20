# Agent Guidelines for `loganthorneloe/skills` Repository

## Repository Layout & Skill Conventions
1. **Source Directory**: All skills MUST ALWAYS be created inside `skills/<skill-name>/` in this repo. NEVER create skills directly in `~/.gemini/config/skills/` on device.
2. **Skill Entrypoint**: Every skill requires `skills/<skill-name>/SKILL.md`.
3. **Executable Helpers**: Place scripts in `skills/<skill-name>/scripts/`.
4. **Installation & Usage**: Skills are installed across agent harnesses using `npx skills add loganthorneloe/skills`. For local testing, symlink `skills/<skill-name>` into your target harness skill folder (e.g. `~/.gemini/config/skills/`, `~/.claude/skills/`).
5. **Git Workflow**: Commit changes to `main` branch with conventional commit messages (`feat(skills): ...`, `fix(skills): ...`).

