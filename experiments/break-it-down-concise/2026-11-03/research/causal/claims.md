# Claims

Question: If people who use a learning app score higher on an exam, why does that not prove the app helped, and how could we find out whether it did? Reader knows averages and percentages, no statistics.

- C1: A higher average exam score among app users than non-users is an association: a comparison between two different groups of people, not between the same people with and without the app.
- C2: The app's causal effect on one student is the difference between the score that student would get with the app and the score the same student would get without it; only one of those two scores can ever be observed (the counterfactual, or "fundamental problem of causal inference").
- C3: The average causal effect compares the whole group in two hypothetical worlds (everyone uses the app vs. no one does); the users-vs-non-users gap compares two subsets in the real world, and the two numbers can differ in size and even in sign.
- C4: When students choose (self-select) whether to use the app, the users-vs-non-users gap equals the true average effect plus selection bias, the difference between what users and non-users would have scored without the app (for example because more motivated or better-prepared students both use the app and score higher).
- C5: Other routes produce a gap without the app helping: reverse causation (doing well leads to using the app), before-and-after comparisons that absorb other changes over time, and usage-versus-score correlations, which are not causal even inside an experiment.
- C6: "Controlling for" measured characteristics (regression, matching) removes only differences that were measured; unmeasured differences can remain, cannot be ruled out from the data, and in real tests such adjusted comparisons have given badly wrong answers.
- C7: Random assignment (a coin flip, lottery, or randomized trial) makes the app and no-app groups alike on average in both measured and unmeasured traits, so the difference in their average scores estimates the app's average causal effect.
- C8: Even with randomization, groups differ somewhat by chance, so trials check baseline balance and report uncertainty (standard errors, p-values); larger samples shrink chance differences, and a small observed difference may be indistinguishable from zero.
- C9: Randomized evaluations of real learning software show that the answer has to be measured, not assumed: a large U.S. federal trial of 16 reading and math products found no statistically significant test-score gains after one year, while a lottery-based trial of an adaptive program in Delhi found large gains; reviews of experiments find mixed but often positive results, especially in math.
- C10: Real experiments raise practical issues that change what is estimated: not everyone offered the app uses it (effect of the offer vs. effect of use), students drop out of follow-up, effects can spill over to others, results come from particular products, places and tests, and generalizing beyond them needs care.
- C11: When randomizing is impossible, quasi-experimental designs (natural experiments and lotteries used as instruments, regression discontinuity at an eligibility cutoff, difference-in-differences, matching) can approximate it, but each rests on an assumption that cannot be fully verified.

## Claims the direct answer depends on most

C1, C2, C4 (why the gap does not prove the app helped) and C7 (how to find out). C3 supplies the precise contrast; C6 and C9 carry the strongest evidence that the distinction matters in practice.
