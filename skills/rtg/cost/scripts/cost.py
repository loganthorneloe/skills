#!/usr/bin/env python3
"""Report recorded token usage and cost from a current agent transcript."""

from __future__ import annotations

import argparse
import glob
import json
import os
import sys
from pathlib import Path
from typing import Any, Iterable

ENV_FILES = (
    "PI_SESSION_FILE",
    "CLAUDE_TRANSCRIPT_PATH",
    "CODEX_SESSION_FILE",
    "OPENCODE_SESSION_FILE",
    "AGY_SESSION_FILE",
)
GLOBS = (
    "~/.pi/agent/sessions/**/*.jsonl",
    "~/.codex/sessions/**/*.jsonl",
    "~/.claude/projects/**/*.jsonl",
    "~/.claude/sessions/**/*.jsonl",
    "~/.opencode/**/*.jsonl",
    "~/.gemini/**/transcript.jsonl",
    "~/.gemini/antigravity-cli/conversations/*.json",
)
USAGE_KEYS = {"usage", "tokenusage", "token_usage", "lasttokenusage", "last_token_usage"}


def discover(explicit: str | None) -> Path:
    if explicit:
        path = Path(explicit).expanduser().resolve()
        if path.is_file():
            return path
        raise FileNotFoundError(path)

    for variable in ENV_FILES:
        value = os.environ.get(variable)
        if value and Path(value).expanduser().is_file():
            return Path(value).expanduser().resolve()

    candidates: list[Path] = []
    for pattern in GLOBS:
        candidates.extend(Path(item) for item in glob.glob(os.path.expanduser(pattern), recursive=True))
    candidates = [path for path in candidates if path.is_file()]
    if not candidates:
        raise FileNotFoundError("no supported session transcript found")
    return max(candidates, key=lambda path: path.stat().st_mtime).resolve()


def load_records(path: Path) -> list[Any]:
    text = path.read_text(encoding="utf-8")
    try:
        parsed = json.loads(text)
        return parsed if isinstance(parsed, list) else [parsed]
    except json.JSONDecodeError:
        records: list[Any] = []
        for number, line in enumerate(text.splitlines(), 1):
            if not line.strip():
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as error:
                raise ValueError(f"invalid JSON on line {number}: {error.msg}") from error
        return records


def usage_objects(value: Any) -> Iterable[dict[str, Any]]:
    if isinstance(value, list):
        for item in value:
            yield from usage_objects(item)
        return
    if not isinstance(value, dict):
        return

    has_increment = any(key.replace("_", "").lower() == "lasttokenusage" for key in value)
    for key, child in value.items():
        normalized = key.replace("_", "").lower()
        if normalized == "totaltokenusage" and has_increment:
            continue
        if normalized in {item.replace("_", "") for item in USAGE_KEYS} and isinstance(child, dict):
            yield child
            continue
        yield from usage_objects(child)


def number(mapping: dict[str, Any], *aliases: str) -> float:
    normalized = {key.replace("_", "").lower(): value for key, value in mapping.items()}
    for alias in aliases:
        value = normalized.get(alias.replace("_", "").lower())
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return float(value)
    return 0.0


def cost_total(usage: dict[str, Any]) -> float | None:
    cost = usage.get("cost")
    if isinstance(cost, dict):
        value = number(cost, "total", "totalCost", "totalCostUsd")
        return value
    value = number(usage, "costUsd", "totalCost", "totalCostUsd")
    return value or None


def aggregate(records: list[Any]) -> tuple[dict[str, float], int, float | None]:
    totals = {key: 0.0 for key in ("input", "output", "cache_read", "cache_write", "reasoning", "total")}
    count = 0
    recorded_cost = 0.0
    cost_seen = False

    for usage in usage_objects(records):
        count += 1
        current = {
            "input": number(usage, "input", "inputTokens", "promptTokens"),
            "output": number(usage, "output", "outputTokens", "completionTokens"),
            "cache_read": number(usage, "cacheRead", "cacheReadInputTokens", "cachedInputTokens"),
            "cache_write": number(usage, "cacheWrite", "cacheCreationInputTokens"),
            "reasoning": number(usage, "reasoning", "reasoningTokens"),
            "total": number(usage, "total", "totalTokens"),
        }
        if not current["total"]:
            current["total"] = current["input"] + current["output"] + current["cache_read"] + current["cache_write"]
        for key, value in current.items():
            totals[key] += value
        cost = cost_total(usage)
        if cost is not None:
            recorded_cost += cost
            cost_seen = True

    return totals, count, recorded_cost if cost_seen else None


def integer(value: float) -> str:
    return f"{int(round(value)):,}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="explicit JSON/JSONL transcript")
    args = parser.parse_args()

    try:
        path = discover(args.file)
        totals, records, cost = aggregate(load_records(path))
    except (OSError, ValueError) as error:
        print(f"BLOCKED: {error}", file=sys.stderr)
        return 2

    if not records:
        print(f"BLOCKED: no explicit usage records in {path}", file=sys.stderr)
        return 2

    print("Session usage")
    print(f"Source: {path}")
    print(f"Usage records: {records}")
    print(f"Input: {integer(totals['input'])}")
    print(f"Output: {integer(totals['output'])}")
    if totals["cache_read"] or totals["cache_write"]:
        print(f"Cache read: {integer(totals['cache_read'])}")
        print(f"Cache write: {integer(totals['cache_write'])}")
    if totals["reasoning"]:
        print(f"Reasoning: {integer(totals['reasoning'])}")
    print(f"Total: {integer(totals['total'])}")
    print(f"Recorded cost: ${cost:.6f} USD" if cost is not None else "Recorded cost: unavailable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
