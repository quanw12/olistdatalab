"""Provided checker, not the learner implementation."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m, tmp):
    import json
    path = tmp / "input.csv"
    path.write_text('order_id,city,amount,updated_at\nA1,"Hue, Central",10.00,t\n', encoding="utf-8")
    rows = m.read_orders_csv(path)
    assert rows[0]["city"] == "Hue, Central"
    assert rows[0]["amount"] == "10.00"
    out = tmp / "out.jsonl"
    m.write_jsonl(out, rows * 2)
    assert [json.loads(x) for x in out.read_text(encoding="utf-8").splitlines()] == rows * 2
    m.write_jsonl(out, [])
    assert out.read_text(encoding="utf-8") == ""
    for body in ["city,amount\nx,1\n", "order_id,city,amount,updated_at\nA1,Hue,1\n", "order_id,city,amount,updated_at\nA1,Hue,1,t,extra\n", "order_id,city,amount,amount\nA,H,1,2\n"]:
        path.write_text(body, encoding="utf-8")
        raises(ValueError, lambda: m.read_orders_csv(path))
    path.write_text("order_id,city,amount,updated_at\n", encoding="utf-8")
    assert m.read_orders_csv(path) == []

if __name__ == "__main__":
    run_checks(__file__, verify)
