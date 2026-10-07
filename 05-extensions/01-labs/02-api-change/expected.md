# LAB02 — Acceptance and evidence

The task's acceptance contract remains in the assignment. Attempt it before opening worked results or reflection explanations.

<details>
<summary>After your attempt — results and explanations</summary>

Both illustrated inputs return {"sku": "A", "units": 7}. v1 quantity "0" is accepted. v2 True, v1 "7.0", version 3 and an empty sku fail with ValueError. Store the original payload and compare it after calling the function.

## Reflection

1. Why should downstream code not know the API version?

2. What bug could accepting True as units hide?

<details>
<summary>After your reflection: compare the reasoning</summary>

The adapter isolates external naming/version changes behind one stable internal shape. Python bool is a subclass of int, so a broad integer check could accept True as one unit; an exact integer policy rejects that ambiguity.

</details>

</details>
