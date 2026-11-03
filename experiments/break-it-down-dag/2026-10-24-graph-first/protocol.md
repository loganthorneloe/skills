# DAG-first refinement experiment

Purpose: improve the prerequisite research graph before attempting another full-report comparison. Previous reports, graphs, scores and snapshots remain unchanged. Only the experimental WIP skill may be updated after testing; the canonical skill remains untouched.

## Design, frozen before generation

Two independent design agents: one revises only the DAG instruction block, using observed first-pilot failures; the other writes a benchmark without access to the candidate. A third agent prepares common primary-source packets without either design. Four paired graph-only tasks: AI evals and transaction isolation (regression); backpropagation and Bayesian spam classification (held out from the instruction designer). Eight fresh generation agents, one per condition/topic. No cross-run reading or nested delegation. Same inherited model/settings and source packet for each pair, with targeted gap research allowed and logged. No imposed node count. Explicit user-requested graph-only output overrides the default full-report format for both arms.

Judge labels are balanced and hidden until scores are saved. The judge receives requests, packets, outputs and independently frozen rubric; no skill files or assignment key. A common renderer makes presentation consistent. Initial/final JSON and append-only research records remain available to audit changes. Schema differences may reveal workflow; record this limitation.

## Acceptance and stopping

Freeze the independent rubric and semantic acceptance criteria before graph generation. Structural correctness is necessary but insufficient. Candidate must address material invalid dependencies, missing foundations, and unsupported complete-support labels, not merely improve its mean score. Do not promote a candidate that fails the semantic gate. If the first candidate fails, preserve it and its outputs, make one narrow evidence-driven repair, and test affected/new cases with fresh generation and independent review. If that still fails, deliver the tested alternatives and exact remaining issues instead of claiming correctness. This is a bounded refinement pilot, not a proof of a unique correct DAG.

## Skill constraints and proof

Read skill-refiner and required gotchas before refinement. Keep the self-contained skill at <=3,000 estimated tokens; preserve all non-DAG instructions. New instructions must remain topic/provider/harness agnostic. Relevant gotchas: structural validity vs behavior; no decorative evidence; single source of truth; honest gaps; names/discovery unchanged. Repository and creator validators, unchanged-text/hash checks, graph structure/replay checks, actual graph-only executions, independent semantic review and readable rendered artifacts are required. Generated reports from the first experiment are not rescored or repaired.

## Limits

Single output per condition/topic, one independent judge, shared inherited model, no human comprehension measurement, no matched token/time budget. Source packets reduce availability differences but may make the task easier; supplemental research can diverge. A DAG represents the concepts needed for this reader and explanatory scope; valid alternatives need not have identical nodes or edges.
