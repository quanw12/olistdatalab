# An independent take-home and debugging rehearsal

## Understand it

Independence means decomposing a new specification, writing code, checking correctness and explaining decisions without relying on a generated solution. Documentation is allowed. Work in a bounded timebox, state trade-offs and prioritize a working tested core over extra tools.

## Syntax and trace

~~~text
Read -> clarify assumptions in notes -> tiny hand-worked example
-> implement core -> test changed inputs -> README -> explain
~~~

You can identify uncertainty without stalling: write a reasonable explicit policy and test it.

## Coding reasoning to practise

Describe work as input size grows. A nested comparison of every pair performs roughly n squared comparisons; sorting compares/reorders the whole collection; a streaming fold with a dictionary processes each input record once while storing current state for each distinct key. State both time and memory assumptions rather than calling all code fast. Do not promise worst-case constant hash lookup for every input.

For this assignment, compare a list scan for each parcel against a parcel-ID dictionary. The dictionary fold avoids repeatedly searching every existing entity, while retaining one current record per distinct ID. Separate this reasoning from measured runtime; a benchmark of six rows cannot establish production scalability. Explain when raw history or large input cannot fit in memory and what database/batching alternative you would consider.

## Engineering connection

Practise the work and communication an internship assignment can assess.

Original practice contract; review [sources.md](../../sources.md) for context.

