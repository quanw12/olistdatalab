# C13-L01 — HTTP responses, pagination, and bounded extraction

**Difficulty: Apply.** 45–120 minutes of coding/checking; environment setup may take longer. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Chapter](../README.md) · [Extension setup](../../de-setup.md) · [Study without Codex](../../../docs/study.md)

[Previous lesson](../../12-data-processing/03-parquet/guide.md) · [Next lesson](../02-retries/guide.md)

## Study order

Finish earlier lessons first. Uses only the standard library. These are original DE extensions, not additional video chapters.

1. Read [lesson.md](lesson.md), predict its example, and try it in scratch.py.
2. Implement the exact contracts in [exercise.py](exercise.py). Put demonstrations under a main guard.
3. Read [help.md](help.md) progressively when stuck.
4. Run:

~~~powershell
Set-Location "C:\DE Courses\02-python\13-apis-and-databases\01-pagination"
& "C:\DE Courses\.venv-python-de\Scripts\python.exe" .\check.py
~~~

5. Correct the first failure, rerun, and compare [expected.md](expected.md).
6. Answer the reflection before revealing its answer, then mark [progress](../../progress.md).

check.py is provided checking infrastructure. Missing functions are expected initially. Do not edit the checker to pass. Checks cover the stated contract; they are not a production certification.

## Commit completed work

~~~powershell
Set-Location "C:\DE Courses"
git status
git add -- "02-python/13-apis-and-databases/01-pagination"
git diff --cached --stat
git diff --cached
git commit -m "feat(python): complete c13-l01 pagination"
git push origin main
~~~

Commit on `main` and inspect previously staged changes too.


## Independent variation

Use a repeated continuation token and a sequence exceeding max_pages. Prove no extra request is made; separately reject a malformed next value.
Record the input, predicted result and actual evidence in notes.md. Do not change the supplied fixture/checker.
