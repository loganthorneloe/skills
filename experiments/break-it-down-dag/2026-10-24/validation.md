# Validation

- Repository validator: `python3 skills/rtg/skill-refiner/scripts/validate_skill.py skills/wip/break-it-down-dag --max-tokens 3000` → **PASS**, 3,000 estimated tokens, local links OK.
- Target authoring validator: `python3 /Users/loganthorneloe/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/wip/break-it-down-dag` → **Skill is valid!**
- `git diff --check` → clean during authoring; final check recorded in results.
- Personal Codex link resolves to repository `SKILL.md`. Personal and workspace Codex/shared skill discovery roots have zero duplicate frontmatter names. See `installation-check.json`. No separate native discovery command was available; resolved entrypoint and creator validator checked instead.
- Baseline working-copy bytes match `inputs/baseline.txt`. The pre-existing uncommitted canonical edit was preserved. Variant bytes match `inputs/variant.txt`; input SHA-256 hashes retained.
- Treatment-boundary assertion passed: outside research replacement, removed source-audit example, name and WIP metadata, every character is identical.
- Representative execution proof: all eight generation agents completed actual researched HTML reports. The four variant runs produced initial graphs, research history, final graph data, and rendered views. This exceeds a trace-only dry run.
- `python3 experiments/break-it-down-dag/2026-10-24/check_graphs.py` → **4/4 PASS**: unique IDs, valid endpoints, edge justifications, acyclicity, target reachability, required node fields, evidence presence, assumptions and revision history. Evidence correctness and edge necessity are separate evaluator judgments.
- All eight workers recorded desktop/mobile checks and font/image loading checks. Interactive reports include applicable keyboard, boundary and static-fallback checks. Details and reproducible checks remain in each run's `run-notes.md` and verification JSON/scripts. Independent evaluator also checks rendered reports.
- Evals starters exercised offline; neither evaluated a live model. Database SQL examples source-checked but not executed against a live database. These limits are disclosed in the reports/notes.
- Eight distinct generation agents (`run_e01` … `run_e08`), one separate evaluator, inherited parent model/settings, no nested delegation. Generation workers used fresh history and did not inspect other runs. Maximum three active workers due to slot limit.

Structural PASS does not establish better explanations. Read the report and graph evaluations separately.

## Review page

`verify_review.cjs` passed with bundled Playwright and isolated Chrome: 1440px/390px widths, local links, all four topic selections, native keyboard type-ahead, static fallback links, no page overflow or JavaScript errors. Desktop and fresh-context mobile screenshots were inspected. Native popup arrow-key automation did not commit a selection in headless macOS Chrome; keyboard type-ahead was verified instead. A stale screenshot after viewport resizing was resolved by a fresh mobile context; page content was unchanged. See `review-verification.json`.

Final `git diff --check` and new-skill whitespace check passed.
