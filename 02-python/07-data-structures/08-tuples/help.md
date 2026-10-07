# Help — Tuples and fixed-shape records

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Match target names to the order of fields. Tuple key boundaries avoid ambiguous concatenation.
~~~python
record = ("A", 8)
name, amount = record
one_item = (name,)
~~~
The comma in one_item is essential. The expected reassignment error is TypeError because tuple slots cannot be changed.

</details>

<details>
<summary>Check your explanation</summary>

What creates a one-item tuple? Can a tuple contain an object that is itself mutable?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
