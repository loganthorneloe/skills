# Run notes

Approximate elapsed time: about 50 minutes (started 13:58 local).

## Decisions
- Claims C1–C9 defined up front (see records/source-audit.md). Ranked: C1–C3 (mechanism) and C5–C6 (timing and why) given full treatment; C4 (real rate, expectations) one paragraph; C7–C8 (variability, size) one section; C9 (limits) closing.
- One worked example carried through: a rise from 4% to 5%.
- No interactive or generated visual: the source exhibits (model simulation, empirical IRFs, US price response, cross-country table) already cover the timing gap. A synthesis "Days / Months / Quarters / A year or more" tile group was used for the lag reasons.
- Distillation: draft.html saved after checks; report.html cut prose (excluding figures and the required source list) from ~2,190 to ~1,200 words (~55%), whole page text from ~3,150 to ~2,035 words (~65%; the six required source entries are a fixed floor). All five figures and the table kept; captions shortened to 1–3 sentences.

## Sources read
- Bank of England QB 1999 Q2, "The transmission mechanism of monetary policy" — full PDF.
- Burr & Willems, BoE QB 2024 — full text extracted; some boxes skimmed.
- Federal Reserve explainer page — partial, via fetch-tool extraction.
- Romer & Romer 2004 AER (author copy) — partial: intro, price section, Figures 4–5.
- Havranek & Rusnak 2013 IJCB — partial: sections 1–3, Tables 2–3, conclusions.
- Coibion 2012 (NBER WP 17034 version) — partial: abstract and intro.
- Rights pages: BoE legal page (personal/internal non-commercial use permitted; non-commercial reuse typically granted); IJCB article page (copyright line only).
- One targeted errata/critique search each for Romer & Romer (found Coibion critique) and Havranek & Rusnak (none found).

## Exhibit reuse decisions
- E1 BoE 2024 Figure 1 (assets/boe2024-fig1-channels.jpeg) — embedded. BoE terms permit non-commercial use with attribution; caption carries © and attribution.
- E2 BoE 1999 Charts 1–2 (assets/boe1999-chart1-gdp.png, boe1999-chart2-inflation.png) — embedded, same BoE terms.
- E3 BoE 2024 Chart 4 (assets/boe2024-chart4-irfs.png) — embedded, same BoE terms. Rendered from the page because the embedded JPEG alone clips the right-hand axis labels.
- E4 Romer & Romer Figure 4 (assets/romer2004-fig4-price-level.png) — embedded, rights unstated (author copy has no terms; AEA holds journal copyright); caption says so. Rendered from the page because the native embedded image is stored inverted; the blue frame is part of the published PDF and slightly overlaps the x-axis title and "48" tick in the original.
- E5 Havranek & Rusnak Table 3 — rebuilt as HTML with exact transcribed values, rights unstated (stated in caption); original crop saved at assets/havranek2013-table3.png and linked.
- E6–E8 metrics/short quotes (price/wage stickiness, £50 per £100, fixed-rate share) — quoted or paraphrased with attribution in prose.
- No exhibit was link-only.

## Verification
- Fonts: after document.fonts.ready, document.fonts.check('600 1em Sora') and ('400 1em Inter') both true at 1280 and 390 (loaded from Google Fonts; network dependency).
- Rendering at 1280×900 and 390×844: all 5 images load (naturalWidth > 0), no console errors or failed requests, no horizontal page overflow (scrollWidth = clientWidth). No image displayed above natural size. Wide channel diagram and Chart 4 sit in keyboard-focusable scroll regions on narrow screens; tab reaches both with a visible outline; ArrowRight scrolled the region (scrollLeft 0 → 200). Screenshots in scratch/.
- Every factual sentence checked against the records; edits made for overstatements (Friedman attribution routed through Havranek & Rusnak; "too late" reasoning tied to BoE footnote 21; energy-shock limit restated as BoE's world-markets and second-round-effects points; "post-communist" replaced).
- No controls exist, so control-state checks do not apply.

## Gaps
- Timing of the peak price effect conflicts across sources (BoE 2024 ≈ 1 year for the price level; BoE 1999 ≈ 2 years for inflation; US and meta-analysis longer). Presented as a range.
- Effect size only conditionally supported; Coibion read in working-paper form only.
- Fed page read via a fetch-tool summary only.
- BoE public reuse would formally need the Bank's permission; reproduced here on its non-commercial terms.
