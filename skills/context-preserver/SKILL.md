---
name: context-preserver
description: Automates project state preservation by documenting key design decisions, updating CLAUDE.md/AGENTS.md files, and maintaining task audit logs.
---

# Context & Documentation Preservation Skill

This skill ensures that task history, project state, and design rationale are saved locally within the codebase, preventing context loss during session restarts or environment handoffs.

## When to Use
- Concluding a chat session or reaching a major task milestone.
- Changing or introducing new dependencies, scripts, or runtime patterns.
- Updating codebase architecture or configuration interfaces.

## Guidelines & Rules

### 1. Guideline File Upkeep (`CLAUDE.md` and `AGENTS.md`)
- If a project uses `CLAUDE.md` or `AGENTS.md`, keep these files updated with any new setups, commands, or architecture details.
- When introducing a new package or configuration requirement, immediately add it to the quickstart or system dependencies section.

### 2. State & Task Progress Tracking
- Use dedicated markdown files (like progress sheets or artifact logs) to maintain task status lists.
- For pipelines or scripts that process data, maintain a local audit log (such as a triage decision trail) to record choices, runs, and validation outcomes.

### 3. Handoff Readiness
- Write status and rationale down in files. Never expect subsequent agents or future conversation sessions to retain chat message context.
- Before ending your turn, write a brief overview of changes, remaining tasks, and next steps to a tracking file.
