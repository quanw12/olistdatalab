# Help — if, elif, else, and boundary order

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Write the ranges on paper first. If the first condition is temperature < 20, reaching elif already means temperature >= 20.
~~~python
size = 7
if size < 5:
    category = "small"
elif size < 10:
    category = "medium"
else:
    category = "large"
~~~
You can print once after the block. Check a value exactly on each threshold, not only typical values.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Why can several separate if statements print multiple labels? Which branch handles exactly 30?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
