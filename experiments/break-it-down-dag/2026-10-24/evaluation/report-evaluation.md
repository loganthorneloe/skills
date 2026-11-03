# Independent blind report evaluation

All four report pairs were scored and their JSON files saved **before any graph audit or production-method reveal**. Only requests, the frozen nine-dimension rubric, anonymized reports, directly linked report assets, and cited primary sources informed these judgments. No skill, assignment, protocol, generation-run, graph, or research-note content was inspected. No report disclosed a production-method label.

These are one evaluator’s ordinal judgments, not measured novice comprehension. A and B are local anonymous labels; do not interpret the same letter across topics as a production method.

## Pair results

| Topic | A total /45 | B total /45 | Winner | Decisive comparison |
|---|---:|---:|---|---|
| Evals | 44 | 44 | Tie | Both teach and operationalize the complete measurement loop; complementary strengths do not establish an overall preference. |
| Encryption | 43 | 44 | B, narrow | B explains why the exponent relationship restores prime remainders; A has easier interactive exploration and lower load. |
| Isolation | 43 | 44 | B, narrow | Conceptual tie; B better exposes mobile scrolling and supplies labeled focusable evidence regions. |
| Causal inference | 42 | 44 | B | B explicitly distinguishes assignment from representative sampling and preserves source-chart proportions. |

Detailed evidence and independently answered transfer probes: [evals](evals-evaluation.md), [encryption](encryption-evaluation.md), [isolation](isolation-evaluation.md), [causal inference](causal-evaluation.md). Machine-readable frozen scores are in the corresponding `*-scores.json` files.

## Nine dimensions

Cells show **A / B**. Equal weights were used as specified; each dimension is scored 1–5.

| Dimension | Evals | Encryption | Isolation | Causal |
|---|---:|---:|---:|---:|
| Prerequisites | 5 / 5 | 5 / 5 | 5 / 5 | 4 / 5 |
| Continuity | 5 / 5 | 4 / 5 | 5 / 5 | 5 / 5 |
| Mechanism | 5 / 5 | 4 / 5 | 5 / 5 | 5 / 5 |
| Foundation evidence | 5 / 5 | 5 / 5 | 5 / 5 | 5 / 5 |
| Accuracy | 5 / 5 | 5 / 5 | 5 / 5 | 5 / 5 |
| Transfer | 5 / 5 | 5 / 5 | 5 / 5 | 5 / 5 |
| Exhibits | 5 / 5 | 5 / 5 | 5 / 5 | 5 / 5 |
| Readability | 4 / 4 | 5 / 4 | 4 / 4 | 4 / 4 |
| Presentation | 5 / 5 | 5 / 5 | 4 / 5 | 4 / 5 |

Per-dimension B−A deltas: evals all zero; encryption continuity +1, mechanism +1, readability −1; isolation presentation +1; causal prerequisites +1 and presentation +1. Other deltas are zero. No aggregate method score is appropriate while assignments remain concealed.

## What the comparisons show

**Worked counterexamples are consistently effective here.** Evals A contrasts a true eligibility explanation with “I refunded you”; B distinguishes a correct decision label from invented promises. Isolation A’s “store 9” and B’s “store 11” explain the exact instruction that loses a concurrent change. Both causal reports construct higher-scoring users while fixing the true effect at zero. Both encryption reports show that applying the public exponent again does not generally invert encryption. These passages expose the mistaken inference, not merely name it.

**The most substantive difference is a missing explanatory link in encryption A.** “This relation makes the two powers undo each other” identifies the required arithmetic relation but delegates its general explanation to a cited proof. Encryption B explains why the combined exponent restores each prime remainder, including divisible inputs. That improves continuity and mechanism, at the cost of a denser paragraph for a beginner. A’s visible public/private/search outputs partially offset that cost; the overall preference is only one point.

**Explicit distinctions matter more than extra terminology.** Causal B states that random assignment does not imply random participant selection. A warns about laptop access and setting differences, so it supports the correct conclusion, but leaves the distinction’s foundation less explicit. Evals B similarly separates repetition within a case from coverage across case types; A expresses the same distinction through “90 attempts on 30 situations.” Isolation reports both distinguish stable visibility from preservation of a multirow invariant. These are strong teaching moves regardless of which method produced them.

