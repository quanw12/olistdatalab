# Help — Aliases, shallow copies, and nested data

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Create all three references/copies before any mutation. Otherwise your deep copy may intentionally capture the already changed value.
~~~python
nested = [[5]]
outer_copy = nested.copy()
print(nested is outer_copy)
print(nested[0] is outer_copy[0])
~~~
The first comparison is False; the second is True. Use that picture to explain the requested result.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Why does a shallow copy not isolate nested rows? What is the difference between changing a row cell and replacing a whole row?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
