# LE04 — Users, permissions and executable files

**Difficulty: Learn.** 15–45 minutes of coding; allow extra time for first setup. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Module](../README.md) · [Course index](../../README.md) · [Setup](../../setup.md) · [Independent study](../../../docs/study.md)

## Before starting

Complete LE03. Use native $LE_LAB_ROOT, not chmod experiments on the mounted Windows repository.

One lesson is one learning unit, not a fixed day. Allow 60–120 minutes initially; setup and projects may take several sessions. Use Bash in Ubuntu unless a block is explicitly marked PowerShell.

## Follow this order

1. Read [lesson.md](lesson.md), predict the example, and try it in your lab area.
2. Work through [exercise.md](exercise.md). Implement only the requested files; teaching examples belong in scratch files.
3. Consult [help.md](help.md) one step at a time.
4. Check [expected.md](expected.md), including failure cases.
5. Answer the reflection before revealing its answer. Record evidence in notes.md and mark [progress](../../progress.md).

## Run or verify

Follow the commands in exercise.md. Record the actual results in notes.md.

Use the terminal named above each code block. A syntax check is not evidence that a command worked on Linux or that Docker ran successfully.

## Commit your completed work

Return to **Windows PowerShell in your original repository**. Lab Git commands use separate disposable repositories.

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "03-linux/01-linux-basics/04-permissions"
git diff --cached --stat
git diff --cached
git commit -m "feat(linux): complete le04 permissions"
git push origin main
~~~

Use your feature/... convention; the course README links the shared branch/staging instructions. Review all previously staged files too. Generated logs, environments and local lab repositories do not belong in this commit.

## Continue

[Previous: LE03](../03-streams-and-text/guide.md) · [Next: LE05](../../02-bash-scripting/01-variables-quoting/guide.md)


If this is familiar, solve and explain a changed example before treating it as a short refresh. Setup recipes teach the environment; copying one is not an independent coding assessment.
