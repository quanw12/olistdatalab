# Help — Comparisons and combined rules

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Write one expression per specified pair or reassign the variables between prints. Keep the two range rules in parentheses.
~~~python
raw = ""
can_parse_positive = raw.isdecimal() and int(raw) > 0
print(can_parse_positive)
~~~
The right side is skipped for empty/nondecimal input. If your code crashes, check operand order. Do not put int(raw) before the guard.

</details>

<details>
<summary>Check your explanation</summary>

How is = different from ==? What exactly gets skipped during short-circuit evaluation?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
