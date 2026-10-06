# Day 20 — Orchestration with Prefect flows and tasks


Create capstone/orchestration.py. Wrap existing functions in one weather flow with observable extraction/transform/load stages. Preserve the single database transaction and disable unintended caching of side effects. Add a main entry point running fixture mode.

Run a successful fixture and one deliberate validation/database failure. Capture their distinct Prefect states. Demonstrate retry syntax using an isolated fake task, then explain which layer owns retries in the real pipeline.
