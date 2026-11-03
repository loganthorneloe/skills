# Blind judge: interest rates and inflation (A vs B)

I rendered both reports with Playwright (Chromium) at 1280px and 390px. Screenshots and the script are in `evaluation/scratch-judge-rates/`. Neither page has console errors or page-level horizontal overflow. Neither has interactive controls. In both, every image links to its full-size asset, and B also adds "Enlarged view" links. I read the records in `blind/rates/<letter>/records/`. I counted words from the visible text, with scripts and styles stripped; the counts include the source cards and captions.

## Scores

Columns 1 to 9 follow the rubric. Column 10 is signal density, 11 is time to answer, 12 is research quality, and 13 is visual explanation.

| Report | 1 Prereq | 2 Order | 3 Mech | 4 Evid | 5 Acc | 6 Transfer | 7 Exhibits | 8 Read | 9 Present | 10 Density | 11 Time | 12 Research | 13 Visual | Total /65 | Probes /16 | Words |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 5 | 5 | **59** | **15** | 3,472 |
| B | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 4 | 4 | **58** | **15** | 1,386 |

### Notes on scores

- **Prerequisites and order.** Both define inflation, the policy rate, demand relative to capacity, and the real rate before using them. A gives a £100 to £105 example and explains why the bank can fix the rate ("only supplier of the money banks use to settle payments"). B's line "Slowing it usually means prices rise 2 or 3% a year instead, not that they fall" heads off a common novice misreading, which A only implies.
- **Mechanism.** A explains each channel: debt cash flow, saving, asset valuation and collateral, firms' hurdle rates and inventories, and the exchange rate. It then walks through the lag chain, from fixed-rate mortgages to the retailer, distributor and manufacturer inventory sequence to sticky prices. B covers the same channels in a single paragraph, plus one running furniture-maker example ("raises prices 3% this year instead of the planned 8%"). That example is effective, but the inventory chain gets only two sentences.
- **Evidence and research.** A uses five sources. Two of them add evidence B lacks: Bank Underground 2019, on how fixed-rate mortgages have stretched UK pass-through to about 3.5 years, and Buda et al. 2026, with daily Spanish data showing spending falls within weeks while the consumer price index (CPI) lags. Its audit records the limits of each source, such as the not-yet-peer-reviewed status, shock size, and a wording mismatch in the Bank Underground chart. B uses four sources. Its added source, the Fed FAQ, is current but thin. B's audit openly notes the gap "no post-2010 direct estimate of the lag", and it checked the working-paper figures against the published journal version. Both sets of records are honest and match their reports.
- **Signal density and time to answer.** Both reports open with a sources block before the short answer. A's block holds five long cards, so its answer starts lower on the page. A's captions often restate the prose; for example, the two lag statements from the 1999 Bank of England report appear in the short answer, the timing section, and a caption. B states each point once.
- **Presentation.** At 390px, both reports show the wide transmission diagram inside a horizontally scrolling box, so its right half is cut off until the reader scrolls. B offers an "Enlarged view" link next to it. A's image is clickable but gives no visible cue. A's multi-panel Buda Figure 2 is dense, and its tick labels are small on mobile.

## Visuals

### A
1. **BoE 1999 transmission diagram.** The official rate fans out through four channels to demand, and only demand reaches inflation. Import prices are the one shortcut.
2. **BoE Chart 1 (GDP).** In the model, output bottoms around quarter 5.
3. **BoE Chart 2 (inflation).** Inflation stays flat for a year and bottoms around quarter 9. This chart shows the lag directly.
4. **Havranek and Rusnak Figure 2 density, with Table 2 in the image.** Lag estimates spread from 1 to 60 months in two clusters.
5. **HTML table transcribing Table 2.** Gives the mean, median and range by response shape, in a form the reader can read and copy.
6. **Bank Underground Chart 1.** UK mortgagors' protection from rate changes grew from about 1 to 2 years to about 3.5 years, which is why the household channel is slow.
7. **Buda et al. Figure 2.** Daily sales and consumption fall within weeks, while employment drifts down over a year. This separates fast demand from slow supply-side adjustment.
8. **Buda et al. Figure 13.** CPI and permanent jobs fall slowly over a year. Prices are the last thing to move.
9. **Pull quote from Nakamura and Steinsson.** Regular prices last 8 to 11 months.

