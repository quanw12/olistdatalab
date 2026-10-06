# Help — Comprehensions and small lambda expressions

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

First write the cleaning as a loop. Once correct, move the output expression before for and the condition after the iterable.
~~~python
labels = [" a ", " "]
cleaned = [label.strip().upper() for label in labels if label.strip()]
~~~
For the sort, the lambda receives one whole row and returns the numeric field. reverse=True belongs to sorted, not inside the lambda.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Which part of a comprehension decides whether an item is kept? Why should complex validation remain a normal loop?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
