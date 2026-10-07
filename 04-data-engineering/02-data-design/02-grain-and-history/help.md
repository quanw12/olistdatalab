# Help — Grain, dimensions and historical meaning

Attempt the smallest case and write its expected result first. Open one section only when you can name the obstacle; record the highest hint used in notes.md.

<details>
<summary>First hint</summary>

Separate source version history from the analytical current-state fact.

</details>

<details>
<summary>Detailed approach</summary>

Sketch the three grains on paper. Store source id/version independently of dimension surrogate keys. Use event_at >= valid_from AND (valid_to IS NULL OR event_at < valid_to). Count matches per event with a LEFT JOIN so missing dimension matches remain visible. Group and fail on counts other than one. Decide how to represent an unknown customer; do not silently drop its revenue.

</details>

<details>
<summary>Troubleshooting</summary>

A Type 2 history is not produced just by adding valid_from. A unique business key would prevent multiple historical rows. An inclusive BETWEEN can double-match a boundary.

</details>
