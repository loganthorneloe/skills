---
name: git-workflow-conventional
description: Guides agents through standard Git operations, conventional commits, and pre-commit verification specifically tailored for Python/Pytest and TypeScript/Node workspaces.
---

# Git Workflow & Conventional Commits Skill

This skill governs version control workflows across your development repositories. It enforces conventional commits and local test-based verification before any commits are made.

## When to Use
- Actively committing, branching, or pushing in any repository in `~/src`.
- Staging changes or preparing a pull request.

## Workspace Conventions

### 1. Branch Structure
Always create a branch using the following patterns:
- **Features**: `feature/<short-desc>` (e.g., `feature/automated-releases`)
- **Fixes**: `fix/<short-desc>` (e.g., `fix/commit-package-lock`)
- **Docs**: `docs/<short-desc>` (e.g., `docs/add-contributing-md`)
- **Chore/Maintenance**: `chore/<short-desc>` (e.g., `chore/bump-version`)

### 2. Conventional Commit Formatting
All commit messages must use semantic prefixes. Keep titles under 72 characters, imperative, and lowercase:
- `feat: add ...` (new features, e.g., `feat: add GitHub Action for automated releases`)
- `fix: resolve ...` (bug fixes, e.g., `fix: commit package-lock.json and remove from .gitignore`)
- `docs: update ...` (documentation changes, e.g., `docs: refine contributing guide for clarity`)
- `chore: update ...` (dependencies, configuration, e.g., `chore: bump version to 1.0.2`)
- `test: add ...` (unit/integration tests)
- `refactor: clean ...` (code restructuring)

### 3. Pre-Commit Verification (Python & TypeScript)
Before staging and committing code, the agent MUST run the appropriate testing suite:

#### For Python Projects (`daily-email`, `hickory-telegram`, `resume`):
1. **Activate Virtual Environment**: Ensure `.venv` is active (`source .venv/bin/activate`).
2. **Run Tests**: Execute `python -m pytest -v` (or the specific test file being modified).
3. **Verify Integration**: If working on `daily-email` or `hickory-telegram`, run the non-mutating integration tests in dry-run mode to verify pipeline integrity:
   ```bash
   python tests/integration_test.py --dry-run
   ```
4. **LaTeX Compiling**: If modifying the resume project, run `python render_resume.py` to ensure the XeLaTeX compiler generates a valid, single-page PDF.

#### For TypeScript/Node Projects (`gemini-cli-readwise-reader`, etc.):
1. **Install Check**: Ensure `package-lock.json` is staged if packages changed.
2. **Run Tests**: Run `npm test` or `bun test` if configured.
3. **Linter Check**: Run the build compiler (`npm run build` or `tsc`) to ensure no compilation errors.

Never stage, commit, or push code with failing test suites.
