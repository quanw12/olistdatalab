---
tags: [decourse, ai, learning]
---

# Learning with AI

## Two modes

**Learning a new skill:** try on your own for 20–30 minutes, then ask for hints and concepts, and ask the AI to explain the error. Afterwards close the chat and write the solution again yourself.

**Building a product:** you may let AI write or refactor code, but you set the requirements, verify the result and are responsible for it.

The difference matters. Research on learners picking up a new library found that people who delegated the work to AI scored lower on later understanding than people who used AI to ask conceptual questions. Use AI to think *with* you, not *instead of* you, while you are learning.

## A prompt for when you are stuck

```text
Goal: load a snapshot so that re-running it gives the same result.
Expected: input A -> B -> A should leave A as the final output.
Actual: the loader skips A on the last run.
Here is my minimal example and the query I used to check: ...
Point out which assumption is wrong and suggest one counter-example test first;
do not give me the full solution yet. Ask me to explain it back after I fix it.
```

Why this works: it states the goal, the expected and actual behaviour, and gives a minimal example. It asks for the *wrong assumption*, not a patch, and it ends with you explaining — which is the retrieval practice that builds memory.

## How to verify AI output

| AI suggests | Independent check |
|---|---|
| Revenue SQL | 3–5 expected rows computed by hand; reconcile with the source; check for fan-out |
| Retry logic | Fake timeout/429/404; count calls and sleeps; no network in unit tests |
| Incremental load | 30-day-old update, delete, moved partition, compared with a rebuild |
| New API/model | Read the official docs for the exact version; never trust invented model names |
| Optimisation | Query plan and before/after measurements on the same data |

Never paste secrets or personal data you are not allowed to share into hosted AI. Code that runs is not proof that it is correct; tests written by the AI under the same wrong assumption can be green too.

## Exercise

Pick one of your changes and ask the AI to criticise it with 3 failure modes. Reproduce at least one of them with a test. Record in your [[Study Log]]: which suggestions were right, which were wrong, and how you checked.

## Ask yourself

1. If AI were switched off for 30 minutes, could I still explain the pipeline?
2. Which test would catch a solution that looks plausible but is wrong?
3. Am I learning the cause, or just asking for the next patch?

Source: [Anthropic research on AI assistance and coding skills](https://www.anthropic.com/research/AI-assistance-coding-skills) — a narrow experiment on learners using a new library; do not generalise it to "every use of AI is harmful".
