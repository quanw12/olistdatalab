# LAB02 — Assignment

Implement normalize_stock(payload).

- v1: {"api_version": 1, "item": {"sku": " A ", "quantity": "007"}}.
- v2: {"api_version": 2, "product": {"sku": "A"}, "stock": {"units": 7}}.

Return exactly {"sku": "A", "units": 7}. sku must be a nonempty trimmed string. In v1 quantity is a trimmed string of ASCII digits only; in v2 units must be an exact int. Range: 0–10000 inclusive. api_version must be an exact int 1 or 2. Reject unknown versions, missing/incorrect nested types, invalid digits, bool and out-of-range units with ValueError. Extra external fields may be ignored. Do not mutate input.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
