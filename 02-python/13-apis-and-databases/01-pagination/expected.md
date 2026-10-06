# Expected results — HTTP responses, pagination, and bounded extraction

The shared API fixture returns A1, A2, A3 in that order. An empty intermediate page is followed. page1 -> page1 fails after one call. A two-page chain with max_pages=1 fails before page2 is requested.

check.py prints PASS when all included cases succeed. Missing functions are expected until implemented.

## Reflection

Why separate pagination from HTTP retries?

<details>
<summary>Reveal reasoning after answering</summary>

They solve different problems. Pagination controls completeness and traversal; retries decide whether/how to repeat one failed request. Separating them allows focused tests.

</details>
