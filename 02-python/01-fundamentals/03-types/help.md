# Help — Data types and explicit conversion

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Use type(variable).__name__ for the first five lines. Double underscores belong to the attribute name; copy that spelling exactly. Conversion creates a value you should assign to another name.
~~~python
raw = "8"
converted = int(raw)
print(type(converted).__name__)
~~~
Use float for decimal text. int("30.4") is not valid integer-string conversion. No loops or functions are needed.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

How is None different from the text 'None'? How is int(3.9) different from round(3.9)?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
