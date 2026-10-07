# Help — Dictionaries, nested records, and aggregation

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>Hint 1 — syntax and reasoning after your attempt</summary>

Use three separate stages inside the loop: retrieve/normalize, reject if blank, then update the group.
~~~python
counts = {}
name = "Zone A"
counts[name] = counts.get(name, 0) + 1
~~~
On a second update, get returns the previous integer. To print sorted results, loop over sorted(city_counts), then look up each count. If every count remains 1, check whether you recreate the dictionary inside the loop.

</details>

<details>
<summary>Check your explanation</summary>

What is the difference between a missing key and a key with None? Why must the grouping dictionary be created before the loop?

Use [expected.md](expected.md) to check the result, then repeat with the additional case. Matching one output by hardcoding it does not complete the task.

</details>
