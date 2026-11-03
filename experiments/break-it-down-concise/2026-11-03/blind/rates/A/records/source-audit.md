# Source audit records

Claims
- C1: A central bank directly controls only one short-term interest rate; that rate passes quickly to other short-term market and bank rates.
- C2: Higher rates reduce spending by households and firms (debt payments, saving incentive, asset/house prices and collateral, exchange rate, confidence).
- C3: Lower demand relative to supply capacity reduces pressure on wages and prices, and a stronger currency lowers import prices, so inflation slows.
- C4: Inflation expectations matter: real rate = nominal minus expected inflation; expectations feed wage and price setting; credibility determines where inflation settles.
- C5: Size of the lag: peak effect on output after about a year and on inflation after about two years (with wide variation; literature average around 29 months).
- C6: Why lags are long: retail rates and fixed-rate mortgages adjust slowly; spending changes ripple through inventories, orders, production, employment and wages; prices are reset infrequently. Modern daily data show demand responds within weeks while prices still lag.
- C7: Limits: monetary policy works on demand, not supply capacity; effects vary with circumstances; rate rises redistribute between borrowers and savers.

### The transmission mechanism of monetary policy
- url: https://www.bankofengland.co.uk/-/media/boe/files/quarterly-bulletin/1999/the-transmission-mechanism-of-monetary-policy.pdf; text read from: same
- byline: Bank of England staff under the guidance of the Monetary Policy Committee · central bank report · Bank of England Quarterly Bulletin, May 1999, pp. 161–170 · May 1999
- verdicts: C1 pass; C2 pass; C3 pass; C4 pass; C5 conditional (model simulation from a 1999 UK model; illustrative, not a forecast; state with the MPC's own uncertainty caveat and pair with the meta-analysis); C6 pass for the spending→inventories→production→employment chain and slow retail-rate adjustment; conditional for UK mortgage structure ("most mortgages ... still floating-rate" is historical, superseded by Bank Underground 2019); C7 pass
- use: p.161 summary and transmission diagram; pp.162–166 links in the chain (short rates, asset prices, exchange rate, individuals, firms); p.167 second-round effects and Time-lags section; pp.167–168 output gap; p.168 inflation expectations and real rates; p.170 Charts 1 and 2 with simulation description
- credibility: Written by the central bank's own staff for its rate-setting committee, at the request of the UK parliament's Treasury Committee and Lords committee, to describe how the committee itself believes its decisions work. Firsthand institutional access.
- contribution: A complete causal account from the official rate to inflation, plus model simulations of a one-point rise held for a year: GDP falls up to 0.2–0.35% after about five quarters; inflation barely moves in year one and falls 0.2–0.4 points, bottoming about nine quarters out.
- limits: Dated (1999) for institutional detail (repo operations, floating-rate mortgages). Simulations come from one macro model with two policy-rule assumptions; the paper itself says they are not forecasts and cannot show how much rates must move to achieve a given inflation fall. Expectation and confidence effects are described as ambiguous in direction. No retraction applies (institutional report); its 1-year/2-year rule of thumb is cited as Bank of England 1999 in Havranek & Rusnak 2013, p.40 (checked).
- read: full (10 pages) · via direct PDF

### Transmission Lags of Monetary Policy: A Meta-Analysis
- url: https://www.ijcb.org/journal/v9n4/transmission-lags-monetary-policy-meta-analysis; text read from: https://www.ijcb.org/sites/default/files/journal/v9n4/ijcb-v9n4-transmission-lags-monetary-policy-meta-analysis.pdf
- byline: Tomas Havranek and Marek Rusnak · peer-reviewed journal article (meta-analysis) · International Journal of Central Banking 9(4), pp. 39–76 · December 2013
- verdicts: C5 pass (as an average across studies, with its spread); C6 conditional (its financial-development explanation is a statistical association plus the authors' interpretation about hedging, not a demonstrated mechanism)
- use: abstract; section 1; section 2 incl. Figure 1, Figure 2 and Table 2 (p.45), Table 3 (p.46); conclusion (p.~70)
- credibility: Researchers at the Czech National Bank research department and Charles University; quantitative synthesis of 198 impulse responses from 67 published VAR studies covering 30 economies, with inclusion criteria (normalised 1-point shocks, confidence intervals reported) and public data/code.
- contribution: Measures when the price level bottoms out after a 1-point policy rate rise: raw mean 33.5 months (median 37, sd 19.4, range 1–60); corrected average 29 months; developed economies 25–50 months; mean maximum price fall 0.9%. Lags estimated from hump-shaped responses average 18.2 months vs 49.1 for strictly decreasing ones.
- limits: Measures the price level's trough, not the inflation rate's; strictly decreasing responses can imply implausibly long lags (authors note); estimates depend on VAR methods, and monthly-data studies report faster transmission. Data mostly decades before 2013. One search for errata or retraction found none.
- read: partial (abstract, sections 1–2, tables 2–3, conclusion; skimmed section 3–4 regressions) · published version

### Five Facts About Prices: A Reevaluation of Menu Cost Models
- url: https://academic.oup.com/qje/article/123/4/1415/1928235 (unverified canonical link); text read from: https://business.columbia.edu/sites/default/files-efs/pubfiles/3556/fivefacts.pdf (author-hosted copy of the QJE article, p.1415 header and QJE copyright line visible)
- byline: Emi Nakamura and Jón Steinsson · peer-reviewed journal article · Quarterly Journal of Economics 123(4), pp. 1415– · November 2008
- verdicts: C6 pass (for the narrower claim that individual US consumer prices excluding sales change only about once every 8–11 months at the median)
- use: abstract; introduction pp.1415–1417; section on frequency and Table I notes (implied duration = −1/ln(1−f))
- credibility: Uses the Bureau of Labor Statistics micro-data underlying the US CPI and PPI (1988–2005), a primary data set; authors are leading empirical macroeconomists (Nakamura later received the Clark Medal for this line of work).
- contribution: Median monthly frequency of non-sale price change for identical items is 9–12%, implying median regular-price durations of 8–11 months; including temporary sales the frequency is 19–20%.
- limits: US data, 1988–2005; with sales counted, prices change about twice as often, so "how sticky" depends on whether temporary sales matter for inflation. Frequency of price change can rise when inflation is high (their fact 3), so stickiness is not fixed. One search found no erratum.
- read: partial (abstract, introduction, frequency section and table notes) · author copy

### Bitesize: Fixing ideas – The Slowing of Interest-rate Pass-through to Mortgagors
- url: https://bankunderground.co.uk/2019/09/27/bitesize-fixing-ideas-the-slowing-of-interest-rate-pass-through-to-mortgagors/; text read from: same
- byline: Fergus Cumming · staff blog post · Bank Underground (Bank of England staff blog) · 27 September 2019
- verdicts: C6 conditional (UK only, to 2019; blog views are not official Bank positions; says how long payments are shielded, not how long spending or inflation takes)
- use: Chart 1 (average time shielded from interest-rate changes, 2005–2019) and text
- credibility: Author works in the Bank of England's Monetary Policy Outlook Division and uses the regulator's Product Sales Database of mortgage transactions.
- contribution: Before the financial crisis UK mortgagors waited just over a year before Bank Rate changes reached their payments; by 2019 almost three times as long (chart ≈3.5 years). Variable-rate share of new mortgages fell from about a third to under 1 in 20.
- limits: Text describes "the average new mortgagor"; the chart note describes the stock of primary residential mortgages — a wording inconsistency, so state it as average time shielded. Blog, not peer reviewed. Pre-2022 tightening.
- read: full · post is short

### The Short Lags of Monetary Policy
- url: https://www.dallasfed.org/~/media/documents/research/papers/2026/wp2631.pdf (https://doi.org/10.24149/wp2631); text read from: same
- byline: Gergely Buda, Vasco M. Carvalho, and colleagues · working paper · Federal Reserve Bank of Dallas Working Paper 2631 · September 2026 (earlier version circulated 2023 as "Short and Variable Lags", CEPR DP18022)
- verdicts: C6 pass (for Spain, 2015–2023, as a refinement: demand falls within weeks, CPI and permanent employment adjust gradually); C5 conditional (one country, one-year horizon, small identified shocks)
- use: abstract; introduction pp.1–6; Figure 2 (p.26); section 4 "Taking stock" (pp.28–29); section 7.3 and Figure 13 (pp.50–51)
- credibility: Academic and central-bank researchers (Cambridge, EUI, UCL/Dallas Fed, ECB/Banco de Portugal, BBVA Research) using bank-transaction records and administrative tax and social-security data, with policy shocks identified from high-frequency market surprises.
- contribution: Consumption and sales respond within days to weeks; retailers accumulate inventories first, then manufacturers; employment falls gradually with trough around a year; CPI declines gradually, deepening after month 6, trough around month 11 within the one-year window. Quarterly data hide the fast response. Authors say this refines rather than overturns "long and variable lags".
- limits: Preliminary working paper, not yet peer reviewed. Spain only; euro-area policy set by ECB. One-year horizon, so it cannot show when inflation's effect fully ends. Shock size is one standard deviation of the identified surprise (3.7–4.1 bp), so magnitudes are not comparable to a 1-point rise. One search found no failed replication; it is a revised version of a 2023 paper.
- read: partial (abstract, introduction, sections 4 and 7.2–7.3, figures 2 and 13; skipped appendices and robustness) · version September 2, 2026

## Gaps
- C5: only conditional sources for a precise current lag — the 1999 model numbers are illustrative and the meta-analysis averages older studies; present as a range, not a single number.
- C6: the hedging/financial-development explanation for long lags is an association; not used as a mechanism.
- C7: the limit that rates cannot fix supply shocks rests on the 1999 statement that monetary policy has little direct effect on supply capacity; no current source on supply-shock episodes was audited, so the report does not discuss 2021–23 causes.
- Disputed premise: none in the question; the question's "why does it take so long" is supported, with the 2026 refinement that spending itself moves quickly.
