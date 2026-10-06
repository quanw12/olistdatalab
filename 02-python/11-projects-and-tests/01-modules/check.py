"""Provided checking infrastructure, not your implementation."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m,tmp):
    import io, contextlib
    assert m.main([" hanoi "," "," hue "]) == ["Hanoi","Hue"]
    assert m.main([]) == []
    out=io.StringIO()
    with contextlib.redirect_stdout(out): m.main(["hue"])
    assert out.getvalue()=="", "main returns; entry point prints"

if __name__ == "__main__":
    run_checks(__file__, verify)
