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
{% content-ref url="{gridgain9}/gridgain9-get-started/quick-start" %}
[Quick Start]({gridgain9}/gridgain9-get-started/quick-start)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Download, install, and start GridGain 9, then run SQL queries against the cluster using the CLI tool.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/gridgain9-get-started/start-cluster" %}
[Start a GridGain 9 Cluster]({gridgain9}/gridgain9-get-started/start-cluster)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Set up and run a three-node GridGain 9 cluster using Docker containers, then initialize and verify it.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/gridgain9-get-started/explore-sql" %}
[Explore SQL Capabilities]({gridgain9}/gridgain9-get-started/explore-sql)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use the GridGain 9 SQL command-line interface to build, populate, and query the sample Chinook database on a distributed cluster.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/gridgain9-get-started/persist-data" %}
[Persist Your Data]({gridgain9}/gridgain9-get-started/persist-data)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Set up and use GridGain 9's RocksDB-based persistent storage with the Chinook database in a Docker environment, and verify that data survives a restart.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/gridgain9-get-started/java-api" %}
[Use the Java API]({gridgain9}/gridgain9-get-started/java-api)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Build a Java application that connects to a GridGain 9 cluster and works with data through the RecordView and KeyValueView table APIs.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/gridgain9-get-started/secondary-storage" %}
[Explore Secondary Storage for Analytics]({gridgain9}/gridgain9-get-started/secondary-storage)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure GridGain 9 secondary columnar storage to run analytical queries alongside transactional workloads in a hybrid HTAP setup.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/gridgain9-get-started/embedded-mode" %}
[Embedded Mode]({gridgain9}/gridgain9-get-started/embedded-mode)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to start and manage a GridGain 9 cluster from a Java project using embedded mode.
{% endcolumn %}
{% endcolumns %}
