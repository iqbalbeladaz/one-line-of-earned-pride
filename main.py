"""one-line-of-earned-pride: one line of quiet, earned pride.

The line turns on a reversal the reader only feels at the last word:
a father who spent forty years mopping a hospital ward watches his
daughter unlock that same ward's door as its nurse. No trophy, no
podium, no graduation, no congratulation — the pride is earned inside
the line by the forty years of night shifts and lands when the door
he used to mop becomes the door she opens as a nurse.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = "After forty years of night shifts, the old janitor watched his daughter, in her nurse's whites, unlock the ward door he used to mop."

MAX_CHARS = 240


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
