# Shared fixtures

These are fixed teaching data, not current weather. Never edit a fixture to make an assertion pass. Days1–12 keep their own inputs. Days13–30 use these files and [the capstone contract](../capstone/contract.md).

| File | Purpose |
|---|---|
| cities.csv | Four configured cities with illustrative coordinates; Hue has no base observations |
| weather_batch.json | Eight normalized observations for the first database load |
| weather_batch_next.json | Four inputs: one replay, one newer correction, two new observations |
| raw_batch.json | The same base eight records in raw API-envelope form |
| raw_batch_with_errors.json | Base eight plus two invalid records: nonnumeric temperature and humidity 110 |
| api_response.json | One API body for an HTTP mock; no request metadata |
| weather_base.csv | Independent fixed input for warehouse/analytics lessons |
| llm_cases.json | Five saved AI proposal strings, with expected accept/reject decisions |

## Known results

Base: 8 distinct observations; sum 251.0, min 29.0, max 34.0, mean 31.375 (31.38 to two decimals). Three observed cities, four configured cities. Hanoi3/mean 31.0; Da Nang2/29.5; HCMC3/33.0; Hue0/NULL.

After the next batch: 10 distinct observations; sum 314.0, mean 31.4. The HCMC Sep19 09:00 local record changes from32.0 to32.5. A replay changes neither count nor values. After Day 17, replaying the older base cannot undo this correction.

Base daily local-date means: Sep18 count 6/mean 31.333333..., Sep19 count 2/mean 31.5. City/date groups: Hanoi Sep18 count 2/31.0, Sep19 count 1/31.0; Da Nang Sep18 count 2/29.5; HCMC Sep18 count 2/33.5, Sep19 count 1/32.0.

Raw input carries a naive local current.time plus a named timezone. Clean input uses offset-aware UTC strings. CSV column types must be assigned deliberately when importing into another system.

Days06–07 used a response field in their saved envelopes. This shared fixture format deliberately names the full API body payload; follow the Days13–30 contract rather than mixing the two envelope formats.
