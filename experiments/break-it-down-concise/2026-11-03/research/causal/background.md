# Background notes (settled textbook material; no records required)

## Concepts the explanation needs, in the reader's terms

- **Average and difference in averages.** The reader already has these. Every comparison in the report is "average score of group 1 minus average score of group 2." The whole topic is about which two groups you are allowed to compare.
- **Association (correlation).** Two things tend to go together in data: app users tend to have higher scores. It says nothing yet about why.
- **Cause / causal effect.** The app causes a higher score for a student if that student would have scored lower without it, everything else the same. Defined by a "what if" comparison of the same student, not by a comparison of different students.
- **Counterfactual.** The outcome in the world that did not happen (the student's score had they not used the app). Never observed for anyone; that is the core difficulty. Sources call the pair of outcomes "potential outcomes."
- **Confounder / common cause.** Something that affects both app use and scores (motivation, prior grades, parental involvement, time available, having a phone and quiet place to study). It creates a gap without the app doing anything. "Selection bias" is the name for the resulting difference between the groups' no-app scores when people choose their group.
- **Reverse causation.** Scores (or the strengths behind them) can drive app use: students doing well may enjoy the app and use it more; struggling students may give up on it. Settled reasoning; the only source instance read is Mixtape's Yule critique.
- **Chance.** Any two groups differ a bit by luck. Statistical significance (p-values) asks whether a gap is bigger than luck alone would usually produce; it does not ask whether the gap is causal (World Bank Table 3.3 has t = −49 for a biased comparison).
- **Random assignment.** Decide who gets the app by coin flip or lottery. Then the only systematic difference between groups is the app; motivated and unmotivated students land in both groups in about equal shares, including traits nobody measured. This is the step that turns "difference in averages" into "average effect."
- **Effect size in standard deviations (SD).** Education studies report gains as a fraction of the spread of scores. Rough guide (Escueta et al. 2017): under 0.10 SD small, 0.10–0.25 encouraging, 0.25–0.40 large, above 0.40 very large. IES: 0.03 SD ≈ 0–2 percentile points. One SD on a typical bell-shaped test is roughly the distance from the 50th to the 84th percentile (standard normal-distribution fact).
- **Intent-to-treat vs. effect of use.** In real trials some people offered the app never open it. Comparing everyone offered vs. everyone not offered (intent-to-treat) keeps the fair comparison; it measures the effect of offering the app. Estimating the effect of actually using it needs an extra step (Mindspark uses the lottery as an "instrument"). Comparing heavy users with light users inside the trial reintroduces self-selection (IES and Mindspark both say so).
- **Quasi-experiments (when you cannot randomize).** Brief, plain descriptions are enough: regression discontinuity compares students just above and just below an eligibility cutoff (e.g., a test score that decides who gets the app); difference-in-differences compares the change over time for users against the change for non-users, assuming they would have changed alike; matching compares users with non-users who look similar on measured traits; natural experiments and lotteries use some as-if-random event. Each swaps randomization for an assumption that cannot be fully checked (World Bank Table 11.2; Hernán & Robins Ch. 3).

## Prerequisite order that works

1. What the reader's observation is (a gap between two groups' averages) → association.
2. What "the app helped" means → the same student, two worlds; one is missing.
3. Averaging over many students → average effect vs. users-vs-non-users gap; they can differ.
4. Why they differ → self-selection: gap = effect + selection bias (Mixtape decomposition, generated app example).
5. Other non-causal routes → reverse causation, before-after, usage correlations.
6. Why "controlling for" is not enough → unmeasured traits; LaLonde's real test.
7. The fix → random assignment; balance check; IES table shows balanced groups.
8. Reading a result → difference, uncertainty, effect size; IES null vs. Mindspark large gain.
9. Practical wrinkles → not everyone uses it, dropouts, which app/where/which test.
10. When you cannot randomize → quasi-experiments and their assumptions.
11. Implication: ask "compared with whom, and how were they chosen?"

## Worked example idea (generated; label as constructed)

Six students. The app raises everyone's score by exactly 2 points. Three motivated students choose the app; three others do not.

| Student | Score without app | Score with app | Chose app? | Observed score |
|---|---|---|---|---|
| A | 80 | 82 | yes | 82 |
| B | 78 | 80 | yes | 80 |
| C | 76 | 78 | yes | 78 |
| D | 64 | 66 | no | 64 |
| E | 62 | 64 | no | 62 |
| F | 60 | 62 | no | 60 |

- Users' average 80; non-users' 62; observed gap 18 points.
- True effect 2 points. Selection bias = users' average without app (78) − non-users' average (62) = 16. Check: 18 = 2 + 16.
- If instead a coin flip decided, each group would on average contain a mix of motivated and unmotivated students; the groups' "without app" averages would match in expectation, and the expected gap would be 2. Any single coin-flip split can still be unlucky (e.g., A, B, C all heads), which is why real trials use many students and report uncertainty.
- Variant for sign reversal: grounded in Mixtape's real worked example (E2–E4), where self-sorting made a beneficial treatment look harmful (−0.4 observed vs +0.6 true). A writer can mention that the gap can also hide a real benefit, or even point the wrong way.
- Variant for usage correlation: within app users, those who log more hours may score higher because the most motivated log more hours; IES (grade 4) and Mindspark both treat such dose patterns as non-causal without further design.

## Source-grounded examples a writer can lean on

- Hernán & Robins: 54% vs 43% death risk (7/13 vs 3/7) with zero causal effect; aspirin halves risk yet looks harmful in raw comparison (both hypothetical).
- Mixtape: ten-patient table with both outcomes known (hypothetical).
- LaLonde 1986: real program, real experimental benchmark (+$886), adjusted survey comparisons often negative (−$8,067 with PSID-1).
- IES 2007: real randomized test of 16 commercial products, no significant gains in year one; balance table; evaluators' own warning that usage correlations are not causal.
- Mindspark 2019: real lottery, balanced baseline, large gains (+0.37 SD math, +0.23 SD Hindi in 4.5 months; control group also improved).
- World Bank HISP: one fictional program, every method, estimates from −$6.65 to −$14.46 around a randomized −$10.14.
