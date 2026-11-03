Q1: 2 — "A transaction is a group of SQL statements between BEGIN and COMMIT that the database treats as one unit"; "Each transaction is checked as if it runs alone" — defines transaction and the serial-order promise of isolation (abort/rollback appears later).
Q2: 2 — "How two correct transactions produce a wrong result" (deposit 100 -> 130 table) — read-then-write lost update with the reason it matches no serial order.
Q3: 2 — "The failure patterns have names" — defines dirty read, non-repeatable read, phantom, lost update, read skew, write skew, dirty write.
Q4: 2 — "Serializable forbids every interleaving whose result no one-at-a-time order could produce... pays by making transactions wait or by aborting one" — plus retry requirement quote.
Q5: 2 — "Write skew is the gap that survives snapshot isolation" (on-call doctors) — same snapshot, different rows, so no write conflict.
Q6: 2 — "Databases enforce these levels in two main ways" — locking vs multiversion snapshots with refused writes, retry, and SELECT ... FOR UPDATE named as fix.
Q7: 2 — "Names and defaults differ between products" — PG Repeatable Read is snapshot isolation, MySQL behavior, Oracle "serializable", defaults weaker.
Q8: 2 — "Write skew" / phantom definitions and "What isolation cannot fix" fixes (Serializable plus retry, FOR UPDATE, constraint) — the booking case is not worked, but the pattern and all three fixes are stated so a novice can map it.
TOTAL: 16/16
ERRORS: none
