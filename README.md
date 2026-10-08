# Personal Mini-Toolkit

## What it does

A menu-driven Python program with four tools. The menu comes back after every tool until you choose Quit.

1. **To-Do List** - add, show and remove tasks from a list that changes while the program runs.
2. **Number Guessing Game** - guess a secret number from 1 to 20 in 5 tries, with "too low" / "too high" hints.
3. **Simple Calculator** - add, subtract, multiply or divide two numbers without crashing on bad input.
4. **Name Formatter** - shows a name in Title Case, UPPER CASE, with initials and a letter count.

## Files

- `toolkit_plan.txt` - my plan: the tools, the menu text and the concepts each tool uses.
- `toolkit.py` - the finished toolkit program.
- `screenshots/` - screenshots of the menu (including an invalid choice) and each tool running.

## How to run it

```bash
python3 toolkit.py
```

Type the number of a tool and press Enter. Choose `5` to quit.

## Reflection

The hardest part was keeping each tool separate while still sharing one menu loop. The bug that took longest to fix was in the guessing game: bad input like letters crashed the program until I added `try` / `except` and `continue`, so a bad guess no longer used up a try. I also had to decide where the to-do list should live, because creating it inside the tool made it reset every time I returned to the menu. Planning in `toolkit_plan.txt` first made the build much faster. With one more week I would save the to-do list to a file, add a high-score tracker to the guessing game, and let the calculator keep a history of past answers.