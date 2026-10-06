# Help — Decimal parsing and exact money

## First hint

Check Decimal finiteness before comparison. Compare cents to its integral value.

## Detailed approach

After construction, test amount.is_finite(), 0 <= amount <= Decimal('1000000'), then cents = amount * 100. cents != cents.to_integral_value() detects a fractional cent. Convert only the accepted result with int(cents). Catch InvalidOperation for malformed input and re-raise ValueError. The defined maximum keeps this lab's arithmetic within ordinary decimal precision.

## Troubleshooting

NaN can make ordering raise unexpectedly. If 1.001 becomes 100, int was applied too early. Decimal(0.1) begins with a float approximation; use original text.

For a failed assertion, compare the input, expected type and value, and any side effect. Rerun the checker after one focused change. If stuck, read the test case in check.py; it is an executable specification.
