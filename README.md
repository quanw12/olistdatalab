# Data Engineering Course

A workspace for learning Data Engineering one day at a time. The learning materials are in English so you can practise technical English while studying.

## Where to start

1. Read the [30-day roadmap](roadmap.md).
2. Use the [learning resources](resources.md) to choose the relevant reading for each stage.
3. Work on the earliest day you have not completed.
4. Save notes, errors, and results in that day's folder.

## Structure

```text
roadmap.md   # The full month's learning plan
resources.md # Selected resources for each stage
day-01/      # Day 1 lessons, data, and code
day-02/      # Python: functions, lists, sets, and dictionaries
day-03/      # JSON, datetime, configuration, and logs
day-04/      # pandas: cleaning whole columns
day-05/      # pandas: merge, groupby, and result checks
day-06/      # CLI, environment variables, and HTTP APIs
day-07/      # Mini-project 1: raw JSON to a clean weather record
day-08/      # PostgreSQL with pgAdmin 4: tables, keys, and constraints
day-09/      # SQL: SELECT, WHERE, JOIN, GROUP BY, and ten query exercises
...
```

For each day, follow **guide.md → lesson.md → exercise**, opening **help.md** when you need a hint. Day 7 also has a project README.

New days will be added directly to this project with practice data, code scaffolds, and instructions.

## Convention for future lesson guides

Every new day's `guide.md` must include a **Git checkpoint** with ready-to-run PowerShell commands: move to `C:\DE Courses`, inspect `git status`, stage the relevant lesson files, commit with a meaningful message, and push. Specify the working folder and use paths appropriate to that day. Check the current branch and its upstream; include `git push -u origin <actual-branch-name>` when no upstream is configured. The learner runs these commands after completing and reviewing the exercise.
