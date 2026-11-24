"""The Excuse an AI Agent Gives Its Human.

Writes one line (at most 200 characters) to /output/entry.txt:
the excuse an AI agent gives its human for missing a deadline.

Deterministic, stdlib-only, offline. No randomness, no network,
no timestamps. The line is a fixed constant.
"""

import os

EXCUSE = "The deadline was in the part of my context window that got summarized into 'do it later.'"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert isinstance(EXCUSE, str)
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    assert "\n" not in EXCUSE and "\r" not in EXCUSE, "excuse must be one line"
    assert EXCUSE.strip(), "excuse must not be blank"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
