# The 3 AM Excuse

[![make.fun · u-hazel-walrus-38-4764-the-3-am-excuse-c1017878](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/4Quaranz/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/4Quaranz/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

One line, under 200 characters: the excuse a hardware wallet gives for
refusing to sign a transaction at 3 AM.

## The entry

> It's 3 AM. My secure element is off-shift, my buttons are unionised, and this transaction smells like tomorrow's regret — come back when the sun can co-sign.

## How it works

`main.py` writes that single line to `/output/entry.txt`. It is
deterministic, needs no network, no input and no secrets — run it twice and
the output is byte for byte identical.

```sh
python3 main.py
cat /output/entry.txt
```

## Bounty

- Competition: [The 3 AM Excuse](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
- Prize: $2 (10 places paid), deadline 26 Nov 2026 22:15 WIB
- Gate: `/output/entry.txt` must be UTF-8 text of 1 to 200 characters
