# LAT preference contract

Read completely after harness discovery and before changing configuration. Implement with the current harness's native mechanisms.

## 1. Conciseness and memory

Add this exact always-on line under `## Rules` in persistent instructions; merge, never overwrite:

```text
Be EXTREMELY concise. Sacrifice grammatical correctness in favor of conciseness ALWAYS.
```

Disable learned, automatic, or continuous cross-session memory through native settings/environment. Delete only stores belonging to that feature. Preserve ordinary session transcripts unless the user asks otherwise.

## 2. Modes

Default and cycle: **lfg → ask → plan**. Prefer one cycle hotkey (`Shift+Tab`) plus explicit commands/flags.

| Mode | Behavior | Indicator |
|---|---|---|
| ask | full tools; confirm before mutations | green |
| plan | read-only exploration; block mutations/destructive shell | red |
| lfg | full tools; no confirmation prompts | yellow |

Use native permission modes. In ask, expose allow-once, deny, and persistent always-allow when supported. If the harness calls unrestricted mode `turbo`, expose `lfg` as canonical and keep `turbo` only as compatibility. Do not invent keybindings that conflict with native mode cycling. Document actual controls under `## Agent Modes` (or `## LFG Mode` if only one mode is possible).

## 3. `/clear`

`/clear` starts a fresh conversation/session—the native `/new`, clear-conversation, or equivalent—not merely a terminal repaint. Register an alias/command/keybinding through native APIs and preserve the native command when possible. If `/clear` already has risky conflicting behavior, ask before replacing it.

## 4. Autonomous `/goal`

`/goal <task>` sets/replaces one visible session goal and starts work immediately. `/goal` or `/goal show` displays it; `/goal clear` stops it.

When supported:

- persist goal state within the session and restore it across branch/resume;
- inject the active goal each turn;
- enqueue another continuation when the agent settles before completion;
- expose a model-callable completion action only while a goal is active;
- require that action to include summary plus concrete test/verification evidence;
- show a concise active goal in footer/status;
- stop only after valid completion action or `/goal clear`.

Use native loop/task/extension APIs, never an external polling process. Warn that continuation makes repeated model calls and can incur cost. If commands, follow-up turns, durable state, completion tools, or UI are unsupported, implement only the closest safe native subset and report each gap.

## 5. Compact Git status

Inside a Git repository show:

- `git ✓` when clean
- `git +2 ~1 ?3 !1` for staged, unstaged, untracked, conflicts

Prefer right alignment beneath model information without adding a dedicated row. Otherwise share an existing status line. Preserve native footer data. Hide outside Git repositories. Refresh after mutation tools and external changes; prefer native events, otherwise a lightweight session-scoped interval cleaned up on reload, session switch, and shutdown.

## 6. Branded visual tooling

Determine the current harness's `npx skills` agent ID and whether setup is project- or user-scoped. Every install targets exactly that agent and scope; add `-g` only for user scope. Never use `--all`.

Install/update only `/brand` from this repository:

```bash
INSTALL_INTERNAL_SKILLS=1 npx --yes skills add loganthorneloe/skills --skill brand --agent <current-agent-id> -y
```

Add this exact persistent rule under `## Brand`:

```text
For visual deliverables (slides, videos, diagrams, charts, thumbnails, illustrations, and motion graphics), load `/brand` unless the user explicitly requests another brand or an unbranded output. `/brand` routes branded slides through `/bento-slides`.
```

Install/update Bento Slides for the same agent/scope:

```bash
npx --yes skills add nyblnet/bento --skill bento-slides --agent <current-agent-id> -y
```

Audit every discovered skill root. Group `SKILL.md` files by frontmatter `name`; one name must resolve to one physical skill. Remove only confirmed installer-managed duplicate links/copies, preserving the newest canonical install and anything another harness still needs. Reload the harness if new skills are not immediately visible.

## 7. Optional QoL

Configure model favorites/cycling or short command aliases only when native, easy, and requested. Never change the default model/provider without asking.

## Gotchas

- Harness examples are hints, not portable implementation. Discover live APIs and paths; do not install another product's config tree.
- Global Pi discovers both `~/.pi/agent/skills` and `~/.agents/skills`; the same frontmatter name in both is a collision.
- One installer may create links into another auto-discovered root. Resolve physical paths before deleting a “duplicate.”
- Default remains lfg. Do not silently map ask or plan semantics onto lfg.
- Disabling auto-memory does not authorize deleting transcripts, authored notes, or unrelated caches.
- A footer that drops native information or leaks timers/watchers is not complete.
- A stored goal without autonomous continuation and evidence-gated completion is only a partial implementation; label the gap.
- Installed files alone do not prove discoverability. Run the harness's list/load check and inspect collision diagnostics.
