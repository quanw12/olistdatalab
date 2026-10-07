# Help — Define and call small functions

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Write the definition first, then leave a blank line and write calls without indentation.
~~~python
def announce(topic):
    """Display the current topic."""
    print(f"Topic: {topic}")

announce("files")
~~~
If nothing prints, check for the parentheses that actually call your function. If the second city appears inside the first function body, check indentation.

</details>

<details>
<summary>Check your explanation</summary>

What is the difference between a parameter and an argument? When does a def body execute?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