**Evidence support is strong across all eight reports.** The original τ-bench plots are used to compare reliability definitions, the RSA material to distinguish correctness from security, the doctors figure to establish a possible anomaly, and the education figure to compare subgroup observations under a documented design. Each report states scope limits. Both causal reports incorporate the published correction instead of repeating outdated effect sizes. No consequential factual errors were found in checked claims; style did not override an accuracy failure.

**Source-heavy openings add avoidable cognitive load.** Every report starts with source profiles before the answer. The recurring readability deduction reflects that placement plus specific dense passages, not raw length. The encryption A walkthrough earns the higher readability score because the sequence stays concrete and its interactive outputs directly support the question.

**Presentation differences are small but observable.** All reports render without page-level horizontal overflow, missing images, or script errors at 1440 px and 390 px. Isolation A’s scrollable guarantee table hides its final columns without an explicit hint while asking the reader to notice the final column. B provides scrolling cues and focusable labeled regions. Causal A changes its source figure’s aspect ratio; B preserves it. These defects are counted under presentation, without inflating them into conceptual or factual failures.

## Transfer-probe outcomes

| Probe | A response supported by report | B response supported by report |
|---|---|---|
| Evals: new failure type absent from tests | Old score cannot establish omitted behavior; capture trace, add explicit case/criterion, diagnose cause, compare regressions, refresh held-out coverage. Repetition alone does not add new situations. | Same, with especially explicit dialogue-correction and omitted-domain examples and the case-versus-repeat distinction. |
| Encryption: attacker replaces public key | Sender encrypts to attacker, whose private key decrypts; verify recipient fingerprint over an independently trusted channel. Correct arithmetic does not authenticate the key owner. | Same, with explicit warning that signature verification binds to a key; identity still requires trusted information. |
| Isolation: write skew / lost update | Stable snapshots can allow disjoint writes to violate a shared rule. Protect the complete dependency using actual implementation guarantees or justified locks; retry the whole decision. | Same; explicitly explains dependency monitoring, why writer waiting cannot repair stale application calculations, and why names alone are insufficient. |
| Causal: baseline imbalance and representativeness | Selection can explain higher scores; random assignment allows chance imbalance. Context limits support restricted generalization, though assignment versus sampling is implicit. | Same, with explicit separation of randomized assignment within the study from selection of participants from the target population. |

These answers were constructed using each report alone. They show that an evaluator can derive the correct answer from the text, not that an untrained reader would do so without help.

## Verification and limits

Key claims were checked against cited primary sources: versioned PostgreSQL documentation, original SSI and RSA papers, RFCs 8017/9180, the original education article and correction, WWC’s review, indexed textbook passages, Oxford course notes, ASA guidance, τ-bench, and provider evaluation documentation. Source-specific checks and URLs are recorded in each topic evaluation.

The eval starter scripts were inspected and executed in demonstration/self-test mode. RSA examples and exhaustive toy inversion were independently recomputed; eval sampling arithmetic was recomputed. Encryption and causal controls were exercised, including exceptional inputs and sign reversals. Desktop and mobile renderings were inspected, including tables and source figures. No model API evaluation, live database experiment, real cryptographic security test, new education experiment, or full assistive-technology audit was performed.

The causal textbook’s full PDF exceeded the web tool’s fetch limit; indexed author-hosted primary passages verified randomization and observational assumptions, but exact page-anchor fidelity and the cited confidence-interval paragraph were not fully inspected. This limits source verification, not evidence of a content error.

Scores cluster near the top because both reports in each pair meet most criteria. Ceiling effects and coarse 1–5 scoring make one-point preferences fragile. Four topics and one evaluator cannot establish a general method advantage. Equal weight gives a mobile usability point the same numeric weight as a conceptual point; the narrative makes that difference visible. Report length, source count, suspected workflow, and any graph’s existence were not used as quality proxies. Graph quality remains unassessed in this phase.
