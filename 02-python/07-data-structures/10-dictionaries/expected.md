# Expected results — Dictionaries, nested records, and aggregation

These are checking targets, not implementation code. Preserve the output order when the task specifies it. Input prompt text may differ where stated.

~~~text
Hanoi: 2
Hue: 1
rejected: 2
~~~

## Additional checks

The given city values are strings when present. Supporting None or other types is a later contract extension; do not assume get replaces present None. Empty rows input produces rejected: 0 and no city lines.

## Explain your result

What is the difference between a missing key and a key with None? Why must the grouping dictionary be created before the loop?
