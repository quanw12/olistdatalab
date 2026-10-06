# Unpack rows and analyze lists

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=28088s), assigned window **07:48:08–08:19:18**. Roadmap connection: PY03/PY05.  These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

Unpacking assigns sequence elements to names: city, temperature = row. Ordinary unpacking requires exactly as many values as target names. A starred target can collect remaining values: first, *rest = values.

sum adds numeric elements. min/max select extremes. len counts items. A mean uses sum(values) / len(values), but only when the list is nonempty. min([]) and max([]) raise ValueError; sum([]) returns zero.

A missing average and a zero average are different. Use None for the unavailable result, then decide separately how to display it. This makes empty input an explicit case rather than an accidental crash.

Unpacking names the meaning of each position and makes a loop easier to read. It does not validate that values have suitable types.

## Syntax in a small example

~~~python
row = ["Hue", 27]
city, temperature = row
print(city, temperature)
values = [2, 4, 9]
first, *rest = values
print(first, rest)
print(min(values), max(values), sum(values))
print(sum(values) / len(values))
~~~

Expected output:

~~~text
Hue 27
2 [4, 9]
2 9 15
5.0
~~~

## Trace what happens

Two targets receive two row fields. The starred target becomes a list containing 4 and 9. The total is 15 across three items.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/library/functions.html#min).
