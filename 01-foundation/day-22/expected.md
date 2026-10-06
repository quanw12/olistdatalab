# Day 22 — Meaningful automated tests with pytest


Unit tests pass offline and no test writes into real output/. Invalid cases fail for the intended reason. Retry checks use no real waits/network. Integration results are reported separately and use the dedicated DB. Temporarily introducing a known wrong expectation makes a test fail, proving it is discovered; restore it before committing.
