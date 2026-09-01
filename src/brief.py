#!/usr/bin/env python3
"""Minimal prototype. No API key required.

You type a question. The script prints a blank contract template
and reminds you to paste only sourced facts.

Later you can call an LLM here. Keep the same five blocks.
"""

from textwrap import dedent


DISCLAIMER = "Not a trade recommendation. 不是交易建议。"

BLOCKS = """
============================================================
STABLECOIN BRIEF
{disclaimer}
============================================================
QUESTION
{question}

1. CONCLUSION (≤3 sentences)
   -

2. FACTS (delete any line without a URL)
   - fact + URL
   - fact + URL
   - fact + URL

3. PRODUCT OPTIONS
   A.
   B.
   C.

4. UNVERIFIED (move leftover claims here)
   -

5. METRIC HYPOTHESIS
   If we shipped this, we would watch:
   -
============================================================
"""


def main() -> None:
    print("Stablecoin Brief  v0")
    print(DISCLAIMER)
    print("Type one question, then Enter. Empty line quits.\n")
    question = input("Question: ").strip()
    if not question:
        return
    print(
        BLOCKS.format(disclaimer=DISCLAIMER, question=question)
    )
    print("Next: fill Facts from docs/compare-table.md only.")


if __name__ == "__main__":
    main()
