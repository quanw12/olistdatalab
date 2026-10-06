"""Provided checker, not the learner implementation."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m, tmp):
    assert m.parse_count(" 0042 ") == 42, "strip and convert"
    assert m.parse_count("0") == 0
    assert m.parse_count("10000") == 10000
    for x in ["", "-1", "1.2", "١٢", "10001", "abc"]:
        raises(ValueError, lambda x=x: m.parse_count(x), repr(x))
    for x in [None, 4, True]:
        raises(TypeError, lambda x=x: m.parse_count(x), repr(x))

if __name__ == "__main__":
    run_checks(__file__, verify)
