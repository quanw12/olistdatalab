# Day 1 cheat sheet

## Run the exercise

Open PowerShell in `C:\DE Courses\day-01`:

```powershell
python clean.py
```

If your terminal is in `C:\DE Courses`, use:

```powershell
python .\day-01\clean.py
```

## Common problems

| Symptom | Common cause | What to check |
|---|---|---|
| `FileNotFoundError` | Wrong working folder | Use `Get-Location`, then run from `day-01` |
| `TypeError: cannot unpack...` | `clean_row` does not return two values | Every branch must return `(clean, reason)` |
| Error when using `clean[...]` | Accessing the result before checking `clean is None` | Handle rejected rows first |
| Empty output | `clean_row` always returns None, or rows are not appended | Print `raw_row`, then `clean` |
| Wrong accepted count | Checking duplicates before validity, or missing `continue` | Compare with the lesson's pseudocode |

Full syntax for TODOs 5–7 is in **section 8.1** of `lesson.md`.

## Print values to debug

Temporarily add one of these inside the loop:

```python
print(raw_row)
print(clean, rejection_reason)
print(seen_keys)
```

Once you understand the problem, remove or comment out these prints to keep the output clear.

## Basic Git commands

```powershell
git status
git add .
git commit -m "feat: clean weather CSV"
git log --oneline
```

A commit saves a snapshot of changes with a description. You do not need branches, rebase, or pull requests today.
