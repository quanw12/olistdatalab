# Day 23 — Data quality and deterministic freshness checks


Implement quality.py and the quality CLI from the contract. Check structural validity, unique identities, dimension references, local-date consistency, configured-city completeness and freshness. Filter by --source and write a machine-readable report.

Use a freshly bootstrapped weather_course_test with base data only for the fixed check. Then load next and demonstrate the expected freshness change. Add unit cases for missing/future/exact-threshold observations. Explain which checks protect loading and which describe monitoring outcomes.
