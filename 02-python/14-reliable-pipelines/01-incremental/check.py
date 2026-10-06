"""Provided checking infrastructure, not your implementation."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m,tmp):
    from copy import deepcopy
    a={"order_id":"A","city":"Hue","amount_cents":100,"updated_at":"2026-10-01T01:00:00.000000+00:00"}
    newer=dict(a,amount_cents=150,updated_at="2026-10-02T01:00:00.000000+00:00")
    b=dict(a,order_id="B")
    old=[a];before=deepcopy(old)
    result=m.merge_latest(old,[newer,b,a])
    assert result==[newer,b]
    assert old==before
    assert m.merge_latest(result,[newer,b,a])==result
    raises(ValueError,lambda:m.merge_latest(result,[dict(newer,amount_cents=160)]))
    result[0]["city"]="Changed"
    assert old==before and newer["city"]=="Hue","shared mutable records"

if __name__ == "__main__":
    run_checks(__file__, verify)
