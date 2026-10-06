# Expected results — Retry only transient failures

Two timeouts then success: 3 calls, sleeps [1,2]. Three timeouts: 3 calls, sleeps [1,2], exception propagated. Immediate success: one call and no sleeps.

check.py prints PASS when all included cases succeed. Missing functions are expected until implemented.

## Reflection

Why can retrying a write be more dangerous than retrying a read?

<details>
<summary>Reveal reasoning after answering</summary>

The write might have succeeded while the response was lost. A repeated write can duplicate effects unless the operation has an explicit idempotency strategy.

</details>
