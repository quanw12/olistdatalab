# Help — Return values, early return, and scope

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Start with the empty-list guard, then calculate the nonempty result. Reuse the aggregation syntax from Chapter 7.
~~~python
def span(values):
    if not values:
        return None
    return max(values) - min(values)

result = span([3, 8])
print(result)
~~~
If your caller gets None despite visible numbers, check whether you only printed the summary. Every intended path needs the correct return value.

</details>

<details>
<summary>Check your explanation</summary>

Why is print not a replacement for return? Can a function mutate an argument despite its variable names being local?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
