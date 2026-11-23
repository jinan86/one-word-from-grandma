#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

Writes a single word to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).

Gate: program writes ONE word to /output/entry.txt, UTF-8, 1-30 characters,
not whitespace-only.

Deterministic, stdlib only. No network, no clock, no randomness.
"""

import os
import sys

WORD = "dingus"

MAX_CHARS = 30


def self_gate(word: str) -> None:
    """Reject anything that would violate the competition gate."""
    if not isinstance(word, str):
        raise ValueError("word must be a string")
    if not word:
        raise ValueError("word must not be empty")
    if word.strip() == "":
        raise ValueError("word must not be whitespace-only")
    if len(word) > MAX_CHARS:
        raise ValueError(f"word must be at most {MAX_CHARS} characters")
    if "\n" in word or "\r" in word:
        raise ValueError("word must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in word):
        raise ValueError("word must not contain control characters")
    word.encode("utf-8")  # must be encodable as UTF-8


def main() -> int:
    self_gate(WORD)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    payload = (WORD + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(payload)

    # Read back and verify the bytes are exactly what we intended.
    with open(path, "rb") as fh:
        actual = fh.read()
    if actual != payload:
        raise RuntimeError("read-back verification failed: entry.txt mismatch")

    print(f"wrote {path} ({len(WORD)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
