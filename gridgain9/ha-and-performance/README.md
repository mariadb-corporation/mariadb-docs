---
description: >-
  Guidance for tuning GridGain 9 performance, covering general considerations,
  JVM, operating system, persistence, SQL, and data streaming.
icon: chart-mixed
---

# Performance Tuning Guide

GridGain 9 exposes many settings that affect throughput, latency, and stability. This guide collects recommendations for tuning a GridGain cluster across several areas: general deployment practices, the JVM, the host operating system, persistence, SQL, and data streaming.

Start with [General Performance Tips](performance-tuning/general-performance-tips.md) for a baseline checklist, then explore the topic-specific pages for the areas that matter most to your workload.

{% columns %}
{% column %}
{% content-ref url="high-availability/" %}
[High Availability](high-availability/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deploying GridGain 9 for high availability — keeping the cluster and its data available through node and zone failures.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="performance-tuning/" %}
[Performance Tuning](performance-tuning/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Tuning GridGain 9 for throughput and latency: JVM, OS, persistence, data streaming, SQL, and memory.
{% endcolumn %}
{% endcolumns %}
