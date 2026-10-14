# C12-L02 — pandas joins, types, and trustworthy totals

**Difficulty: Apply.** 45–120 minutes of coding/checking; environment setup may take longer. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Chapter](../README.md) · [Extension setup](../../de-setup.md) · [Study without Codex](../../../docs/study.md)

[Previous lesson](../01-generators/guide.md) · [Next lesson](../03-parquet/guide.md)

## Study order

Finish earlier lessons first. Requires pandas from requirements-de.txt. These are original DE extensions, not additional video chapters.

1. Read [lesson.md](lesson.md), predict its example, and try it in scratch.py.
2. Implement the exact contracts in [exercise.py](exercise.py). Put demonstrations under a main guard.
3. Read [help.md](help.md) progressively when stuck.
4. Run:

~~~powershell
Set-Location "C:\DE Courses\02-python\12-data-processing\02-pandas"
& "C:\DE Courses\.venv-python-de\Scripts\python.exe" .\check.py
~~~

5. Correct the first failure, rerun, and compare [expected.md](expected.md).
6. Answer the reflection before revealing its answer, then mark [progress](../../progress.md).

check.py is provided checking infrastructure. Missing functions are expected initially. Do not edit the checker to pass. Checks cover the stated contract; they are not a production certification.

## Commit completed work

~~~powershell
Set-Location "C:\DE Courses"
git status
git add -- "02-python/12-data-processing/02-pandas"
git diff --cached --stat
git diff --cached
git commit -m "feat(python): complete c12-l02 pandas"
git push origin main
~~~

Commit on `main` and inspect previously staged changes too.


## Independent variation

Add a duplicate dimension key, then an unmatched fact key in separate fixtures. Require explicit failure instead of inflated or silently missing totals.
Record the input, predicted result and actual evidence in notes.md. Do not change the supplied fixture/checker.
