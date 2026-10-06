# Day 27 — Use AI assistance with deterministic verification


1. Calculate count, unique observed city count, maximum temperature and the city attached to that maximum from CSV. Define a tie policy if generalizing; the supplied maximum is unique.
2. Pass only the proposal string and trusted metrics to your validator. Load expected accept labels separately in the test harness.
3. Catch JSONDecodeError. Then check dict, exact keys, integer counts, string city, finite numeric temperature and no Boolean numeric values.
4. Compare counts/city exactly. Compare the temperature with an explicit tiny tolerance if using floats. Reject missing/extra keys instead of ignoring them.
5. Output case name, decision and reason. Compare against the fixture's expected flags after the decision is computed.
6. Keep the original proposal for traceability; do not replace it with corrected text. Optional live output may be rejected even if it sounds plausible.
