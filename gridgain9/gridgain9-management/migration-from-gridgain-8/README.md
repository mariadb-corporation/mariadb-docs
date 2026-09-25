---
description: >-
  Tools and workflows for migrating a cluster, its persistent data, and its
  applications from GridGain 8 to GridGain 9.
---

# Migrating to GridGain 9

This section guides you through migrating a cluster from GridGain 8 to GridGain 9, covering configuration, persistent data, codebase, and data center replication. Start with [About Migration From GridGain 8](introduction.md) for an overview of what can and cannot be migrated.

{% columns %}
{% column %}
{% content-ref url="introduction.md" %}
[About Migration](introduction.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
What can and cannot be migrated when moving a cluster from GridGain 8 to GridGain 9, and where to start.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuration-migration.md" %}
[Configuration Migration](configuration-migration.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to configure a GridGain 9 cluster to receive the components of a GridGain 8 cluster, either from the GridGain 8 configuration or from scratch.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="persistent-data-migration.md" %}
[Persistent Data Migration](persistent-data-migration.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert GridGain 8 caches to GridGain 9 tables, either by replicating caches or by migrating persistent storage files directly with the migration tool.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="codebase-migration.md" %}
[Codebase Migration](codebase-migration.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Run GridGain 8 client code against a GridGain 9 cluster with the migration adapter, configure the client connection, and rewrite collocated compute jobs.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="dcr-connector.md" %}
[DCR from GridGain 8 Tool](dcr-connector.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure, run, secure, and monitor the DR connector tool that receives data from a GridGain 8 cluster and writes it into GridGain 9 tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="dcr-from-gridgain-8.md" %}
[DCR from GridGain 8 Guide](dcr-from-gridgain-8.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Near-zero downtime migration from GridGain 8 to GridGain 9 using one-way data center replication: prepare tables, replicate, monitor, cut over, and roll back.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql-function-comparison.md" %}
[SQL Function Comparison](sql-function-comparison.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How SQL functions and data types map from GridGain 8 to the Calcite-based GridGain 9 engine: renamed, removed, and directly equivalent functions.
{% endcolumn %}
{% endcolumns %}
