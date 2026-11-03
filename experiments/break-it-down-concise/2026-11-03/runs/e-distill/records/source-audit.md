# Source audit records

Claims
- C1: LLM application outputs vary between runs and prompt/model changes can fix one behavior while breaking another; informal "vibe checks" do not reveal this at scale, which is why evals are needed.
- C2: An eval is a set of tasks (input + success criteria), run for one or more trials, scored by graders (code-based, model-based, human), with results aggregated into metrics.
- C3: A practical start is to read real transcripts/traces, name the failures, and turn roughly 20–50 real failures and common tasks into eval tasks; criteria emerge from looking at outputs.
- C4: LLM-as-judge graders can approach human agreement but have measurable biases, so they must be checked against human labels.
- C5: For customer-support agents, grade the end state (what actually happened in the system) and policy adherence, and measure consistency across repeated trials (pass^k); per-trial averages hide inconsistency.
- C6: Capability evals (low pass rate, hill to climb) differ from regression evals (near 100%, run on every change); evals sit alongside production monitoring, human review and A/B tests.

### Demystifying evals for AI agents
- url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents; text read from: same (via fetch-tool summary of full page; figures downloaded from www-cdn.anthropic.com)
- byline: Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares, and Jiri De Jonghe · engineering blog post · Anthropic · January 9, 2026
- verdicts: C1 pass; C2 pass; C3 pass; C4 conditional (states model graders need human calibration; no measurements — pair with Zheng et al.); C5 pass (refund-agent example, pass^k definition); C6 pass
- use: definitions section; "Components of evaluations for agents" figure; grader-types table; capability vs regression; pass@k vs pass^k; getting-started steps (20–50 tasks from real failures); conversational/support example; "check the transcripts"
- credibility: Written by the engineering team of a model developer that builds and runs agent evals internally; firsthand practitioner account.
- contribution: Vocabulary and workflow for building evals (task, trial, grader, transcript, outcome, harness, suite) and practical rules (grade outcomes not paths, balanced cases, reference solutions, read transcripts).
- limits: Practitioner guidance, not a controlled study. Vendor with interest in agent adoption. The pass@k/pass^k chart is an illustrative curve, not measured data. Read through a fetch-tool summary, so counts as partial; quotes and numbers taken from it were cross-checked against the summary only (unverified verbatim for anything not quoted in records).
- read: partial (fetch-tool summary of whole page plus direct inspection of downloaded figures) · undated revisions unknown · accessed 2026-11-03

