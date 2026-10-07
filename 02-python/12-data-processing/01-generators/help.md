# Help — Generators, batching, and memory

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Replace the buffer after yield; do not clear it.

</details>

<details>
<summary>Detailed approach</summary>

Validate size, create [], append items, yield at the size boundary, then bind a new empty list. After the loop yield the remaining buffer if nonempty. The checker watches source consumption: fetching one batch of size two should consume only two items.

</details>

<details>
<summary>Troubleshooting</summary>

Empty earlier batches indicate reused mutable storage. Reading all source records before the first yield violates laziness.

Read the first failing check, compare input/type/output and side effects, then make one focused change. The checker is an executable specification.

</details>

<details>
<summary>See where yield pauses</summary>

~~~python
def squares(values):
    for value in values:
        print("read", value)
        yield value * value

stream = squares([2, 3])
print(next(stream))
print(next(stream))
~~~

Calling squares creates a generator; the loop does not execute yet. The first next reads 2 and yields 4. The second resumes after that yield, reads 3 and yields 9.

For batches, maintain a small current list. After yielding a full list, assign a NEW empty list. Clearing the yielded list would also clear the object held by the caller. Do not call list() on the entire source; that defeats the bounded-consumption requirement. Validate size before consuming records; validation inside a generator runs when iteration begins.

</details>
