"""Provided checking infrastructure, not your implementation."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m,tmp):
    from unittest.mock import MagicMock
    c=MagicMock()
    row={"order_id":"A","city":"O'Brien","amount_cents":100,"updated_at":"2026-10-01T01:00:00+00:00"}
    assert m.upsert_postgres(c,[row]) is None
    c.transaction.assert_called_once_with()
    c.transaction.return_value.__enter__.assert_called_once()
    cursor=c.cursor.return_value.__enter__.return_value
    cursor.executemany.assert_called_once()
    sql,params=cursor.executemany.call_args.args
    assert "O'Brien" not in sql,"values must not enter SQL"
    assert sql.count("%s")==4
    normalized=" ".join(sql.upper().split())
    assert "ON CONFLICT" in normalized and "WHERE" in normalized and ">" in normalized
    assert list(params)==[("A","O'Brien",100,"2026-10-01T01:00:00+00:00")]

if __name__ == "__main__":
    run_checks(__file__, verify)
