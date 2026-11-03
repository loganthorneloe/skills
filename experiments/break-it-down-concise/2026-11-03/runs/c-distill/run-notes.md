# Run notes

Elapsed: about 10 minutes of wall-clock time (11:10 to 11:20 CST, 2026-11-03), starting at step 3 from the frozen research packet.

## Files

- `report.html` is the delivered, distilled version (about 2,320 words in the main column, including source entries).
- `draft.html` is the full checked draft saved before distilling (about 4,240 words). The report is about 55% of the draft's reading length.
- `assets/` holds copies of exhibits E1, E2, E3, E5, E6, E8, E9 from the packet. The report uses E1, E6, E8, E9; the draft also uses E2, E3, E5.

## Decisions

- Structure follows the packet's prerequisite order: association, potential outcomes, average effect vs. gap, selection bias, other non-causal routes, adjustment limits, randomization, chance, trial evidence, practical issues, quasi-experiments, implications.
- One interaction, a simulator of self-selection versus coin-flip assignment. It resolves a gap the exhibits leave: readers can see the selection-bias term (unobservable in real data) and how chance imbalance shrinks with sample size. Model is invented and labeled as such; seeded RNG so the no-JavaScript static text matches the default output exactly (gap 11.9 = 2.0 effect + 9.9 bias).
- Six-student worked example (packet E16) kept as a labeled constructed table.
- Rights: IES tables are public domain. Mixtape, Mindspark and LaLonde exhibits have unstated reuse terms and are embedded with attribution and a caption note. Hernán & Robins Figure 1.1 is "all rights reserved"; embedded with attribution as commentary and labeled as such. A stricter policy would replace it with a link.
- Distillation cuts: Mixtape Tables 4.2/4.3 images (sign reversal kept in one sentence), IES baseline-balance table E5 (balance kept in prose and via the Mindspark baseline bars), separate sections on other routes and chance merged into neighbors, World Bank HISP numbers reduced to one sentence, practical issues compressed to one paragraph, source entries to one or two sentences.

## Verification

- Factual sentences checked against `audit-records.md` and `evidence-records.md`. Every claim C1–C11 maps to a pass or conditional record. C5 reverse causation is stated as settled reasoning (packet notes no education source). Mindspark published estimates (0.37/0.23 SD) used in text; the figure is from the working paper and its raw-mean gaps are described without contradicting them. In the draft, the raw-mean gaps were stated explicitly (0.36 math, 0.31 Hindi from bar labels).
- Fixes from checking: draft quasi-experiment sentence changed from "methods that mimic randomization" to "the other designs"; report sentence on the simulator corrected after testing showed the self-selected gap varies at n=20 (now says more students pin the wrong number down more precisely); "started out alike" softened to "largely alike" because two IES baseline rows differ at p = 0.03.
- Rendering with Python Playwright (Chromium) at 1280 and 390 px, both files. `document.fonts.check('600 1em Sora')` and `('400 1em Inter')` returned true after `document.fonts.ready` (fonts loaded from Google Fonts over the network). No horizontal page scroll at either width; all images loaded; none displayed above natural size; LaLonde table sits in a keyboard-focusable scroll region on mobile (640 px wide inside 350 px). No console errors.
- Defect found and fixed: the simulator section was shifted 500 px off-screen left because `.sim{margin:32px 0}` overrode the `.wide` centering margin; changed to top/bottom margins only, confirmed position 140–1140 px at 1280 and 20–370 px at 390. Mobile tables got a 520 px minimum width inside their scroll regions after the 390 px screenshot showed cramped columns.
- Controls operated: default; redraw (history accumulates); true effect at 0, −5 (min) and +10 (max); motivation strength 0% and 100%; coin-flip mode (strength slider disables, bias tile relabels to "Chance imbalance"); sample sizes 20, 200, 2,000; reset restores default output exactly; keyboard ArrowRight on the effect slider and Enter on the redraw button work; Tab order moves effect slider to sample-size select. Results region is `aria-live="polite"`. No-JavaScript render shows the correct default numbers and sentence.

## Gaps

- Fonts depend on network access to Google Fonts; offline the page falls back to system sans-serif.
- Focus-ring appearance was set in CSS (2px red outline) but not visually inspected in a screenshot.
- Evidence limits carried from the packet: no randomized trial of a consumer self-study smartphone app; real-world adjustment failure evidence is from job training; HISP data are fictional; Escueta counts from the 2017 working paper.
- The shared scratchpad was also used by other concurrent processes, which overwrote one of my check scripts mid-run; one check run therefore executed someone else's script against a different file. I moved my scripts to a private subfolder and re-ran every check; the results above come from those re-runs. I did not open or use the other runs' content.
