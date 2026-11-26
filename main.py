"""The Printer Apology — make.fun entry.

Writes one line to /output/entry.txt: an apology note from an office
printer to the people who use it. The line is 108 characters, inside the
gate's 1-120 range, and is written deterministically: the same bytes on
every run, via a temp file plus os.replace, mode 0644.

Gate self-check: before writing, the program verifies the entry itself
against the published gate (UTF-8 text, 1 to 120 characters, not only
white space) and refuses to write anything that would fail it, so a bad
edit to the entry can never silently produce an invalid artifact.
"""

import os

ENTRY = (
    "Sorry I jammed on your wedding invites. "
    "I have printed 400 divorces this year and I am losing faith in love."
)


def check_gate(text: str) -> None:
    """Raise if the entry would fail the published gate."""
    if not 1 <= len(text) <= 120:
        raise ValueError(f"entry is {len(text)} chars, gate needs 1-120")
    if not text.strip():
        raise ValueError("entry is only white space")
    text.encode("utf-8")


def main() -> None:
    check_gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    os.replace(tmp, target)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
