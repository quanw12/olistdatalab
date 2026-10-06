# Comprehensions and small lambda expressions

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=34898s), assigned window **09:41:38–10:12:01**. Roadmap connection: PY05.  These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

A list comprehension combines an expression, iteration and optional filter: [expression for item in items if condition]. Read the for and if parts first to understand which items exist, then the expression to understand what each output contains.

Comprehensions are suitable for short transformations. A long nested expression is usually clearer as a loop, especially when you need several error reasons or side effects. Avoid comprehensions used only to call print.

lambda parameter: expression creates a small unnamed function that returns one expression. This is an early callable preview before Chapter 8. sorted(rows, key=lambda row: row[1]) asks Python to compute the second field for comparison.

The lambda is a function value. Passing it to key allows sorted to call it for every row. Do not call it yourself without the intended row.

## Syntax in a small example

~~~python
values = [-2, 0, 4]
doubled = [value * 2 for value in values if value >= 0]
print(doubled)
rows = [["A", 9], ["B", 3]]
print(sorted(rows, key=lambda row: row[1]))
~~~

Expected output:

~~~text
[0, 8]
[['B', 3], ['A', 9]]
~~~

## Trace what happens

The filter removes -2, then the expression doubles 0 and 4. The sort compares numeric second fields rather than the first labels.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/datastructures.html#list-comprehensions).
