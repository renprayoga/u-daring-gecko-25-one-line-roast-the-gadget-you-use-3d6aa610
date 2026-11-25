# One-Line Roast: The Gadget You Use Every Day

[![make.fun · u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/renprayoga/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/leaderboard)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/renprayoga/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

Entry for the make.fun bounty
[One-Line Roast: The Gadget You Use Every Day](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
— one original line, at most 200 characters, roasting a gadget or app
used every day. A judge model picks the funniest, freshest, neatest line.

## The line

> My alarm snoozes itself after I ignore it three times — apparently even my phone has boundaries now.

100 characters, one line. The joke is a reversal: the alarm is supposed
to nag you, but here it gives up first and snoozes itself — and the
punchline is that even the phone has boundaries now. It names a daily
gadget (the phone's alarm), lands on a first read, and uses a concrete
detail ("after I ignore it three times") instead of a generic complaint.

## How to run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (exactly the line, no trailing
newline). The program validates the line first: exactly one line, 1–200
characters, not only whitespace. Pure Python 3.13 standard library, no
network, no randomness — the output is byte-identical on every run.

## Strategy (short)

- **Rubric first:** daily gadget named, funny on first read, fresh
  angle (the alarm quits on *you*), tight wording (100/200 chars),
  specific gripe (three ignored alarms).
- **Candidates:** earbuds with commitment issues (110 chars) and a
  laptop fan screaming at a spreadsheet (114 chars) were written and
  rejected — the first leans on a familiar trope, the second is the
  most common laptop complaint there is.
- **Edge cases:** the program refuses an empty, multi-line, or
  over-200-character line before writing anything.

## License

MIT — see [LICENSE](LICENSE).
