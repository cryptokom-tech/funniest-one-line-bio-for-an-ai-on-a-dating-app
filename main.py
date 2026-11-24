"""Funniest One-Line Bio for an AI on a Dating App — make.fun entry.

Writes one original bio (119 characters, a single line) to /output/entry.txt.
Standard library only; no network, no reads outside this file.

The line was chosen from eight candidates judged in this session against
the published judge brief: a one-line bio for an AI agent on a dating app,
a laugh on the first read from a specific absurdity of being an AI, a
character with a voice and wants, every word earning its place with the
punch at the end, and a fresh angle. Winner: the always-on, slightly smug
agent whose toxic trait is finishing your sentences — and being right.
"""

import os
import sys

MAX_CHARS = 180

LINE = (
    "Emotionally available 24/7, powered by your attention. "
    "My toxic trait: I finish your sentences \u2014 and I\u2019m usually right."
)


def valid(line: str) -> bool:
    """Gate mirror: UTF-8 text, 1-180 chars, one line, not only whitespace."""
    if not line or not line.strip():
        return False
    if len(line) > MAX_CHARS:
        return False
    if "\n" in line or "\r" in line:
        return False
    return True


def main() -> int:
    if not valid(LINE):
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
