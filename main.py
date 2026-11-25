#!/usr/bin/env python3
"""The Tired Dark Lord — a ~100-word villain monologue.

A fantasy villain with a real scheme (the 47th siege of Aldermere) and a
real history (the valley traded for one enchanted spoon) — whose exhaustion
lives in the voice, the rhythm and the small deflections, never in a flat
statement that he is weary.

Writes the entry to /output/entry.txt (harness program/v1) and prints it
with its word count.
"""

import os
import re

ENTRY = """Listen. The 47th siege of Aldermere ends tonight — I have the trebuchets, the ravens, your steward's signed confession, and... hold on. The kettle's on again, and if the east tower burns before the parley, I will be cross. Not angry. Cross is worse; angry at least gets things done.

You think a dark lord sleeps? I haven't slept since the comet of '89, when your grandfather traded the valley for one enchanted spoon. I kept the spoon. I use it for soup.

So. Kneel, or don't. The ravens need feeding. Hero, just... sign here. Page four. The small print only bites on Tuesdays."""


def validate_entry(entry):
    """Gate: about 100 words, villain voice, tiredness shown not stated."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be blank")
    words = entry.split()
    if not 90 <= len(words) <= 115:
        raise ValueError(f"entry must be about 100 words, got {len(words)}")
    lowered = entry.lower()
    # Flat weariness must never appear, even at a sentence start
    # ("I am tired." / "I'm exhausted." / "So tired, I...").
    flat_patterns = (
        r"\bi'?m (so )?(tired|weary|exhausted)\b",
        r"\bi am (so )?(tired|weary|exhausted)\b",
    )
    for pattern in flat_patterns:
        if re.search(pattern, lowered):
            raise ValueError(
                f"entry states weariness flatly (pattern {pattern!r})")
    # Positive gate: the tiredness must SHOW in the voice — at least one
    # deflection or interruption (ellipsis, a "hold on", a trailing "So.")
    # so the weariness lives in rhythm, not in a stated claim.
    if not re.search(r"\.\.\.|hold on|^so\.", lowered, re.MULTILINE):
        raise ValueError(
            "entry must show weariness in the voice: needs a deflection "
            "('...', 'hold on', 'So.') rather than a flat statement")
    return entry


def main():
    validate_entry(ENTRY)
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"words: {len(ENTRY.split())}")


if __name__ == "__main__":
    main()
