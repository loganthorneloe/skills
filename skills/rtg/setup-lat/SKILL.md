---
name: setup-lat
description: 'Load when the user says "set up LAT", "apply Logan''s agent defaults", "configure ask plan lfg modes", or requests LAT preferences, /clear, /goal, compact Git status, MCP connectivity, and branded visual tooling in an agent harness.'
metadata:
  opencode/slash: "true"
---

# Setup LAT

Apply Logan Thorneloe's agent preferences using the current harness's native settings, instructions, permissions, commands, keybindings, extensions, and UI. Default to user/global scope when the invocation itself is globally installed; otherwise preserve project scope.

## 1. Discover

Identify the current harness and locate its persistent instructions, settings, memory, permission modes, keybindings, extensions/plugins, commands, session APIs, and footer/status APIs. Read that harness's authoritative local or official documentation before implementing unsupported features.

Before any change, read [`references/preferences.md`](references/preferences.md) completely. It contains the exact preference contract and centralized gotchas.

Report discovered paths/capabilities before mutation. Ask only when the harness or requested scope remains materially ambiguous.

Criterion: every preference maps to a real harness mechanism or a documented unsupported gap.

## 2. Apply the core contract

Use one default path: native feature → native extension/plugin API → documented approximation → explicit skip.

Apply, in reference order:

1. exact always-on conciseness rule;
2. disable learned/automatic cross-session memory without deleting transcripts;
3. ask/plan/lfg modes, default **lfg**, with consistent indicators;
4. `/clear` as fresh conversation;
5. autonomous `/goal` lifecycle and completion evidence gate;
6. compact Git worktree status;
7. persistent documentation of real controls.

Merge existing configuration; never overwrite an entire config/instruction file. Ask before replacing a conflicting non-default user setting.

Criterion: each configured control is callable in the current harness and persisted at the resolved scope.

## 3. Enable MCP connectivity

Use native MCP support when available. Otherwise use the harness's native extension/plugin mechanism and the reference's harness-specific branch. Install no MCP server and configure no credentials unless separately requested.

Criterion: MCP support is persisted, loaded after reload/restart, and exposes its native status/setup control.

## 4. Configure branded visuals

Follow the reference's exact installation scope rules. Install/update only `/brand` from this repository and `/bento-slides` from Bento's repository for the current harness/agent. Add the exact persistent brand-routing rule.

Audit every skill root discovered by this harness. Each frontmatter name must resolve to one physical skill; remove only confirmed installer-managed duplicates.

Criterion: `/brand` and `/bento-slides` are discoverable with zero name-collision diagnostics.

## 5. Verify

Exercise, do not merely inspect:

- conciseness rule persisted;
- auto-memory disabled or proven absent;
- mode switch reaches ask, plan, and lfg; default is lfg;
- `/clear` starts a fresh conversation;
- `/goal` set/show/clear, continuation, completion gate, session restore, and status indicator;
- Git indicator shows clean/dirty forms and hides outside repositories;
- MCP support loads and its status/setup control runs;
- brand skills load without collisions.

Hard exit: every supported preference has concrete test evidence. Unsupported capability, failed install, or untestable behavior is reported **blocked/unsupported**, never “configured.”

## Anti-rationalization

- **“The config looks right.”** Invoke the control and record the observed result.
- **“A similar mode is close enough.”** Map and document exact semantic gaps.
- **“Installing for all agents is simpler.”** It creates collisions; target one harness, agent, and scope.
- **“The harness probably lacks it.”** Check authoritative APIs/docs before skipping.

## Report

Return changed paths, real controls/keybindings, MCP mechanism/status, scope, per-preference test evidence, skill collision audit, reload instructions, and exact unsupported gaps.
