# Help — Comprehensions and small lambda expressions

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

First write the cleaning as a loop. Once correct, move the output expression before for and the condition after the iterable.
~~~python
labels = [" a ", " "]
cleaned = [label.strip().upper() for label in labels if label.strip()]
~~~
For the sort, the lambda receives one whole row and returns the numeric field. reverse=True belongs to sorted, not inside the lambda.

</details>

<details>
<summary>Check your explanation</summary>

Which part of a comprehension decides whether an item is kept? Why should complex validation remain a normal loop?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
