# Apply

Args: proposal path or slug (required).

1. Read proposal; accepted or user just said apply this file
2. Target = owned skill only. Vendor → fork first
3. Backup: git-safe or `.scratch/skill-evolution/backups/`
4. Apply listed hunks only
5. Re-gate with [../references/skill-quality.md](../references/skill-quality.md); revert if fail
6. Mark proposal `applied`; append CHANGELOG; touch LAST_RUN
7. Verify (default on): one pressure scenario; report pass/fail

No batch apply unless user lists proposals.
