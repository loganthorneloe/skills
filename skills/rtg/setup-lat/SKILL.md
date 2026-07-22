---
name: setup-lat
description: "Harness-agnostic workflow: apply LAT preferences (conciseness, no memory, ask/plan/lfg modes, /clear=fresh session, autonomous /goal loop, compact Git status) using whatever config system the current agent harness supports."
metadata:
  opencode/slash: "true"
---

# Setup LAT (Logan Thorneloe's Agent defaults)

**Harness-agnostic preference workflow.** You are running inside some agent harness. Discover that harness's config system and apply the preferences below as far as it allows. Do not assume pi, Claude Code, Codex, or any other specific product — use your knowledge of *this* harness.

Do not ship or depend on harness-specific asset bundles. Implement preferences via the harness's native instructions, settings, permissions, keybindings, extensions, or docs.

---

## Preferences (goals)

Apply these in order. Skip only what the harness cannot support; say so explicitly.

| # | Preference | Intent |
|---|------------|--------|
| 1 | **Conciseness** | Always-on instruction: be extremely concise |
| 2 | **No auto-memory** | Disable learned/auto memory between sessions |
| 3 | **Modes: ask / plan / lfg** | Easy switch; default = **lfg** (no prompts) |
| 4 | **`/clear` = fresh session** | `/clear` starts a new/empty session (same as harness `/new` / clear-conversation). Keep native names too |
| 5 | **Autonomous `/goal` loop** | Set one visible session goal; keep running until implementation, tests, and verification succeed |
| 6 | **Compact Git status** | Show clean/dirty worktree state without adding avoidable footer height |
| 7 | **Document controls** | Write how to toggle modes/keys into persistent instructions |

### Mode semantics (map harness features to these names)

| Mode | Behavior | Indicator color |
|------|----------|-----------------|
| **ask** | Full tools; confirm before mutating actions (shell, writes, edits) | **Green** |
| **plan** | Read-only exploration; no file mutations; block destructive shell | **Red** |
| **lfg** | Full tools; no confirmation prompts | **Yellow** |

Ideal UX when the harness allows it:

- One hotkey to cycle modes (prefer **Shift+Tab**)
- Explicit commands/flags too (e.g. `/mode`, `/plan`, `/lfg`, CLI flags)
- In ask mode, confirmations offer: **allow once** / **deny** / **always allow** (persistent allow-list if supported)
- **LFG on by default**; easy switch to ask/plan
- If the harness already calls unrestricted mode `turbo`, expose `lfg` as the canonical user-facing name; retain `turbo` only as an optional compatibility alias

Thinking / model keybinds are harness-specific QoL — only set them if the harness exposes them and the user wants defaults; do not invent conflicts with mode cycling.

### `/clear` semantics

Goal: **user types `/clear` → fresh session / wiped conversation context.**

Map to whatever the harness calls that natively (`/new`, clear conversation, new chat, etc.). Prefer aliasing or registering `/clear` via native command/keybind/extension APIs. Keep the native command working too when possible.

If `/clear` already means something else (e.g. clear TTY only), override it to mean fresh session, or ask if override is risky. If the harness cannot alias/register commands, skip and report.

### Autonomous `/goal` semantics

Goal: **user types `/goal <task>` → agent starts immediately and continues autonomously until fully implemented, tested, and verified.**

Ideal UX when the harness allows it:

- `/goal <task>` sets/replaces the active session goal and starts work
- `/goal` or `/goal show` displays it; `/goal clear` stops the loop
- Show a concise goal in the footer/status area while active
- Persist goal state within the session and restore the correct state when branching/resuming
- Inject the active goal into each turn
- When the agent settles without completion, enqueue another continuation automatically
- Provide an explicit model completion action requiring a summary and concrete verification evidence; expose it to the model only while a goal is active, and stop only after that action or `/goal clear`

Use native loop/task/extension APIs. Avoid external polling processes. If the harness cannot register commands, completion actions, or follow-up turns, implement the closest safe approximation and report the gap. Warn that autonomous loops can make repeated model calls and incur cost.

### Compact Git status semantics

When the current directory is inside a Git repository, show a compact worktree indicator:

- `git ✓` — clean
- `git +2 ~1 ?3 !1` — staged, unstaged, untracked, conflicts
- Right-align it beneath the model indicator when the harness supports custom footer layout
- Otherwise place it compactly in an existing single-line status/footer area
- Preserve native footer information and other extension statuses
- Hide it outside Git repositories
- Refresh after mutation tools and external changes; prefer native file/Git events, otherwise use a lightweight session-scoped interval and clean it up on shutdown
- Do not add a dedicated vertical line when it can share an existing one

