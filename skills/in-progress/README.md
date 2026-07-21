# In progress

Workshop skills. Rough edges expected. **Not** in the stable README table.

## Install

Hidden from default `npx skills` discovery (`metadata.internal: true`).

```bash
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --list
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill evolve-skills
```

Local: symlink `skills/in-progress/<name>` into the harness skills dir.

## Graduate to stable

1. Drop `metadata.internal: true` (keep other metadata)
2. `mv skills/in-progress/<name> skills/<name>`
3. Add row under **Available Skills** in root `README.md`
4. Remove from any in-progress lists
5. Commit: `feat(skills): graduate <name>`

## Current

| Skill | Notes |
| --- | --- |
| `skill-quality` | Skill authoring constitution |
| `skill-sessions` | Trajectory ingest |
| `skill-health` | Health scores |
| `skill-mine` | New-skill forge |
| `skill-diagnose` | One-skill evidence |
| `skill-propose` | Gated proposals |
| `skill-apply` | Apply + verify |
| `evolve-skills` | Router for the pack above |
