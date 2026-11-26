#!/usr/bin/env python3
"""Everyday Things, Two Lines: an escalator, explained to a 10-year-old.

Line 1 explains the escalator with a vivid analogy; line 2 says why the
analogy works and what it leaves out. Stdlib only.
"""
import os

ENTRY = (
    "An escalator is a staircase that got tired of waiting and decided to walk for you, carrying you up step by step while you just stand still.\n"
    "The analogy works because the steps really do move and carry you like a walking staircase, but it leaves out that escalators run on motors and fixed tracks, so they can break, stop, and need repairs, unlike ordinary stairs."
)


def validate(text):
    """Mirror the sealed gate: UTF-8 text, 1-400 chars, not only whitespace,
    exactly two non-empty lines."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 400):
        raise ValueError(f"entry is {len(text)} chars, gate is 1-400")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    lines = [line for line in text.split("\n") if line.strip()]
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly two lines, got {len(lines)}")
    return True


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
