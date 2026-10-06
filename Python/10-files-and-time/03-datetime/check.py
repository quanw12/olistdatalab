"""Provided checker, not the learner implementation."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m, tmp):
    expected = "2026-10-01T01:00:00.000000+00:00"
    assert m.utc_text("2026-10-01T08:00:00+07:00") == expected
    assert m.utc_text("2026-10-01T01:00:00Z") == expected
    assert m.utc_text("2026-10-01T08:00:00.123456+07:00") == "2026-10-01T01:00:00.123456+00:00"
    for text in ["2026-10-01T08:00:00", "2026-10-01", "2026-02-30T00:00:00Z"]:
        raises(ValueError, lambda text=text: m.utc_text(text))

if __name__ == "__main__":
    run_checks(__file__, verify)
