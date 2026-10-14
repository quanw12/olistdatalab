> Write the complete program yourself using exercise.md. The numbered steps below teach the syntax and logic.

# Day 1 cheat sheet

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Run the exercise</summary>

Open PowerShell in `C:\DE Courses\01-foundation\day-01`:

```powershell
python clean.py
```

If your terminal is in `C:\DE Courses`, use:

```powershell
Set-Location "C:\DE Courses\01-foundation\day-01"
python clean.py
```

</details>

<details>
<summary>Common problems</summary>

| Symptom | Common cause | What to check |
|---|---|---|
| `FileNotFoundError` | Wrong working folder | Use `Get-Location`, then run from `day-01` |
| `TypeError: cannot unpack...` | `clean_row` does not return two values | Every branch must return `(clean, reason)` |
| Error when using `clean[...]` | Accessing the result before checking `clean is None` | Handle rejected rows first |
| Empty output | `clean_row` always returns None, or rows are not appended | Print `raw_row`, then `clean` |
| Wrong accepted count | Checking duplicates before validity, or missing `continue` | Compare with the lesson's pseudocode |

Full syntax for TODOs 5–7 is in **section 8.1** of `lesson.md`.

</details>

<details>
<summary>Print values to debug</summary>

Temporarily add one of these inside the loop:

```python
print(raw_row)
print(clean, rejection_reason)
print(seen_keys)
```

Once you understand the problem, remove or comment out these prints to keep the output clear.

</details>

<details>
<summary>Basic Git commands</summary>

```powershell
Set-Location "C:\DE Courses"
git status
git add -- 01-foundation/day-01
git commit -m "feat: clean weather CSV"
git log --oneline
```

A commit saves a snapshot of changes with a description. You do not need branches, rebase, or pull requests today.

</details>

<details>
<summary>Building the driver when starting from a blank file</summary>

Define helper functions first; call them from main. A function definition does not execute its body. This small unrelated example shows the syntax:

~~~python
from pathlib import Path

def save_message(text):
    folder = Path("output")
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "message.txt").write_text(text, encoding="utf-8")

def main():
    save_message("Practice complete")

if __name__ == "__main__":
    main()
~~~

Read input inside main, pass data to your transformation, validate the result, then write output. Test one helper with a tiny input before connecting all steps. Use print(repr(value)) to inspect an unexpected value; remove temporary prints after debugging. Return data from helpers and print only at the CLI boundary.

For CSV use csv.DictReader/csv.DictWriter (or pandas read_csv/to_csv on Days4–5). For JSON use json.load/json.dump with an opened UTF-8 file. CSV writer files need newline="". JSON datetime values must become ISO strings before serialization. Catch the expected exception around the risky conversion; do not hide every error behind except Exception: pass.

</details>
