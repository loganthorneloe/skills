# Run notes

Approximate elapsed time: 9.0 minutes since initial graph creation (plus initial instruction read).

## Output
- report.html: complete offline HTML, embedded Sora 600 and Inter 400/500, inline CSS/JS, embedded original published figure.
- source-figure2.png: optional full-size companion linked by the report; image is also embedded so the report itself remains readable alone.
- dag.json: initial graph in revisions[0], two research rounds, final nine-node/twelve-edge graph and validation results.
- dag.svg, dag.html, dag-render.png: rendered prerequisite view and dependency justifications.
- verification.json; desktop.png, mobile.png, interaction.png, figure-render.png: browser checks and screenshots.
- build_report.py, finalize_graph.py, verify.cjs: reproducible local generation/check scripts.

## Research actually read
1. Hernán and Robins, *Causal Inference: What If*, January 2, 2025 PDF: https://miguelhernan.org/s/hernanrobins_WhatIf_2jan25.pdf . Read relevant passages in §§1.1–1.5; all §2.1 pp.13–16; §§3.1–3.2 pp.27–29; §10.1 pp.132–134; Fine Point 10.2 p.136. Local PDF and extraction retained. These support counterfactual outcomes, comparison of averages, assignment, common causes, observational assumptions, and uncertainty.
2. Didelez and Evans, Oxford APTS course homepage and Introduction §§1.1–1.3: https://www.stats.ox.ac.uk/~evans/APTS/ and https://www.stats.ox.ac.uk/~evans/APTS/intro.html . Read full introductory chapter and target-trial table. Verified author names and date at course homepage.
3. Roschelle et al. 2016, AERA Open: https://doi.org/10.1177/2332858416673968 . Read Research Design, Intervention, Recruitment/Attrition, Procedure, Measures, Data Analysis, Results, and relevant Discussion/limitations. Actual study analyzed 2,850 students in 43 schools; original search guess about PNAS/2,769 was discarded. Read original Figure 2 and Table 4 in published PDF page 9, obtained from https://files.eric.ed.gov/fulltext/EJ1194398.pdf . The study evaluates an app-plus-teacher-training package.
4. 2017 corrigendum: https://doi.org/10.1177/2332858417707489 . Read full correction and corrected Table 4. Original effect-size column erroneously showed 50.10; corrected values are 0.29 and 0.12. Main article text also says 13.35 for the low subgroup, while table/means and correction give 14.35; report uses corrected table. Higher group's displayed means subtract to 5.85 but reported difference is 5.84; report flags rounding rather than silently changing source result.
5. WWC study review: https://ies.ed.gov/ncee/wwc/Study/86375 . Read August 2026 review, Findings, Setting and Sample; also checked older 2019 Findings. Current review uses 2,850 students and adjusted means 690.79/681.95; older review uses 2,728 and excludes joiners. Report uses current review and does not combine those samples. WWC '0 Days' field was not used as a study duration; primary article establishes end-of-year measurement.
6. IES funding/project record: https://ies.ed.gov/use-work/awards/efficacy-study-online-mathematics-homework-support-evaluation-assistments-formative-assessment-and . Read Purpose, Project Activities, Structured Abstract, Design, Measures and Outcomes. Supports laptop access, teacher preparation, intervention and trial setting.
7. Credential checks: Harvard CAUSALab history https://hsph.harvard.edu/research/causalab/our-history/ and James Robins faculty/profile information https://hsph.harvard.edu/profile/james-m-robins/ . Publisher author biography also surfaced in search. Report uses conservative research-method expertise claims.

## Evidence and exhibit decisions
- Original Figure 2 retained unchanged, including truncated y-axis (487), legend, labels and grayscale. It teaches why an average may conceal different effects by starting preparation. Extracted the original image object with pypdf from PDF page 9; visually inspected source page and mobile-rendered figure. Full-size companion supports close reading. CC BY 3.0 attribution included.
- WWC adjusted overall means shown as a small attributed table. Teaches average effect magnitude and why scaled points differ from percentages. Clearly separated from unadjusted Figure 2 values.
- Corrected Table 4 subgroup values discussed next to Figure 2; unnecessary standardized-effect-size jargon omitted.
- Article Figure 1 (teacher report UI) examined through description but omitted: useful for app operation, not needed to explain identification of a causal effect. Figure 2 and overall result table answer the central causal question more directly.
- Textbook medical outcome tables and Oxford conceptual Figure 1.1 considered but omitted: report already explains same-person alternatives concretely and uses an app-specific worked calculation; introducing a second medical example or abstract population figure would add translation burden.
- Original interactive selection-composition calculation explicitly invented: fixed zero effect, 200 students, two preparation types with scores 90/60. Reader changes which types choose the app; observed difference can reverse while effect remains zero. This closes the gap between saying 'confounding' and seeing how an average changes.
- No quotations or claims that the unspecified app works. No statistical confidence bounds attributed to the real trial; +4 and interval examples clearly hypothetical.

## Graph research history
Initial graph saved before prerequisite research. Round 1 supplied causal definitions and trial specification; round 2 added actual education evidence and split bundled implementation concerns into assignment/use, missingness/interference, and uncertainty. Added nonrandom alternative because the question asks how we could find out, not only how an ideal trial works. Final IDs unique, endpoints valid, all branches acyclic, every node reaches target. Each dependency checked against report prose. This is an explanation dependency graph, not a causal DAG of app variables.

## Access and verification
- Web tool could not fetch the 11 MB textbook PDF; curl succeeded and local PDF extraction was used.
- SAGE figure CDN returned 403; original figure successfully recovered from ERIC-hosted published PDF.
- A PMC methods page returned a browser challenge; not used as evidence. An Oxford guessed randomization URL failed; not used. ERIC metadata web request timed out, but directly downloaded article PDF succeeded.
- Shell subprocess network calls failed in one attempt; direct curl tool calls successfully retrieved font assets and OFL notices. All three font files and both notices preserved; notices also embedded in HTML.
- Default Playwright bundled browser was absent. Installed Chrome initially failed under sandbox. Approved escalated execution then ran a separate headless Chrome with isolated new contexts; no existing browser sessions altered.
- Desktop 1440 px and narrow 390 px: document width equals viewport, no horizontal overflow. Original figure loaded with 712-pixel intrinsic width. Sora 600 and Inter 400/500 all reported loaded by the FontFaceSet, beyond computed-family inspection.
- Controls: default 80 -> 84 vs 66, +18; midpoint 50 -> 75 vs 75, 0; boundary 0 -> 60 vs 90, -30; boundary 100 -> 90 vs 60, +30. Keyboard ArrowLeft moved 100 to 99; reset restored 80. No page errors. Status is aria-live; focus-visible CSS provided. No motion.
- JavaScript-disabled context preserved 40 explanatory paragraphs, initial table and +18 result with no-script disclosure.
- Visually inspected desktop and narrow opening layout, narrow interaction, source-page extraction, narrow rendered source figure, and rendered graph. Full-page screenshots preserved for both widths. Did not run a screen reader or exhaustive external-link checker.
- Latest report regenerated after adding Chapter 10 citation; full automated browser checks repeated successfully. No unresolved material rendering or source-access gap remains for included exhibits.

- Final graph screenshot initially showed a browser full-page capture repetition after viewport resize. The HTML had one heading and one graph. Recaptured after two animation frames as a viewport image; graph arrow routing improved to avoid crossing behind a node. Final graph screenshot visually inspected.