**What A could have borrowed from B:** B's stylized impulse-response figure (Havranek and Rusnak Figure 1). It shows what "the lag" measures (the month of the deepest fall in prices), which A explains only in words.

### B
1. **BoE 1999 transmission diagram.** Same lesson as A's, with an enlarge link.
2. **BoE Charts 1 and 2 (GDP and inflation).** Same lesson: output moves first, inflation about a year later.
3. **Havranek and Rusnak Figure 1 (stylized impulse responses).** Defines the transmission lag visually and shows why still-falling responses push the average up.
4. **Havranek and Rusnak Figure 2 density.** Lags are long and widely spread.

**What B should have had from A:** the Bank Underground fixed-rate chart. B states that "Fixed-rate borrowers pay the old rate until their term ends" but shows no evidence for it, and this is a central reason the effect is slow today. Buda Figure 13, or another visual separating fast spending from slow prices, would also have helped. The figure is the strongest direct picture of "demand falls quickly, prices slowly". The Table 2 numbers are a smaller loss; B gives the key averages in prose.

## Probes (0/1/2)

| Probe | A | B | Note |
|---|---|---|---|
| Q1 Inflation and the policy rate | 2 | 2 | Both define inflation and the short-term policy rate. B names the federal funds rate; A names Bank Rate. |
| Q2 Reaching households and firms | 2 | 2 | Both give a mortgage example, the saving incentive, and investment. |
| Q3 Why less spending lowers inflation | 2 | 2 | Both explain demand against capacity and weaker wage bargaining. |
| Q4 Other channels | 2 | 2 | Both cover asset prices, the exchange rate, and expectations. A also covers collateral. |
| Q5 Expectations | 2 | 2 | Both cover the real rate, expectations feeding into wages, and credibility. |
| Q6 Why it takes so long | 2 | 2 | Both cover fixed-rate debt, the inventory chain, sticky prices, and 29-month and 1-plus-1-year estimates. |
| Q7 Costs and risks | 2 | 2 | Both cover lost output and jobs, supply limits, and acting on a forecast. A says outright that the bank "may tighten too much"; B implies it ("probably done enough"). Neither says "recession". |
| Q8 Oil supply shock | 1 | 1 | Both say a rate rise cannot create oil and only cuts spending elsewhere, at a cost. Neither links this to keeping the shock out of expectations and wages, though each has an expectations section a reader might connect. |
| **Total** | **15** | **15** | |

## Errors and overclaims

No consequential factual errors in either report. The spot checks agree with the records: £2,000 a year on £200k at +1pt, $3,000 a year on $300k at +1pt, 29 months, 0.9%, 25 to 50 months, 8 to 11 months, and quarters 5 and 9.

**A**
- "Before 2008 it was mostly between one and two years". The record says "just over a year" before the crisis. This reads off the chart and is roughly fair.
- "reach their low point within about two months" (Buda Figure 2). This is an eyeball reading of a noisy figure with wide bands for investment. The caption does flag the bands. Minor.
- "Most inflation-targeting central banks set their policy horizon at 12 to 24 months... according to Havranek and Rusnak". This is a secondhand claim, and the record does not show the exact locator. Plausible.

**B**
- "more developed financial systems, where borrowers can shield themselves longer, had longer lags". The audit marks this as a statistical association plus the authors' interpretation (C6 conditional). The report states the mechanism as if it were fact. This is a mild overclaim.
- "by the time inflation is visibly falling, it has probably done enough". This is a reasonable inference that no source directly supports.
- "Fixed-rate borrowers pay the old rate until their term ends". True, but no source in B gives its size or how it has changed over time. B's audit admits the currentness gap.

## Verdict

B gets a novice to real understanding faster. Its answer starts sooner, each point appears once, and its running furniture-maker example ties the rate rise, lower demand and smaller price increases into one concrete chain. On probes, B matches A at 15/16 with 40% of the words.

The shorter report did lose something real, mostly in evidence and visuals rather than in the core explanation. It drops the fixed-rate-mortgage evidence and the modern daily-data finding that spending reacts in weeks while prices lag. Those are A's best answers to "why so long today", and they explain why A scores higher on research and visuals. A's extra length is mostly repetition and long captions, so a trimmed A would have kept those two exhibits.

On balance the two reports are near equal (59 vs 58). B is the better reading experience. A is the better-evidenced answer to the lag question.
