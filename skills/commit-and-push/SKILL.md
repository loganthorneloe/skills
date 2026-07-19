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

### 1. Analyze the Working Tree
- Run `git status` to identify modified, deleted, and untracked files.
- Run `git diff` (and `git diff --cached`) to examine the exact code changes.
- Pay close attention to functional changes, new configurations, and modified imports.

### 2. Determine Commit Message Style
- Review the project history (`git log -n 5`) to check if the repository uses conventional commits (e.g., `feat:`, `fix:`, `docs:`, `chore:`).
- For all commit messages, construct the title and body according to these rules:
  1. **Title Line**: A single line under 72 characters written in the active, present tense (e.g., "Add X to Y" or "Update X to do Y"). The grammatical tense of these examples is strictly required. Do not use past tense ("Added X", "Updated X") or gerunds ("Adding X", "Updating X").
  2. **Spacing**: Exactly two line breaks (one empty line) must separate the title line from the detailed body description.
  3. **Body Details**: After the spacing, add a detailed description, bullet points, or lists outlining what changed and why, using whatever structure fits best.
- If conventional commit styling is detected (or if the repository has a `git-workflow-conventional` rule active), prepend the type to the title (e.g., `feat: Add X to Y` or `fix: Update X to do Y`). Otherwise, write the title line directly.

### 3. Verification
- Confirm that all modifications are correct and that tests have been executed.
- Ensure that you are not committing credentials, temp files, or build artifacts (check `.gitignore`).

### 4. Stage and Commit
- Stage the changes:
  ```bash
  git add .
  ```
- Commit the changes preserving the title, double line breaks, and detailed body:
  ```bash
  git commit -m "Add X to Y

  - Detail about change 1
  - Detail about change 2"
  ```

### 5. Push Changes
- Identify the current branch name (e.g., `git branch --show-current`).
- Push to the matching upstream branch:
  ```bash
  git push origin <branch-name>
  ```
