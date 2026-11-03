# Evidence records — database transaction isolation

Claim IDs from `claims.md`. Sources audited in `audit-records.md`. Asset paths are relative to `research/isolation/`. All images were rendered from the source PDF at 300 dpi with PyMuPDF (or, for the PostgreSQL table, a 2x headless-Chrome screenshot of the live page), then opened at full size and checked.

### E1: Lost update as a precise interleaving (H4)
- claim: C3, C4, C5 (support)
- type: quote+metric
- source: A Critique of ANSI SQL Isolation Levels — https://arxiv.org/abs/cs/0701157 (v1)
- locator: §4.1 Cursor Stability, history H4 and following sentence (PDF p. 7–8; paper pp. 6–7)
- asset: "H4: r1[x=100] r2[x=100] w2[x=120] c2 w1[x=130] c1" and "The final value of x contains only the increment of 30 added by T1."
- inspected: not applicable (text; copied from extraction and checked against rendered page 7)
- notice: Each transaction alone is correct (T2 adds 20, T1 adds 30). Run back-to-back, x would end at 150. Interleaved, both read 100 before either writes, so T1's write of 130 overwrites T2's 120 and T2's +20 vanishes even though T2 committed. Notation: r1[x=100] = transaction 1 reads x and sees 100; w = write; c = commit. This is the cleanest worked example for the reader's "why" question.
- limits: The paper notes P4 is possible at READ COMMITTED and prevented by its locking REPEATABLE READ and by snapshot isolation; whether a given product prevents it depends on the product (see E12). A single SQL statement `UPDATE … SET x = x + 20` is not this pattern in PostgreSQL READ COMMITTED (see E9) — the lost update needs a separate read, then a write computed in the application.
- rights: ACM 1995 notice permits copying without fee for non-commercial use with notice; arXiv non-exclusive license. Quote with attribution.

### E2: Inconsistent read during a transfer (H1)
- claim: C3, C4, C8 (support)
- type: quote+metric
- source: A Critique of ANSI SQL Isolation Levels — https://arxiv.org/abs/cs/0701157
- locator: §3, history H1 (PDF p. 6; paper p. 5)
- asset: "H1: r1[x=50]w1[x=10]r2[x=10]r2[y=50]c2 r1[y=50]w1[y=90]c1" — T1 transfers 40 from x to y keeping total 100; T2 "reads an inconsistent state where the total balance is 60."
- inspected: not applicable (text)
- notice: A read-only reporting transaction sees the money "in flight": 10 + 50 = 60 instead of 100. Also shows why the paper says the strict reading of the standard is too weak: H1 violates none of the strict anomalies A1–A3, yet it is non-serializable. Pairs with H2 (T1 sees total 140) in the same section.
- limits: Logical example; numbers illustrative. Under snapshot isolation the same actions become H1.SI, which is serializable (§4.2).
- rights: as E1.

### E3: Standard's level table (three phenomena)
- claim: C7 (support); C8 (context)
- type: table
- source: A Critique of ANSI SQL Isolation Levels — https://arxiv.org/abs/cs/0701157
- locator: Table 1 (PDF p. 4; paper p. 3)
- asset: assets/berenson1995-table1-ansi-phenomena.png (2147×472 px); values in assets/tables.md
- inspected: opened at full size; title, all 4 rows and 3 phenomenon columns visible, no clipping
- notice: This is how the SQL standard defines the levels: each step up forbids one more named phenomenon. The paper's key point is that the bottom row is labeled "ANOMALY SERIALIZABLE," not "SERIALIZABLE": forbidding these three things is not the same as serializability.
- limits: The paper says "Table 1 is not a final result; Table 3 will superseded it." Use as "the standard's view," then contrast with Table 4 (E4).
- rights: as E1; embed with attribution.

