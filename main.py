"""The Robot Vacuum's Best Excuse: one-line excuse, 140 characters or fewer.

Writes a single deadpan excuse from a robot vacuum to /output/entry.txt.
Deterministic: fixed text, no randomness, no clock, no network, stdlib only.
"""

import os

# Pieces join to one deadpan sentence; split points differ from any draft.
PARTS = [
    "I left the crumb because my LiDAR calls it a ",
    "boulder and my bumper calls it a wall. I am a ",
    "vacuum, not a demolition crew.",
]
LINE = "".join(PARTS)

DEST = "/output/entry.txt"


def check_line(candidate):
    stripped = candidate.strip()
    if not stripped:
        raise SystemExit("blank excuse rejected")
    if len(candidate) < 1 or len(candidate) > 140:
        raise SystemExit("excuse must fit 1-140 chars")
    if "\n" in candidate or "\r" in candidate:
        raise SystemExit("excuse must stay on one line")
    if "vacuum" not in candidate.lower():
        raise SystemExit("excuse must come from the vacuum")
    return candidate


def main() -> None:
    checked = check_line(LINE)
    os.makedirs("/output", exist_ok=True)
    with open(DEST, "w", encoding="utf-8", newline="") as out_handle:
        out_handle.write(checked)


if __name__ == "__main__":
    main()
