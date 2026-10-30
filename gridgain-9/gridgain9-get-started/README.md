---
description: >-
  A step-by-step introduction to GridGain 9: start a cluster, run SQL, persist
  data, use the Java API, work with secondary storage, and connect monitoring.
icon: rabbit-running
---

# Start With GridGain 9

This section walks you through the essentials of working with GridGain 9, from starting your first cluster to exploring SQL, persisting data, using the Java API, secondary storage for analytics, and connecting monitoring.

{% columns %}
{% column %}
{% content-ref url="quick-start.md" %}
[Quick Start](quick-start.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Download, install, and start GridGain 9, then run SQL queries against the cluster using the CLI tool.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="start-cluster.md" %}
[Start a GridGain 9 Cluster](start-cluster.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Set up and run a three-node GridGain 9 cluster using Docker containers, then initialize and verify it.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="explore-sql.md" %}
[Explore SQL Capabilities](explore-sql.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use the GridGain 9 SQL command-line interface to build, populate, and query the sample Chinook database on a distributed cluster.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="persist-data.md" %}
[Persist Your Data](persist-data.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Set up and use GridGain 9's RocksDB-based persistent storage with the Chinook database in a Docker environment, and verify that data survives a restart.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="java-api.md" %}
[Use the Java API](java-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Build a Java application that connects to a GridGain 9 cluster and works with data through the RecordView and KeyValueView table APIs.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="secondary-storage.md" %}
[Explore Secondary Storage for Analytics](secondary-storage.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure GridGain 9 secondary columnar storage to run analytical queries alongside transactional workloads in a hybrid HTAP setup.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="embedded-mode.md" %}
[Embedded Mode](embedded-mode.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to start and manage a GridGain 9 cluster from a Java project using embedded mode.
{% endcolumn %}
{% endcolumns %}
