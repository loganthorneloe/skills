# Source audit records

Claims
- C1: AI applications need evals because model outputs vary between runs and changes (prompts, models, tools) can silently regress behavior; manual checking and public benchmarks do not tell you how your product performs.
- C2: An eval is a task (input + success criteria), one or more trials, a grader, and a recorded transcript/outcome, aggregated over a suite.
- C3: Graders come in three kinds (code, model/LLM-judge, human) with distinct trade-offs; prefer code where possible.
- C4: Start with error analysis: read real traces, write open notes, group into a failure taxonomy, count; then build evals for the important failures.
- C5: Binary pass/fail judgments are usually preferable to 1–5 scales for product evals.
- C6: LLM judges can approximate human judgment but must be validated against human labels; they have measurable biases.
- C7: For a customer-support agent, check end-state outcomes (database/ticket state) and consistency across repeated trials (pass^k), often using a simulated user.
- C8: Support agents fail in recognizable categories (wrong tool arguments, wrong information, wrong policy decision, partial resolution of compound requests).
- C9: Small eval sets are a fine start but scores carry sampling error; differences must be judged against error bars, ideally with paired comparisons.
- C10: Capability evals vs regression evals; the suite grows from observed failures and should be maintained.
- C11: Automated evals complement, not replace, production monitoring, user feedback, A/B tests and human review.

### Demystifying evals for AI agents
- url: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents; text read from: same
- byline: Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares, and Jiri De Jonghe · engineering blog post · Anthropic · January 9, 2026
- verdicts: C1 pass; C2 pass; C3 pass; C6 conditional (states calibration is needed; no measurements of its own); C7 pass (support example is illustrative, labeled "theoretical"); C9 conditional (20–50 tasks is practitioner advice, not a statistical result); C10 pass; C11 pass
- use: "The structure of an evaluation" definitions; grader table; capability vs regression; conversational agents section and support YAML; pass@k vs pass^k; roadmap steps 0–8; methods comparison table; figures "Single-turn vs agent evaluations" and "Components of evaluations for agents".
- credibility: Written by the engineering team of a model developer that builds and runs evals for its own agent products (Claude Code, Claude for Chrome) and with named customers; firsthand practice.
- contribution: Vocabulary (task, trial, grader, transcript, outcome, suite, harness), trade-offs of grader types, practical roadmap, and worked support-agent example.
- limits: Vendor practitioner guidance, not controlled research; anecdotes (CORE-Bench 42%→95%) are self-reported. Examples are explicitly "theoretical". Model vendor has an interest in promoting agent adoption.
- read: full · accessed 2026-11-03

### AI Evals: Everything You Need to Know (AI Evals FAQ)
- url: https://hamel.dev/blog/posts/evals-faq/; text read from: same
- byline: Hamel Husain and Shreya Shankar · practitioner FAQ / blog · hamel.dev · September 18, 2026 (modified September 21, 2026)
- verdicts: C1 pass (product evals vs benchmarks); C4 pass (as recommended practice); C5 conditional (authors label these "sharp opinions", no controlled comparison); C6 pass (validation method: train/dev/test split, TPR/TNR); C9 conditional (example counts are rules of thumb); C10 pass
- use: "What are AI Evals?"; "What's a minimum viable evaluation setup?"; "Why is error analysis so important"; "Do I need a reference answer or rubric"; "Should I record problems that aren't the model's fault?"; "How many examples do I need"; "Why binary"; "How do I combine evals"; "How do I know if I can trust my automated eval?"
- credibility: Husain is a consultant who has built evals for many AI products; Shankar is a researcher on LLM evaluation (her criteria-drift research is linked from the FAQ; publication details unverified). They report teaching the method to 5,000+ engineers and PMs.
- contribution: A concrete, beginner-ready process: error analysis (open coding, axial coding, saturation), binary evaluators, judge validation against human labels.
- limits: Opinionated practice guidance; numbers (30 traces, 100–200 labels per judge) are heuristics. The authors sell a course on this topic (conflict of interest noted). Living document, version read Nov 3, 2026.
- read: partial (fundamentals, error analysis, evaluation design, judge trust sections read; tooling, RAG, agent-specific sections skimmed by heading only)

### τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains
- url: https://arxiv.org/abs/2406.12045; text read from: https://arxiv.org/html/2406.12045v1 and e-print source (figure PDFs)
- byline: Shunyu Yao, Noah Shinn, Pedram Razavi, and Karthik Narasimhan · research preprint · arXiv (Sierra) · June 17, 2024
- verdicts: C7 pass; C8 pass (for the τ-retail setup and gpt-4o agent); C1 conditional (shows inconsistency across trials in 2024 models; does not measure current models)
- use: §3 reward definition (database end-state + required outputs); pass^k definition; Table 2; Figure 4 (pass^k vs pass@k); §5.2 failure breakdown and Figure 5; §6 limitations of simulated users.
- credibility: Authors built the benchmark at Sierra, a customer-service-agent company, and report their method, tasks and code publicly; the benchmark is widely used (Anthropic article cites it).
- contribution: Shows how to grade a support conversation objectively by comparing final database state to an annotated goal state, and that success on repeated trials falls sharply (gpt-4o retail pass^1 ≈61%, pass^8 <25%).
- limits: 2024 models; scores are historical. Original task files later declared outdated by the maintainers (successors τ²/τ³-bench fixed task errors) — use for method and shape of the result, not current numbers. Simulated users (gpt-4) have their own errors. Reward r=1 is "necessary but not sufficient" (e.g., can miss missing user confirmation). Text says "wrong info ~55%" which conflicts with Figure 5 (22.2%); the 55% appears to be wrong argument + wrong info combined (33.3+22.2) — rely on the figure. Retraction search: none found; maintenance note found.
- read: full main text (§1–6); appendix skimmed · version v1 · CC BY 4.0

### Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena
- url: https://arxiv.org/abs/2306.05685; text read from: https://arxiv.org/html/2306.05685v4
- byline: Lianmin Zheng, Wei-Lin Chiang, and colleagues · conference paper · NeurIPS 2023 Datasets and Benchmarks Track · June 2023 (v4 December 2023)
- verdicts: C6 conditional (historical models: GPT-4, GPT-3.5, Claude-v1 of 2023; general-chat preference, not support-policy correctness)
- use: §3.3 position bias (Table 2), verbosity bias ("repetitive list" attack, Table 3), §3.4 swap-order mitigation, §4.2 agreement (GPT-4 vs experts 85% vs human–human 81%, setup S2 no ties).
- credibility: The LMSYS team that ran Chatbot Arena; collected 3K expert votes and 30K crowd conversations and measured judge-human agreement directly.
- contribution: Quantifies that a strong LLM judge can agree with humans about as often as humans agree with each other, and that judges show position and verbosity biases.
- limits: Judges and models are 2023 versions; agreement measured on pairwise chat preferences excluding ties. Position-bias test used near-identical answer pairs (deliberately hard). Later work (Shi et al., "Judging the Judges", IJCNLP-AACL 2025; seen only via search listing) reports position bias varies by judge and task — consistent, not contradicting. License: arXiv non-exclusive (no reuse grant) → table rebuilt with attribution, rights unstated.
- read: partial (abstract, §1, §3.3–3.4, §4.1–4.2 read; appendix not read) · version v4

### Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations
- url: https://arxiv.org/abs/2411.00640; text read from: https://arxiv.org/html/2411.00640v1
- byline: Evan Miller · research preprint · arXiv (Anthropic) · November 1, 2024
- verdicts: C9 pass
- use: §1 recommendations list; §2.1 standard error formulas (Bernoulli SE = sqrt(p(1−p)/n)), CI = mean ± 1.96 SE; §4.2 paired analysis recommendation.
- credibility: Statistician writing at a model developer (prior A/B-testing tool authorship: unverified); derivations follow standard sampling theory.
- contribution: Treats an eval as a sample from a larger population of possible questions, so scores have standard errors; recommends paired comparisons and power analysis.
- limits: Written for benchmark-scale evals ("large number of questions"); normal-approximation intervals are poor for very small n — the report's calculator uses the Wilson interval (textbook) instead and says so. Search found no erratum.
- read: partial (§1, §2.1, §4.1–4.2, conclusion read; clustered SE and power-analysis derivations skimmed)

Gaps
- C5: only conditional sources — binary-vs-Likert recommendation rests on practitioner opinion, no controlled study read.
- C9: sample-size starting points (20–50 tasks) are practitioner advice; statistics source supports only the error-bar reasoning.
- C6: judge-agreement numbers are from 2023 models on general chat, not support conversations — presented historically.
