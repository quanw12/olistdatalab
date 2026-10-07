# Add, remove, and update list elements

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=29958s), assigned window **08:19:18–08:41:46**. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

append(value) adds one element to the end. extend(iterable) adds each supplied element. insert(index, value) inserts before that position. Assigning items[index] = value replaces an existing element.

remove(value) removes the first equal value and raises ValueError if missing. pop(index) removes and returns an element; pop() defaults to the last. del removes by position or slice without returning a value. clear empties the list.

Many list methods mutate the object and return None. items = items.append(x) is a common bug: it replaces your list variable with None. Call the method as a statement.

Avoid removing elements from the same list you are iterating when indexes can shift. Build a filtered list instead, which we practise later.

## Syntax in a small example

~~~python
labels = ["raw"]
labels.append("clean")
labels.extend(["mart", "report"])
removed = labels.pop()
labels[0] = "source"
print(labels)
print(removed)
~~~

Expected output:

~~~text
['source', 'clean', 'mart']
report
~~~

## Trace what happens

append contributes one string. extend contributes two. pop removes report and returns it. Index assignment changes only the first element.


Technical reference: [Python documentation](https://docs.python.org/3.13/tutorial/datastructures.html#more-on-lists).
