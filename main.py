#!/usr/bin/env python3
"""One word for the boss: Flipflopper.

A boss who reverses every decision: Monday's plan is Tuesday's
mistake, Wednesday's U-turn is Thursday's new direction. The word
is a person-noun anyone would actually use about the boss they
report to, it lands on its own with no caption, and it travels
from a kitchen to a warehouse to an office.

The program writes that one word, and nothing else, to entry.txt
under the output directory the grader provides. Fixed text, no
clock, no network, no randomness, so every run writes the same
11 bytes.
"""

import sys
from pathlib import Path

WORD = "Flipflopper"
MAX_CHARS = 30


def entry_path() -> Path:
    import os

    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def main() -> int:
    word = WORD.strip()
    if not word or any(c in word for c in (" ", "\t", "\n", "\r")):
        print("entry must be a single word with no spaces", file=sys.stderr)
        return 1
    if len(word) > MAX_CHARS:
        print(f"entry is {len(word)} chars, limit is {MAX_CHARS}", file=sys.stderr)
        return 1
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(word, encoding="utf-8")
    print(word)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