### E4: Which anomalies each level allows (fuller picture)
- claim: C5, C6, C8, C10 (support)
- type: table
- source: A Critique of ANSI SQL Isolation Levels — https://arxiv.org/abs/cs/0701157
- locator: Table 4 (PDF p. 11; paper p. 10)
- asset: assets/berenson1995-table4-anomalies-by-level.png (2218×959 px); values in assets/tables.md
- inspected: opened at full size; all 6 rows and 8 anomaly columns plus header visible; "Sometimes Possible" in A5B column slightly tight to the right border but legible
- notice: Read across the Snapshot row: it blocks everything up to and including lost update and read skew, but write skew (A5B) is "Possible." Read down: REPEATABLE READ (the paper's locking definition) and Snapshot are each missing something different (Phantom vs. Write Skew), so neither is strictly stronger. Only SERIALIZABLE says "Not Possible" everywhere. This is the best single exhibit for "how isolation levels help."
- limits: REPEATABLE READ here means the paper's locking definition; products differ (E11, E12). "Sometimes Possible" is coarse. Uses Berenson vocabulary (P0–P4, A5A/B), not Adya's G-codes used by Hermitage.
- rights: as E1.

### E5: Strength hierarchy of isolation levels
- claim: C6, C10 (support); C8 (context)
- type: figure
- source: A Critique of ANSI SQL Isolation Levels — https://arxiv.org/abs/cs/0701157
- locator: Figure 2 and caption (PDF p. 11; paper p. 10)
- asset: assets/berenson1995-fig2-isolation-hierarchy.png (1046×1317 px)
- inspected: opened at full size; all nodes, edge labels and the full caption visible; original has typos "Degreee 2", "Repeat abl e" spacing — these are in the source
- notice: Higher boxes are stronger; each edge is labeled with the anomaly the stronger level removes (P0 → P1 → … up to Serializable). Snapshot Isolation sits off to the side, joined to Repeatable Read by an oval labeled A5B / A3: each forbids something the other allows. The edge from Snapshot Isolation up to Serializable is A5B, write skew — the one thing left to remove.
- limits: Caption says it assumes the paper's strengthened definitions, not the standard's original wording, and omits per-statement snapshot levels. Oracle Consistent Read node is 1995 behavior.
- rights: as E1.

### E6: Locking definitions of each level
- claim: C9 (support)
- type: table
- source: A Critique of ANSI SQL Isolation Levels — https://arxiv.org/abs/cs/0701157
- locator: Table 2 (PDF p. 5; paper p. 4)
- asset: assets/berenson1995-table2-locking-levels.png (1909×900 px); values in assets/tables.md
- inspected: opened at full size; all 6 rows and 3 columns visible
- notice: Shows that in a locking database the levels differ only in how long read locks are held: none (READ UNCOMMITTED), released right after each read (READ COMMITTED), held to commit on rows read (REPEATABLE READ), held to commit on rows and on search conditions/predicates (SERIALIZABLE). Write locks are always held to commit. That gives the reader a concrete mechanism behind each level name.
- limits: Locking only; multiversion systems (PostgreSQL, MySQL plain reads, Oracle) work differently (E9, E10). Needs short glossary: "well-formed" = takes a lock before every access; "long duration" = held until commit/abort; "predicate lock" = lock on everything matching a WHERE condition, including rows not yet inserted.
- rights: as E1.

### E7: Isolation as a trade-off; serializability defined
- claim: C2, C6 (support)
- type: quote
- source: A Critique of ANSI SQL Isolation Levels — https://arxiv.org/abs/cs/0701157
- locator: §1 Introduction (first sentence); §2.1 (serializable definition)
- asset: "Running concurrent transactions at different isolation levels allows application designers to trade throughput for correctness." / "A history is serializable if it is equivalent to a serial history"
- inspected: not applicable
- notice: The first sentence states the whole purpose of isolation levels in one line. The second gives the reference standard ("serial history" = one transaction at a time).
- limits: "Throughput for correctness" is the authors' framing; Ports & Grittner (E14) show the cost of full correctness can be small on some workloads.
- rights: as E1.

### E8: Write skew — two doctors go off call
- claim: C3, C10 (support); C5 (context)
- type: figure
- source: Serializable Snapshot Isolation in PostgreSQL — https://arxiv.org/abs/1208.4179 (v1)
- locator: Figure 1, §2.1.1 (PDF p. 2)
- asset: assets/ports2012-fig1-write-skew-doctors.png (1043×818 px)
- inspected: opened at full size; both transaction columns, SQL, time arrow, and caption visible
- notice: Plain SQL the reader can follow. Rule: at least one doctor on call. Each transaction counts on-call doctors (sees 2), then takes one doctor off. Either order run alone leaves one doctor on call. Under snapshot isolation both read the same snapshot and update different rows (Alice vs. Bob), so the row write locks never collide and both commit: zero doctors on call. Paper's text: "The write locks taken on update don't solve this problem, because the two transactions modify different rows and thus do not conflict."
- limits: Example adapted by the authors from Cahill et al. Applies to snapshot isolation (PostgreSQL REPEATABLE READ, Oracle "serializable"); also occurs at READ COMMITTED. Prevented by SERIALIZABLE (PostgreSQL SSI or 2PL) or by SELECT … FOR UPDATE on the rows read.
- rights: VLDB 2012 notice permits personal/classroom copies with full citation; arXiv non-exclusive distribution license; reuse otherwise rights unstated — embed with attribution.

### E9: PostgreSQL's level table and level semantics
- claim: C7, C10, C11, C12, C13 (support)
- type: table+quote
- source: PostgreSQL 18 Documentation §13.2 — https://www.postgresql.org/docs/current/transaction-iso.html
- locator: Table 13.1; §13.2.1–13.2.3
- asset: assets/postgresql18-table13-1-isolation-levels.png (1570×400 px); values in assets/tables.md. Quotes: "Read Committed is the default isolation level in PostgreSQL." / "The Repeatable Read isolation level is implemented using a technique known in academic database literature and in some other database products as Snapshot Isolation." / "Applications using this level must be prepared to retry transactions due to serialization failures."
- inspected: opened at full size; caption, all 4 rows and 5 columns visible
- notice: Same shape as the standard's table but with a fourth column, "Serialization Anomaly," which is "Possible" at every level except Serializable — the plain-language version of Berenson's point. "Allowed, but not in PG" marks where PostgreSQL is stronger than the standard requires.
- limits: PostgreSQL only; current manual (v18). Also useful from §13.2.1: an `UPDATE accounts SET balance = balance + 100.00 WHERE acctnum = 12345` re-checks the latest committed row, so single-statement increments do not lose updates in Read Committed; the website.hits = 9/10 DELETE example shows a case that misbehaves.
- rights: PostgreSQL Licence ("Permission to use, copy, modify, and distribute this software and its documentation for any purpose, without fee…"), keep copyright notice "Portions Copyright © 1996-2026, The PostgreSQL Global Development Group".

### E10: Serializable mode catches the class/value write skew
- claim: C3, C10, C13 (support)
- type: quote+metric
- source: PostgreSQL 18 Documentation §13.2.3 — https://www.postgresql.org/docs/current/transaction-iso.html
- locator: §13.2.3, mytab example
- asset: Table mytab rows (class, value): (1,10), (1,20), (2,100), (2,200). A sums class 1 = 30, inserts (2,30); B sums class 2 = 300, inserts (1,300). At Repeatable Read both commit; at Serializable one is rolled back with "ERROR:  could not serialize access due to read/write dependencies among transactions". Reason quoted: "if A had executed before B, B would have computed the sum 330, not 300, and similarly the other order would have resulted in a different sum computed by A."
- inspected: not applicable (text)
- notice: A second write-skew example built from plain SELECT SUM and INSERT; the arithmetic lets the reader check that no serial order gives (30, 300). Also shows what "help" looks like in practice: an error the app must retry, not a silent fix.
- limits: PostgreSQL behavior. Error and SQLSTATE 40001 are PostgreSQL-specific wording.
- rights: as E9.

### E11: Serialization graphs — why there is no valid order
- claim: C4, C10 (support)
- type: figure
- source: Serializable Snapshot Isolation in PostgreSQL — https://arxiv.org/abs/1208.4179
- locator: Figure 3 (PDF p. 4), §3.1
- asset: assets/ports2012-fig3-serialization-graphs.png (1059×693 px)
- inspected: opened at full size; both graphs, edge labels (rw, wr) and caption visible
- notice: Each arrow means "must come before." In (a) T1 must precede T2 and T2 must precede T1 — a cycle — so no one-at-a-time order exists. That is the general test for "wrong result": a cycle in this graph. (b) shows a three-transaction case where even a read-only report takes part.
- limits: Requires explaining rw-antidependency ("T2 read the old version of something T1 wrote, so T2 appears to come first"). Optional for the reader; use only if the report explains the general rule.
- rights: as E8.

### E12: Same name, different guarantee — tested behavior
- claim: C10, C11 (support); C12 (context); C17 (qualify)
- type: table+quote
- source: Hermitage — https://github.com/ept/hermitage (master @ 2026-01-23)
- locator: README "Summary of test results" table, legend, "Caveats"
- asset: text table transcribed in assets/tables.md (PostgreSQL, MySQL/InnoDB, Oracle rows). Quote: "It's not the speed that matters, it's the ordering of events."
- inspected: not applicable (markdown table; rows copied from raw README and checked)
- notice: Column P4 (Lost Update): PostgreSQL "repeatable read" ✓, MySQL "repeatable read" ★ (the default) —, Oracle "read committed" ★ —. Column G2-item (write skew): — for everything except the "serializable" rows, and Oracle "serializable" is actually snapshot isolation. Shows that a level's name tells you less than its tested behavior.
- limits: Tests run by hand on particular versions (PostgreSQL scripts: 9.3.5); results can show presence, not prove absence. Uses Adya-style anomaly names; map for reader: P4 = lost update, G-single = read skew, G2-item = write skew.
- rights: CC BY 4.0 (Copyright Martin Kleppmann, 2014) — reuse with attribution.

### E13: Runnable two-session lost update in SQL
- claim: C3, C10, C13 (support)
- type: quote
- source: Hermitage postgres.md — https://github.com/ept/hermitage/blob/master/postgres.md
- locator: sections "Lost Update (P4)" and "Write Skew (G2-item)"; setup `create table test (id int primary key, value int); insert into test (id, value) values (1, 10), (2, 20);`
- asset: Read committed script:
  ```
  begin; set transaction isolation level read committed; -- T1
  begin; set transaction isolation level read committed; -- T2
  select * from test where id = 1; -- T1
  select * from test where id = 1; -- T2
  update test set value = 11 where id = 1; -- T1
  update test set value = 11 where id = 1; -- T2, BLOCKS
  commit; -- T1. This unblocks T2, so T1's update is overwritten
  commit; -- T2
  ```
  At repeatable read, the same steps end with T2 getting "ERROR: could not serialize access due to concurrent update" and aborting.
- inspected: not applicable (text copied from raw file)
- notice: The reader's own SQL vocabulary (SELECT, UPDATE) in two windows. Both sessions read 10 and each decides to write 11 (think "+1"); the result is 11, not 12. At the stronger level, the database refuses the second write instead.
- limits: Run on PostgreSQL 9.3.5; current PG 18 docs describe the same RR error. The script writes a constant computed from the earlier read; it models application-side read-modify-write.
- rights: CC BY 4.0.

### E14: Cost of serializability — throughput relative to snapshot isolation
- claim: C14 (support); C9 (context)
- type: figure+metric
- source: Serializable Snapshot Isolation in PostgreSQL — https://arxiv.org/abs/1208.4179
- locator: Figure 5 (PDF p. 11), §8.2; §1 summary
- asset: assets/ports2012-fig5-dbt2-throughput.png (2168×759 px). Metrics: "our serializable mode has a performance cost of less than 7% relative to snapshot isolation" (§1); in-memory DBT-2++ "SSI causes a 5% slowdown relative to snapshot isolation" (§8.2); disk-bound "serialization failure rate was under 0.25%"
- inspected: opened at full size; both panels, axes (0.4x–1.0x normalized rate vs. 0–100% read-only fraction), legends and caption visible
- notice: The y-axis is throughput as a fraction of snapshot isolation (1.0x). The blue SSI line stays near the top; the red S2PL (classic locking serializable) line drops to about 0.43x at 90–95% read-only transactions in panel (a). Reading: serializability's cost depends heavily on how it is implemented and on workload.
- limits: PostgreSQL 9.1, 2011–2012 hardware, DBT-2++ (TPC-C variant with an added "credit check" transaction); S2PL is the authors' own simple implementation. Not a general rule for other databases.
- rights: as E8.

### E15: RUBiS application benchmark
- claim: C14 (support)
- type: table
- source: Serializable Snapshot Isolation in PostgreSQL — https://arxiv.org/abs/1208.4179
- locator: Figure 6 (PDF p. 11), §8.3
- asset: assets/ports2012-fig6-rubis.png (1043×334 px); values in assets/tables.md (SI 435 req/s, 0.004% failures; SSI 422, 0.03%; S2PL 208, 0.76%)
- inspected: opened at full size; 3 rows, 2 columns, caption visible
- notice: On an eBay-like auction workload (85% read-only), serializable via SSI kept 97% of snapshot isolation's throughput (422/435), while locking-based serializable got under half (208/435) and aborted more.
- limits: Single benchmark, 2012 hardware, PHP RUBiS "bidding" mix; ratio computed here (422/435 ≈ 0.97; 208/435 ≈ 0.48).
- rights: as E8.

### E16: Defaults are rarely serializable (2013 survey)
- claim: C12 (support, historical); C11 (context)
- type: table+metric
- source: Highly Available Transactions: Virtues and Limitations — https://arxiv.org/abs/1302.0309 (v2)
- locator: Table 2 and §3 text (PDF p. 3)
- asset: assets/bailis2013-table2-default-isolation.png (1051×972 px); values in assets/tables.md. Metric: "only three out of 18 databases provided serializability by default, and eight did not provide serializability as an option at all" (January 2013).
- inspected: opened at full size; 18 rows, legend and caption visible
- notice: Shows how normal weak isolation is: Postgres, SQL Server, Oracle all defaulted to read committed; Oracle's maximum was snapshot isolation.
- limits: January 2013, vendor-documentation survey, old versions; current defaults verified only for PostgreSQL 18 (RC) and MySQL 8.4 (RR).
- rights: CC BY-NC-SA 3.0 (arXiv); attribute and note license.

### E17: Check-then-withdraw race in code
- claim: C3, C15, C16 (support)
- type: figure
- source: ACIDRain — https://doi.org/10.1145/3035918.3064037 (author PDF)
- locator: Figure 1 and caption (PDF p. 1)
- asset: assets/warszawski2017-fig1-withdraw-race.png (1059×1218 px)
- inspected: opened at full size; both code panels (a), (b) with line numbers and full caption visible
- notice: Four lines of code that are correct alone: read balance, check it covers the amount, write the new balance. Caption: two concurrent calls "could both read balance $100, check that $100 ≥ $99, and each allow $99 to be withdrawn, resulting $198 total withdrawals." Panel (b) wraps it in a transaction, and the caption warns that this is still vulnerable "at isolation levels at or below Read Committed, unless explicit locking such as SELECT FOR UPDATE is used."
- limits: Simplified pseudocode, not from a specific application.
- rights: ACM 2017 notice (personal/classroom use with citation); otherwise rights unstated — embed with attribution.

### E18: Real-world scale of concurrency bugs
- claim: C15 (support); C12, C11 (context)
- type: metric+table+quote
- source: ACIDRain — https://doi.org/10.1145/3035918.3064037
- locator: Abstract; §1; §4.2.5 and Table 2 (PDF p. 10); footnote 6 (p. 9)
- asset: assets/warszawski2017-table2-anomalies-by-db.png (1050×571 px). Metrics: 22 verified vulnerabilities in 12 e-commerce applications (four languages), software deployed on ~2M websites; 5 level-based (4 lost update, 1 phantom), 17 scope-based. Flexcoin quote (from the exchange's statement, as quoted in §1): "By sending thousands of simultaneous requests, the attacker was able to “move” coins from one user account to another until the sending account was overdrawn, before balances were updated." Footnote 6: "we were surprised to trigger Lost Updates under MySQL Repeatable Read anyway".
- inspected: Table 2 image opened at full size; 4 rows, all columns, caption visible
- notice: Table 2: under each database's default, all 5 level-based attacks work; at the maximum level 0 or 1 remain — but the "Remaining" 17 survive any level because the code never put the steps in one transaction. Isolation levels help only with what is inside a transaction.
- limits: ~2M is deployment reach (builtwith.com), not exploited sites; 8 of 22 attacks needed 200 ms injected delay. Flexcoin details come from the company's statement; corroborated by March 2014 news coverage of the closure (896 BTC), but no independent technical analysis read.
- rights: as E17.

### E19: Implementation bug in serializable mode (fixed)
- claim: C17 (support)
- type: quote
- source: PostgreSQL 12.4 Release Notes — https://www.postgresql.org/docs/release/12.4/ (with Jepsen, https://jepsen.io/analyses/postgresql-12.3, June 2020)
- locator: 12.4 release notes, item "Fix conflict-checking anomalies in SERIALIZABLE isolation mode (Peter Geoghegan)"
- asset: "This could allow a serializable transaction to commit when it should have failed with a serialization error."
- inspected: not applicable
- notice: Independent testing (Jepsen) found a case where PostgreSQL's serializable mode let a write-skew-type anomaly through; the project fixed it in August 2020. Guarantees depend on correct implementation.
- limits: Rare three-transaction case; fixed; not current behavior. Jepsen full text read only via summary — do not quote Jepsen verbatim.
- rights: PostgreSQL Licence.

### E20: Why it matters operationally — silent corruption
- claim: C15 (support); C2 (context)
- type: quote
- source: Serializable Snapshot Isolation in PostgreSQL — https://arxiv.org/abs/1208.4179
- locator: §2 (PDF p. 2) and §2.2 (p. 3)
- asset: "snapshot isolation anomalies are difficult to deal with because they typically manifest themselves as silent data corruption (e.g. lost updates)." (source text uses a ligature in "difﬁcult")
- inspected: not applicable
- notice: Explains why these bugs persist: no error, wrong data, discovered later and hard to reproduce. §2.2 adds the Wisconsin Court System case: hundreds of tables and 20+ programmers made checking every pair of transactions for conflicts infeasible — the argument for using serializable rather than reasoning case by case.
- limits: Authors' experience/argument, not a measurement.
- rights: as E8.

## Claims lacking evidence or with only weak exhibits

- C1: no exhibit needed (textbook background; Berenson §2.1 definition sentence available if wanted: "A transaction groups a set of actions that transform the database from one consistent state to another.").
- C9: multiversion mechanism has quote support only (PG §13.1: "reading never blocks writing and writing never blocks reading"; Berenson §4.2 SI definition); no source diagram of version chains extracted — none found in the sources read.
- C14: single source (Ports & Grittner 2012); no current cross-vendor measurement.

## Candidates omitted or not extracted

- Berenson Table 3 (four phenomena incl. P0): superseded by Table 4 for reader use; not extracted.
- Ports & Grittner Figure 2 (batch-processing three-transaction anomaly) and Figure 4 (SIBENCH): Figure 2 is a harder second example; Figure 4 duplicates Figure 5's message. Not extracted.
- PostgreSQL website.hits DELETE example (§13.2.1): text only; available in source if a writer wants a Read Committed oddity.
- MySQL manual's x-lock trace example: too implementation-specific for this reader.
- Hermitage full table for SQL Server, CockroachDB, YugabyteDB, Memgraph: transcribable from README if needed; omitted from tables.md for focus.
- Adya et al. ICDE 2000 definitions: source inaccessible (pmg.csail.mit.edu refused connection).
- Jepsen PostgreSQL 12.3 figures: not extracted (read via summary only).
