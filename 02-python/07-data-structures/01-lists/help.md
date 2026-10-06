# Help — Create and access lists

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Count brackets from outside inward.
~~~python
table = [["A", 10], ["B", 20]]
row = table[1]
value = row[1]
print(value)
~~~
You can combine the two indexing steps after you understand them. If you see a single character, inspect whether you selected a string too early.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

How is indexing different from slicing? Why does len(rows) not count every nested field?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
