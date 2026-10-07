# Help — Collect and unpack arguments with * and **

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Treat values as a tuple and reuse the empty guard from the previous lesson. Treat metadata as a dictionary.
~~~python
def count_values(*items):
    return len(items)

items = [1, 2]
print(count_values(items))
print(count_values(*items))
~~~
The outputs are 1 and 2. If your average receives a list inside a tuple, inspect whether the call needs unpacking.

</details>

<details>
<summary>Check your explanation</summary>

What do * and ** mean in a definition versus a call? Why are explicit parameters often easier to validate?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
