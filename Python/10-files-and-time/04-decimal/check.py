"""Provided checker, not the learner implementation."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m, tmp):
    for text, value in [("20.50",2050), (" 1.2300 ",123), ("0",0), ("1000000",100000000)]:
        assert m.to_cents(text) == value, text
    for text in ["1.001","-0.01","NaN","Infinity","oops","","1000001"]:
        raises(ValueError, lambda text=text: m.to_cents(text), text)
    raises(TypeError, lambda: m.to_cents(1.2))

if __name__ == "__main__":
    run_checks(__file__, verify)
