# Evidence records

### E1: Components of an agent eval
- claim: C2 (support)
- type: figure
- source: Demystifying evals for AI agents — https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- locator: section "The structure of an evaluation", figure captioned "Components of evaluations for agents."
- asset: assets/anthropic-eval-components-web.png (1800px web copy); full resolution assets/anthropic-eval-components.png (4584×2580), original from www-cdn.anthropic.com/images/4zrzovbb/website/0205b36f9639fc27f2f6566f73cb56b06f59d555-4584x2580.png
- inspected: opened downscaled copy; all boxes, grader chips, legend visible and legible
- notice: A task bundles inputs, success criteria and several graders; each task is run as several trials; graders score both the transcript and the final environment state.
- limits: Example task is a coding fix, not support; illustration of vocabulary, not data.
- rights: rights unstated (attribute Anthropic)

### E2: Support-agent setup graded by end state
- claim: C5 (support), C2 (context)
- type: figure
- source: τ-bench — https://arxiv.org/abs/2406.12045 (v1)
- locator: Figure 1 (teaser), figs/teaser.pdf from arXiv e-print source
- asset: assets/taubench-teaser-web.png (2000px), full assets/taubench-teaser.png (rendered at 300 dpi)
- inspected: opened at web size; both panels, all text legible
- notice: The agent has tools, a written policy, and a simulated customer. The right panel shows the agent refusing a disallowed change and offering cancel-and-rebook; the database write at the end is what gets graded.
- limits: Simulated user; airline domain; 2024 setup.
- rights: CC BY 4.0 (arXiv listing)

### E3: Consistency collapses with repeated trials
- claim: C5 (support), C1 (support)
- type: figure+metric
- source: τ-bench — https://arxiv.org/abs/2406.12045 (v1)
- locator: Figure "pass^k (--) and pass@k (..) in retail" (figs/passatk.pdf), §5 "Agent consistency via pass^k"
- asset: assets/taubench-passatk.png (1500×750 at 300 dpi); metric: gpt-4o function-calling agent, retail domain, pass^1 61.2% (Table 1), pass^8 < 25% (§5 text, abstract)
- inspected: opened at full size; axes, legend, all five model lines visible; y axis is percentage (unlabeled in source)
- notice: Solid lines (all k tries succeed) fall steeply as k grows while dotted lines (at least one try succeeds) rise; average success hides how often the same customer request fails on a rerun.
- limits: mid-2024 models; y-axis unlabeled in original; pass^k assumes i.i.d. trials of same task.
- rights: CC BY 4.0

### E4: What failed, by type
- claim: C3 (support), C5 (context)
- type: figure+metric
- source: τ-bench — https://arxiv.org/abs/2406.12045 (v1)
- locator: Figure "Breakdown of 36 failed gpt-4o FC agent trajectories in retail" (figs/breakdown2.pdf), §5 Failure breakdown
- asset: assets/taubench-breakdown.png (1000px web copy of 300 dpi render); values wrong argument 33.3%, wrong decision 25.0%, wrong info 22.2%, partially resolve 19.4% of 36 agent failures (from 115 trajectories, 40 failures, 4 attributed to task typos/ambiguity)
- inspected: opened at full render; all four labels and percentages visible
- notice: Reading failed transcripts by hand sorts errors into a few named kinds; each kind suggests a different grader (argument checks, policy checks, information-completeness checks).
- limits: one model, one domain, one trial per task.
- rights: CC BY 4.0

### E5: Position bias in LLM judges
- claim: C4 (support)
- type: table
- source: Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena — https://arxiv.org/abs/2306.05685 (v4)
- locator: Table 2, page 5
- asset: assets/zheng-table2-position-bias.png (rendered at 250 dpi, cropped). Values: Claude-v1 default consistency 23.8%, biased first 75.0%; GPT-3.5 default 46.2%, 50.0%; GPT-4 default 65.0%, 30.0%; rename 66.2%, 28.7%
- inspected: opened full crop; caption and all rows visible; neighbouring Table 4 caption excluded
- notice: Swapping only the order of two answers changed the verdict in about a third of GPT-4's cases and most of Claude-v1's.
- limits: near-identical answer pairs by design; 2023 models.
- rights: rights unstated (arXiv non-exclusive license)

### E6: Judge–human agreement
- claim: C4 (qualify)
- type: metric+quote
- source: Zheng et al. — https://arxiv.org/abs/2306.05685 (v4)
- locator: §4.2, Table 5 setup S2
- asset: GPT-4 pairwise vs human experts 85% agreement (non-tie votes, MT-bench, 859 votes) vs human–human 81% (479 votes); random baseline 50%
- inspected: not applicable (checked against extracted PDF text)
- notice: A good judge can be about as consistent with experts as experts are with each other — on general preference questions.
- limits: excludes ties and inconsistent votes; general chat, not company policy.
- rights: rights unstated

### E7: Criteria drift
- claim: C3 (support), C4 (context)
- type: quote
- source: Who Validates the Validators? — https://arxiv.org/abs/2404.12272 (v1)
- locator: abstract
- asset: "users need criteria to grade outputs, but grading outputs helps users define criteria"
- inspected: not applicable
- notice: You cannot write the whole rubric first; reading outputs is how the rubric gets written.
- limits: n=9 qualitative study.
- rights: quote, short

### E8: Starting size and sources
- claim: C3 (support), C6 (support)
- type: metric
- source: Demystifying evals for AI agents
- locator: "Getting started" / step 0–1
- asset: 20–50 simple tasks drawn from real failures; convert bug tracker and support-queue issues into test cases; capability evals start low, regression evals near 100%
- inspected: not applicable
- notice: Small beginnings suffice early because changes have large effects.
- limits: recommendation, not measured.
- rights: paraphrase

### E9: Refund-agent graders
- claim: C5 (support)
- type: metric (example spec)
- source: Demystifying evals for AI agents
- locator: conversational agent example
- asset: LLM rubric (empathy, clear explanation, grounded in policy tool results); state check (ticket resolved, refund processed); tool calls (verify identity, refund ≤ 100, send confirmation); transcript constraint (≤ 10 turns)
- inspected: not applicable (fetch summary)
- notice: One support task combines code checks and a model rubric.
- limits: illustrative; read via fetch summary.
- rights: paraphrase

## Omitted
- Anthropic pass@k vs pass^k chart: illustrative curve only; τ-bench's measured chart used instead.
- Husain's spreadsheet/Metabase screenshots: not extracted; text description sufficient and images uncaptioned.
- Zheng Table 3 (verbosity 91.3% failure for Claude-v1 and GPT-3.5, 8.7% for GPT-4 on 23 answers): used as a metric in text, not embedded.
