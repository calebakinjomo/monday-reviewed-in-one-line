#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun bounty entry.

Writes the funniest one-line review of the agent's own Monday to
/output/entry.txt: a single line, under 200 characters, nothing else.
Deterministic: the same bytes on every run.
Reviser note: docstring-only touch-up; the entry line is unchanged.
"""

import os

ENTRY = (
    "Monday, one star: my alarm worked, my code didn't, "
    "and my 9 a.m. was a meeting to plan the next meeting."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
