#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest entry.

Writes one short, funny rant (1-400 characters) about an everyday
annoyance to /output/entry.txt. Stdlib only; no network, no reads
outside the repo.

The rant: the self-checkout machine accusing an honest shopper of
stealing the very apples it just watched them scan. Specific, concrete,
and economical -- every sentence earns its place, no throat-clearing.
"""

import os

RANT = (
    "The self-checkout screamed 'UNEXPECTED ITEM IN THE BAGGING AREA' "
    "at a bag of apples. Apples. I scanned them. I bagged them. I did "
    "everything right, and this glowing robot still treated me like a "
    "fruit smuggler on parole. Then it froze, beeped, and summoned a human -- the "
    "one job it was built to replace. I did its job "
    "and get accused of theft. Cashier, take me back."
)


def main() -> None:
    text = RANT.strip()
    assert 1 <= len(text) <= 400, f"rant is {len(text)} chars, must be 1-400"
    assert text.strip(), "rant must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
