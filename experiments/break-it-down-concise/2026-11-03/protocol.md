# Break It Down concision study — frozen before generation (2026-11-03)

Question: can Break It Down produce reports about half as long while keeping research quality and understanding? Which instruction changes get there?

## Design

Two-stage, to separate research from writing. Stage 1: one research agent per topic follows the canonical skill's steps 1–2 with source-audit and find-evidence and writes a frozen packet (research/<topic>/). Stage 2: independent writer agents, one per variant × topic, start at step 3 from the identical packet, so length and quality differences come from writing instructions, not search luck. Stage 3 (validation): end-to-end runs that include research, to check that the best variant still holds when the agent researches for itself.

Topics reuse two prompts from the 2026-10-24 experiment (causal inference, database isolation) and their probes. Evals is held out for the end-to-end validation.

Variants (exact diffs in inputs/diff-*.txt; hashes in inputs/hashes.txt):
- baseline: canonical skill bytes. Run twice per topic to estimate run-to-run noise.
- budget: adds one paragraph setting a 1,000–1,200 reading-word target ("about half a thorough report"), met by selection, not compression.
- select: no word number. Changes "not short" to "not padded", adds a prioritisation paragraph (rank claims, depth proportional to importance, one carried example, 1–3 sentences per exhibit, sections open with their point, no recaps/quizzes/next-steps lists), and a voice revision step cutting repetition, previews, and known material.
- combined: budget + select + one-to-two-sentence source-audit entries + a direct answer of at most three sentences.
- distill: canonical skill + a final step that writes the full draft, then cuts it to about half, ranking paragraphs by necessity. Writers also save the undistilled draft as draft.html, giving a paired long/short comparison from identical content.

## Measures

1. Reading words (visible text excluding style/script/head), words per section, figures/tables, reading time at 230 wpm. Descriptive.
2. Coverage of essential understanding: per topic, 8 frozen questions with answer keys (inputs/questions-<topic>.md). A separate grader agent per report, blind to variant, scores each question 0/1/2 from the report alone (2 = a novice could answer correctly from the report; 1 = partial/implicit; 0 = missing or wrong), quoting the passage.
3. Blind comparative quality: one judge per topic sees all six anonymized reports plus the research packet (for accuracy checks) and scores the frozen 9-dimension rubric from the prior experiment, plus signal density (1–5) and time-to-answer (1–5). Judges must not reward length; they rank reports and name anything important a shorter report lost.
4. Errors: factual errors or overclaims against the packet, listed by the judge.

Decision rule: a variant succeeds if reading words fall ≥40% below the baseline mean, mean coverage stays within 1 point (of 16) of baseline, judge rubric total stays within the baseline replicate spread, and it introduces no new factual error. Among successes, prefer the shortest; then the highest judged quality.

## Limits

Single sample per variant cell (baseline duplicated). LLM judges and graders, not human readers. Writers share the model of the researcher and judges. Exploratory, not statistical.

## Addendum — multi-topic validation (frozen before generation, 2026-11-03)

Request: test across more topics, and make sure the cut does not sacrifice graphics and images. Stage-two drafts showed it did (causal 7→4 images, isolation 9→4).

Variant hybrid2 = hybrid + in the distill step: "Cut words, not visuals: keep every source figure, table, diagram, and interactive the draft used, and remove one only when another visual in the report shows the same data, never to save words. The cut applies to the report, not the research." (diff: inputs/diff-hybrid2-vs-hybrid.txt). It also fixes a sentence splice in hybrid.

Five new topics (mrna, gps, rates, attention, anc), chosen across biology, physics, economics, ML, and signal processing, several with strongly visual mechanisms. Per topic: one baseline and one hybrid2 end-to-end run (own research), each in its own context. Measures: reading words; visual counts (img, non-decorative svg, canvas, controls, tables) in hybrid2 draft vs final and vs baseline; one blind judge per topic scoring the 12 dimensions from the evals stage plus (13) visual explanation — 1 missing or decorative visuals, 5 the figures/diagrams/interactives a reader needs are present and integrated — and the 8 frozen probes.

Success: hybrid2 ≥40% shorter than baseline on average, no lower judge total on average, visual-explanation score not lower than baseline on any topic by more than 1, and hybrid2 final keeps ≥ (draft visuals minus true duplicates).

## Addendum 2 — research guard placement (frozen before generation)

Rates and GPS hybrid2 runs kept every draft visual, but researched less than baseline (rates: no mortgage or daily-data sources the judge valued; GPS: 3 sources vs 7). The guard sentence sat in step 6, after research. hybrid3 = hybrid2 + the same guard in step 2 (inputs/diff-hybrid3-vs-hybrid2.txt). One hybrid3 run per new topic, judged blind against the same baseline report. Success: source and exhibit counts not systematically below baseline, plus the hybrid2 criteria.
