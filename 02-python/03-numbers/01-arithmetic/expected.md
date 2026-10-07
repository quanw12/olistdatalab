# Expected results — Integers, floats, and arithmetic

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

These are checking targets, not implementation code. Preserve the output order when the task specifies it. Input prompt text may differ where stated.

~~~text
4
3
4.6
3750
86.0
-3
2
~~~

## Additional checks

Manually check full_batches * batch_size + remainder == records. A batch size of zero would raise ZeroDivisionError; do not silently choose another divisor.

## Explain your result

When do you want / instead of //? Why is integer cents useful for exact arithmetic?

</details>
