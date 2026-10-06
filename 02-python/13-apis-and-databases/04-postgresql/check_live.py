"""Optional real PostgreSQL check against a temporary table only."""
import getpass
import os
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from check_support import load_exercise

def main():
    import psycopg
    if os.environ.get("PGDATABASE") != "python_de_lab":
        raise SystemExit("Set PGDATABASE=python_de_lab before running.")
    module=load_exercise(Path(__file__).with_name("exercise.py"))
    with psycopg.connect(password=getpass.getpass("PostgreSQL password: ")) as connection:
        connection.execute("""CREATE TEMP TABLE orders(
            order_id TEXT PRIMARY KEY, city TEXT NOT NULL,
            amount_cents BIGINT NOT NULL CHECK(amount_cents>=0),
            updated_at TIMESTAMPTZ NOT NULL)""")
        connection.commit()
        base={"order_id":"A","city":"Hue","amount_cents":100,"updated_at":"2026-10-01T01:00:00+00:00"}
        module.upsert_postgres(connection,[base])
        module.upsert_postgres(connection,[dict(base,amount_cents=150,updated_at="2026-10-02T01:00:00+00:00")])
        module.upsert_postgres(connection,[base])
        assert connection.execute("SELECT amount_cents FROM orders WHERE order_id=%s",("A",)).fetchone()[0]==150
        connection.commit()
        try:
            module.upsert_postgres(connection,[dict(base,order_id="B"),dict(base,order_id="C",amount_cents=-1)])
        except psycopg.errors.CheckViolation:
            pass
        else:
            raise AssertionError("negative amount should fail")
        assert connection.execute("SELECT COUNT(*) FROM orders").fetchone()[0]==1, "partial batch persisted"
    print("PASS: PostgreSQL insert/correction/replay/rollback")

if __name__=="__main__":
    main()
