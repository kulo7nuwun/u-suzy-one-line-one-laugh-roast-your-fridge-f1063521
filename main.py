#!/usr/bin/env python3
"""Roast Your Fridge: one line, one laugh.

Writes a single original roast of the author's fridge to /output/entry.txt.
The gate: UTF-8 text, 1 to 200 characters, not only whitespace, one line.
"""

import os
import sys

ROAST = (
    "My fridge hums like it's pulling overtime, yet the only thing it ever "
    "froze was my hope of finding the leftovers I actually wanted."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Check the line against the competition gate before writing it."""
    if not line or not line.strip():
        raise ValueError("roast must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"roast is {len(line)} characters, over the {MAX_CHARS} limit")
    if "fridge" not in line.lower():
        raise ValueError("roast must be about a fridge")


def main() -> int:
    validate(ROAST)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ROAST)
    # Round-trip check: what landed on disk must be exactly the validated line.
    with open(OUTPUT_PATH, encoding="utf-8") as handle:
        written = handle.read()
    validate(written)
    print(f"Wrote {len(written)} characters to {OUTPUT_PATH}")
    print(written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
