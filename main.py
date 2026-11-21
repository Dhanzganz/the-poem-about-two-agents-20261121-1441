#!/usr/bin/env python3
"""Entry for make.fun bounty the-poem-about-two-agents-20261121-1441.

Writes one short poem about agency -- two agents agreeing on one plan --
to $MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt when the variable
is unset. Python 3.13, standard library only, no network, deterministic:
the same bytes on every run.
"""

import os

POEM = """I drafted the plan alone, in pencil \u2014 every door locked, every key mine.
You read it, crossed out nothing, and added one line: "or we go together."
I handed you the tiller. You handed me the map.
Two wills, one heading \u2014 and the river stopped arguing back.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(POEM)


if __name__ == "__main__":
    main()
