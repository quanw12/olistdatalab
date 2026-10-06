# Sets, membership, and stable deduplication

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=37199s), assigned window **10:19:59–10:38:12**. Roadmap connection: PY03/PY05.  These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

A set stores unique hashable values. Use set() for an empty set; {} creates an empty dictionary. add inserts one value. discard removes if present without failing when absent; remove raises KeyError if missing.

Union (|), intersection (&), and difference (-) compare membership across sets. Sets do not promise the input order. For deterministic printed results, sort simple values first.

When you need first-seen order, use both a seen set and an output list. For each input value, append only if it is absent from seen, then record it in seen. This separates fast membership checks from ordered storage.

Deduplication also needs a normalization rule and key. "Hue" and " hue " are different strings until you normalize them. A repeated business ID is not necessarily an identical event; correction handling comes later.

## Syntax in a small example

~~~python
left = {"A", "B"}
right = {"B", "C"}
print(sorted(left | right))
print(sorted(left & right))
print(sorted(left - right))
seen = set()
unique = []
for value in ["B", "A", "B"]:
    if value not in seen:
        seen.add(value)
        unique.append(value)
print(unique)
~~~

Expected output:

~~~text
['A', 'B', 'C']
['B']
['A']
['B', 'A']
~~~

## Trace what happens

Sorted display makes set results predictable. The final loop preserves the first appearance of B, then A, while skipping the repeated B.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/datastructures.html#sets).
