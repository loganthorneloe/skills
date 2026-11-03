# Evidence records

Claim IDs as in source-audit.md.

### E1: Single-turn vs agent evaluations diagram
- claim: C2 (support)
- type: figure
- source: Demystifying evals for AI agents — https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- locator: first figure, section "The structure of an evaluation"
- asset: assets/anthropic-single-turn-vs-agent.png (original 4584×2834 PNG from www-cdn.anthropic.com)
- inspected: opened preview at 1100px; title, both rows, all boxes and grading logic text legible
- notice: Top row is the whole idea in miniature: prompt + data go in, a response comes out, and grading logic (`response == 18`) scores it. Bottom row: for an agent, the grader checks what happened in the environment, not the "I did it!" message.
- limits: Coding-agent example, not support; illustrative.
- rights: rights unstated

### E2: Components of evaluations for agents diagram
- claim: C2 (context)
- type: figure
- source: same as E1
- locator: figure after the definitions list
- asset: assets/anthropic-eval-components.png (downscaled to 2200px wide from 4584px original)
- inspected: opened at 1100px; legend and all labels legible
- notice: A suite holds tasks; each task has graders, tracked metrics and multiple trials; outcome + trajectory feed the graders.
- limits: Not embedded in the report; redundant with E1 and prose.
- rights: rights unstated

### E3: Support-agent eval spec (quote)
- claim: C3, C7 (support)
- type: quote
- source: same as E1
- locator: "Example: Theoretical evaluation for a conversational agent"
- asset: exact text excerpt of the grader YAML: llm_rubric assertions "Agent showed empathy for customer's frustration", "Resolution was clearly explained", "Agent's response grounded in fetch_policy tool results"; state_check tickets {status: resolved}, refunds {status: processed}; tool_calls verify_identity, process_refund amount "<=100", send_confirmation; transcript max_turns: 10
- inspected: not applicable (text copied from fetched page)
- notice: One support task mixes all grader kinds: a model-graded rubric for tone, a code check on database state, required tool calls, a turn limit.
- limits: Labeled "theoretical"; the article says in practice conversational evals lean on model-based graders, and elsewhere warns that requiring exact tool-call sequences is brittle.
- rights: rights unstated

