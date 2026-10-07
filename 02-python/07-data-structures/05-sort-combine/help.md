# Help — Sort, reverse, and combine lists

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Create all_temperatures with + and derive the two sorted copies from it.
~~~python
numbers = [3, 1, 2]
print(list(reversed(numbers)))
print(sorted(numbers, reverse=True))
~~~
The two outputs differ. If a variable becomes None after sorting, check whether you assigned a .sort() return value.

</details>

<details>
<summary>Check your explanation</summary>

When would you choose sort over sorted? Why do combination and deduplication need separate rules?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
