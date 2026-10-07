# Help — if, elif, else, and boundary order

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Write the ranges on paper first. If the first condition is temperature < 20, reaching elif already means temperature >= 20.
~~~python
size = 7
if size < 5:
    category = "small"
elif size < 10:
    category = "medium"
else:
    category = "large"
~~~
You can print once after the block. Check a value exactly on each threshold, not only typical values.

</details>

<details>
<summary>Check your explanation</summary>

Why can several separate if statements print multiple labels? Which branch handles exactly 30?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
