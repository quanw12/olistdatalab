# Day 16 — ETL, file layers, and a complete batch pipeline


Base: input 8/accepted 8/rejected 0. Invalid fixture: input 10/accepted 8/rejected 2, with useful temperature/humidity reasons. When the DB contains only base data, both leave staging 8/fact 8. Raw content remains unchanged; clean timestamps carry UTC offsets; each run has a separate directory. Fixture mode works offline and manifests do not announce success before commit.
