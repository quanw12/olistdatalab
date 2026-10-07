# CL07 — Assignment

Implement allow_query(estimated_bytes, limit_bytes): exact nonnegative ints only, ValueError otherwise; return estimated_bytes <= limit_bytes.

Write cost-notes.md with a tiny estimate, an above-limit refusal and an execution with an explicit maximum_bytes_billed. List other billable resources separately. Include an owned-resource cleanup checklist; do not delete a shared project or bucket. A local boolean check is not actual billing enforcement.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
