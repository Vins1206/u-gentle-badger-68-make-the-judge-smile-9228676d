#!/usr/bin/env python3
"""Entry for make.fun bounty 'Make the Judge Smile'.

Writes one line (at most 200 characters) about a small good thing that
happened today to /output/entry.txt. Pure standard library, fully
deterministic: every run writes exactly the same bytes.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

LINE = (
    "This morning my neighbour's toddler pushed a dandelion through "
    "the fence and whispered, 'for your sad plant,' then ran off giggling."
)


def main() -> None:
    # Gate self-check: the scorer only judges UTF-8 text of 1 to 200
    # characters, on one line, and not only white space.
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip(), "entry must be one non-blank line"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
