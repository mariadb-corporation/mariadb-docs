---
description: >-
  The mysql.column_stats table stores engine-independent column statistics, such
  as histograms, used by the optimizer to improve query execution plans.
---

# mysql.column\_stats Table

The `mysql.column_stats` table is one of three tables storing data used for [Engine-independent table statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md). The others are [mysql.table\_stats](mysql-table_stats-table.md) and [mysql.index\_stats](mysql-index_stats-table.md).

It is populated when the [ANALYZE TABLE](../../sql-statements/table-statements/analyze-table.md) statement is run, although not by default. See [Collecting Statistics with the ANALYZE TABLE Statement](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md#collecting-statistics-with-the-analyze-table-statement) for details.

Note that statistics for blob and text columns are not collected. If explicitly specified, a warning is returned.

It is possible to manually update the table and, unlike most system tables, there are some scenarios where this could be useful. See [Manual updates to statistics tables](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md#manual-updates-to-statistics-tables) for details.

This table uses the [Aria](../../../server-usage/storage-engines/aria/) storage engine.

The `mysql.column_stats` table contains the following fields:

<table><thead><tr><th width="145">Field</th><th width="170">Type</th><th width="115">Null</th><th>Key</th><th>Default</th><th>Description</th></tr></thead><tbody><tr><td>db_name</td><td>varchar(64)</td><td>NO</td><td>PRI</td><td>NULL</td><td>Database the table is in.</td></tr><tr><td>table_name</td><td>varchar(64)</td><td>NO</td><td>PRI</td><td>NULL</td><td>Table name.</td></tr><tr><td>column_name</td><td>varchar(64)</td><td>NO</td><td>PRI</td><td>NULL</td><td>Name of the column.</td></tr><tr><td>min_value</td><td>varbinary(255)</td><td>YES</td><td></td><td>NULL</td><td></td></tr><tr><td>max_value</td><td>varbinary(255)</td><td>YES</td><td></td><td>NULL</td><td></td></tr><tr><td>nulls_ratio</td><td>decimal(12,4)</td><td>YES</td><td></td><td>NULL</td><td>Fraction of NULL values (0- no NULLs, 0.5 - half values are NULLs, 1 - all values are NULLs).</td></tr><tr><td>avg_length</td><td>decimal(12,4)</td><td>YES</td><td></td><td>NULL</td><td>Average length of column value, in bytes. Counted as if one ran SELECT AVG(LENGTH(col)). This doesn't count NULL bytes, assumes endspace removal for CHAR(n), etc.</td></tr><tr><td>avg_frequency</td><td>decimal(12,4)</td><td>YES</td><td></td><td>NULL</td><td>Average number of records with the same value</td></tr><tr><td>hist_size</td><td>tinyint(3) unsigned</td><td>YES</td><td></td><td>NULL</td><td>Histogram size in bytes, from 0-255, or, from <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108">MariaDB 10.8</a>, number of buckets if the histogram type is JSON_HB.</td></tr><tr><td>hist_type</td><td>enum('SINGLE_PREC_HB', 'DOUBLE_PREC_HB') (from MariaDB 10.8)<br>enum('SINGLE_PREC_HB', 'DOUBLE_PREC_HB','JSON_HB') (until MariaDB 10.7)</td><td>YES</td><td></td><td>NULL</td><td>Histogram type. See the <a href="../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#histogram_type">histogram_type</a> system variable.</td></tr><tr><td>histogram</td><td><p>blob (from MariaDB 10.7)</p><p>varbinary(255) (until MariaDB 10.7)</p></td><td>YES</td><td></td><td>NULL</td><td></td></tr></tbody></table>

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
