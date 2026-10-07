# Help — Built-ins, named functions, and lambdas

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

In apply_to_all, operation is a local parameter containing a function. Call it with one item, not the whole list.
~~~python
def apply_once(value, operation):
    return operation(value)

print(apply_once("abc", len))
~~~
If you write normalize_city() while passing the argument, it runs immediately and lacks its required text argument. Supply the function value instead.

</details>

<details>
<summary>Check your explanation</summary>

Why is passing len different from passing len(values)? What makes a function easier to test independently?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
