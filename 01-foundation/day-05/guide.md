# Day 05 — Join and aggregate with pandas

**Difficulty: Learn.** 15–45 minutes of coding; allow extra time for first setup. Syntax documentation is allowed; keep approach hints closed until you try.

Complete the core task before any optional extension.

## Before starting

Read [setup](../setup.md) if your environment or current directory is unclear. Inputs are supplied; implementation belongs to you. A comment-only code file does nothing until you implement it.

## Study order

1. Read [lesson.md](lesson.md), about 35–50 minutes. Type each small syntax example and predict its output.
2. Read [exercise.md](exercise.md). Identify inputs, outputs, and failure behavior before writing code.
3. Implement one small step at a time, about 90–120 minutes. Exercise files contain problem statements only.
4. Use [help.md](help.md) for the step you are stuck on; return to your own implementation after reading it.
5. Compare with [expected.md](expected.md), about 20–30 minutes. Keep your evidence and write reflection.md.
6. Review the diff and use the Git checkpoint below, about 10 minutes.

## Run after implementing

Install pandas for Days4–5: `python -m pip install "pandas>=2.2,<3"`.

~~~powershell
Set-Location "C:\DE Courses\01-foundation\day-05"
python summary.py
~~~

Commands above describe the interface you will build; supplied starters are deliberately unfinished. SQL lessons use pgAdmin as described in the lesson. Keep full error messages if a step fails.

## Send for review

Send the command output or query result, the files you changed, any error, and your reflection answers. You may simply ask me to read your files. Explain the result in your own words before committing.

## Git checkpoint

Work on `main`. Stage only this lesson (plus shared project files you changed on purpose).

~~~powershell
Set-Location "C:\DE Courses"
git checkout main
git pull origin main
git status
git add -- 01-foundation/day-05
git diff --cached --stat
git commit -m "feat(day-05): complete the daily DE exercise"
git push origin main
~~~

Generated output stays ignored; put selected evidence in `evidence/` when a guide asks for it.



[Course index](../README.md) · [Lesson index](../lessons.md)
