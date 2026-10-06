# Help — Membership, equality, and identity

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Draw names as arrows to objects. Two names assigned to the same list share one arrow destination.
~~~python
items = [1]
alias = items
copy_of_values = [1]
print(alias is items)
print(copy_of_values == items)
~~~
Use the exact city spelling in membership tests; matching is case-sensitive.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Can two equal objects have different identities? When should you use is None?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
