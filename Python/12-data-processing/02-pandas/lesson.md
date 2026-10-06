# pandas joins, types, and trustworthy totals

Original Python-for-DE extension. [Source reference](https://pandas.pydata.org/docs/user_guide/merging.html).

## Concept and purpose

A DataFrame has named columns and dtypes. Inspect missing values and inferred types before assuming a CSV column is numeric.

A merge has a cardinality contract. An order-to-city dimension should be many-to-one; duplicate dimension keys can multiply fact rows and inflate totals. validate="many_to_one" detects that shape. indicator=True records whether each key matched.

pandas can match null keys to other null keys, unlike ordinary SQL equality. Reject null business keys before this exercise's join. A left join followed by an explicit unmatched-row check preserves evidence of missing dimension entries.

Use clear column operations for simple transformations. Do not automatically replace every loop with apply. Empty input also needs a defined output schema and behavior.

## Syntax example

~~~python
import pandas as pd
facts=pd.DataFrame({"city":["Hue","Hue"],"cents":[100,200]})
dim=pd.DataFrame({"city":["Hue"],"region":["central"]})
joined=facts.merge(dim,on="city",validate="many_to_one")
print(joined.groupby("region")["cents"].sum().to_dict())
~~~

## Trace

The central total is 300. Each of two facts matches exactly one dimension row.

## DE connection

A successful merge can still produce incorrect totals if its relationship is wrong.

Use [exercise.py](exercise.py) for the exact input/output contract.
