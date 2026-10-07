# Day 26 — Continuous integration with GitHub Actions

**Difficulty: Integrate.** 2–6 hours across several sessions. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

Complete the core task before any optional extension.

## Before starting

Finish the preceding lesson and use the shared Python environment from setup.md.

Read [setup](../setup.md) if your environment or current directory is unclear. Inputs are supplied; implementation belongs to you. A comment-only code file does nothing until you implement it.

## Study order

1. Read [lesson.md](lesson.md), about 35–50 minutes. Type each small syntax example and predict its output.
2. Read [exercise.md](exercise.md). Identify inputs, outputs, and failure behavior before writing code.
3. Implement one small step at a time, about 90–120 minutes. Exercise files contain problem statements only.
4. Use [help.md](help.md) for the step you are stuck on; return to your own implementation after reading it.
5. Compare with [expected.md](expected.md), about 20–30 minutes. Keep your evidence and write reflection.md.
6. Review the diff and use the Git checkpoint below, about 10 minutes.

## Run after implementing


~~~powershell
Set-Location "C:\DE Courses\01-foundation\capstone"
python -m pytest -m "not integration" -q
# Also stage .github/workflows/ci.yml from repository root before committing.

~~~

Commands above describe the interface you will build; supplied starters are deliberately unfinished. SQL lessons use pgAdmin as described in the lesson. Keep full error messages if a step fails.

## Send for review

Send the command output or query result, the files you changed, any error, and your reflection answers. You may simply ask me to read your files. Explain the result in your own words before committing.

## Git checkpoint

Run this only after checking your result. Review what is staged; do not commit passwords or the .env file. Stay on your current feature branch. If starting a later study session from an updated main branch, you may first create feature/day26; do not recreate an existing branch.

~~~powershell
Set-Location "C:\DE Courses"
git status
git add -- 01-foundation/day-26 01-foundation/capstone .github/workflows/ci.yml
git diff --cached --stat
git commit -m "feat(day-26): complete the daily DE exercise"
$lessonBranch = git branch --show-current
git push -u origin $lessonBranch
~~~

The curriculum itself must be committed first using the repository README's commands. These daily commands stage only today's work and shared project changes. Generated output remains ignored; selected sanitized evidence belongs in evidence/.


[Course index](../README.md) · [Lesson index](../lessons.md)
