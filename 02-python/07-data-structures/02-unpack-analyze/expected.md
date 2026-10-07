# Expected results — Unpack rows and analyze lists

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

These are checking targets, not implementation code. Preserve the output order when the task specifies it. Input prompt text may differ where stated.

~~~text
Nonempty case:
count: 3
min: 29.0
max: 33.0
avg: 31.0
Hanoi 31.0

Empty case:
count: 0
min: None
max: None
avg: None
Hanoi 31.0
~~~

## Additional checks

Do not use zero as a replacement for a missing average. A single value [0.0] must produce a valid average of 0.0.

## Explain your result

Why is a missing average different from zero? When does ordinary unpacking raise ValueError?

</details>
