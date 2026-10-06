# Create and access lists

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=25804s), assigned window **07:10:04–07:48:08**. Roadmap connection: PY03.  These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

A list is an ordered, mutable collection written with square brackets. Its elements can have different types, although consistent row shapes are easier to process. list() creates a list from an iterable; [] creates an empty list.

Indexing and slicing follow the rules you learned for strings. Negative indexes count backward. A nested list contains lists as elements: rows[0] selects a row, then rows[0][1] selects one field from that row.

len(items) counts top-level elements, not all values recursively. A list with two rows has length two even if each row has three fields. An empty list has no first or last element.

Access should follow the known shape. If rows[0] is a city name string instead of a record, rows[0][1] would give a character rather than a field. Inspect types when unexpected values appear.

## Syntax in a small example

~~~python
rows = [["Hue", 25], ["Hanoi", 28]]
print(len(rows))
print(rows[0][0])
print(rows[-1][1])
print(rows[:1])
~~~

Expected output:

~~~text
2
Hue
28
[['Hue', 25]]
~~~

## Trace what happens

There are two top-level rows. The first nested access gives Hue. The last row's second field is 28. A slice returns a list, even when it selects one row.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/introduction.html#lists).
