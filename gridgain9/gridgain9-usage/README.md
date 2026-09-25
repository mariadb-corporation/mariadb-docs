---
description: >-
  Guides for building applications on GridGain 9 — setting up a project, working
  with tables and SQL, and using the transactional, caching, and query APIs.
icon: tv
---

# Developer's Guide

The Developer's Guide covers how to build applications on GridGain 9, from setting up a project and its dependencies to working with the Table and SQL APIs, transactions, caching, and continuous queries. Start with [Project Setup](project-setup.md) to configure your build, then explore the individual feature guides.

{% columns %}
{% column %}
{% content-ref url="project-setup.md" %}
[Project Setup](project-setup.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Set up a Java project for GridGain 9 — add the GridGain repository and the client dependency, and learn which GridGain modules to add for each feature.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="table-api.md" %}
[Table API](table-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Execute table operations in GridGain 9 with RecordView and KeyValueView, map user objects to table tuples, run criterion queries, and use the partition API.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tables-from-java-classes.md" %}
[Tables from Java Classes](tables-from-java-classes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create tables, zones, and indexes directly from Java POJOs using the GridGain 9 catalog API, with annotation-based and builder-based examples.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="caches.md" %}
[Caches](caches.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use GridGain 9 caches as temporary storage, create them from SQL, Java classes, or a builder, and connect a cache to an external JDBC database.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="near-caches.md" %}
[Near Caches](near-caches.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure a near cache in GridGain 9 to store frequently accessed data locally, eliminating network latency for a specific data subset.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="expiry-policies.md" %}
[Expiry Policies](expiry-policies.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure data expiry in GridGain 9 with a dedicated TIMESTAMP column and the EXPIRE AT keyword, and enable or disable expiration on existing tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="transactions.md" %}
[Transactions](transactions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Perform explicit and implicit transactions in GridGain 9 — lifecycle, isolation, read-only transactions, timeouts, labels, and runInTransaction.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="continuous-queries.md" %}
[Continuous Queries](continuous-queries.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Monitor data modifications in a GridGain 9 table with continuous queries — subscribers, watermarks, dedicated executors, remote filters, and event types.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-streaming.md" %}
[Data Streaming](data-streaming.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Load large volumes of data into a GridGain 9 cluster with the Data Streamer API, configure batching and flushing, use receivers, and track failed entries.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="code-deployment.md" %}
[Code Deployment](code-deployment.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deploy user code to GridGain 9 cluster nodes as immutable deployment units using the CLI, REST API, or manual placement, and manage their lifecycle.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="distributed-computing/" %}
[Distributed Computing](distributed-computing/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Run your own code across a GridGain 9 cluster as distributed, balanced, and fault-tolerant compute jobs, including colocated execution, MapReduce tasks, and WebAssembly jobs.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-structures/" %}
[Data Structures](data-structures/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Distributed data structures in GridGain 9, including distributed maps for storing key-value pairs across the cluster.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="events/" %}
[Events](events/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure event channels and sinks in GridGain 9 to track and deliver cluster events, and browse the full list of available event types.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="machine-learning/" %}
[Machine Learning](machine-learning/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Deploy machine learning models to a GridGain 9 cluster and run inference predictions using the GridGain ML engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql/" %}
[Working with SQL](sql/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Work with SQL in GridGain 9 through the Apache Calcite-based SQL engine, the Java SQL API, and the ODBC driver.
{% endcolumn %}
{% endcolumns %}
