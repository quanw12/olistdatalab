# Dictionaries, nested records and aggregation

Companion video window: [10:38:12–11:09:45](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=38292s).
These explanations/exercises are original; see [source notes](../../sources.md).

A dictionary maps unique hashable keys to values. d[key] requires a present key;
d.get(key, fallback) uses the fallback only for an absent key, not a present None.
Assignment replaces that key's value. in tests keys; items() gives key/value pairs.

~~~python
stock = {"pens": 4, "books": 2}
stock["pens"] = 7
print(stock.get("paper", 0))
print({"paper": None}.get("paper", 0))
for label, units in stock.items():
    print(label, units)
~~~

The outputs start with 0 and None, then pens 7 and books 2.
keys() / values() expose each side; len(stock) counts keys, not input records.
Dictionary iteration preserves insertion order; sorted(stock) supplies sorted keys.

A list of dictionaries represents named-field records. For grouping, decide what
each output key means and what value it stores. You need to handle a first occurrence
and a later occurrence differently, but the exercise leaves that logic to you.
If values are nested mutable dictionaries, each group needs independent state.

Predict the result for two repeated groups and an empty input before implementing.
[Required syntax reference](https://docs.python.org/3.13/tutorial/datastructures.html#dictionaries).
