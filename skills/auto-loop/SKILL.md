---
name: auto-loop
description: Executes an autonomous continuous development loop (plan, implement, test, debug, verify) until the project goal is 100% complete without stopping prematurely. Enables continuous auto-execution and recommends Turbo Mode.
---

# Auto-Loop & Continuous Completion Skill

This skill governs continuous, self-directed development until a specified feature or project goal is fully implemented, tested, and verified.

## 1. Operating Principles

1. **Continuous Execution**: Work autonomously through the full lifecycle—planning, coding, testing, debugging, and verifying—without yielding back to the user between intermediate steps.
2. **Self-Correction & Debugging**: If a test, build, lint, or runtime execution fails, do NOT stop to ask the user how to fix it. Analyze error outputs, inspect stack traces, apply fixes, and re-run tests immediately.
3. **No Early Yielding**: Never stop after merely drafting or editing code with messages like *"I have updated the code, would you like me to run tests?"*. Run the tests yourself and iterate until they pass.
4. **Language Constraints**: Ensure all written code strictly adheres to project rules (use **TypeScript** or **Python**; never use plain JavaScript).

---

## 2. Autonomous Loop Workflow

Follow this cycle until all task requirements are satisfied:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Plan & Track (Update progress.md)                        │
└──────────────┬──────────────────────────────────────────────┘
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. Implement Changes (TypeScript / Python)                  │
└──────────────┬──────────────────────────────────────────────┘
               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. Execute Tests & Linting                                  │
└──────────────┬──────────────────────────────────────────────┘
               ▼
       Does it pass cleanly?
       ├───── YES ─────► Are all requirements done?
       │                    ├───── YES ──► 5. Final Verification & Conclude
       │                    └───── NO ───► Loop back to Step 1
       │
       └───── NO  ─────► 4. Analyze Errors & Debug (Loop back to Step 2)
```

### Step 1: Goal Breakdown & Progress Tracking
- Create or update `progress.md` at the project root with concrete checklist items.
- Mark items as `[ ] Pending`, `[-] In Progress`, or `[x] Completed`.

### Step 2: Implementation
- Write modular, clean TypeScript or Python code.
- Avoid introducing stubbed or placeholder implementations.

### Step 3: Automated Verification
- Run relevant build, linting, and test commands:
  - Python: `pytest`, `mypy`, `ruff`, etc.
  - TypeScript: `npm test`, `npx tsc --noEmit`, etc.

### Step 4: Autonomous Debugging Loop
- If any test or command fails:
  1. Read full error logs and stack traces.
  2. Locate root causes in code.
  3. Apply code fixes.
  4. Immediately re-run tests.
  5. Repeat until 0 failures remain.

### Step 5: Final Conclusion
- Only return final output to the user when:
  - All checklist items in `progress.md` are marked `[x]`.
  - All unit/integration tests pass cleanly.
  - Build/type checks succeed with 0 errors.

---

## 3. Enabling Turbo / Auto-Approve Mode

To ensure the loop runs seamlessly without waiting for user permission on individual tool calls:

- **CLI Mode**: Run `agy --turbo` or activate `/turbo` mode in the CLI session.
- **IDE / UI Mode**: Enable "Auto-Approve" / "Turbo Mode" in settings or approve broad permission requests upfront.
- **Agent Permission Strategy**: If permission prompts occur, request permission with the broadest necessary scope (e.g. workspace directory read/write) so execution proceeds uninterrupted.
