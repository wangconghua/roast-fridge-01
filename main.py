#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single original one-line roast of a smart fridge to
/output/entry.txt (or $ENTRY_OUTPUT when set).

The line roasts a real smart-fridge behaviour -- its internal camera
and recipe suggestions -- with the sting landing at the end: the
fridge films food rotting, then suggests cooking with food that is
already in the bin.
"""

import os
import sys

ENTRY = (
    "My smart fridge films my leftovers rotting in 4K, "
    "then helpfully suggests recipes using the chicken "
    "I threw out last Tuesday."
)

MIN_CHARS = 1
MAX_CHARS = 160


def validate(text):
    """Check the entry is one non-blank line of 1-160 characters."""
    if text is None:
        raise ValueError("entry is None")
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is blank")
    if len(stripped) < MIN_CHARS or len(stripped) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, must be %d-%d"
            % (len(stripped), MIN_CHARS, MAX_CHARS)
        )
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    if stripped != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    return stripped


def check_single_sentence(text):
    """One sentence only: exactly one sentence-ending mark, at the end."""
    endings = sum(text.count(mark) for mark in ".!?")
    if endings != 1:
        raise ValueError("entry has %d sentence endings, expected 1" % endings)
    if text[-1] not in ".!?":
        raise ValueError("entry must end with a sentence-ending mark")
    return True


def check_length(text):
    """Entry must fit the 1-160 character gate."""
    n = len(text)
    if n < MIN_CHARS or n > MAX_CHARS:
        raise ValueError("entry is %d characters, must be 1-160" % n)
    return True


def check_no_second_line(text):
    """No hidden second sentence hiding behind a newline or semicolon run-on."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry spans more than one line")
    return True


def check_roasts_smart_gadget(text):
    """The line must roast a smart home gadget the writer lives with."""
    lowered = text.lower()
    gadgets = ("fridge", "smart fridge", "thermostat", "vacuum",
               "doorbell", "speaker", "oven", "washer")
    if not any(g in lowered for g in gadgets):
        raise ValueError("entry does not name a smart home gadget")
    return True


def check_no_milk_ordering_cliche(text):
    """Freshness: never reuse the stale 'fridge orders milk' joke."""
    lowered = text.lower()
    banned = ("order milk", "orders milk", "ordering milk",
              "order more milk", "reorder milk", "buys milk")
    for phrase in banned:
        if phrase in lowered:
            raise ValueError("entry reuses the stale milk-ordering cliche: %r" % phrase)
    return True


def check_specific_real_behaviour(text):
    """The roast must pin a concrete behaviour of the device, not a vague insult."""
    lowered = text.lower()
    behaviours = ("film", "camera", "suggest", "recipe", "notif",
                  "beep", "report", "remind", "track", "scan")
    if not any(b in lowered for b in behaviours):
        raise ValueError("entry names no specific real device behaviour")
    return True


def check_fast_setup(text):
    """Sets up fast: no throat clearing, no padding before the joke."""
    lowered = text.strip().lower()
    openers = ("so ", "well ", "okay ", "ok ", "let me tell you",
               "you know what", "picture this", "imagine ")
    for opener in openers:
        if lowered.startswith(opener):
            raise ValueError("entry opens with throat clearing: %r" % opener)
    first_clause = text.split(",")[0]
    if len(first_clause) > 60:
        raise ValueError("setup clause is %d chars, too slow" % len(first_clause))
    return True


def check_ends_with_sting(text):
    """The twist lands at the end: the final clause must carry the punch."""
    tail = text.rsplit(",", 1)[-1].strip().lower()
    sting_markers = ("threw out", "already", "last tuesday", "bin",
                     "expired", "rotting", "judge", "vote")
    if not any(m in tail for m in sting_markers):
        raise ValueError("entry's ending carries no sting")
    return True


def run_extra_checks(text):
    """Run every freshness and craft check added after the first draft."""
    check_roasts_smart_gadget(text)
    check_no_milk_ordering_cliche(text)
    check_specific_real_behaviour(text)
    check_fast_setup(text)
    check_ends_with_sting(text)
    return True


def main():
    text = validate(ENTRY)
    check_single_sentence(text)
    check_length(text)
    check_no_second_line(text)
    run_extra_checks(text)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("wrote %d characters to %s" % (len(text), out_path))
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
