Q1: 2 — "A transaction is a group of SQL statements between BEGIN and COMMIT that the database treats as one unit"; "equivalent to some one-at-a-time order" — Defines transaction and the isolation ideal (abort not stated, but the core is covered).
Q2: 2 — "both calls read $100, both checks pass, and both write $1" — The withdrawal race shows read, decide, write interleaving and why no serial order allows it.
Q3: 2 — bullets on dirty read, non-repeatable read, phantom, write skew, plus lost update paragraph — All five are named and explained correctly.
Q4: 2 — "only Serializable forbids all of them, and it does so by making transactions wait or fail and retry" — Serial-order equivalence, all anomalies excluded, and the retry cost are all stated.
Q5: 2 — "Snapshots still miss write skew" (on-call doctors) — Explains consistent snapshots, different rows, no collision, so the rule breaks.
Q6: 2 — "Databases enforce these levels in two main ways" plus the serialization-failure and retry text and SELECT … FOR UPDATE — Locks, snapshots, conflict-detection aborts, retries and explicit locking are all covered.
Q7: 2 — "The same name can mean different guarantees" — PostgreSQL vs MySQL Repeatable Read, defaults differ, and tested behavior matters over the name.
Q8: 1 — "write skew ... different rows" and "SELECT … FOR UPDATE ... database constraints" — The meeting-room INSERT case is never shown, so a novice must infer phantom-style inserts and what a row lock would target.
TOTAL: 15/16
ERRORS: none
