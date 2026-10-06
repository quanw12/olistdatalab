# Expected results — Aliases, shallow copies, and nested data

These are checking targets, not implementation code. Preserve the output order when the task specifies it. Input prompt text may differ where stated.

~~~text
[['Hanoi', 31], ['Hue', 28]]
[['Hanoi', 31], ['Hue', 28], ['Da Nang', 29]]
[['Hanoi', 30], ['Hue', 28]]
~~~

## Additional checks

Mutating deep[1][1] afterward must not affect original. Adding an outer element to shallow must not extend original.

## Explain your result

Why does a shallow copy not isolate nested rows? What is the difference between changing a row cell and replacing a whole row?
