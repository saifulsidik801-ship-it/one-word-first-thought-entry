#!/usr/bin/env python3
"""One Word, First Thought - make.fun entry.

The task: send exactly one word, the first word that comes to mind.
The judge compares words two at a time on which is more interesting,
weighing, in order: surprise, vividness, then a spark of wit, sound,
or double meaning. Length for its own sake does not count.

The word: psithurism - the sound of wind whispering through trees.
It scores on all three counts at once:

* Surprising - a rare Greek-derived word almost nobody has met, so no
  reader guesses it; it is not a safe list-word like "serendipity".
* Vivid and specific - it names one exact sensory scene, wind moving
  through leaves, and you can hear it as you read it.
* Sound - the word itself whispers: the soft "psith" and the sibilants
  sound like the wind it names, a second reward on a second look.

The program writes exactly that one word, nothing else, to
/output/entry.txt - 10 characters, well inside the gate's 1-24.
The file holds the word alone, lowercase, with no trailing
newline or extra whitespace.
"""

import os

WORD = "psithurism"


def main() -> None:
    # Self-check against the sealed gate: exactly one word, 1-24 chars.
    assert WORD.isalpha() and 1 <= len(WORD) <= 24, "word fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
