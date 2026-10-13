---
description: >-
  How MariaDB partitioning maps onto TidesDB column families, and how partitions
  are added and dropped on a TideSQL table.
---

# TideSQL Partitioning

TidesDB tables can be partitioned with MariaDB's standard partitioning syntax. Each partition becomes a separate TidesDB table, and therefore a separate column family with its own SSTables, so compaction runs independently per partition. The memtable and write-ahead log are database-level and shared by every column family, so a flush is not per partition.

```sql
CREATE TABLE metrics (
  id    INT NOT NULL,
  ts    DATE NOT NULL,
  value DOUBLE,
  PRIMARY KEY (id, ts)
) ENGINE=TIDESDB
PARTITION BY RANGE COLUMNS(ts) (
  PARTITION p_2024   VALUES LESS THAN ('2025-01-01'),
  PARTITION p_2025   VALUES LESS THAN ('2026-01-01'),
  PARTITION p_future VALUES LESS THAN MAXVALUE
);
```

MariaDB's partitioning schemes are handled by the server, and the engine's test suite covers `HASH`, `KEY`, `RANGE`, `LIST`, and `RANGE COLUMNS`. Secondary indexes on partitioned tables work too, with each partition holding its own index column family.

Partitions are added, split, and dropped with `ALTER TABLE`. Because `metrics` ends with a `MAXVALUE` partition, a new range is split out of `p_future` with `REORGANIZE PARTITION` rather than appended with `ADD PARTITION`, which MariaDB refuses after a `MAXVALUE` partition. Dropping a partition removes all of its data:

```sql
ALTER TABLE metrics REORGANIZE PARTITION p_future INTO (
  PARTITION p_2026   VALUES LESS THAN ('2027-01-01'),
  PARTITION p_future VALUES LESS THAN MAXVALUE
);
ALTER TABLE metrics DROP PARTITION p_2024;
```

{% hint style="warning" %}
A partitioned table cannot carry a vector index. See [TideSQL Vector Search](tidesql-vector-search.md).
{% endhint %}

<sub>_This page is licensed: GPLv2_</sub>
