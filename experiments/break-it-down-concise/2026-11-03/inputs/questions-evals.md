# Coverage questions — AI application evals (frozen before generation)

Score each 0/1/2 from the report alone. 2 = a novice reading only this report could answer correctly; 1 = partial, implicit, or needs inference the report does not support; 0 = missing or wrong.

Q1. Why does a working API call not show the application works?
Key: model outputs are variable and plausible-sounding; a few good examples don't show behavior across the range of real inputs; you need systematic measurement of task success.

Q2. What is an eval made of?
Key: a set of representative inputs (test cases), a definition of correct/acceptable behavior per case, a way to grade outputs, and an aggregate score/report.

Q3. How do you define "correct" for a customer-support assistant?
Key: turn requirements into checkable criteria (accurate policy answer, correct action/tool use, escalation when needed, tone, refusal of unsafe/out-of-scope requests), ideally with examples of good and bad answers.

Q4. What kinds of graders exist and what are their limits?
Key: exact/code-based checks (cheap, reliable, narrow), model-based graders/LLM-as-judge (flexible, must be validated against human labels, can be biased), human review (gold standard, expensive).

Q5. Why run cases multiple times or look at score variability?
Key: outputs vary between runs; a single run can pass or fail by chance; repeated trials and enough cases make comparisons trustworthy.

Q6. How do evals guide changes?
Key: read failures to find categories (error analysis), change prompt/model/tools, rerun the same eval to compare before/after and catch regressions.

Q7. Why must the eval set keep growing after launch?
Key: real users bring new inputs and failure types; production logs and new failures become new test cases; distribution shift makes old scores stale.

Q8 (transfer). Your assistant scores 95% on your eval, but customers complain it mishandles refund requests for subscriptions. What does that tell you and what do you do?
Key: the eval set doesn't represent that input type (coverage gap), so the score doesn't measure it; collect real examples of the failure, add them with criteria, grade, fix, and rerun to confirm without regressions.
