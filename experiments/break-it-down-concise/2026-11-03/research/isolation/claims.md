# Claims — database transaction isolation

Reader: can read basic SQL SELECT/UPDATE; no database internals. Question: why can two individually correct operations produce a wrong result when run at the same time, and how do isolation levels help?

- C1. A transaction groups a sequence of reads and writes into one unit meant to move the database from one consistent state to another; "correct" means it preserves the data's rules (invariants) when it runs alone.
- C2. The reference definition of correct concurrent execution is serializability: the outcome must equal running the same transactions one at a time in some order; if each transaction is correct alone, any serializable mix is correct.
- C3. When the steps of two individually correct transactions interleave, the result can match no one-at-a-time order (for example a lost update: both read balance 100, each writes its own new value, one change vanishes).
- C4. The mechanism is a conflict: two transactions touch the same data item and at least one writes it, so one transaction decides or writes based on a value the other changes (or has not yet committed) before it finishes.
- C5. The recurring failure patterns have names: dirty write, dirty read, non-repeatable (fuzzy) read, phantom, lost update, read skew, and write skew.
- C6. Isolation levels let an application trade concurrency/throughput for protection: each weaker level permits more of these anomalies in exchange for less blocking or fewer aborts.
- C7. The SQL standard names four levels (READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE) and defines the lower three by which phenomena (dirty read, non-repeatable read, phantom) each must prevent.
- C8. The standard's phenomenon definitions are ambiguous and incomplete: preventing the three named phenomena does not guarantee serializability, and dirty writes, lost updates, and write skew fall outside them.
- C9. Databases implement isolation mainly two ways: locks (held briefly or until commit; long-held read and write locks under two-phase locking give serializability) and multiversion snapshots (each transaction reads a consistent past version).
- C10. Snapshot isolation prevents dirty reads, non-repeatable reads, the standard's phantoms, and lost updates (first-committer-wins), but still allows write skew, so it is not serializable.
- C11. The same level name means different guarantees in different products (for example PostgreSQL REPEATABLE READ is snapshot isolation; MySQL/InnoDB REPEATABLE READ allows lost updates; Oracle "serializable" is snapshot isolation).
- C12. Default isolation levels are usually weaker than serializable (PostgreSQL and many others default to READ COMMITTED; MySQL/InnoDB defaults to REPEATABLE READ; in a 2013 survey only 3 of 18 databases defaulted to serializable).
- C13. Stronger levels prevent anomalies by blocking or by aborting a transaction with a serialization failure, so applications using them must be ready to retry.
- C14. Stronger isolation has a measurable but workload-dependent cost (PostgreSQL's serializable mode measured within about 7% of snapshot isolation; strict two-phase locking far slower on read-heavy workloads).
- C15. These anomalies cause real damage when concurrency rises: attacks exploiting weak isolation or missing transactions have drained accounts and corrupted e-commerce data, and many such bugs come from not wrapping logic in a transaction at all, which no isolation level fixes.
- C16. At weaker levels, applications can close specific gaps with explicit tools: atomic single-statement updates, SELECT ... FOR UPDATE / explicit locks, materialized conflicts, and database-enforced constraints.
- C17. Limits: isolation guarantees are only as good as their implementation (a serializable-mode bug in PostgreSQL was found in 2020 and fixed), and tests can show but not prove a database's behavior.

## Claims the direct answer depends on most

C2 (what "correct together" means), C3 and C4 (why interleaving breaks individually correct operations), C6 and C7 (what isolation levels are and how they help), and C10/C13 (that only serializable closes every gap, at the price of blocking or retries). C8 and C11 are the most important caveats.
