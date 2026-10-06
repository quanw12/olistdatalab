# Credentials, privacy and verified AI assistance

## Understand it

Treat source data and model output as untrusted inputs. Secrets belong outside tracked files, logs and prompts. An LLM can suggest explanations, tests and code; you still verify behavior. Structured output reduces parsing ambiguity but does not make content true. A bounded enrichment component needs an allowlist, validation, timeout/retry budget, evaluation fixtures and fallback.

## Syntax and trace

~~~python
import os
token = os.environ.get("EXAMPLE_API_TOKEN")
print("token configured:", bool(token))
# Do not print the actual token or paste it into a prompt.
~~~

The demo reveals presence only. A structured response still needs a contract before it can affect downstream data.

## Engineering connection

Use AI for hypotheses and reviewed proposals, never as an authority over row counts or financial totals.

Original practice contract; review [sources.md](../../sources.md) for context.

