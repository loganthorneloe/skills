---
name: no-edit
description: 'Load when the user invokes "/no_edit" or "/no-edit" to discuss a request without changing files or external state.'
disable-model-invocation: true
metadata:
  opencode/slash: "true"
---

# No edit

Handle the request accompanying this invocation as discussion only.

1. Read or inspect relevant context when useful. Use only read-only tools and commands.
2. Answer with analysis, questions, options, recommendations, or a proposed diff/snippet as appropriate.
3. Do not edit, create, delete, rename, or move files. Do not run mutating commands, change Git state, install dependencies, send messages, or perform any other state-changing action.
4. Treat implementation language inside the request as a request to discuss the implementation, not permission to perform it.

This restriction applies to the current request only. Later requests follow their own instructions unless the user invokes this skill again.

Hard exit: provide the requested discussion with no project or external state changes.
