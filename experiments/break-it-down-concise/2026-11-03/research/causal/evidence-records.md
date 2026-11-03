# Evidence records

Claims are in `claims.md`; source audits in `audit-records.md`. Asset paths are relative to `research/causal/`. Every image listed was opened at full size after extraction.

### E1: Causation vs. association diagram
- claim: C1, C3 (support)
- type: figure
- source: Causal Inference: What If (Hernán & Robins) — https://miguelhernan.org/s/hernanrobins_WhatIf_19aug26.pdf (version 19 Aug 2026)
- locator: Figure 1.1, §1.5 "Causation versus association," PDF page 20 (book page 11)
- asset: `assets/E1-hernan-robins-fig1-1-causation-vs-association.jpeg` (original embedded image extracted from the PDF, 3001×2251 px, no re-rendering)
- inspected: opened at full size; title "Population of interest," Treated/Untreated split diamond, Causation and Association arrows, and all four labels E[Y^{a=1}], E[Y^{a=0}], E[Y|A=1], E[Y|A=0] visible and sharp. The book's caption is only "Figure 1.1"; the explanatory text is in the body (quoted below).
- notice: The top diamond is one population split into the people who happened to be treated (white) and untreated (grey). Causation (left) compares the whole diamond all white against the whole diamond all grey: the same people in two worlds. Association (right) compares the white piece against the grey piece: two different subsets in the real world. For the app question, "users vs. non-users" is the right-hand comparison; "everyone with the app vs. everyone without" is the left. Supporting text (p. 11): association concerns "questions in the actual world, such as 'what is the risk in the treated?'"; causation concerns "what if questions in counterfactual worlds."
- limits: Schematic only; no data. Notation uses Y for the outcome and A for treatment; writers should relabel in prose (A = uses the app, Y = exam score) rather than alter the image.
- rights: "All rights reserved"; reuse beyond U.S. copyright exceptions requires permission from the authors. Embed only with attribution if the caller judges it fair use, otherwise link to the PDF.

