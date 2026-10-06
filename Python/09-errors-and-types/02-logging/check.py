"""Provided checker, not the learner implementation."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m, tmp):
    from unittest.mock import Mock
    logger = Mock()
    details = {"run_id": "r1", "accepted": 3, "token": "secret", "password": "hidden"}
    expected = {"event": "complete", "run_id": "r1", "accepted": 3}
    result = m.emit_event(logger, "complete", details)
    assert result == expected, "allowlist only"
    logger.info.assert_called_once_with(expected)
    assert details["token"] == "secret", "do not mutate input"
    assert result is not details

if __name__ == "__main__":
    run_checks(__file__, verify)
