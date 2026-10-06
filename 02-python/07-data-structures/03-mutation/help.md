# Help — Add, remove, and update list elements

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

After insertion, the original second element moves one position right. Track positions before updating.
~~~python
stages = ["extract", "load"]
stages.insert(1, "validate")
last_stage = stages.pop()
print(stages, last_stage)
~~~
If cities becomes None, inspect an assignment from a mutating method. For missing values, decide whether membership should be checked before remove.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

How does append differ from extend? Why is pop's return value useful while append's usually is not?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
