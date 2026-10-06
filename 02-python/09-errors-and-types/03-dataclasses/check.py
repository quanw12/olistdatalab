"""Provided checker, not the learner implementation."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m, tmp):
    from dataclasses import is_dataclass, FrozenInstanceError
    assert is_dataclass(m.Order), "use a dataclass"
    order = m.Order("A1", 100)
    assert m.order_dict(order) == {"order_id": "A1", "amount_cents": 100}
    assert m.Order("A1", 0).amount_cents == 0
    raises(FrozenInstanceError, lambda: setattr(order, "amount_cents", 5))
    for args in [("", 0), (" ", 0), (None, 0), ("A", -1), ("A", True), ("A", "10")]:
        raises(ValueError, lambda args=args: m.Order(*args), repr(args))

if __name__ == "__main__":
    run_checks(__file__, verify)
