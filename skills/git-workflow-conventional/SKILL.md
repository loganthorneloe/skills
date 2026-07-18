---
name: git-workflow-conventional
description: Guides agents through standard Git operations, conventional commit naming, branch prefix patterns, and running pre-commit test verifications.
---

# Git Workflow & Conventional Commits Skill

This skill defines the Git workflow and commit conventions expected when contributing features, fixes, or documentation updates to this workspace's projects.

## When to Use
- Actively running Git operations (branching, staging, committing, pushing).
- Creating PRs or preparing code for review.
- Prior to finalizing any feature or task that requires a commit.

## Guidelines & Rules

### 1. Branch Naming Conventions
Always create a descriptive branch for your changes using the appropriate prefix:
- **Features**: `feature/<short-description>` (e.g., `feature/automated-releases`)
- **Bug Fixes**: `fix/<short-description>` (e.g., `fix/commit-package-lock`)
- **Documentation**: `docs/<short-description>` (e.g., `docs/add-contributing-md`)
- **Maintenance/Refactoring**: `chore/<short-description>` or `refactor/<short-description>`

### 2. Conventional Commit Messages
Structure all commit messages using conventional prefixes:
- `feat: <description>` — A new feature
- `fix: <description>` — A bug fix
- `docs: <description>` — Documentation-only changes
- `chore: <description>` — Maintenance tasks, dependencies, version bumps
- `test: <description>` — Adding or correcting tests
- `refactor: <description>` — Code changes that neither fix a bug nor add a feature

*Keep messages concise, in the imperative tense, and under 72 characters.*

### 3. Pre-Commit Verification
Before staging and committing your code, you must verify correctness:
- Run the project's test suite (e.g., `pytest`, `npm test`) if available.
- Resolve any linter or compiler warnings.
- Never commit or push code that breaks the existing build or test suites unless explicitly requested.
