# Help — Sort, reverse, and combine lists

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Create all_temperatures with + and derive the two sorted copies from it.
~~~python
numbers = [3, 1, 2]
print(list(reversed(numbers)))
print(sorted(numbers, reverse=True))
~~~
The two outputs differ. If a variable becomes None after sorting, check whether you assigned a .sort() return value.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

When would you choose sort over sorted? Why do combination and deduplication need separate rules?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
