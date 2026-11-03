Q1: 2 — "A transaction is a group of SQL statements, between BEGIN and COMMIT, that the database treats as one unit" / "equivalent to a serial history" — defines the unit and the one-at-a-time ideal, and "Isolation levels tell the database which of these interleavings to forbid."
Q2: 2 — "How two correct operations go wrong" (both calls read $100 before either writes; lost update x=100 example) — read-decide-write pattern with stale reads and the serial-order contrast are explicit.
Q3: 2 — "A dirty read uses data another transaction has not yet committed. A non-repeatable read gets different values from the same row twice. A phantom is a repeated search that finds a different set of rows." — three anomalies plus lost update and write skew are explained.
Q4: 2 — "Only Serializable forbids all of them, by making transactions wait or cancelling one for the application to retry" — equivalence to a serial order, all anomalies ruled out, cost and retry stated.
Q5: 2 — "Why snapshots are not enough" (doctors on call; "modify different rows and thus do not conflict") — snapshot copy, cross-row rule, and why no write conflict are all covered.
Q6: 2 — "making a transaction wait or by cancelling it"; snapshot "refuses the second of two writes to the same row"; "be prepared to retry"; SELECT ... FOR UPDATE — locking, snapshot conflict detection, retry and explicit locking all appear, though multiversion is only implied.
Q7: 2 — "A level's name does not tell you what it prevents" (PostgreSQL Repeatable Read is snapshot isolation; MySQL's Repeatable Read allows lost updates; defaults) — fully covered.
Q8: 1 — "Only Serializable, or an explicit SELECT ... FOR UPDATE on the rows counted, stops it" and "constraints the database enforces" — write skew is taught, but the INSERT/phantom booking case (no row to lock, exclusion constraint) needs inference the report does not directly support.
TOTAL: 15/16
ERRORS: none
