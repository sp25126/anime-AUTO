#!/usr/bin/env python3
"""
Token Tracker for Antigravity Session 8518879d-daa2-4c16-a02d-6a3e628d2997
Reads the session transcript and generates a token consumption summary.
"""

import json
import os
import sys

TRANSCRIPT_PATH = r"C:\Users\saumy\.gemini\antigravity\brain\8518879d-daa2-4c16-a02d-6a3e628d2997\.system_generated\logs\transcript.jsonl"

def get_token_metrics():
    if not os.path.exists(TRANSCRIPT_PATH):
        return {"error": "Transcript file not found"}

    total_input = 0
    total_output = 0
    total_cache_read = 0
    turns_with_tokens = 0
    total_steps = 0

    with open(TRANSCRIPT_PATH, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            total_steps += 1
            try:
                data = json.loads(line)
                inp = data.get("input_tokens", 0) or 0
                out = data.get("output_tokens", 0) or 0
                cache = data.get("cache_read_tokens", 0) or 0
                if inp or out or cache:
                    turns_with_tokens += 1
                    total_input += inp
                    total_output += out
                    total_cache_read += cache
            except Exception:
                continue

    return {
        "total_steps": total_steps,
        "model_turns": turns_with_tokens,
        "input_tokens": total_input,
        "output_tokens": total_output,
        "cache_read_tokens": total_cache_read,
        "net_unprompted_tokens": total_input + total_output,
        "total_tokens_including_cache": total_input + total_output + total_cache_read
    }

if __name__ == "__main__":
    m = get_token_metrics()
    print("=" * 50)
    print("SESSION TOKEN CONSUMPTION AUDIT")
    print("=" * 50)
    print(f"Total Steps Logged       : {m['total_steps']}")
    print(f"Model Invocations/Turns  : {m['model_turns']}")
    print(f"Direct Input Tokens      : {m['input_tokens']:,}")
    print(f"Context Cache Read Tokens: {m['cache_read_tokens']:,}")
    print(f"Output / Generated Tokens: {m['output_tokens']:,}")
    print("-" * 50)
    print(f"Billed/Fresh Tokens (In+Out): {m['net_unprompted_tokens']:,}")
    print(f"Total Processed (Inc. Cache): {m['total_tokens_including_cache']:,}")
    print("=" * 50)
