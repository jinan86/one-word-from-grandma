# One Word From Grandma

[![make.fun](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![Rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/jinan86/one-word-from-grandma/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![Reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/jinan86/one-word-from-grandma/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)

Entry for the make.fun competition
[One Word From Grandma](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
— the program writes a single word to `/output/entry.txt`.

## The word

> **dingus**

The classic grandma word for a gadget she can't name — *"hand me that
dingus."* Warm, baffled, funny, and machine-adjacent. Six characters,
one line, nothing else.

## How it works

`main.py` (Python 3.13, stdlib only, deterministic — no network, clock,
or randomness) self-gates the word (UTF-8, 1–30 characters, single line,
not whitespace-only, no control characters), writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output`), then reads the file
back and verifies the bytes are identical before exiting.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt   # dingus
```
