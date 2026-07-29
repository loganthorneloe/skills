# Apply

Args: proposal path or slug (required).

1. Read proposal; accepted or user just said apply this file
2. Target = owned skill only. Vendor → fork first
3. Backup: git-safe or `.scratch/skill-evolution/backups/`
4. Apply listed hunks only
5. Run the target validator/tests and one representative pressure scenario
6. Re-gate with [../references/skill-quality.md](../references/skill-quality.md); any failure → revert
7. Mark proposal `applied`; update an existing target CHANGELOG if it uses one; touch `.scratch/skill-evolution/LAST_RUN`

Hard exit: diff matches accepted hunks and every gate/test passes. No batch apply unless user lists proposals.
