# Help — Run a script, comments, and print

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Start with one print call per output line. Text needs quotes; a numeric literal does not. For the last line, pass three strings and set sep to the required separator.
~~~python
print("one", "two", sep=" / ")
~~~
That example prints one / two. Apply the same argument pattern to the required labels. If Python reports an unterminated string literal, check that each opening quote has a matching closing quote.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

What is the difference between a terminal command and Python source code? Why is the comment absent from output?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
