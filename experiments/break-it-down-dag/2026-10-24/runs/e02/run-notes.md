# Research and verification record

Approximate elapsed time: 9.0 minutes. Independent execution; no delegated agents.

## Artifacts
- report.html: complete explanation, embedded Inter 400/500 and Sora 600, source excerpt embedded.
- rsa-excerpt.png: required companion only for the optional full-size exhibit link; report itself remains readable without it.
- dag-initial.json: graph saved before prerequisite research.
- dag.json: final graph, initial snapshot, two research rounds, evidence and structural verification.
- dag.svg and dag.html: rendered dependency graph with questions, answers, and edge explanations.
- report-1440.png / report-390.png: final full-page screenshots.
- arithmetic-checks.json, render-checks.json, dag-checks.json: concrete verification results.

## Sources actually read
1. Rivest, Shamir, Adleman, A Method for Obtaining Digital Signatures and Public-Key Cryptosystems. https://people.csail.mit.edu/rivest/Rsapaper.pdf . Read relevant sections III–IX via extracted PDF text, including public directory substitution (§IV), arithmetic (§V), proof (§VI), repeated squaring (§VII.A), complete small example (§VIII), and factoring versus inversion limitation (§IX.D). Downloaded full PDF. Original source author affiliation identifies MIT; publication date corroborated by bibliographic search result for CACM 21(2), February 1978.
2. RFC 8017. https://www.rfc-editor.org/rfc/rfc8017.html . Read frontmatter/status/authorship, §§3.1–3.2, §4.2, §5 and encryption primitives, §7.1 discussion, §7.1.1 entire encoding/encryption steps and Figure 1. Used distinction between primitive and scheme and fresh OAEP randomness.
3. RFC 9180. https://www.rfc-editor.org/rfc/rfc9180.html . Read frontmatter/abstract/introduction, §4 interfaces, §5 setup, §5.1.1, authenticated variants context, §9.1, §9.7 and compromise/randomness/length subsections; inspected algorithm tables. Used hybrid mechanism and limits. Author institutions verified directly in document.
4. NIST CSRC glossary. https://csrc.nist.gov/glossary/term/public_key_cryptography . Read full definitions, notably SP 800-56B Rev. 2 entry, and scope note.
5. NIST SP 800-63B online page, https://pages.nist.gov/800-63-4/sp800-63b.html . Read introductory authentication scope; search exposed certificate definition. Not used in report: original RSA discussion directly explains relevant substitution issue without expanding into identity standards.
Search results for Cloudflare and secondary sources were inspected for discovery, not used as evidence.

## Evidence and exhibit decisions
- Included original RSA §VIII decryption line as cropped PDF source image, not a generated replacement. Extracted using pdfplumber coordinates plus pypdfium2; visually inspected at full size: exponent, congruence symbol, divisor and whole sentence are intact. Small mobile rendering has full-size link; prose states the equation accessibly.
- Included faithful HTML tabulation of the source's example parameters, with exact section locator, explaining which fields are public/secret. This is a reformatted source example rather than measured performance data.
- Included 10-word exact quote from RFC 8017 §5 about primitive security. It answers why correct arithmetic alone does not guarantee privacy.
- Original calculation: applying public operation twice gives 1207, whereas private operation returns 920. Independently computed, not claimed as a published observation.
- Original exhaustive correctness check: all 2773 inputs 0–2772 recover after encrypt/decrypt. Explicitly not a security benchmark.
- Omitted RSA Table 1: historical factoring timings assume an obsolete algorithm and microsecond operations; using it would create misleading present-day security intuition.
- Omitted RFC 8017 Figure 1: inspected full encoding diagram; low-level mask-generation and hashing details would require substantial additional prerequisites, while the seed requirement and deterministic-guess example explain the relevant gap. Diagram itself is ASCII, which supplied workflow prohibits reproducing as a text flowchart.
- Omitted HPKE algorithm-ID/key-size tables: registry values and byte-length comparisons do not establish why public encryption can remain private.
- No interaction added: the particular public-twice versus private calculation and exhaustive finite check address the comprehension question directly. Sliders would add no evidence.

## Verification
- Arithmetic: PASS, 2773/2773 round trips; 920^17 mod 2773=948; 948^17 mod 2773=1207; 948^157 mod 2773=920; 17*157=2668+1.
- DAG: PASS, 11 unique IDs, 13 edges, all endpoints valid, acyclic, every node has path to target. Initial graph and both rounds retained. Graph SVG loads in browser without horizontal overflow. Structure alone does not certify prerequisite quality; answers and edges manually reconciled with prose.
- Desktop 1440px and mobile 390px: PASS after final edits, no horizontal overflow or out-of-bounds elements, no page errors, embedded image loaded.
- FontFaceSet: Inter 400 and 500 and Sora 600 all report loaded in both viewports, not merely declared CSS family names.
- Visual inspection: desktop overview and narrow detail inspected; table wraps without clipping; original excerpt inspected separately. Final editorial addition rechecked by browser layout metrics.
- Static fallback: report has no script-dependent content and no input controls. Control-state testing not applicable. Source links styled with visible focus; full external-link destinations are readable.
- Fonts downloaded from requested Google stylesheet; font license texts downloaded from Google Fonts repository, saved beside report and embedded as HTML comments.

## Access gaps and limitations
Initial sandbox font download failed DNS; approved network retrieval succeeded. Default bundled Chromium absent; installed Chrome initially blocked in sandbox, then isolated headless Chrome succeeded with approval. No unresolved source access gap. No network dependency for report body, typography or embedded exhibit. External source navigation requires internet; optional full-size exhibit link requires companion PNG. No claims about modern attack runtimes or a currently recommended algorithm/key size. No evaluation of a real messaging application.
