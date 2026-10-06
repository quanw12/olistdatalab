# Day 16 — ETL, file layers, and a complete batch pipeline


Implement transform.py and pipeline.py. Add the run CLI: --mode fixture/live, --input for fixture, --cities for live, --output-dir for either. Follow the shared contract.

Create output/<run_id>/raw.json, clean.json, rejected.json and manifest.json. Include mode, counts, status, file paths and start/end times. Quarantined rows produce a warning status while valid accepted rows may commit. Database failure rolls back the accepted batch and fails the run.

Run the base and invalid raw batches. Explain why accepted 8 does not mean eight NEW database rows. Optionally compare CSV with Parquet.
