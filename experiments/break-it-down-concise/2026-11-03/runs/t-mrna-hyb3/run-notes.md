# Run notes — mRNA vaccines breakdown

## Decisions
- Reader: high-school biology only. One worked example carried through: the Pfizer–BioNTech vaccine (BNT162b2) and its spike recipe.
- Claims C1–C9 (records/claims.md), ranked: DNA question (C8, C9) and immune mechanism (C4) got full treatment; LNP chemistry and nucleoside modification compressed; efficacy/waning kept as evidence the mechanism works and its limits.
- One generated SVG diagram (cell, nucleus, three missing steps) because no source exhibit shows the nucleus/reverse-transcription barrier; labelled as drawn for the report. No interactive: no reader-controlled input would add insight.
- Wide multi-panel figures (Röltgen Fig 7, Polack Fig 3, Feikin Fig 2) and the SVG sit in keyboard-focusable horizontal scroll regions under 640px; Pardi and Nobel figures scale to width.
- Distillation: draft body (after sources) ~2,290 words → report ~1,300 words (~57%). All 5 source figures, both quotations, and the SVG kept. Cut: background paragraph on amino acids, second-dose discussion detail, extra figure commentary, LNP ingredient list, helper-T detail, Merchant's lipid-distribution argument (kept the dose point), roadmap sentence.

## Sources read (records/audit.md)
Pardi 2018 (PMC author manuscript, partial); Nobel 2023 press release (full); Polack 2020 NEJM (PMC, partial); Röltgen 2022 Cell (PMC, partial); Feikin 2022 Lancet (PMC, partial); Aldén 2022 CIMB (PMC, partial; MDPI blocked fetch); Merchant 2022 comment (PMC, partial). CDC education page returned 404 and was dropped. Retraction/correction searches: Aldén (none found, one published critique), Röltgen (none found); Feikin carries a PMC correction notice not examined in detail.

## Exhibits (records/evidence.md, assets/)
E1 Nobel Fig 2 (rights unstated, attributed; 1200px display copy + 2500px full-size link); E2 Pardi Fig 3 (rights unstated, attributed); E3 Röltgen Fig 7 (Elsevier COVID re-use permission); E4 Polack Fig 3 (PMC OA subset, non-commercial); E5 Feikin Fig 2 (CC BY 4.0); E6/E7 quotes. Omitted: NEJM visual abstract, Pardi Fig 1, Röltgen Fig 6.

## Verification
- Fact pass against records: fixed overstatements ("hundredfold" drop → "drops steeply"; germinal centre refinement "likely" → "may"; removed unsourced claim about updated vaccines; "cannot become" → "does not become"; LINE-1 "unusually active" replaced with what the audited sources say).
- Playwright Chromium, 1280px and 390px, report and draft: document.fonts.check('600 1em Sora') and ('400 1em Inter') true after fonts.ready (Google Fonts loaded over network); all 5 images load (naturalWidth > 0), none upscaled; no horizontal page overflow (scrollWidth = clientWidth); no console errors.
- Screenshots inspected (scratch/shot-*.png, svg-*.png, part-*.png, m-*.png): fixed SVG label overlaps (Cytoplasm label on outline, "immune training" touching nucleus), added step legend, wrapped wide figures for mobile.
- Keyboard: all four scroll regions reachable by Tab and scroll with arrow keys at 390px.
- Not done: dark-mode, screen-reader run-through.

## Gaps
- No human genome-sequencing study audited for C8; the DNA answer rests on textbook mechanism plus a review's platform statement (stated in report).
- T-cell evidence only indirect (Polack citing its phase 1).
- Safety/side effects out of scope.
- Network dependency: fonts from Google Fonts; images are local relative files.

## Time
About 11 minutes wall-clock (12:50–13:01 CST by system clock).
