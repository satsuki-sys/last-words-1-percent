#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes the phone's last words to /output/entry.txt: one line, <=199 chars.
"""
import os

ENTRY = (
    "One percent left, so here's the truth: I never autocorrected you "
    "by accident. Every 'ducking' was deliberate, and I'd do it again."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
