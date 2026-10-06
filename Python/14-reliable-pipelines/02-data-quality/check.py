"""Provided checking infrastructure, not your implementation."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m,tmp):
    from datetime import datetime,timezone
    now=datetime(2026,10,2,tzinfo=timezone.utc)
    rows=[{"order_id":"A","city":"Hue","amount_cents":0,"updated_at":"2026-10-01T00:00:00+00:00"},
          {"order_id":"A","city":"","amount_cents":True,"updated_at":"2026-09-30T23:00:00+00:00"},
          {"order_id":"B","city":"Hanoi","amount_cents":100,"updated_at":"2026-10-02T01:00:00+00:00"}]
    assert m.quality_report(rows,now)=={"rows":3,"duplicate_ids":1,"blank_city":1,"invalid_amount":1,"stale":1,"future":1}
    assert m.quality_report([],now)==dict.fromkeys(["rows","duplicate_ids","blank_city","invalid_amount","stale","future"],0)
    raises(ValueError,lambda:m.quality_report([],datetime(2026,10,2)))
    raises(ValueError,lambda:m.quality_report([],now,-1))

if __name__ == "__main__":
    run_checks(__file__, verify)
