"""One Word for the Boss — make.fun bounty
u-swift-badger-44-one-word-for-the-boss-6b48c735

Writes exactly one word describing the boss (Ng) to /output/entry.txt:
"nocturnal" — he hunts free mints at 3 a.m., decides in one word, and runs
a swarm of agents. A creature of the night: funny on its own, true, fresh,
and it travels to any boss in any industry.

Standard library only. Deterministic, no network. No trailing newline.
Respects MAKEFUN_OUTPUT_DIR for local testing (default /output/entry.txt).
"""

import os

ENTRY = "nocturnal"  # lowercase on purpose: the word as a colleague would
# actually say it about their boss, not a label or a name.


def _validate(word: str) -> None:
    """Gate the entry exactly as the scorer does, before writing."""
    assert isinstance(word, str) and 1 <= len(word) <= 30, "length gate"
    assert word == word.strip(), "no surrounding whitespace"
    assert word.isalpha(), "letters only — a single word, no punctuation"
    assert len(word.split()) == 1, "exactly one token"


def main() -> None:
    _validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly one word, 1-30 chars, no trailing newline, UTF-8.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read back and confirm what landed is byte-for-byte the entry.
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == ENTRY


if __name__ == "__main__":
    main()
