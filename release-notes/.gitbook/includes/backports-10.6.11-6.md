---
title: backports-10.6.11-6
---

* The new [slave\_max\_statement\_time system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is available to set the maximum execution time for queries on replica nodes. ([MENT-1566](https://jira.mariadb.org/browse/MENT-1566), [MDEV-27161](https://jira.mariadb.org/browse/MDEV-27161))
  * When a query takes more than `slave_max_statement_time` seconds to run on the replica (slave) node, the query is aborted, and replication stops with an error.
  * The system variable can be set to a decimal value, where the decimal component has microsecond precision.
  * When set to `0`, there is no timeout.
  * The default value is `0`.
* To simplify maintenance, the [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) statement supports new clauses to convert tables to partitions and partitions to tables. ([MENT-1454](https://jira.mariadb.org/browse/MENT-1454))
  * To convert a partition to a table, use the `CONVERT PARTITION .. TO TABLE ..` clause:

```sql
ALTER TABLE partitioned_table
 CONVERT PARTITION part1
 TO TABLE normal_table;
```

* To convert a table to a partition, use the `CONVERT TABLE .. TO PARTITION ..` clause:

```sql
ALTER TABLE partitioned_table
 CONVERT TABLE normal_table
 TO PARTITION part1 VALUES LESS THAN (12345);
```

* The new `CONVERT PARTITION` and `CONVERT TABLE` clauses are crash-safe operations.
* The `EXCHANGE PARTITION` clause can still be used, but it is not a crash-safe operation.
