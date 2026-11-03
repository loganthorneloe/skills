# Research and delivery notes

Task: explain transaction isolation to a reader comfortable with basic SELECT/UPDATE. Applied supplied baseline instructions only. No research graph required or created. Approximate elapsed time: 20 minutes.

## Deliverable

- `report.html`: complete standalone report, approximately 1 MB. Embedded Inter 400/500, Sora 600, original source-figure crop, inline CSS, no JavaScript, no external asset dependencies. Source hyperlinks require internet.
- `build_report.py`: report generation source.
- Supporting source downloads and screenshots remain in this run directory.

## Sources actually read and evidence

Read through web tools, then downloaded the paper and isolation HTML for asset/reference preservation. URLs appear in the report.

1. PostgreSQL 18 tutorial §3.4, Transactions: whole tutorial section including transfer example, atomicity, visibility, rollback, implicit transactions, savepoints. Used transaction boundaries and atomicity. Savepoint mechanics omitted as unrelated to core question.
2. PostgreSQL 18 §13.2, Transaction Isolation: definitions, Table 13.1, Read Committed details and account/website examples, Repeatable Read snapshot timing and update failures, Serializable example and dependency monitoring. Used table intact, two PG exceptions, statement versus transaction snapshots, retry and conflict semantics. Table is documentation evidence, not an experiment. Download preserved as source-isolation.html.
3. PostgreSQL 18 §13.1: complete short MVCC introduction, snapshot model and locking caveat. Used to explain row versions and concurrent reading/writing.
4. PostgreSQL 18 §13.3: table lock descriptions/table, full row lock subsection/table, deadlocks and advisory locks. Used row locks, waits, and deadlocks. Lock-mode matrices omitted because they add terminology without teaching the central failure. Advisory lock details omitted.
5. PostgreSQL 18 §13.5: entire serialization failure handling section. Used SQLSTATE 40001 and complete retry requirement; noted retries need not succeed immediately. Did not promise a fixed retry count.
6. PostgreSQL 18 §5.5: introduction, full CHECK subsection and its cross-row/NULL warnings, NOT NULL and beginning of UNIQUE; used constraints' limited scope. Exclusion/foreign-key implementation not explained.
7. PostgreSQL 18 BEGIN command reference: synopsis, description, notes, compatibility. Used syntax and autocommit boundary clarification.
8. Ports and Grittner (2012), Serializable Snapshot Isolation in PostgreSQL, PVLDB 5(12), pp.1850–1861: first-page abstract/overview/author affiliations and p.1851 §2, §2.1, full §2.1.1 and Figure 1. Read surrounding discussion of snapshot isolation versus serializability. Figure proves a possible write-skew schedule; no performance claims drawn from old benchmarks. Original PDF downloaded and second page rendered and visually inspected. Figure cropped with original labels, time arrow, proportions, and caption preserved.
9. PostgreSQL license page: permission to reuse documentation and required notices copied into report.
10. Google Fonts stylesheet and Inter/Sora OFL notices: downloaded actual font bytes, embedded in report, retained both licenses as HTML comments and companion text files.

## Exhibit decisions

- Included original PostgreSQL Table 13.1 with unchanged values and adapted typography. Shows that absence of three read anomalies is insufficient and differentiates PG from standard minima.
- Included original Figure 1 from Ports/Grittner p.1851: different rows can participate in one invalid decision. Both reads happen before either write. Full source PDF linked for enlargement; reuse permission/attribution retained for personal educational use.
- Added clearly labeled constructed lost-update timeline using a product count 10 → 11 instead of 12. This is an analytical example, not an observed trace. Its role differs from write skew: stale literal overwrite on the same row.
- Omitted source transfer SQL because it teaches atomicity but adds accounting machinery before concurrency. Explained grouping directly.
- Omitted the manual's class/sum serializability example: same logical lesson as the more accessible original doctor figure.
- Omitted paper performance plots and batch example: no performance recommendation or advanced multi-transaction anomaly is needed. Historical benchmarks cannot substantiate current performance.
- No generated diagram or interaction: the two source exhibits and explicit schedule already expose the relevant decisions and timing.

## Verification

- Isolated Playwright browser contexts; did not attach to existing sessions.
- Playwright's expected Chromium revision was absent. System Chrome used in an isolated temporary profile. Sandbox initially blocked launch; escalated read/render commands succeeded.
- Desktop 1440×1050: document scroll width = 1440. Mobile 390×844: document scroll width = 390. No page-level horizontal overflow.
- FontFaceSet reported Inter 400, Inter 500, Sora 600 all loaded on both viewports; checked real load statuses, not only CSS family names.
- Original figure complete, natural width 495; no failed images. Zero external asset elements. No browser page errors.
- JavaScript-disabled context retained title and image; report requires no JavaScript.
- Keyboard link focus had visible solid outline.
- Visually inspected desktop level-table region, mobile top/source audit, mobile figure region, desktop full source figure, mobile table region, and mobile SQL. Initial mobile figure labels were too small; repaired by preserving minimum image width in a keyboard-focusable horizontal scroll area, with a visible narrow-screen scroll hint.
- Verified ArrowRight moves both mobile exhibit scroll regions. Verified right boundaries: table 300px of 300px; figure 145px of 145px. Viewed rightmost screenshots; final column and right transaction remain accessible, not lost.
- `verification.json` and `scroll-verification.json` contain browser results. `desktop-*.png` and `mobile-*.png` preserve representative views. Scroll-hint addition followed the main screenshots; final right-edge checks ran on final HTML.

## Limits

- SQL examples were reasoned from documented PostgreSQL 18 semantics, not executed. No local psql found at common installation paths; did not install a database or claim runtime validation.
- Standard guarantees are represented through PostgreSQL's official table rather than a separately accessed ISO standard document.
- Source URLs were successfully read during research; did not automatically click every final hyperlink.
- Full figure uses educational/personal-use permission. No claim of unrestricted republication rights.
