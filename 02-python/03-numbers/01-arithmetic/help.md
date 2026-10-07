# Help — Integers, floats, and arithmetic

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Compute the quotient and remainder separately. For the Celsius expression, Python evaluates multiplication/division before addition, but parentheses may make your intent clearer.
~~~python
total_units = 19
group_size = 6
print(total_units // group_size, total_units % group_size)
~~~
For the negative example, verify -7 = (-3 * 3) + 2. Floor means toward negative infinity.

</details>

<details>
<summary>Check your explanation</summary>

When do you want / instead of //? Why is integer cents useful for exact arithmetic?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
