"""Provided checking infrastructure, not your implementation."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m,tmp):
    import pandas as pd
    rows=[{"order_id":"A","city":"Hue","amount_cents":105,"updated_at":"2026-10-01T01:00:00.000000+00:00"}]
    p=tmp/"orders.parquet"
    assert m.write_read_parquet(rows,p)==rows
    frame=pd.read_parquet(p)
    assert list(frame.columns)==["order_id","city","amount_cents","updated_at"]
    assert str(frame["amount_cents"].dtype)=="int64"
    assert m.write_read_parquet([],p)==[]
    assert list(pd.read_parquet(p).columns)==list(frame.columns)

if __name__ == "__main__":
    run_checks(__file__, verify)
