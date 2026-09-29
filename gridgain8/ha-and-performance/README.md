---
description: >-
  Guidance for keeping a GridGain 8 cluster highly available and performant,
  including performance tuning, capacity planning, and troubleshooting.
icon: chart-mixed
---

# Performance and Troubleshooting Guide

This section covers the practices that keep a GridGain cluster fast and available: performance and tuning techniques, capacity and disk-space planning, monitoring and maintenance operations, and troubleshooting common issues.

{% columns %}
{% column %}
{% content-ref url="capacity-planning.md" %}
[Capacity Planning](capacity-planning.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Techniques for planning and identifying the minimum hardware requirements for a GridGain deployment, covering memory, heap, compute, and disk usage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="disk-capacity-estimation.md" %}
[Empirical Estimation of Disk Capacity Usage](disk-capacity-estimation.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An empirical approach to estimating how much disk space your data will require when loaded into GridGain's internal binary format.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="handling-large-objects.md" %}
[Handling Large Objects](handling-large-objects.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Considerations for storing and processing large objects in GridGain, including multipage objects, concurrency, field counts, and schemas.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="maintenance-mode.md" %}
[Maintenance Mode](maintenance-mode.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain nodes enter maintenance mode, the conditions that trigger it, and the operations available while a node is isolated from the cluster.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="monitoring-rebalance.md" %}
[Monitoring Rebalance Progress](monitoring-rebalance.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Methods for tracking GridGain data rebalance progress and status using the control script, cache-group metrics, cache-level metrics, and log patterns.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="troubleshooting.md" %}
[Troubleshooting and Debugging](troubleshooting.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Common tips and techniques for debugging and troubleshooting GridGain and Ignite deployments, including persistence, thin clients, GC issues, and node recovery.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="performance-tuning/" %}
[Performance Tuning](performance-tuning/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Tuning GridGain 8 for throughput and latency: general practices, memory and JVM, persistence, SQL, memory quotas, and thread pools.
{% endcolumn %}
{% endcolumns %}
