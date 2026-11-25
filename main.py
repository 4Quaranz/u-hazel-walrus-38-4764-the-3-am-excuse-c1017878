#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun bounty u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.

Writes one line (under 200 characters) to /output/entry.txt: the excuse a
hardware wallet gives for refusing to sign a transaction at 3 AM.
Deterministic, no network, no input, no secrets.
"""

import os

ENTRY = (
    "It's 3 AM. My secure element is off-shift, my buttons are unionised, "
    "and this transaction smells like tomorrow's regret \u2014 come back "
    "when the sun can co-sign."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} characters")


if __name__ == "__main__":
    main()
