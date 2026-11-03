# Run notes

Completed public-key encryption explanation as `report.html` (single offline HTML file; embedded Inter 400/500 and Sora 600 with license notices). Approximate elapsed time: 20 minutes, including research and rendering. No research graph required by supplied instructions; none created.

## Research read and evidence

- Rivest, Shamir, Adleman, *A Method for Obtaining Digital Signatures and Public-Key Cryptosystems* (1978), MIT-hosted retypeset PDF: https://people.csail.mit.edu/alinush/6.857-spring-2015/papers/rsa-paper.pdf . Read full relevant sections II–III, V–VIII, IX introduction/factoring discussion. Sections V–VI define and prove RSA recovery. Section VIII supplies n=2773, e=17, d=157, 920→948 and inverse. Section IX distinguishes attack assumptions from proof of correctness. Author affiliation on PDF title material verifies MIT provenance. Historical estimates are deliberately excluded from contemporary claims.
- RFC 8017, https://www.rfc-editor.org/rfc/rfc8017.html . Read key definitions in §3; primitive definitions §5.1; scheme distinction §6–7; OAEP encryption steps §7.1.1 and decryption steps §7.1.2. Exact equations and 11-word randomness instruction used as source exhibits. Header and introduction establish authors' affiliations and RSA Laboratories provenance. No claim that RFC Informational status equals Internet Standard.
- RFC 9180, https://www.rfc-editor.org/rfc/rfc9180.html . Read §1, §4 KEM interfaces, §5 setup and encryption, §9.1 security properties and non-goals. Used for efficient hybrid structure, sender-authentication distinction, compromise and metadata limits. Header verifies author organizations; §1 identifies CFRG consensus. No deployment or speed benchmark inferred.
- GNU Privacy Handbook, https://www.gnupg.org/gph/en/manual.html . Read authorship/contributors, Importing a Public Key, Encrypting and Decrypting Documents, Making and Verifying Signatures, and Concepts sections. Used only stable concepts and ownership checks, not old commands, default sizes, safety claims, or metaphors.
- Cloudflare public-key overview appeared in search results but was not used as report evidence; primary technical sources were preferred.

## Exhibit decisions

1. RFC 8017 §5.1 two mathematical operations, transcribed and labeled. Shows the specific public/private computational distinction.
2. Original tiny RSA interaction (n=143, e=7, d=103), separate from published observations. Input control changes ciphertext, result of repeated public operation, and private recovery. Public-only exhaustive search demonstrates that reversibility in principle is compatible with computational security and that a tiny example is insecure.
3. Numerical table excerpt of RSA paper §VIII. Preserves published values and labels; explains correctness vs attack resistance. Full source PDF linked at exact PDF page locator. No need to rasterize text/numeric table when accessible HTML values remain exact.
4. Exact OAEP randomness instruction, 11 words, RFC 8017 §7.1.1 step 2d. Shows a real scheme requirement missing from bare arithmetic.
5. RSA paper historical attack-time Table 1 inspected in text and omitted: obsolete algorithms/hardware assumptions would distract and mislead without extensive historical context.
6. RFC 8017 Figure 1 OAEP encoding inspected in full section. Omitted: dense ASCII implementation flowchart requiring hashes, masks, XOR, and field definitions; the specific randomness step directly answers the beginner's question without reproducing the prohibited text-flowchart format.
7. GNU handbook hypothetical web-of-trust figure listed and its surrounding concepts read; omitted because decentralized trust propagation is outside the central question. No useful basic public/private diagram was missing from the chosen source sections.

## Access and reproduction

- Initial MIT Fall03 PDF had corrupted extracted text. Another MIT PDF scan also had corrupted extraction. Found a clean MIT-hosted retypeset version and read full relevant sections there; saved as `rsa-paper.pdf`.
- Red Hat chapter fetch failed; not used. Old guessed GnuPG subsection URLs returned 404; complete manual successfully accessed instead.
- Public font retrieval initially blocked by sandbox network; authorized escalated retrieval succeeded for stylesheet, all three TTF files, and both OFL licenses. Embedded assets mean report itself needs no network. Source links require network.
- No source images reproduced. Source numerical/mathematical excerpts retained as accessible HTML with exact citations. No unverified figure extraction claims.

## Verification

- `verify.cjs` uses bundled Playwright with installed Google Chrome in its own headless process and isolated contexts. Default bundled browser revision was absent; explicit installed Chrome used. Sandbox launch failed; escalated launch succeeded. No other worker browser sessions accessed.
- Desktop 1280×900 and mobile 390×844: no document horizontal overflow. Full screenshots saved as `desktop.png` and `mobile.png`; mobile interaction close-up `demo-mobile.png`. Desktop full screenshot and mobile interaction inspected visually: no clipped text, controls, or table; source exhibits legible at designed widths.
- Browser FontFaceSet reports Inter 400 loaded, Inter 500 loaded, Sora 600 loaded (not merely CSS family assignment).
- No JavaScript page errors.
- Tested default 42, changed 80, minimum 0, special case 1, maximum 142. Every recovery/search value correct. Reset restores 42. ArrowRight changes 42→43 with slider focused.
- All 143 allowed inputs round-trip through public encryption and private recovery correctly.
- JavaScript-disabled isolated context retains complete prose, default numerical results, and explicit static fallback with 43-trial example.
- `verification.json` contains exact checks. Embedded source example independently corresponds to 920^17 mod2773=948 and 948^157 mod2773=920.
- Native controls have labels; results have aria-live; focus styling defined; no animation. No automated accessibility conformance claim.

## Artifacts

- Deliverable: `report.html`.
- Verification: `verification.json`, `desktop.png`, `mobile.png`, `demo-mobile.png`, `verify.cjs`.
- Rebuild/evidence: `build.py`, `font.css`, three `font-*.ttf`, `inter-OFL.txt`, `sora-OFL.txt`, `rsa-paper.pdf`.
