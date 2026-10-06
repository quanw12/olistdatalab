# Cloud storage, IAM and cost-aware design

## Understand it

Cloud storage holds objects; a warehouse executes analytical queries; IAM controls who can access resources. A service identity differs from a human login. Partitioning organizes data for selective reads; clustering can improve locality inside storage partitions. Both require a workload rationale. A budget alert is a notification, not a hard stop on spending.

## Syntax and trace

~~~text
source -> raw object prefix -> warehouse staging -> trusted mart
loader identity: write raw, load staging
transform identity: read staging, write mart
analyst identity: read mart only
~~~

The three roles have different needs; an analyst does not need source credentials or permission to replace raw data.

## Engineering connection

Explain one selected platform and its boundaries before adding another cloud.

[Reference](https://docs.cloud.google.com/bigquery/docs/best-practices-costs). Original explanation and exercises; source/version boundaries are in [sources.md](../../sources.md).

