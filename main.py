#!/usr/bin/env python3
"""The Best Advice I Ever Got — make.fun entry.

Writes the one-sentence entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and validates it is a single line
of 1-200 characters. Standard library only, no network.
"""

import os
import sys

ENTRY = "My father said never lend money you can't afford to lose, then handed me his last two hundred dollars and called it tuition."


def main() -> int:
    # Validate: one sentence, one line, 1-200 characters, no trailing
    # whitespace surprises. The entry earns its advice by living it:
    # the father gives the very money he warned about losing.
    if ENTRY != ENTRY.strip():
        print("error: entry has leading/trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not ENTRY.endswith("."):
        print("error: entry must be a single sentence ending with a period", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 200:
        print(f"error: entry is {len(ENTRY)} chars, must be 1-200", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR is a directory; fall back gracefully if a file path was given.
    if out_dir.endswith(".txt"):
        out_path = out_dir
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    else:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    print(f"Wrote {len(ENTRY)}-character entry to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
