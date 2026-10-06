# Help — Collect and unpack arguments with * and **

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Treat values as a tuple and reuse the empty guard from the previous lesson. Treat metadata as a dictionary.
~~~python
def count_values(*items):
    return len(items)

items = [1, 2]
print(count_values(items))
print(count_values(*items))
~~~
The outputs are 1 and 2. If your average receives a list inside a tuple, inspect whether the call needs unpacking.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

What do * and ** mean in a definition versus a call? Why are explicit parameters often easier to validate?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
