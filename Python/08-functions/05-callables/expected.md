# Expected results — Built-ins, named functions, and lambdas

These are checking targets, not implementation code. Preserve the output order when the task specifies it. Input prompt text may differ where stated.

~~~text
['Hanoi', 'Hue']
[1, 4, 9]
2
~~~

## Additional checks

Pass normalize_city without calling it at the call site. Empty values must return an empty list without calling the operation.

## Explain your result

Why is passing len different from passing len(values)? What makes a function easier to test independently?
