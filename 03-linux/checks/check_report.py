"""Verify fixed-fixture report data served by the local teaching viewer."""
import argparse
import json
from urllib.parse import urlparse
from urllib.request import urlopen


def verify(base):
    parsed=urlparse(base)
    if parsed.scheme!="http" or parsed.hostname not in {"localhost","127.0.0.1"} or parsed.username or parsed.password:
        raise ValueError("Use the local http://127.0.0.1:<port> viewer, without credentials.")
    def read(name):
        with urlopen(base.rstrip("/")+"/"+name,timeout=5) as response:
            return json.load(response)
    manifest=read("manifest.json")
    report=read("report.json")
    expected={"input_rows":6,"accepted_rows":4,"rejected_rows":2,"event_count":3,"total_cents":3050}
    assert manifest==expected,"unexpected manifest"
    assert report=={"event_count":3,"total_cents":3050},"unexpected report"
    assert all(type(value) is int for value in manifest.values()),"manifest integer types"
    assert all(type(value) is int for value in report.values()),"report integer types"
    return manifest


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--url",required=True)
    args=parser.parse_args()
    try:
        verify(args.url)
    except Exception as exc:
        print(f"FAIL: local report: {type(exc).__name__}: {exc}")
        return 1
    print("PASS: local fixture report. Record actual container/run evidence separately.")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
