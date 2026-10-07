# Generators, batching, and memory

Original Python-for-DE extension. [Source reference](https://docs.python.org/3.13/tutorial/classes.html#generators).

## Concept and purpose

A generator function contains yield. Calling it produces an iterator; execution advances only as values are requested. Each yield pauses with local state preserved.

A bounded batch avoids holding an entire source in memory. That benefit disappears if a downstream consumer immediately calls list on a huge generator. Keep the entire chain bounded.

A yielded list remains an object the caller can hold. Clearing that same buffer mutates previously returned data. Yield the completed list, then create a fresh buffer. Emit a final partial batch only if nonempty.

Generators are consumed; an exhausted iterator is not automatically replayable. Measure runtime with time.perf_counter and memory with tracemalloc on representative inputs before optimizing. A tiny timing comparison is not evidence about large-data scaling.

## Syntax example

~~~python
def evens(stop):
    for n in range(stop):
        if n%2==0:yield n
stream=evens(5)
print(next(stream))
print(list(stream))
print(list(stream))
~~~

## Trace

The results are 0, [2, 4], then []. Each operation consumes more of the same stream.

## DE connection

File and API processing should use bounded memory where possible.

Use [exercise.py](exercise.py) for the exact input/output contract.


## API quick reference

| Syntax | Purpose |
|---|---|
| `yield value` | Suspend the generator and expose one value; state continues on the next request. |
| `iter(values) / next(iterator)` | Create/advance an iterator. Exhaustion raises StopIteration. |
| `list(iterator)` | Consume the remaining values; this materializes them and is not streaming. |
