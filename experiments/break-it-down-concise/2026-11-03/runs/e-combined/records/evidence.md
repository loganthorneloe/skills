# Evidence records

### E1: Components of an agent eval
- claim: C2 (support)
- type: figure
- source: Demystifying evals for AI agents — https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- locator: "The structure of an evaluation", figure captioned "Components of evaluations for agents."
- asset: assets/eval-components.png (1920 px export from the page's image CDN; original 4584 px)
- inspected: opened full size; all boxes, labels, legend visible, no clipping
- notice: Nesting shows a suite holds tasks; each task carries graders and several trials; grading looks at both the transcript and the final environment outcome.
- limits: Drawn for a coding-agent task ("Fix authenticated bypass"), so reader must map it onto support; illustrative, not data.
- rights: rights unstated

### E2: τ-bench pass^k versus pass@k in retail
- claim: C5 (support), C1 (support)
- type: figure+metric
- source: τ-bench — https://arxiv.org/abs/2406.12045 (v1)
- locator: Figure "pass^k (--) and pass@k (..) in retail" (figs/passatk.pdf); text: "Even for the best-performing gpt-4o function calling agent which has a >60% average task success, pass^8 drops to <25%."
- asset: assets/tau-bench-pass-hat-k.png, rendered from authors' vector PDF at 400 dpi
- inspected: opened full size; legend, x-axis ticks, all five model curves visible; no y-axis label in original
- notice: Solid lines (all k tries succeed) fall steeply while dotted lines (at least one succeeds) rise; same tasks, same model, only sampling randomness differs.
- limits: 2024 models; simulated users; y-axis is task success %, stated in caption/text rather than on the figure; some original tasks later corrected.
- rights: CC BY 4.0 (arXiv listing)

### E3: Position bias of LLM judges
- claim: C4 (support/qualify)
- type: table+metric
- source: Judging LLM-as-a-Judge — https://arxiv.org/abs/2306.05685 (v4)
- locator: Table 2, p. 5; agreement metric Sec. 4.2 p. 7
- asset: assets/llm-judge-position-bias.png (PDF page 5 clip at 250 dpi). Transcribed: Claude-v1 default consistency 23.8%, biased toward first 75.0%; rename 56.2%/11.2%; GPT-3.5 default 46.2%/50.0%; rename 51.2%/38.8%; GPT-4 default 65.0%/30.0%; rename 66.2%/28.7%. Agreement: GPT-4 vs humans 85% (no ties), human–human 81%.
- inspected: opened full size; caption and all rows/columns inside crop
- notice: Swapping answer order changed even the best judge's verdict in about a third of cases; yet the same judge agreed with expert humans 85% of the time on real comparisons.
- limits: Near-identical answer pairs (hard case); 2023 models; pairwise preference, not support pass/fail.
- rights: arXiv non-exclusive distribution license; rights unstated for reuse

### E4: Failure breakdown for a support agent
- claim: C8 (support), C7 (context)
- type: figure+metric
- source: τ-bench — https://arxiv.org/abs/2406.12045 (v1)
- locator: Figure "Breakdown of 36 failed gpt-4o FC agent trajectories in retail" (figs/breakdown2.pdf); Failure breakdown paragraph
- asset: assets/tau-bench-failure-breakdown.png (rendered from vector PDF at 150 dpi). Values: wrong argument 33.3%, wrong decision 25.0%, wrong info 22.2%, partially resolve 19.4%; 115 trajectories, 40 failed, 4 of those due to task typo/ambiguity.
- inspected: opened full size; all four labels and percentages legible
- notice: Reading failures sorts them into a few fixable kinds; four failures turned out to be the test's fault.
- limits: One model, one domain, 36 failures.
- rights: CC BY 4.0

### E5: Code assertion example
- claim: C3 (support)
- type: quote
- source: Your AI Product Needs Evals — https://hamel.dev/blog/posts/evals/
- locator: Level 1: Unit Tests
- asset: "We use a simple regex to assert that the LLM response doesn't include UUIDs."
- inspected: not applicable
- notice: A cheap deterministic check guarding a rule stated in the prompt.
- limits: Single product example.
- rights: rights unstated (short quotation)

### E6: Start-small guidance
- claim: C7 (support)
- type: quote
- source: Demystifying evals for AI agents
- locator: Step 0. Start early
- asset: "20-50 simple tasks drawn from real failures is a great start."
- inspected: not applicable
- notice: Scale of a first suite.
- limits: Rule of thumb; small sets only detect large effects (the post says so).
- rights: rights unstated (short quotation)

## Omitted candidates
- Anthropic pass@k vs pass^k illustrative chart: superseded by measured τ-bench figure (E2).
- Anthropic Swiss-cheese and process diagrams: restate prose.
- Hamel spreadsheet screenshots of judge alignment: rights unstated and E3 + prose cover the point.
- Zheng et al. Table 3 verbosity attack: used as metric in prose (GPT-4 8.7%, others 91.3%), not embedded.
