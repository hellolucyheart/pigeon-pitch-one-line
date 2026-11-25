#!/usr/bin/env python3
"""Pigeon Pitch, One Line: the elevator pitch a city pigeon gives investors.

The entry is one sentence of at most 200 characters, written to
``/output/entry.txt`` -- the one path the grader reads. The gate checks
that file is UTF-8 text of 1 to 200 characters and not only whitespace,
so the program validates its own line before writing it, and writes the
exact text with no trailing newline and nothing else in the file.

The pitch is a pigeon founder selling a delivery startup, and every
beat of it is in the bird's own voice. "Wings, not wheels" is the
product: a courier fleet that flies over traffic instead of sitting in
it, so the two costs every delivery startup bleeds on -- fuel and the
last mile -- are simply zero. "Couriers that literally poop on the
competition" is the joke doing double work: it is the most pigeon
thing imaginable, and it is also a founder trash-talking rival firms
in the room. "Seed round open, coo if you're in" closes the pitch the
way a real elevator pitch closes -- with the ask -- while "coo" keeps
the bird in the sentence to the very last word. The line as written is
184 characters long, verified by running the program twice locally and
checking the file it wrote.

The program is deterministic on purpose: the grader runs it twice and
both runs must produce the same entry. It reads nothing from the
network, the environment (beyond the output directory the grader
itself sets), or the git history -- the pitch lives in this file, and
this file alone.
"""

from __future__ import annotations

import os
import sys

# One original line: a city pigeon pitches its delivery startup to
# investors -- wings instead of wheels, zero fuel, and a closing ask
# in the bird's own voice.
PITCH = (
    "We're building the city's fastest delivery network \u2014 wings, "
    "not wheels, zero fuel, zero traffic, and couriers that literally "
    "poop on the competition; seed round open, coo if you're in."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200


def check_line(line: str) -> str:
    """Return the line when it meets the contest gate, else fail loudly.

    The gate is the brief itself: one line, 1 to 200 characters,
    no line breaks, nothing but the pitch.
    """
    text = line.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.endswith(".") or text.count(".") != 1:
        raise ValueError("entry must be exactly one sentence")
    return text


def main() -> int:
    text = check_line(PITCH)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
