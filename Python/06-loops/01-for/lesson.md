# for loops and accumulators

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=19496s), assigned window **05:24:56–05:47:57**. Roadmap connection: PY02.  These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

A for loop takes one item at a time from an iterable. Its loop variable is rebound for each iteration. The indented body runs once per item.

range(stop) provides integers from 0 through stop - 1. range(start, stop, step) lets you choose boundaries and a step. The stop is excluded, like slicing. A string is also iterable, yielding characters.

An accumulator holds a result across iterations. Initialize it before the loop, then update it inside. total += value means total = total + value. Resetting total inside the loop loses previous work.

Trace a loop with columns for iteration, current item, old total and new total. This makes off-by-one errors visible.

## Syntax in a small example

~~~python
total = 0
for value in range(2, 5):
    total += value
    print(value, total)
print("total:", total)
~~~

Expected output:

~~~text
2 2
3 5
4 9
total: 9
~~~

## Trace what happens

The values are 2, 3 and 4. The running totals are 2, 5 and 9. The final print is outside the loop.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/controlflow.html#for-statements).
