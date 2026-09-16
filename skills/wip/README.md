# WIP

Workshop skills. Rough edges expected. **Not** in the RTG README table.

## Install

Hidden from default `npx skills` (`metadata.internal: true`).

```bash
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --list
```

Local: symlink `skills/wip/<name>` → harness skills dir.

## Current

No WIP skills currently.

## Graduate

1. Drop `metadata.internal`
2. `mv skills/wip/<name> skills/rtg/<name>`
3. Root README Available Skills row; remove its entry here
4. `feat(skills): graduate <name>`
