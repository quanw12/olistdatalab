"""Provided checker, not the learner implementation."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m, tmp):
    import json
    path = tmp / "nested" / "result.json"
    m.write_atomic_json(path, {"city": "Huế"})
    assert json.loads(path.read_text(encoding="utf-8")) == {"city": "Huế"}
    before = path.read_bytes()
    raises(TypeError, lambda: m.write_atomic_json(path, {"bad": {1}}))
    assert path.read_bytes() == before, "serialization failure changed old output"
    raises(ValueError, lambda: m.write_atomic_json(path, {"bad": float("nan")}))
    assert path.read_bytes() == before
    assert list(path.parent.iterdir()) == [path], "temporary files left behind"

if __name__ == "__main__":
    run_checks(__file__, verify)
