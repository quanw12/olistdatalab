# Help — for loops and accumulators

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

To include the number 5, choose a stop after 5. Initialize the character counter before its loop.
~~~python
hits = 0
for character in "level":
    if character == "e":
        hits += 1
print(hits)
~~~
Print summaries after the loop by returning to the outer indentation. If you see one summary per item, inspect indentation.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

Why does range(1, 5) omit 5? What goes wrong if the accumulator is initialized inside the loop?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
