# Day 30 — Package the portfolio and explain your decisions


1. Read the README as if you had never seen this chat. Follow the quickstart or use the Day 29 evidence to identify missing context.
2. Pick one base load, one replay, one newer correction and one controlled failure. Keep the demo commands deterministic and within five minutes.
3. Link charts, actual test counts, a CI run if available, and a short architecture diagram. Label optional cloud/live/LLM work according to what you ran.
4. Inspect git status and staged diff. Keep .env, virtual environments, generated raw dumps and server files out. Commit selected evidence explicitly.
5. Record versions from the tested environment. If pip freeze includes unrelated packages, rebuild a clean environment from the intentional requirements before claiming reproducibility.
6. Answer: why these keys, why both timestamps, why quarantine, why this transaction boundary, why finite retries, why source filtering and why Hue is NULL.
7. Use the rubric to choose specific fixes. 'Learn more Python' is vague; 'write a module and unit tests without copying a scaffold' is a useful next target.
