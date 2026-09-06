---
description: >-
  TideSQL is a transactional, log-structured merge-tree storage engine for
  MariaDB Server, built on the TidesDB library, optimized for high write
  throughput with full SQL, MVCC, encryption, and secondary, spatial,
  full-text, and vector indexes.
---

# TideSQL

{% hint style="info" %}
TideSQL is a community contribution to MariaDB Server. It is a storage engine plugin built on the TidesDB library, which is developed and maintained upstream, outside MariaDB. TideSQL 5.0.0 ships at Beta maturity.
{% endhint %}

TideSQL stores a table's data in a TidesDB log-structured merge tree instead of InnoDB, reached through ordinary SQL. Moving a table from InnoDB to TidesDB is a change to the `ENGINE` clause and nothing more. The engine favors write throughput, keeps read cost bounded through background compaction, and provides transactions through the library's optimistic multi-version concurrency control, so readers proceed without blocking writers. In `SHOW ENGINES` the engine reports its name as `TidesDB`.

{% columns %}
{% column %}
{% content-ref url="getting-started-with-tidesql.md" %}
[getting-started-with-tidesql.md](getting-started-with-tidesql.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Load the plugin, build it with the `install.sh` builder, create your first TidesDB table, and understand the one linkage detail that decides whether the plugin loads at all.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-versions-and-compatibility.md" %}
[tidesql-versions-and-compatibility.md](tidesql-versions-and-compatibility.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How TideSQL major versions map to the TidesDB library, and which MariaDB Server versions each release is tested against.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-data-model.md" %}
[tidesql-data-model.md](tidesql-data-model.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How TideSQL maps SQL rows and indexes onto TidesDB column families, key namespaces, and the on-disk row format.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-transactions-and-isolation.md" %}
[tidesql-transactions-and-isolation.md](tidesql-transactions-and-isolation.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The optimistic MVCC model, how the SQL isolation levels map onto the library, and how write contention behaves compared with InnoDB's row locks.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-durability-and-sync-modes.md" %}
[tidesql-durability-and-sync-modes.md](tidesql-durability-and-sync-modes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The sync modes that trade durability for throughput, what each one guarantees on a crash, and how they compare with InnoDB's log flushing.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-table-options.md" %}
[tidesql-table-options.md](tidesql-table-options.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The table options that control compression, encryption, TTL, bloom filters, and other per-table behavior.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-system-variables.md" %}
[tidesql-system-variables.md](tidesql-system-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A complete reference for TideSQL system variables, for tuning memory, compaction, durability, and other engine behavior.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-status-variables.md" %}
[tidesql-status-variables.md](tidesql-status-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The status variables that report cache activity, compaction, memtable and flush metrics, and other engine internals.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-encryption.md" %}
[tidesql-encryption.md](tidesql-encryption.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Per-row data-at-rest encryption through MariaDB key management, key versions and rotation, and how encryption interacts with compression and indexes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-time-to-live.md" %}
[tidesql-time-to-live.md](tidesql-time-to-live.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Row expiration through a time-to-live column, how expired rows are reclaimed during compaction, and how TTL composes with the rest of the engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-full-text-search.md" %}
[tidesql-full-text-search.md](tidesql-full-text-search.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Full-text indexes on TidesDB tables, the supported query syntax, and how the engine builds and maintains the index.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-vector-search.md" %}
[tidesql-vector-search.md](tidesql-vector-search.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Vector indexes for approximate nearest-neighbor search, the supported distance functions, and how to run a similarity query.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-spatial-indexes.md" %}
[tidesql-spatial-indexes.md](tidesql-spatial-indexes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Spatial indexes on geometry columns, the supported types, and how spatial predicates are evaluated.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-generated-columns-and-json.md" %}
[tidesql-generated-columns-and-json.md](tidesql-generated-columns-and-json.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Virtual and stored generated columns, indexing them, and working with JSON documents on TidesDB tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-foreign-keys.md" %}
[tidesql-foreign-keys.md](tidesql-foreign-keys.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Foreign-key constraints on TidesDB tables, the referential actions the engine enforces, and how they are checked.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-backup-and-checkpoint.md" %}
[tidesql-backup-and-checkpoint.md](tidesql-backup-and-checkpoint.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Taking a consistent online backup with a TidesDB checkpoint, what the checkpoint contains, and how to restore it.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-table-maintenance.md" %}
[tidesql-table-maintenance.md](tidesql-table-maintenance.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How ANALYZE, OPTIMIZE, and REPAIR behave on TidesDB tables, and when to run them.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-monitoring.md" %}
[tidesql-monitoring.md](tidesql-monitoring.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reading engine status through status variables and `SHOW ENGINE TidesDB STATUS`, and the metrics that matter for compaction and cache health.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-online-ddl.md" %}
[tidesql-online-ddl.md](tidesql-online-ddl.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Which schema changes TidesDB performs instantly or in place, which require a table copy, and how ALGORITHM and LOCK clauses apply.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-partitioning.md" %}
[tidesql-partitioning.md](tidesql-partitioning.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Partitioning TidesDB tables, the supported partition types, and how partitions map onto storage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-replication-and-ha.md" %}
[tidesql-replication-and-ha.md](tidesql-replication-and-ha.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How TideSQL participates in MariaDB replication and Galera clustering, including engine-level write-set certification and cross-node conflict resolution.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tidesql-limitations.md" %}
[tidesql-limitations.md](tidesql-limitations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The current limitations of the engine to know before putting a workload on it.
{% endcolumn %}
{% endcolumns %}

<sub>_This page is licensed: GPLv2_</sub>
