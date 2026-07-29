#!/usr/bin/env python3
"""Dependency-free structural validator for an Agent Skill."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path
from urllib.parse import unquote

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
EMPTY_IMPERATIVES = ("make no mistakes", "do your best", "be careful")


def scalar(frontmatter: str, key: str) -> str | None:
    lines = frontmatter.splitlines()
    for index, line in enumerate(lines):
        match = re.match(rf"^{re.escape(key)}:\s*(.*)$", line)
        if not match:
            continue
        value = match.group(1).strip()
        if value in ("|", "|-", ">", ">-"):
            parts: list[str] = []
            for following in lines[index + 1 :]:
                if following.startswith((" ", "\t")) or not following.strip():
                    parts.append(following.strip())
                else:
                    break
            separator = "\n" if value.startswith("|") else " "
            return separator.join(parts).strip()
        if value.startswith('"') and value.endswith('"'):
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value[1:-1]
        if value.startswith("'") and value.endswith("'"):
            return value[1:-1].replace("''", "'")
        return value
    return None


def local_link_target(raw: str) -> str | None:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(maxsplit=1)[0]
    target = unquote(target).split("#", 1)[0]
    if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
        return None
    return target


def validate(skill_arg: str, max_tokens: int) -> int:
    supplied = Path(skill_arg).expanduser().resolve()
    skill_file = supplied / "SKILL.md" if supplied.is_dir() else supplied
    failures: list[str] = []

    if skill_file.name != "SKILL.md" or not skill_file.is_file():
        print(f"FAIL: SKILL.md not found at {skill_file}")
        return 1

    text = skill_file.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", text, re.S)
    if not match:
        print("FAIL: missing or malformed YAML frontmatter")
        return 1

    frontmatter = match.group(1)
    name = scalar(frontmatter, "name")
    description = scalar(frontmatter, "description")

    if not name:
        failures.append("frontmatter name is missing")
    else:
        if len(name) > 64 or not NAME_RE.fullmatch(name):
            failures.append("name must be <=64 chars, lowercase alphanumeric, hyphen-separated")
        if name != skill_file.parent.name:
            failures.append(f"name {name!r} does not match parent directory {skill_file.parent.name!r}")

    if not description:
        failures.append("frontmatter description is missing")
    else:
        if len(description) > 1024:
            failures.append("description exceeds 1,024 characters")
        if not description.startswith("Load when"):
            failures.append("description must start with 'Load when'")
        if not re.search(r'["“][^"”]{3,}["”]', description):
            failures.append("description needs at least one quoted phrase a user would type")

    approximate_tokens = max(
        math.ceil(len(text) / 4),
        math.ceil(len(re.findall(r"\S+", text)) / 0.75),
    )
    if approximate_tokens > max_tokens:
        failures.append(
            f"SKILL.md is ~{approximate_tokens} tokens; default maximum is {max_tokens}"
        )

    lowered = text.lower()
    for phrase in EMPTY_IMPERATIVES:
        if phrase in lowered:
            failures.append(f"remove empty imperative: {phrase!r}")

    missing_links: list[str] = []
    markdown_files = sorted(skill_file.parent.rglob("*.md"))
    for markdown_file in markdown_files:
        markdown = markdown_file.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(markdown):
            target = local_link_target(raw)
            if target and not (markdown_file.parent / target).resolve().exists():
                relative = markdown_file.relative_to(skill_file.parent)
                missing_links.append(f"{relative}: {target}")
    if missing_links:
        failures.append("missing local links: " + ", ".join(sorted(set(missing_links))))

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(
            f"RESULT: FAIL | {skill_file} | description={len(description or '')} chars "
            f"| approximate_tokens={approximate_tokens}"
        )
        return 1

    print(
        f"PASS: {skill_file} | description={len(description or '')} chars "
        f"| approximate_tokens={approximate_tokens} | markdown_files={len(markdown_files)} "
        f"| local_links=ok"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill", help="Skill directory or SKILL.md path")
    parser.add_argument("--max-tokens", type=int, default=1500)
    args = parser.parse_args()
    return validate(args.skill, args.max_tokens)


if __name__ == "__main__":
    sys.exit(main())
