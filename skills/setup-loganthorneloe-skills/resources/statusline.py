#!/usr/bin/env python3
"""
Custom statusline script for Google Antigravity CLI (agy).
Parses AGY telemetry JSON from stdin and renders a context usage progress bar.
"""
import sys
import json

def format_tokens(n):
    if not isinstance(n, (int, float)):
        return "0"
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}k"
    return str(int(n))

def to_int(val):
    if isinstance(val, (int, float)):
        return int(val)
    if isinstance(val, str):
        try:
            s = val.strip().lower()
            if s.endswith("k"):
                return int(float(s[:-1]) * 1_000)
            if s.endswith("m"):
                return int(float(s[:-1]) * 1_000_000)
            return int(float(s))
        except ValueError:
            return None
    if isinstance(val, dict):
        for subkey in ["total_input_tokens", "used", "max", "total", "tokens", "count", "size", "limit", "used_tokens", "max_tokens", "context_window_size"]:
            if subkey in val:
                res = to_int(val[subkey])
                if res is not None:
                    return res
    return None

def extract_tokens(data, keys, default=0):
    for key in keys:
        curr = data
        parts = key.split(".")
        found = True
        for p in parts:
            if isinstance(curr, dict) and p in curr:
                curr = curr[p]
            else:
                found = False
                break
        if found and curr is not None:
            res = to_int(curr)
            if res is not None:
                return res
    return default

def generate_statusline():
    raw_input = ""
    try:
        raw_input = sys.stdin.read()
        if not raw_input.strip():
            data = {}
        else:
            data = json.loads(raw_input)
    except Exception:
        data = {}

    ctx_w = data.get("context_window") if isinstance(data.get("context_window"), dict) else {}

    # Extract max tokens with fallback options
    max_tokens = (
        to_int(ctx_w.get("context_window_size"))
        or to_int(ctx_w.get("max"))
        or to_int(ctx_w.get("limit"))
        or extract_tokens(data, ["max_tokens", "total_tokens", "tokens.max", "context_window_size"], default=200_000)
    )

    # Extract used tokens with fallback options
    if "total_input_tokens" in ctx_w:
        used_tokens = to_int(ctx_w.get("total_input_tokens", 0)) + to_int(ctx_w.get("total_output_tokens", 0))
    elif "used_percentage" in ctx_w and max_tokens > 0:
        used_tokens = int((ctx_w.get("used_percentage") / 100.0) * max_tokens)
    else:
        used_tokens = extract_tokens(
            data,
            ["context_usage", "used_tokens", "current_tokens", "tokens.used", "tokens.current", "context.used", "token_count", "prompt_tokens"],
            default=0
        )

    if max_tokens > 0:
        percent = min(100.0, max(0.0, (used_tokens / max_tokens) * 100))
    else:
        percent = 0.0

    # Build visual progress bar
    bar_width = 15
    filled_len = int(round(bar_width * percent / 100))

    # ANSI color coding: Green (<60%), Yellow (60-85%), Red (>85%)
    if percent < 60:
        color = "\033[32m"   # Green
    elif percent < 85:
        color = "\033[33m"   # Yellow
    else:
        color = "\033[31m"   # Red

    reset = "\033[0m"
    bold = "\033[1m"
    dim = "\033[2m"

    bar = f"{color}{'█' * filled_len}{'░' * (bar_width - filled_len)}{reset}"
    used_str = format_tokens(used_tokens)
    max_str = format_tokens(max_tokens)

    # Model and Agent State info if present
    model = data.get("model")
    if isinstance(model, dict):
        model_name = model.get("display_name") or model.get("name") or model.get("id") or "AGY"
    elif isinstance(model, str):
        model_name = model
    else:
        model_name = "AGY"

    agent_state = data.get("agent_state") or "idle"

    status_str = (
        f"{bold}Context:{reset} [{bar}] {color}{percent:.1f}%{reset} "
        f"({used_str}/{max_str}) | {dim}{model_name} [{agent_state}]{reset}"
    )

    print(status_str, flush=True)

if __name__ == "__main__":
    generate_statusline()
