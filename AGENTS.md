# Agent Guidelines for `loganthorneloe/skills` Repository

## Rules

Be EXTREMELY concise. Sacrifice grammatical correctness in favor of conciseness ALWAYS.

## Repository Layout & Skill Conventions

1. **Source only here**: create/edit skills under `skills/` in this repo. NEVER only in a harness folder (`~/.claude/skills`, `~/.pi/agent/skills`, etc.).
2. **Entrypoint**: every skill is `…/<skill-name>/SKILL.md` (YAML frontmatter + body).
3. **Scripts**: `scripts/` only when portable (no single-harness config trees).
4. **Install**: `npx skills add loganthorneloe/skills`. Local test: symlink into harness skills dir.
5. **Commits**: conventional (`feat(skills): …`, `fix(skills): …`).

## Stable vs in-progress

Two tiers. Do not mix.

| Tier | Path | `metadata.internal` | README |
|------|------|---------------------|--------|
| **Stable** | `skills/<name>/` | omit or `false` | Root **Available Skills** table |
| **In progress** | `skills/in-progress/<name>/` | **`true` (required)** | `skills/in-progress/README.md` + short root **In progress** blurb |

### Why

- `npx skills` hides `metadata.internal: true` unless `INSTALL_INTERNAL_SKILLS=1`
- Folder makes WIP obvious in git; flag makes WIP non-default for consumers

### New stable skill

1. `skills/<name>/SKILL.md` (no `internal: true`)
2. Row in root `README.md` → **Available Skills**
3. Thin SKILL.md; heavy detail in `references/` if needed

### New in-progress skill

1. `skills/in-progress/<name>/SKILL.md`
2. Frontmatter must include:

```yaml
metadata:
  internal: true
```

(merge with existing `metadata` keys, e.g. `opencode/slash`)

3. One-line entry in `skills/in-progress/README.md`
4. Do **not** add to root Available Skills table
5. Description may say WIP; internal flag is what hides from default CLI

### Graduate WIP → stable

1. Remove `internal: true` (delete key; drop empty `metadata` only if nothing else left)
2. `mv skills/in-progress/<name> skills/<name>`
3. Root README Available Skills row; remove from `skills/in-progress/README.md`
4. Commit: `feat(skills): graduate <name>`

### Demote stable → WIP

1. `mv skills/<name> skills/in-progress/<name>`
2. Set `metadata.internal: true`
3. Swap README rows
4. Commit: `chore(skills): demote <name> to in-progress`

### CLI cheatsheet

```bash
npx skills add loganthorneloe/skills --list          # stable only
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

Evolve pack pattern: one `evolve-skills` skill; pipeline in `steps/*.md`.

## Harness-agnostic skills (required)

1. Workflows/preferences, not product installers. Any harness.
2. Never hard-code one harness’s paths/APIs as the only path.
3. Discover current harness; use native instructions/settings/permissions/keybindings/extensions.
4. Harness examples OK as brief illustrations. Prefer semantic goals.
5. Do not commit machine-local harness config into skills.
6. `setup-lat`: preference workflow only. No pi-only install trees.

## LAT Preferences (reference)

- Conciseness always on
- Auto-memory off
- Modes: **turbo** (default) → **ask** → **plan**
- `/clear` = fresh session (alias native `/new` / clear-conversation)