### Your AI Product Needs Evals
- url: https://hamel.dev/blog/posts/evals/; text read from: same (fetch-tool summary)
- byline: Hamel Husain · blog post / case study · hamel.dev · March 29, 2024
- verdicts: C1 pass; C3 pass; C4 pass (process for aligning judge with human labels); C6 conditional (three levels with cadence; practitioner opinion)
- use: Rechat/Lucy case study motivation; three levels (unit tests, human & model eval, A/B tests); "looking at your traces"; LLM-as-judge alignment via spreadsheet, 25–50 human labels at a time; precision/recall warning
- credibility: Consultant who built the eval system for a deployed product (Rechat's Lucy assistant) and describes it firsthand; previously led CodeSearchNet work (self-reported).
- contribution: Concrete account of how a real conversational assistant stalled under prompt-only iteration ("whack-a-mole") and how assertions, trace review and judge alignment fixed the process.
- limits: Single case study, no quantitative results reported; opinionated. Tooling mentions dated (2024).
- read: partial (fetch-tool summary of full post) · accessed 2026-11-03

### τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains
- url: https://arxiv.org/abs/2406.12045; text read from: arXiv e-print LaTeX source (main.tex) and figure PDFs
- byline: Shunyu Yao, Noah Shinn, and colleagues · research preprint · arXiv (Sierra) · June 17, 2024
- verdicts: C1 pass (inconsistency across trials measured); C2 conditional (one benchmark's design); C5 pass; C3 conditional (manual failure breakdown illustrates error analysis)
- use: §1 design (simulated user, policy, compare final database to goal state); pass^k definition (§ metric); Table 1 pass^1; Figure "pass^k (--) and pass@k (..) in retail"; failure breakdown of 36 gpt-4o trajectories; retail/airline numbers
- credibility: Authors built the benchmark, its databases and user simulator, and ran the experiments; Yao is an established agent researcher (ReAct). Primary research.
- contribution: Shows a customer-service style benchmark graded by final database state; best 2024 model (gpt-4o function calling) succeeds on 61.2% retail / 35.2% airline per trial, and pass^8 in retail falls below 25%. Manual failure analysis: wrong argument 33.3%, wrong decision 25.0%, wrong info 22.2%, partial resolve 19.4% of 36 agent failures.
- limits: Models are from mid-2024 and later models score higher, so the absolute numbers are historical; the reliability pattern (pass^k falling with k) is the enduring point. User simulated by an LLM. 4 of 40 sampled failures came from task typos/ambiguity, showing evals themselves contain errors. Targeted search for errata/retraction found none specific. Only v1 on arXiv. License CC BY 4.0.
- read: partial (intro, metric, experiments, failure analysis in main.tex; appendix not read) · version v1

### Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena
- url: https://arxiv.org/abs/2306.05685; text read from: arXiv PDF v4 (text extracted)
- byline: Lianmin Zheng, Wei-Lin Chiang, and colleagues · conference paper (Datasets and Benchmarks track) · NeurIPS 2023 (per arXiv; venue not verified in this read) · June 2023 (v4 December 24, 2023)
- verdicts: C4 pass; C1 fail (not about applications)
- use: §3 limitations (Table 2 position bias, Table 3 verbosity attack, Table 4 math); §4.2 agreement (Table 5: GPT-4 vs humans 85% vs human–human 81%, non-tie setup S2)
- credibility: Authors ran controlled experiments with expert human votes on MT-bench and crowd votes on Chatbot Arena, which they operate; primary research.
- contribution: Strong LLM judges can agree with human experts about as often as experts agree with each other on pairwise preferences, yet judges flip verdicts when answer order swaps (GPT-4 consistent in 65% of the constructed near-identical pairs), favor padded answers (Claude-v1 and GPT-3.5 fooled 91.3% on 23 answers), and mis-grade math.
- limits: 2023 judge models; bias magnitudes for current models will differ. Position test uses deliberately near-identical answers, which exaggerates inconsistency. Agreement measured on general chat preference, not domain-specific support policies. Spot-checked 85%/81% and Table 2 values against the PDF text. arXiv license is non-exclusive distribution only, so rights for figure reuse are unstated.
- read: partial (abstract, §3, §4 read; appendix skimmed) · version v4

### Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences
- url: https://arxiv.org/abs/2404.12272; text read from: arXiv HTML v1
- byline: Shreya Shankar, J.D. Zamfirescu-Pereira, and colleagues · research preprint (user study) · arXiv (header names UIST 2024; publication not verified) · April 18, 2024
- verdicts: C3 conditional (qualitative, n=9); C4 conditional (supports need to align judges with humans)
- use: abstract and findings on criteria drift
- credibility: HCI and data-systems researchers at UC Berkeley who built the EvalGen tool and observed nine industry practitioners using it.
- contribution: Observed that people define what "good" means partly by grading outputs ("criteria drift"), so criteria cannot be fully fixed before looking at outputs.
- limits: Small qualitative study of 9 practitioners; no effect sizes. Read only the abstract and study summary via fetch tool.
- read: partial (abstract, method summary) · version v1

## Gaps
- C1: only practitioner sources for the "changes break other behaviors" point (Husain, Anthropic); tau-bench supplies the measured run-to-run variation.
- C6: only practitioner sources (Anthropic, Husain) — framed as recommended practice, not measured effect.
- Current-model numbers: no current measured τ-bench results audited; report presents 2024 numbers historically.
