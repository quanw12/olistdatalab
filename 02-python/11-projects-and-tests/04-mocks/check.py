"""Provided checking infrastructure, not your implementation."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m,tmp):
    from unittest.mock import Mock,call
    client=Mock();response=client.get.return_value
    response.json.return_value={"count":0}
    assert m.fetch_count(client)==0
    client.get.assert_called_once_with("/orders",timeout=5)
    assert response.mock_calls[:2]==[call.raise_for_status(),call.json()],"status before JSON"
    for payload in [{},{"count":True},{"count":-1},{"count":"2"},[]]:
        client=Mock();client.get.return_value.json.return_value=payload
        raises(ValueError,lambda:m.fetch_count(client))
    client=Mock();client.get.return_value.raise_for_status.side_effect=RuntimeError("503")
    raises(RuntimeError,lambda:m.fetch_count(client))
    client.get.return_value.json.assert_not_called()

if __name__ == "__main__":
    run_checks(__file__, verify)
