# Sort, reverse, and combine lists

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=31306s), assigned window **08:41:46–09:18:29**. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

sorted(values) returns a new sorted list. values.sort() sorts the existing list and returns None. reverse=True chooses descending order. reversed(values) gives an iterator over reverse order, which is not the same as sorting descending.

The key argument chooses a comparison value for each element. sorted(words, key=len) orders by length. It receives the function len without parentheses; Python calls that function for each element. Sorting is stable: equal keys retain their prior order.

left + right creates a combined list. extend changes the left list. Neither operation removes duplicates automatically. Keep order and duplicate rules explicit.

Do not assume text-form numbers sort numerically: "10" comes before "2" as strings. Convert when the data contract requires numeric order.

## Syntax in a small example

~~~python
values = [8, 2, 5]
ordered = sorted(values)
print(values)
print(ordered)
print(sorted(values, reverse=True))
print(sorted(["bbb", "a", "cc"], key=len))
~~~

Expected output:

~~~text
[8, 2, 5]
[2, 5, 8]
[8, 5, 2]
['a', 'cc', 'bbb']
~~~

## Trace what happens

The original list remains in its input order. sorted creates ascending and descending results. key=len compares string lengths rather than spelling.


Technical reference: [Python documentation](https://docs.python.org/3.13/howto/sorting.html).
