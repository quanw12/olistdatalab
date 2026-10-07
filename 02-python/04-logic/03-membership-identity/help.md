# Help — Membership, equality, and identity

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Draw names as arrows to objects. Two names assigned to the same list share one arrow destination.
~~~python
items = [1]
alias = items
copy_of_values = [1]
print(alias is items)
print(copy_of_values == items)
~~~
Use the exact city spelling in membership tests; matching is case-sensitive.

</details>

<details>
<summary>Check your explanation</summary>

Can two equal objects have different identities? When should you use is None?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
