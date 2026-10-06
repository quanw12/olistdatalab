# Help — Metric definitions and honest analytics

## First hint

Separate arithmetic evidence from causal explanations.

## Detailed approach

Show the two changes: A +200, B -1500, C +800, net -500. Define whether c2 remains in a customer table with zero versus omitted from active-only mart. If computing a rate, write numerator and denominator first. Label cents/currency clearly; divide by 100 only for presentation. The tiny synthetic sample cannot establish seasonality or customer behavior.

## Troubleshooting

A LEFT JOIN COUNT(*) can give one for a zero-order customer; count a non-null order key. Never silently fill an unknown monetary amount with zero.

If stuck, write the smallest input, expected result and actual result. Check interpreter, cwd, schema and units before changing multiple things. Preserve the error; do not silently return success.

