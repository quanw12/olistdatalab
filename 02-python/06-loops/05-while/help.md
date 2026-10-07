# Help — while loops and guaranteed progress

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Use the same no-break meaning of else as for-else. Put the increment on the unsuccessful path.
~~~python
remaining = 2
while remaining > 0:
    print(remaining)
    remaining -= 1
~~~
Manually trace attempt before each condition. If the program does not stop, use Ctrl+C, then identify the path that leaves the state unchanged.

</details>

<details>
<summary>Check your explanation</summary>

Why can a while loop run zero times? What guarantees that this retry simulation terminates?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
