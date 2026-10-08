---
description: >-
  The mysql.innodb_index_stats table stores persistent index statistics for
  InnoDB, allowing optimizer plans to remain stable across restarts.
---

# mysql.innodb\_index\_stats

The `mysql.innodb_index_stats` table stores data related to particular [InnoDB Persistent Statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md), and contains multiple rows for each index.

This table, along with the related [mysql.innodb\_table\_stats](mysql-innodb_table_stats.md) table, can be manually updated in order to force or test differing query optimization plans. After updating, [FLUSH TABLE innodb\_index\_stats](../../sql-statements/administrative-sql-statements/flush-commands/flush.md) is required to load the changes.

`mysql.innodb_index_stats` is not replicated, although any [ANALYZE TABLE](../../sql-statements/table-statements/analyze-table.md) statements on the table will be by default..

It contains the following fields:

| Field             | Type                | Null | Key | Default              | Description                                                |
| ----------------- | ------------------- | ---- | --- | -------------------- | ---------------------------------------------------------- |
| database\_name    | varchar(64)         | NO   | PRI | NULL                 | Database name.                                             |
| table\_name       | varchar(64)         | NO   | PRI | NULL                 | Table, partition or subpartition name.                     |
| index\_name       | varchar(64)         | NO   | PRI | NULL                 | Index name.                                                |
| last\_update      | timestamp           | NO   |     | current\_timestamp() | Time that this row was last updated.                       |
| stat\_name        | varchar(64)         | NO   | PRI | NULL                 | Statistic name.                                            |
| stat\_value       | bigint(20) unsigned | NO   |     | NULL                 | Estimated statistic value.                                 |
| sample\_size      | bigint(20) unsigned | YES  |     | NULL                 | Number of pages sampled for the estimated statistic value. |
| stat\_description | varchar(1024)       | NO   |     | NULL                 | Statistic description.                                     |

## Example

```sql
SELECT * FROM mysql.innodb_index_stats\G
*************************** 1. row ***************************
   database_name: mysql
      table_name: gtid_slave_pos
      index_name: PRIMARY
     last_update: 2017-08-19 20:38:34
       stat_name: n_diff_pfx01
      stat_value: 0
     sample_size: 1
stat_description: domain_id
*************************** 2. row ***************************
   database_name: mysql
      table_name: gtid_slave_pos
      index_name: PRIMARY
     last_update: 2017-08-19 20:38:34
       stat_name: n_diff_pfx02
      stat_value: 0
     sample_size: 1
stat_description: domain_id,sub_id
*************************** 3. row ***************************
   database_name: mysql
      table_name: gtid_slave_pos
      index_name: PRIMARY
     last_update: 2017-08-19 20:38:34
       stat_name: n_leaf_pages
      stat_value: 1
     sample_size: NULL
stat_description: Number of leaf pages in the index
*************************** 4. row ***************************
   database_name: mysql
      table_name: gtid_slave_pos
      index_name: PRIMARY
     last_update: 2017-08-19 20:38:34
       stat_name: size
      stat_value: 1
     sample_size: NULL
stat_description: Number of pages in the index
*************************** 5. row ***************************
   database_name: test
      table_name: ft
      index_name: FTS_DOC_ID_INDEX
     last_update: 2017-09-15 12:58:39
       stat_name: n_diff_pfx01
      stat_value: 0
     sample_size: 1
stat_description: FTS_DOC_ID
*************************** 6. row ***************************
   database_name: test
      table_name: ft
      index_name: FTS_DOC_ID_INDEX
     last_update: 2017-09-15 12:58:39
       stat_name: n_leaf_pages
      stat_value: 1
     sample_size: NULL
stat_description: Number of leaf pages in the index
...
```

## See Also

* [InnoDB Persistent Statistics](../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md)
* [mysql.innodb\_table\_stats](mysql-innodb_table_stats.md)
* [ANALYZE TABLE](../../sql-statements/table-statements/analyze-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
