"""Provided checking infrastructure, not your implementation."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m,tmp):
    import pandas as pd
    orders=pd.DataFrame({"city":["Hanoi","Hue","Da Nang"],"amount_cents":[1000,2050,0]})
    cities=pd.DataFrame({"city":["Hanoi","Hue","Da Nang"],"region":["north","central","central"]})
    before=orders.copy(deep=True)
    assert m.region_totals(orders,cities).to_dict("records")==[{"region":"central","total_cents":2050},{"region":"north","total_cents":1000}]
    pd.testing.assert_frame_equal(orders,before)
    assert list(m.region_totals(orders.iloc[:0],cities).columns)==["region","total_cents"]
    raises(ValueError,lambda:m.region_totals(orders,pd.concat([cities,cities.iloc[:1]],ignore_index=True)))
    raises(ValueError,lambda:m.region_totals(orders,cities.iloc[:1]))
    bad=orders.copy();bad.loc[0,"city"]=None
    raises(ValueError,lambda:m.region_totals(bad,cities))

if __name__ == "__main__":
    run_checks(__file__, verify)
