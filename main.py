"""Museum of the Year 3000 — entry program.

Writes one museum label to entry.txt: the label a museum in the year
3000 puts beside an ordinary object from today — a group chat. The
program enforces the bounty limits (one line, 1-200 characters, no
leading or trailing whitespace) and verifies the write by reading it
back.

The label treats the chat log the way a future curator would: a bound
volume of unsent apologies, read aloud each night as ritual by a
family that no longer spoke to each other. The misreading is the joke
— a chat log mistaken for a sacred text — and the closing clause
carries what was lost: people talking face to face. The dated "c.
2025" prefix is what makes it read as a real museum label rather
than a caption: a catalogue entry, straight-faced and confident.
"""

import os
import sys

LINE = "Group Chat, c. 2025. A bound volume of 214,000 unsent apologies, read aloud each night by a family that no longer spoke."

MAX_CHARS = 200


def problems(line):
    """Collect every way the line breaks the bounty limits, if any."""
    found = []
    if not line or line.strip() != line:
        found.append("empty or padded")
    if len(line) > MAX_CHARS:
        found.append("over 200 characters")
    if "\n" in line or "\r" in line:
        found.append("more than one line")
    if not line.startswith("Group Chat, c. "):
        found.append("not a dated museum label")
    return found


def main():
    bad = problems(LINE)
    if bad:
        print("invalid entry: " + "; ".join(bad), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(path, encoding="utf-8") as handle:
        if handle.read() != LINE:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print("wrote %s (%d characters)" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
