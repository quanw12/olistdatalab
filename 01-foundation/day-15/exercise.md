# Day 15 — Reliable HTTP extraction and bounded retries


Implement capstone/weather_pipeline/extract.py with fetch_envelope and the lesson's retry policy. Accept city/configuration plus an injectable client, sleeper and clock. Return the contract's raw envelope.

Build capstone/retry_demo.py using ../data/api_response.json. Show immediate200, 503 then200, three503 failures, permanent400 and malformed200 JSON. Print attempts/delays/outcome. Save successful envelopes as a JSON list under a unique run name. One optional live GET is enough; fixture values are not a live forecast.
