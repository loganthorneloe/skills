# Judge: mrna3 (A vs B)

I read both reports and their records, rendered each at 1280px and 390px with Playwright, and inspected every figure on its own. Screenshots and the render script are in `evaluation/scratch-judge-mrna3/`. Neither report has interactive controls. The only operable elements are full-size image links and keyboard-focusable horizontal-scroll regions (A has 2, B has 4). Neither report logged console errors or caused horizontal page overflow. Neither has a dark-mode stylesheet.

## Scores

Dimensions: 1 prerequisites, 2 order, 3 mechanism, 4 evidence for foundations, 5 accuracy, 6 transfer, 7 source/exhibit quality, 8 readability, 9 presentation, 10 signal density, 11 time to answer, 12 research quality, 13 visual explanation.

| Report | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | Total /65 | Probes /16 | Words counted |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 4 | 54 | 14 | 3,136 |
| B | 4 | 4 | 4 | 5 | 5 | 3 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 57 | 13 | 1,887 |

The word counts cover all visible text, including the source cards and captions.

### Per-dimension notes

1. **Prerequisites (A 5, B 4).** A teaches the nucleus, proteins, the cytoplasm, ribosomes, and innate versus adaptive immunity ("Your immune system has two layers"). B fits the whole of the central dogma into one paragraph and never explains innate versus adaptive immunity. B does define dendritic cells and germinal centres.
2. **Order (A 5, B 4).** A builds each idea before using it and then reuses its one-way-flow idea for the DNA answer. B is sound but brings in "T follicular helper cells" with little setup.
3. **Mechanism (A 5, B 4).** A explains the ionizable-lipid charge and endosomal escape, the TLR alarm and the shutdown of protein making, the cap and poly(A) tail that let ribosomes read the mRNA, how CD4 and CD8 T cells are reached, and three barriers to DNA. B adds the route from dendritic cells to the lymph node, which A does not have, but gives less on delivery.
4. **Evidence for foundations (A 4, B 5).** B backs each step with a primary exhibit: Pardi Fig 3 for immune induction, Röltgen Fig 7 for persistence, and Feikin Fig 2 for waning. A states persistence and waning in prose only.
5. **Accuracy (A 4, B 5).** See the errors section. A has one imprecise denominator. B is careful throughout.
6. **Transfer (A 4, B 3).** A says that changing only the encoded protein lets updated vaccines be made quickly. B never addresses a new virus.
7. **Exhibits (A 4, B 5).** B reads panels and gives provenance and limits for each one, for example the note that Pardi Fig 3 "shows a skin injection; the COVID vaccines go into muscle". A's exhibits are good but fewer, and it chose not to use Röltgen Fig 7.
8. **Readability (A 4, B 4).** A is clear but long. B is tight, but Röltgen Fig 7 and Feikin Fig 2 are dense multi-panel research figures that load a novice reader.
9. **Presentation (A 4, B 4).** Both have clean typography and alt text and work at 390px. In both, the SVG needs a sideways scroll on mobile, and B's diagram hides the nucleus until the reader scrolls. On mobile, B also puts three dense figures in sideways-scroll regions, and the small text in Röltgen panel D is hard to read even at desktop width.
10. **Signal density (A 3, B 5).** A spends words on side detail, such as the ionizable-lipid acidity and the dose-justification argument in Merchant. B makes nearly the same argument in 60% of the words.
11. **Time to answer (A 4, B 5).** Both open with a short answer. B's short answer also gives all three DNA reasons in one sentence.
12. **Research quality (A 4, B 5).** Both records are solid, with verdicts per claim, locators, and rights. B adds a separate claims file and a WHO-led meta-analysis with a risk-of-bias assessment, and it notes the correction to Feikin. A used the Nobel scientific background, a stronger mechanism source than B's press release, and logged a CDC source it dropped.
13. **Visual explanation (A 4, B 4).** A's figures fit a novice better. B's are more evidential but harder to read (lists below).

## Visuals

