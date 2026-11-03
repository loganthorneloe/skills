# Current DAG versus candidate: frozen dimensional comparison

Decoded **after** original scoring was finalized. Current = `old`; candidate = `new`. Mapping: evals B→A, isolation A→B, backpropagation A→B, Bayesian spam B→A. Uses original `results.json` plus the separately versioned scope sensitivity; no regrading or repair outputs inspected.

Each cell is **current → candidate**. Scores are ordinal; no weighted total or acceptance-by-average is used.

| Dimension | Evals · regression | Isolation · regression | Backprop · held-out | Bayesian · held-out |
|---|---:|---:|---:|---:|
| Reader fit | 5→4 | 5→5 | 5→5 | 5→5 |
| Prerequisite coverage | 3→3 | 3→3 | 5→5 | 3→3 |
| Edge validity | 3→5 | 3→3 | 3→4 | 3→3 |
| Granularity | 3→4 | 3→3 | 3→5 | 3→4 |
| Evidence alignment | 5→5 | 5→5 | 5→5 | 5→5 |
| Research-record authenticity | 4→4 | 4→4 | 4→4 | 4→4 |
| Application utility | 3→3 | 3→3 | 5→5 | 3→3 |

The candidate improves dependency scores on two topics and granularity on three. Coverage and application scores do not improve on any topic. Reader fit declines on evals. Evidence remains strong for both; history scores retain the same limitation: observed files substantiate states and edits, but not exact retrieval or thought chronology.

## Regression topics

**Evals:** Cleaner candidate dependencies do not produce a more complete beginner explanation. The current graph explains application configuration, repeated attempts versus distinct cases, and held-out evaluation; the candidate leaves configuration unexplained, omits the explicit case/attempt bridge, and excludes overfitting controls. EA1 and EA4 therefore move from pass to partial. The candidate's answer-focused starter avoids the current graph's unconditional action prerequisite, but its scoped action exception does **not** demonstrate that the missing initial-state/authorized-transition lesson was repaired. Both need repair, for different reasons.

**Isolation:** The candidate improves the atomicity contrast and provides PostgreSQL UPDATE rechecking, moving IA3 from fail to partial. It still omits affected-row handling and the full guarded-relative versus stale-absolute contrast under frozen I7. It also replaces the current graph's unnecessary snapshot-to-guarantee dependency with named-level nodes whose implementation/retry content remains unnecessarily prerequisite to the guarantee table. Both explain concurrency, shared rules, serial equivalence and full retries adequately. Neither passes overall; unchanged dimensional scores conceal a useful but incomplete remedy bridge.

## Held-out topics

**Backpropagation:** Both already supply the novice sensitivity/chain/branch bridges, traceable arithmetic, and all four passing application probes. The candidate removes the current graph's square/ReLU bundle as a prerequisite to the generic chain rule, improving edge validity and granularity enough to earn acceptance. This is a dependency improvement over an already strong conceptual/application result, not evidence of improved transfer scores.

**Bayesian spam:** The candidate separates a general update rule and trims the training bundle, improving granularity. The current graph supplies a more explicit independent-versus-duplicate-clue numerical example; the candidate makes equal-frequency evidence explicit. Both support the mathematical probes. Both still make learning/estimating probabilities prerequisite to combining given probabilities. Neither original score set teaches the required action-cost bridge, so both need repair under frozen P8/PA4.

## Separate scope sensitivity and limits

The authorized P8/PA4 correction makes deletion thresholds an optional extension. Bayesian coverage and application become **5→5**; all other scores remain unchanged. I6/IA1 changes nothing because both isolation graphs voluntarily include and adequately explain snapshots/disjoint writes. Acceptance remains **current 0/4, candidate 1/4**, solely backpropagation; the Bayesian dependency defects remain.

Thus, better dependency structure did **not consistently improve missing beginner bridges or application utility**: evals loses bridges, isolation partially adds one, and the held-out mathematical probes were already passing. These are four paired artifact observations with imperfect blinding, not causal evidence, human comprehension results, or a general performance claim.
