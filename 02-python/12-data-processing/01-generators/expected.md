# Expected results — Generators, batching, and memory

range(5), size=2 -> [[0,1],[2,3],[4]]. Empty input -> []. Invalid size values 0, -1, True and 1.5 fail.

check.py prints PASS when all included cases succeed. Missing functions are expected until implemented.

## Reflection

Does a generator guarantee a memory-efficient pipeline?

<details>
<summary>Reveal reasoning after answering</summary>

No. Producers and consumers may still materialize all data. Bounded processing must hold across the chain.

</details>
