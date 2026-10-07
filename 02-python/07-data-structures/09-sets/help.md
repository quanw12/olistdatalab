# Help — Sets, membership, and stable deduplication

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Increment duplicate_count only on the repeated branch. Membership and insertion use the same value/key.
~~~python
seen = set()
for value in ["X", "X"]:
    if value in seen:
        print("duplicate")
    else:
        seen.add(value)
~~~
Difference is directional: required - actual answers what is missing, while actual - required answers what is unexpected.

</details>

<details>
<summary>Check your explanation</summary>

Why does list(set(values)) not promise first-seen order? Why does {} not make an empty set?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
