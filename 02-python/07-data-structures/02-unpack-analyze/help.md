# Help — Unpack rows and analyze lists

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Use if temperatures to distinguish nonempty input before calling min/max or dividing.
~~~python
values = []
if values:
    mean = sum(values) / len(values)
else:
    mean = None
print(mean)
~~~
Compute first, print afterward. Check that the empty branch assigns every variable that will later be printed.

</details>

<details>
<summary>Check your explanation</summary>

Why is a missing average different from zero? When does ordinary unpacking raise ValueError?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
