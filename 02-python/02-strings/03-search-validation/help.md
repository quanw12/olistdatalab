# Help — Search strings and define validation limits

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Translate each requirement into one Boolean or integer expression. Do not write conditional branches yet.
~~~python
tag = " REPORT.JSON ".strip().lower()
print(tag.endswith(".json"))
~~~
For the identifier, combine isascii() and isdecimal() with and. If find returns 0, that means a match at the first character, not failure. The missing-value sentinel here is -1.

</details>

<details>
<summary>Check your explanation</summary>

Why is a digit-character test insufficient for a decimal number such as '-7.5'? Why is find's missing result different from index?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
