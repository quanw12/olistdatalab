# Help — Unpack rows and analyze lists

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Use if temperatures to distinguish nonempty input before calling min/max or dividing.
~~~python
values = []
if values:
    mean = sum(values) / len(values)
else:
    mean = None
print(mean)
~~~
Compute first, print afterward. Check that the empty branch assigns every variable that will later be printed.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Why is a missing average different from zero? When does ordinary unpacking raise ValueError?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
