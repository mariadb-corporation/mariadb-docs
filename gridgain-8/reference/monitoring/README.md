---
description: >-
  Monitoring reference for GridGain 8 — the JMX metrics, system views, and
  generic metrics you can query to observe a running cluster.
---

# Monitoring Reference

Reference lists of everything GridGain 8 exposes for monitoring. For how to set up and configure monitoring, see [Monitoring](../../gridgain8-management/monitoring/README.md) in the Management section.

{% columns %}
{% column %}
{% content-ref url="jmx-metrics.md" %}
[JMX Metrics](jmx-metrics.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The most useful GridGain JMX metrics, grouped by monitoring task — data size, checkpointing, rebalancing, topology, caches, transactions, and more.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="system-views.md" %}
[System Views](system-views.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference of the built-in GridGain SQL system views in the SYS schema — caches, nodes, metrics, transactions, queries, statistics, and more.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="generic-metrics.md" %}
[Generic Metrics](generic-metrics.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The GridGain generic metrics system — metric registers, exporters (JMX, SQL view, log, OpenCensus, OpenTelemetry), and the full catalog of available metrics.
{% endcolumn %}
{% endcolumns %}
