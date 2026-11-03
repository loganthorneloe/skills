Q1: 2 — "A transaction is a group of SQL statements, started with BEGIN and ended with COMMIT... one unit"; "Isolation levels are rules about which of these interleavings the database will allow" — defines transaction and says isolation targets outcomes equivalent to a one-at-a-time order.
Q2: 2 — "How two correct operations produce a wrong result" deposit table (130 instead of 150) — walks through read, read, write, write and explains the lost update and why no serial order matches.
Q3: 2 — "The failure patterns have names" table — defines dirty write, dirty read, lost update, non-repeatable read, read skew, phantom and write skew in plain terms.
Q4: 2 — "Serializable, allows only interleavings equivalent to some one-at-a-time order"; "What protection costs" — states the guarantee and that it works by waiting or aborting, with retry required.
Q5: 2 — "The gap that snapshots leave" (two doctors) — each reads the same snapshot, updates different rows, no write conflict, so the rule across rows breaks.
Q6: 2 — "Two ways databases enforce the levels" (Locks, Snapshots) plus retry and SELECT ... FOR UPDATE text — covers locking, multiversion snapshots with first-committer-wins abort, and application retry or explicit locks.
Q7: 2 — "The same name means different things" Hermitage table; "Defaults are weak" — shows PostgreSQL vs MySQL repeatable read differ, Oracle serializable is snapshot, and defaults vary.
Q8: 2 — "The gap that snapshots leave" and "What isolation cannot fix" — a novice can map the booking case onto write skew from the doctors and the insert example, and the report names Serializable with retries, FOR UPDATE and enforced constraints as fixes, though it never discusses the booking scenario directly.
TOTAL: 16/16
ERRORS: none
