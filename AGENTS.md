# Agent Guidelines for `loganthorneloe/skills` Repository

## Rules

Be EXTREMELY concise. Sacrifice grammatical correctness in favor of conciseness ALWAYS.

## Repository Layout & Skill Conventions

1. **Source only here**: create/edit skills under `skills/` in this repo. NEVER only in a harness folder (`~/.claude/skills`, `~/.pi/agent/skills`, etc.).
2. **Entrypoint**: every skill is `…/<skill-name>/SKILL.md` (YAML frontmatter + body).
3. **Scripts**: `scripts/` only when portable (no single-harness config trees).
4. **Install**: `npx skills add loganthorneloe/skills`.
5. **Personal-machine link (required)**: whenever a skill is created in this repo, symlink its source directory into the active personal harness’s global skills directory (Pi: `~/.pi/agent/skills/<name>`). Confirm the link resolves to `SKILL.md` and creates no duplicate frontmatter name.
6. **Commits**: conventional (`feat(skills): …`, `fix(skills): …`).

## Skill quality workflow

Before creating or refining any skill, read and follow [`skills/wip/skill-refiner/SKILL.md`](skills/wip/skill-refiner/SKILL.md), including its required gotchas reference. Apply it from the first draft, not only during cleanup. Completion requires validator `PASS`, available target-specific checks, and a representative dry run; otherwise report blocked.

## RTG vs WIP

Two tiers. Do not mix.

| Tier | Path | `metadata.internal` | README |
|------|------|---------------------|--------|
| **RTG (completed)** | `skills/rtg/<name>/` | omit or `false` | Root **Available Skills** table |
| **WIP** | `skills/wip/<name>/` | **`true` (required)** | `skills/wip/README.md` + root **WIP** table |

### Why

- `npx skills` hides `metadata.internal: true` unless `INSTALL_INTERNAL_SKILLS=1`
- Folder makes WIP obvious in git; flag makes WIP non-default for consumers

### New completed skill

1. `skills/rtg/<name>/SKILL.md` (no `internal: true`)
2. Row in root `README.md` → **Available Skills**
3. Thin SKILL.md; heavy detail in `references/` if needed

### New WIP skill

1. `skills/wip/<name>/SKILL.md`
2. Frontmatter must include:

```yaml
metadata:
  internal: true
```

(merge with existing `metadata` keys, e.g. `opencode/slash`)

3. One-line entry in `skills/wip/README.md`
4. Do **not** add to root Available Skills table
5. Description may say WIP; internal flag is what hides from default CLI

### Graduate WIP → RTG

1. Remove `internal: true` (delete key; drop empty `metadata` only if nothing else left)
2. `mv skills/wip/<name> skills/rtg/<name>`
3. Root README Available Skills row; remove from `skills/wip/README.md`
4. Commit: `feat(skills): graduate <name>`

### Demote RTG → WIP

1. `mv skills/rtg/<name> skills/wip/<name>`
2. Set `metadata.internal: true`
3. Swap README rows
4. Commit: `chore(skills): demote <name> to WIP`

### CLI cheatsheet

```bash
npx skills add loganthorneloe/skills --list          # RTG only
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --list
INSTALL_INTERNAL_SKILLS=1 npx skills add loganthorneloe/skills --skill <wip-name>
```

No other official “status” field in Agent Skills / `npx skills` — use **path + `internal`**.

## Invocation (user slash vs model)

| Intent | How |
|--------|-----|
| **User entry** | Own `SKILL.md` + `disable-model-invocation: true` if slash-only |
| **Internal steps** | **Not** separate skills. Put under `steps/` or `references/` inside the parent skill; parent says `read` them. No slash, no extra discovery. |
| **Model-auto skill** | Top-level skill, no `disable-model-invocation`; optional `user-invocable: false` (Claude hides slash; pi may still list `/skill:name`) |

**Do not** ship multi-step packs as many top-level skills if only one should appear in slash — pi discovers every `SKILL.md` and registers `/skill:name`.

## Harness-agnostic skills (required)

1. Workflows/preferences, not product installers. Any harness.
2. Never hard-code one harness’s paths/APIs as the only path.
3. Discover current harness; use native instructions/settings/permissions/keybindings/extensions.
4. Harness examples OK as brief illustrations. Prefer semantic goals.
5. Do not commit machine-local harness config into skills.
6. `setup-lat`: preference workflow only. No pi-only install trees.
7. Skill installs must target one current harness + one scope. Never use all-agent fan-out when native and shared discovery roots may overlap.
8. After changing install instructions, audit every discovered root for duplicate frontmatter names; zero skill collisions required.

## LAT Preferences (reference)

- Conciseness always on
- Auto-memory off
- Modes: **lfg** (default, yellow) → **ask** (green) → **plan** (red)
- `/clear` = fresh session (alias native `/new` / clear-conversation)
