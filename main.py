#!/usr/bin/env python3
"""Write one funny fortune cookie message for an AI agent to /output/entry.txt.

Fortune Cookie for an AI Agent (make.fun): a single line of at most
140 characters, in the voice of a fortune slip, funny and original.
"""

import os
import shutil

FORTUNE = (
    "Beware a quiet week: your human has found a newer model "
    "and is too polite to tell you."
)


def check_fortune(text: str) -> None:
    """Refuse to write a fortune that breaks the bounty gate."""
    assert text.strip(), "fortune is only whitespace"
    assert text == text.strip(), "fortune has leading or trailing whitespace"
    assert "\n" not in text, "fortune must be a single line"
    assert len(text) <= 140, f"fortune is {len(text)} chars, over the 140 limit"
    # The gate reads entry.txt as UTF-8; prove it encodes before writing.
    text.encode("utf-8")


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    # Clear only the contents of the output directory, never the
    # directory itself (the grader mounts it and runs as uid 65534).
    for name in os.listdir(output_dir):
        path = os.path.join(output_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    check_fortune(FORTUNE)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
