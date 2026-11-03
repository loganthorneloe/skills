Q1: 2 — "What a transaction promises" (BEGIN/COMMIT/ROLLBACK, "treats as one unit"); "What 'correct together' means" (serializable = result of one-at-a-time order) — defines transaction and the one-at-a-time ideal; the word "isolation" is tied to levels that forbid interleavings, which is enough.
Q2: 2 — "How two correct transactions produce a wrong result" (read-modify-write, 100 -> 130 table) — walks a lost update step by step and shows no serial order matches.
Q3: 2 — "The named ways interleaving goes wrong" table — defines dirty read, non-repeatable read, phantom, lost update, read skew, write skew with examples.
Q4: 2 — "forbids every interleaving whose result doesn't match some one-at-a-time order"; "What the stronger levels cost" — states the serial-equivalence guarantee and the wait/cancel-and-retry cost.
Q5: 2 — "Snapshot isolation stops ... It does not stop write skew"; doctors example "T1 writes Alice's row and T2 writes Bob's" — explains the snapshot, the cross-row rule, and why writes do not conflict.
Q6: 2 — "Two ways a database enforces a level" (locking; multiversion with first-committer-wins) plus retry and SELECT ... FOR UPDATE in "Limits" — covers locks, snapshots, aborts, retry and explicit locking.
Q7: 2 — "The same name means different things" (Hermitage table; MySQL RR allows lost update; Oracle "serializable" is snapshot; defaults weaker) — directly teaches that names differ and to check your database.
Q8: 2 — doctors write skew, phantom row, and the fix list (SERIALIZABLE with retry, FOR UPDATE, shared row, constraint) — the report never discusses room booking, but the INSERT-based write skew and the fixes map directly with light inference.
TOTAL: 16/16
ERRORS: Minor internal inconsistency: it says snapshot isolation's first-committer-wins applies to "PostgreSQL, MySQL's InnoDB engine, and Oracle", yet later shows InnoDB Repeatable Read allowing lost updates. No other errors noticed.
