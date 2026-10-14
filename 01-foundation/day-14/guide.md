# Day 14 — Mini-project 2: a reusable loader and SQL mart

**Difficulty: Integrate.** 45–120 minutes; split across sessions if needed. Syntax documentation is allowed; keep approach hints closed until you try.

Complete the core task before any optional extension.

## Before starting

Complete Day 13. Work in capstone from now on unless a guide specifies another directory.

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
python -m weather_pipeline --help
python -m weather_pipeline load --input ../data/weather_batch.json
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
git add -- 01-foundation/day-14
git diff --cached --stat
git commit -m "feat(day-14): complete the daily DE exercise"
git push origin main
~~~

Generated output stays ignored; put selected evidence in `evidence/` when a guide asks for it.



[Course index](../README.md) · [Lesson index](../lessons.md)


## Independent variation

Run from another current directory and replace the input path with a new fixture. Prove the package, not the shell location, determines its behavior.
Record the input, predicted result and actual evidence in notes.md. Do not change the supplied fixture/checker.
