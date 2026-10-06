# Membership, equality, and identity

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=14773s), assigned window **04:06:13–04:19:19**. Roadmap connection: PY03.  These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

in asks whether something belongs to a container: a character/substring in a string, an element in a list, or a key in a dictionary. not in negates membership.

== compares values. is compares object identity: whether two references point to the very same object. Use is None for absence, and == for text/numeric equality. Python may reuse some immutable objects; do not rely on their identity for content checks.

For this preview, square brackets create a list. alias = original makes another reference to the same list. Creating a second list with the same contents creates an equal but different object. The full list lesson comes later.

This distinction matters when changing a collection: aliases see a shared mutation. The dedicated copying lesson will make independent copies.

## Syntax in a small example

~~~python
first = ["north"]
alias = first
equal_value = ["north"]
print(first == equal_value)
print(first is equal_value)
print(first is alias)
print("north" in first)
print(None is None)
~~~

Expected output:

~~~text
True
False
True
True
True
~~~

## Trace what happens

first and equal_value have equal contents but separate identities. alias points at the exact object referenced by first. Membership checks content.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/reference/expressions.html#comparisons).
