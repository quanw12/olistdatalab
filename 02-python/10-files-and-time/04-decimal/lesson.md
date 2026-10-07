# Decimal parsing and exact money

Original Python-for-DE extension. [Source reference](https://docs.python.org/3.13/library/decimal.html).

## Concept and purpose

Binary floats approximate many decimal fractions. For currency text, construct Decimal from the original string rather than from a float that has already lost decimal exactness.

A data contract must specify currency, precision, rounding and permitted range. This lab uses fictional units with two decimal places and rejects sub-cent values rather than rounding them. Another business process may use quantize with an explicitly chosen rounding rule.

Decimal accepts special strings such as NaN and Infinity, so successful construction is not enough. Check is_finite before ordering or converting to int. Multiplying an accepted amount by 100 gives integer cents that aggregate exactly.

Catch decimal.InvalidOperation when text is malformed. If your public contract promises ValueError, translate the decimal exception explicitly with raise ... from exc.

## Syntax example

~~~python
from decimal import Decimal, ROUND_HALF_UP
amount = Decimal("2.675")
print(amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
print(Decimal("0.10") + Decimal("0.20"))
~~~

## Trace the example

An explicit half-up rule yields 2.68. Decimal addition from strings yields the exact decimal 0.30. The exercise chooses rejection rather than rounding for excess precision.

## Apply it to DE

Financial totals should not drift because one stage used floats and another used integer cents.

The problem contract is in [exercise.py](exercise.py). The checker supplies fixtures; it does not contain your implementation.


## API quick reference

| Syntax | Purpose |
|---|---|
| `Decimal(text) / InvalidOperation` | Parse decimal text / catch a malformed decimal. |
| `value.is_finite()` | Reject NaN and infinities before range comparisons. |
| `value.to_integral_value()` | Compare with the original scaled amount to detect fractional cents; do not silently round invalid data. |
| `int(value)` | Convert only after validating integrality and range. |
