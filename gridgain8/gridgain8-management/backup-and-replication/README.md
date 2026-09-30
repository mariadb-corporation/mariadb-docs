---
description: >-
  Protect and replicate cluster data — snapshots and point-in-time recovery, cross-datacenter replication, and cache update conflict resolution.
---

# Backup, Recovery, and Replication

This section groups the following topics:

{% columns %}
{% column %}
{% content-ref url="../snapshots/" %}
[Snapshots and Recovery](../snapshots/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of GridGain snapshots and recovery: full and incremental snapshots, point-in-time recovery, network backups, heterogeneous recovery, and tooling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../data-center-replication/" %}
[Data Center Replication](../data-center-replication/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain data center replication lets you replicate data caches between multiple data centers and recover quickly when a data center goes offline.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../conflict-resolution.md" %}
[Conflict Resolution](../conflict-resolution.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain resolves cache update conflicts, including automatic resolution and the CacheConflictResolver interface for custom conflict handling.
{% endcolumn %}
{% endcolumns %}
