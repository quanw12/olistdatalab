# C14-L01 — Incremental state, replays, and corrections

[Chapter](../README.md) · [Extension setup](../../de-setup.md) · [Study without Codex](../../self-study.md)

[Previous lesson](../../13-apis-and-databases/04-postgresql/guide.md) · [Next lesson](../../14-reliable-pipelines/02-data-quality/guide.md)

## Study order

Finish earlier lessons first. Uses only the standard library. These are original DE extensions, not additional video chapters.

1. Read [lesson.md](lesson.md), predict its example, and try it in scratch.py.
2. Implement the exact contracts in [exercise.py](exercise.py). Put demonstrations under a main guard.
3. Read [help.md](help.md) progressively when stuck.
4. Run:

~~~powershell
Set-Location "C:\DE Courses\Python\14-reliable-pipelines\01-incremental"
& "C:\DE Courses\.venv-python-de\Scripts\python.exe" .\check.py
~~~

5. Correct the first failure, rerun, and compare [expected.md](expected.md).
6. Answer the reflection before revealing its answer, then mark [progress](../../progress.md).

check.py is provided checking infrastructure. Missing functions are expected initially. Do not edit the checker to pass. Checks cover the stated contract; they are not a production certification.

## Commit completed work

~~~powershell
Set-Location "C:\DE Courses"
git status
git add -- "Python/14-reliable-pipelines/01-incremental"
git diff --cached --stat
git diff --cached
git commit -m "feat(python): complete c14-l01 incremental"
git push -u origin HEAD
~~~

Keep your feature/... convention and inspect previously staged changes too.
