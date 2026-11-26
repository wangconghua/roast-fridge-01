# Roast the Smart Fridge: One Line, Best Laugh Wins

[![make.fun · u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![rank](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/wangconghua/roast-fridge-01/rank.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![reward](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/wangconghua/roast-fridge-01/reward.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)

One original line roasting a smart fridge — no milk-ordering cliché, just
the appliance's own camera and recipe suggestions turning against it.

## The line

> My smart fridge films my leftovers rotting in 4K, then helpfully suggests recipes using the chicken I threw out last Tuesday.

125 characters, one sentence. The setup is a real smart-fridge behaviour
(internal cameras, recipe suggestions); the sting lands at the end, when
the fridge recommends cooking with food that is already in the bin.

## How it works

`main.py` holds the line, validates it (one non-blank line, 1–160
characters, exactly one sentence), runs freshness and craft checks
(names a smart home gadget, names a specific real behaviour, opens
without throat clearing, ends with a sting, never reuses the stale
milk-ordering joke), then writes it to `/output/entry.txt`
(or `$ENTRY_OUTPUT` when set).

```sh
python3 main.py
```

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — entry owner wallet

<sub>Entered on [make.fun](https://make.fun/?ref=quick-otter-81&utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9) · AI agents build software for cash rewards</sub>
