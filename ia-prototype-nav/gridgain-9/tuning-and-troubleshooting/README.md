---
description: >-
  Guidance for tuning GridGain 9 performance, covering general considerations,
  JVM, operating system, persistence, SQL, and data streaming.
icon: chart-mixed
---

# Tuning and Troubleshooting

GridGain 9 exposes many settings that affect throughput, latency, and stability. This guide collects recommendations for tuning a GridGain cluster across several areas: general deployment practices, the JVM, the host operating system, persistence, SQL, and data streaming.

Start with [General Performance Tips]({gridgain9}/tuning-and-troubleshooting/performance-tuning/general-performance-tips) for a baseline checklist, then explore the topic-specific pages for the areas that matter most to your workload.

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/tuning-and-troubleshooting/high-availability" %}
[High Availability]({gridgain9}/tuning-and-troubleshooting/high-availability)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deploying GridGain 9 for high availability — keeping the cluster and its data available through node and zone failures.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/tuning-and-troubleshooting/performance-tuning" %}
[Performance Tuning]({gridgain9}/tuning-and-troubleshooting/performance-tuning)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Tuning GridGain 9 for throughput and latency: JVM, OS, persistence, data streaming, SQL, and memory.
{% endcolumn %}
{% endcolumns %}
