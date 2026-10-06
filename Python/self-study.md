# Study this course without Codex

All teaching text, exercise prompts, hints, fixed inputs and local checking scripts are stored in this repository. They remain readable in your editor without an active Codex subscription. External videos/documentation and installing packages need internet access; the supplied offline checks need no model or API account once setup is complete.

## Choose your starting point

- If functions, loops or dictionaries still feel uncertain: start at [C01-L01](01-fundamentals/01-run-print/guide.md) and follow Chapters 1–8.
- If you can independently finish [the weather mini-project](08-functions/06-clean-functions/guide.md), continue at [C09-L01](09-errors-and-types/01-exceptions/guide.md).
- Finish the [extension setup](de-setup.md) before running Chapters 9–14. Do not skip straight to the final pipeline.

There are 56 lesson units, not 56 fixed calendar days. A small lesson may fit one session; parsing, databases and the capstone may take several. Keep your existing 30-day foundation course as a separate tool-introduction track.

## One repeatable study cycle

1. Read guide.md. Name the new skill and prerequisite in your own words.
2. Read lesson.md. Before running its example, write down the values you expect at each step.
3. Put the example in scratch.py and experiment. Change one input at a time.
4. Close the example and implement the contract in exercise.py. Start with one simple valid input.
5. If stuck for about 15–20 minutes, reveal one hint in help.md. Draw the data flow or trace a single row before writing more code.
6. Check normal, empty, boundary and malformed inputs.
7. Explain why the result is correct; answer the reflection before revealing its key where supplied.
8. Review your diff, update progress.md and use the guide's commit commands.

Do not copy the same finished function repeatedly and count that as practice. On the following day, rebuild one important part with a different small fixture.

## What each file does

| File | Use |
|---|---|
| guide.md | Entry point: study order, exact run commands and commit commands |
| lesson.md | Concepts, relevant syntax, an example and a trace |
| exercise.py | Your implementation space; initially problem statements only |
| help.md | Gradually stronger hints and troubleshooting |
| expected.md | Output examples, edge cases and reflection checking |
| check.py | Provided automated checker in Chapters 9–14 |
| contract.md | Detailed capstone specification and demonstration checklist |
| data/ at course root | Shared, fixed retail fixtures with documented meaning |

Chapters 1–8 use manual expected-output and edge-case checks. Chapters 9–14 additionally have 21 executable checkers and collapsible reflection answer keys. Passing a checker covers its supplied cases; it does not prove every possible input or your understanding.

The active exercise file never contains an instructor's completed solution. Learn from the teaching example and the detailed hint sequence, then implement your own program.

## Read a failure systematically

- SyntaxError/IndentationError: fix the highlighted structure first; no later logic can run yet.
- AttributeError mentioning a missing function: compare the requested name and your definition.
- TypeError: print or inspect the actual type at the failing boundary.
- ValueError: decide whether the input should be rejected or your conversion rule is incorrect.
- AssertionError: inspect the expected condition in check.py and reproduce that exact input in scratch.py.
- A blank assertion message still has a traceback location. Open that line and examine the assertion.

Do not change check.py or hard-code its fixture outputs to get PASS. Reduce the failure to one record. Check what goes into a function, what it returns, and whether it changes input objects unexpectedly. Remove temporary prints from functions whose contracts require silence.

Example debugging notes:

~~~text
Lesson:
Exact command:
Expected:
Actual result / final traceback line:
Smallest input that reproduces it:
What each variable contains:
Hypothesis:
One change to test:
What happened:
~~~

Use the relevant linked official documentation if a behavior remains unclear. If you later ask a teacher or assistant, these notes make the question precise.

## Chapter gates

| After | Demonstrate without reading a solution |
|---|---|
| 03 | Convert and format values while explaining numeric limits |
| 06 | Trace a loop and choose break/continue/return appropriately |
| 08 | Build a small validator and grouped report from functions |
| 10 | Read files, reject malformed rows, preserve money and timezone meaning |
| 11 | Import code safely, run a CLI and write tests that catch wrong behavior |
| 12 | Process chunks and prevent a join from multiplying totals |
| 13 | Bound API work and prove batch rollback/replay behavior |
| 14 | Demonstrate corrections, replay, conflicts and output recovery |

For PostgreSQL, record offline-check and live-lab results separately. The offline fake connection cannot prove actual SQL execution on your server.

## Keep evidence and prepare for review

Add notes.md beside each exercise: one concept explanation, one bug and its fix, one extra case, and 3–5 useful English terms. Mark a progress box only after solving and explaining the task.

At the capstone, write portfolio.md using its rehearsal checklist. Record commands, counts, screenshots if useful, and limitations. Include one failure-and-recovery demonstration. A trustworthy small project is better evidence than an unexplained large one.

Review all staged files before committing: Git commits everything already staged, even if this lesson's command stages only one folder. Use your existing feature/... branch convention. No lesson requires uploading credentials or generated environment files.

## AI is optional

If you still have access to any assistant, ask for a hint, a variable trace or additional edge cases. Verify every suggestion locally. Never paste a database password, private records or an .env file. Try to reproduce the key function yourself afterward. Every required exercise in this course can be completed without an LLM call.

## Coverage limits

This course prepares core Python programming and a practical DE workflow. It does not claim mastery of all Python, advanced asynchronous systems, distributed Spark internals, cloud operations, every SQL topic or interview readiness by itself.

After the capstone, use the [internship roadmap](../intern-prep/roadmap.md) to deepen SQL, modeling and deployment. Its future tracks are plans unless they link to prepared lessons. Use the existing [30-day foundation](../de-30-days/README.md) for the scheduled tool introductions.
