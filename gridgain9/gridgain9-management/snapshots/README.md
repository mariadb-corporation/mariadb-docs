---
description: >-
  Create snapshots of cluster data for backup and recovery, and restore a
  GridGain 9 cluster to a point in time.
---

# Data Snapshots and Recovery

GridGain 9 can create snapshots of the data stored across the cluster and use them later to recover the cluster to a recorded state. This section covers how to create, manage, and restore snapshots, and how to recover the cluster to a specific point in time.

{% columns %}
{% column %}
{% content-ref url="data-snapshots.md" %}
[Data Snapshots](data-snapshots.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create full and incremental data snapshots in GridGain 9, restore them, manage snapshot storage, and follow snapshot best practices.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="point-in-time-recovery.md" %}
[Point in Time Recovery](point-in-time-recovery.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Restore a GridGain 9 cluster to any point in time within the low watermark window with point-in-time recovery (PITR).
{% endcolumn %}
{% endcolumns %}
