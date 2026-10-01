# Day 1 — Python foundations for a small data pipeline

## Learn before coding

Read these before opening `clean.py`:

1. [Lesson: from raw CSV to clean data](lesson.md)
2. [Help: commands and debugging](help.md)

You do not need to understand everything on the first reading. After each tutorial section, run a small example, then return to the exercise scaffold.

## Today's outcome

Turn a small, imperfect CSV file into a clean CSV and a short quality report.

You are not expected to know how to build a full system. Today's job is to learn the shape of one:

`raw file -> validate -> clean -> output + report`

## Time budget

About 2.5–3.5 hours. Stop after the required part if you get stuck; record the error instead of guessing.

## 1. Set up the project (15 min)

Open a terminal in `C:\DE Courses` and activate the project's existing Python environment:

```powershell
.\.venv\Scripts\Activate.ps1
python --version
git status
```

Do not create another `.venv` inside `day-01`; the whole course shares one environment in the root folder.

Create `.gitignore` containing:

```text
.venv/
__pycache__/
output/
```

## 2. Read the input by hand (15 min)

Open `weather.csv`. Before coding, write your predictions in `notes.txt`:

1. Which rows should be rejected?
2. What makes a row a duplicate?
3. Which values should be converted to numbers?

Use this data contract for the required part:

- A valid row has a non-empty `city` and a date in `YYYY-MM-DD` format.
- `temperature_c` must be a number from -50 to 60.
- `humidity_pct` must be an integer from 0 to 100.
- A duplicate means the same `city` and `observed_at`.
- If duplicates conflict, keep the first valid row and reject later rows.

## 3. Complete `clean.py` (90 min)

From `C:\DE Courses\day-01`, run the scaffold first:

```powershell
python clean.py
```

Then implement the TODOs in this order:

1. Read CSV with the standard-library `csv` module.
2. Validate and clean one row at a time with `clean_row`.
3. Reject invalid rows with a useful reason.
4. Track duplicate keys with a `set`.
5. Write valid rows to `output/clean.csv`.
6. Print accepted/rejected counts and rejection reasons.

Do not use pandas today. Practise ordinary Python: functions, dictionaries, loops, conditionals, exceptions, and files.

## 4. Verify it (25 min)

Your program must report:

- `accepted: 5`
- `rejected: 5`
- Exactly one duplicate

Open the clean output and check for five data rows, no duplicate `(city, observed_at)` pair, and consistently formatted numbers.

## 5. Git checkpoint (15 min)

From the `day-01` folder:

```powershell
git add guide.md lesson.md help.md weather.csv clean.py notes.txt
git commit -m "feat: add weather CSV cleaning exercise"
git log --oneline
```

## Optional stretch (30 min)

Add an `--input` argument with `argparse`, so this works:

```powershell
python clean.py --input weather.csv
```

## What to send after finishing

1. Your program's final report.
2. Any error that blocked you, verbatim.
3. One sentence: which part felt least clear?

I will review the result and use the unclear parts to shape your Day 2 lesson.
