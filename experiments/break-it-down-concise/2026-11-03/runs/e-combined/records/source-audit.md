# Source audit records

Claims
- C1: Model-backed features vary run to run, and a prompt change that fixes one case can break others; without a repeatable test set a team cannot tell a regression from noise.
- C2: An eval is a set of tasks (input + success criteria), run as one or more trials, scored by graders, with results aggregated.
- C3: Graders come in three kinds (code, model, human) with distinct trade-offs; code checks are preferred where they fit.
- C4: LLM judges can agree with humans about as often as humans agree with each other (2023 study), but show measurable biases (position, verbosity) and must be checked against human labels.
- C5: Average success hides inconsistency; pass^k (all k trials succeed) measures reliability, and in τ-bench retail gpt-4o fell from >60% pass^1 to <25% pass^8.
- C6: For a support agent, grading the end state (database/outcome) rather than the exact path is objective and tolerant of varied conversations; quality dimensions need rubrics.
- C7: Start small (20–50 tasks from real failures), read transcripts, and expect the eval itself to have bugs.
- C8: In a customer-service benchmark, agent failures fall into recognizable categories (wrong arguments, wrong info, wrong decisions, partial resolution) that manual review can count.

### Demystifying evals for AI agents
- url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents; text read from: same (raw HTML via curl, converted to text)
- byline: Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares, and Jiri De Jonghe · engineering blog post · Anthropic · January 9, 2026
- verdicts: C1 pass; C2 pass; C3 pass; C4 conditional (supports "calibrate against humans" only, no measured agreement data); C5 conditional (definitions and illustrative arithmetic only; measured numbers come from τ-bench); C6 pass; C7 pass
- use: "The structure of an evaluation" (definitions of task, trial, grader, transcript, outcome; "Components of evaluations for agents" figure); "Why build evaluations?"; grader-type tables; conversational-agent YAML refund example; non-determinism section (pass@k, pass^k, 0.75^3 ≈ 42%); roadmap Steps 0–6 (20–50 tasks, real failures, unambiguous tasks, grade outcome not path, partial credit, read transcripts, CORE-Bench 42% grading-bug anecdote)
- credibility: Written by Anthropic engineers who build and evaluate agents in production (Claude Code, Claude.ai search) and with named customers; firsthand practitioner account.
- contribution: Vocabulary and a practical roadmap distilled from internal and customer practice, with concrete support-agent example.
- limits: Vendor practitioner guidance, not controlled research; the 20–50 figure is a rule of thumb; anecdotes (CORE-Bench, Descript, Bolt) are not independently verified; agent-focused, so some machinery exceeds a simple chat assistant's needs. Targeted search found no correction or rebuttal.
- read: full (all sections) · via curl of canonical page

### τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains
- url: https://arxiv.org/abs/2406.12045; text read from: arXiv e-print LaTeX source (main.tex) and figure PDFs
- byline: Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan · research paper (preprint; ICLR 2025 per proceedings listing) · arXiv / Sierra · June 2024
- verdicts: C1 pass (LM sampling alone produces enough variation to change outcomes on identical tasks); C5 pass; C6 pass; C8 conditional (one model, 36 failures, one domain)
- use: Introduction (evaluation compares end database state to annotated goal state); pass^k definition and unbiased estimator (Sec. 4/metric); Fig. "pass^k (--) and pass@k (..) in retail"; Key characteristics ("faithful rule-based evaluation", trade quantity for quality, cost ~$200 per trial pass); Failure breakdown (115 trajectories, 40 failed, 4 caused by task typos/ambiguity, 36 agent failures, figure breakdown2)
- credibility: Primary benchmark research from the team that built the simulated retail and airline environments; data, code, and method are described and released.
- contribution: Shows measured inconsistency of 2024 tool-calling agents on customer-service tasks and a reliability metric suited to customer-facing agents.
- limits: Only v1 on arXiv; models are 2024 generation (gpt-4o, claude-3-opus) and today's scores differ; simulated users, not real customers; the authors' own repository README (github.com/sierra-research/tau-bench, accessed 2026-11-03) warns the original airline and retail tasks are outdated and points to τ³-bench for fixed tasks; third-party work (τ²-bench-Verified) also reports incorrect or ambiguous tasks, so exact scores are approximate, though the authors already found 4 of 40 failures were task errors. Figure has no y-axis label; caption and text give it as success percentage.
- read: partial (abstract, intro, benchmark construction, key characteristics, metric, main results, failure analysis; appendix trajectories skimmed) · version v1 · via arXiv e-print source

### Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena
- url: https://arxiv.org/abs/2306.05685; text read from: arXiv PDF v4 and LaTeX source
- byline: Lianmin Zheng, Wei-Lin Chiang, and colleagues · research paper · NeurIPS 2023 Datasets and Benchmarks track (arXiv v4) · June 2023
- verdicts: C4 pass (as historical, 2023-model framing)
- use: Sec. 3.3 limitations (Table 2 position bias; Table 3 verbosity "repetitive list" attack: Claude-v1 91.3%, GPT-3.5 91.3%, GPT-4 8.7% failure on 23 answers); Sec. 4.2 agreement (GPT-4 vs expert humans 85% without ties; human–human 81%; ~3K expert votes on 80 MT-bench questions, 58 labelers)
- credibility: Primary experimental study with controlled expert votes and crowdsourced votes; authors built MT-bench and Chatbot Arena and measured judges directly.
- contribution: Quantifies both how well and how badly LLM judges work on open-ended answer comparison.
- limits: 2023 judge models; tasks are general chat questions, not support transcripts; agreement is on pairwise preferences, not pass/fail grading; the position test used deliberately near-identical answers, which the authors say is hard even for humans. Position bias later corroborated at larger scale by Shi et al., "Judging the Judges" (arXiv 2406.07791, ACL 2025) — found via targeted search, not audited in full.
- read: partial (intro, Sec. 3 judge limitations, Sec. 4 agreement setup and results) · version v4 · via arXiv

### Your AI Product Needs Evals
- url: https://hamel.dev/blog/posts/evals/; text read from: same
- byline: Hamel Husain · practitioner blog post · hamel.dev · March 29, 2024
- verdicts: C1 pass (case-study symptoms: whack-a-mole failures, "vibe checks"); C3 pass (assertion "unit tests" example); C4 pass (align judge with a human labeler, track agreement, prefer precision/recall under imbalance); C7 pass (read traces, binary good/bad labels, start simple)
- use: Case study (Lucy / Rechat symptoms); Level 1 unit tests (UUID regex assertion, scenario assertions, synthetic test cases); Level 2 trace review and judge alignment with a domain expert; note on agreement metric
- credibility: Firsthand account from a practitioner who built the evaluation system for a deployed assistant (Rechat's Lucy) and earlier led CodeSearchNet.
- contribution: Shows a concrete, low-tech eval workflow on a real conversational product.
- limits: Single case study, self-reported; author sells an evals course (disclosed in post), a commercial interest; tooling mentions dated to 2024. Targeted search found no critique or retraction.
- read: full

## Gaps
- C5: measured numbers come from 2024 models in simulation only; no source gives current production support-agent pass^k.
- C4: no audited source measures LLM-judge accuracy specifically on customer-support transcripts.
- C8: only conditional (single model, single domain, 36 failures).
