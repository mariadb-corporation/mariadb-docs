---
description: >-
  The mysql.table_stats table stores engine-independent statistics about tables,
  such as row counts, to assist the optimizer.
---

# mysql.table\_stats Table

The `mysql.table_stats` table is one of three tables storing data used for [Engine-independent table statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md). The others are [mysql.column\_stats](mysql-column_stats-table.md) and [mysql.index\_stats](mysql-index_stats-table.md).

It is populated when the [ANALYZE TABLE](../../sql-statements/table-statements/analyze-table.md) statement is run, although not by default. See [Collecting Statistics with the ANALYZE TABLE Statement](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md#collecting-statistics-with-the-analyze-table-statement) for details.

It is possible to manually update the table and, unlike most system tables, there are some scenarios where this could be useful. See [Manual updates to statistics tables](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md#manual-updates-to-statistics-tables) for details.

This table uses the [Aria](../../../server-usage/storage-engines/aria/) storage engine.

The `mysql.table_stats` table contains the following fields:

| Field       | Type                | Null | Key | Default | Description                     |
| ----------- | ------------------- | ---- | --- | ------- | ------------------------------- |
| db\_name    | varchar(64)         | NO   | PRI | NULL    | Database the table is in .      |
| table\_name | varchar(64)         | NO   | PRI | NULL    | Table name.                     |
| cardinality | bigint(21) unsigned | YES  |     | NULL    | Number of records in the table. |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
