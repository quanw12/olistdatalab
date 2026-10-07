# Help — Create and access lists

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Count brackets from outside inward.
~~~python
table = [["A", 10], ["B", 20]]
row = table[1]
value = row[1]
print(value)
~~~
You can combine the two indexing steps after you understand them. If you see a single character, inspect whether you selected a string too early.

</details>

<details>
<summary>Check your explanation</summary>

How is indexing different from slicing? Why does len(rows) not count every nested field?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
