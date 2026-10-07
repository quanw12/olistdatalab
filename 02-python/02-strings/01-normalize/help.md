# Help — Clean and format strings

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

First produce the whitespace-normalized string, then call title().
~~~python
label = "  river   station "
collapsed = " ".join(label.split())
print(collapsed.title())
~~~
Use strip().lower() for the source. If multiple internal spaces remain, you used strip without split/join. If your raw value changed, check which variable you reassigned.

</details>

<details>
<summary>Check your explanation</summary>

Why does strip alone not collapse internal spaces? Why should the normalization rule be documented?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
