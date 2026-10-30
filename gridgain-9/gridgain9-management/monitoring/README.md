---
description: >-
  Monitor a GridGain 9 cluster with metrics, system views, and exporters, and
  learn the best practices for keeping a production cluster healthy.
---

# Metrics and Monitoring

GridGain 9 exposes the state of a running cluster through metrics, SQL system views, and events. This section explains how to enable metric sources, configure exporters for external monitoring tools, and apply monitoring best practices in production.

To get started, see [Configuring Metrics](configuring-metrics.md).

{% columns %}
{% column %}
{% content-ref url="configuring-metrics.md" %}
[Configuring Metrics](configuring-metrics.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Enable metric sources on a node or across the cluster, and configure JMX, LogPush, and OpenTelemetry exporters to collect GridGain 9 metrics.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="monitoring-best-practices.md" %}
[Monitoring Best Practices](monitoring-best-practices.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Best practices for monitoring a production GridGain 9 cluster: which metrics to watch, the alerts to configure, and how to diagnose problems.
{% endcolumn %}
{% endcolumns %}
