# LAB06 — Assignment

Implement enrich_movements(rows, products). rows is a list of dictionaries containing sku; products is a list of {"sku": string, "category": string}. Assume other row fields are valid. Trim sku for lookup only; preserve the original row's sku and other fields. Reject empty/non-string SKUs, non-string categories and duplicate normalized dimension SKUs with ValueError. Unknown product → category=None. Return a new list of copied rows in the input order; overwrite an existing category in the copied row. Do not mutate either input.

Use benchmark.py to compare baseline and implementation, record elapsed values and a cProfile observation. Add your own unknown/duplicate tests. The benchmark is provided instrumentation, not a solution.

## Deliver

Submit your implementation, your own regression tests and the evidence listed in [expected.md](expected.md). Explain one changed input before committing.
