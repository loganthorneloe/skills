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
- If conventional commit styling is detected (or if the repository has a `git-workflow-conventional` rule active), construct the message as:
  ```text
  <type>: <short summary>

  [Optional body explaining the rationale behind major changes]
  ```
- If the repository has a plain descriptive style, use a concise, imperative sentence (e.g., "Implement database connections and add tests") under 72 characters.

### 3. Verification
- Confirm that all modifications are correct and that tests have been executed.
- Ensure that you are not committing credentials, temp files, or build artifacts (check `.gitignore`).

### 4. Stage and Commit
- Stage the changes:
  ```bash
  git add .
  ```
- Commit the changes with the generated message:
  ```bash
  git commit -m "<title>"
  ```
  *(Include a multi-line message with `-m` if there are multiple separate changes to document.)*

### 5. Push Changes
- Identify the current branch name (e.g., `git branch --show-current`).
- Push to the matching upstream branch:
  ```bash
  git push origin <branch-name>
  ```
