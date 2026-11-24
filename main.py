"""make.fun one-line-pitches entry.

Writes a single sentence that would convince a friend who has never
coded to let an AI agent build their first app idea on make.fun.
"""

import os

LINE = (
    "Describe that app idea you've been carrying around in plain "
    "words tonight, and an AI agent on make.fun will build you a real "
    "first version you can tap through tomorrow \u2014 you never touch "
    "a line of code."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
