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

## 6. MCP connectivity

Enable MCP through the current harness's native client when available. Otherwise use its native extension/plugin mechanism; do not add a standalone compatibility layer outside the harness.

For Pi, install and enable the token-efficient `pi-mcp-adapter` as a user package. Resolve and pin the current registry version rather than using a floating tag:

```bash
version="$(npm view pi-mcp-adapter version)"
pi install "npm:pi-mcp-adapter@$version"
```

Verify the package appears in `pi list` and the persistent package list, then reload or restart and invoke `/mcp`. Installation is incomplete until `/mcp` loads without an extension error. Do not import host-specific MCP configuration or configure servers other than Readwise.

For another harness, persist its native MCP enablement and run its server-status or setup command. If neither native MCP nor a documented extension/plugin API exists, report MCP as unsupported rather than installing another harness's files.

### Readwise Reader

After MCP connectivity works, configure Readwise as part of the standard setup:

1. Check Readwise's official MCP documentation and confirm its current remote HTTP endpoint is on `readwise.io`. The expected endpoint is `https://mcp2.readwise.io/mcp`; stop if official documentation disagrees or redirects to a non-Readwise domain.
2. Merge one server named `readwise` into the harness's native MCP config at the resolved scope. Never overwrite unrelated servers or settings.
3. Configure remote HTTP plus OAuth. The server definition may contain only the official URL and non-secret transport/lifecycle options—no bearer token, API key, client secret, authorization code, callback URL, or credential command.
4. Reload/restart, start browser OAuth through the harness's native auth control, and let the callback complete locally. Never ask the user to paste a token, code, authorization URL, or callback URL into chat or a shell command.
5. Require the harness's OS/native secure credential store. If it is unavailable or the harness would persist OAuth material in plaintext, stop and report **blocked**; do not downgrade to a Reader API token.
6. Verify connected status and tool metadata containing both `reader_` and `readwise_` tools. Do not call a create, update, delete, move, tag, highlight, or bulk-edit tool as a setup test.

For Pi user scope, merge this non-secret entry into `~/.config/mcp/mcp.json`; for project scope, use `.mcp.json`:

```json
{
  "mcpServers": {
    "readwise": {
      "url": "https://mcp2.readwise.io/mcp",
      "auth": "oauth",
      "lifecycle": "lazy"
    }
  }
}
```

Create a user config directory with mode `0700` and config file with mode `0600` when possible. Then run `/reload`, `/mcp-auth readwise`, approve the browser prompt, and inspect `/mcp` or `mcp({ connect: "readwise" })`. The adapter stores OAuth credentials in the operating-system credential store; its legacy OAuth directory is not an acceptable new credential target.

For another harness, use its native equivalent of the same remote server and browser OAuth flow. Do not copy Pi config paths or commands.

## 7. Branded visual tooling

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

## 8. Optional QoL

Configure model favorites/cycling or short command aliases only when native, easy, and requested. Never change the default model/provider without asking.

## Gotchas

- Harness examples are hints, not portable implementation. Discover live APIs and paths; do not install another product's config tree.
- Global Pi discovers both `~/.pi/agent/skills` and `~/.agents/skills`; the same frontmatter name in both is a collision.
- One installer may create links into another auto-discovered root. Resolve physical paths before deleting a “duplicate.”
- Default remains lfg. Do not silently map ask or plan semantics onto lfg.
- Disabling auto-memory does not authorize deleting transcripts, authored notes, or unrelated caches.
- A footer that drops native information or leaks timers/watchers is not complete.
- A stored goal without autonomous continuation and evidence-gated completion is only a partial implementation; label the gap.
- An installed MCP package is not necessarily enabled or loaded. Verify persisted enablement and invoke the harness's MCP status/setup control after reload.
- MCP enablement does not authorize importing server definitions or credentials from another host.
- Readwise setup is incomplete until browser OAuth and tool metadata loading succeed; a config entry alone is not completion.
- OAuth URLs, callback URLs, and authorization codes are transient secrets. Keep them out of prompts, skills, shell history, logs, and tracked files.
- Installed files alone do not prove discoverability. Run the harness's list/load check and inspect collision diagnostics.
