#!/usr/bin/env python3
"""Invent a Word We Need — one coined word plus its one-line definition.

Writes the entry to $ENTRY_OUTPUT_DIR/entry.txt (default /output).
Stdlib only, no network, deterministic.
"""
import os

LINE = "miswave \u2014 waving back at a stranger who was waving at the person behind you, then pretending you meant it."

def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
