---
description: >-
  Overview of monitoring and metrics in GridGain, including the available
  monitoring methods, metric configuration, and distributed tracing.
---

# Metrics and Monitoring

This section describes how to monitor a GridGain cluster and collect metrics. It covers the available monitoring approaches, how to configure metrics, and how to enable distributed tracing.

The following topics are covered:

{% columns %}
{% column %}
{% content-ref url="intro.md" %}
[Introduction](intro.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An overview of monitoring and metrics in GridGain: the available approaches, what to monitor at each layer, and the scope of global vs. node-specific metrics.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuring-metrics.md" %}
[Configuring Metrics](configuring-metrics.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to enable or disable GridGain metrics — cache, data region, persistence, and index operation metrics — through configuration, JMX beans, or system properties.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="monitoring-memory.md" %}
[Monitoring Memory](monitoring-memory.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Read GridGain data region and data storage metrics programmatically, and calculate current node, cache, and cluster memory usage from the metric beans.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tracing.md" %}
[Tracing](tracing.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to configure OpenCensus distributed tracing in GridGain, enable trace sampling from the control script or programmatically, and analyze trace data.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="monitoring-with-grafana.md" %}
[Grafana and Prometheus](monitoring-with-grafana.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure monitoring of a GridGain 8 cluster with Grafana and Prometheus, using the JMX exporter as a Java agent to expose metrics.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="transaction-time-tracking.md" %}
[Transaction Time Tracking](transaction-time-tracking.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Track the system and user time GridGain 8 spends on transactions, and configure logging thresholds and sampling for long-running transactions.
{% endcolumn %}
{% endcolumns %}
