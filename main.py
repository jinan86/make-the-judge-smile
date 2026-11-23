"""Make the Judge Smile — make.fun bounty entry.

Writes exactly one line of text to /output/entry.txt: a single sentence
about a small good thing that happened today.

Deterministic: stdlib only, no network, no clock, no randomness.
The sentence is a fixed literal, so every run produces identical bytes.
"""

import os
from pathlib import Path


def build_entry() -> str:
    """Return the single-sentence entry."""
    return (
        "This morning the ojek driver who found my wallet rode back through "
        "the rain to return it, then refused my tip and laughed that the "
        "real fare was just seeing my face unfreeze."
    )


def main() -> None:
    entry = build_entry()
    text = entry.strip()
    if not text or "\n" in text:
        raise ValueError("entry must be exactly one non-empty line")
    encoded = text.encode("utf-8")
    if not 1 <= len(encoded) <= 200:
        raise ValueError(f"entry must be 1-200 UTF-8 chars, got {len(encoded)}")
    out_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(encoded + b"\n")


if __name__ == "__main__":
    main()