---

## Workflow

### Step 0 — Identify the harness

1. Name the harness you are running in
2. List paths/files for: persistent instructions, settings, memory, permissions/modes, keybindings, extensions/plugins, custom commands
3. If unsure, ask the user
4. If the harness can register this skill as a command, do so

Report findings before changing anything.

### Step 1 — Conciseness

Add this exact line under a `## Rules` heading in the harness's persistent instruction file (global scope preferred):

```
Be EXTREMELY concise. Sacrifice grammatical correctness in favor of conciseness ALWAYS.
```

- Append/merge only — never overwrite existing instruction content
- Use always-on / always-apply if the harness has rule activation modes
- Create the file only if the harness expects one and it is missing

### Step 2 — Disable auto-memory

1. Check for auto-memory / learned-memory / continuous-memory features
2. If present: disable via settings (and env vars if supported); delete existing memory stores for that feature
3. If absent: skip
4. Do **not** delete ordinary session transcripts unless the user asks

### Step 3 — Modes (ask / plan / lfg)

1. Research native permission modes, plan mode, auto-accept, bypass-permissions, etc.
2. Map them onto ask / plan / lfg as closely as possible
3. Wire the best available toggle (hotkey and/or command/flag)
4. **Default mode = lfg** (full tools, no confirmation). Keep ask/plan available via hotkey/commands.
5. Color mode indicators consistently: **ask = green**, **plan = red**, **lfg = yellow**.
6. If mutable tool calls can be gated in ask mode, offer always-allow persistence when supported.
7. Document the real harness controls (not aspirational ones) in persistent instructions under `## Agent Modes` (or `## LFG Mode` if only one switch exists)

If the harness cannot implement a mode, skip it and report the gap. Build only with native extension/plugin APIs if that is the normal way to configure *this* harness — do not drop in files meant for a different product.

### Step 4 — `/clear` = fresh session

1. Discover native session-reset / new-conversation command(s) and APIs
2. Wire `/clear` to that behavior (alias, custom slash command, keybind, or extension)
3. Prefer keeping the native command (`/new`, etc.) working as well
4. Document real reset commands in persistent instructions
5. Skip + report if unsupported

### Step 5 — Autonomous `/goal` loop

1. Discover native commands, durable session state, turn hooks, model-callable completion actions, and footer/status UI
2. Wire `/goal <task>` to store the goal and start work immediately
3. Keep issuing continuation turns whenever the agent settles while the goal remains active
4. Let the model complete the loop only through an explicit completion action containing a summary and concrete test/verification evidence; keep that action hidden/disabled when no goal is active
5. Add `/goal`/`/goal show` and `/goal clear`; show a concise active goal in footer/status UI when available
6. Restore branch/session state correctly; a new goal replaces the old one
7. Document controls and repeated-call/cost behavior

Do not use a harness-specific implementation in another harness. Skip unsupported pieces and report exact gaps.

### Step 6 — Compact Git status

1. Discover native Git state, footer/status, and custom layout APIs
2. Add the compact clean/dirty indicator described above
3. Prefer right alignment beneath model information without replacing or dropping native footer data
4. Refresh promptly after writes/edits/shell mutations and eventually after external changes
5. Keep watchers/timers session-scoped and clean them up on reload, session switch, and shutdown
6. If custom alignment is unsupported, use the existing status line; skip + report if no compact status surface exists

### Step 7 — Optional QoL (only if native + easy)

- Model favorites / cycle list
- Shorter skill/command aliases
- Ensure this skills repo's skills are installed for the harness

Never change default model/provider without asking.

### Step 8 — Verify and report

1. **Conciseness** — file + change
2. **Memory** — disabled / skipped; anything deleted
3. **Modes** — how to switch; default mode; allow-list if any
4. **`/clear`** — wired / skipped; native equivalent
5. **`/goal`** — set/show/clear, continuation behavior, completion gate, persistence, footer/status
6. **Git status** — clean/dirty formats, placement, refresh behavior, non-repo behavior
7. **Keys/commands** — actual bindings for this harness
8. **Unable** — what could not be configured and why

Reload/restart instructions if the harness needs them.

---

## Safety

- Harness-agnostic: no hard-coded paths for a single product except what you discovered in Step 0
- Never delete outside known config/memory locations for this harness
- Never overwrite config/instruction files — merge or append
- Ask before changing an existing non-default setting
- Default mode is lfg; do not force ask-by-default
