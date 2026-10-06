# Help — pandas joins, types, and trustworthy totals

## First hint

Validate dimension keys, merge left with validation/indicator, then aggregate.

## Detailed approach

Use isna and duplicated checks. Merge with how='left', validate='many_to_one', indicator=True; require all _merge values to equal 'both'. Group, sum, rename amount_cents, sort and reset the index. Detecting unmatched facts after an inner join is too late.

## Troubleshooting

Unexpectedly high totals suggest duplicate dimension keys. Missing totals suggest silently dropped unmatched facts.

Read the first failing check, compare input/type/output and side effects, then make one focused change. The checker is an executable specification.

## Break pandas operations into visible steps

~~~python
import pandas as pd

frame = pd.DataFrame({"group": ["a", "a", "b"], "value": [2, 3, 4]})
print(frame["group"].isna().any())
summary = frame.groupby("group", as_index=False)["value"].sum()
summary = summary.rename(columns={"value": "total"})
summary = summary.sort_values("group").reset_index(drop=True)
print(summary.to_dict(orient="records"))
~~~

frame["group"] selects one Series. isna produces Boolean flags; any reduces them to one yes/no result. groupby forms groups; sum adds each group's values. as_index=False leaves the group as a normal column. rename changes an output column label. reset_index(drop=True) gives consecutive row positions without preserving the old index as a column.

For the exercise, first reject missing keys and duplicated city keys in the dimension. Then inspect an intermediate left merge with indicator=True. _merge == "left_only" identifies an order with no dimension match. Raise a clear ValueError before grouping when such rows exist. Never replace their region with a guessed value.

Use copies or expressions that return new frames. Keep the promised columns for empty input too.
