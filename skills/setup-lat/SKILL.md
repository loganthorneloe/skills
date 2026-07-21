---
name: setup-lat
description: "Harness-agnostic workflow: apply LAT preferences (conciseness, no memory, ask/plan/turbo modes, /clear=fresh session) using whatever config system the current agent harness supports."
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
| 3 | **Modes: ask / plan / turbo** | Easy switch; default = **turbo** (no prompts) |
| 4 | **`/clear` = fresh session** | `/clear` starts a new/empty session (same as harness `/new` / clear-conversation). Keep native names too |
| 5 | **Document controls** | Write how to toggle modes/keys into persistent instructions |

### Mode semantics (map harness features to these names)

| Mode | Behavior |
|------|----------|
| **ask** | Full tools; confirm before mutating actions (shell, writes, edits) |
| **plan** | Read-only exploration; no file mutations; block destructive shell |
| **turbo** | Full tools; no confirmation prompts |

Ideal UX when the harness allows it:

- One hotkey to cycle modes (prefer **Shift+Tab**)
- Explicit commands/flags too (e.g. `/mode`, `/plan`, `/turbo`, CLI flags)
- In ask mode, confirmations offer: **allow once** / **deny** / **always allow** (persistent allow-list if supported)
- **Turbo on by default**; easy switch to ask/plan

Thinking / model keybinds are harness-specific QoL — only set them if the harness exposes them and the user wants defaults; do not invent conflicts with mode cycling.

### `/clear` semantics

Goal: **user types `/clear` → fresh session / wiped conversation context.**

Map to whatever the harness calls that natively (`/new`, clear conversation, new chat, etc.). Prefer aliasing or registering `/clear` via native command/keybind/extension APIs. Keep the native command working too when possible.

If `/clear` already means something else (e.g. clear TTY only), override it to mean fresh session, or ask if override is risky. If the harness cannot alias/register commands, skip and report.

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

### Step 3 — Modes (ask / plan / turbo)

1. Research native permission modes, plan mode, auto-accept, bypass-permissions, etc.
2. Map them onto ask / plan / turbo as closely as possible
3. Wire the best available toggle (hotkey and/or command/flag)
4. **Default mode = turbo** (full tools, no confirmation). Keep ask/plan available via hotkey/commands.
5. If mutable tool calls can be gated in ask mode, offer always-allow persistence when supported.
6. Document the real harness controls (not aspirational ones) in persistent instructions under `## Agent Modes` (or `## Turbo Mode` if only one switch exists)

If the harness cannot implement a mode, skip it and report the gap. Build only with native extension/plugin APIs if that is the normal way to configure *this* harness — do not drop in files meant for a different product.

### Step 4 — `/clear` = fresh session

1. Discover native session-reset / new-conversation command(s) and APIs
2. Wire `/clear` to that behavior (alias, custom slash command, keybind, or extension)
3. Prefer keeping the native command (`/new`, etc.) working as well
4. Document real reset commands in persistent instructions
5. Skip + report if unsupported

### Step 5 — Optional QoL (only if native + easy)

- Model favorites / cycle list
- Shorter skill/command aliases
- Ensure this skills repo's skills are installed for the harness

Never change default model/provider without asking.

### Step 6 — Verify and report

1. **Conciseness** — file + change
2. **Memory** — disabled / skipped; anything deleted
3. **Modes** — how to switch; default mode; allow-list if any
4. **`/clear`** — wired / skipped; native equivalent
5. **Keys/commands** — actual bindings for this harness
6. **Unable** — what could not be configured and why

Reload/restart instructions if the harness needs them.

---

## Safety

- Harness-agnostic: no hard-coded paths for a single product except what you discovered in Step 0
- Never delete outside known config/memory locations for this harness
- Never overwrite config/instruction files — merge or append
- Ask before changing an existing non-default setting
- Default mode is turbo; do not force ask-by-default
