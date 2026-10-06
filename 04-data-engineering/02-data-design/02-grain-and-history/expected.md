# Expected — DE05

Two boundary events produce two fact rows and exactly one match each. An intentionally overlapping interval makes the match-count test fail. The schema explicitly distinguishes current-state revenue from historical revenue.

## Reflection answer

<details>
<summary>Open after answering</summary>

No. A current attribute describes now; historical revenue needs a valid event-time dimension mapping and preserved history.

</details>

Passing a supplied fixture is one piece of evidence. Explain the result and show one changed-input or failure example before marking the lesson complete.

