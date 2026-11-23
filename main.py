#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry (rewrite).

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt
(falls back to /output when the variable is unset).

Competition gate: the file must hold a single word, UTF-8 encoded,
1-30 characters long, and not whitespace-only.

Deterministic, standard library only. No network access, no clock,
no randomness, no environment-dependent behaviour beyond the
output directory.
"""

import os
import sys

THE_WORD = "dingus"
MAX_WORD_CHARS = 30
OUTPUT_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def check_word(candidate: str) -> bytes:
    """Validate the word against the competition gate.

    Returns the exact UTF-8 payload (word + newline) to write.
    Raises ValueError on any gate violation.
    """
    if not isinstance(candidate, str):
        raise ValueError("word must be a string, got %r" % type(candidate).__name__)
    if len(candidate) == 0:
        raise ValueError("word must not be empty")
    if len(candidate) > MAX_WORD_CHARS:
        raise ValueError(
            "word is %d characters, over the %d-character limit"
            % (len(candidate), MAX_WORD_CHARS)
        )
    if candidate.strip() == "":
        raise ValueError("word must not be whitespace-only")
    if any(char.isspace() for char in candidate):
        raise ValueError("word must be a single word with no whitespace inside it")
    if "\n" in candidate or "\r" in candidate:
        raise ValueError("word must fit on a single line")
    for char in candidate:
        code = ord(char)
        if code < 0x20 or code == 0x7F:
            raise ValueError("word must not contain control characters")
    try:
        payload = (candidate + "\n").encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("word must be encodable as UTF-8") from exc
    return payload


def resolve_output_dir() -> str:
    """Output directory from the environment, defaulting to /output."""
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if configured:
        return configured
    return DEFAULT_OUTPUT_DIR


def write_and_verify(payload: bytes, directory: str) -> str:
    """Write the payload and read it back; the bytes must match exactly."""
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, OUTPUT_NAME)
    with open(target, "wb") as handle:
        handle.write(payload)
    with open(target, "rb") as handle:
        written = handle.read()
    if written != payload:
        raise RuntimeError("read-back mismatch in %s" % target)
    return target


def run() -> int:
    payload = check_word(THE_WORD)
    target = write_and_verify(payload, resolve_output_dir())
    print("wrote %s (%d characters)" % (target, len(THE_WORD)))
    return 0


if __name__ == "__main__":
    sys.exit(run())
