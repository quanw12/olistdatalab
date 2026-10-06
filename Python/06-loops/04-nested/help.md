# Help — Nested loops and pairs

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Choose range boundaries that include 3. The total counter belongs before the outer loop.
~~~python
for group in "XY":
    for index in range(2):
        print(group, index)
~~~
Draw the outer item beside each inner iteration. If you produce only three identifiers total, check whether the inner loop is actually nested.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

How many body executions occur for 4 outer and 5 inner items? Why does an inner break not stop the outer loop?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
