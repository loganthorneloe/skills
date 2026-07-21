# Harness discovery (hints)

| Family | Sessions | Skills roots |
|--------|----------|--------------|
| pi | `~/.pi/agent/sessions/**/*.jsonl` | `~/.pi/agent/skills` |
| Claude Code | `~/.claude/projects/**`, `~/.claude/sessions` | `~/.claude/skills`, `.claude/skills` |
| Codex | config session/history | `.agents/skills`, Codex skills |
| Cursor | agent/chat logs if any | `.cursor/skills` |
| OpenCode | session store | OpenCode skills path |
| Gemini / Antigravity | gemini/agy sessions | `~/.gemini/**/skills`, `.agent/skills` |

Discover live: harness → search session/transcript/history/skills → mtime → recent only.
