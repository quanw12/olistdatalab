# Dependency graphs, parameters and run boundaries

## Understand it

An orchestrator manages dependencies, execution state and retries; it cannot fix incorrect transformation logic. Define extract -> validate -> load -> transform -> check -> publish. Distinguish the business interval from when a worker starts, and define retry-safe durable stage boundaries.

## Syntax and trace

~~~python
dependencies = {"extract": [], "load": ["extract"], "report": ["load"]}
print(dependencies["report"])
~~~

report requires successful load. Concurrent branches must respect single-writer state assumptions.

## Engineering connection

Never publish after a failed load or failed quality gate.

Original practice contract; review [sources.md](../../sources.md) for context.

