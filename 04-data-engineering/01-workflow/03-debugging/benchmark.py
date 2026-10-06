"""Provided bounded workload for the learner's corrected implementation."""
from pathlib import Path
import importlib.util

def main():
    path = Path(__file__).with_name("exercise.py")
    spec = importlib.util.spec_from_file_location("profiled_exercise", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    build_report = getattr(module, "build_report", None)
    if not callable(build_report):
        raise RuntimeError("implement build_report in exercise.py before profiling")
    rows = [{"customer_id": f" c{i % 100} ", "amount_cents": 7} for i in range(50000)]
    for _ in range(5):
        result = build_report(rows)
        assert len(result) == 100 and sum(result.values()) == 350000, "incorrect aggregate"
    print("profile workload: 5 calls, 50000 rows/call, 100 customers, 350000 cents/call")

if __name__ == "__main__":
    main()
