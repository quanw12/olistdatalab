# Parquet and explicit storage schemas

Original Python-for-DE extension. [Source reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html).

## Concept and purpose

Parquet stores typed columns and metadata in a binary file. Column-oriented storage can avoid reading unneeded columns and can compress repeated values. It does not repair inconsistent schemas or guarantee that every tiny operation is faster.

pandas.to_parquet uses an engine such as pyarrow. index=False avoids writing an accidental DataFrame index. read_parquet(..., columns=[...]) requests selected columns.

Explicit dtypes matter for empty batches too. A missing integer column or a cents field inferred as text breaks compatibility. This exercise uses string fields and an int64 amount. In real systems also decide nullability and numeric bounds.

Partitioning can help selective reads on larger data, but a partition per order ID creates many tiny files. Choose partitioning based on query patterns and measurement.

## Syntax example

~~~python
import pandas as pd
from tempfile import TemporaryDirectory
from pathlib import Path
with TemporaryDirectory() as directory:
    path=Path(directory)/"sample.parquet"
    pd.DataFrame({"id":["A"],"cents":[100]}).to_parquet(path,engine="pyarrow",index=False)
    print(pd.read_parquet(path,columns=["cents"]).to_dict("records"))
~~~

## Trace

The result is [{'cents': 100}]. The selected column remains numeric.

## DE connection

Stable storage schemas let batches combine predictably.

Use [exercise.py](exercise.py) for the exact input/output contract.


## API quick reference

| Syntax | Purpose |
|---|---|
| `frame.astype({'amount_cents': 'int64'})` | Choose a storage type only after checking values fit it. |
| `frame.to_parquet(path, index=False, engine='pyarrow')` | Write Parquet using the configured engine. |
| `pd.read_parquet(path, engine='pyarrow')` | Read back and verify values plus dtypes; file existence is insufficient. |
