# Day 22 — Meaningful automated tests with pytest


Begin with the valid raw envelope and assert exact normalized UTC time/temperature/source. Then change just one field per case and assert a field-specific ValueError. A broad 'any exception' assertion can pass for the wrong bug.

Use copy.deepcopy for nested fixture input. Compare the original object before/after normalization to prove no mutation. For retry tests, assert the number of calls and delays as well as the returned envelope.

Test transform_batch counts on raw_batch_with_errors.json. For manifest timing, inject a failing loader and assert no success manifest is published; use tmp_path.

Run python -m pytest -m "not integration" -q. Integration test files must not connect while being imported/collected, because marker deselection happens after collection. Put connections inside fixtures/test bodies. Before running integration, set PGDATABASE=weather_course_test and verify current_database() inside the test fixture.

A meaningful rollback check compares both the stored data and watermark before/after a forced failure. A test that simply mocks commit() is insufficient.
