# Help — for loops and accumulators

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

To include the number 5, choose a stop after 5. Initialize the character counter before its loop.
~~~python
hits = 0
for character in "level":
    if character == "e":
        hits += 1
print(hits)
~~~
Print summaries after the loop by returning to the outer indentation. If you see one summary per item, inspect indentation.

</details>

<details>
<summary>Check your explanation</summary>

Why does range(1, 5) omit 5? What goes wrong if the accumulator is initialized inside the loop?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
