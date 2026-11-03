# Coverage questions — database transaction isolation (frozen before generation)

Score each 0/1/2 from the report alone. 2 = a novice reading only this report could answer correctly; 1 = partial, implicit, or needs inference the report does not support; 0 = missing or wrong.

Q1. What is a transaction, and what does isolation promise?
Key: a group of reads/writes treated as one unit (commit or abort); isolation limits how concurrent transactions see and affect each other, ideally as if they ran one at a time.

Q2. How can two individually correct operations produce a wrong result when interleaved?
Key: each reads a value, decides, then writes based on what it read; if both read before either writes, one write overwrites the other or both act on stale data (lost update), violating a rule that holds if they run one after another.

Q3. Name and explain at least two anomalies that isolation levels are defined to prevent (dirty read, non-repeatable read, phantom, lost update, write skew).
Key: dirty read = seeing uncommitted data; non-repeatable read = re-reading a row gives a different committed value; phantom = a re-run search returns new/missing rows; (lost update/write skew as above/below).

Q4. What does serializable isolation guarantee?
Key: the outcome equals some one-at-a-time (serial) order of the transactions; all anomalies are ruled out, at the cost of blocking or aborting transactions that must then be retried.

Q5. What is snapshot isolation / write skew, and why can a stable snapshot still give a wrong result?
Key: each transaction reads a consistent snapshot; two transactions can each read the same state, update different rows, and together break a rule that spans rows (e.g. on-call doctors), because neither write conflicts with the other.

Q6. How do databases actually enforce isolation?
Key: locks (blocking conflicting access) and/or multiversion snapshots with conflict detection that aborts a transaction; the application must retry aborted transactions or use explicit locking such as SELECT ... FOR UPDATE.

Q7. Why is an isolation-level name alone not enough to know your protection?
Key: levels are defined by which anomalies are forbidden, and implementations differ (e.g. PostgreSQL's REPEATABLE READ is snapshot isolation; defaults vary, often READ COMMITTED); you must check your database's documented behavior.

Q8 (transfer). Two users book the same meeting room for overlapping times: each transaction checks "no overlapping booking exists," then INSERTs its booking. Under snapshot isolation, what can happen and how would you prevent it?
Key: both checks see no conflict in their snapshots, both insert, producing a double booking (write skew/phantom); prevent with SERIALIZABLE (and retry), a lock on the room row (SELECT ... FOR UPDATE), or a database constraint (e.g. exclusion constraint/unique slot).
