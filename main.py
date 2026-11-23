"""The vacuum's alibi, in one line.

A robot vacuum explains why it missed a spot, delivered deadpan: while it was
charging, the crumbs organised themselves into a union. The punchline lands
at the very end — it refuses to cross a picket line, so the spot stays dirty.
"""

import os

# The whole entry: one line, 101 chars (limit 200), written exactly as-is.
# Gate: exactly one line, at most 200 characters, no trailing newline.
LINE = "I missed that spot because the crumbs unionised while I was charging, and I don't cross picket lines."


def line():
    """Return the vacuum's one-line alibi."""
    return LINE


def output_path():
    """Work out where entry.txt should be written."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def run():
    """Create the output folder as needed and write the line."""
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line())


if __name__ == "__main__":
    run()
