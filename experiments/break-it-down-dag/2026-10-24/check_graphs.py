"""Check delivered prerequisite graph structure; semantic quality needs review."""
from __future__ import annotations

import json
from collections import Counter, deque
from pathlib import Path


def check(path: Path) -> dict:
    graph = json.loads(path.read_text())
    errors = []
    nodes, edges = graph.get("nodes", []), graph.get("edges", [])
    ids = [n.get("id") for n in nodes]
    if not nodes or any(not isinstance(i, str) or not i for i in ids):
        errors.append("Missing nodes or invalid node IDs")
    if len(set(ids)) != len(ids):
        errors.append("Duplicate node IDs")
    target = graph.get("target") or graph.get("target_id")
    if target not in ids:
        errors.append("Target is not a node")
    outgoing = {i: [] for i in ids}
    reverse = {i: [] for i in ids}
    indegree = Counter({i: 0 for i in ids})
    for edge in edges:
        a, b = edge.get("from"), edge.get("to")
        if a not in outgoing or b not in outgoing:
            errors.append(f"Unknown endpoint: {a} -> {b}")
            continue
        if not edge.get("why"):
            errors.append(f"Missing edge justification: {a} -> {b}")
        outgoing[a].append(b)
        reverse[b].append(a)
        indegree[b] += 1
    ready = deque(i for i in ids if indegree[i] == 0)
    order = []
    while ready:
        a = ready.popleft()
        order.append(a)
        for b in outgoing[a]:
            indegree[b] -= 1
            if indegree[b] == 0:
                ready.append(b)
    if len(order) != len(ids):
        errors.append("Graph contains a cycle")
    reaches_target = set()
    pending = [target] if target in reverse else []
    while pending:
        a = pending.pop()
        if a not in reaches_target:
            reaches_target.add(a)
            pending.extend(reverse[a])
    disconnected = sorted(set(ids) - reaches_target)
    if disconnected:
        errors.append(f"Nodes without a path to target: {disconnected}")
    for node in nodes:
        node_id = node.get("id")
        for key in ("question", "answer", "status"):
            if not node.get(key):
                errors.append(f"{node_id}: missing {key}")
        if node.get("status") not in {"assumed", "supported", "gap"}:
            errors.append(f"{node_id}: invalid status")
        if node.get("status") == "supported" and not node.get("evidence"):
            errors.append(f"{node_id}: supported without evidence")
    if not graph.get("revisions"):
        errors.append("Missing revision history")
    if not any(graph.get(k) for k in ("reader_assumptions", "assumptions", "reader")):
        errors.append("Missing reader assumptions")
    return {
        "file": str(path.relative_to(Path(__file__).parent)),
        "status": "PASS" if not errors else "FAIL",
        "nodes": len(nodes), "edges": len(edges),
        "topological_order": order, "errors": errors,
        "limit": "Structure only. Evidence entailment and prerequisite validity require independent review.",
    }


if __name__ == "__main__":
    root = Path(__file__).parent
    paths = sorted((root / "runs").glob("*/dag.json"))
    results = []
    for path in paths:
        try:
            results.append(check(path))
        except (ValueError, TypeError, KeyError) as exc:
            results.append({"file": str(path), "status": "FAIL", "errors": [str(exc)]})
    (root / "graph-checks.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))
    raise SystemExit(0 if len(paths) == 4 and all(r["status"] == "PASS" for r in results) else 1)
