# Help — Add, remove, and update list elements

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

After insertion, the original second element moves one position right. Track positions before updating.
~~~python
stages = ["extract", "load"]
stages.insert(1, "validate")
last_stage = stages.pop()
print(stages, last_stage)
~~~
If cities becomes None, inspect an assignment from a mutating method. For missing values, decide whether membership should be checked before remove.

</details>

<details>
<summary>Check your explanation</summary>

How does append differ from extend? Why is pop's return value useful while append's usually is not?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
