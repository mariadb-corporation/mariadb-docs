---
description: >-
  Task-focused guides for GridGain 9: Java client logging, SQL statistics, cluster lifecycle with the REST API, and monitoring with Prometheus and Grafana.
---

# How-To Guides

Each guide solves one task from start to finish.

{% columns %}
{% column %}
{% content-ref url="configuring-java-client-logging.md" %}
[How to Configure Logging for the Java Thin Client](configuring-java-client-logging.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure logging for the GridGain 9 Java thin client using java.util.logging, Logback, or Log4j2.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="improve-query-performance-sql-statistics.md" %}
[How to Improve Query Performance With SQL Statistics](improve-query-performance-sql-statistics.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Collect SQL statistics on a TPC-H data set in GridGain 9, measure the effect on query time, and add column groups for correlated columns.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="manage-cluster-lifecycle-rest-api.md" %}
[How to Manage Cluster Lifecycle With the REST API](manage-cluster-lifecycle-rest-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Monitor node startup, initialize a cluster, and verify health using REST endpoints on GridGain 9.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="prometheus-grafana-step-by-step.md" %}
[How to Monitor GridGain 9 With Prometheus and Grafana](prometheus-grafana-step-by-step.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Export GridGain 9 metrics over OTLP to Prometheus, then connect Grafana to visualize cluster performance with a prebuilt dashboard.
{% endcolumn %}
{% endcolumns %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
