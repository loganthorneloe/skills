---
name: commit-and-push
description: 'Load when the user says "commit and push", "ship these changes", "push my changes", or asks to commit the current worktree and synchronize it with Git remote.'
metadata:
  opencode/slash: "true"
---

# Commit and push

Commit the intended worktree changes and push the current branch. Default: include all changes belonging to the completed task, use the repository's convention, and push to the configured upstream.

## 1. Inspect

Run:

```bash
git status --short --branch
git diff
git diff --cached
git log -n 5 --oneline
```

Identify intended files, unrelated pre-existing changes, secrets, generated artifacts, and the current branch/upstream. Never discard user changes. Ask before staging only when ownership is genuinely ambiguous or sensitive material appears.

Criterion: every file to stage is understood and belongs in this commit.

## 2. Synchronize documentation

Inspect `README.md` files in changed directories and their parents up to the repository root. Update only documentation affected by changed features, commands, setup, structure, or skill lists.

Criterion: docs describe the post-commit state; unrelated READMEs remain untouched.

## 3. Check and stage

Run available checks relevant to the changed files plus:

```bash
git diff --check
git add <intended-paths>
git diff --cached --check
git diff --cached --stat
git diff --cached
```

Use explicit paths by default. If the staged diff is empty, stop and report that there is nothing to commit.

Criterion: staged diff contains exactly the intended, checked change.

## 4. Commit

Match `git log` conventions. Default message:

- conventional title, active voice, ≤72 characters
- blank line
- concise bullets describing material changes

Commit without rewriting existing history unless the user explicitly requests it. Capture the resulting commit hash.

Criterion: `git show --stat --oneline HEAD` matches the staged intent.

## 5. Push and prove

Push the current branch to its upstream. If none exists, default to `origin` and set upstream:

```bash
git push -u origin <current-branch>
```

Then run `git status --short --branch`. Hard exit: push succeeds and local HEAD is synchronized with its upstream. Authentication, hooks, rejected updates, or conflicts mean **blocked**, not complete.

## Gotchas

- A clean working tree does not prove the remote received the commit; require successful push output and synchronized status.
- Do not stage unrelated files merely because `git add .` is shorter.
- Do not bypass hooks or force-push to make a failure disappear.
- Detached HEAD, protected branches, submodules, and multiple remotes require resolving the real target before commit.

## Report

Return commit hash/title, pushed remote/branch, checks run, and final sync state. Keep it brief.