### A
- **Nobel Fig 3 (U vs ψ mRNA).** Shows that modified mRNA yields far more surface protein. The caption flags it as an illustration.
- **Nobel Fig 4 (nanoparticle to ribosome to spike on the surface, with B cells).** The best single image of the mRNA's path in either report. It shows the mRNA never entering the nucleus.
- **Card grid (B cells, helper T, killer T, memory).** A compact comparison table of the adaptive arms.
- **Polack Fig 3 (cumulative incidence).** The roughly 12-day lag and then the flat vaccine curve show that immune training takes time and then works.
- **Generated SVG (one-way flow, with a crossed-out route from mRNA back to DNA).** The DNA answer at a glance. The "copy" label sits close to the dashed return arrow, which is slightly ambiguous.
- **Missing compared with B.** A waning-over-time chart (Feikin Fig 2), something showing the trip from injection site to lymph node (Pardi Fig 3), and the direct evidence of lymph-node persistence (Röltgen Fig 7). Nobel Fig 2 sits in A's assets but is unused, which is intended according to its records.

### B
- **Nobel press-release Fig 2 (U vs ψ, with the inflammatory signal crossed out).** Shows both effects, more protein and less alarm. The caption corrects the drawing's overstatement.
- **Pardi Fig 3 (injection, then dendritic cell migration, then the lymph node).** Teaches where the training happens. The caption flags the skin versus muscle difference.
- **Röltgen Fig 7 (vaccine mRNA and spike in germinal centres, days 7 to 60).** Primary evidence that the mRNA lasts weeks in lymph nodes. The figure is very dense for a novice even though the text points to panels B and D.
- **Polack Fig 3.** Same as in A. B gives the correct no-prior-infection denominator.
- **Feikin Fig 2 (effectiveness by months since the last dose).** Shows waning, with protection against severe disease holding up better. It is dense, with four vaccines mixed in.
- **Generated SVG (mRNA read in the cytoplasm and broken down, with three numbered blocked steps toward the nucleus).** The DNA answer in mechanism form.
- **Missing compared with A.** A figure of the inside of a cell (Nobel Fig 4) showing the mRNA stopping at the ribosome while spike goes to the surface. B's SVG covers this only schematically. B also lacks a summary of the adaptive arms like A's card grid.

## Probes (0/1/2)

| Probe | A | B | Notes |
|---|---|---|---|
| Q1 mRNA's normal job | 2 | 2 | |
| Q2 what it encodes and what happens after injection | 2 | 2 | |
| Q3 how it trains immunity | 2 | 2 | Both cover B cells, antibodies, T cells, and memory. |
| Q4 why lipid nanoparticles and modified bases | 2 | 2 | |
| Q5 why it can't change DNA | 2 | 2 | Both give the three barriers and degradation. |
| Q6 how long it lasts | 2 | 2 | Both say weeks in lymph nodes and that protection comes from memory. |
| Q7 evidence and limits | 1 | 1 | Both give 95% and waning. A mentions only mild reactions, and B explicitly leaves side effects out. Neither mentions myocarditis. |
| Q8 new-virus transfer | 1 | 0 | A gives the fast part (swap the sequence, same delivery) but not what still takes time, which is trials and approval. B has nothing. |
| **Total** | **14** | **13** | |

## Factual errors and overclaims

### A
- "8 in the vaccine group against 162 with placebo, out of roughly 21,700 people in each group". The 8 vs 162 comparison was in the evaluable no-prior-infection population of about 36,500 people in total, roughly 18,000 per arm. The figure of about 21,700 per arm is the mITT and safety population. This is a minor denominator mix-up.
- "The slow fade of antigen there may be part of why the response gets strong". This is hedged speculation and is acceptable.
- "Both licensed COVID-19 mRNA vaccines replace every U". This is correct and attributed to the Nobel Committee.
- I found no consequential errors.

### B
- I found no factual errors.
- "consistent with blood antibodies declining while memory cells persist" is an interpretation that Feikin's figure does not test directly. It is hedged.
- "Side effects are outside this report" is an omission against the probe set, not an error.

## Verdict

**B gives a reader real understanding faster.** It answers the question in about 60% of A's words, with every key claim backed by a primary exhibit, and it adds the lymph-node route and quantified waning, which A lacks.

The shorter report did lose some things. B drops A's explicit teaching of innate versus adaptive immunity, A's lipid-delivery and cap/tail detail, Nobel Fig 4's inside-the-cell picture, and A's partial answer to the new-virus transfer question. B's extra data figures (Röltgen, Feikin) are also harder for a novice to read than A's illustrations.

On balance, B wins the rubric total (57 vs 54) through density, exhibits, and research. A wins on foundations and probes (14 vs 13). The margin is narrow, and A remains the better pick for a reader with weaker biology.
