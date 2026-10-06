# Help — break, continue, and pass

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Check the stop marker first, then the skip marker, then print the accepted character.
~~~python
for marker in "x.y":
    if marker == ".":
        continue
    print(marker)
~~~
Replacing continue with pass would allow the dot to reach print. For debugging, trace the statement that executes immediately after each control keyword.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Why is pass not interchangeable with continue? Which loop does break exit?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
