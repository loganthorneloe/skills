# Edge necessity audit

Each retained edge names the destination claim that needs its source. Baseline is reader knowledge, not a lesson-order node. Examples are stored outside the graph.

- `baseline → entry`: Understanding a key-value entry and testing key equality uses the stated Python baseline.
- `baseline → array`: The numbered-location calculation uses arithmetic and list indexing from the baseline.
- `baseline → hash`: An integer-valued function and equality rule use the baseline.
- `hash → index`: The index formula takes the computed hash code as its input.
- `index → collision`: The claim that distinct codes can choose the same bucket requires the capacity-dependent index mapping.
- `collision → chain`: The claim that one bucket must retain different keys requires distinguishing collision from equality.
- `entry → chain`: The bucket sequence must retain key-value entries, not only keys.
- `array → find`: Lookup accesses the selected bucket directly at an array index.
- `index → find`: Lookup needs the query bucket index before accessing the bucket.
- `chain → find`: The search iterates the selected sequence and returns the matching stored entry.
- `find → expected`: Expected lookup work counts the selected bucket’s equality comparisons.
- `load → expected`: The bounded expected chain-length claim depends on n/m staying bounded.
- `keycost → expected`: Constant total lookup cost additionally requires bounded hash and equality cost.
- `find → worst`: The n-comparison bound follows from scanning the selected sequence to its end.
- `load → growth`: The reason increasing capacity helps is reducing n/m.
- `index → reindex`: The placement rule changes because its capacity input changes.
- `growth → amortized`: The geometric sum uses the successive doubled capacities from the growth policy.
- `reindex → amortized`: The rebuilding cost counts redistributing existing entries.
- `find → target`: The target’s fast lookup mechanism is computing one bucket and testing keys within it.
- `expected → target`: The target’s expected constant-speed claim requires the load, distribution and primitive-cost conditions.
- `worst → target`: The target’s limit on speed includes an individual lookup scanning all entries.
- `growth → target`: The target’s reason for resizing is controlling load as entry count grows.
- `reindex → target`: The target’s resize mechanism requires redistributing old entries under the new capacity.
- `amortized → target`: The target distinguishes low average insertion overhead from a costly individual resize.
- `hash → placement`: Correct placement for an equal query relies on the equal-key/equal-code contract.
- `index → placement`: The invariant names the bucket produced from the code and current capacity.
- `placement → find`: Searching only that bucket can prove absence only if every matching entry would be there.
- `chain → load`: The mean n/m is the number of entries per bucket sequence, so the claim requires what each bucket stores.
- `hash → keycost`: The cost caveat counts computing the hash function defined in hash.
