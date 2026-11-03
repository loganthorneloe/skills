# r02 — transaction isolation graph

Complete: graph-only task. Final `dag.json` has 23 nodes and 43 edges. No remaining gap/partial nodes; `rule` is an explicit supplied example assumption, not a database guarantee.

## Sources actually used

Started from the assigned verified packet, then directly read these official HTML passages:

- [PostgreSQL 18 — Transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html): §3.4 transfer, atomicity, BEGIN/COMMIT/ROLLBACK, implicit transactions. Establishes the unit of work; does not supply every isolation guarantee.
- [PostgreSQL 18 — Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html): §13.2 definitions and Table 13.1; §13.2.1 statement snapshots, updater waiting/recheck, bank and website examples; §13.2.2 stable snapshots and concurrent-update failures; §13.2.3 sum example, serial comparison, dependency monitoring, nonblocking predicate tracking, correctness and retry conditions. Engine-specific details retain PostgreSQL qualifications.
- [MySQL 8.4 — Transaction Isolation Levels](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html): §17.7.2.1 four levels, plain versus locking reads, record/range protection, update-lock examples, and SERIALIZABLE’s autocommit condition. Used for engine/statement distinctions, not a general speed ranking.
- [SQLite — Isolation In SQLite](https://www.sqlite.org/isolation.html): separate connections and shared-cache exception, one writer, WAL read snapshots, X/Y stale-snapshot failure, own-write visibility. Documentation says last updated 2022-04-18; this is a mechanism explanation, not a contemporary performance claim.
- Supplemental: [PostgreSQL 18 — Concurrency Control Introduction](https://www.postgresql.org/docs/current/mvcc-intro.html), §13.1: retained data versions and version-based reads versus explicit locking. Fills the beginner snapshot/mechanism bridge.
- Supplemental: [PostgreSQL 18 — Serialization Failure Handling](https://www.postgresql.org/docs/current/mvcc-serialization-failure-handling.html), §13.5: retry the complete transaction, including decision logic; repeat failures remain possible. Fills the retry-scope gap.

No search-engine queries. Used direct URL opens and follow-up section opens. All accessed successfully; initial PostgreSQL and MySQL excerpts omitted later relevant sections, which were explicitly opened afterward. No credentials or author biographies needed for this requested graph-only artifact. PostgreSQL `current` identified version 18 at retrieval.

## Actual chronology

1. Read only assigned instructions, skill, request, source packet. Saved `dag.initial.json` and working `dag.json` before supplemental research.
2. Opened isolation, MVCC, retry, and MySQL pages. Logged first reading immediately in `history.jsonl`, including no-change status and still-unread sections.
3. Read remaining relevant sections and the transaction/SQLite pages. Saved researched state as `dag.round-2.json`; resolved research gaps, separated stable snapshots from serial outcomes, added correctness conditions, removed two edges that imposed example order.
4. Structural check found Read Committed lacked a target path. Added its genuine dependency into statement-kind behavior. Semantic target audit made engine qualification explicit. Saved `dag.round-3.json` and final `dag.json`.
5. Ran final structural and constructed reasoning checks; saved `verification.json`. No graph change from the final checks. History includes timestamps and reconstructable before/after artifacts; no reconstructed research rounds.

## Verification

PASS: unique node IDs, valid endpoints, no duplicate edges, acyclicity, every node reaches target, required node/evidence fields. Every edge was reviewed against its named dependent claim; teaching order and the on-call example stay outside dependency edges.

Constructed checks using graph claims and explicit inputs:

- Unfamiliar capacity reservation: two requests of six against capacity ten can jointly reserve twelve from overlapping old observations, whereas either serial order reserves six.
- Counterexample: two PostgreSQL Read Committed relative increments can reach 102 from 100; two stale replacement writes can instead leave 101. Concurrency alone does not establish a lost update.
- Boundary counterexample: serializable SQL transactions do not protect a complete application decision split across separate read and write transactions.

These are executable arithmetic/decision models plus documented semantic reasoning, not live database integration tests. No claim that a particular engine executed the constructed on-call or capacity schedule.

## Evidence and presentation limits

Table 13.1, PostgreSQL’s two sum transactions and serial comparison, MySQL’s lock traces, and SQLite’s X/Y examples are identified evidence candidates. No copied figures or full explanation report were required. Shared rendering is handled externally; this worker did not render or inspect HTML/SVG.

Scope covers ordinary transactional table data on separate connections. Sequence exceptions, distributed side effects, detailed lock tuning, and universal performance recommendations are outside this request. The graph does preserve required transaction-boundary, application-rule, own-write, engine, statement, waiting, and retry distinctions.
