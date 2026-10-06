# Help — Search with for-else

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Align else with for, not with if. Reuse the ASCII/digit rule from the string lesson.
~~~python
for letter in "xyz":
    if letter == "q":
        print("found q")
        break
else:
    print("q absent")
~~~
If your no-match message appears once per character, it probably belongs to an inner if instead of the loop.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Does loop-else run for an empty iterable? Does continue prevent it?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
