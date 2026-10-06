# Expected results — Indexing and slicing without off-by-one errors

These are checking targets, not implementation code. Preserve the output order when the task specifies it. Input prompt text may differ where stated.

~~~text
VN
HCM
2026
6
6202-MCH-NV
[]
~~~

## Additional checks

Use slices rather than hardcoding pieces or calling split. Explain the different behavior of code[20] and code[20:].

## Explain your result

Why is the stop index excluded? What happens to a slice when its boundaries are beyond the string?
