# How to study

[Home](../README.md) · [Roadmap](../roadmap.md) · [Lesson references](lesson-references.md) · [Assessments](assessment.md)

Use one main course at a time, in the roadmap's order. The materials, hints, fixtures and checkers are local; you can continue without a Codex subscription. Video/documentation, package installation and live services need the relevant internet/environment setup.

## One lesson, one cycle

1. Open **guide.md** and name the observable goal. Confirm the required shell and interpreter.
2. Read **lesson.md**. Predict a small example before running it in a scratch file.
3. Read the assignment and implement its first small case yourself. Close the teaching example while writing.
4. When stuck after a concrete attempt, open one hint in **help.md**. Trace a row/value before adding more code.
5. Run the guide's check or collect the requested observations. Preserve a useful error instead of hiding it.
6. Try one changed input and one failure/boundary case. Explain why the result is correct.
7. Answer the reflection, then reveal its explanation where provided. Write short notes, review your diff, update progress and commit using the guide.

A focused block can be 60–90 minutes. A lesson or integration can span several blocks. If most hints were needed, count it as guided practice and repeat a small variation independently later. In DE26, finish the diagnostic before seeking implementation help; using it early makes the attempt practice rather than an independent assessment.


## Difficulty and hints

| Level | Work expected | Help |
|---|---|---|
| Learn | Small syntax/concept drill; first setup may take longer. | Toy example and documentation. Group familiar drills after a changed-case check. |
| Apply | Choose logic for a specified contract and handle failures. | Attempt first, then one closed hint at a time. |
| Integrate | Connect boundaries; demonstrate durable/recoverable behavior. | Documentation and focused questions; stronger plans after effort. |
| Assess | Transfer to unfamiliar work or rehearse independent delivery. | Syntax references allowed; approach help only after the attempt ends. |

Pace excludes some installation/service troubleshooting. Inputs, required names/
types, failure rules and acceptance criteria are visible task contracts, not hidden
hints. Setup/run commands remain visible. A short drill does not certify mastery.

Try for 15–25 focused minutes after identifying an obstacle before revealing an
approach. Do not guess an undocumented function for an hour: use its API reference
immediately. Record highest help used: none / syntax pointer / approach / walkthrough.
After a walkthrough, repeat a changed case independently.

Worked results/reflection explanations are closed until the first attempt. A
Markdown preview supports expandable details; the raw editor still shows contents.
Stop before reading a section you have not chosen to reveal.

## What the files mean

| File | Purpose |
|---|---|
| Course README.md | Course scope and lesson/module index |
| guide.md | Lesson entry point, order, verification and manual commit commands |
| lesson.md | Concepts, syntax and a small teaching example |
| exercise.md / named starter | Task contract / your implementation space |
| help.md | Hints, approach and troubleshooting |
| expected.md | Results, edge cases and explanations to compare after attempting |
| check.py / checks/ | Supplied executable checks where available |
| contract.md | Larger project's interfaces and acceptance criteria |
| progress.md | Your demonstrated completion, not the author's preparation status |
| sources.md | Source provenance and verification limits |

The files inside a lesson belong together. Some early Python lessons use exercise.py as the task itself and do not need a separate exercise.md. Prompt starters intentionally do nothing until you implement them. Supplied app/setup/check files are infrastructure; their presence is not a completed learner solution.

## Diagnose a failure

Check **shell → working directory → path → interpreter → arguments → status/traceback → external resource → data/logic**. Test one explanation at a time with a small input that can distinguish it from another explanation.

| Symptom | First check |
|---|---|
| SyntaxError / IndentationError | Highlighted structure; later logic cannot run yet |
| Missing function / AttributeError | Exact contract name and imported file |
| TypeError | Actual types at the failing boundary |
| ValueError | Whether the input should be rejected or the conversion is wrong |
| AssertionError / wrong total | Reproduce the failing case; trace cardinality, filters and state |
| Missing module | Interpreter/venv selected by the exact command |
| Connection / daemon / port error | Correct host, service and environment before changing data logic |
| Old output after a failed run | File ownership, run time and whether publication occurred |

Keep a short error journal in the lesson's notes.md:

~~~text
Lesson and goal:
Shell / interpreter / working directory:
Exact command:
Expected behavior:
Actual result and useful error:
Smallest reproduction:
Hypothesis and distinguishing check:
One change:
Verification after the change:
Remaining limitation:
~~~

For code, use a tiny regression test and the debugger; DE03 teaches both. For SQL, count rows before/after a join and calculate a tiny expected result by hand. Return to the lesson's linked documentation for the specific question you cannot resolve.

## What counts as evidence

An offline checker proves its cases on the interpreter used. Add changed-input evidence; do not hard-code totals or weaken checks. An untouched starter is expected to fail. A syntax check alone does not prove Linux permissions, PostgreSQL rollback, Docker delivery or a live CI job.

Label evidence as **offline**, **native database**, **container**, **CI**, or **concept only**, and record the environment. A workflow draft is not an executed job. A local HTTP checker proves response data, not how the service was deployed. Author reference validation does not mark your progress complete.

Keep source fixtures unchanged. Put experiments in a scratch file or the scoped lab directory. Stop only processes/containers you started for the lab. Retain sanitized summaries and selected evidence; keep databases, logs, environments and credentials out of commits as directed by setup and .gitignore.

## Review each week

Rebuild one important function using a new fixture, solve an unfamiliar SQL question, and explain one project stage in English. Review your weakest error-journal entry and reproduce its repair. If a gate fails, select one or two relevant lessons and retry the gate; do not restart all four courses.

Use AI, when available, for an explanation, a graded hint or candidate test cases. Verify suggestions, use synthetic inputs and record what you accepted or rejected. Keep credentials and private data out of prompts. All core assignments have local instructions; an AI account is optional.

Choose extra material only for a demonstrated gap. [Resources](resources.md) are references and possible substitutes, not another required workload. Progress comes from working results, explanations and recovery evidence rather than video time or certificates.
