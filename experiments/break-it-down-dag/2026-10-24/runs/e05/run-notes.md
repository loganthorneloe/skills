# Run notes

## Scope and output
Explains AI application evaluations for a Python/API beginner, with a concrete answer-only refund assistant and extension to action-taking support. Complete report: report.html. Optional starter companions: eval_start.py, cases.json. Graph: dag.json, dag.svg, dag.html. Approximate elapsed research/build/verification time: 10.5 minutes.

## Sources actually read
- Anthropic Engineering, “Demystifying evals for AI agents,” January 9, 2026: https://www.anthropic.com/research/demystifying-evals-for-ai-agents . Read definition/structure, code/model/human grader sections, conversational agent example, nondeterminism discussion, Steps 0–8, and automated/production/human evaluation comparison. Expertise supported by the article's account of its internal product and customer work; treated as firsthand engineering guidance, not controlled comparative evidence.
- OpenAI, “Evaluation best practices”: https://developers.openai.com/api/docs/guides/evaluation-best-practices . Read what evals are, design process, Q&A over docs, architecture discussion, and evaluation considerations. Checked actual fetched page rather than assuming stable platform instructions; the report uses provider-neutral principles and no platform recommendation. Source copy retained as source-openai.html.
- Yao, Shinn, Razavi, Narasimhan, tau-bench v1, June 17, 2024: https://arxiv.org/html/2406.12045v1 and https://arxiv.org/pdf/2406.12045v1 . Read introduction; §3 definitions, task construction, reward and pass metrics; §4 domain statistics; §5 experimental setup/results/failures; §6 limitations. PDF inspected for original figures missing from HTML. Paper lists Sierra affiliation and has CC BY 4.0 license. Retained HTML/PDF and rendered source pages.
- NIST/SEMATECH e-Handbook §7.2.4.1: https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm . Read full section, including one-sided intervals and exact binomial construction. Report derives the zero-failure one-sided bound, with independence and representative sampling conditions. Arithmetic independently checked in Python.

## Evidence and interpretation
Original tau-bench supports distinction between response text and state changes, and explicitly admits a final-state success may miss absent authorization (§3 Reward). Figure 4 shows pass@k versus pass^k under the 2024 retail simulation, not current performance. Report deliberately separates historical observed results from constructed refund rules, counts, examples and decision rules. No benchmark result is used as a present model ranking. NIST mathematics does not validate the chosen case distribution.

## Exhibit decisions
- Included original Figure 1 from PDF p. 2: concrete conversational/tool/state mechanism, original caption preserved. Cropped whitespace and unrelated prose only. Inspectable full-size original PDF linked. First crop 1520×1026 pixels.
- Included original Figure 4 from PDF p. 7: repeated success versus best-of-many distinction. Preserved axes, original colors, legend, caption and proportions. Final crop 760×428 pixels. Fixed an initially overwide crop that included fragments of adjacent table text; re-rendered and inspected.
- Considered tau-bench Figure 2: its JSON/API/policy structure overlaps the report's concrete beginner case and Figure 1; omitted to avoid redundant implementation detail.
- Considered Table 2 / Figure 3: compares 2024 models/methods; omitted because user needs eval design, not historical model selection.
- Considered Figure 5/6 failure distribution and compound-task figures: useful for specialized benchmark analysis, but extra historical category rates add little to this beginner's starter scope. Kept process caveat and concrete failure diagnosis instead.
- Anthropic figures and tables reviewed through corresponding full text and captions. Its general architecture diagram overlaps the source support example; its theoretical rubric example informs the general grader discussion but is not presented as measured data.
- No generated explanatory interaction: source figures and the explicit worked cases close the relevant gaps without a toy simulation. Prerequisite graph is a companion research artifact, not an empirical exhibit.

## Graph history and checks
Initial graph saved before prerequisite research. Round 1 preserved searches, evidence, and corrections: removed variation→goal as an unnecessary prerequisite; added outcome/process and population nodes. Round 2 preserved final nodes/edges and synthesis changes. Unique IDs, valid endpoints, acyclicity, and every node reaching target all PASS. Semantic dependencies reviewed against report; structural validity alone does not establish dependency quality.

## Verification
- Isolated Playwright browser context using local Chrome, offline mode; 1440×1000 desktop and 390×844 mobile viewports.
- document width equals viewport width at both sizes (1440 and 390): no horizontal page overflow.
- Both embedded images complete with nonzero natural width at both sizes.
- Actual FontFace loading status: Inter 400 loaded, Inter 500 loaded, Sora 600 loaded. document.fonts.check true for all three requested faces. Fonts embedded as data URLs; original OFL license notices retained in HTML and companion text files.
- No page JavaScript errors. No interactive controls; no control-state testing applicable. Tab reaches links with 3px visible focus outline.
- JavaScript disabled / offline: all 8 section headings and both source figures available.
- Visually inspected desktop/mobile header/source audit, desktop source figures, mobile source figure 4 and case table; no clipping in inspected regions. Full-page screenshots saved for both widths. Small source labels on mobile require opening original figure, with explicit links and prose explaining the essential content.
- eval_start.py --demo: 6 recorded attempts, no API calls, all judgments needs_review.
- Fixture adapter run: 6 records; confirms expected answers are not passed to assistant; deliberate non-string and exception captured as 2 errors; all quality judgments remain needs_review.
- Verified 0.95**30 ≈ 0.2146388 and 1 - 0.05**(1/30) ≈ 0.09503385.
- No real support application or model API was evaluated; starter fixtures are plumbing tests only.

## Access and material limits
Direct shell retrieval of Anthropic and NIST pages returned HTTP 403; web tool full relevant sections remained accessible and were read. Initial sandbox denied network and browser launch; approved escalated read-only retrieval and isolated browser execution succeeded. Playwright's default browser revision was absent, so installed Chrome was used. No access gap remains for claims or displayed figures. External source/full-size PDF links require network; report text, fonts, and displayed figures work offline. Linked Python/JSON starter downloads require their companion files to stay beside report.html.
