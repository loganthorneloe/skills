# Run r04

Complete for the requested graph-only scope. Final: `dag.json` (17 nodes, 29 prerequisite edges). Initial: `dag.initial.json`. Chronological changes: `history.jsonl`; intermediate snapshots retained. `verification.json`, `verify_graph.py`, and `edge-audit.md` record checks. No skill files or other runs read or modified.

## Sources actually used

- [Cornell CS2110: 20. Hashing](https://courses.cis.cornell.edu/courses/cs2110/2026sp/lectures/lec20/): supplied verified packet for code/index distinction, equality and resizing; opened introductory array-access and placement-invariant passages. No assertion that all 1,327 extracted lines were studied.
- [Pat Morin: Open Data Structures §5.1](https://opendatastructures.org/ods-cpp/5_1_Hashing_with_Chaining.html): opened array-of-lists, find/add, load, doubling, random multiplier and expected-length sections. Advanced number-theory proof not needed for the conditional claim.
- [Cornell CS3110: Lecture 22](https://www.cs.cornell.edu/courses/cs3110/2008fa/lectures/lec22_amort.html): opened initial growth, geometric-sum and threshold discussion. Historical analysis supports algorithmic reasoning, not present performance measurements.
- [Berkeley CS61BL Summer 2014 Midterm 2 Solutions](https://hkn.eecs.berkeley.edu/examfiles/cs61bl_su14_mt2_sol.pdf): Question 1, printed pages 1–2, character-wise equality and uncached hash loops. Used as concrete teaching routines, not claims about current Java or Python implementations.
- [OpenDSA: Arrays](https://opendsa-server.cs.vt.edu/OpenDSA/Books/Catalog/html/Arrays.html): opening definition and accessing-array section. Address formula derived from stated contiguous storage plus explicit equal-size slots; Cornell supplies the direct-access cost claim.

## Research chronology and access gaps

Initial graph saved before supplemental browsing. Rounds 1–7 record passage reads, searches, failed accesses, no-change rounds and reconstructable edits. Search strings and exact candidate URLs are in the JSON history and tool record. Oxford array-notes PDF failed with UnexpectedStatusCode; Princeton Hash Tables failed with HTTP 403 on both URL forms; Iowa array notes failed with Cache miss; one ODS chapter click failed with invalid arguments. Those sources were not promoted to claim evidence. OpenDSA and Berkeley resolved the primitive-mechanism and key-cost gaps. No core evidence gap remains in the stated model.

## Checks performed

- Unique IDs, valid endpoints, acyclicity, evidence presence and every node reaching target: PASS.
- Manual edge-necessity audit: completed; added chain→load and hash→keycost after identifying missing term prerequisites. Examples remain outside edges.
- Numerical example: lookup success, missing lookup, four-to-eight resize, unchanged codes, moved key and remaining collision: PASS.
- Unfamiliar case: h(k)=3k+1, capacity 5→10, keys 2/7/4, query 7 and missing 12: PASS.
- Counterexample: constant hash 7, capacity 8→16, all four entries still collide and missing query scans all four: PASS.
- Incorrect resize without redistribution, inconsistent stored-key hash and geometric copied-population arithmetic: PASS.

The graph was repaired to state placement consistency, to separate capacity collisions from equal-code collisions, and to separate expected lookup from amortized rebuilding overhead. Test execution required no outside algorithmic inputs beyond the graph and supplied case parameters.

## Limits

Generic separate chaining; no CPython layout, probing algorithm, timing benchmark or universal load threshold. Constant lookup is conditional on distribution, bounded load and primitive costs. Physical memory is the standard fixed-size-slot/direct-access model. Source figures were not extracted because only graph/evidence/history were requested. No HTML or visual QA claimed; the common renderer handles visuals.
