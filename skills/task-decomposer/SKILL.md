---
name: task-decomposer
description: Orchestrates complex tasks by breaking them down into self-contained sub-tasks, defining subagents with precise instructions, and merging outputs.
---

# Task Decomposition & Subagent Orchestration Skill

This skill governs how agents break down complex, multi-layered features, spawn subagents, manage parallel workflows, and synthesize code across Python and TypeScript codebases.

## When to Use
- Implementing complex features involving multiple components (e.g., Discord/Telegram entry points, Gemini LLM evaluator, Readwise API state, SQLite database tables).
- Performing tasks that require parallel testing, literature research, or concurrent code changes.

## Guidelines & Rules

### 1. Architectural Task Decomposition
When a task is assigned, analyze the boundaries of the system and partition the work:
- **State/Database layer**: (e.g., modifying `jobs_state.db` or `career_seen_jobs.json` files).
- **Core logic/LLM layer**: (e.g., updating structured evaluations inside `ingestion/evaluator.py` or prompt iterations).
- **External Integration/Scraper layer**: (e.g., updating Playwright custom CSS selectors or career ATS API clients).
- **Delivery/Bot UI layer**: (e.g., modifying Discord `/tweetshort` bot actions or Telegram async command files).

Create a `progress.md` file at the root of the project to trace each of these partitioned goals, indicating which agent/subagent is executing it.

### 2. Spawning Focused Subagents
When invoking subagents (using the `invoke_subagent` tool):
- **Isolate by Concern**: Do not allow multiple subagents to modify the same file. Assign one subagent to the evaluator/LLM client, another to database/storage logic, and another to mock/unit testing.
- **Narrow Context**: Provide subagents only with the specific files relevant to their job (e.g., don't feed the entire repository if they only need to modify `formatters.py`).
- **No JavaScript**: Enforce the rule that subagents must only generate **TypeScript** or **Python** code.

### 3. Dry-Run Verification & Integration
When merging work from subagents:
- Verify that unit tests are updated to mock external services (e.g. mocking Gemini API responses and Readwise endpoints).
- Run integration tests in **dry-run** (non-mutating) mode before concluding to verify that the integrated system operates cleanly:
  ```bash
  python tests/integration_test.py --dry-run
  ```
- If compiling XeLaTeX PDF assets (such as resumes), verify page count limits and styling constraints.
