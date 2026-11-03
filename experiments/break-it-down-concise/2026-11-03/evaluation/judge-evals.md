# Blind judge: AI application evals (reports A–D)

Inputs read: the four `report.html` files (rendered with Playwright at 1280px and 390px, in light and dark color schemes), each report's `records/source-audit.md` and `records/evidence.md`, the rubric, and the probe file. No source URLs needed opening; doubtful facts were checked against the records' transcribed values and by recomputing the arithmetic (both calculators' intervals, 0.75³). Screenshots and scripts are in `evaluation/scratch-judge-evals/`.

Rendered body text length: A 3,562 words, B 1,352, C 1,597, D 1,934. None of the reports overflows horizontally at 390px; wide SVG, tables and code sit inside scroll containers. All four ignore `prefers-color-scheme: dark` and stay light, a small issue shared by every report. The calculators in A and D work. None of the reports shows how it was produced, apart from ordinary source-vetting notes in captions.

## Score table

Dimensions: 1 prerequisites · 2 dependency order · 3 mechanism · 4 evidence for foundations · 5 accuracy · 6 transfer · 7 exhibits · 8 readability · 9 presentation · 10 signal density · 11 time to answer · 12 research quality.

| Report | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | Total /60 | Probes /16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 3 | 2 | 5 | 53 | 16 |
| B | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 4 | 52 | 16 |
| C | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 4 | 4 | 53 | 15 |
| D | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 58 | 16 |

## Probe scores (0/1/2)

| Probe | A | B | C | D |
|---|---|---|---|---|
| Q1 working call is not proof | 2 | 2 | 2 | 2 |
| Q2 parts of an eval | 2 | 2 | 2 | 2 |
| Q3 defining "correct" for support | 2 | 2 | 2 | 2 |
| Q4 grader types and limits | 2 | 2 | 2 | 2 |
| Q5 repeated runs and variability | 2 | 2 | 2 | 2 |
| Q6 how evals guide changes | 2 | 2 | 2 | 2 |
| Q7 growing the set after launch | 2 | 2 | 1 | 2 |
| Q8 95% score but refund complaints | 2 | 2 | 2 | 2 |
| Total | 16 | 16 | 15 | 16 |

The probes barely separate the reports. On Q5, all four explain repeated trials through pass^k. Only A and D also teach the other half of the key, that a pass rate over a small number of cases is itself uncertain. B and C still get 2, because a novice could answer "why run it several times" from either one. That gap shows up instead in dimensions 3 and 6. On Q7, C only implies that the set grows. It says an eval "measures only the cases you wrote" and is paired with monitoring, but it never says that production failures become new cases.

## Report A (3,562 words)

**Teaches best.** A is the most complete foundation. It shows why `assert` fails, using the `add(2, 3)` contrast and two correct refund phrasings. It then lays out the four-part loop with a diagram, compares three grader types, and gives a runnable harness that uses both a code check and a judge. It shows criteria drift with the Shankar quote, and it makes the warning "a judge that always says PASS agrees 90% of the time" concrete. Its Wald error-bar calculator includes the √n consequence ("halving the error bar takes four times as many cases") and Miller's paired-comparison tip. It also explains clearly why τ-bench's end-state grading makes many reruns cheap. The final limits section is well bounded.

**Errors and overclaims.**
- "The paper also documents judges preferring longer answers and favoring their own outputs." Zheng et al. present self-enhancement bias only tentatively, because they had limited data, so "documents" overstates it. This is minor.
- "removing the policy from gpt-4o's prompt barely changed its retail score". This is plausible, but the claim goes beyond A's own records, whose evidence file lists the policy-ablation table as an "omitted candidate". It is therefore unsupported in A's evidence chain.
- Otherwise accurate. The calculator values check out (50 cases at 80% gives ±11.1; 400 cases gives about ±3.9). It correctly reports the 85%/81% agreement figures together with the 66%/63% figures that count ties.

**Costs.** About 650 words of source descriptions come before "The short answer", roughly two phone screens. Source limits are then repeated in captions and again in the closing section, for example the "2024 models" caveat appears four times. A spends many words to reach the same understanding D reaches in 55% of the length.

**Omits relative to D.** The distinction between capability and regression evals, the warning that graders themselves have bugs, Husain and Shankar's TPR/TNR framing, and the point that public benchmarks are not product evals.

## Report B (1,352 words)

**Teaches best.** B is the fastest route to a usable mental model. A five-line source list leads to a short answer that already names the whole recipe. B introduces the task, trial, transcript and outcome vocabulary, including the key point that the outcome "can differ from what the assistant claimed." Its grader table sets strengths and weaknesses side by side. Its code runs each task five times and flags "INCONSISTENT" results. It is the only short report besides D that names capability versus regression suites and the warning that "evals need debugging too" (4 of the 40 τ-bench failures were task errors, and Anthropic's score rose from 42% to 95% after grading fixes).

**Errors and overclaims.**
- "Husain labels 25 to 50 transcripts himself". In Husain's case study a domain expert does the labeling, so the attribution is slightly off.
- Shankar et al. is listed as an arXiv "research preprint". The records note the UIST 2024 header, so this understates the source.
- "which makes the test harsher than typical use". This is a reasonable inference but no source states it.
- B never explains *why* outputs vary ("can return a different reply each time"), so the sampling mechanism is missing.

**Omits relative to D.** Uncertainty about the score and its dependence on sample size, so the reader cannot tell whether a change from 80% to 85% means anything. It also omits pass/fail versus 1–5 scales and how to measure a judge (TPR/TNR). Its research leaned on fetch-tool summaries for the Anthropic and Husain posts ("read: partial"), which is weaker than C's and D's full reads.

## Report C (1,597 words)

**Teaches best.** C has the best use of a running example. The cracked-mug, order-1042, $18 refund recurs through the vocabulary, the graders, the pass^k arithmetic and the code, which keeps the cognitive load low. It is the only short report that explains *why* outputs vary ("picks each next word with some randomness") and why one prompt "couples everything." It defines pass^k from first principles before showing the τ-bench figure ("0.75³, about 42%"), contrasts pass^k with pass@k by use case, and includes τ-bench's actual unbiased estimator `comb(c,k)/comb(n,k)`. Its explanation of each τ-bench failure type, including "partially resolve", is the clearest of the four.

**Errors and overclaims.**
- "The pairs were deliberately near-identical, so real cases flip less." This is stated as fact, but it is an inference.
- "Solid lines fall because ... only sampling randomness changing." This is broadly right. D's records note that the agent ran at temperature 0, so most of the variation came from the simulated user. C does not mention that, though it is not wrong.
- No hard errors were found. The Table 2 values and the 85%/81% figures match the records.

**Omits relative to D.** Score uncertainty and error bars, criteria drift (it reads failures but never says the rubric emerges from reading), pass/fail versus scales, how to measure a judge beyond "revises the judge's prompt until its labels match", and an explicit step that feeds new production failures back into the suite (Q7). Its research uses four sources and no statistics source. The sources it did audit were audited well, including the τ-bench README noting that the original tasks are outdated.

## Report D (1,934 words)

**Teaches best.** D covers the most ground per word. It separates product evals from public benchmarks and starts with a tiny loop the reader could write that day. It caption-teaches the "I did it!" versus actual-state distinction from Anthropic's first figure. It shows a real mixed-grader refund spec in YAML, with the caveat that exact tool-call sequences punish valid routes. It turns error analysis into steps a beginner can follow: open coding, axial coding, saturation, and criteria drift. It argues for pass/fail over 1–5 scales with a reason. Judge validation becomes two computable numbers, TPR and TNR, with worked examples. It explains end-state grading in τ-bench and notes that grading still misses things ("a refund issued without the customer's confirmation"). Its Wilson-interval calculator is the right choice at small n and says why. It closes with capability versus regression evals, grader bugs, and monitoring.

**Errors and overclaims.** None found. The Wilson interval (40 cases at 80% gives 65–90%) checks out. D's vetting caught a real discrepancy: the τ-bench text says "~55%" for wrong info, against 22.2% in the figure, and D flags it in the caption. It also rebuilt Table 2 from transcribed values because reuse rights were unstated. Every claim is bounded ("practitioners' defaults, not controlled findings").

**Costs.** It is denser than B and C. "open coding", "axial coding", "true positive rate" and the YAML block raise the cognitive load for a novice, although each term is glossed. Five source entries (about 400 words) come before the short answer.

## Ranking (real understanding, fast)

1. **D**. It matches or exceeds A's understanding at 55% of A's length, and it has the strongest vetting.
2. **C**. It is the clearest first-principles build (sampling mechanism, running example, pass^k from arithmetic), but it lacks score uncertainty, criteria drift and the feedback loop after launch.
3. **A**. Its understanding is about equal to D's, but it is slow. About 650 words of sources come before the answer, and its caveats repeat.
4. **B**. It is the fastest and has no real errors, but it is the thinnest on mechanism (no explanation of why outputs vary, no error bars) and its research relied on summaries.

C and A tie on total score. C ranks higher because the reader gets most of the understanding in under half the reading time.

**Which shorter reports match the best long one.** A is the long report. D matches it on every probe and rubric dimension except time to answer, where D is faster. C and B match it on the core recipe (Q1–Q4, Q6, Q8). Neither matches A's treatment of how sure you can be of a score, and C also misses criteria drift and growing the set after launch.

## Patterns: words that earned their place vs. wasted

**Worthwhile**
- **A running concrete case reused across sections.** C's mug ("refund the $18, say what happens next, and promise nothing your policy forbids") turns every abstract term into a check the reader can picture.
- **Captions that tell the reader where to look and what it means.** D wrote: "the grader ignores the agent's 'I did it!' and checks the result, just as a support reply saying 'refund processed' proves nothing until the refund exists." A wrote: "Follow the orange gpt-4o line."
- **Arithmetic before the chart.** C's "0.75³, about 42%" makes pass^k obvious before the τ-bench figure appears.
- **Turning a warning into a number.** A: "a judge that always says PASS agrees 90% of the time on a set that is 90% good while catching nothing." D: "8 of 10 is 80%".
- **Interactive uncertainty.** D: "At 40 cases, 80% is compatible with anything from 65% to 90%, so a move to 85% proves nothing alone."
- **Saying what each failure type implies for testing.** A: "A 'wrong argument' ... which a code check on the tool call catches". D did the same in its figure caption.
- **Short, bounded closing limits.** D: "practitioners' defaults, not controlled findings; adjust them when your own data disagrees."

**Wasted**
- **Long source descriptions placed before the answer.** A's "Sources and how far to trust them" runs to seven entries and about 650 words, and on a phone the short answer starts about two screens down.
- **Repeating the same caveat.** A gives the "2024 models" qualification in its source list, under the pass^k chart ("These are 2024 models, and the chart says nothing about current ones"), in the failure-chart text, and again in "What evals can and cannot tell you."
- **Reconciling sources at length when one line would do.** A's paragraph squaring Husain's cost ladder with Anthropic's "volume over quality" adds little for a beginner.
- **Generic code that does not use the example's specifics.** D's first loop (`must_mention: "refund"`) is less instructive than its later YAML. B's and C's code shows the support state directly.
- **Asserting without a reason.** B says "Prefer code where possible, because model graders err systematically" before it shows the bias. C states the position-test qualifier as fact ("so real cases flip less").
