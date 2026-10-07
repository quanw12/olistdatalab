# Help — Conditional expressions and match

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Read the conditional expression as 'choose A when condition is true, otherwise choose B'. For match, keep the colon and indentation at both levels.
~~~python
extension = "json"
match extension:
    case "json":
        print("structured")
    case _:
        print("other")
~~~
If Python flags unreachable patterns, check whether you wrote an unquoted name that captures everything.

</details>

<details>
<summary>Check your explanation</summary>

When is a full if block clearer than an inline expression? Why must string case labels be quoted?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
