# Aliases, shallow copies, and nested data

Companion to [Data With Baraa's video](https://www.youtube.com/watch?v=Rq5gJVxz55Q&t=29958s), assigned window **08:19:18–09:18:29**. Roadmap connection: PY03. Supplementary focused practice within the list-mutation/sorting region. Copying also appears in the public course syllabus; an exact video subtopic timestamp was not verified. These explanations and exercises are original companion material; see [source notes](../../sources.md).

## Understand the idea

alias = original creates a second reference to one object. Mutating through either name changes that object. original.copy() or original[:] creates a new outer list.

A shallow copy still refers to the same nested objects. For a table represented as a list of lists, changing a cell inside a shared row changes both views. Replacing an entire row in the copy is different: it changes an outer-list slot.

copy.deepcopy creates recursively copied structures for ordinary nested lists in this lesson. Import the standard-library copy module first. Deep copying is not an automatic best choice for every program: think about which objects need independence.

A useful picture has arrows from names to outer lists and arrows from slots to inner lists. Draw it before running the example.

## Syntax in a small example

~~~python
import copy

original = [[1], [2]]
alias = original
shallow = original.copy()
deep = copy.deepcopy(original)
alias.append([3])
shallow[0][0] = 9
print(original)
print(shallow)
print(deep)
~~~

Expected output:

~~~text
[[9], [2], [3]]
[[9], [2]]
[[1], [2]]
~~~

## Trace what happens

Appending changes the shared outer object, so original gains a third row. The shallow copy has only two rows but shares its first inner row. The deep copy keeps independent inner values.

## Before the exercise

Predict one result after changing a value in the example. Run the example, compare it with your prediction, and explain any mismatch. Then use the exercise's own data and requirements.

Technical reference: [Python documentation](https://docs.python.org/3.13/library/copy.html).
