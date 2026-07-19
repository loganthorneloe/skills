#!/usr/bin/env python3
"""
Setup script for loganthorneloe/skills.
Installs and configures custom statusline script and settings for Antigravity CLI (agy).
"""
import os
import sys
import json
import shutil
import subprocess

def main():
    print("🚀 Running loganthorneloe/skills environment setup...")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_root = os.path.dirname(script_dir)
    res_statusline = os.path.join(skill_root, "resources", "statusline.py")

    gemini_dir = os.path.expanduser("~/.gemini/antigravity-cli")
    target_statusline = os.path.join(gemini_dir, "statusline.py")
    settings_file = os.path.join(gemini_dir, "settings.json")

    os.makedirs(gemini_dir, exist_ok=True)

    # 1. Install statusline.py
    if os.path.exists(res_statusline):
        print(f"📦 Copying statusline script to {target_statusline}...")
        shutil.copy2(res_statusline, target_statusline)
    else:
        print(f"⚠️ Warning: Could not find resource file at {res_statusline}")
        return

    # Make statusline.py executable
    os.chmod(target_statusline, 0o755)

    # 2. Update settings.json
    settings = {}
    if os.path.exists(settings_file):
        try:
            with open(settings_file, "r") as f:
                settings = json.load(f)
        except Exception as e:
            print(f"⚠️ Could not parse existing settings.json ({e}), initializing new settings dictionary.")

    settings["statusLine"] = {
        "command": target_statusline,
        "enabled": True
    }

    with open(settings_file, "w") as f:
        json.dump(settings, f, indent=2)

    print(f"⚙️ Configured statusLine in {settings_file}")

    # 3. Test verification
    print("🧪 Verifying statusline script execution...")
    test_json = json.dumps({
        "context_window": {
            "total_input_tokens": 1000,
            "total_output_tokens": 500,
            "context_window_size": 200000
        },
        "model": {"display_name": "Setup-Check"},
        "agent_state": "idle"
    })

    try:
        proc = subprocess.run(
            [sys.executable, target_statusline],
            input=test_json,
            text=True,
            capture_output=True,
            check=True
        )
        print(f"✅ Statusline verification output: {proc.stdout.strip()}")
    except Exception as e:
        print(f"❌ Error verifying statusline script: {e}")
        sys.exit(1)

    print("\n🎉 Setup complete! All skills and the statusline are fully configured for your AGY CLI.")

if __name__ == "__main__":
    main()
