---
name: setup-lat
description: "Configures a new agent harness with productivity defaults: conciseness rule, memory disabled, and documents turbo/auto-accept toggle. Run once on first use of any harness."
metadata:
  opencode/slash: "true"
---

# Setup LAT (Logan Thorneloe's Agent defaults)

One-time setup for any agent harness. You are the harness — use your own knowledge of your config system to apply three productivity defaults.

---

## Step 0: Identify Your Harness

Before doing anything, identify which harness you are running in:

1. Name the harness (e.g. "OpenCode", "Claude Code", "Gemini CLI", "Aider", etc.)
2. List the config paths/files your harness uses for persistent instructions, memory, and permissions
3. If you are unsure which harness you are, ask the user
4. If the harness supports it, attempt to register this skill as a slash command (e.g. `/setup-lat`).

Report your findings before proceeding.

---

## Step 1: Conciseness Rule
...

Add this exact line to your instruction/config file:

```
Be EXTREMELY concise. Sacrifice grammatical correctness in favor of conciseness ALWAYS.
```

### What to do

1. Identify where your harness reads persistent instructions (e.g. project-level instruction files, rules directories, settings).
2. If a file already exists, append the rule under a `## Rules` heading. Never overwrite existing content.
3. If creating a new file, use whatever filename your harness expects for project-level instructions.
4. If your harness uses a rules system with activation modes (always-apply vs conditional), set this rule to always apply.

---

## Step 2: Disable Memory

Harness memory (auto-memory, learned conventions, session history) causes inconsistent behavior across sessions. Disable it and delete existing memory files.

### What to do

1. Research whether your harness has an auto-memory or learned-memory feature that writes persistent notes between sessions.
2. If it does:
   - Find the setting that disables it and set it.
   - If your harness supports environment variables in its settings, set the disable flag there too.
   - Delete any existing memory directories/files so old learned behavior doesn't persist.
3. If it doesn't, skip this step.

---

## Step 3: Turbo Mode (Auto-Accept)

Document how to enable auto-approve so the user can toggle it when needed. **Do NOT enable turbo mode by default.** The goal is to make it easy to activate, not to have it always on.

### What to do

1. Research whether your harness has a permission mode or auto-accept setting that controls whether the agent asks before executing tool calls (file writes, shell commands, edits).
2. If it does:
   - Find the most permissive mode available (e.g. `--auto` flag, "bypass permissions", "auto-accept", "dont-ask", "turbo").
   - **Do NOT enable it by default in config files.** Leave the default permission mode as-is (prompting/ask).
   - If it uses a CLI flag (e.g. `--auto`), document the flag in the instruction file under a `## Turbo Mode` section so the user can invoke it when desired.
   - If it uses a config setting, document how to toggle it but leave it off.
3. If it doesn't, skip this step.

---

## Verification

After applying all three steps, report what was configured:

1. **Conciseness**: Which file was created/modified and what was added.
2. **Memory**: Whether memory was disabled or skipped. List deleted memory directories if any.
3. **Turbo**: Documented how to toggle turbo mode, or that it was skipped.

If any step failed (file not writable, directory not found, setting doesn't exist), report the error and continue with remaining steps. After all steps complete, explicitly tell the user what you were UNABLE to configure and why.

---

## Safety

- Never delete files outside the harness's known config/memory directories.
- Never overwrite existing config files — always merge or append.
- If a setting already has a value, ask the user before changing it.
