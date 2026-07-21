# Agent Guidelines for `loganthorneloe/skills` Repository

## Repository Layout & Skill Conventions
1. **Source Directory**: All skills MUST ALWAYS be created inside `skills/<skill-name>/` in this repo. NEVER create skills directly in a harness skill folder on device (e.g. `~/.gemini/config/skills/`, `~/.claude/skills/`, `~/.pi/agent/skills/`).
2. **Skill Entrypoint**: Every skill requires `skills/<skill-name>/SKILL.md`.
3. **Executable Helpers**: Place scripts in `skills/<skill-name>/scripts/` only when the logic is truly portable (no single-harness config trees).
4. **Installation & Usage**: Skills are installed across agent harnesses using `npx skills add loganthorneloe/skills`. For local testing, symlink `skills/<skill-name>` into the target harness skill folder.
5. **Git Workflow**: Commit changes to `main` with conventional commits (`feat(skills): ...`, `fix(skills): ...`).

## Harness-Agnostic Skills (required)
1. Skills are **workflows and preferences**, not product installers. They must run usefully in any agent harness (pi, Claude Code, Codex, OpenCode, Gemini, etc.).
2. **Never** hard-code one harness's paths, APIs, or asset bundles as the only implementation path.
3. The agent executing the skill must **discover** the current harness and its config system, then apply the skill's goals with native mechanisms (instructions, settings, permissions, keybindings, extensions).
4. Harness-specific examples are OK only as brief illustrations. Prefer semantic goals ("enable read-only plan mode") over copy-paste for a named product.
5. Do **not** commit machine-local harness config (e.g. `~/.pi/agent/extensions/*`) into skills. If a preference needs code, describe behavior; let the agent implement it for the active harness when possible.
6. `setup-lat` especially: preference workflow only (conciseness, no auto-memory, ask/plan/turbo, /clear=fresh session). No pi-only install trees.

## LAT Preferences (reference)
When relevant, honor these user defaults:
- Conciseness always on
- Auto-memory off
- Modes: **turbo** (default, no prompts) → **ask** (confirm mutations) → **plan** (read-only)
- Turbo default-on
- `/clear` = fresh session (alias native `/new` / clear-conversation)
