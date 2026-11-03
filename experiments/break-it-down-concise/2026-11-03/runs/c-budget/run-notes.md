# Run notes

Elapsed: about 8 minutes of writing and checking (11:10 to 11:18 CST, 2026-11-03), starting from the frozen research packet.

## Decisions

- Reading-text length about 1,240 words (prose, headings, source entries, exhibit discussion, simulation note; excludes metadata lines, captions, tables, titles), near the 1,000–1,200 target. Trimmed from about 1,400.
- Sources shown: Hernán & Robins, Mixtape, IES 2007, Mindspark, LaLonde, Escueta et al., World Bank (all pass or conditional for the claims they support). World Bank used only for C11; its fictional HISP numbers were not cited.
- Exhibits embedded (copied to `assets/`): E9 LaLonde Table 5 (rights unstated, caption says so), E6 IES Table II.6 (public domain), E8 Mindspark Figure 2 with note (rights unstated, caption says so). E1 Hernán figure not embedded (all rights reserved); its point carried by E14 metrics in prose and one short quote (E14). E5 balance table summarized in one sentence rather than embedded to save length.
- Constructed six-student table (E16) rebuilt as an HTML table, labeled as invented.
- One interaction: coin-flip simulation (6 vs 600 students) to close the C8 gap (chance variation in small randomized groups, convergence to the true effect). Input is class size and flips; output is latest gap, running average, count; aria-live; noscript fallback with simulated figures (20,000-run check: 29% of six-student flips land 10+ points from 2; 86% of 600-student flips land within 1 point).
- Fact fixes during review: Hernán example reworded (average effect zero, 50% vs 50%, not "changes nobody's outcome"); p-value phrased as "at least this large"; Mindspark attendance phrased as average attendance 58%; "a lottery" removed from the non-randomized designs list; published (AER) Mindspark figures 0.37/0.23 used, figure caption notes the working-paper version.
- Heading "The fix: ..." renamed to avoid colon-label phrasing.

## Verification

- Playwright Chromium at 1280 and 390 px: `document.fonts.check` true for 600 Sora and 400 Inter after `fonts.ready`; no page errors; no horizontal page overflow (scrollWidth equals viewport); all three images loaded at natural sizes 1814/1826/1356 px, displayed no larger than natural. On 390 px the two wide tables sit in focusable horizontal scroll regions with full-size links.
- Screenshots of full page at both widths inspected: no clipping or broken assets; brand palette, tiles, hairlines as specified.
- Simulation operated: default state "none yet"/0; single flip; 20 flips; class-size change resets; 600-student flips average near +2; reset; keyboard Enter on focused button works. Six-student single flips varied widely (+0.5, -5.2, +15.5), matching the text's claim.
- JS disabled: noscript explanation renders inside the simulation panel.

## Gaps

- Fonts load from Google Fonts; offline viewing falls back to system sans-serif.
- Exhibit images are local copies; LaLonde and Mindspark reuse rights unstated.
- Research gaps carried from the packet: no audited trial of a self-study phone app (stated in report); reverse causation stated as settled reasoning; Mindspark read from the working paper plus published abstract.
- The shared scratchpad held a `check.py` from another process that overwrote mine; its output was ignored and checks were rerun with a separate script.
