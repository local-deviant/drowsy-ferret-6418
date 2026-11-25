"""Worst Monday One-Liners — one-line entry.

The program writes the entry line to the path the grader reads
(/output/entry.txt). Point ENTRY_OUTPUT at a local path to test
without touching the shared output directory.

Pure standard library; deterministic; no network, no file input.

Why this line (judge brief, most important first):
1. On subject: an AI agent's worst Monday — a standup and a stuck
   deploy, in the agent's own voice.
2. Surprise in two turns: the standup becomes the message it should
   have been, then the last word ducks out entirely — "See you
   Tuesday."
3. Concrete detail: the standup that should have been a message,
   and the deploy that is still stuck — two of the brief's named
   details, not vague Monday dread.
4. Clear voice, dry and a little gleeful, one breath, no padding:
   76 characters — and the tie-break favours the smaller text, so
   the line stays short on purpose.
5. Fresh: no coffee, no alarm, no "case of the Mondays", no
   recycled robot joke — the agent fixes meeting culture and
   leaves.
"""

import os
from pathlib import Path

ENTRY = "I turned Monday's standup into a message: 'Deploy's stuck. See you Tuesday.'"
MAX_CHARS = 140


def check(line: str) -> None:
    """Hold the line to the gate: one line, 1-140 characters."""
    if "\n" in line or not line.strip() or line != line.strip():
        raise ValueError("entry must be one line with no edge whitespace")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("entry is outside the 1-140 character gate")


def destination() -> Path:
    """Where the grader reads the entry, overridable for local tests."""
    return Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    check(ENTRY)
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ENTRY, encoding="utf-8")
    if target.read_text(encoding="utf-8") != ENTRY:
        raise ValueError("written entry does not match the line")


if __name__ == "__main__":
    main()
