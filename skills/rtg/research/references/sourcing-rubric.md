# Research Sourcing Rubric

This rubric defines the standards for research supporting AI for Software Engineers. The goal is depth, technical precision, and verifiable primary evidence across all engineering concepts in AI.

## Source Hierarchy

### Tier 1 Primary Sources
At least 3 sources in every research dossier must be Tier 1.

* Primary Engineering Blogs including technical write-ups written by infrastructure and research teams building the systems. Examples include Google Cloud or Research, OpenAI Engineering, Anthropic Research, Meta Engineering, xAI Engineering, AWS Architecture Blog, Cloudflare Blog.
* Original Research Papers and Technical Reports including direct links to arXiv, IEEE, ACM, NeurIPS, ICML, SOSP, or official laboratory preprints authored by the creators of the model, architecture, or benchmark.
* Source Repositories and Artifacts including official GitHub repositories, pull requests detailing architectural decisions, RFCs, issue tracker debates with core maintainers, and commit logs.
* Direct Primary Commentary including quotes, podcast transcripts, or technical talks from creators, lead researchers, or primary maintainers.
* First-Party Documentation including official developer documentation, API specs, SDK reference implementations, and architecture guides.
* Security Advisories and Vulnerability Databases including official CVE disclosures, NVD records, and OCI security advisories.

### Tier 2 High-Signal Independent Analysis
Use at most 1 to 2 Tier 2 sources per piece, and only if they provide unique benchmarks or synthesis.

* Recognized independent ML engineering practitioners such as Simon Willison, Eugene Yan, Chip Huyen, or Lilian Weng.
* In-depth reproducibility studies and independent benchmarks that publish their full methodology and datasets.

### Disqualified Sources
Immediately discard and do not cite the following categories.

* Generic SEO content farms, aggregators, and listicles.
* Medium or Substack posts that merely summarize existing documentation without original engineering work or benchmarks.
* AI-generated summaries and automated regurgitations.
* Vendor press releases and marketing collateral devoid of technical architectural depth.
* Secondary news roundups that quote other news articles rather than primary sources.

## Sourcing and Citation Rules

1. Concept-First Sourcing. Lab implementations, API docs, and model reports must be cited to substantiate universal engineering concepts and empirical mechanics, never to produce single-vendor tutorials.
2. Mandatory Inline Citations. Every single bullet asserting a technical claim, invariant, parameter, or benchmark must include an inline markdown link directly to the primary source. Zero sections may be left without inline citations.
3. Trace to the Root. When a secondary article mentions a benchmark, feature, or statistic, track down the original paper, pull request, or documentation page. Cite the original source.
4. Recency Standard. AI infrastructure moves rapidly. Primary sources must be from the past 1 to 2 years unless citing a foundational architecture whose core mechanism remains actively deployed in modern production stacks without change.
5. Verify Quotes and Data. Pull exact quotes, specific latency numbers, context sizes, memory requirements, and parameter counts. Avoid approximate claims when exact metrics exist.
6. Live Link Validation. Check that every URL resolves cleanly and links directly to the cited section or document.
7. Deep Linking. Whenever possible, link directly to the specific anchor, chapter, sub-page, or GitHub line range containing the information.
8. Sources First Standard. Place the Sources section immediately after the premise at the beginning of the research brief. Under each source, provide dense bullets pulling essential findings, architecture details, proven benchmarks, and direct quotes without repetitive meta-schemas.
9. Contrast and Failure Modes. Document where an approach fails. Identify edge cases, operational bottlenecks, latency costs, or structural limits of the technology being analyzed.

## Output Formatting Standards
* Present verified links inline using markdown link format.
* Keep takeaways crisp, structured, and purely bulleted.
* Never use colons anywhere in headers, bold labels, or notes.
* Exclude any parenthetical asides in the analysis prose.
* Avoid em dashes. Use commas, periods, or hyphens instead.
* Avoid marketing buzzwords. Stick strictly to concrete technical mechanisms.
