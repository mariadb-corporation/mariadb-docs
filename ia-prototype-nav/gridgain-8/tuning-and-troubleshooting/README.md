---
description: >-
  Guidance for tuning a GridGain 8 cluster and troubleshooting it, including
  performance tuning, capacity planning, and debugging.
icon: chart-mixed
---

# Tuning and Troubleshooting

This section covers the practices that keep a GridGain cluster fast and available: performance and tuning techniques, capacity and disk-space planning, monitoring and maintenance operations, and troubleshooting common issues.

{% hint style="info" %}
GridGain also supports cross-datacenter replication for disaster recovery and geographic high availability — see [Data Center Replication](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/eT25bMH2KsyxewnTuBMM/gridgain8-management/data-center-replication).
{% endhint %}

{% columns %}
{% column %}
{% content-ref url="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/eT25bMH2KsyxewnTuBMM/tuning-and-troubleshooting/performance-tuning" %}
[Performance Tuning](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/eT25bMH2KsyxewnTuBMM/tuning-and-troubleshooting/performance-tuning)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Tuning GridGain 8 for throughput and latency: general practices, memory and JVM, persistence, SQL, memory quotas, and thread pools.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/eT25bMH2KsyxewnTuBMM/tuning-and-troubleshooting/handling-large-objects" %}
[Handling Large Objects](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/eT25bMH2KsyxewnTuBMM/tuning-and-troubleshooting/handling-large-objects)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Considerations for storing and processing large objects in GridGain, including multipage objects, concurrency, field counts, and schemas.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/eT25bMH2KsyxewnTuBMM/tuning-and-troubleshooting/troubleshooting" %}
[Troubleshooting and Debugging](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/eT25bMH2KsyxewnTuBMM/tuning-and-troubleshooting/troubleshooting)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Common tips and techniques for debugging and troubleshooting GridGain and Ignite deployments, including persistence, thin clients, GC issues, and node recovery.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/eT25bMH2KsyxewnTuBMM/tuning-and-troubleshooting/critical-failures-handling" %}
[Critical Failures Handling](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/eT25bMH2KsyxewnTuBMM/tuning-and-troubleshooting/critical-failures-handling)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain detects critical failures, configures the failure handler, and runs health checks on critical system workers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/eT25bMH2KsyxewnTuBMM/tuning-and-troubleshooting/monitoring-rebalance" %}
[Monitoring Rebalance Progress](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/eT25bMH2KsyxewnTuBMM/tuning-and-troubleshooting/monitoring-rebalance)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Methods for tracking GridGain data rebalance progress and status using the control script, cache-group metrics, cache-level metrics, and log patterns.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/eT25bMH2KsyxewnTuBMM/tuning-and-troubleshooting/capacity-planning" %}
[Capacity Planning](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/eT25bMH2KsyxewnTuBMM/tuning-and-troubleshooting/capacity-planning)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Techniques for planning and identifying the minimum hardware requirements for a GridGain deployment, covering memory, heap, compute, and disk usage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/eT25bMH2KsyxewnTuBMM/tuning-and-troubleshooting/disk-capacity-estimation" %}
[Empirical Estimation of Disk Capacity Usage](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/eT25bMH2KsyxewnTuBMM/tuning-and-troubleshooting/disk-capacity-estimation)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An empirical approach to estimating how much disk space your data will require when loaded into GridGain's internal binary format.
{% endcolumn %}
{% endcolumns %}
