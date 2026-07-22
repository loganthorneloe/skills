---
name: commit-and-push
description: Automatically inspects and updates affected READMEs, stages, commits, and pushes recent changes with conventional commit messages.
metadata:
  opencode/slash: "true"
---

# Commit and Push Skill

This skill automates the process of identifying changes in the working directory, writing a descriptive commit message based on the diffs, staging the changes, committing them, and pushing to the remote repository.

## When to Use
- You are explicitly asked to "commit and push" changes.
- A feature or fix is complete and ready to be synchronized with the remote branch.

## Procedure

1. **Analyze Working Tree**: Run `git status`, `git diff`, and `git diff --cached` to identify modified, untracked, or deleted files and code changes.
2. **Inspect & Update Relevant READMEs**:
   - Identify the directory paths of all modified/added/deleted files.
   - Inspect relevant `README.md` files in those modified file directories and parent directories up to the repository root.
   - Do NOT inspect or edit `README.md` files in untouched, unrelated directories.
   - If the code changes alter features, skill lists, CLI commands, setup procedures, or repo structure, update the affected `README.md` file(s) so documentation stays synchronized with code changes.
3. **Determine Commit Message Style**: Review `git log -n 5` for conventions (`feat:`, `fix:`, `docs:`, etc.).
   - Title: Single line under 72 chars, active present tense ("Add X", "Update Y").
   - Spacing: Exactly two line breaks (one empty line).
   - Body: Detailed bullet points of changes.
4. **Stage, Commit & Push**:
   - Stage modified/untracked/updated files: `git add .`
   - Commit: `git commit -m "<title>\n\n<body>"`
   - Push: `git push origin <current-branch>`

