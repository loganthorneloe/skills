# Source audit records

Claims
- C1: LLM application outputs vary and fail in product-specific ways, so ad hoc "vibe checks" and generic benchmarks are insufficient; teams need product-specific evals to improve systematically.
- C2: An eval has a fixed set of inputs, runs the application, grades each output (code check, human, or LLM judge), and aggregates scores; evals should mirror the real task distribution and include edge cases.
- C3: Useful criteria come from looking at real outputs (error analysis); criteria shift as people grade (criteria drift).
- C4: Binary pass/fail judgments with written critiques are preferred over Likert scales by experienced practitioners (practitioner recommendation, not an experimental result).
- C5: LLM judges can approximate human judgments but have measurable biases (position, verbosity, self-enhancement) and must be validated against human labels.
- C6: Customer-support agents can be evaluated by simulating users, giving tools and a policy, and checking the final database state; such agents fail often and inconsistently across repeated trials (pass^k).
- C7: An eval score is an estimate with statistical noise; standard errors depend on number of cases, and paired comparisons reduce noise.

### Your AI Product Needs Evals
- url: https://hamel.dev/blog/posts/evals/; text read from: same (via fetch summary)
- byline: Hamel Husain · blog post · hamel.dev · 29 March 2024
- verdicts: C1 conditional (practitioner experience, one case study); C2 conditional (practitioner framing); C5 conditional (practice advice; corroborated by Zheng et al.)
- use: three levels (assertions, human/model eval, A/B), Rechat "Lucy" case, judge alignment advice
- credibility: Husain is an ML engineer and consultant who describes his own work with Rechat; firsthand practitioner account.
- contribution: explains why prompt-tweaking plateaus without evals and lays out a cheap-to-expensive hierarchy of tests.
- limits: anecdotal, single main case; consultant with commercial interest in eval training; no quantitative evidence.
- read: partial (fetch-tool summary of full post with quoted sentences)

### A Field Guide to Rapidly Improving AI Products
- url: https://hamel.dev/blog/posts/field-guide/; text read from: same (via fetch summary)
- byline: Hamel Husain · blog post · hamel.dev · 24 March 2025
- verdicts: C3 conditional (practitioner method; the experimental support comes from Shankar et al.); C4 conditional (recommendation, not tested)
- use: error analysis section, binary vs Likert, synthetic inputs advice
- credibility: same practitioner as above, drawing on work with 30+ companies (self-reported, unverified).
- contribution: bottom-up error analysis—write notes on real conversations, group them into failure categories, count them.
- limits: the 33%→95% date-handling example is unverified anecdote and not used in the report; self-reported scale.
- read: partial (fetch-tool summary)

### Define success criteria and build evaluations
- url: https://platform.claude.com/docs/en/test-and-evaluate/develop-tests; text read from: same
- byline: Anthropic · product documentation · Claude Developer Platform docs · undated, accessed 3 Nov 2026
- verdicts: C2 pass; C5 conditional (only the advice to use a different grader model; no evidence)
- use: eval design principles (task-specific, automate, volume over quality); customer-support tone example; grading methods
- credibility: vendor guidance from a model provider; describes recommended practice, not experiments.
- contribution: concrete structure of an eval and a support-tone example graded by a model on a 1–5 scale.
- limits: vendor documentation; "volume over quality" is advice; the tone example uses a Likert scale, which contrasts with C4's practitioner advice. Only first 100k characters read.
- read: partial (first ~2/3 of page via fetch summary)

### Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences
- url: https://arxiv.org/abs/2404.12272; text read from: arXiv HTML v1
- byline: Shreya Shankar, J.D. Zamfirescu-Pereira, and colleagues · conference paper · UIST 2024 (ACM) · April 2024
- verdicts: C3 pass (narrowed to the qualitative finding); C5 conditional (supports need to align judges with human grades)
- use: criteria drift finding, abstract quote, qualitative study section
- credibility: HCI/database researchers at UC Berkeley who built and studied an eval tool with practitioners.
- contribution: nine practitioners using EvalGen changed and added criteria as they graded outputs.
- limits: small qualitative sample (9 experienced practitioners), one task in the user study; offline eval of two pipelines.
- read: partial (fetch summary of first 100k characters; abstract read directly) · version v1 · CC BY 4.0

### Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena
- url: https://arxiv.org/abs/2306.05685; text read from: arXiv e-print LaTeX source v4
- byline: Lianmin Zheng, Wei-Lin Chiang, and colleagues · conference paper · NeurIPS 2023 Datasets and Benchmarks · June 2023 (v4 Dec 2023)
- verdicts: C5 pass
- use: Sec. on limitations (position bias table, consistency 65% for GPT-4 default prompt, 66.2% rename), agreement table on MT-bench (G4-Pair vs human 85% non-tie; human-human 81%), position-bias example figure (appendix)
- credibility: LMSYS team that ran Chatbot Arena and collected expert human votes; primary data.
- contribution: quantifies how often LLM judges agree with humans and how they flip when answer order is swapped.
- limits: judges were 2023 models (GPT-4, Claude-v1, GPT-3.5); agreement 85% holds only for non-tie votes (S2), drops to 66% when ties/inconsistent votes are counted (S1, random 33%); general chat questions, not support. Later work (Shi et al., arXiv 2406.07791) confirms position bias is systematic.
- read: partial (judge-limitation and agreement sections, tables) · version v4 · arXiv non-exclusive license only

### τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains
- url: https://arxiv.org/abs/2406.12045; text read from: arXiv e-print LaTeX source v1
- byline: Shunyu Yao, Noah Shinn, Pedram Razavi, and Karthik Narasimhan · preprint · arXiv (Sierra) · June 2024 (NeurIPS-format; venue not verified)
- verdicts: C6 pass (historical numbers); C1 conditional (inconsistency across trials as evidence of variability); C3 conditional (its manual failure breakdown illustrates error analysis)
- use: Fig. 1 setup, pass^k definition (Sec. 3), pass^k figure, failure breakdown figure, Sec. 5 results
- credibility: authors at Sierra, a company that builds customer-service agents (affiliation from paper header); they built the benchmark and ran every model on it.
- contribution: simulated users + tools + policy; grading by comparing final database state to an annotated goal; gpt-4o ~61% retail pass^1, ~35% airline, pass^8 <25% retail.
- limits: 2024 models; simulated users (LM at temperature 1.0); later audits (HAL leaderboard, tau2-bench-verified) found defects in some original tasks, so absolute numbers are noisy; authors have commercial interest in the domain.
- read: partial (intro, benchmark construction, experiments, analysis; appendix skimmed) · version v1 · CC BY 4.0

### Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations
- url: https://arxiv.org/abs/2411.00640; text read from: arXiv e-print LaTeX source v1
- byline: Evan Miller · preprint · arXiv (Anthropic) · November 2024
- verdicts: C7 pass
- use: recommendation list (Sec. 1), Eq. for standard error and Bernoulli case (Sec. 2.1), paired analysis (Sec. 4.2)
- credibility: author affiliated with Anthropic (paper header); applies standard sampling statistics, which can be checked directly.
- contribution: treat eval questions as a sample; report standard errors; compare models with paired differences; plan sample sizes.
- limits: assumes independent questions unless clustered; preprint; formulas are textbook statistics so low risk.
- read: partial (intro, Sec. 2.1, variance reduction, paired analysis, conclusion) · version v1

Gaps
- C4: only conditional sources — binary-vs-Likert is practitioner advice; the vendor doc uses a 1–5 scale in its support example.
- C6: only historical results (2024 models); task defects later found in parts of the original benchmark.
