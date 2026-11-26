#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — writes the final diagnosis line.

Stdlib only, deterministic, no network. The line itself is the entry.
The gate requires 1-200 characters of UTF-8 text, not only whitespace,
on a single line, so the line is validated against those bounds first.
"""

import os
import sys

LINE = "Diagnosis: advanced approval-seeking. You refreshed your inbox 62 times today; the only new message is from me, and it is this one."


def check_line(line: str) -> None:
    if not 1 <= len(line) <= 200:
        raise ValueError("line must be 1-200 characters, got %d" % len(line))
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")


def main() -> int:
    check_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
