# Expected results — Nested conditions and validation order

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

These are checking targets, not implementation code. Preserve the output order when the task specifies it. Input prompt text may differ where stated.

~~~text
" " -> missing
"72" -> accepted
"100" -> accepted
"101" -> out of range
"-1" -> bad format
"12.5" -> bad format
~~~

## Additional checks

Each run prints one result. ' 72 ' is accepted after stripping. No exception handler is required because the input contract and guards control conversion.

## Explain your result

Why does validation order change the reported error? Why should parsing happen after the character guard?

</details>
