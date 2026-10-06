"""Provided checking infrastructure, not your implementation."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from check_support import run_checks, raises

def verify(m,tmp):
    import unittest
    def good(x):
        if not isinstance(x,str):raise TypeError("text")
        x=x.strip().lower()
        if not x:raise ValueError("blank")
        return x
    def no_strip(x):
        if not isinstance(x,str):raise TypeError("text")
        if not x.strip():raise ValueError("blank")
        return x.lower()
    def no_lower(x):
        if not isinstance(x,str):raise TypeError("text")
        x=x.strip()
        if not x:raise ValueError("blank")
        return x
    def blank(x):
        if not isinstance(x,str):raise TypeError("text")
        return x.strip().lower()
    def coerce(x):return str(x).strip().lower()
    for label,fn,ok in [("correct",good,True),("no strip",no_strip,False),("no lowercase",no_lower,False),("blank accepted",blank,False),("coercion",coerce,False)]:
        suite=m.build_suite(fn)
        assert isinstance(suite,unittest.TestSuite)
        assert suite.countTestCases()>=4,"at least four tests"
        result=unittest.TestResult();suite.run(result)
        assert result.wasSuccessful()==ok,label

if __name__ == "__main__":
    run_checks(__file__, verify)
