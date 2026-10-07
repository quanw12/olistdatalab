# Help — Rounding, display precision, and randomness

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Use the f-string format specifier :.2f inside the braces.
~~~python
value = 6.5
print(f"{value:.2f}")
~~~
For random draws, keep separate generator variables. Drawing twice from one generator advances its state and is not the same experiment. Check the range with 1 <= draw <= 6.

</details>

<details>
<summary>Check your explanation</summary>

Why should expected results avoid one exact unseeded random number? Why do equal-looking rounded/formatted results have different types?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
