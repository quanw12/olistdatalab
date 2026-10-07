# LAB06 — Learn

## Correctness before speed

The supplied baseline searches every product for every movement. With R rows and D dimension entries it can make R×D comparisons. Build one lookup once, then look up each row: average O(R+D) under normal hash-table behavior. This is a design argument; measure your actual run before claiming an improvement.

## Syntax — Python

~~~python
import time
started = time.perf_counter()
# Call the implementation being measured.
elapsed = time.perf_counter() - started
copy = dict(row)
~~~
dict(row) copies the outer mapping, allowing category enrichment without editing the original row. A duplicate dimension key must be reported, otherwise a lookup may silently hide ambiguity. Review Python collections and DE03 profiling.

Use the same generated workload for before/after runs. Do not require a universal speed threshold: CPU load and interpreters differ.

[Assignment](exercise.md) · [Hints](help.md)
