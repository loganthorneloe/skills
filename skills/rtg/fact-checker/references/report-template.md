# Fact-Check Report Template and Verification Standards

Use this reference to structure fact-check reports and evaluate linked claims.

## Verification Status Categories

Every linked claim must be classified into one of four statuses.

* Verified. The source directly supports the claim, metric, or quote in full context without distortion.
* Inaccurate. The source contradicts the claim, or the document misrepresents numbers, findings, or mechanisms.
* Missing Evidence. The linked source does not mention or substantiate the specific claim made in the text.
* Inaccessible. The link is broken, returns an HTTP error, sits behind an unauthenticated paywall, or redirects away from the content.

## Report Template

```markdown
# Fact-Check Report

* Document Checked. [Document Name](https://example.com/document)
* Date Evaluated. Current Date
* Total Links Checked. 0
* Verified Claims. 0
* Inaccurate Claims. 0
* Missing Evidence. 0
* Inaccessible Links. 0

## Executive Summary
* High-level summary of factual accuracy and link reliability.
* Primary patterns of misalignment or data drift identified.

## Detailed Findings

### Section Name

* Claim. Excerpt of the claim made in the document
  * Source Link. [Source Title](https://example.com/source)
  * Status. Verified, Inaccurate, Missing Evidence, or Inaccessible
  * Source Evidence. Exact quote, figure, or metric extracted from the retrieved source
  * Analysis. Clear explanation of what is right, what is wrong, or why the source fails to back up the claim
  * Recommended Fix. Exact replacement text, corrected metric, or updated primary URL

## Recommended Corrections Summary
* Short bulleted list of high-priority text corrections and URL replacements.
```

## Pre-Flight Verification Checklist
Before saving and presenting the report, verify every item.

1. Every link in the document was fetched and inspected against its underlying source text.
2. Snippets and search summaries were not treated as proof; primary source text was retrieved directly.
3. Every finding includes the original claim, source link, exact retrieved evidence, and clear correction.
4. The report contains zero colons outside https URLs.
5. The report contains zero parentheses outside markdown links.
6. The report contains zero em dashes.
7. The report contains zero marketing buzzwords.
