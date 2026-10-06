# Iterables, enumerate, zip, and filtering

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=33509s), assigned window **09:18:29–09:41:38**. Roadmap connection: PY03/PY05.  These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

An iterable can provide items to a loop. An iterator is a stateful stream consumed as you request items. Lists can be iterated repeatedly; the same iterator may be exhausted after one traversal.

enumerate(values, start=1) pairs each item with a counter. zip(left, right) pairs aligned elements. By default zip stops at the shortest iterable, which can silently hide unmatched data. zip(..., strict=True) raises ValueError if lengths differ in supported Python versions.

Filtering means keeping elements that satisfy a condition. A loop with if and append is often the clearest starting point. filter(None, values) keeps truthy values, which also discards zero; that is unsuitable when zero is valid data. Predicate-based filter is revisited after callable syntax.

Use stable input order unless the requirement calls for sorting.

## Syntax in a small example

~~~python
cities = ["Hue", "Hanoi"]
values = [27, 30]
for position, city in enumerate(cities, start=1):
    print(position, city)
for city, value in zip(cities, values, strict=True):
    print(city, value)
valid_values = []
for value in [0, -1, 3]:
    if value >= 0:
        valid_values.append(value)
print(valid_values)
~~~

Expected output:

~~~text
1 Hue
2 Hanoi
Hue 27
Hanoi 30
[0, 3]
~~~

## Trace what happens

enumerate creates numbered pairs. zip matches by position, not by a database key. The explicit filter keeps zero because the condition is >= 0.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/library/functions.html#zip).
