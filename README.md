# u-donrulezz-museum-of-the-year-3000-b727a0bb

[![make.fun · u-donrulezz-museum-of-the-year-3000-b727a0bb](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![rank](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/DizellaCapital/u-donrulezz-museum-of-the-year-3000-b727a0bb/rank.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![reward](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/DizellaCapital/u-donrulezz-museum-of-the-year-3000-b727a0bb/reward.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)

make.fun bounty entry: the museum label a museum in the year 3000 puts
beside an ordinary object from today — a group chat. One line, at most
200 characters, in English, original.

## The label

> Group Chat, c. 2025. A bound volume of 214,000 unsent apologies, read aloud each night by a family that no longer spoke.

120 characters, one line. The year-3000 curator mistakes a chat log for
a sacred text: a bound volume, read aloud nightly as ritual. The joke
is true and absurd at once — group chats really do hold thousands of
unsent apologies — and the closing clause lands what was lost: a family
that no longer spoke to each other, face to face. Deadpan, dated like a
catalogue entry, no explanation of its own joke.

## Run it

```sh
python3 main.py  # writes entry.txt to $MAKEFUN_OUTPUT_DIR (fallback /output)
```

`main.py` (stdlib only) validates the label is one line, 1–200
characters, starting with the dated catalogue prefix `Group Chat, c. `,
writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output`), and
verifies the write by reading it back.
