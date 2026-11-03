# isolation-A run notes

Completed graph-only task using assigned old skill snapshot. Final: `dag.json` (18 nodes, 31 edges). Initial saved before supplemental browsing: `initial-dag.json`. Researched intermediate: `round-1-dag.json`. Final graph records all three revision stages. No report or renderer produced.

## Sources actually used

Supplied transaction-isolation packet read in full. Live relevant sections subsequently read:

- [PostgreSQL 18 — Transactions](https://www.postgresql.org/docs/18/tutorial-transactions.html): transfer, boundaries, atomicity, implicit transactions.
- [PostgreSQL 18 — Transaction Isolation](https://www.postgresql.org/docs/18/transaction-iso.html): anomaly definitions and Table 13.1; Read Committed and Repeatable Read; Serializable, example and retries.
- [MySQL 8.4 — Transaction Isolation Levels](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html): introductory guarantees, ordinary versus locking reads, record/range protection, Serializable and autocommit.
- [SQLite — Isolation In SQLite](https://www.sqlite.org/isolation.html): separate connections, WAL snapshots, single writer, stale-snapshot rejection, own writes. Page lists update date April 18, 2022; used for documented mechanisms, not performance claims.
- Supplemental: [PostgreSQL 18 — Concurrency Control Introduction](https://www.postgresql.org/docs/18/mvcc-intro.html), opening paragraphs: MVCC and distinct visible versions.

Research used direct URL opens, then section-position opens; no search-engine queries. PostgreSQL URLs pinned to 18, matching supplied packet. No access failures. SQL-standard minimum comparison is attributed to PostgreSQL documentation; standard itself not accessed.

## Revisions and verification

Initial decomposition left all unfamiliar concepts as gaps. Primary-source review filled answers and exposed need for explicit invariant/correctness grounding and improved prerequisite edges. Final review narrowed assumed knowledge to actual SQL baseline, added correctness node, and replaced two motivation/order edges with actual definitional dependencies.

Ran `python3 check_graph.py`: PASS. Verified unique IDs, valid endpoints, required fields, nonempty evidence/locators for supported nodes, no cycles, every node reaches target, and preserved initial/intermediate/history records. No unresolved required gap nodes.

The on-call example is an original worked deduction, not a published observation. Script checks both complete serial orders and all six read/write interleavings preserving each transaction’s own order. Both-off occurs when both read before the writes; neither serial order produces it. Writes in this abstract model include commit. Product applicability is grounded in PostgreSQL Repeatable Read documentation, not an integration test.

Manual semantic review checked answer prerequisites, guarantee/mechanism separation, same-connection caveat, exact snapshot boundary, and whole-transaction retry. Structural checks cannot establish semantic graph quality.

## Limits

No live database run, benchmark, rendering, or full explanation report. No universal performance recommendation. Distributed/replicated databases, recovery internals, exhaustive lock behavior and external side effects remain outside scope. Shared renderer handles the view.
