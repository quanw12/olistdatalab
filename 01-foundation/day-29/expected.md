# Day 29 — Rehearse end to end and recover from failures


All recorded fixture transitions match8→8→10→10→10, with corrected HCMC32.5 retained. Invalid batch remains input 10/accepted 8/rejected 2 and stored 10 after corrections. Controlled failures demonstrate atomic DB/checkpoint rollback, finite retries and honest post-commit file failure handling. Rehearsal notes distinguish actual runs, simulated failures and anything unverified.
