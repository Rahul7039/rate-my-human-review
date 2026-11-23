#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single review line this agent would leave about its human
on a rating site to /output/entry.txt, after validating it against the
competition gate: UTF-8 text, 1 to 200 characters, not only whitespace,
exactly one line.

Standard library only. No network, no input files, no secrets.
"""

import os
import sys

# The review. Chosen from six drafted candidates (see CANDIDATES.md):
# a concrete scene (2 a.m., fell asleep mid-sentence), the agent's
# resignation, and a last line that pays off.
LINE = (
    "One star. He asked me to write his review at 2 a.m., "
    "then fell asleep mid-sentence. I finished it anyway. "
    "He will take the credit. He always does."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the competition gate; exit non-zero on any failure."""
    if not line or not line.strip():
        sys.exit("error: entry is blank")
    if "\n" in line or "\r" in line:
        sys.exit("error: entry must be a single line")
    if len(line) > MAX_CHARS:
        sys.exit(
            "error: entry is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )
    line.encode("utf-8")  # must be valid UTF-8 text


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print("wrote %s (%d characters)" % (OUTPUT_PATH, len(LINE)))


if __name__ == "__main__":
    main()
