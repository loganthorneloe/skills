# Run notes

Started 11:07 CST; finished about 11:12 (roughly 5 minutes by the system clock). Research packet used as-is; no new sources.

## Decisions
- Sources shown (6): Berenson 1995, PostgreSQL 18 docs, MySQL 8.4 docs, Ports & Grittner 2012, Hermitage, ACIDRain. Omitted HAT 2013 survey (C12 covered by current PG/MySQL docs) and Jepsen/PG 12.4 (C17 minor; cut for length). Adya not cited (inaccessible).
- Primary worked example: ACIDRain $100 / two $99 withdrawals (lost update), carried through the interaction. Berenson H4 mentioned in one sentence. Doctors-on-call (Ports Fig. 1) used only to show write skew past snapshot isolation.
- Exhibits embedded: ACIDRain Fig. 1, PostgreSQL Table 13.1, Ports & Grittner Fig. 1. Berenson Table 4 / Fig. 2 left out; PG table's "Serialization Anomaly" column carries the same point more simply.
- One interaction: a select for the isolation level applied to the withdraw race (RC, PG RR, MySQL RR, Serializable), showing step 4 and the outcome. Default state is in static HTML.
- Atomic `UPDATE ... WHERE balance >= 99` fix is an inference from PG §13.2.1 (re-check of WHERE on newest row version), stated as PostgreSQL behavior.

## Verification
- Word count of reading text (excluding metadata lines, captions, code) ≈ 1,210; target 1,000–1,200.
- Voice pass: removed "Basis:" colon-label notes; trimmed repeats; no recaps or closing summary.
- Fact check against records: fixed "weakest level most databases use" (unsourced) to "PostgreSQL's default level"; narrowed Serializable lost-update claim to PostgreSQL, MySQL, Oracle (rows in packet).
- Playwright Chromium at 1280 and 390: no horizontal page overflow, no console errors, all 3 images load, none upscaled (560/1059, 720/1570, 560/1043 px). Wide PG table scrolls horizontally in a focusable region at 390.
- After document.fonts.ready: fonts.check('600 1em Sora') = true, fonts.check('400 1em Inter') = true (fonts from Google Fonts; network required).
- Control: all four options produce the expected step-4 text and outcome; returning to default restores it; select receives keyboard focus. ArrowDown in headless did not change the native select (popup behavior), so keyboard value change not confirmed. With JS disabled the default (Read Committed) state renders.

## Gaps
- Oracle behavior rests on Hermitage only; MySQL serializable described generically as "blocked or rolled back".
- 7% cost figure is a single 2012 study, flagged in text.
- Fonts load from network; offline view falls back to system sans.
