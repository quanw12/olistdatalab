"""Provided checking infrastructure, not your implementation."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m,tmp):
    import json,io,contextlib
    args=m.parse_args(["--input","a.csv"])
    assert args.input=="a.csv" and args.limit==100
    assert m.parse_args(["--input","a","--limit","2"]).limit==2
    with contextlib.redirect_stderr(io.StringIO()):
        raises(SystemExit,lambda:m.parse_args([]))
        raises(SystemExit,lambda:m.parse_args(["--input","a","--limit","0"]))
    p=tmp/"config.json"
    p.write_text(json.dumps({"source":" fixture ","batch_size":2,"token":"x"}),encoding="utf-8")
    assert m.load_settings(p)=={"source":"fixture","batch_size":2}
    for data in [{},[],{"source":"x","batch_size":True},{"source":" ","batch_size":2},{"source":"x","batch_size":0}]:
        p.write_text(json.dumps(data),encoding="utf-8")
        raises(ValueError,lambda:m.load_settings(p))

if __name__ == "__main__":
    run_checks(__file__, verify)
