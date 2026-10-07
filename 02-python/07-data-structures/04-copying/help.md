# Help — Aliases, shallow copies, and nested data

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Create all three references/copies before any mutation. Otherwise your deep copy may intentionally capture the already changed value.
~~~python
nested = [[5]]
outer_copy = nested.copy()
print(nested is outer_copy)
print(nested[0] is outer_copy[0])
~~~
The first comparison is False; the second is True. Use that picture to explain the requested result.

</details>

<details>
<summary>Check your explanation</summary>

Why does a shallow copy not isolate nested rows? What is the difference between changing a row cell and replacing a whole row?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
