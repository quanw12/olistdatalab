# C08-L02 — Positional, keyword, and default arguments

**Difficulty: Learn.** 15–45 minutes of coding; allow extra time for first setup. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Chapter overview](../README.md) · [Course start](../../README.md)

[Previous lesson](../01-define-call/guide.md) · [Next lesson](../03-return-scope/guide.md)

## Study order

1. Watch [the assigned video window](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=41292s): **11:28:12–12:20:31**. This long video section is split across three lessons: argument binding, returns/scope, and flexible arguments. The window is shared; no finer timestamp is claimed.
2. Read [lesson.md](lesson.md) and predict the example output before running it.
3. Implement the prompts in [exercise.py](exercise.py). Keep teaching examples in a scratch file if needed.
4. Use [help.md](help.md) one hint at a time when stuck.
5. Compare with [expected.md](expected.md), including the extra checks.
6. Answer the reflection questions in your own words, then review and commit.

## Run

Use your existing Python 3.13 or 3.14 interpreter; see [setup](../../setup.md). No packages are required. In PowerShell:

~~~powershell
Set-Location "C:\DE Courses\02-python\08-functions\02-parameters"
python .\exercise.py
~~~

The initial exercise contains comments only, so it intentionally prints nothing. Write your solution below the prompts. Do not type the PowerShell prompt prefix or the code-fence marks.

## Completion

- [ ] I attempted the exercise before consulting detailed hints.
- [ ] My output meets the contract and the additional checks.
- [ ] I can explain the values and decisions without reading the example.
- [ ] I answered: When is a default value evaluated? Why can a list default accidentally share state?

Send the exercise file for review and describe any mismatch. Completion is about correct reasoning as well as output.

## Commit after completing this lesson

These commands stage this lesson folder only. Shared course documents have their own initial commit command in the [course README](../../README.md). Keep your `main` branch workflow.

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "02-python/08-functions/02-parameters"
git diff --cached --stat
git diff --cached
git commit -m "feat(python): complete c08-l02 parameters"
git push origin main
~~~

Review all staged files: changes staged earlier remain in the index. These commands do not change your branch or apply any stash.


If this is familiar, solve and explain a changed example before treating it as a short refresh. Setup recipes teach the environment; copying one is not an independent coding assessment.
