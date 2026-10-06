# Help — Tuples and fixed-shape records

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Match target names to the order of fields. Tuple key boundaries avoid ambiguous concatenation.
~~~python
record = ("A", 8)
name, amount = record
one_item = (name,)
~~~
The comma in one_item is essential. The expected reassignment error is TypeError because tuple slots cannot be changed.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

What creates a one-item tuple? Can a tuple contain an object that is itself mutable?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
