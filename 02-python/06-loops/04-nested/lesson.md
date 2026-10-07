# Nested loops and pairs

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=22719s), assigned window **06:18:39–06:40:52**. Roadmap connection: PY02. Reuses the previous lesson's video window. Focus on nested loops; the split is our practice design. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

A nested loop starts an inner iteration for every outer item. If the outer loop visits m items and the inner loop visits n items each time, its body runs m × n times.

Use distinct loop-variable names so you do not overwrite the outer value. Initialize a per-group accumulator inside the outer loop; initialize a whole-run accumulator before both loops.

This pattern can create combinations or inspect tabular data. It can also create accidental duplicate pairs. State whether you need every combination, aligned pairs, or unique pairs before coding.

break stops the nearest loop only. Exiting the inner loop still allows the outer loop to continue. Do not expect one break to leave several nested levels.

## Syntax in a small example

~~~python
pair_count = 0
for zone in "AB":
    for batch in range(1, 3):
        print(f"{zone}-{batch}")
        pair_count += 1
print("pairs:", pair_count)
~~~

Expected output:

~~~text
A-1
A-2
B-1
B-2
pairs: 4
~~~

## Trace what happens

For A, the inner range completes 1 and 2. Then the outer loop moves to B and restarts that range. Two zones times two batches makes four pairs.


Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/controlflow.html#break-and-continue-statements).
