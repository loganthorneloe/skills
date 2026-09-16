---
name: fact-checker
description: 'Load when the user says "fact check this", "verify links", "check claims in this article", "audit sources in this draft", or asks to verify that linked sources actually substantiate the claims made in a document.'
---

# Fact-Checker Skill

Audit articles, research briefs, and technical drafts to verify that embedded links actually contain the information they claim to and substantiate the assertions made in the text.

Produce a structured fact-check report detailing what was checked, what was accurate, what was inaccurate or unsupported, and specific recommendations for corrections.

When evaluating a document file, write the complete verification report directly to `[filename]-fact-check.md` in the same directory, or output directly in the conversation when checking an inline passage.

## 1. Extract Links and Assertions

1. Read the target document completely.
2. Extract every hyperlink, including external URLs and internal linkbacks.
3. Pair each link with the immediate claim, assertion, metric, or quote it intends to support.
4. Capture the surrounding paragraph context so the claim's scope and intent are unambiguous.

Criterion. Every link in the document is mapped to its specific textual assertion and surrounding context.

## 2. Retrieve Underlying Sources

1. Fetch the actual content of each linked source using web retrieval or file inspection tools.
2. Never rely on search engine snippet summaries or cached metadata as evidence.
3. Locate the specific section, table, figure, or passage within the source that addresses the claim.
4. If a link returns an HTTP error, broken redirect, or blocked page, record the link as Inaccessible.

Criterion. Every candidate link is retrieved directly and its relevant content isolated for comparison.

## 3. Verify Claims Against Evidence

Compare the author's claim against the retrieved primary source content.

1. Classify each claim into one of four standard statuses defined in [references/report-template.md](references/report-template.md).
2. For claims marked Verified, pull an exact quote or quantitative data point from the source that corroborates the text.
3. For claims marked Inaccurate, pinpoint the exact discrepancy, determining whether numbers diverge, conclusions are exaggerated, or mechanisms are misstated.
4. For claims marked Missing Evidence, confirm that the source mentions no data or findings relevant to the assertion.
5. Identify outdated data where a cited benchmark or specification has been superseded by newer authoritative releases.

Criterion. Every link is categorized with exact source excerpts and a clear explanation of alignment or failure.

## 4. Draft the Fact-Check Report

Before drafting, read [references/report-template.md](references/report-template.md) for the required structure.

1. Begin with an executive summary including total links checked, verified claims, inaccurate claims, missing evidence, and inaccessible links.
2. Group detailed findings by document section or chronological appearance.
3. Under each finding, present the document claim, source URL, verification status, retrieved source evidence, analysis, and recommended fix.
4. Provide concrete, actionable corrections, including suggested rewording, corrected numbers, or replacement primary sources.
5. Conclude with a short summary list of recommended edits.

Criterion. The complete fact-check report is saved to `[filename]-fact-check.md` or returned in the conversation.

## 5. Formatting and Proof Gates

Enforce strict formatting constraints across all report text.

* Zero colons rule. Never use a colon anywhere in headings, bullet labels, or prose notes. Colons are permissible only inside verified markdown link protocol prefixes like https.
* Zero parentheses rule. Never use parentheses in prose notes. Rewrite sentences smoothly with commas or periods. Parentheses are strictly reserved for markdown link syntax.
* Zero em dashes. Use commas, periods, or hyphens instead.
* Zero buzzwords. Eliminate words like game-changing, delve, tapestry, landscape, revolutionize, crucial, and foster.
* Zero metaphors. Describe findings using literal technical terminology.

Verify all items in the pre-flight checklist in [references/report-template.md](references/report-template.md) before final delivery.

## Hard Exit

Verify each condition before concluding.
* Every link in the source document has been retrieved and evaluated.
* The report explicitly classifies every link as Verified, Inaccurate, Missing Evidence, or Inaccessible.
* Exact quotes or metrics from primary sources support every finding.
* Concrete replacement text or URLs are supplied for all failed checks.
* The report contains zero colons outside https URLs, zero parentheses in prose notes, and zero em dashes.
