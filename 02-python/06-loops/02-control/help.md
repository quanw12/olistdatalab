# Help — break, continue, and pass

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Check the stop marker first, then the skip marker, then print the accepted character.
~~~python
for marker in "x.y":
    if marker == ".":
        continue
    print(marker)
~~~
Replacing continue with pass would allow the dot to reach print. For debugging, trace the statement that executes immediately after each control keyword.

</details>

<details>
<summary>Check your explanation</summary>

Why is pass not interchangeable with continue? Which loop does break exit?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
