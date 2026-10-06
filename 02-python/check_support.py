"""Local exercise-checking infrastructure. No learner implementations."""
import importlib.util
import sys
import tempfile
import traceback
from pathlib import Path

def load_exercise(path):
    name = "learner_" + path.parent.parent.name.replace("-", "_") + "_" + path.parent.name.replace("-", "_")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    sys.path.insert(0, str(path.parent))
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.pop(0)
    return module

def raises(kind, operation, label="expected exception"):
    try:
        operation()
    except kind:
        return
    except Exception as exc:
        raise AssertionError(f"{label}: expected {kind.__name__}, got {type(exc).__name__}") from exc
    raise AssertionError(f"{label}: expected {kind.__name__}, but nothing was raised")

def run_checks(check_path, verify):
    lesson = Path(check_path).resolve().parent
    try:
        module = load_exercise(lesson / "exercise.py")
        with tempfile.TemporaryDirectory(prefix="python_de_check_") as directory:
            verify(module, Path(directory))
    except (Exception, SystemExit) as exc:
        traceback.print_exc(limit=4)
        print(f"FAIL: {lesson.name}: {type(exc).__name__}: {exc}")
        print("Read the matching requirement in exercise.py and hint in help.md. Do not change check.py.")
        raise SystemExit(1)
    print(f"PASS: {lesson.name}")
