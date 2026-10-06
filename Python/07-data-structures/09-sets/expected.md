# Expected results — Sets, membership, and stable deduplication

These are checking targets, not implementation code. Preserve the output order when the task specifies it. Input prompt text may differ where stated.

~~~text
['Hue', 'Hanoi', 'Da Nang']
2
['Can Tho']
['Da Nang']
~~~

## Additional checks

An empty incoming list gives [] and zero duplicates; all expected cities are then missing. Never compare the unsorted display order of a set.

## Explain your result

Why does list(set(values)) not promise first-seen order? Why does {} not make an empty set?
