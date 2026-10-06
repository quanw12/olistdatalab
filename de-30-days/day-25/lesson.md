# Day 25 — Analytics: turn clean data into an honest report


## Start with a question and a grain

Data engineering supports consumers. Today ask: how many observations do we have per city, what are the observed daily averages, and how do recorded temperatures change over time?

Use the fixed weather_base.csv, not the live API or an incrementally updated DB. Each row is an observation. A simple mean weights observations equally; with irregular sampling it is not automatically a time-weighted daily mean or an official weather statistic.

## pandas syntax you can reuse

~~~python
import pandas as pd

example = pd.DataFrame({"group": ["A", "A", "B"], "value": [2, 4, 9]})
summary = example.groupby("group", as_index=False).agg(
    count=("value", "size"),
    mean_value=("value", "mean"),
)
print(summary)
~~~

Named aggregation explicitly names output columns. Parse observed_at with pd.to_datetime(..., utc=True), convert to the configured local zone, then derive the reporting date. Sort timestamps before plotting lines.

Left-merge a city count summary onto all configured cities to retain Hue. Filling a missing COUNT with0 is appropriate; filling a missing temperature with0 fabricates a measurement.

## Matplotlib figure syntax

~~~python
import matplotlib.pyplot as plt
from pathlib import Path

folder = Path("output")
folder.mkdir(exist_ok=True)
fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(["A", "B"], [3, 5])
ax.set(title="Example counts", xlabel="Group", ylabel="Rows")
fig.tight_layout()
fig.savefig(folder / "example.png", dpi=150)
plt.close(fig)
~~~

A Figure is the whole image; an Axes is a plotting area. Label units and timezones. Save charts as standalone files so they can appear in a README. Use bars for counts and points/lines for ordered observations. A connecting line is a visual aid, not evidence that every intermediate moment was measured.

## Write claims the data supports

A report should name the period, source, count, missingness and method. Separate 'highest recorded temperature in this fixture' from 'hottest city in general'. Eight synthetic observations cannot support climate trends or causal claims.

For a later ML track, data splits and feature timestamps matter. Predicting the future requires features available before the target time. A rolling average accidentally including future observations leaks information. This month's fixture is for pipeline mechanics, not training a useful forecast model.

Read: [pandas aggregation](https://pandas.pydata.org/docs/user_guide/groupby.html), [Matplotlib tutorial](https://matplotlib.org/stable/tutorials/pyplot.html).
