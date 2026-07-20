---
name: commit-and-push
description: Automatically stages, commits, and pushes recent changes with a descriptive conventional commit message by analyzing the exact changes made.
---

# Commit and Push Skill

This skill automates the process of identifying changes in the working directory, writing a descriptive commit message based on the diffs, staging the changes, committing them, and pushing to the remote repository.

## When to Use
- You are explicitly asked to "commit and push" changes.
- A feature or fix is complete and ready to be synchronized with the remote branch.

## Procedure

1. **Analyze Working Tree**: Run `git status`, `git diff`, and `git diff --cached` to identify modified/untracked files and code changes.
2. **Determine Commit Message Style**: Review `git log -n 5` for conventions (`feat:`, `fix:`, `docs:`, etc.).
   - Title: Single line under 72 chars, active present tense ("Add X", "Update Y").
   - Spacing: Exactly two line breaks (one empty line).
   - Body: Detailed bullet points of changes.
3. **Stage, Commit & Push**:
   - Stage modified/untracked files: `git add .`
   - Commit: `git commit -m "<title>\n\n<body>"`
   - Push: `git push origin <current-branch>`

