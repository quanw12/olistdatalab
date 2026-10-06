# C08-L01 — Define and call small functions

[Chapter overview](../README.md) · [Course start](../../README.md)

[Previous lesson](../../07-data-structures/10-dictionaries/guide.md) · [Next lesson](../../08-functions/02-parameters/guide.md)

## Study order

1. Watch [the assigned video window](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=40185s): **11:09:45–11:28:12**. Pause to try each new expression.
2. Read [lesson.md](lesson.md) and predict the example output before running it.
3. Implement the prompts in [exercise.py](exercise.py). Keep teaching examples in a scratch file if needed.
4. Use [help.md](help.md) one hint at a time when stuck.
5. Compare with [expected.md](expected.md), including the extra checks.
6. Answer the reflection questions in your own words, then review and commit.

## Run

Use your existing Python 3.13 or 3.14 interpreter; see [setup](../../setup.md). No packages are required. In PowerShell:

~~~powershell
Set-Location "C:\DE Courses\Python\08-functions\01-define-call"
python .\exercise.py
~~~

The initial exercise contains comments only, so it intentionally prints nothing. Write your solution below the prompts. Do not type the PowerShell prompt prefix or the code-fence marks.

## Completion

- [ ] I attempted the exercise before consulting detailed hints.
- [ ] My output meets the contract and the additional checks.
- [ ] I can explain the values and decisions without reading the example.
- [ ] I answered: What is the difference between a parameter and an argument? When does a def body execute?

Send the exercise file for review and describe any mismatch. Completion is about correct reasoning as well as output.

## Commit after completing this lesson

These commands stage this lesson folder only. Shared course documents have their own initial commit command in the [course README](../../README.md). Keep your feature/... branch convention.

~~~powershell
Set-Location "C:\DE Courses"
git status
git branch --show-current
git add -- "Python/08-functions/01-define-call"
git diff --cached --stat
git diff --cached
git commit -m "feat(python): complete c08-l01 define-call"
git push -u origin HEAD
~~~

Review all staged files: changes staged earlier remain in the index. These commands do not change your branch or apply any stash.
