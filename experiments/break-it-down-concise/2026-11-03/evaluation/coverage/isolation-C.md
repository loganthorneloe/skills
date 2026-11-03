Q1: 2 — "What a transaction promises": "a group of SQL statements between BEGIN and COMMIT that the database treats as one unit"; "An isolation level is the setting that tells the database which of these interleavings to refuse" — defines the unit and ties isolation to results matching a serial order.
Q2: 2 — "How two correct transactions produce a wrong result" and H4 / $100 balance example — read-modify-write with both reads before either write gives a lost update that matches no serial order.
Q3: 2 — "The named failure patterns" table — defines dirty read, non-repeatable read, phantom, lost update, write skew (and more) in plain language.
Q4: 2 — "the result must equal the result of some serial order"; "Only serializable refuses every interleaving..."; "by making a transaction wait or by aborting it so the application can retry" — covers guarantee, all anomalies excluded, and cost.
Q5: 2 — "A failure where no row is shared" and "Two ways a database enforces a level" — snapshot isolation described, doctors example shows different rows written so no write conflict.
Q6: 2 — "Two ways a database enforces a level" and "The price of stronger isolation" — locking, multiversion snapshots with abort on conflicting writes, retry, and SELECT ... FOR UPDATE.
Q7: 2 — "The same name can mean different guarantees" and "Defaults are usually weak" — Hermitage table shows PG repeatable read = snapshot isolation, MySQL differs, defaults vary.
Q8: 1 — "At weaker levels, an application can still close specific gaps" list plus write skew and phantom definitions — the report never discusses an insert-based overlap check, so the double booking and fixes (serializable plus retry, constraint) must be inferred; FOR UPDATE caveat about locking rows being counted is only implicit.
TOTAL: 15/16
ERRORS: none
