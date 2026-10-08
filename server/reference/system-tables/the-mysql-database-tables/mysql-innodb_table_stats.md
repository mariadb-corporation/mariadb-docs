---
description: >-
  The mysql.innodb_table_stats table holds persistent table-level statistics for
  InnoDB, such as row counts, used for query optimization.
---

# mysql.innodb\_table\_stats

The `mysql.innodb_table_stats` table stores data related to [InnoDB Persistent Statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md), and contains one row per table.

This table, along with the related [mysql.innodb\_index\_stats](mysql-innodb_index_stats.md) table, can be manually updated in order to force or test differing query optimization plans. After updating, [FLUSH TABLE innodb\_table\_stats](../../sql-statements/administrative-sql-statements/flush-commands/flush.md) is required to load the changes.

`mysql.innodb_table_stats` is not replicated, although any [ANALYZE TABLE](../../sql-statements/table-statements/analyze-table.md) statements on the table will be by default.

It contains the following fields:

| Field                        | Type                | Null | Key | Default              | Description                             |
| ---------------------------- | ------------------- | ---- | --- | -------------------- | --------------------------------------- |
| database\_name               | varchar(64)         | NO   | PRI | NULL                 | Database name.                          |
| table\_name                  | varchar(64)         | NO   | PRI | NULL                 | Table, partition or subpartition name.  |
| last\_update                 | timestamp           | NO   |     | current\_timestamp() | Time that this row was last updated.    |
| n\_rows                      | bigint(20) unsigned | NO   |     | NULL                 | Number of rows in the table.            |
| clustered\_index\_size       | bigint(20) unsigned | NO   |     | NULL                 | Size, in pages, of the primary index.   |
| sum\_of\_other\_index\_sizes | bigint(20) unsigned | NO   |     | NULL                 | Size, in pages, of non-primary indexes. |

## Example

```sql
SELECT * FROM mysql.innodb_table_stats\G
*************************** 1. row ***************************
           database_name: mysql
              table_name: gtid_slave_pos
             last_update: 2017-08-19 20:38:34
                  n_rows: 0
    clustered_index_size: 1
sum_of_other_index_sizes: 0
*************************** 2. row ***************************
           database_name: test
              table_name: ft
             last_update: 2017-09-15 12:58:39
                  n_rows: 0
    clustered_index_size: 1
sum_of_other_index_sizes: 2
...
```

## See Also

* [InnoDB Persistent Statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md)
* [mysql.innodb\_index\_stats](mysql-innodb_index_stats.md)
* [ANALYZE TABLE](../../sql-statements/table-statements/analyze-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
