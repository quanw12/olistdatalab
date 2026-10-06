# Choosing teachers and supplying materials

Use this file when selecting additional sources. You have selected [Data With Baraa's Python video](https://www.youtube.com/watch?v=Rq5gJVxz55Q); [the companion course](../Python/README.md) is now prepared. Its [source notes](../Python/sources.md) distinguish the verified outline from original supplementary explanations. The course now also includes 21 original DE extensions. The checklist remains useful for additional depth and SQL.

## Criteria for future Python sources

**Subject: practical beginner-to-intermediate Python programming.**

You know some coding logic but need to understand syntax and independently build a small program. The selected companion course now covers the core language targets in [the roadmap](roadmap.md). Use these criteria when choosing extra explanations or more advanced practice after the prepared files, debugging, modules and testing lessons.

A useful brief to send a teacher:

> I am an Information Systems student preparing for a Data Engineering internship. I understand basic code logic but cannot yet independently write a complete Python program. I need step-by-step explanations of types, control flow, collections, functions, files, exceptions, modules and tests. Please include independent exercises, code review, and a small CSV/JSON project. I want to understand and debug my own code before adding data engineering frameworks.

Suggested search phrases:
- Python beginner functions exercises
- Python programming file handling testing
- Python collections debugging course
- SQL PostgreSQL joins window exercises — for the parallel SQL track

Keep Baraa's video as the main fundamentals course, then follow the prepared DE extensions. Choose additional sources for demonstrated gaps rather than restarting the same beginner content.

## Evaluate a sample before choosing

| Criterion | What to inspect |
|---|---|
| Beginner fit | Explains assignment, indentation, return values and collection operations rather than assuming you already know them |
| Execution reasoning | Traces values through branches/loops/functions and explains why a solution works |
| Independent practice | Has tasks before solutions, with feedback or a way to check your answer |
| Debugging | Teaches reading errors and repairing deliberately broken code |
| Data edge cases | Covers empty input, missing fields, malformed values and duplicates |
| Complete programs | Builds from smaller functions toward a runnable program with files and clear output |
| Engineering habits | Includes imports, environments, useful tests and readable structure |
| Accessible sources | You can provide the exact chapter, notes/transcript, examples and exercise requirements |
| Suitable syntax | The Python version and dependencies are identified; examples can be adapted to your environment |
| Review quality | Feedback addresses logic and correctness rather than only checking that code runs |

A teacher can use Vietnamese explanations if that helps understanding; our generated study documents remain in English. Prefer English notes/subtitles when they are clear enough to support your parallel language practice.

Avoid a first Python course that immediately builds framework-heavy applications without explaining functions and collections. OOP can be taught later through small examples; elaborate class hierarchies are not the initial objective.

For the later SQL teacher, specifically inspect join cardinality, NULL handling, window-function ties/frames, and exercises with expected results. PostgreSQL-compatible examples are preferable for your existing setup.

## Syllabus benchmarks and references

These are comparison/reference sources, not a requirement to choose a particular teacher.

- [CS50P](https://cs50.harvard.edu/python/): beginner Python with functions, control flow, exceptions, libraries, tests, file I/O and later OOP. Compare your candidate's practical coverage against this syllabus.
- [Python 3.13 tutorial](https://docs.python.org/3.13/tutorial/): language reference while studying; it assumes basic programming knowledge and should not be your only beginner instruction.
- [PostgreSQL tutorial](https://www.postgresql.org/docs/18/tutorial.html): reference for SQL and relational database exercises.
- [PostgreSQL EXPLAIN guide](https://www.postgresql.org/docs/18/using-explain.html): reference when query-plan lessons begin.
- [roadmap.sh Data Engineer](https://roadmap.sh/data-engineer): broad topic map; use it for long-term coverage rather than treating every box as an immediate prerequisite.

References were inspected during planning on October 6, 2026. Installation/version-specific teaching will be checked again when preparing the relevant lessons.

## What to send

Start with one or two chapters or a manageable video segment covering PY01–PY04. A course title alone lets us review its syllabus, but does not reveal the content of inaccessible lessons.

Copy and fill this template:

~~~text
Track/topic IDs: Python — PY01–PY04
Teacher/course title:
Source URL or local file path:
Exact chapters/pages/video timestamps:
Notes or transcript available:
Example code and exercise/data files available:
Language and Python version, if stated:
Study time available per day/week:
What I already understand:
What currently confuses me:
Preferred first chapter:
~~~

Include the chapters or notes you are allowed to share. If a video, login-protected lesson, or file cannot be accessed, provide the relevant transcript/notes or an accessible file. We will identify missing material explicitly rather than claim to have reviewed it.

If choosing between two teachers, send both syllabuses and one sample lesson from each. We can compare them against the checklist before you commit substantial time.

## How supplied material becomes lessons

1. Inspect the actual content and map it to roadmap IDs.
2. State what it covers, assumes, omits, or conflicts with your environment.
3. Pick a small lesson sequence; split a long chapter when it contains several new concepts.
4. Explain concepts and syntax before the exercise, using small traced examples.
5. Create original exercises that require transfer, with fixed fixtures and checkable outputs.
6. Provide graded hints and a debugging path in help, separate from active exercise code.
7. Review your submission and explanation before marking the capability demonstrated.

Source material guides the sequence; we do not reproduce entire copyrighted courses. The lesson identifies the relevant source chapter and any added explanation. Missing coverage becomes a clearly labeled supplementary lesson.

## Lesson folder layout

The roadmap files stay here. The selected Python course uses the top-level Python folder and the video's chapter organization:

~~~text
Python/
  README.md
  setup.md
  sources.md
  progress.md
  01-fundamentals/
    01-run-print/
      guide.md
      lesson.md
      exercise.py
      help.md
      expected.md
  ...
  08-functions/
~~~

Current IDs use chapter and lesson, such as C01-L01, to distinguish this course from foundation Day 01. Guides identify roadmap topics and video windows. Future tracks can use the same small lesson-file pattern, with queries.sql for SQL and a data folder only when needed. Paths and run commands are explicit.

File purposes:
- **guide.md:** prerequisites, order, exact setup/run commands, completion checklist, reflection and commit/push commands.
- **lesson.md:** definitions, why the concept matters, syntax, traced examples and source references.
- **exercise.py / queries.sql:** problem requirements and TODO prompts. Your implementation remains yours.
- **help.md:** progressively stronger hints, relevant syntax and small examples; detailed reasoning separately from the exercise.
- **expected.md:** fixed-fixture outputs, edge cases and how to check them. It does not prefill the implementation.
- **data/:** small inputs with a documented meaning and stable expected results.

If a lesson is conceptual, use exercise.md instead of an artificial code file. Setup SQL, fixtures, or test harnesses may be supplied fully when necessary, but they must be labeled as provided infrastructure. Preserve your submitted code when reviewing or reorganizing.

## Study routine

For each lesson:
1. Read/watch the selected section and write a short explanation in your own words.
2. Trace one example manually and predict the result.
3. Close the example and solve the task yourself.
4. If stuck, read the first hint; ask a precise question with the error and your current reasoning.
5. Test normal and edge cases, explain a function/query, and review the diff.
6. Commit using the guide's commands after completion.

Record useful English terms in the lesson reflection, with a short example. Completion means you can reproduce and explain the important part, not that you watched the video.

## Next handover

Begin [Python C01-L01](../Python/01-fundamentals/01-run-print/guide.md). For a future extension or SQL track, send the selected source and chapters using the template above. You do not need to choose the Python teacher again.
