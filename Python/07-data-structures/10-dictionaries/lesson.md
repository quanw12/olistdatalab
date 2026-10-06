# Dictionaries, nested records, and aggregation

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=38292s), assigned window **10:38:12–11:09:45**. Roadmap connection: PY03/PY05.  These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

A dictionary maps unique hashable keys to values. Write {"city": "Hue", "temperature": 29}. Access a required field with row["city"]; a missing key raises KeyError. row.get("city", "unknown") uses the fallback only when the key is absent, not when its value is None.

Assigning row["city"] = "Hanoi" changes that field. Reusing a key replaces its value rather than adding a second entry with the same key. in checks dictionary keys. items() supplies key/value pairs; keys() and values() expose the two sides separately.

A list of dictionaries represents multiple named-field records. Process one row at a time. For aggregation, totals[city] = totals.get(city, 0) + amount creates the first total or extends an existing one.

For several statistics per city, create a nested dictionary when a city is first seen, then update that city's count and sum. Avoid reusing one mutable default dictionary across all cities. This lesson focuses on counts; the function mini-project adds richer summaries.

Dictionary iteration preserves insertion order in modern Python, but a report can explicitly sort keys to define its display order.

## Syntax in a small example

~~~python
rows = [{"city": "Hue"}, {"city": "Hanoi"}, {"city": "Hue"}]
counts = {}
for row in rows:
    city = row["city"]
    counts[city] = counts.get(city, 0) + 1
for city in sorted(counts):
    print(city, counts[city])
print({"city": None}.get("city", "unknown"))
print({}.get("city", "unknown"))
~~~

Expected output:

~~~text
Hanoi 1
Hue 2
None
unknown
~~~

## Trace what happens

The first Hue creates count 1; the second increments it to 2. Sorting determines report order. A present key with None does not trigger get's fallback.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/datastructures.html#dictionaries).
