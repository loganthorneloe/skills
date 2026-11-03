# Run notes

Elapsed: about 6–10 minutes of wall-clock time for steps 3–6 by the system clock (11:10 to 11:16 CST, 2026-11-03), starting from the frozen research packet.

## Decisions
- Sources shown: six of seven audited sources (Hernán & Robins; LaLonde 1986; IES 2007; Muralidharan et al. 2019; Escueta et al. 2017; Gertler et al. 2016). Mixtape dropped: its claims (C1–C4, sign reversal) were carried by Hernán & Robins and the constructed example, saving words.
- Ranked claims: C1, C2, C4, C7 got full treatment; C3, C6, C9 carried evidence; C5, C8, C10, C11 got one or two sentences each. C10's attrition detail (84% vs 88% follow-up) was cut for length; offer-vs-use (58% attendance), bundled program, and setting limits kept.
- Worked example: the packet's six-student constructed example (E16), labeled as constructed, carried through the report and into the interactive.
- Exhibits embedded: E6 (IES Table II.6, public domain) and E8 (Mindspark Figure 2, rights unstated, embedded at natural 595 px with attribution and rights note; link to captioned render). E9 (LaLonde) rebuilt as a three-row HTML table with attribution, per its record, since table rights are publisher-held. E1 (Hernán Figure 1.1, all rights reserved) not embedded; its point is carried by the E14 numbers in prose. E5 balance table not embedded; balance is shown by E8's baseline bars.
- Quotations limited to one short quote (Hernán & Robins, "In ideal randomized experiments, association is causation.").
- Interactive: one lottery simulator (class size 6/60/600, new lottery, reset) resolving the gap "randomization works on average, so why check balance and report chance?" Constructed model stated beside it. Seeded RNG so reset is reproducible. No-JS fallback text gives exact/simulated ranges (6 students: all 20 lotteries give −14 to +18, average 2; 60: ~−2.1 to +6.3; 600: ~+0.6 to +3.3, computed separately in node and matching the page).
- Word count: about 1,260 reading words excluding source titles, metadata lines, captions, tables, and the model note (slightly over the 1,200 guide after two trimming passes).

## Verification (Playwright, Python, headless Chromium)
- 1280 px and 390 px: no console errors, no failed requests, no horizontal page overflow (scrollWidth − innerWidth = 0 at both).
- Fonts after document.fonts.ready: document.fonts.check('600 1em Sora') true, check('400 1em Inter') true, check('500 1em Inter') true, at both widths (Google Fonts loaded over network).
- Images: both load (naturalWidth 1826 and 595); Mindspark figure shown at natural 595 px (never upscaled) and in a keyboard-focusable scroll region on narrow screens; IES table 900 px at desktop, scroll region with min-width 560 px plus full-size link on mobile.
- Screenshots inspected at both widths. Fixed after inspection: wide-figure caption misaligned (constrained to 720 px), Mindspark figure shrinking on mobile (moved into scroll region), histogram text too small on mobile (SVG now re-renders at container width with 12 px labels; labels staggered to avoid overlap), empty SVG space in no-JS view (hidden until JS runs).
- Controls: default (60 students, +2.8 gap, 95% −2.1 to +6.3), changed (6 students: enumerates "only 20 lotteries", range −14 to +18; 600: 95% +0.6 to +3.3), boundary sizes 6 and 600 both exercised, reset restores default state exactly, keyboard Tab reaches the button and Enter triggers a new draw, aria-live result and SVG aria-label update. Fixed "−0.0" formatting and a misleading "95%" statement for the 6-student case.
- No-JS render: readable fallback text present; controls inert.
- Factual check against records: every figure in prose traced to audit/evidence records (54%/43%; +$886/+$798, −$15,578/−$8,067, −$8,870/−$4,416; 0.73, 0.03 SD, p = 0.34, 0–2 percentile points; 0.37/0.23 SD published; 58% attendance; 29 RCTs = 20/8/1; World Bank −14.46 vs −10.14 ≈ 43% larger, stated as "about 40%"). Hindi 0.23 described as "encouraging" per the Escueta rule of thumb, not "large".

## Gaps
- Fonts depend on network access to Google Fonts; offline viewing falls back to system sans-serif.
- Mindspark figure is from the 2017 working paper while headline numbers are the published 2019 values (figure bar values differ slightly); caption names the working paper.
- No source audited a consumer phone app; the report says so in its closing.
- Reverse causation is stated as settled reasoning without a source exhibit (packet gap C5).