### E4: pass^k falls as trials increase (τ-retail)
- claim: C7, C1 (support)
- type: figure
- source: τ-bench — https://arxiv.org/abs/2406.12045 (v1)
- locator: Figure 4, §5.1
- asset: assets/taubench-fig4-passk.png (rendered at 1800px from authors' figs/passatk.pdf in the arXiv e-print)
- inspected: opened full size; axes, five-model legend, solid/dotted lines, k ticks 1–32 visible
- notice: Solid lines (pass^k: every one of k tries succeeds) fall while dotted lines (pass@k: at least one succeeds) rise. gpt-4o starts near 61% and its solid line ends near 25% at k=8.
- limits: 2024 models, original task files since declared outdated; y-axis is percent of tasks; agent temperature 0, user simulator temperature 1, so variation comes largely from the simulated user.
- rights: CC BY 4.0

### E5: Failure breakdown of 36 failed gpt-4o trajectories
- claim: C8 (support), C4 (context)
- type: figure+metric
- source: τ-bench (v1)
- locator: Figure 5, §5.2
- asset: assets/taubench-fig5-failures.png (rendered from figs/breakdown2.pdf); values: wrong argument 33.3%, wrong decision 25.0%, wrong info 22.2%, partially resolve 19.4% of 36 agent-caused failures (40 failed of 115 tasks, 1 trial each; 4 were task-annotation errors)
- inspected: opened full size; all four labels and percentages visible
- notice: This is a failure taxonomy, the product of error analysis: humans read failed conversations and grouped them. Each category suggests a different check.
- limits: One model, one domain, n=36. Text says wrong info "~55%", conflicting with figure's 22.2%; figure used.
- rights: CC BY 4.0

### E6: Position bias of LLM judges (table)
- claim: C6 (qualify)
- type: table
- source: Judging LLM-as-a-Judge — https://arxiv.org/abs/2306.05685 (v4)
- locator: Table 2, §3.3
- asset: transcribed values — Claude-v1 default: consistency 23.8%, first 75.0%, second 0.0%, error 1.2%; Claude-v1 rename: 56.2 / 11.2 / 28.7 / 3.8; GPT-3.5 default: 46.2 / 50.0 / 1.2 / 2.5; GPT-3.5 rename: 51.2 / 38.8 / 6.2 / 3.8; GPT-4 default: 65.0 / 30.0 / 5.0 / 0.0; GPT-4 rename: 66.2 / 28.7 / 5.0 / 0.0. Rebuilt as HTML (default prompt rows only in distilled report).
- inspected: values copied from HTML v4 text and cross-checked row by row
- notice: Swapping the order of two answers changed the verdict often; even the best judge was consistent only about two-thirds of the time.
- limits: 2023 judges; answer pairs were deliberately similar; consistency is not accuracy.
- rights: rights unstated (arXiv non-exclusive license)

### E7: Judge–human agreement
- claim: C6 (support)
- type: metric+quote
- source: Judging LLM-as-a-Judge (v4)
- locator: §4.2, Table 5 setup S2
- asset: GPT-4 vs human experts agreement 85% (non-tie votes, MT-bench, 80 questions, 58 expert labelers, ~3K votes); human–human agreement 81%
- inspected: not applicable
- notice: A strong judge can match human agreement levels — which is why judges are worth using, and why you measure agreement rather than assume it.
- limits: Pairwise preference on general chat, ties excluded; 2023 model.
- rights: rights unstated

### E8: Error analysis quote
- claim: C4 (support)
- type: quote
- source: AI Evals FAQ — https://hamel.dev/blog/posts/evals-faq/
- locator: "Q: Why is error analysis so important in AI evals"
- asset: "Error analysis is the most important activity in evals."
- inspected: not applicable
- notice: Positions the reading of traces before building any automated check.
- limits: Practitioner opinion.
- rights: rights unstated (short quotation)

### E9: Judge validation metrics
- claim: C6 (support)
- type: metric
- source: AI Evals FAQ
- locator: "Q: How do I know if I can trust my automated eval?"
- asset: TPR example — humans find 10 failures, judge catches 8 → 80%; TNR example — 100 good outputs, judge passes 95 → 95%; split ~10–20% train, 40–45% dev, 40–45% test; 100–200 labeled examples per failure mode
- inspected: not applicable
- notice: Gives the beginner two numbers to compute for any judge.
- limits: Rules of thumb.
- rights: rights unstated

### E10: Standard error of a pass rate
- claim: C9 (support)
- type: metric
- source: Adding Error Bars to Evals — https://arxiv.org/abs/2411.00640 (v1)
- locator: §2.1 Eq. 2 and 95% CI formula
- asset: SE_Bernoulli = sqrt(p̄(1−p̄)/n); CI95 = p̄ ± 1.96·SE; §4.2 recommends paired differences
- inspected: not applicable
- notice: The error bar shrinks only with the square root of the number of cases.
- limits: Normal approximation intended for many questions; calculator uses Wilson interval for small n.
- rights: formula (not copyrightable expression)

### E11: Start with 20–50 tasks (quote)
- claim: C9, C10 (support)
- type: quote
- source: Demystifying evals for AI agents
- locator: "Step 0. Start early"
- asset: "20-50 simple tasks drawn from real failures is a great start."
- inspected: not applicable
- notice: Pairs with E10 — small sets detect large effects only.
- limits: Practitioner advice.
- rights: rights unstated

### G1: Confidence-interval calculator
- claim: C9
- type: generated
- source: Wilson score interval (textbook), motivated by E10
- asset: inline JS in report
- notice: Reader sets number of test cases and pass rate, sees the plausible range of the true rate.
- limits: Assumes independent cases drawn from the same population; ignores grader error.

Claims lacking evidence: none. C5 and C11 supported by quoted text in sources but no exhibit extracted (C11's methods table is long; summarized in prose with attribution). Omitted candidates: Anthropic pass@k vs pass^k chart (duplicates E4 with real data preferred); τ-bench Table 3 (policy-removal ablation, tangential); Pawel Huryn error-analysis diagram in FAQ (student-made, rights unclear).
