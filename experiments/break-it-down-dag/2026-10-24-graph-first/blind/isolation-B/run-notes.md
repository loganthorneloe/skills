# isolation-B run notes

Completed graph-only deliverable: `dag.json`. Initial graph saved before supplemental research in `history/initial.json`; actual round records and the researched snapshot are in `history/`. No report or renderer produced.

Used supplied skill snapshot, request, worker instructions, and transaction-isolation packet. No other runs, designs, rubric, or skills inspected. No skill modified. No delegation.

Sources actually opened and used:

- [PostgreSQL 18 Transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html): transfer correctness, atomicity, BEGIN/COMMIT/ROLLBACK.
- [PostgreSQL 18 Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html): anomaly definitions, Table 13.1, complete relevant Read Committed, Repeatable Read, and Serializable sections; read/write dependencies, updates versus ordinary reads, whole-transaction retries.
- [MySQL 8.4 InnoDB isolation levels](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html): snapshot reads versus locking statements, search-condition effects, and Serializable autocommit qualification.
- [SQLite isolation](https://www.sqlite.org/isolation.html): separate connections, WAL snapshots, blocked access, stale snapshot promotion rejection, own-write visibility.

No keyword searches or additional sources needed. Opened further portions of the four pages to read relevant sections omitted from initial tool excerpts. All accessed successfully. SQL-standard claims rely on PostgreSQL's official summary; the standard itself was not accessed.

Evidence entries state the precise supported claim in paraphrase, not purported verbatim quotations. Synthesis and the original withdrawal schedule are labeled. The withdrawal example assumes a total-balance rule, permits negative individual accounts, uses different written rows, and assumes no extra lock or constraint enforcing the total. It is a mathematical construction, not a measured database run.

`check.py` passed: unique IDs, endpoints, acyclicity, paths from all nodes to target, required fields/statuses/evidence locators, initial preservation, and example arithmetic for concurrent and both serial orders. `checks.json` contains results. Manual review reconciled claims with source passages and removed weak or motivational dependencies. Optional application choice material stays outside prerequisite nodes.

Limits: no live database test; no formal proof of pedagogical necessity; no HTML/SVG render check because the shared renderer handles display. No remaining partial/gap nodes within the declared scope. Storage internals, engine tuning, and performance recommendations intentionally excluded.
