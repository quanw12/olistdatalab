# Expected results — Incremental state, replays, and corrections

A=100 on day 1 corrected to 150 on day 2 stays 150 after a day-1 replay. A new B is inserted. Equal day-2 A=160 conflicts. Repeating the same batch returns equal state.

check.py prints PASS when all included cases succeed. Missing functions are expected until implemented.

## Reflection

Why does 'drop duplicate IDs' lose valid information?

<details>
<summary>Reveal reasoning after answering</summary>

The same ID can represent a newer correction. Deduplication needs a version/winner rule, not just a seen-key set.

</details>
