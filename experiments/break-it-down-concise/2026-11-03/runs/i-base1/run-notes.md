# Run notes

Elapsed: about 7 minutes of writing and verification (11:07 to about 11:14 CST, 2026-11-03), starting from the frozen research packet.

## Decisions
- Structure: title, source audit (8 passing/conditional sources; Adya 2000 omitted as failed/inaccessible), direct answer, then prerequisite order: transaction and invariant, serializability, lost update (ACIDRain Fig. 1, Berenson H4, Hermitage two-session SQL), write skew (Ports & Grittner Fig. 1 and Fig. 3), anomaly glossary, isolation levels (PostgreSQL Table 13.1, Berenson Table 4, locking vs snapshots, Berenson Fig. 2), product differences (Hermitage synthesis table, Bailis 2013 Table 2), cost (retries, PostgreSQL mytab example, Ports & Grittner Fig. 5 plus RUBiS numbers in prose), limits (ACIDRain Table 2, mitigation list, PostgreSQL 12.4 bug).
- One interaction: choose one of six interleavings of two read-modify-write transactions and a database/level; shows step trace, final balance, and abort + retry where applicable. Purpose is to show that 4 of 6 orders lose an update at both defaults and that stronger PostgreSQL levels refuse rather than reorder. Logic is deterministic arithmetic; level behavior follows Hermitage P4 tests and PG 18 docs. Static default state is in the HTML for no-JS readers.
- Hermitage and glossary tables are labeled synthesis tables in HTML; Berenson Table 1, Table 2 (locking), Ports Fig. 6, and Hermitage full table were described in prose rather than embedded.
- Single-statement `balance = balance + n` nuance kept beside the lost-update example (PG §13.2.1). The conditional-WHERE variant in the mitigation list is an extension of that documented re-check behavior.
- Oracle claims attributed to Hermitage's tests; 7% cost presented as one 2012 study; ACIDRain 17 scope-based bugs used to correct the "raise the level" premise.

## Verification
- Voice pass: removed colon-label "Assumptions:", tightened claims ("Most widely used" -> "Many"; "every wrong result in this report" -> non-serializable outcomes generally). Prose checked against claims C1–C17; each maps to a pass/conditional record.
- Playwright (python, Chromium) at 1280px and 390px: no horizontal page overflow (scrollWidth equals viewport at both), no broken images, no upscaled images, no console/page errors. After document.fonts.ready, document.fonts.check('600 1em Sora') and ('400 1em Inter') returned true at both widths (Google Fonts reached over network).
- Screenshots inspected: wide exhibits (PG Table 13.1, Berenson Table 4, Ports Fig. 5) sit in focusable horizontal scroll regions on mobile with full-size links; Hermitage table scrolls on mobile; glossary table changed to fit width after first inspection.
- Control: all 24 order x level combinations operated. pgrc and myrr: serial orders 150, interleaved 130/120/130/120. pgrr and pgser: 150 everywhere (abort + retry rows shown). Reset restores ABAB / pgrc / 130 and focuses the first select. aria-live outcome region. With JavaScript disabled, the default outcome text renders.
- Keyboard: selects and button are native and focusable with visible red focus outline; a scripted ArrowDown on a closed select did not change the value in headless Chromium (native popup behavior), so keyboard value change was not confirmed by script.

## Gaps
- Fonts load from Google Fonts; offline viewing falls back to system sans-serif.
- Exhibits whose reuse terms are unstated (ACIDRain, Ports & Grittner) are embedded with attribution and that status noted in captions.
- No new sources consulted; packet limits carry over (Jepsen read only in summary, Oracle behavior from Hermitage, cost data from one 2012 study).
