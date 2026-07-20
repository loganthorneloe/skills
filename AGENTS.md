# Agent Guidelines for `loganthorneloe/skills` Repository

## Repository Layout & Skill Conventions
1. **Source Directory**: All skills MUST ALWAYS be created inside `skills/<skill-name>/` in this repo. NEVER create skills directly in `~/.gemini/config/skills/` on device.
2. **Skill Entrypoint**: Every skill requires `skills/<skill-name>/SKILL.md`.
3. **Executable Helpers**: Place scripts in `skills/<skill-name>/scripts/`.
4. **Symlink Installation**: When creating or modifying a skill, symlink it via the setup script or run:
   ```bash
   ln -s "$(pwd)/skills/<skill-name>" ~/.gemini/config/skills/<skill-name>
   ```
5. **Git Workflow**: Commit changes to `main` branch with conventional commit messages (`feat(skills): ...`, `fix(skills): ...`).

