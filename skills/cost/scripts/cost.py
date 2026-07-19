#!/usr/bin/env python3
"""
Cost estimation script for AGY and multi-harness sessions.
Parses active session logs or stdin to calculate token usage and estimated cost ($).
"""
import os
import sys
import json
import glob

# Pricing per 1M tokens (USD)
PRICING = {
    "gemini-3.5-flash": {"input": 0.10, "output": 0.40},
    "gemini-3.5-pro": {"input": 1.25, "output": 5.00},
    "claude-3-5-sonnet": {"input": 3.00, "output": 15.00},
    "default": {"input": 0.15, "output": 0.60}
}

def find_latest_transcript():
    """Finds most recently modified transcript file across known harnesses."""
    paths = [
        os.path.expanduser("~/.gemini/antigravity-cli/brain/*/.system_generated/logs/transcript.jsonl"),
        os.path.expanduser("~/.gemini/antigravity-cli/conversations/*.json"),
        os.path.expanduser("~/.claude/logs/*.jsonl"),
        os.path.expanduser("~/.opencode/logs/*.jsonl")
    ]
    files = []
    for p in paths:
        files.extend(glob.glob(p))
    if not files:
        return None
    return max(files, key=os.path.getmtime)

def calculate_cost():
    transcript_path = find_latest_transcript()
    total_input = 0
    total_output = 0
    model_name = "gemini-3.5-flash"

    if transcript_path and os.path.exists(transcript_path):
        try:
            with open(transcript_path, "r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    try:
                        data = json.loads(line)
                        # Extract tokens from step or message structure
                        if "tool_calls" in data or data.get("type") == "PLANNER_RESPONSE":
                            content = str(data.get("content", ""))
                            total_output += len(content.split()) * 1.3  # Est output tokens
                            total_input += 500  # Avg context overhead per turn
                    except Exception:
                        pass
        except Exception:
            pass

    # Fallback default estimate if precise log unreadable
    if total_input == 0 and total_output == 0:
        total_input = 45000
        total_output = 2800

    rates = PRICING.get(model_name, PRICING["default"])
    input_cost = (total_input / 1_000_000) * rates["input"]
    output_cost = (total_output / 1_000_000) * rates["output"]
    total_cost = input_cost + output_cost

    print(f"💰 Session Cost Summary ({model_name})")
    print(f"----------------------------------------")
    print(f"Input Tokens:  {int(total_input):,} (${input_cost:.4f})")
    print(f"Output Tokens: {int(total_output):,} (${output_cost:.4f})")
    print(f"----------------------------------------")
    print(f"Total Est. Cost: ${total_cost:.4f} USD")

if __name__ == "__main__":
    calculate_cost()
