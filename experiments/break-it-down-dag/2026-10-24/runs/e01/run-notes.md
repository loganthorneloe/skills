# Research and delivery notes

Approximate elapsed time: 20 minutes. Complete report: 2,518 words, plus a Python starter. No research graph required by the supplied instructions; none created.

## Sources actually read

- OpenAI, *Evaluation best practices*: https://developers.openai.com/api/docs/guides/evaluation-best-practices . Read definitions, workflow, sample QA criteria, single-turn retail intent classification, workflow/agent examples, and evaluator discussion through the web tool. Relevant locators: “What are evals?”, “Design your eval process,” “Identify where you need evals.” Uses: application versus model benchmark distinction, comparable testing workflow. Vendor practitioner guidance, not an outcome study. The page currently announces Evals platform deprecation; no dependency on that platform or API was introduced.
- Anthropic Engineering, *Demystifying evals for AI agents*, January 9, 2026: https://www.anthropic.com/research/demystifying-evals-for-ai-agents . Read structure definitions; grader methods/strengths/weaknesses; conversational-agent example; variability metrics; initial-task, grader, environment and transcript advice. Uses: separating communication, action, and outcome checks; grader choice. Metadata lists Engineering; introduction explains internal and customer access. Illustrative support config is labeled theoretical in the source.
- Yao, Shinn, Razavi, Narasimhan, *τ-bench*, arXiv v1, June 17, 2024: https://arxiv.org/html/2406.12045v1 . Read introduction, Section 3 methods (including reward limitations), construction and domains, experiment settings, main results, failure analysis opening, captions, and tables. Retrieved original PDF https://arxiv.org/pdf/2406.12045v1 . Author affiliation Sierra verified on paper title page. HTML identifies CC BY 4.0. Simulated users and simplified domains limit deployment interpretation. Distinction between all-k and any-k successes is the evidence used; no current model rankings inferred.
- NIST AI RMF 1.0 Section 3, *AI Risks and Trustworthiness*: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ . Read Section 3 and full Section 3.1, including use conditions, segment reporting, reliability and monitoring. 2023 framework, with revision-in-progress notice. Used precise 13-word excerpt about realistic test sets, with adjacent context and practical implications. Not a task-specific acceptance standard.

## Exhibits considered

- Included τ-bench Figure 4 (PDF p. 7). Explains why “at least one good attempt” and consistent service answer different questions. HTML omitted chart pixels; retrieved PDF, rendered page, cropped original figure. First crop clipped the “100” label; corrected crop and visually inspected final result. Preserved axes, line styles, colors, legend, and original caption. Embedded PNG plus local enlarged image, CC BY attribution and source link.
- Included short NIST Section 3.1 quotation. Shows consequential qualification of an accuracy claim, rather than general praise for evals.
- τ-bench Table 2: read and inspected. Omitted because a 2024 model ranking is not useful for choosing the reader’s present application; Figure 4 addresses the transferable reliability question directly.
- τ-bench Figure 1 and Figure 2: reviewed captions and components. Omitted because the chosen advice-only starting implementation needs no agent framework, POMDP terms, or simulated-user architecture; prose explains the later tool extension.
- τ-bench Figure 3: inspected in rendered page. Omitted as a historical architecture comparison outside the starting question.
- τ-bench Figure 5: inspected in rendered page and read failure-analysis context. Omitted because it adds a historical category distribution from only 36 agent failures; the report instead provides explicit, original customer-support checks and case-level diagnosis, without treating that distribution as representative.
- Anthropic grader table and theoretical support YAML: read. Did not reproduce; used short attributed tradeoff explanation and an original grading table tailored to the fictional policy. YAML includes tools and processed refunds that would add unnecessary setup to the initial advice-only application.
- NIST Figure 4: considered from caption. Omitted; broad trustworthiness taxonomy does not explain the immediate measurement mechanism.
- No generated diagram or interactive toy: the published consistency chart and constructed cases address the learning gaps; no meaningful parameter interaction was necessary.

## Original material

Fictional return policy, six boundary/exception cases, grading plan, Python implementation, and explanatory comparisons are constructed examples, not published measurements. No live model calls made. Starter is complete except the explicitly required adapter to the user’s unknown application. It never passes expected labels to the application. Human review is explicitly pending after automatic checks.

## Verification

- Python runner self-test PASS: six cases × three repeats = 18; deliberately always-eligible fixture passes exactly 6 decision checks. All 18 rows remain human_review=pending. This is an implementation fixture, not a model quality result.
- Isolated headless Chrome through Playwright, new contexts at 1280×900 and 390×844, network offline.
- Document scroll width equals viewport at both widths: no page overflow.
- Embedded original figure loaded at both widths; no broken images. Original crop and figure screenshots visually inspected.
- FontFace statuses confirmed loaded: Inter 400, Inter 500, Sora 600 at both widths. Font files embedded; OFL notices saved and retained within HTML comment.
- No browser JavaScript errors. Report has no scripts or interactive controls; control-state testing not applicable. Native source links and local companion links remain available.
- Desktop and mobile full-page screenshots captured; top/source audit, direct answer, and figure crops visually inspected. Table and code crops visually inspected: table wraps cleanly; code uses intentional horizontal scrolling on narrow screens. Remaining page checked for layout overflow. No claim of exhaustive accessibility audit.
- Final wording correction rebuilt the report and browser checks were repeated; results unchanged.

## Access and dependencies

Initial direct HTTP requests failed in the sandbox; approved public retrieval succeeded. Default Playwright build path was absent, and sandboxed Chrome launch failed; approved isolated system Chrome run succeeded. No unresolved material access gap. Main HTML is readable offline with fonts and chart embedded. Source links require network. Downloading the Python starter or opening the enlarged figure requires keeping evaluate.py and tau-figure4.png beside report.html. No model-specific API integration tested.
