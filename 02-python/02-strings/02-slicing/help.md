# Help — Indexing and slicing without off-by-one errors

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Write positions 0 through 10 under VN-HCM-2026. The first hyphen is at 2 and the second at 6. For a three-character segment beginning at index k, its stop is k + 3.
~~~python
sample = "Q-789"
print(sample[2:5])
~~~
Use an f-string with square brackets around the empty slice so you can see that it is empty.

</details>

<details>
<summary>Check your explanation</summary>

Why is the stop index excluded? What happens to a slice when its boundaries are beyond the string?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
