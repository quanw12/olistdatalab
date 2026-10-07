# Help — Iterables, enumerate, zip, and filtering

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Initialize hot_cities once, then unpack each zip pair into two names. Append only the city after checking its temperature.
~~~python
names = ["A", "B"]
scores = [1, 4]
for name, score in zip(names, scores, strict=True):
    print(name, score)
~~~
zip aligns positions. If you need matching by a business ID, this simple pattern is not a substitute for a keyed join.

</details>

<details>
<summary>Check your explanation</summary>

Why can ordinary zip hide data? Why might filter(None, readings) incorrectly remove a valid reading?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
