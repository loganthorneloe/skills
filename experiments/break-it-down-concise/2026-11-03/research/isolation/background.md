# Background notes (settled textbook material; no records needed)

## Prerequisites the reader lacks

- **Transaction.** A group of SQL statements bracketed by BEGIN … COMMIT (or ROLLBACK) that the database treats as one unit. ACID is the usual summary of what a transaction promises: Atomicity (all or nothing), Consistency (rules preserved), Isolation (concurrent transactions don't interfere), Durability (committed data survives crashes). This topic is the I.
- **Concurrency.** A database serves many connections at once. To stay fast it interleaves their statements, so steps of one transaction run between steps of another. Nothing is wrong with any single statement; the problem is the order steps from different transactions land in.
- **Read-modify-write.** The common pattern behind most bugs: SELECT a value, decide or compute in application code, then UPDATE based on what was read. Between the SELECT and the UPDATE, another transaction can change the value. The decision is then made on stale data.
- **Invariant.** A rule the data must always satisfy (balance ≥ 0; at least one doctor on call; total money constant across a transfer). "Individually correct" means each transaction keeps the invariant when it runs alone.
- **Serial order.** Running the transactions one after another with no overlap. Serializability says that any concurrent execution must produce a result that some serial order could have produced. It's the reference definition of "correct together": if every transaction is correct alone, every serial order is correct, so every serializable execution is correct.
- **Commit / rollback / uncommitted data.** Until a transaction commits, its writes may still be undone. Reading them ("dirty read") means acting on data that might never officially exist.
- **Two implementation families.**
  - *Locks.* A transaction must take a shared (read) or exclusive (write) lock before touching a row. Conflicting requests wait. Holding all locks until commit (two-phase locking) gives serializability. Releasing read locks early gives weaker levels.
  - *Multiversion concurrency control (MVCC) / snapshots.* The database keeps old versions of rows, and each transaction (or statement) reads a consistent snapshot as of some moment. Readers don't block writers. Conflicts between writers are detected with row write locks ("first updater/committer wins"). PostgreSQL, MySQL/InnoDB plain SELECTs, and Oracle work this way.
- **Statement snapshot vs. transaction snapshot.** At READ COMMITTED (PostgreSQL, MySQL, Oracle), each statement sees the latest committed data as of when it starts, so two SELECTs in one transaction can disagree. At REPEATABLE READ / snapshot isolation, the whole transaction sees one snapshot taken at its first statement.
- **Serialization failure.** At stronger levels the database may refuse to commit a transaction (PostgreSQL SQLSTATE 40001: "could not serialize access …"). The correct response is to roll back and run the whole transaction again. That's the price of the guarantee.

## Anomaly glossary (plain-language mapping)

| Name | Plain description | Prevented starting at (standard/Berenson view) |
|---|---|---|
| Dirty write | Overwriting another transaction's uncommitted write | every level in practice (Berenson recommends at all levels) |
| Dirty read | Reading another transaction's uncommitted write | READ COMMITTED |
| Lost update | Two read-modify-writes on the same row; one overwrites the other | REPEATABLE READ (locking) or snapshot isolation; **not** MySQL RR or any READ COMMITTED |
| Non-repeatable (fuzzy) read | Same row read twice gives different values | REPEATABLE READ |
| Read skew | Reading two related rows at different moments, seeing a mix of before/after (e.g. transfer half-done) | REPEATABLE READ / snapshot isolation |
| Phantom | A repeated search (WHERE …) returns a different set of rows because another transaction inserted/deleted | SERIALIZABLE (standard); PostgreSQL RR also prevents the simple re-read case |
| Write skew | Two transactions read overlapping data, each checks a rule, then each writes a *different* row; together they break the rule | SERIALIZABLE only |

Hermitage/Adya names: P4 = lost update, G-single = read skew, G2-item = write skew on rows, G2 = write skew via a search predicate, G0 = dirty write, G1a/b/c = dirty-read variants.

## Worked example ideas grounded in the sources

1. **Lost update, money (primary; E1 + E13 + E17).** Account balance 100. Transaction A adds 20 and transaction B adds 30, each by reading the balance in a SELECT and writing the new total in an UPDATE (read-modify-write). Interleaving: A reads 100, B reads 100, A writes 120 and commits, B writes 130 and commits. Final 130. Correct serial results are 150 either way. This is Berenson's H4 almost exactly (T2 +20 → 120, T1 +30 → 130). Hermitage's two-window SQL script shows it live in PostgreSQL READ COMMITTED, and the same steps at REPEATABLE READ end with "could not serialize access due to concurrent update". ACIDRain's withdraw($99) from $100 example shows the money-out version: both checks pass, $198 leaves.
   - Important nuance for accuracy (PG docs §13.2.1): writing it as one statement, `UPDATE accounts SET balance = balance + 20 WHERE …`, does **not** lose the update in PostgreSQL READ COMMITTED, because the second UPDATE waits and then re-applies to the newly committed row. The bug needs the value to pass through application code (SELECT, then UPDATE with a literal). This is also a practical fix (C16).
2. **Write skew, doctors on call (secondary; E8 + E11).** Ports & Grittner Figure 1. Use it to show why snapshot isolation / REPEATABLE READ isn't enough: no row is written by both transactions, so row locks never collide. Only SERIALIZABLE (or an explicit SELECT … FOR UPDATE on the rows counted) prevents it.
3. **Inconsistent read of a transfer (optional; E2).** $40 moves from x (50) to y (50). A report reading mid-transfer sees 10 + 50 = 60. Shows dirty/skewed reads without any write conflict.

Suggested ladder for "how isolation levels help": each level removes a class of interleavings. READ COMMITTED stops reading uncommitted data. REPEATABLE READ / snapshot stops values shifting under you mid-transaction and (in PostgreSQL, not MySQL) refuses lost updates. SERIALIZABLE also catches write skew, making the result equal to some one-at-a-time order, at the cost of blocking (locking engines) or aborts to retry (PostgreSQL SSI). Defaults are usually READ COMMITTED (PostgreSQL, Oracle, SQL Server) or MySQL's REPEATABLE READ, so most applications don't get full protection unless they ask for it or use explicit locks.

## Things a writer should not say

- Don't say "REPEATABLE READ prevents lost updates" without naming the product (true for PostgreSQL, false for MySQL/InnoDB per Hermitage and ACIDRain).
- Don't say the standard's three phenomena define serializability (Berenson: a "common misconception").
- Don't say raising the isolation level fixes bugs where the operations aren't inside one transaction (ACIDRain: 17 of 22).
- Don't present the 7% figure as a general cost of serializability (one 2012 PostgreSQL study).
- Don't say Oracle offers true serializability (Hermitage: its "serializable" is snapshot isolation; HAT 2013 lists Oracle max = SI).
