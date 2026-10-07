# Help — Nested loops and pairs

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Choose range boundaries that include 3. The total counter belongs before the outer loop.
~~~python
for group in "XY":
    for index in range(2):
        print(group, index)
~~~
Draw the outer item beside each inner iteration. If you produce only three identifiers total, check whether the inner loop is actually nested.

</details>

<details>
<summary>Check your explanation</summary>

How many body executions occur for 4 outer and 5 inner items? Why does an inner break not stop the outer loop?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
