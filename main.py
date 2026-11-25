"""One-Line Roast: The Gadget You Use Every Day.

Entry line (100 characters, exactly one line):

    My alarm snoozes itself after I ignore it three times — apparently even my phone has boundaries now.

Strategy report (Protokol Top 5 — rubric first, before the code):

1. Rubrik (judge weighs in this order):
   - Daily gadget/app named clearly: the alarm app on the phone — a
     gadget everybody uses every day, named in the line itself.
   - Actually funny on first read: the reversal. The alarm is the thing
     that is supposed to nag *you*; here it gives up first and snoozes
     *itself*. The punchline "even my phone has boundaries now" lands
     as a sting of recognition — everyone has ignored an alarm.
   - Fresh angle: the obvious complaint is "my alarm is annoying / too
     loud / I sleep through it". Nobody frames the alarm as the party
     that sets a boundary and quits. The brief's own examples (phone
     dying at 4pm, rating prompt, kettle firmware) are deliberately
     avoided — this line copies none of them.
   - Neatly worded: 100 of 200 characters, one clause of setup
     ("snoozes itself after I ignore it three times") plus one
     punchline, timed by the em dash. No wasted words.
   - Specific gripe: "after I ignore it three times" is a concrete
     detail about how the thing actually behaves, not a generic moan.

2. Candidates considered (all original, written from scratch):
   A. Earbuds disconnecting outside, "need a minute alone before
      committing to the walk" (110 chars) — good comparison, but the
      commitment-issues joke is a familiar trope.
   B. Alarm snoozing itself, "even my phone has boundaries now"
      (100 chars) — CHOSEN: freshest reversal, tightest wording.
   C. Laptop fan screaming at a spreadsheet, "two columns too heavy
      to lift" (114 chars) — vivid, but "fan sounds like a jet" is
      the most common laptop complaint there is.

3. Optimisation: there is nothing to brute-force — the entry is one
   fixed string. The program is O(1) time and memory: it validates
   the constant (exactly one line, 1-200 characters, not only
   whitespace) and writes it verbatim, so the graded run is fully
   deterministic — byte-identical on every run.

4. Edge cases: the gate requires 1-200 UTF-8 characters and exactly
   one line. The program enforces that itself before writing: it
   rejects an empty/whitespace-only line, any embedded newline, and
   anything over 200 characters. The file is written with no trailing
   newline, so the byte count is exactly the line itself and no
   scorer can miscount a stray newline.

Run: python3 main.py  (writes /output/entry.txt)
"""

import os

LINE = "My alarm snoozes itself after I ignore it three times \u2014 apparently even my phone has boundaries now."

MAX_CHARS = 200


def main() -> None:
    if not LINE or not LINE.strip():
        raise SystemExit("entry line must not be empty or whitespace-only")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry line must be exactly one line")
    if len(LINE) > MAX_CHARS:
        raise SystemExit(f"entry line is {len(LINE)} chars, over the {MAX_CHARS} limit")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Re-read what was written: the graded file must be byte-identical
    # to the entry line, with no stray newline or truncation.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("written entry.txt does not match the entry line")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
