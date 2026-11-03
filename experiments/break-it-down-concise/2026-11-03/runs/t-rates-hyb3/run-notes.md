# Run notes

Elapsed: about 12 minutes (12:50 to 13:02 CST, 2026-11-03).

## Decisions
- Claims C1–C8 (see records/audit.md). Ranked top: C2/C3 (why rates slow inflation) and C4/C5 (why it takes long); C6–C8 stated briefly.
- One worked example carried through: a $30,000 five-year car loan moving from 7% to 8% (~$594 to ~$608/month, computed), then the dealer/factory/wage chain.
- Exhibits embedded: Fed *The Fed Explained* Figures 3.1 and 3.3 (Board site states public domain). Bank of England Charts 1–2 and FRBSF Figure 3 were the best timing exhibits but their stated terms require permission (BoE: permission for re-use; FRBSF: written permission to reprint), so they are linked and described, not embedded.
- One generated visual: an SVG timeline plotting only milestones stated in the BoE simulation and FRBSF estimates (no invented curve shapes), labeled as drawn for the report. It fills the gap left by not embedding the source timing charts.
- No interactive: none resolved a specific gap beyond the timeline.
- Distill: body (answer onward, excluding SVG text) 1,953 words in draft.html to ~1,150 in report.html (~59%). All three visuals kept. Source entries tightened.

## Sources read
- Bank of England 1999, Transmission mechanism (full PDF).
- The Fed Explained 2021 (Ch. 3 pp. 21–27, 39–46). Currentness spot-check on Fed policy tools page (updated Dec 15, 2025).
- FRBSF Economic Letter 2024-10 (full PDF).
- Waller speech July 2023 (opening and lags section).
- KC Fed Doh & Foerster 2022 (web page via fetch summary only; PDF download timed out) — partial, conditional.
- Retraction/critique searches run for FRBSF and KC Fed notes; none found. BoE and Fed copyright terms checked.

## Verification
- Fact pass: removed two unsupported draft claims (size of 2022–23 Fed hikes; US mortgages "fixed for decades") and softened wage-contract wording to Waller's "nominal contracts".
- Playwright (Chromium) at 1280 and 390 px: document.fonts.check('600 1em Sora') and ('400 1em Inter') true at both widths after fonts.ready (fonts from Google Fonts, network required); no horizontal page overflow (scrollWidth = clientWidth); both images load at natural 1226 px, never upscaled; timeline SVG and Figure 3.3 sit in keyboard-focusable horizontal scroll regions on narrow screens. Screenshots inspected in scratch/.
- No controls to operate.

## Gaps
- C6 (magnitudes) and C8 (lags shortening) rest on conditional sources; stated as rough or debated.
- No primary micro study of price-change frequency; "about once a year" is Waller's summary.
- BoE/FRBSF charts not embedded for rights reasons. KC Fed read only via summary.
- Report depends on network for fonts; falls back to system sans-serif offline.
