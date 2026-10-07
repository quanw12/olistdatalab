# Help — Data types and explicit conversion

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Use type(variable).__name__ for the first five lines. Double underscores belong to the attribute name; copy that spelling exactly. Conversion creates a value you should assign to another name.
~~~python
raw = "8"
converted = int(raw)
print(type(converted).__name__)
~~~
Use float for decimal text. int("30.4") is not valid integer-string conversion. No loops or functions are needed.

</details>

<details>
<summary>Check your explanation</summary>

How is None different from the text 'None'? How is int(3.9) different from round(3.9)?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
