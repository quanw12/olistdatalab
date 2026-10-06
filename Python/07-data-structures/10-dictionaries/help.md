# Help — Dictionaries, nested records, and aggregation

## Hint 1: identify the contract

Write down the required input values and output order from exercise.py. Predict the result for the main case manually. Separate each requirement into a small operation.

## Hint 2: syntax and reasoning

Use three separate stages inside the loop: retrieve/normalize, reject if blank, then update the group.
~~~python
counts = {}
name = "Zone A"
counts[name] = counts.get(name, 0) + 1
~~~
On a second update, get returns the previous integer. To print sorted results, loop over sorted(city_counts), then look up each count. If every count remains 1, check whether you recreate the dictionary inside the loop.

## Hint 3: inspect intermediate values

Temporarily print the intermediate value and its type after the operation you suspect. Compare it with the lesson trace. Remove diagnostic prints when comparing exact required output.

## Check your explanation

What is the difference between a missing key and a key with None? Why must the grouping dictionary be created before the loop?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.
