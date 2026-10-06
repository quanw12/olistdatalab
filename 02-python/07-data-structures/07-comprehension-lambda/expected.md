# Expected results — Comprehensions and small lambda expressions

These are checking targets, not implementation code. Preserve the output order when the task specifies it. Input prompt text may differ where stated.

~~~text
['Hanoi', 'Hue']
[['Hanoi', 31], ['Da Nang', 30], ['Hue', 29]]
~~~

## Additional checks

The whitespace-only string must be omitted. Equal-temperature rows retain their original relative order unless you explicitly add a tie-breaker.

## Explain your result

Which part of a comprehension decides whether an item is kept? Why should complex validation remain a normal loop?
