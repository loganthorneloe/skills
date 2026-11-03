# Run notes

Approximate elapsed time is 25 minutes (11:07 to about 11:32 CST, 2026-11-03).

## Decisions
- Used the frozen research packet as the audit and evidence records and started at step 3. No new sources were added and no source URLs were opened.
- All eight passing or conditional sources appear in the audit section: Berenson 1995, PostgreSQL 18 docs, MySQL 8.4 manual, Ports & Grittner 2012, HAT 2013, ACIDRain 2017, Hermitage, and the PostgreSQL 12.4 release notes with Jepsen. Adya 2000 failed (inaccessible) and is left out.
- Six image exhibits are embedded, copied to assets/: E17 (ACIDRain Fig. 1), E8 (Ports Fig. 1), E9 (PG Table 13.1), E4 (Berenson Table 4), E14 (Ports Fig. 5), and E18 (ACIDRain Table 2). E1 (H4), E7, E10, E13, E15, E16, E19, and E20 appear as quotes or metrics in the prose. E12 (Hermitage) is a transcribed HTML table under CC BY 4.0. E2 (H1) is in the anomaly synthesis table.
- Not embedded: Berenson Table 1, Table 2, and Fig. 2, which Table 4 and the PG table already cover, with the locking mechanism explained in prose. Also not embedded: Ports Fig. 3 (the conflict-cycle idea is explained in prose with the deposit example), Fig. 6 (numbers given in prose), and HAT Table 2 (stat in prose).
- The worked lost-update timeline comes from H4 and is labelled as built for the report.
- One interaction was added: a step-by-step deposit interleaver. The reader chooses which transaction steps next and which level/query style applies (PG Read Committed, PG Repeatable Read/snapshot, or a single atomic UPDATE), then sees the committed balance, each transaction's state, a log, and a verdict. It closes a specific gap: only some orders lose data, and the stronger level reports an error and needs a retry instead of fixing the problem silently. The stated simplification is that UPDATE and COMMIT are one step, so the wait a real database adds does not appear. A noscript fallback states the outcomes.
- Caveats are placed beside their claims: MySQL RR lost updates, Oracle "serializable" = SI per Hermitage, 2013 survey is historical, 7% is one 2012 study, isolation can't fix logic outside a transaction, and the fixed PG SSI bug.
- Fonts load from the Google Fonts stylesheet (network dependency). Images are local relative files.

## Verification
- Ran the voice pass. There is no colon-label phrasing and no analogies, and caveats sit beside their claims. A sentence saying "most implementations" of RR refuse lost updates was an overstatement and was changed to name PostgreSQL and Berenson's locking definition, with MySQL excluded.
- Checked facts against the records. Each claim C1–C17 maps to a passing or conditional record, and the numbers (130/150, $198, 3 of 18, 435/422/208, failure rates, <7%, 22/5/17) match the records.
- Rendered with Python Playwright/Chromium at 1280 and 390 px. Sora 600 and Inter 400 both returned true from document.fonts.check after fonts.ready at both widths. There were no console errors and all 6 images loaded. No image is upscaled: displayed widths are at most natural size, and the 2x PG screenshot is capped at 785px. scrollWidth equals clientWidth at both widths.
- Fixes made after the first render: the select overflowed at 390px (scrollWidth 619) and was capped at 100%. The PG table was unreadable at 390px and was moved into a focusable horizontal scroll region at 700px. Wide figures (Table 4, Fig. 5) scroll at 880px on mobile and link to full-size files. Table wrappers are focusable regions.
- Interaction checks, all observed:
  - Default state: balance 100, both transactions waiting to SELECT.
  - RC with A-read, B-read, A-write, B-write gives 130 and the "lost 20" verdict.
  - RC with B-first interleaving also gives 130.
  - RC serial (A, A, B, B) gives 150.
  - RR with the interleaved order: B fails with the serialization error and the balance is 120. Retrying gives 150 "after retry", and both buttons are disabled at the boundary.
  - Atomic UPDATE with the interleaved order gives 150.
  - Reset and mode change re-initialize.
  - Keyboard: Enter on a focused button runs a step, Tab moves to the next control, and focus outlines show.
  - With JavaScript disabled, the noscript text renders.

## Gaps
- Oracle behavior rests on Hermitage (older version) and the 2013 survey. No current Oracle docs were in the packet, and the report says so.
- Jepsen was read only in summary, so the report quotes the release notes instead.
- Rights for ACM/VLDB exhibits are unstated beyond their copying notices. The captions say so.
- The report needs network access for brand fonts. Offline, it falls back to system sans-serif.
- No screen-reader test was run beyond the aria-live verdict and labelled controls.
