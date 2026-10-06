"""Provided checking infrastructure, not your implementation."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m,tmp):
    pages={"page1":{"items":[1],"next":"p2"},"p2":{"items":[],"next":"p3"},"p3":{"items":[2],"next":None}}
    calls=[]
    def get(token):calls.append(token);return pages[token]
    assert m.fetch_all(get)==[1,2]
    assert calls==["page1","p2","p3"]
    calls.clear()
    raises(ValueError,lambda:m.fetch_all(get,max_pages=1))
    assert calls==["page1"],"request bound"
    calls.clear()
    def loop(token):calls.append(token);return {"items":[],"next":token}
    raises(ValueError,lambda:m.fetch_all(loop))
    assert len(calls)==1,"cycle guard"
    for page in [{},{"items":"bad","next":None},{"items":[],"next":3}]:
        raises(ValueError,lambda page=page:m.fetch_all(lambda token:page))
    raises(ValueError,lambda:m.fetch_all(get,max_pages=0))

if __name__ == "__main__":
    run_checks(__file__, verify)
