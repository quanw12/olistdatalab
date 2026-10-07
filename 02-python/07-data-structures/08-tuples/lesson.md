# Tuples and fixed-shape records

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=36721s), assigned window **10:12:01–10:19:59**. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

A tuple is an ordered collection whose element references cannot be reassigned after construction. Commas create tuples: ("Hue", 29) has two elements; ("Hue",) has one. Parentheses without a comma, ("Hue"), still represent a string.

Indexing, slicing and unpacking work much like lists. Tuples are useful for fixed-shape records or compound keys when the components are hashable. They do not automatically give positions meaningful field names.

Tuple immutability is shallow: a mutable object inside a tuple can still change. For example, a tuple containing a list cannot be assumed deeply immutable or hashable.

Choose a list when you need to add/remove elements, a tuple for a fixed position-based grouping, and later a dictionary when named fields improve clarity.

## Syntax in a small example

~~~python
reading = ("Hue", 29)
city, temperature = reading
print(city, temperature)
single = ("Hue",)
print(len(single))
print(type(("Hue")).__name__)
print(type(single).__name__)
~~~

Expected output:

~~~text
Hue 29
1
str
tuple
~~~

## Trace what happens

The two-field tuple unpacks into two names. The trailing comma makes single a tuple even though it contains only one value.


Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/datastructures.html#tuples-and-sequences).
