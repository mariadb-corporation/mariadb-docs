---
description: >-
  Distributed data structures in GridGain 9, including distributed maps for
  storing key-value pairs across the cluster.
---

# Data Structures

GridGain 9 provides distributed data structures that let you store and share data across the cluster. These structures are backed by the cluster's distribution zones and storage engines, so the data is partitioned and available to every client.

- [Distributed Maps](distributed-maps.md) — store key-value pairs where each key maps to a specific value or object, using either the synchronous or asynchronous API.

{% columns %}
{% column %}
{% content-ref url="distributed-maps.md" %}
[Distributed Maps](distributed-maps.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create and use distributed maps in GridGain 9 to store key-value pairs, with synchronous and asynchronous put, get, remove, and destroy operations.
{% endcolumn %}
{% endcolumns %}
