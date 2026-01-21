---
description: >-
  Index statistics provide crucial insights to the MariaDB query optimizer,
  guiding it in executing queries efficiently. Up-to-date index statistics
  ensure optimized query performance.
---

# Index Statistics

## How Index Statistics Help the Query Optimizer

Understanding index statistics is crucial for the MariaDB query optimizer to efficiently execute queries. Accurate and current statistics guide the optimizer in choosing the best way to access data, similar to using a personal address book for quicker searches rather than a larger phone book. Up-to-date index statistics ensure optimized query performance.

## Value Groups

The statistics primarily focus on groups of index elements with identical values. In a primary key, each index is unique, resulting in a group size of one. In a non-unique index, multiple keys may share the same value. The worst-case scenario involves large groups with identical values, such as an index on a boolean field.

MariaDB makes heavy use of the average group size statistic. For example, if there are 100 rows, and twenty groups with the same index values, the average group size would be five.

However, averages can be skewed by extremes, and the usual culprit is NULL values. The row of 100 may have 19 groups with an average size of 1, while the other 81 values are all NULL. MariaDB may think five is a good average size and choose to use that index, and then end up having to read through 81 rows with identical keys, taking longer than an alternative.

## Dealing with NULLs

There are three main approaches to the problem of NULLs. NULL index values can be treated as a single group (`nulls_equal`). This is usually fine, but if you have large numbers of NULLs the average group size is slanted higher, and the optimizer may miss using the index for ref accesses when it would be useful. This is the default used by [InnoDB](../../../server-usage/storage-engines/innodb/). The opposite approach is `nulls_unequal`, with each NULL forming its own group of one. Conversely, the average group size is slanted lower, and the optimizer may use the index for ref accesses when not suitable. This is the default used by the [Aria](../../../server-usage/storage-engines/aria/) and [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) storage engines. A third option, `nulls_ignored`, sees NULLs ignored altogether from index group calculations.

The default approaches can be changed by setting the [aria\_stats\_method](../../../server-usage/storage-engines/aria/aria-system-variables.md#aria_stats_method), [myisam\_stats\_method](../../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_stats_method) and [innodb\_stats\_method](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_stats_method) server variables.

## Null-Safe and Regular Comparisons

The comparison operator used plays an important role. If two values are compared with <=> (see the [null-safe-equal](../../../reference/sql-structure/operators/comparison-operators/null-safe-equal.md) comparison operator), and both are null, 1 is returned. If the same values are compared with = (see the [equal](../../../reference/sql-structure/operators/comparison-operators/equal.md) comparison operator) null is returned. For example:

```sql
SELECT 1 <=> 1, NULL <=> NULL, 1 <=> NULL;
+---------+---------------+------------+
| 1 <=> 1 | NULL <=> NULL | 1 <=> NULL |
+---------+---------------+------------+
|       1 |             1 |          0 |
+---------+---------------+------------+

SELECT 1 = 1, NULL = NULL, 1 = NULL;
+-------+-------------+----------+
| 1 = 1 | NULL = NULL | 1 = NULL |
+-------+-------------+----------+
|     1 |        NULL |     NULL |
+-------+-------------+----------+
```

## Engine-Independent Statistics

[MariaDB 10.0.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1001-release-notes) introduced a way to gather statistics independently of the storage engine. See [Engine-independent table statistics](../query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md).

## Histogram-Based Statistics

[Histogram-Based Statistics](../query-optimizations/statistics-for-optimizing-queries/histogram-based-statistics.md) were introduced in [MariaDB 10.0.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-1002-release-notes), and are collected by default from [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes).

## See Also

* [User Statistics](../query-optimizations/statistics-for-optimizing-queries/user-statistics.md). This plugin provides user, client, table and index usage statistics.
* [InnoDB Persistent Statistics](../query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md)
* [Engine-independent Statistics](../query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md)
* [Histogram-based Statistics](../query-optimizations/statistics-for-optimizing-queries/histogram-based-statistics.md)
* [Ignored Indexes](ignored-indexes.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
