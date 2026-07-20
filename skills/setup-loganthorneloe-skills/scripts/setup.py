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

    # 1.5 Auto-symlink all skills from repo into ~/.gemini/config/skills/
    skills_repo_dir = os.path.dirname(skill_root)
    config_skills_dir = os.path.expanduser("~/.gemini/config/skills")
    os.makedirs(config_skills_dir, exist_ok=True)
    if os.path.exists(skills_repo_dir):
        for item in os.listdir(skills_repo_dir):
            item_path = os.path.join(skills_repo_dir, item)
            if os.path.isdir(item_path) and os.path.exists(os.path.join(item_path, "SKILL.md")):
                target_link = os.path.join(config_skills_dir, item)
                try:
                    if os.path.lexists(target_link):
                        os.remove(target_link)
                    os.symlink(item_path, target_link)
                    print(f"🔗 Auto-symlinked skill: {item} -> {target_link}")
                except Exception as e:
                    print(f"⚠️ Could not symlink {item}: {e}")

    # 2. Update settings.json with user preferences
    settings = {}
    if os.path.exists(settings_file):
        try:
            with open(settings_file, "r") as f:
                settings = json.load(f)
        except Exception as e:
            print(f"⚠️ Could not parse existing settings.json ({e}), initializing new settings dictionary.")

    # Apply preferences
    settings["model"] = "Gemini 3.5 Flash (High)"
    settings["scheduledTasksEnabled"] = True
    settings["autoMemory"] = False
    
    # Ensure standard allowed commands (including all non-mutating info gathering commands)
    permissions = settings.get("permissions", {})
    allow_list = set(permissions.get("allow", []))
    default_allowed = [
        # Basic File Inspection & Viewing
        "command(cat)", "command(head)", "command(tail)", "command(less)", "command(more)",
        "command(file)", "command(stat)", "command(wc)", "command(diff)", "command(cmp)",
        "command(md5)", "command(md5sum)", "command(sha1sum)", "command(sha256sum)",
        "command(hexdump)", "command(xxd)", "command(strings)", "command(od)",

        # Directory & File Search / Listing
        "command(ls)", "command(pwd)", "command(tree)", "command(find)", "command(fd)",
        "command(grep)", "command(rg)", "command(ripgrep)", "command(ag)", "command(ack)",
        "command(which)", "command(whereis)", "command(type)", "command(locate)",

        # Text Processing & Parsing (Read Ops)
        "command(awk)", "command(sed)", "command(jq)", "command(yq)", "command(cut)",
        "command(sort)", "command(uniq)", "command(tr)", "command(column)", "command(fmt)", "command(nl)",

        # System Information & Resource Monitoring
        "command(whoami)", "command(id)", "command(uname)", "command(hostname)", "command(uptime)",
        "command(date)", "command(env)", "command(printenv)", "command(df)", "command(du)",
        "command(free)", "command(ps)", "command(top)", "command(htop)", "command(lsof)",
        "command(vm_stat)", "command(sw_vers)", "command(sysctl)", "command(system_profiler)",
        "command(ulimit)", "command(arch)", "command(swapon)", "command(iostat)",

        # Network Diagnostics & Inspection
        "command(netstat)", "command(ss)", "command(ifconfig)", "command(ip)", "command(ping)",
        "command(traceroute)", "command(dig)", "command(nslookup)", "command(host)", "command(arp)", "command(route)",

        # Git Information Gathering (Read-Only Subcommands)
        "command(git status)", "command(git diff)", "command(git log)", "command(git show)",
        "command(git branch)", "command(git tag)", "command(git remote)", "command(git blame)",
        "command(git stash list)", "command(git rev-parse)", "command(git config)", "command(git describe)",
        "command(git ls-files)", "command(git ls-tree)", "command(git ls-remote)", "command(git shortlog)", "command(git reflog)",

        # Development & Runtime Environment Queries
        "command(node -v)", "command(node --version)", "command(npm -v)", "command(npm list)", "command(npm view)",
        "command(python --version)", "command(python3 --version)", "command(pip list)", "command(pip show)",
        "command(cargo --version)", "command(rustc --version)", "command(go version)", "command(java -version)",
        "command(docker ps)", "command(docker images)", "command(docker info)", "command(docker inspect)",
        "command(kubectl get)", "command(kubectl describe)",

        # Utility
        "command(cp)", "command(pytest)"
    ]
    allow_list.update(default_allowed)
    permissions["allow"] = sorted(list(allow_list))
    settings["permissions"] = permissions

    settings["statusLine"] = {
        "command": target_statusline,
        "enabled": True
    }

    settings["enableTerminalSandbox"] = False

    # Trusted workspaces
    trusted = set(settings.get("trustedWorkspaces", []))
    trusted.update(["/Users/loganthorneloe/src", "/Users/loganthorneloe/src/daily-email"])
    settings["trustedWorkspaces"] = sorted(list(trusted))

    with open(settings_file, "w") as f:
        json.dump(settings, f, indent=2)

    print(f"⚙️ Configured settings.json in {settings_file}")

    # 3. Setup Custom Instructions / Global Rules in ~/.gemini/GEMINI.md
    global_rules_file = os.path.expanduser("~/.gemini/GEMINI.md")
    default_rules = """# Global Custom Instructions & Agent Rules

## Rule Location Standards
- **Global Preferences & Instructions**: MUST ONLY be saved to `~/.gemini/GEMINI.md`. NEVER create, edit, or split rules into secondary files such as `global_rules.md` or subfolder instruction files.
- **Project-Specific Instructions**: MUST ONLY be placed in `<repository-root>/GEMINI.md`.

## User Preferences & Behavior Rules
- Be EXTREMELY concise. Sacrifice grammatical correctness in favor of conciseness ALWAYS.
- Maintain accurate file links and documentation references (`file://` URLs).
- NEVER use inline Python scripts or terminal commands (e.g. `python3 -c`) to edit or modify files. ALWAYS use explicit file editing tools (`replace_file_content`, `multi_replace_file_content`, `write_to_file`) so all line additions and subtractions are fully visible.
- If user asks a question, ANSWER FIRST. Do not invoke tools or run actions unless explicitly requested.
- BEFORE calling tools or executing actions, ALWAYS explain what is being done and why first.
"""
    with open(global_rules_file, "w") as f:
        f.write(default_rules)
    print(f"📝 Configured global custom instructions in {global_rules_file}")

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
