# Judge: rates3 (A vs B)

Rendered both reports with Playwright (chromium) at 1280px and 390px. Screenshots and script are in `evaluation/scratch-judge-rates3/`. Neither page has horizontal page overflow. Neither report has real interactive controls. The only operable elements are scroll regions and image links, and I exercised both. I counted words from visible text, captions included.

## Scores

| | Prereq | Order | Mechanism | Evid. foundations | Accuracy | Transfer | Exhibits | Readability | Presentation | Signal density | Time to answer | Research | Visual | Total /65 | Probes /16 | Words |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 4 | 5 | 4 | 4 | 4 | 4 | 3 | 5 | 4 | 5 | 5 | 4 | 3 | **54** | **13** | 1,592 |
| B | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | **60** | **15** | 3,472 |

### Notes on scores
- **A, prerequisites.** A never defines inflation as a sustained rise in the general price level. It does teach the policy rate, IORB, potential output, the output gap and the real rate.
- **A, exhibits and visuals.** A's two embedded figures are Fed schematics, and Fig 3.3 shows a rate *cut* on mechanics a novice barely needs. A chose not to embed the BoE GDP and inflation charts because of rights and links to them instead. Its own SVG timeline is clear and honest ("Only stated milestones are plotted"), but at 390px it is cut off at month 6 with no scroll cue, so the key milestones sit off screen.
- **B, exhibits and visuals.** Every figure supports a step of the argument, and each caption tells the reader how to read it and where it stops. The Buda Fig 2 panel grid is dense for a novice, and on mobile it needs horizontal scrolling.
- **B, readability.** B is longer. A few passages, such as the mortgage-wait wording caveat and the paragraph on Havranek's two response shapes, add load for this reader.
- **Research.** A used 5 sources: BoE 1999, the Fed Explained, an FRBSF letter, a Waller speech, and a KC Fed note. Its audit and evidence records are careful about limits and rights. One gap is that it took the claim about how often prices change from Waller's speech instead of a micro study, and it flags that itself. B used 5 sources: BoE 1999, a peer-reviewed meta-analysis, Nakamura and Steinsson (QJE), a Bank Underground post, and a 2026 Dallas Fed working paper. Each step of the lag explanation has its own primary evidence. Its records are thorough, including the price-level versus inflation trough distinction, the shock size, and the wording mismatch in the post. B is the stronger body of research.

## Visuals

**A**
1. Fed Fig 3.1 (source figure). Five boxes running from the policy decision to the goals, showing that the decision reaches prices only through rates and choices.
2. Fed Fig 3.3 (source figure). How IORB and ON RRP pull market rates. It is drawn for a cut, and the caption says to reverse it.
3. Generated SVG timeline. Plots BoE and FRBSF milestones on one 36-month axis: rates move at once, output falls most near month 15, inflation near month 27. This is the best single visual for the "why so long" question, though mobile clips it.
4. A should have had several of B's visuals. The most important are BoE Charts 1–2, which show output moving before inflation. A links them but does not show them. It also lacks the BoE transmission diagram with its four channels, and B's evidence on how often prices change and on mortgage fixing.

**B**
1. BoE transmission diagram (source figure). The official rate fans out to market rates, asset prices, expectations and the exchange rate, then to demand, then to inflation.
2. BoE Charts 1–2 (source figures, paired). GDP bottoms around Q5 and inflation around Q9. They make the lag visible directly.
3. Havranek and Rusnak Fig 2 plus Table 2 (source figure and table). The distribution of lag estimates shows there is no single lag.
4. A transcribed HTML table of Table 2 (table). Makes the lag numbers readable.
5. Bank Underground Chart 1 (source figure). The time UK mortgages are shielded from rate changes rose from about 1 year to 3.5 years, so fixed-rate debt slows transmission.
6. Buda et al. Fig 2 (source figure). Daily data show spending falls within weeks while employment drifts down. The lag is in supply chains and prices, not spending.
7. Buda et al. Fig 13 (source figure). CPI declines last and gradually, deepening after month 6.
8. B could have used one generated summary graphic like A's timeline, putting all the delays on one clock. It is not essential, because Charts 1–2 cover that point.

## Probes (0/1/2)

| Probe | A | B | Note |
|---|---|---|---|
| Q1 inflation and the policy rate | 1 | 2 | A explains the policy rate well but never defines inflation. B gives a definition and a £100 to £105 example. |
| Q2 reaching households and firms | 2 | 2 | A uses a car-loan example and B a mortgage example. Both cover saving. |
| Q3 why less spending lowers inflation | 2 | 2 | Both explain the output gap and wages. |
| Q4 other channels | 2 | 2 | Both cover assets, the exchange rate, investment and expectations. |
| Q5 expectations | 2 | 2 | Both use the real-rate example. B also explains anchoring more fully. |
| Q6 why so long | 2 | 2 | Both cover contracts, inventories, sticky prices and the timing. |
| Q7 costs and risks | 1 | 2 | A covers overtightening and the supply limit, but job and output losses appear only inside the mechanism, never named as the cost. B says outright that "costs some output and jobs" and covers overtightening and redistribution. |
| Q8 oil supply shock | 1 | 1 | Both say rates cannot create supply and can only cut demand elsewhere at a cost. Neither ties this to stopping second-round effects on wages or expectations. |
| **Total** | **13** | **15** | |

## Factual errors and overclaims

**A.** I found no hard errors. The car-loan arithmetic is correct ($594.04 a month becomes $608.29), and the BoE milestones match the records. There are a few soft points:
- "Governor Waller notes firms typically change prices about once a year" is attributed correctly, but it is a speech summary, not micro evidence.
- "which he says cut roughly six months off the usual lag" is one policymaker's view. A labels it a view in its source tile, but the body text could read as settled fact.
- The timeline puts a UK model and US estimates on one axis. The caption discloses this, so it is acceptable.

**B.** I found no hard errors. There is one mild overclaim and a few soft points:
- The short answer says "studies across many countries put the typical delay at around two years or more". That evidence is Havranek's figure for when the *price level* reaches its low point, not the inflation lag. The figure caption gives the qualifier ("These measure the price level's low point, not inflation's"), but the short answer does not.
- "Most inflation-targeting central banks set their policy horizon at 12 to 24 months ... according to Havranek and Rusnak" is attributed but does not appear in the evidence records. It is plausible from the paper's introduction.
- The Buda figures cover one country, a one-year window and a 4bp shock. The captions state these limits.

## Verdict

**Real understanding faster.** A gets a reader to a correct, usable model faster, with half the words and a crisp short answer, and its one timeline graphic directly answers "why so long". B gives deeper and better-evidenced understanding. It *shows* output moving before inflation, the spread of lag estimates, fixed-rate shielding, and spending falling fast while prices stay sticky.

**Did the shorter one lose anything important?** Yes. A dropped the visual evidence that matters most. It linked the BoE output and inflation charts instead of showing them, and it has no primary evidence on how often prices change or how mortgages are fixed. It also lost a definition of inflation and an explicit statement of the cost in jobs and output. In text it kept nearly every probe and every mechanism step.

**Why B wins overall.** The gap is in exhibits, research and visual explanation, not in length. A could have closed most of it with the BoE charts and one sentence each defining inflation and naming the unemployment cost. B's extra length is mostly evidence, and much of it earns its place.
