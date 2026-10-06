"""Provided checking infrastructure, not your implementation."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m,tmp):
    import json,sqlite3
    from contextlib import closing
    source=Path(__file__).resolve().parents[2]/"data"
    original=(source/"orders.csv").read_bytes()
    database=tmp/"state.sqlite";out=tmp/"output"
    first=m.run_pipeline(source/"orders.csv",database,out)
    assert first=={"input_rows":8,"accepted_rows":4,"rejected_rows":4,"stored_rows":3,"total_cents":3050}, "base counts"
    assert json.loads((out/"manifest.json").read_text(encoding="utf-8"))==first
    rejected=[json.loads(line) for line in (out/"rejected.jsonl").read_text(encoding="utf-8").splitlines()]
    assert len(rejected)==4
    assert sorted(x["reason"] for x in rejected)==["amount","amount","city","time"]
    assert [x["row_number"] for x in rejected]==[6,7,8,9], "CSV record numbering"
    assert rejected[0]["raw"]["city"]==" ", "preserve the raw rejected value"
    assert m.run_pipeline(source/"orders.csv",database,out)==first
    second=m.run_pipeline(source/"orders_next.csv",database,out)
    assert second=={"input_rows":3,"accepted_rows":3,"rejected_rows":0,"stored_rows":4,"total_cents":3850}, "correction/stale handling"
    replay=m.run_pipeline(source/"orders.csv",database,out)
    assert replay["stored_rows"]==4 and replay["total_cents"]==3850
    assert json.loads((out/"report.json").read_text(encoding="utf-8"))==[{"city":"Da Nang","total_cents":0},{"city":"Hanoi","total_cents":1500},{"city":"Hue","total_cents":2350}]
    with closing(sqlite3.connect(database)) as c:
        assert c.execute("SELECT COUNT(*) FROM batches").fetchone()[0]==2
    conflict=tmp/"conflict.csv"
    conflict.write_text("order_id,city,amount,updated_at\nNEW,Hue,1.00,2026-10-03T00:00:00Z\nA2,Hue,24.00,2026-10-02T08:00:00+07:00\n",encoding="utf-8")
    raises(ValueError,lambda:m.run_pipeline(conflict,database,out),"equal-version conflict")
    with closing(sqlite3.connect(database)) as c:
        assert c.execute("SELECT COUNT(*) FROM orders").fetchone()[0]==4,"partial state persisted"
        assert c.execute("SELECT COUNT(*) FROM batches").fetchone()[0]==2,"failed batch checkpointed"
    # Publication failure after ingestion can be repaired by replay.
    output_file=tmp/"not_a_directory";output_file.write_text("occupied",encoding="utf-8")
    repairdb=tmp/"repair.sqlite"
    raises(OSError,lambda:m.run_pipeline(source/"orders.csv",repairdb,output_file))
    repaired=m.run_pipeline(source/"orders.csv",repairdb,tmp/"repaired")
    assert repaired==first
    assert (tmp/"repaired"/"manifest.json").is_file()
    empty=tmp/"empty.csv"
    empty.write_text("order_id,city,amount,updated_at\n",encoding="utf-8")
    result=m.run_pipeline(empty,tmp/"empty.sqlite",tmp/"emptyout")
    assert result=={"input_rows":0,"accepted_rows":0,"rejected_rows":0,"stored_rows":0,"total_cents":0}
    assert json.loads((tmp/"emptyout"/"report.json").read_text(encoding="utf-8"))==[]
    for index,body in enumerate([
        "order_id,city,amount,amount\nA,Hue,1,1\n",
        "order_id,city,amount,updated_at\nA,Hue,1\n",
        "order_id,city,amount,updated_at\nA,Hue,1,t,extra\n",
    ]):
        malformed=tmp/f"malformed{index}.csv"; malformed.write_text(body,encoding="utf-8")
        bad_database=tmp/f"malformed{index}.sqlite"
        bad_output=tmp/f"malformed{index}out"
        raises(ValueError,lambda:m.run_pipeline(malformed,bad_database,bad_output),"malformed file")
        assert not bad_database.exists() and not bad_output.exists(), "validate shape before loading/publishing"
    assert (source/"orders.csv").read_bytes()==original, "do not modify source data"

if __name__ == "__main__":
    run_checks(__file__, verify)
