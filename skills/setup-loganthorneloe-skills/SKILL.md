---
name: setup-loganthorneloe-skills
description: Sets up and configures the loganthorneloe/skills environment. Automatically installs the custom statusline script, configures settings.json, and verifies all skills.
---

# Setup Logan Thorneloe Skills (`/setup-loganthorneloe-skills`)

When this skill is invoked (or when the user runs `/setup-loganthorneloe-skills`), perform the complete setup for `loganthorneloe/skills`.

## Setup Procedure

1. **Run Setup Script**:
   Execute the automated Python setup script located at `scripts/setup.py` within this skill directory:
   ```bash
   python3 scripts/setup.py
   ```

2. **Setup Tasks Performed by `setup.py`**:
   - Copies `statusline.py` to `~/.gemini/antigravity-cli/statusline.py`.
   - Makes `statusline.py` executable (`chmod +x`).
   - Updates `~/.gemini/antigravity-cli/settings.json` to enable `statusLine`, set `"autoMemory": false`, and automatically set all non-mutating common bash commands used for information gathering (file viewing, searching, text processing, system info, network diagnostics, git read ops, runtime versions) to `ALWAYS ALLOW`.
   - Sets global custom instructions in `~/.gemini/GEMINI.md` including strict directives for rule location standards, extreme conciseness, forbidding inline Python script file edits, answering questions first before tools, and explaining actions before execution.
   - Verifies Python 3 environment and tests `statusline.py` execution against JSON stdin.

3. **Report Status**:
   Report to the user that all skills, permission rules for non-mutating commands, and the statusline have been successfully installed and configured.