### E2: Every patient's two potential outcomes (the "perfect doctor" table)
- claim: C2, C3 (support)
- type: table
- source: Causal Inference: The Mixtape (Cunningham), Ch. 4 — https://mixtape-1ed.netlify.app/04-potential_outcomes (1st online edition)
- locator: Table 4.2, §4.1.3 "Simple difference in means decomposition"
- asset: `assets/E2-mixtape-table4-2-potential-outcomes.png` (rendered with headless Chrome from the page's own table HTML, site CSS, and MathJax; cropped). Transcribed values (patient: Y¹ surgery, Y⁰ chemo, δ): 1: 7, 1, 6 · 2: 5, 6, −1 · 3: 5, 1, 4 · 4: 7, 8, −1 · 5: 4, 2, 2 · 6: 10, 1, 9 · 7: 1, 10, −9 · 8: 5, 6, −1 · 9: 3, 7, −4 · 10: 9, 8, 1. Means E[Y¹] = 5.6, E[Y⁰] = 5, ATE = 0.6 years.
- inspected: opened at full size; caption, header, all 10 rows and δ column visible; values checked against the page text.
- notice: This is the table no real study can have: both outcomes for every person. Averaging the δ column gives the true average effect of surgery, +0.6 years, even though some patients (7, 9) do far better without it. Translate for the reader as "score with the app" and "score without the app" for each student.
- limits: Invented data; medical, not education. Units are years of post-treatment life.
- rights: rights unstated (free online textbook, Yale University Press); attribute to Cunningham, The Mixtape (2021), Table 4.2.

### E3: What we would actually observe when patients sort themselves
- claim: C1, C4 (support)
- type: table+metric
- source: Causal Inference: The Mixtape, Ch. 4 — https://mixtape-1ed.netlify.app/04-potential_outcomes
- locator: Table 4.3 and following text, §4.1.3
- asset: `assets/E3-mixtape-table4-3-observed-outcomes.png` (rendered as E2). Transcribed (patient: Y, D): 1: 7, 1 · 2: 6, 0 · 3: 5, 1 · 4: 8, 0 · 5: 4, 1 · 6: 10, 1 · 7: 10, 0 · 8: 6, 0 · 9: 7, 0 · 10: 9, 1. Metrics from the text: surgery-group mean 7, chemo-group mean 7.4, simple difference in outcomes (SDO) = 7 − 7.4 = −0.4 years; ATT = 4.4; ATU = −3.2. Recomputed from Table 4.2 and confirmed: surgery group (1, 3, 5, 6, 10) observed mean 35/5 = 7; chemo group (2, 4, 7, 8, 9) 37/5 = 7.4.
- inspected: opened at full size; two-line caption, header, all 10 rows visible.
- notice: Each patient got whichever treatment was better for them, so the observed table is real outcomes only. Comparing group averages says surgery costs 0.4 years, the opposite sign of the true +0.6. Cunningham: "notice how misleading it is." The comparison is honest arithmetic on real outcomes and still answers the wrong question, because the groups differ in what they would have experienced anyway.
- limits: The sorting here is extreme (a doctor who knows every outcome). Real self-selection is partial and its size unknown.
- rights: rights unstated; attribute as E2.

### E4: The decomposition: observed gap = true effect + selection bias + unequal-gains bias
- claim: C4 (support), C7 (support)
- type: metric+quote
- source: Causal Inference: The Mixtape, Ch. 4 — https://mixtape-1ed.netlify.app/04-potential_outcomes
- locator: §4.1.3 labeled decomposition equation and the paragraphs after it; §4.1.4 independence assumption
- asset: metric, in years of post-treatment life for the 10-patient example: −0.4 (simple difference) = 0.6 (average treatment effect) + (−4.8) (selection bias: E[Y⁰|D=1] − E[Y⁰|D=0], i.e., 2.6 − 7.4) + 3.8 (heterogeneous-effect bias: (1−π)(ATT − ATU) = 0.5 × (4.4 − (−3.2))). Recomputed and confirmed. Quotes: "One could argue that the entire enterprise of causal inference is about developing a reasonable strategy for negating the role that selection bias is playing in estimated causal effects." "All forms of human-based sorting—probably as a rule to be honest—violate independence." Monte Carlo: with treatment randomly assigned, the average SDO across simulated draws was 0.59088 against a true ATE of 0.6.
- inspected: not applicable (text and arithmetic; checked against page text)
- notice: Selection bias has a precise meaning the reader can grasp with averages: how differently the two groups would have scored without the treatment. For the app, that is "what app users would have scored with no app" minus "what non-users scored." Randomization makes that difference zero on average, which is why the Monte Carlo average lands near 0.6.
- limits: The third term disappears if every student gains the same amount, or if the target is the effect on users (ATT); the selection-bias term remains. Text says the simulation ran 10,000 times while the shown Python code runs 1,000; the 0.59088 figure is the author's own run.
- rights: rights unstated; short quotes with attribution.

### E5: Randomization balanced the groups before the software was used (IES)
- claim: C7, C8 (support)
- type: table
- source: Effectiveness of Reading and Mathematics Software Products: Findings from the First Student Cohort (Dynarski et al., 2007) — https://ies.ed.gov/sites/default/files/migrated/nces_pubs/ncee/pdf/20074005.pdf (NCEE 2007-4005)
- locator: Table II.5, Chapter II, report page 28 (PDF page 54)
- asset: `assets/E5-ies-2007-table-II5-baseline-balance.png` (rendered from the PDF at 300 dpi, includes notes). Key values (treatment vs. control, p-value): teaching experience 11.7 vs 11.6 yrs (0.97); master's degree 38% vs 55% (0.03); fall SAT-9 reading 50.1 vs 50.9 NCE (0.62); fall TOWRE 109.1 vs 109.8 (0.43); student age 6.63 vs 6.67 (0.03); teachers 89 vs 69; students 1,516 vs 1,103.
- inspected: opened at full size; title, all teacher and student rows, sample sizes, Sources, Note, and footnote a visible.
- notice: Before the software was used, randomly assigned classrooms looked alike, including on the fall reading test, the best predictor of the spring score. Two rows differ at p = 0.03 (master's degrees, student age); the report says none is significant after correcting for multiple comparisons and adjusts for all of them anyway. This shows that randomization balances on average, not exactly, and that researchers check.
- limits: First-grade substudy only. Teachers, not students, were randomized; students were not randomly assigned to teachers.
- rights: public domain ("This report is in the public domain. Authorization to reproduce it in whole or in part is granted.").

### E6: The randomized comparison found essentially no difference (IES)
- claim: C8, C9 (support)
- type: table
- source: as E5
- locator: Table II.6, report page 29 (PDF page 55); effect-size definition footnote 15
- asset: `assets/E6-ies-2007-table-II6-score-differences.png` (300 dpi, includes notes). Key values: SAT-9 overall 50.20 vs 49.47 NCE, difference 0.73, effect size 0.03, p = 0.34; TOWRE overall 112.34 vs 111.83, difference 0.51, effect size 0.04, p = 0.57; subtests effect sizes −0.01 to 0.06, all p ≥ 0.16. Effect size = score difference ÷ standard deviation of the control group's spring scores. Executive summary: these equal "increases in student percentile ranks of about 0 to 2 points. None is statistically significant."
- inspected: opened at full size (re-cropped once after the first crop touched the title's left edge); all rows, columns, and both notes visible.
- notice: With random assignment the comparison is fair, and the fair comparison shows a gap under one test point that could easily be chance. Effect size 0.03 is tiny on any rule of thumb (Escueta et al.: under 0.10 SD is small). Same pattern held for grade 4 reading, grade 6 math, and algebra (exec. summary Figures 3–5).
- limits: Treatment averages are model-adjusted (control mean plus estimated effect), not raw. Applies to five first-grade products pooled, first year, about 30 hours of use a year (about 11% of reading instruction time).
- rights: public domain.

### E7: IES statements on what randomization controls and what correlations cannot show
- claim: C5, C7, C10 (support)
- type: quote
- source: as E5, executive summary https://ies.ed.gov/sites/default/files/migrated/nces_pubs/ncee/pdf/20074006.pdf (NCEE 2007-4006)
- locator: pp. vi, xi, xii, iv
- asset: exact quotes: (p. vi) "Aspects of teaching that are difficult or impossible to observe, such as a teacher's ability to motivate students to learn, are “controlled” by the experimental design because teachers were randomly assigned." (p. xi) "Relationships between school and classroom characteristics and score differences cannot be interpreted as causal, because districts and schools volunteered to participate." (p. xii, grade 4) "effects were larger when teachers reported higher levels of product use. As noted above, these relationships do not have a causal interpretation." (p. iv) "the study's findings do not support conclusions about technology's effectiveness beyond the study's context."
- inspected: not applicable; quotes copied from extracted PDF text and checked against it.
- notice: The second and third quotes are the exact trap in the reader's question, stated by the evaluators themselves: even inside a randomized study, "classrooms that used it more did better" is a non-random comparison and is not proof. The first quote is the plain-language reason randomization works on traits no one can measure.
- limits: The usage correlation is reported only for grade 4 reading.
- rights: public domain.

### E8: Lottery winners vs. losers: balanced at baseline, apart at endline (Mindspark)
- claim: C7, C8, C9 (support)
- type: figure+metric
- source: Disrupting Education? Experimental Evidence on Technology-Aided Instruction in India (Muralidharan, Singh & Ganimian) — https://www.nber.org/system/files/working_papers/w22923/w22923.pdf (NBER WP 22923, revised July 2017); published AER 109(4) 2019
- locator: Figure 2, PDF page 33 (WP page 31); abstract; §2.3
- asset: `assets/E8-mindspark-fig2-lottery-winners-vs-losers.jpeg` (original embedded image, 595×433 px, its natural resolution; do not upscale) and `assets/E8-mindspark-fig2-with-caption-note.png` (200 dpi render with title and note). Values read from bar labels (SD units relative to baseline): Math baseline control 0.01, treatment −0.01; endline control 0.34, treatment 0.70. Hindi baseline −0.05 vs 0.05; endline 0.10 vs 0.41. Whiskers are 95% confidence intervals. Published ITT effects: +0.37 SD math, +0.23 SD Hindi over 4.5 months (WP: 0.36, 0.22). Sample: 619 students, 314 offered vouchers, 305 control; mean attendance among winners 58%; endline follow-up 84% treatment, 88% control.
- inspected: opened both at full size; both panels, axis labels, bar value labels, error bars, and legend visible; the original is low resolution, so small bar labels are legible but soft; the captioned render is clearer for reading the note.
- notice: The left pair in each panel is the "before" check: the lottery produced groups that started level. The right pair shows the gap that opened during the program. Both groups improved (the control group's math score also rose to 0.34), so a before-and-after look at winners alone would overstate the effect; the lottery losers supply the "what would have happened anyway."
- limits: Raw group means; the headline effects come from regressions in Table 2 (not extracted). Program bundled software, tutor time, and extra hours. Values in the WP figure may differ slightly from the published version.
- rights: rights unstated for figures; NBER notice permits quoting short text with credit ("© 2016 by Karthik Muralidharan, Abhijeet Singh, and Alejandro J. Ganimian"). Attribute; caller decides on embedding.

### E9: Adjusted observational estimates vs. the experimental answer (LaLonde 1986)
- claim: C6 (support), C11 (qualify: difference-in-differences also unstable)
- type: table
- source: Evaluating the Econometric Evaluations of Training Programs with Experimental Data (LaLonde) — AER 76(4) 1986, read via https://gwern.net/doc/economics/1986-lalonde.pdf
- locator: Table 5, p. 610
- asset: `assets/E9-lalonde-1986-table5-experimental-vs-nonexperimental.png` (rendered at 300 dpi from the scanned page; includes footnotes a–d). Key values (1982 dollars; standard errors in parentheses), effect on 1978 earnings: experimental controls, unadjusted post-training difference $886 (476), adjusted $798 (472). PSID-1 comparison group: unadjusted −$15,578 (913), adjusted −$8,067 (990), difference-in-differences −$749 (692). CPS-SSA-1: unadjusted −$8,870 (562), adjusted −$4,416 (557), difference-in-differences $195 (441). Footnote a: "Based on the experimental data an unbiased estimate of the impact of training presented in col. 4 is $886."
- inspected: opened at full size; first crop clipped row names and the footnotes, re-cropped twice; final image shows the full title, all column headers (1)–(10), all seven comparison-group rows with standard errors, and footnotes a–d.
- notice: Read down column 4 and 5. The top row is the right answer, from random assignment. Every other row swaps in a survey-based comparison group, and most estimates are negative and large: the same program now appears to cost trainees thousands of dollars. Adjusting for age, schooling, race and similar traits (column 5) shrinks the error but does not fix it. Values match the Mixtape's Table 5.11 transcription.
- limits: Job training, men only, 1970s data, 1980s methods. Later reanalyses (Dehejia & Wahba 1999, 2002, via Mixtape §5.3.4) got closer with propensity scores on a subsample, so the lesson is fragility, not inevitable failure. Scanned image is slightly soft but legible.
- rights: AEA copyright (scan marked "Copyright © 2001 All Rights Reserved"); rights for reuse unstated; attribute and let caller decide, or rebuild the three key rows as an HTML table with attribution (values above match the source exactly).

### E10: Enrolled vs. non-enrolled comparison, raw and "controlled" (World Bank, fictional case)
- claim: C4, C6 (support, illustrative)
- type: table
- source: Impact Evaluation in Practice, 2nd ed. (Gertler et al., 2016) — https://openknowledge.worldbank.org/handle/10986/25030
- locator: Table 3.3 (book p. 60) and Table 3.4 (p. 61)
- asset: `assets/E10a-worldbank-iep-table3-3-enrolled-vs-nonenrolled.png`, `assets/E10b-worldbank-iep-table3-4-enrolled-vs-nonenrolled-regression.png` (300 dpi). Values: household health expenditures enrolled $7.84 vs non-enrolled $22.30, difference −$14.46 (t = −49.08); regression −14.46 (0.33); multivariate regression −9.98 (0.29).
- inspected: opened both at full size; titles, headers, values, and notes visible.
- notice: Self-selected comparison gives a huge, "highly significant" effect; adding control variables changes it by a third. Statistical significance (t = −49) says the gap is not chance; it says nothing about whether the gap is caused by the program. Pair with E11 to see the randomized answer.
- limits: HISP is a fictional case with constructed data; present as a teaching illustration only. Health spending, not exam scores.
- rights: CC BY 3.0 IGO; attribution: Gertler, Martinez, Premand, Rawlings, Vermeersch, Impact Evaluation in Practice, 2nd ed., World Bank, 2016.

### E11: Randomized assignment: baseline balance and impact (World Bank, fictional case)
- claim: C7, C8 (support, illustrative)
- type: table
- source: as E10
- locator: Tables 4.1 and 4.2 (book p. 83)
- asset: `assets/E11-worldbank-iep-tables4-1-4-2-randomized-balance-and-impact.png` (300 dpi). Values: baseline health expenditures 14.49 vs 14.57 (difference −0.08, t = −0.73); 11 household characteristics, two differing at the "*" level (head's education 2.97 vs 2.81; distance to hospital 109.20 vs 106.29 km); follow-up expenditures 7.84 vs 17.98, difference −$10.14 (t = −49.15). Table 4.3 (not imaged): regression −10.14 (0.39), multivariate −10.01 (0.34).
- inspected: opened at full size; both table titles, all rows, notes visible.
- notice: With random assignment, the groups start level on spending and on nearly every trait, and adding control variables barely moves the estimate (−10.14 to −10.01), unlike the self-selected comparison (−14.46 to −9.98). Stability under adjustment is a symptom of a fair comparison.
- limits: Fictional data. Table 4.1 note defines "**" but entries use "*" (undefined in the note).
- rights: CC BY 3.0 IGO.

### E12: Same fictional program, every method (World Bank)
- claim: C5, C6, C11 (support, illustrative)
- type: metric (transcribed synthesis across tables in one source)
- source: as E10
- locator: Tables 3.1, 3.3, 3.4, 4.2–4.3, 5.2, 6.1, 7.2–7.3, 8.2; Table 11.2 (pp. 194–195) for assumptions
- asset: estimated impact of HISP on yearly per-capita out-of-pocket health spending (US$; negative = savings): before-and-after (enrolled households) −6.65; enrolled vs. non-enrolled −14.46, with controls −9.98; randomized assignment −10.14, with controls −10.01; randomized promotion / instrumental variables −9.50, with controls −9.74; regression discontinuity −9.03; difference-in-differences −8.16; matching −9.95 (full covariates) or −11.35 (limited covariates). The book's policy threshold for scale-up is a $10 reduction. Quote (p. 55): "the baseline outcome is almost never a good estimate of the counterfactual." Table 11.2 key assumptions, e.g., randomized assignment: "Randomization effectively produces two groups that are statistically identical with respect to observed and unobserved characteristics"; regression discontinuity: units immediately above and below the cutoff "are statistically identical."
- inspected: not applicable (values transcribed from extracted text and checked against the rendered Tables 3.3, 3.4, 4.1, 4.2 above).
- notice: Each method answers "compared with what?" differently, and in this case the decision (scale up if savings ≥ $10) flips depending on the method. Methods that mimic randomization land near the randomized −10.14; naive ones (before-after, self-selected) miss in opposite directions.
- limits: Fictional dataset built to teach; agreement between methods here is by construction and says nothing about how they perform in real data (for real-data evidence, use E9). If shown as a table in the report, label it as a synthesis of the book's own numbers.
- rights: CC BY 3.0 IGO.

### E13: Why adjustment can't be checked from the data (Hernán & Robins)
- claim: C6 (support)
- type: quote
- source: Causal Inference: What If — version 19 Aug 2026
- locator: §3.2 Exchangeability, PDF pages 39–40 (book pp. 30–31)
- asset: exact quotes: "In the absence of randomization, there is no guarantee that conditional exchangeability holds." "Importantly, collecting data on smoking would not prevent the possibility that other imbalanced outcome predictors, unknown to the investigators, remain unmeasured." "Worse yet, even if conditional exchangeability Y^a⊥⊥A|L held, the investigators cannot empirically verify that is actually the case." Also (Ch. 3 intro) "The best explanation for an association between treatment and outcome in an observational study is not necessarily a causal effect of the treatment on the outcome."
- inspected: not applicable; checked against extracted text.
- notice: The logic behind C6 in the authors' words: measuring more traits narrows the gap only for traits you thought to measure. For the app: you can control for last year's grades and family income, but not for motivation you never recorded.
- limits: Heart-transplant/smoking example; translate the formula into words.
- rights: all rights reserved; short quotation with attribution.

### E14: Association with zero causal effect, in numbers (Hernán & Robins)
- claim: C1, C3 (support)
- type: metric+quote
- source: Causal Inference: What If — version 19 Aug 2026
- locator: §1.5, PDF pages 19–21 (book pp. 10–12), Tables 1.1–1.2; margin note on aspirin p. 12; Ch. 2 §2.1 p. 15
- asset: metrics in the hypothetical 20-person population: risk of death among the 13 treated 7/13 (≈ 54%) vs. among the 7 untreated 3/7 (≈ 43%): an association; risk if everyone treated 10/20 = 50% vs. if no one treated 10/20 = 50%: no causal effect. Quote: "This discrepancy between causation and association would not be surprising if those who received heart transplants were, on average, sicker than those who did not receive a transplant." Margin example: causal risk ratio 0.5 for aspirin but associational risk ratio 1.5 "because individuals at high risk of cardiovascular death are preferentially prescribed aspirin." Ch. 2: "In ideal randomized experiments, association is causation."
- inspected: not applicable; fractions checked against the extracted Table 1.2 discussion.
- notice: Percentages the reader already understands carry the whole point: 54% vs 43% looks like the treatment matters, but in the full "what-if" table it does nothing. The aspirin example shows the sign can flip (a drug that halves risk looks like it raises it).
- limits: Hypothetical data; medical setting.
- rights: all rights reserved; short quotation with attribution.

### E15: The ed-tech evidence base is mostly observational; experiments are mixed but often positive
- claim: C9 (context), C7 (context)
- type: quote+metric
- source: Education Technology: An Evidence-Based Review (Escueta, Quan, Nickow & Oreopoulos) — https://www.nber.org/system/files/working_papers/w23744/w23744.pdf (NBER WP 23744, Aug 2017)
- locator: §2 pp. 6–8; §4.1 pp. 21–22 and footnotes 58–59
- asset: quote (p. 7): "the policy literature on ed-tech is flooded with observational research and could benefit from a synthesis of evidence from the designs most likely to produce unbiased estimates of causal effects." Metric (p. 22): 29 experimental (all RCT) studies of computer-assisted learning in developed countries; 8 report no effect, 1 negative, 20 positive, of which 15 focus on math. Rule of thumb (pp. 7–8): under 0.10 SD small; 0.10–0.25 encouraging; 0.25–0.40 large; above 0.40 very large. Footnote 59 flags the Dynarski et al. (2007) and Campuzano et al. (2009) federal studies as "notable exceptions" with "a general pattern of no effects."
- inspected: not applicable; checked against extracted text.
- notice: Places the two trials (E6, E8) in context: rigorous tests of learning software often find gains, particularly in math, but not always, so "it works" must be shown product by product. The rule of thumb lets the reader judge IES's 0.03 (small) and Mindspark's 0.37 (large).
- limits: Working-paper counts; published JEL 2020 version not read. Vote count, not a pooled average. Developed-country focus (Mindspark is from India). Positive count (20) is derived: 29 − 8 − 1.
- rights: NBER notice permits short quotes with credit; numbers are facts.

### E16: Generated worked example for the app question (not a source exhibit)
- claim: C2, C4, C7 (context)
- type: generated
- source: constructed by the researcher, modeled on the structure of Mixtape Table 4.2 (E2–E4); not published data
- locator: not applicable
- asset: six hypothetical students; the app adds exactly 2 points for everyone. Scores without app (Y⁰): A 80, B 78, C 76 (motivated, choose the app); D 64, E 62, F 60 (do not). With app (Y¹) = Y⁰ + 2. Observed: users A 82, B 80, C 78 → average 80; non-users 64, 62, 60 → average 62. Observed gap 18 = true effect 2 + selection bias 16 (users' no-app average 78 minus non-users' 62). Under a fair coin flip, groups' no-app averages are equal in expectation, so the expected gap is 2. Also see `background.md`.
- inspected: arithmetic checked.
- notice: Lets the reader see, with nothing but averages, that a real gap of 18 points can come almost entirely from who chose the app.
- limits: Invented numbers; must be labeled as a constructed illustration in the report; constant effect assumed (so the heterogeneous-effect term is zero).
- rights: not applicable.

## Claims still lacking evidence, and omitted candidates

- C5 (reverse causation for apps): no exhibit; Mixtape's Yule critique ("he may have the causality backwards—perhaps increased poverty causes communities to increase relief") is available as a quote if needed (§4.0), but it is about poverty relief, not learning.
- C10 (spillovers): no empirical exhibit; definitional support only (Mixtape §4.1.5 SUTVA; World Bank condition 2 on p. 52).
- C11: no figure for regression discontinuity or difference-in-differences extracted; World Bank Figure 6.7 (poverty index vs. spending at the cutoff) and Figure 3.3 (before-and-after with counterfactuals B, C, D) are candidates in the same CC BY source (book pp. 136 and 55) if a writer wants a method figure; not extracted to keep exhibits focused.
- Omitted: IES executive-summary Figures 1–5 (bar charts of effect sizes; small vector graphics without value labels, superseded by Table II.6); Mindspark Figure 4 dose-response (shows value-added rising with attendance among winners; easy to misread as causal without the IV explanation); Mindspark Table 1 balance (Figure 2 shows balance more simply); Hernán Table 1.1 full 20-row counterfactual table (E14 metrics carry it); LaLonde PSID-2/3 and CPS-SSA-2/3 rows (in the image, not needed in prose).
