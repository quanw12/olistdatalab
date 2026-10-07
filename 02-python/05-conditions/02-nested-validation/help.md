# Help — Nested conditions and validation order

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Write the checks in the required order. Do not call int until the format checks pass.
~~~python
raw = " 42 ".strip()
format_ok = raw.isascii() and raw.isdecimal()
~~~
Inside the final else, numeric comparisons become possible. If '101' is accepted, check the inclusive upper bound. If '-1' reaches a range check, you have changed the required format rule.

</details>

<details>
<summary>Check your explanation</summary>

Why does validation order change the reported error? Why should parsing happen after the character guard?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
