# Help — Search with for-else

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Align else with for, not with if. Reuse the ASCII/digit rule from the string lesson.
~~~python
for letter in "xyz":
    if letter == "q":
        print("found q")
        break
else:
    print("q absent")
~~~
If your no-match message appears once per character, it probably belongs to an inner if instead of the loop.

</details>

<details>
<summary>Check your explanation</summary>

Does loop-else run for an empty iterable? Does continue prevent it?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
