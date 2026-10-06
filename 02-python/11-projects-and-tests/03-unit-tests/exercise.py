# C11-L03 — Tests that detect meaningful defects
# Implement your own solution below these problem statements.
#
# Implement build_suite(normalize) -> unittest.TestSuite containing at least four test methods.
# Contract of the supplied callable: accept str, strip surrounding whitespace, lowercase; reject blank-after-strip with ValueError; reject non-str with TypeError.
# Tests must pass a correct implementation and fail variants that omit strip, omit lowercase, accept blank, or coerce non-text.
# Do not implement normalize or inspect its source/name. Return fresh test instances on every call.
# See help.md for hints and expected.md for cases.
