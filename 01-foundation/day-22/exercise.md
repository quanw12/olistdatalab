# Day 22 — Meaningful automated tests with pytest


Create capstone/tests and pytest.ini. Write at least eight meaningful unit cases covering: UTC conversion; missing field; bool/fractional/out-of-range humidity; nonfinite temperature; batch counts; raw-input immutability; retry503→200; permanent400; retry exhaustion; and manifest files under tmp_path. Parametrized cases can cover multiple values.

Write separately marked PostgreSQL integration tests for replay, correction, old replay, and atomic rollback including checkpoint. Use only weather_course_test. Record actual passed/skipped counts; do not claim integration passed if you did not run it.
