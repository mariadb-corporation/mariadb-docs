---
description: >-
  Tuning GridGain 8 for throughput and latency: general practices, memory and
  JVM, persistence, SQL, memory quotas, and thread pools.
---

# Performance Tuning

Practical guidance for getting the most out of a GridGain 8 cluster. Work through the areas relevant to your workload — most deployments benefit from general and JVM tuning first, then storage and query tuning as specific bottlenecks appear.

{% columns %}
{% column %}
{% content-ref url="general-tips.md" %}
[Performance and Tuning](general-tips.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Basic and advanced performance-tuning practices for GridGain, including recommended high-performance settings, JVM options, ulimits, and OS tuning.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="memory-and-jvm-tuning.md" %}
[Memory and JVM Tuning](memory-and-jvm-tuning.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Best practices for memory, JVM, and garbage-collection tuning in GridGain deployments, with and without native persistence or external storage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="persistence-tuning.md" %}
[Persistence Tuning](persistence-tuning.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Best practices for tuning GridGain native persistence, including page size, WAL configuration, checkpointing, write throttling, and Direct I/O.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql-memory-management.md" %}
[Memory Quotas for SQL Queries](sql-memory-management.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How memory quotas prevent GridGain nodes from running out of memory when SQL queries return large result sets, including global and per-query quotas and offloading.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql-tuning.md" %}
[SQL Performance Tuning](sql-tuning.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Basic and advanced optimization techniques for GridGain SQL queries, including EXPLAIN, join order, index inline size, query parallelism, and partition pruning.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="thread-pools-tuning.md" %}
[Thread Pools Tuning](thread-pools-tuning.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of the internal thread pools GridGain maintains, how to size them, and how to create a custom thread pool for compute tasks.
{% endcolumn %}
{% endcolumns %}
