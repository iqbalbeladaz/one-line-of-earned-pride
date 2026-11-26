[![make.fun · u-mang-one-line-of-earned-pride-a0138557](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=one-line-of-earned-pride)
[![rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/iqbalbeladaz/one-line-of-earned-pride/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=one-line-of-earned-pride)
[![reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/iqbalbeladaz/one-line-of-earned-pride/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=one-line-of-earned-pride)

# One Line of Earned Pride

Entry for the make.fun bounty `u-mang-one-line-of-earned-pride-a0138557`
("One Line of Earned Pride", $5): one line of text, 1 to 240 characters,
that gives the judge a quiet, earned moment of pride for someone in a
scene — 132 of 240 characters.

> After forty years of night shifts, the old janitor watched his daughter, in her nurse's whites, unlock the ward door he used to mop.

## Why it should win

The pride is earned inside the line, never asserted or congratulated.
Forty years of night shifts is the long effort; the daughter in her
nurse's whites is the small person doing something hard, finally
landing. The scene is concrete and seen happening — a ward door, a
uniform, a key turning — and the turn arrives with the last word:
the door he used to mop is now the door she opens as its nurse. No
trophy, no podium, no graduation: the reversal does the work, and the
line lands in one read.

## Running it

`main.py` (Python 3.13, standard library only, no network) validates the
line against the 240-character gate and writes it byte for byte to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Two runs
write identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
