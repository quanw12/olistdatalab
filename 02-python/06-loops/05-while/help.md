# Help — while loops and guaranteed progress

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Use the same no-break meaning of else as for-else. Put the increment on the unsuccessful path.
~~~python
remaining = 2
while remaining > 0:
    print(remaining)
    remaining -= 1
~~~
Manually trace attempt before each condition. If the program does not stop, use Ctrl+C, then identify the path that leaves the state unchanged.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Why can a while loop run zero times? What guarantees that this retry simulation terminates?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
