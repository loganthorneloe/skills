# Run notes

## Deliverable and scope
- report.html: complete source-audited explanation for a reader who knows SELECT/UPDATE; PostgreSQL 18 examples explicitly distinguished from standard minimum guarantees.
- Self-contained body styling, figure, and actual font bytes. Opening source PDF or enlarged PNG uses companion files; outbound evidence links need network.
- dag.json preserves initial graph, first evidence round, final research round, and validation. dag.svg / dag.html render the final graph. This research dependency graph is distinct from database serialization graphs.
- Approximate elapsed time: 7.6 minutes.

## Research actually read
1. https://www.postgresql.org/docs/18/tutorial-transactions.html — §3.4 complete tutorial, transaction boundaries, atomicity, implicit transactions.
2. https://www.postgresql.org/docs/18/transaction-iso.html — definitions, Table 13.1, Read Committed update rechecking, Repeatable Read snapshots/conflicts, Serializable monitoring and example. Full relevant sections retrieved across search and open calls.
3. https://www.postgresql.org/docs/18/mvcc-intro.html — complete §13.1, multiple versions and reader/writer concurrency.
4. https://www.postgresql.org/docs/18/sql-set-transaction.html — syntax and description, exact snapshot timing and level-setting restrictions.
5. https://www.postgresql.org/docs/18/explicit-locking.html — introduction; row lock section §13.3.2; deadlock section §13.3.4; inspected lock matrices for usefulness.
6. https://www.postgresql.org/docs/18/mvcc-serialization-failure-handling.html — complete §13.5, SQLSTATE 40001 and retrying all transaction logic.
7. https://www.postgresql.org/docs/18/ddl-constraints.html — §5.5 introduction, check constraints and cross-row limitation, not-null context; unique constraint identified in section structure and project feature list. Used only basic unique/check claims.
8. https://arxiv.org/pdf/1208.4179 — paper first page, §§2.1, 2.1.1, 2.1.2, 2.2, 3, 3.1–3.3; Figure 1 extracted from PDF p.2 (printed p.1851), viewed original page and crop. Author affiliations and firsthand implementation contribution verified on first page.
9. https://www.postgresql.org/about/ — project identity and implementation ownership.
10. https://www.postgresql.org/docs/18/legalnotice.html — permission for documentation reuse.
11. Google Fonts CSS for Inter 400/500, Sora 600; font URLs from that stylesheet downloaded, plus Google Fonts OFL files for both families.

## Evidence and exhibit choices
- Retained source-derived Table 13.1 as accessible HTML, transformed wording with explicit standard-vs-PostgreSQL distinction. Teaches the gap between three named read anomalies and serial equivalence.
- Retained original paper Figure 1, preserving labels, SQL, time arrow, and caption. Read full relevant surrounding sections before crop. It demonstrates different-row write skew, which the stock example cannot teach.
- Added constructed stock schedule to explain stale absolute writes without requiring internals. Explicitly not measured data.
- Did not reproduce paper Figure 2: three-transaction read-only anomaly is valid but adds prerequisites beyond this introductory central question. Mentioned limits of snapshots without asserting read-only transactions universally need Serializable.
- Did not reproduce Figure 3 serialization dependency graphs: understanding edge types and false-positive SSI structures is unnecessary for explaining the isolation guarantee. The report gives the mechanism at conflict-monitoring level.
- Omitted old benchmark figures and percentages: PostgreSQL 9.1 measurements cannot answer current workload performance; not needed for this request.
- Omitted explicit-lock compatibility matrices: many lock names without additional explanatory value for this reader.
- No generated interactive control: the original figure and worked schedule resolve the relevant gaps; no invented numerical model.

## Reasoning review
- Distinguishes atomicity from isolation; overlapping lifetimes from simultaneous CPU execution; committed data from a stable transaction snapshot; stable snapshot from serializability.
- Lost-update schedule uses constant assignment; arithmetic UPDATE handled separately with PostgreSQL row recheck semantics.
- Multirow rule failure is distinct from collision on the same row.
- Serializable assumes complete correct transaction logic and consistently participating operations; retries include the read and application decision.
- Constraints enforce specific declared properties, not every business rule; external effects are not undone by a database rollback.
- Final graph expanded to include rule, write skew, lock behavior, and retry prerequisites. Every edge was reviewed against explanatory prose. Structural validity alone does not certify pedagogical quality.

## Verification
- Headless Chrome in a newly created isolated context; report rendered at 1440×1000 and 390×1000.
- Full-page screenshots saved as report-1440.png and report-390.png; desktop title/audit and mobile original figure visually inspected using desktop-detail.png and figure-mobile.png. Original full PDF page and cropped Figure 1 also inspected.
- No page-level horizontal overflow at either width (scrollWidth equals viewport width). Wide comparison tables scroll within their container.
- Image loaded at both sizes; all three actual FontFace entries report loaded (Inter 400/500, Sora 600).
- No JavaScript page errors; report readable with JavaScript disabled.
- No controls needing boundary testing. Keyboard Tab focus checked: link receives solid visible outline. Local enlarged-image and PDF links verified to exist.
- dag.json: 13 unique IDs; valid edge endpoints; acyclic; every node reaches target. Final rendered graph image loads without page overflow in isolated Chrome; screenshot dag-preview.png.
- No local PostgreSQL executable found; SQL schedules are source-grounded worked reasoning, not claimed live database tests.

## Access gaps and recoveries
- arXiv HTML endpoint returned 404; original PDF retrieved and read instead.
- Initial sandbox downloads could not resolve hosts; authorized read-only network escalation downloaded cited PDF and public fonts successfully.
- Default Playwright browser binary missing; used installed Google Chrome in isolated context. Sandbox blocked Chrome startup; authorized escalation succeeded.
- Full SQL standard text not accessed; minimum guarantee table is sourced to PostgreSQL’s explicit account of it, with that limitation stated in audit.
- Original figure is retained for personal educational use with citation and paper permission context; public redistribution may require permission. Font licenses retained beside report and embedded as HTML comments.
