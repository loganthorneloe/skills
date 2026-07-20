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
   - Updates `~/.gemini/antigravity-cli/settings.json` to enable `statusLine` and set `"autoMemory": false`:
     ```json
     "statusLine": {
       "command": "<expand-home>/.gemini/antigravity-cli/statusline.py",
       "enabled": true
     },
     "autoMemory": false
     ```
   - Sets global custom instructions in `~/.gemini/antigravity-cli/rules/global_rules.md` including a strict directive to **ALWAYS ignore auto-saved memories and treat every session as a clean slate**.
   - Verifies Python 3 environment and tests `statusline.py` execution against JSON stdin.

3. **Report Status**:
   Report to the user that all skills and the statusline have been successfully installed and configured.
