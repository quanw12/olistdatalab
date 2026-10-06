# C12-L01 — Generators, batching, and memory
# Implement your own solution below these problem statements.
#
# Implement batches(iterable, size), returning a lazy iterator of NEW lists.
# size must have exact type int and be positive; invalid size raises ValueError at call or first iteration.
# Preserve order; emit full batches and a final nonempty partial batch.
# Empty input yields nothing. Never materialize the whole source.
# Previously yielded lists must remain unchanged.
# See help.md for hints and expected.md for cases.
