# Run notes

Started about 11:07, finished about 11:15 CST, 2026-11-03 (about 8 minutes of writing and checking; research packet supplied).

## Decisions

- Claim ranking: C2, C3, C4, C6, C7, C10, C13 got full mechanism and evidence. C8 and C11 are treated as the main caveats. C1, C5, C9, C12, C14, C15, C16 and C17 get a paragraph or a sentence each.
- One worked example runs through the report: a balance of 100 with deposits of +20 and +30 (Berenson H4 numbers), shown as a two-session SQL timeline I wrote and labeled as an illustration. It comes back in the snapshot-isolation paragraph (B is refused, retried, ends at 150) and in the fixes paragraph. The doctors-on-call write skew is the only second example, because snapshot isolation needs a case that the first example cannot show.
- Exhibits embedded (5): ACIDRain Fig. 1 (E17), PostgreSQL Table 13.1 (E9), Berenson Table 4 (E4), Ports & Grittner Fig. 1 (E8) and Fig. 5 (E14). Quotes used: E7 (in paraphrase), E9, E10, E13 error text, E18 Flexcoin phrase, E19 release-note sentence. RUBiS numbers (E15), defaults survey (E16) and ACIDRain counts (E18) are in prose rather than images.
- Not embedded, on purpose: Berenson Table 1 (PostgreSQL's table makes the same point with the serialization-anomaly column), Table 2 (locking durations given in one prose sentence), Figure 2 hierarchy, Ports Fig. 3 graphs (the "both can't be first" sentence carries the cycle idea without the rw-antidependency vocabulary), HAT Table 2 image, ACIDRain Table 2 image, Hermitage script (its 10 → 11 numbers would have introduced a second example; its RR error message is used instead).
- No interaction or generated diagram: the timeline table and source figures covered the comprehension gap; a stepper would have restated them.
- Vocabulary: Berenson/standard names only; Adya G-codes left out.
- Sources listed: all eight passing or conditional records (Adya failed and is omitted). Entries shortened from the packet drafts.
- Rights: ACIDRain and Ports & Grittner figures carry "rights unstated beyond personal/classroom use" notes in their captions; Berenson figure carries the ACM 1995 notice; PostgreSQL table carries its copyright notice and licence.

## Verification

- Voice pass done: removed one unsourced claim ("cheaper than its reputation suggests"), named the 2013 survey's authors where it is used, checked for colon-label phrasing and analogies (none).
- Fact check against records: lost update at PostgreSQL RC and MySQL RR (Hermitage, ACIDRain fn. 6); single-statement UPDATE nuance (PG §13.2.1); RR = SI and both error messages (PG §13.2.2–13.2.3, Hermitage); Oracle "serializable" = SI stated as per Hermitage's tests; defaults PG RC / MySQL RR from current manuals, 3 of 18 marked as January 2013; 7% / 422 / 435 / 208 / ~0.43x with 2012 PostgreSQL 9.1 limits stated; ACIDRain 22 / 12 / 5 (4 lost update, 1 phantom) / 17; Jepsen bug quoted via release notes only.
- Rendering (Python Playwright, Chromium, file:// URL): 1280px and 390px full-page screenshots inspected. No horizontal page scroll at either width (scrollWidth equals clientWidth). All 5 images load (naturalWidth > 0) and none render above natural size. At 390px, the three wide exhibits and the timeline sit in keyboard-focusable horizontal scroll regions; each figure links its full-size file. No console errors or failed requests.
- Fonts: after document.fonts.ready, document.fonts.check('600 1em Sora') and document.fonts.check('400 1em Inter') both returned true at both widths. Fonts load from Google Fonts, so offline viewing falls back to system sans-serif.
- Fix made after the first render: at 390px the wide images expanded to natural width inside their scroll regions; set them to 680px. The timeline's caption was clipped inside its scroll region; moved to a figcaption outside it.
- Controls: none in the report, so no control-state checks applied.

## Gaps

- Network dependency for fonts (Google Fonts stylesheet).
- Oracle behavior rests on Hermitage's tests of an older release; no current Oracle documentation in the packet.
- Cost numbers come from a single 2012 study.
- Jepsen report known only from a summary; only the release-note text is quoted.
