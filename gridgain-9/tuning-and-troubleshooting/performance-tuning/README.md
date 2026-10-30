---
description: >-
  Tuning GridGain 9 for throughput and latency: JVM, OS, persistence, data
  streaming, SQL, and memory.
---

# Performance Tuning

Practical guidance for getting the most out of a GridGain 9 cluster. Work through the areas relevant to your workload — most deployments benefit from JVM and OS tuning first, then storage and query tuning as specific bottlenecks appear.

{% columns %}
{% column %}
{% content-ref url="general-performance-tips.md" %}
[General Performance Tips](general-performance-tips.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
General performance considerations for GridGain 9, including deployment practices, colocation, heap and metadata placement, partitioning, and efficient data access.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="jvm-tuning.md" %}
[JVM Tuning](jvm-tuning.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Recommended JVM options for GridGain 9, including heap sizing guidance, garbage collector tuning, thread pools, and NUMA-aware memory allocation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="os-tuning.md" %}
[OS Tuning](os-tuning.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Operating system tuning for GridGain 9, including CPU power management, user limits, virtual memory, swappiness, RAM sharing, and advanced memory and I/O settings.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="persistence-tuning.md" %}
[Persistence Tuning](persistence-tuning.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Persistence tuning for GridGain 9, covering log and data separation, checkpointing and write throttling, SSD selection and over-provisioning, and MVCC considerations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-streaming-tuning.md" %}
[Data Streaming Tuning](data-streaming-tuning.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Tuning the GridGain 9 Data Streamer for stability and throughput under heavy load, including batching, timeout configuration, and streamer options.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql-memory-management.md" %}
[SQL Memory Management](sql-memory-management.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to manage SQL query memory in GridGain 9 using node and query memory quotas and memory offloading to run large queries safely.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="general-configuration-tips.md" %}
[General Configuration Tips](general-configuration-tips.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Practical tips for configuring GridGain 9 cluster storage, local paths, heap usage, and server logging.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql-tuning/" %}
[SQL Tuning](sql-tuning/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Techniques for analyzing and improving GridGain 9 SQL query performance, starting with the EXPLAIN command.
{% endcolumn %}
{% endcolumns %}
