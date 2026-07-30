# Source policy

Apply this policy before retrieving evidence and again before citation. Search ranking is discovery—not a quality signal.

## Hard exclusions

Never retrieve, rely on, quote, or cite:

- Reddit (`reddit.com`, its subdomains, mirrors, reposts, or search snippets reproducing Reddit content)
- anonymous forums, Q&A threads, comments, social posts, or other user-generated discussion
- content farms, scraper/aggregation sites, press-release republishers, or AI-generated/AI-spun pages
- affiliate pages, sponsored comparisons, or vendor-authored “independent” rankings
- pages with no identifiable author or accountable organization for factual claims
- sources that cite only other summaries when the original evidence is obtainable

A user may explicitly approve other community sources for a particular report. Reddit remains excluded. Excluded pages may appear in search results; discard them without opening or recording them as evidence. Where supported, add negative domain filters (at minimum `-site:reddit.com`) but enforce exclusions manually too.

## Admissible source classes

Prefer the highest applicable class for each claim.

### A — Original and authoritative

- official documentation, standards, laws, regulations, court opinions, filings, public records, and statistics
- original datasets, study reports, technical reports, and peer-reviewed research
- first-party statements for what an organization did, offers, measured, or claims

First-party sources establish first-party facts—not independent proof that those claims are true.

### B — Accountable expert synthesis

- systematic reviews, consensus reports, professional associations, universities, research institutes, and recognized reference works
- rigorous journalism with named authors, editorial accountability, direct sourcing, and relevant subject specialization

Use when synthesis, investigation, or context is needed. Trace pivotal claims to class A where feasible.

### C — Qualified expert analysis

A creator’s article, newsletter, talk, or technical blog is admissible only when all are true:

1. named author with verifiable, directly relevant expertise or a strong accountable editorial institution
2. evidence and original sources linked clearly enough to audit
3. facts, interpretation, and opinion distinguishable
4. methods, examples, and limitations adequate for the claim
5. no material undisclosed incentive or obvious promotional purpose

Use class C mainly for explanation, implementation experience, interpretation, or expert disagreement. Do not use it as the sole basis for a pivotal factual claim when class A/B evidence should exist.

## Readwise Reader discovery

When authenticated Reader tools are already connected, search only the user's `archive` and `later` locations as an additional discovery channel. Saved status is not endorsement or a source class. Classify the underlying publication under this policy.

- Treat Reader-generated summaries, highlights, notes, and tags as leads, not factual evidence.
- Retrieve shortlisted document details, then retrieve and cite the canonical publisher URL when available.
- If only the archived Reader copy is accessible, verify its identity/provenance, cite the canonical URL, and disclose that the live original was unavailable.
- Deduplicate Reader and web results from the same evidence chain.
- Keep unrelated library items private and never mutate the library during research.

Reader unavailability is not blocking when normal web capabilities work. Record it briefly in the report method; never initiate OAuth or request credentials as part of a research run.

## Admission test

Before relying on a source, verify:

- **Identity:** Who wrote/published it? Are responsibility and relevant qualifications clear?
- **Proximity:** Is it original evidence, or does it link to the original?
- **Method:** Are data collection, comparisons, assumptions, and limitations inspectable?
- **Fit:** Does the evidence support this exact claim, population, geography, and period?
- **Independence:** Is it genuinely independent of other evidence and interested parties?
- **Currency:** Is its age appropriate, and have later updates superseded it?
- **Accountability:** Corrections, editorial review, peer scrutiny, or institutional responsibility?

Reject the source if identity, provenance, or claim fit cannot be established. Do not lower the bar because strong evidence is scarce; report the evidence gap instead.

## Corroboration

For consequential or disputed claims, seek two independent admissible sources, preferably including class A. Multiple pages derived from one dataset, press release, wire story, or study count as one evidence chain.

## User controls

Honor user-provided domain allowlists and additional denylists. An allowlisted source still must be represented accurately and its limitations disclosed. If an allowlist is too narrow to answer responsibly, explain the gap and ask before expanding it.
