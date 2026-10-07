# Sets, membership and ordered output

Companion video window: [10:19:59–10:38:12](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=37199s).
These explanations/exercises are original; see [source notes](../../sources.md).

A set contains unique hashable values. set() makes an empty set; {} makes a dictionary.
add inserts one value; discard ignores an absent value, while remove raises KeyError.
in / not in test membership. Sets do not promise first-input order.
An ordered result may need a different collection alongside membership tracking; decide how yourself.

~~~python
available = {"small", "large"}
requested = {"large", "medium"}
available.add("medium")
available.discard("missing")
print("large" in available)
print(sorted(available & requested))
print(sorted(available - requested))
~~~

The outputs are True, ['large', 'medium'], then ['small'].
| means union, & intersection and - difference. A list cannot be a set element;
a tuple of hashable values can serve as a composite key.

Normalization and identity are separate decisions: "Hue" and " hue " are unequal
until normalized. Your exercise requires a particular normalization and first-seen
order. A sorted set would satisfy uniqueness but violate that output order.
Try an input where those two orders differ before opening a hint.

[Required syntax reference](https://docs.python.org/3.13/tutorial/datastructures.html#sets).
