# Evidence records

### E1: τ-bench setup and example support conversation
- claim: C6 (support), C2 (context)
- type: figure
- source: τ-bench — https://arxiv.org/abs/2406.12045 (v1)
- locator: Figure 1 (teaser), e-print figs/teaser.pdf
- asset: assets/tau-bench-fig1-setup.png (rendered from authors' vector PDF at 3x, 3923x1905)
- inspected: opened at full size; both panels, tool names, policy text, and trajectory visible
- notice: the agent sees tools and a written policy; a simulated user has hidden instructions; the correct outcome is a specific database write (cancel), so grading is a state comparison.
- limits: airline domain; simplified compared with real support systems.
- rights: CC BY 4.0

### E2: pass^k falls as trials increase
- claim: C6 (support), C1 (support)
- type: figure+metric
- source: τ-bench — https://arxiv.org/abs/2406.12045 (v1)
- locator: figure "pass^k (–) and pass@k (..) in τ-retail", Sec. 5.1; e-print figs/passatk.pdf
- asset: assets/tau-bench-fig4-passk.png; metric gpt-4o function-calling pass^1 ≈61% retail, pass^8 <25% retail; airline pass^1 35.2%
- inspected: opened at full size; legend, axes, all five model curves visible
- notice: solid lines (all k trials succeed) fall steeply while dotted lines (at least one succeeds) rise; average success hides inconsistency.
- limits: 2024 models; agent temperature 0, user simulator temperature 1.0; some original tasks later found defective.
- rights: CC BY 4.0

### E3: Failure categories from manual review
- claim: C3 (support), C6 (context)
- type: figure+metric
- source: τ-bench — https://arxiv.org/abs/2406.12045 (v1)
- locator: figure "Breakdown of 36 failed gpt-4o FC agent trajectories in τ-retail", Sec. 5.2; e-print figs/breakdown2.pdf
- asset: assets/tau-bench-fig5-failures.png; wrong argument 33.3%, wrong decision 25.0%, wrong info 22.2%, partially resolve 19.4% of 36 failures
- inspected: opened at full size; all four labels and percentages visible
- notice: reading failed conversations and grouping them yields a short list of named failure types to target.
- limits: 36 failures from one model, one domain; 4 further failures were benchmark defects, fixed by authors.
- rights: CC BY 4.0

### E4: Position bias example
- claim: C5 (support)
- type: figure
- source: Judging LLM-as-a-Judge — https://arxiv.org/abs/2306.05685 (v4)
- locator: appendix figure (position bias example), e-print figures/position_bias.pdf
- asset: assets/mt-bench-position-bias-example.png
- inspected: opened at full size; both answers and both judgments legible
- notice: the same GPT-4 judge prefers whichever answer comes first.
- limits: one hand-picked example; 2023 model.
- rights: rights unstated (arXiv non-exclusive distribution license); embedded with attribution

### E5: Judge consistency and agreement numbers
- claim: C5 (support/qualify)
- type: metric
- source: Judging LLM-as-a-Judge — https://arxiv.org/abs/2306.05685 (v4)
- locator: Table "Position bias of different LLM judges"; Sec. 3.4 text; Table "Agreement between two types of judges on MT-bench" (first turn)
- asset: GPT-4 consistent when order swapped 65.0% (default prompt), 77.5% with few-shot; GPT-4 pairwise vs human agreement 85% on non-tie votes (859 votes) vs human–human 81% (479 votes); 66% vs 63% when ties and inconsistent votes are counted (random baseline 33%)
- inspected: values read from LaTeX table source
- notice: a judge can match humans about as well as humans match each other, yet flip a third of the time when order changes.
- limits: general chat questions; 2023 judges.
- rights: rights unstated

### E6: Criteria drift quote
- claim: C3 (support)
- type: quote
- source: Who Validates the Validators? — https://arxiv.org/abs/2404.12272 (v1)
- locator: abstract
- asset: "users need criteria to grade outputs, but grading outputs helps users define criteria."
- inspected: not applicable
- notice: you cannot write a complete rubric before looking at outputs.
- limits: 9-participant qualitative study.
- rights: CC BY 4.0

### E7: Standard error formula
- claim: C7 (support)
- type: quote+metric
- source: Adding Error Bars to Evals — https://arxiv.org/abs/2411.00640 (v1)
- locator: Sec. 2.1 Eq. (Bernoulli standard error) and Sec. 1 recommendation list
- asset: SE = sqrt(p̄(1−p̄)/n) for pass/fail scores; recommendation to use question-level paired differences when comparing two models
- inspected: read from LaTeX source
- notice: the uncertainty of a pass rate shrinks with the square root of the number of cases; used by the calculator in the report (type generated for the calculator itself).
- limits: assumes independent cases.
- rights: rights unstated (formula is standard statistics)

### E8: Support tone eval example
- claim: C2 (support)
- type: quote
- source: Define success criteria and build evaluations — https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
- locator: "Prioritize volume over quality" principle; tone-and-style example
- asset: "More questions with slightly lower signal automated grading is better than fewer questions with high-quality human hand-graded evals."
- inspected: not applicable
- notice: vendor practice favors many automatically graded cases.
- limits: advice, not tested; tension with Husain's emphasis on human review early — both reported.
- rights: rights unstated (quoted briefly)

### E9 (generated): eval loop diagram, Python harness sketch, error-bar calculator
- claim: C2, C3, C7
- type: generated
- notice: synthesis of sources above; not observations.

Claims lacking evidence: none fully; C4 has only practitioner advice (no exhibit extracted).
Omitted candidates: MT-bench verbosity-bias figure (redundant with E4); τ-bench policy-ablation table (beyond reader's need); Rechat screenshots (not extracted).
