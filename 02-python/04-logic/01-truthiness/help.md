# Help — Boolean values and truthiness

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Inspect the type and content before predicting truthiness. Quotes make the value text.
~~~python
raw = "   "
print(bool(raw))
print(bool(raw.strip()))
~~~
Do not convert the word False with bool and expect semantic parsing. For values that need specific meanings, define explicit accepted strings later.

</details>

<details>
<summary>Check your explanation</summary>

Why is 'False' truthy? Why is truthiness insufficient to validate a temperature?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
