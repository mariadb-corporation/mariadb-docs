---
description: >-
  How MariaDB partitioning maps onto TidesDB column families, and how partitions
  are added and dropped on a TideSQL table.
---

# TideSQL Partitioning

TidesDB tables can be partitioned with MariaDB's standard partitioning syntax. Each partition becomes a separate TidesDB table, and therefore a separate column family, so compaction and flushes happen independently per partition.

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

All of MariaDB's partitioning schemes work, `HASH`, `KEY`, `RANGE`, `LIST`, and `RANGE COLUMNS`. Secondary indexes on partitioned tables work too, with each partition holding its own index column family.

Partitions are added and dropped with `ALTER TABLE`. Dropping a partition removes all of its data:

```sql
ALTER TABLE metrics ADD PARTITION (PARTITION p_2026 VALUES LESS THAN ('2027-01-01'));
ALTER TABLE metrics DROP PARTITION p_2024;
```

{% hint style="warning" %}
A partitioned table cannot carry a vector index. See [TideSQL Vector Search](tidesql-vector-search.md).
{% endhint %}

<sub>_This page is licensed: GPLv2_</sub>
