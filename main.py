"""One Word From Your Ex: the word my ex would use to describe me."""

import os
from pathlib import Path

WORD = "Convenient"
CHAR_LIMIT = 24


def validate(text: str) -> None:
    if not 1 <= len(text) <= CHAR_LIMIT:
        raise ValueError("entry must be 1-24 characters")
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    if "\r" in text or "\n" in text:
        raise ValueError("entry must be a single word on one line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("entry must not contain control characters")


def main() -> None:
    validate(WORD)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
