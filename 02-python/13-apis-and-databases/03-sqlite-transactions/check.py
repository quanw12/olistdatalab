"""Provided checking infrastructure, not your implementation."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m,tmp):
    import sqlite3
    c=sqlite3.connect(":memory:",autocommit=False)
    try:
        c.execute("CREATE TABLE orders(order_id TEXT PRIMARY KEY,city TEXT NOT NULL,amount_cents INTEGER CHECK(amount_cents>=0),updated_at TEXT NOT NULL)")
        c.commit()
        rows=[{"order_id":"A","city":"O'Brien","amount_cents":100,"updated_at":"t"},{"order_id":"B","city":"Hue","amount_cents":0,"updated_at":"t"}]
        assert m.load_sqlite(c,rows)==2
        assert m.load_sqlite(c,rows)==0
        assert c.execute("SELECT city FROM orders WHERE order_id='A'").fetchone()[0]=="O'Brien"
        c.commit()
        bad=[dict(rows[0],order_id="C"),dict(rows[0],order_id="D",amount_cents=-1)]
        raises(sqlite3.IntegrityError,lambda:m.load_sqlite(c,bad))
        assert c.execute("SELECT count(*) FROM orders").fetchone()[0]==2,"partial batch committed"
    finally:c.close()

if __name__ == "__main__":
    run_checks(__file__, verify)
