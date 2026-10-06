# DE internship preparation

Start with [the detailed roadmap](roadmap.md), then use [the material checklist](materials.md) to choose a teacher or course.

## Recommended first subject

**Practical Python: from understanding examples to writing a complete small program independently.** Keep SQL practice alongside it.

You previously said you understand some Python/SQL logic but still struggle with Python syntax, functions, and building a whole program yourself. That is the reason for this recommendation. It is a personalized starting point, not a universal rule that Python always comes before SQL.

You selected Data With Baraa's Python video. The [Python companion course](../Python/README.md) now follows its eight chapters through 35 focused lessons. It covers core values, control flow, collections and functions, with additional practice on difficult topics. The course also includes 21 original DE extension lessons in Chapters 9–14, bringing it to 56 lessons. They cover errors, files, dates, tests, pandas/Parquet, APIs, databases and a reliable retail pipeline. Follow the [independent-study guide](../Python/self-study.md).

## Learning order

| Order | Track | What you should be able to do |
|---|---|---|
| 1 | Python | Build, debug, and test a small file-processing program |
| 2 | SQL | Answer unfamiliar business questions without losing or duplicating rows |
| 3 | PostgreSQL and modeling | Design a defensible schema and load data safely |
| 4 | Reliable pipelines | Handle bad data, retries, reruns, corrections, and recovery |
| 5 | Delivery and platforms | Run and explain a reproducible pipeline with one selected platform stack |
| 6 | Internship rehearsal | Solve a new assignment and explain the result in an interview |

Git, tests, debugging, and short English explanations recur throughout. Do not wait until Track 5 to practise them.

Start with approximately 60% Python, 30% SQL, and 10% review/Git/documentation. This is a suggested study allocation, not a hiring statistic. Rebalance after the Python diagnostic in the roadmap.

## Relationship to the 30-day course

The [foundation course](../de-30-days/README.md) is prepared through Day 30. Preparation of those files does not mean you have completed those lessons. The recorded course position was Day 12, with unfinished work saved in the stash described in the [workspace README](../README.md).

Use that course for the first guided exposure to tools. Use this roadmap for deeper practice and transfer to unfamiliar data. You can strengthen Python now; later foundation lessons provide context for the pipeline/platform tracks. Avoid taking two full workloads at once.

This folder holds the roadmap and material-selection process. The selected Python lessons are in the separate top-level Python folder. Lesson preparation does not mark learning targets complete; exercise implementations are left for you.

## Start here

1. Start at [Python C01-L01](../Python/01-fundamentals/01-run-print/guide.md).
2. Follow the selected video's chapter order and the companion lesson splits.
3. Work through guide → lesson → exercise → help when needed → expected results → reflection and commit.
4. Use the [Python progress checklist](../Python/progress.md) to record demonstrated learning.
5. Use [materials.md](materials.md) later when choosing additional depth or SQL sources.

One lesson has one main learning target and may take more than one study session. The current course uses chapter/lesson folders; it is not a fixed 56-calendar-day commitment.

## Save this roadmap

The existing curriculum is already committed. These commands stage only this new roadmap and its workspace link. Review the staged changes before committing.

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- README.md intern-prep
git diff --cached --stat
git diff --cached
git commit -m "docs(roadmap): plan deeper DE internship preparation"
git push -u origin HEAD
~~~

The current branch when this roadmap was prepared is feature/de-30-day-course. These commands do not create or rename a branch. If you choose a separate branch, use your feature/... naming convention.
