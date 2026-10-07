# DE27 — Discover a source before building its pipeline

**Difficulty: Apply.** Allow 2–3 hours. Prerequisites: Python files/time, DE02, DE04 and DE23.

[Module](../README.md) · [Previous: DE26](../04-unseen-assignment/guide.md)

1. Read [lesson.md](lesson.md), then inspect [the source](fixtures/source.csv).
2. Attempt [exercise.md](exercise.md). List observations and questions before opening the source owner's clarification.
3. Implement [profile.py](profile.py). Use [help.md](help.md) only after an attempt.
4. Run the checker, write the catalog/lineage handoff, then compare [expected.md](expected.md).
5. Record evidence and highest hint used in [notes.md](notes.md).

## Run — PowerShell

~~~powershell
Set-Location "C:\DE Courses\04-data-engineering\07-internship\05-source-discovery"
python .\check.py
python .\profile.py --input .\fixtures\source.csv --output .\output\profile.json
~~~

The starter is intentionally unfinished. The checker also uses empty, changed and
malformed sources and runs your CLI from another directory. Profiling does not
decide an unconfirmed production cleaning policy.

## Commit after verification

Use your current feature/... branch. Review previously staged work too.

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "04-data-engineering/07-internship/05-source-discovery"
git diff --cached
git commit -m "feat(engineering): complete de27 source discovery"
git push -u origin HEAD
~~~

[Next: DE28](../06-backup-and-restore/guide.md)
