# Day 17 — Incremental loads, corrections, and backfills


| Operation | Stored observations | HCMC Sep19 09:00 local |
|---|---:|---:|
| Base | 8 | 32.0 |
| Next | 10 | 32.5 |
| Replay next | 10 | 32.5 |
| Replay base | 10 | 32.5 |

Final sum 314.0, mean 31.4. Watermark after next:2026-09-19T05:01:00+00:00. Failed transactions change neither data nor checkpoint. Base backfill Sep18..Sep20 reads8 old observations and leaves ten stored rows and the correction intact: replay is not full replacement.
