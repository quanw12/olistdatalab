"""Provided checking infrastructure, not your implementation."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m,tmp):
    assert list(m.batches(range(5),2))==[[0,1],[2,3],[4]]
    assert list(m.batches([],2))==[]
    for size in [0,-1,True,1.5]:raises(ValueError,lambda size=size:list(m.batches([],size)))
    consumed=[]
    def source():
        for n in range(6):
            consumed.append(n);yield n
    stream=iter(m.batches(source(),2));first=next(stream)
    assert consumed==[0,1],"eager source consumption"
    next(stream)
    assert first==[0,1],"yielded batch was mutated"

if __name__ == "__main__":
    run_checks(__file__, verify)
