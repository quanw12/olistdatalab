# Help — Positional, keyword, and default arguments

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Use a default string in the signature and one f-string after return.
~~~python
def badge(name, prefix="ID"):
    return f"{prefix}: {name}"

print(badge("station", prefix="KEY"))
~~~
Trace each call as city -> value, count -> value, label -> value. If Python says multiple values for an argument, check for a positional value already assigned to that keyword.

</details>

<details>
<summary>Check your explanation</summary>

When is a default value evaluated? Why can a list default accidentally share state?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
