# Run notes — mRNA vaccines

Elapsed: about 15 minutes by system clock (12:37–12:52 CST, 2026-11-03).

## Decisions
- Nine claims (C1–C9) covering delivery, translation, immune training, persistence of germinal centres, efficacy, modified bases, non-integration, mRNA lifetime, and the Aldén cell-line challenge.
- Exhibits embedded: FDA Figure 2 (cumulative incidence; US government document), Turner et al. Fig. 2 (author manuscript via PMC; rights unstated, attributed and stated in caption), Fertig et al. Fig. 1 (CC BY 4.0).
- Nobel press-release Figure 2 downloaded but NOT embedded: nobelprize.org terms forbid reproduction outside press/legal/educator exemptions. Linked instead. Images moved out of assets/.
- Pardi et al. figures not used (rights unclear, too technical).
- Two generated SVGs: mechanism diagram and a synthesis timeline (labelled as drawn for the explanation, with data points from E1, E3, E4). No interactive control: no comprehension gap needed one.
- Distilled: non-source prose 1951 → 1070 words (55%); total incl. source entries 2486 → 1463 (59%). Source entries are required, which kept total above half. All five visuals kept.

## Sources read
CDC how-they-work page (fetch-tool summary with verbatim quotes; direct curl/Playwright blocked by Akamai); Pardi et al. 2018 (PMC author manuscript, rendered via Playwright); Nobel 2023 press release (full, curl); FDA VRBPAC briefing PDF (pp. 6, 23–31); Turner et al. 2021 (PMC author manuscript via Playwright); Fertig et al. 2022, Aldén et al. 2022, Merchant 2022 comment (Europe PMC full-text XML). Records in records/audit.md and records/evidence.md.

## Verification
- Fonts: document.fonts.check('600 1em Sora') and ('400 1em Inter') true at 1280 and 390 (after fonts.ready), draft and report.
- No horizontal page overflow at 1280 or 390 (scrollWidth == clientWidth); no broken or upscaled images; no console errors or failed requests.
- Screenshots inspected (scratch/report-*.png, r-*-el*.png): fixed diagram label overlap and nucleus text overflow; on narrow screens SVGs and wide figures sit in keyboard-focusable horizontal scroll regions (confirmed scrollWidth > clientWidth for each, and Tab reaches each region).
- Quotes checked against source text; removed an unverified CDC quote, an unsourced "memory for years" claim, and an unsourced LINE-1 characterization during the check pass.

## Gaps
- No human whole-genome study read for C7; the no-integration answer rests on mechanism, the field's design rationale, and the absence of any demonstrated in-person integration in the sources read (stated in report).
- CDC page read only through fetch summary.
- Efficacy against later variants/waning not sourced beyond stating the 2020 limit.
- Report depends on network for Google Fonts; images are local relative assets.
