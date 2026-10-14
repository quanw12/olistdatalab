# C03-L01 — Integers, floats, and arithmetic

**Difficulty: Learn.** 15–45 minutes of coding; allow extra time for first setup. For an independent attempt, syntax documentation is allowed; leave approach hints closed until you have tried.

[Chapter overview](../README.md) · [Course start](../../README.md)

[Previous lesson](../../02-strings/03-search-validation/guide.md) · [Next lesson](../02-round-random/guide.md)

## Study order

1. Watch [the assigned video window](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=10771s): **02:59:31–03:11:33**. Pause to try each new expression.
2. Read [lesson.md](lesson.md) and predict the example output before running it.
3. Implement the prompts in [exercise.py](exercise.py). Keep teaching examples in a scratch file if needed.
4. Use [help.md](help.md) one hint at a time when stuck.
5. Compare with [expected.md](expected.md), including the extra checks.
6. Answer the reflection questions in your own words, then review and commit.

## Run

Use your existing Python 3.13 or 3.14 interpreter; see [setup](../../setup.md). No packages are required. In PowerShell:

~~~powershell
Set-Location "C:\DE Courses\02-python\03-numbers\01-arithmetic"
python .\exercise.py
~~~

The initial exercise contains comments only, so it intentionally prints nothing. Write your solution below the prompts. Do not type the PowerShell prompt prefix or the code-fence marks.

## Completion

- [ ] I attempted the exercise before consulting detailed hints.
- [ ] My output meets the contract and the additional checks.
- [ ] I can explain the values and decisions without reading the example.
- [ ] I answered: When do you want / instead of //? Why is integer cents useful for exact arithmetic?

Send the exercise file for review and describe any mismatch. Completion is about correct reasoning as well as output.

## Commit after completing this lesson

These commands stage this lesson folder only. Shared course documents have their own initial commit command in the [course README](../../README.md). Keep your `main` branch workflow.

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "02-python/03-numbers/01-arithmetic"
git diff --cached --stat
git diff --cached
git commit -m "feat(python): complete c03-l01 arithmetic"
git push origin main
~~~

Review all staged files: changes staged earlier remain in the index. These commands do not change your branch or apply any stash.


If this is familiar, solve and explain a changed example before treating it as a short refresh. Setup recipes teach the environment; copying one is not an independent coding assessment.
