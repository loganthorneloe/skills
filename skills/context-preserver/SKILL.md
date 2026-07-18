---
name: context-preserver
description: Automates project state preservation by keeping CLAUDE.md/AGENTS.md files in sync and logging key design choices in python/typescript workspaces.
---

# Context & Documentation Preservation Skill

This skill ensures that task history, project commands, and architectural rules are maintained locally in the repository, making it easy for subsequent agent sessions to resume work without starting from scratch.

## When to Use
- Concluding a task, reaching a milestone, or preparing to end a session.
- Modifying project dependencies (`requirements.txt`, `package.json`), environment variables, or setup steps.
- Introducing new scripts, modules, or services.

## Guidelines & Rules

### 1. Enforcing CLAUDE.md & AGENTS.md Layout
Whenever you modify or inspect a workspace project, check for a `CLAUDE.md` or `AGENTS.md` file. If they exist, you must keep them in sync. Follow this strict layout standard:

- **What This Is / Project Overview**: Summary of the project, LLM usages, and bounds.
- **Commands**: Accurate setup (`python -m venv .venv`, `source .venv/bin/activate`, `pip install`), running (`python bot/main.py --dry-run`), and testing commands (`python -m pytest -v`, `pytest tests/test_evaluator.py`).
- **Architecture**: A file-by-file or directory map showing entry points (e.g. `core/engine.py` orchestrator, `ingestion/evaluator.py` classifier).
- **Key Patterns**: Coding patterns (e.g., async-first, LLM as filter/bouncer, personalized jobs radar constraints, no-hallucination XeLaTeX margins, single-page page limits).
- **Environment Variables**: Listing all required (`READWISE_API_KEY`, `GEMINI_API_KEY`, etc.) and optional variables.
- **System Dependencies**: Target runtimes (Python 3.11+, Playwright Chromium, etc.).

If you introduce any new command, library, or architectural changes, immediately update these files.

### 2. Audit Trails & Run Decisions
When building features that involve evaluation, triage, or content decisions (such as Readwise filters):
- Ensure there is a bottom audit trail pattern: log choices under `Included` and `Filtered Out` categories with clear, plain-English reasons (avoiding developer/system IDs).
- Write details of any pipeline runs or batch execution outcomes directly to a local log or output markdown file (e.g., `daily_output.md`) for visibility.

### 3. Handoff Documentation
- Do not rely on chat history. When completing a task, write a summary block at the bottom of the relevant project walkthrough or document.
- Ensure that any scripts generated are strictly in **TypeScript** or **Python** (no raw JavaScript).
