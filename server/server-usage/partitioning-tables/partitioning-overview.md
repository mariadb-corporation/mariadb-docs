# Partitioning Overview

In MariaDB, a table can be split in smaller subsets. Both data and indexes are partitioned.

## Uses for Partitioning

There can be several reasons to use this feature:

* If you often need to delete a large set of rows, such as all rows for a given year, using partitions can help, as dropping a partition with many rows is very fast, while deleting a lot of rows can be very slow.
* Very large tables and indexes can be slow even with optimized queries. But if the target table is partitioned, queries that read a small number of partitions can be much faster. However, this means that the queries have to be written carefully in order to only access a given set of partitions.
* Partitioning allows one to distribute files over multiple storage devices. For example, we can have historical data on slower, larger disks (historical data are not supposed to be frequently read); and current data can be on faster disks, or SSD devices.
* In case we separate historical data from recent data, we will probably need to take regular backups of one partition, not the whole table.

## Partitioning Types

When partitioning a table, the use should decide:

* a partitioning type;
* a partitioning expression.

A partitioning type is the method used by MariaDB to decide how rows are distributed over existing partitions. Choosing the proper partitioning type is important to distribute rows over partitions in an efficient way.

With some partitioning types, a partitioning expression is also required. A partitioning function is an SQL expression returning an integer or temporal value, used to determine which partition will contain a given row. The partitioning expression is used for all reads and writes on involving the partitioned table, thus it should be fast.

MariaDB supports the following partitioning types:

* [RANGE](partitioning-types/range-partitioning-type.md)
* [LIST](partitioning-types/list-partitioning-type.md)
* [RANGE COLUMNS and LIST COLUMNS](partitioning-types/range-columns-and-list-columns-partitioning-types.md)
* [HASH](partitioning-types/hash-partitioning-type.md)
* [LINEAR HASH](partitioning-types/linear-hash-partitioning-type.md)
* [KEY](partitioning-types/key-partitioning-type.md)
* [LINEAR KEY](partitioning-types/linear-key-partitioning-type.md)
* [SYSTEM\_TIME](../../reference/sql-structure/temporal-tables/system-versioned-tables.md)

## Enabling Partitioning

By default, MariaDB permits partitioning. You can determine this by using the [SHOW PLUGINS](../../reference/sql-statements/administrative-sql-statements/show/show-plugins.md) statement, for example:

```sql
SHOW PLUGINS;
...
| Aria                          | ACTIVE   | STORAGE ENGINE     | NULL    | GPL     |
| FEEDBACK                      | DISABLED | INFORMATION SCHEMA | NULL    | GPL     |
| partition                     | ACTIVE   | STORAGE ENGINE     | NULL    | GPL     |
+-------------------------------+----------+--------------------+---------+---------+
```

If partition is listed as DISABLED:

```sql
| partition                     | DISABLED | STORAGE ENGINE     | NULL    | GPL     |
+-------------------------------+----------+--------------------+---------+---------+
```

MariaDB has either been built without partitioning support, or has been started with the [--skip-partition](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) option, or one of its variants:

```sql
--skip-partition
--disable-partition
--partition=OFF
```

and you will not be able to create partitions.

## Using Partitions

It is possible to create a new partitioned table using [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md).

[ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) allows one to:

* Partition an existing table;
* Remove partitions from a partitioned table (with all data in the partition);
* Add/remove partitions, or reorganize them, as long as the partitioning function allows these operations (see below);
* Exchange a partition with a table;
* Perform administrative operations on some or all partitions (analyze, optimize, check, repair).

### Adding Partitions

```
ADD PARTITION [IF NOT EXISTS] (partition_definition)
```

`[ALTER TABLE](../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md) ... ADD PARTITION` can be used to add partitions to an existing table:

```sql
CREATE OR REPLACE TABLE t1 (
  dt DATETIME NOT NULL
)
  ENGINE = InnoDB
  PARTITION BY RANGE (YEAR(dt))
  (
  PARTITION p0 VALUES LESS THAN (2013),
  PARTITION p1 VALUES LESS THAN (2014),
  PARTITION p2 VALUES LESS THAN (2015),
  PARTITION p3 VALUES LESS THAN (2016)
);

ALTER TABLE t1 ADD PARTITION (
  PARTITION p4 VALUES LESS THAN (2017), 
  PARTITION p5 VALUES LESS THAN (2018)
);
```

With [RANGE](partitioning-types/range-partitioning-type.md) partitions, it is only possible to add a partition to the high end of the range, not the low end. For example, the following results in an error:

```sql
ALTER TABLE t1 ADD PARTITION (
  PARTITION p0a VALUES LESS THAN (2012)
);
ERROR 1493 (HY000): VALUES LESS THAN value must be strictly increasing for each partition
```

You can work around this by using REORGANIZE PARTITION to split the partition instead. See [Splitting Partitions](partitioning-overview.md#splitting-partitions).

### Coalescing Partitions

```sql
COALESCE PARTITION number
```

[ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) is used to reduce the number of `HASH` or `KEY` partitions by the specified number. For example, given the following table with 5 partitions:

```sql
CREATE OR REPLACE TABLE t1 (v1 INT)
  PARTITION BY KEY (v1)
  PARTITIONS 5;
```

The following statement reduces the number of partitions by 2, leaving the table with 3 partitions:

```sql
ALTER TABLE t1 COALESCE PARTITION 2;
```

### Converting Partitions to/from Tables

{% hint style="info" %}
This feature is available from MariaDB 10.7.
{% endhint %}

```sql
CONVERT PARTITION partition_name TO TABLE tbl_name
CONVERT TABLE normal_table TO partition_definition
```

[ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) can be used to convert partitions in an existing table to a standalone table:

```sql
CREATE OR REPLACE TABLE t1 (
   dt DATETIME NOT NULL
 )
   ENGINE = InnoDB
   PARTITION BY RANGE (YEAR(dt))
   (
   PARTITION p0 VALUES LESS THAN (2013),
   PARTITION p1 VALUES LESS THAN (2014),
   PARTITION p2 VALUES LESS THAN (2015),
   PARTITION p3 VALUES LESS THAN (2016)
 );

INSERT INTO t1 VALUES ('2013-11-11'),('2014-11-11'),('2015-11-11');

SELECT * FROM t1;
+--------------+
| dt           |
+--------------+
| 2013-11-11 00:00:00 |
| 2014-11-11 00:00:00 |
| 2015-11-11 00:00:00 |
+---------------------+

ALTER TABLE t1 CONVERT PARTITION p3 TO TABLE t2;

SELECT * FROM t1;
+--------------+
| dt           |
+--------------+
| 2013-11-11 00:00:00 |
| 2014-11-11 00:00:00 |
+---------------------+

SELECT * FROM t2;
+--------------+
| dt           |
+--------------+
| 2015-11-11 00:00:00 |
+---------------------+

SHOW CREATE TABLE t1\G
*************************** 1. row ***************************
       TABLE: t1
CREATE TABLE: CREATE TABLE `t1` (
  `dt` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci
 PARTITION BY RANGE (year(`dt`))
(PARTITION `p0` VALUES LESS THAN (2013) ENGINE = InnoDB,
 PARTITION `p1` VALUES LESS THAN (2014) ENGINE = InnoDB,
 PARTITION `p2` VALUES LESS THAN (2015) ENGINE = InnoDB)

SHOW CREATE TABLE t2\G
*************************** 1. row ***************************
       TABLE: t2
CREATE TABLE: CREATE TABLE `t2` (
  `dt` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci
```

`CONVERT TABLE` does the reverse, converting a table into a partition:

```sql
ALTER TABLE t1 CONVERT TABLE t2 TO PARTITION p3 VALUES LESS THAN (2016);

SELECT * FROM t1;
+--------------+
| dt           |
+--------------+
| 2013-11-11 00:00:00 |
| 2014-11-11 00:00:00 |
| 2015-11-11 00:00:00 |
+---------------------+
3 rows in set (0.001 sec)

SELECT * FROM t2;
ERROR 1146 (42S02): Table 'test.t2' doesn't exist

SHOW CREATE TABLE t1\G
*************************** 1. row ***************************
       TABLE: t1
CREATE TABLE: CREATE TABLE `t1` (
  `dt` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci
 PARTITION BY RANGE (year(`dt`))
(PARTITION `p0` VALUES LESS THAN (2013) ENGINE = InnoDB,
 PARTITION `p1` VALUES LESS THAN (2014) ENGINE = InnoDB,
 PARTITION `p2` VALUES LESS THAN (2015) ENGINE = InnoDB,
 PARTITION `p3` VALUES LESS THAN (2016) ENGINE = InnoDB)
```

#### CONVERT TABLE ... WITH / WITHOUT VALIDATION

{% hint style="info" %}
This feature is available from MariaDB 11.4.
{% endhint %}

When converting tables to a partition, validation is performed on each row to ensure it meets the partition requirements. This can be very slow in the case of larger tables. It is possible to disable this validation by specifying the `WITHOUT VALIDATION` option.

```sql
CONVERT TABLE normal_table TO partition_definition [{WITH | WITHOUT} VALIDATION]
```

`WITH VALIDATION` will result in the validation being performed, and is the default behaviour.

An alternative to convert partitions to tables is to use [ALTER TABLE EXCHANGE PARTITION](../../reference/sql-statements/data-definition/alter/alter-table/#exchange-partition). This requires having to manually do the following steps:

1. Create an empty table with the same structure as the partition.
2. Exchange the table with the partition.
3. Drop the empty partition.

For example:

```sql
CREATE OR REPLACE TABLE t1 (
   dt DATETIME NOT NULL
 )
   ENGINE = InnoDB
   PARTITION BY RANGE (YEAR(dt))
   (
   PARTITION p0 VALUES LESS THAN (2013),
   PARTITION p1 VALUES LESS THAN (2014),
   PARTITION p2 VALUES LESS THAN (2015),
   PARTITION p3 VALUES LESS THAN (2016)
 );

INSERT INTO t1 VALUES ('2013-11-11'),('2014-11-11'),('2015-11-11');

SELECT * FROM t1;
+--------------+
| dt           |
+--------------+
| 2013-11-11 00:00:00 |
| 2014-11-11 00:00:00 |
| 2015-11-11 00:00:00 |
+---------------------+

CREATE OR REPLACE TABLE t2 LIKE t1;

ALTER TABLE t2 REMOVE PARTITIONING;

ALTER TABLE t1 EXCHANGE PARTITION p3 WITH TABLE t2;

ALTER TABLE t1 DROP PARTITION p3;

SELECT * FROM t1;
+--------------+
| dt           |
+--------------+
| 2013-11-11 00:00:00 |
| 2014-11-11 00:00:00 |
+---------------------+

SELECT * FROM t2;
+--------------+
| dt           |
+--------------+
| 2015-11-11 00:00:00 |
+---------------------+

SHOW CREATE TABLE t1\G
*************************** 1. row ***************************
       TABLE: t1
CREATE TABLE: CREATE TABLE `t1` (
  `dt` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci
 PARTITION BY RANGE (year(`dt`))
(PARTITION `p0` VALUES LESS THAN (2013) ENGINE = InnoDB,
 PARTITION `p1` VALUES LESS THAN (2014) ENGINE = InnoDB,
 PARTITION `p2` VALUES LESS THAN (2015) ENGINE = InnoDB)

SHOW CREATE TABLE t2\G
*************************** 1. row ***************************
       TABLE: t2
CREATE TABLE: CREATE TABLE `t2` (
  `dt` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci
```

Similarly, to do the reverse and convert a table into a partition `[ALTER TABLE](../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md) ... EXCHANGE PARTITION` can also be used, with the following manual steps required:

* create the partition
* exchange the partition with the table
* drop the old table:

For example:

```sql
ALTER TABLE t1 ADD PARTITION (PARTITION p3 VALUES LESS THAN (2016));

ALTER TABLE t1 EXCHANGE PARTITION p3 WITH TABLE t2;

DROP TABLE t2;

SELECT * FROM t1;
+--------------+
| dt           |
+--------------+
| 2013-11-11 00:00:00 |
| 2014-11-11 00:00:00 |
| 2015-11-11 00:00:00 |
+---------------------+

SHOW CREATE TABLE t1\G
*************************** 1. row ***************************
       TABLE: t1
CREATE TABLE: CREATE TABLE `t1` (
  `dt` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci
 PARTITION BY RANGE (year(`dt`))
(PARTITION `p0` VALUES LESS THAN (2013) ENGINE = InnoDB,
 PARTITION `p1` VALUES LESS THAN (2014) ENGINE = InnoDB,
 PARTITION `p2` VALUES LESS THAN (2015) ENGINE = InnoDB,
 PARTITION `p3` VALUES LESS THAN (2016) ENGINE = InnoDB)
```

### Dropping Partitions

```
DROP PARTITION [IF EXISTS] partition_names
```

[ALTER TABLE DROP PARTITION ](../../reference/sql-statements/data-definition/alter/alter-table/#drop-partition)can be used to drop specific partitions (and discard all data within the specified partitions) for [RANGE](partitioning-types/range-partitioning-type.md) and [LIST](partitioning-types/list-partitioning-type.md) partitions. It cannot be used on [HASH](partitioning-types/hash-partitioning-type.md) or [KEY](partitioning-types/key-partitioning-type.md) partitions. To rather remove all partitioning, while leaving the data unaffected, see [Removing Partitioning](partitioning-overview.md#removing-partitioning).

```sql
CREATE OR REPLACE TABLE t1 (
  dt DATETIME NOT NULL
)
  ENGINE = InnoDB
  PARTITION BY RANGE (YEAR(dt))
  (
  PARTITION p0 VALUES LESS THAN (2013),
  PARTITION p1 VALUES LESS THAN (2014),
  PARTITION p2 VALUES LESS THAN (2015),
  PARTITION p3 VALUES LESS THAN (2016)
);

INSERT INTO t1 VALUES ('2012-11-15');
SELECT * FROM t1;
+--------------+
| dt           |
+--------------+
| 2012-11-15 00:00:00 |
+---------------------+

ALTER TABLE t1 DROP PARTITION p0;

SELECT * FROM t1;
Empty set (0.002 sec)
```

### Exchanging Partitions

{% tabs %}
{% tab title="Current" %}
{% code overflow="wrap" %}
```sql
EXCHANGE PARTITION partition_name WITH TABLE tbl_name [{WITH | WITHOUT} VALIDATION]
```
{% endcode %}
{% endtab %}

{% tab title="< 11.4" %}
```sql
EXCHANGE PARTITION partition_name WITH TABLE tbl_name
```
{% endtab %}
{% endtabs %}

`ALTER TABLE t1 EXCHANGE PARTITION p1 WITH TABLE t2` allows to exchange a partition or subpartition with another table.

```sql
CREATE OR REPLACE TABLE t1 (
  dt DATETIME NOT NULL
)
  ENGINE = InnoDB
  PARTITION BY RANGE (YEAR(dt))
  (
  PARTITION p0 VALUES LESS THAN (2013),
  PARTITION p1 VALUES LESS THAN (2014)
);

CREATE OR REPLACE TABLE t2 (
  dt DATETIME NOT NULL
) ENGINE = InnoDB;

INSERT INTO t1 VALUES ('2012-01-01'),('2013-01-01');

INSERT INTO t2 VALUES ('2013-02-02');

SELECT * FROM t1;
+--------------+
| dt           |
+--------------+
| 2012-01-01 00:00:00 |
| 2013-01-01 00:00:00 |
+---------------------+

SELECT * FROM t2;
+--------------+
| dt           |
+--------------+
| 2013-02-02 00:00:00 |
+---------------------+

ALTER TABLE t1 EXCHANGE PARTITION p1 WITH TABLE t2;

SELECT * FROM t1;
+--------------+
| dt           |
+--------------+
| 2012-01-01 00:00:00 |
| 2013-02-02 00:00:00 |
+---------------------+

SELECT * FROM t2;
+--------------+
| dt           |
+--------------+
| 2013-01-01 00:00:00 |
+---------------------+
```

The following requirements must be met:

* Table t1 must be partitioned, and table t2 cannot be partitioned.
* Table t2 cannot be a temporary table.
* Table t1 and t2 must otherwise be identical.
* Any existing row in t2 must match the conditions for storage in the exchanged partition p1 unless, from [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/what-is-mariadb-114), the `WITHOUT VALIDATION` option is specified.

By default, MariaDB performs the validation to see that each row meets the partition requirements, and the statement fails if a row does not fit.

This attempted exchange fails, as the value is already in t2, and `2015-05-05` is outside of the partition conditions:

```sql
CREATE OR REPLACE TABLE t1 (
  dt DATETIME NOT NULL
)
  ENGINE = InnoDB
  PARTITION BY RANGE (YEAR(dt))
  (
  PARTITION p0 VALUES LESS THAN (2013),
  PARTITION p1 VALUES LESS THAN (2014)
);

CREATE OR REPLACE TABLE t2 (
  dt DATETIME NOT NULL
) ENGINE = InnoDB;

INSERT INTO t1 VALUES ('2012-02-02'),('2013-03-03');

INSERT INTO t2 VALUES ('2015-05-05');

ALTER TABLE t1 EXCHANGE PARTITION p1 WITH TABLE t2;
```

```
ERROR 1526 (HY000): Table has no partition for value 0
```

#### WITH / WITHOUT VALIDATION

{% hint style="info" %}
This feature is available from MariaDB 11.4.
{% endhint %}

This validation is performed for each row, and can be very slow in the case of larger tables. It is possible to disable this validation by specifying the `WITHOUT VALIDATION` option:

```sql
ALTER TABLE t1 EXCHANGE PARTITION p1 WITH TABLE t2 WITHOUT VALIDATION;
```

```
Query OK, 0 rows affected (0.048 sec)
```

`WITH VALIDATION` results in the validation being performed, and is the default behavior.

### Removing Partitioning

```sql
REMOVE PARTITIONING
```

[ALTER TABLE REMOVE PARTITIONING](../../reference/sql-statements/data-definition/alter/alter-table/#remove-partitioning) removes all partitioning from the table, while leaving the data unaffected. To rather drop a particular partition (and discard all of its data), see [Dropping Partitions](partitioning-overview.md#dropping-partitions).

```sql
ALTER TABLE t1 REMOVE PARTITIONING;
```

### Reorganizing Partitions

```sql
REORGANIZE PARTITION [partition_names INTO (partition_definitions)]
```

Reorganizing partitions allows one to adjust existing partitions, without losing data. Specifically, the statement can be used for:

* Splitting an existing partition into multiple partitions.
* Merging a number of existing partitions into a new, single, partition.
* Changing the ranges for a subset of existing partitions defined using `VALUES LESS THAN`.
* Changing the value lists for a subset of partitions defined using `VALUES I`.
* Renaming partitions.

### Splitting Partitions

An existing partition can be split into multiple partitions. This can also be used to add a new partition at the low end of a [RANGE](partitioning-types/range-partitioning-type.md) partition (which is not possible by [Adding Partitions](partitioning-overview.md#adding-partitions)).

```sql
CREATE OR REPLACE TABLE t1 (
  dt DATETIME NOT NULL
)
  ENGINE = InnoDB
  PARTITION BY RANGE (YEAR(dt))
  (
  PARTITION p0 VALUES LESS THAN (2013),
  PARTITION p1 VALUES LESS THAN (2014),
  PARTITION p2 VALUES LESS THAN (2015),
  PARTITION p3 VALUES LESS THAN (2016)
);

ALTER TABLE t1 REORGANIZE PARTITION p0 INTO (
    PARTITION p0a VALUES LESS THAN (2012),
    PARTITION p0b VALUES LESS THAN (2013)
);
```

Similarly, if `MAXVALUE` binds the high end:

```sql
CREATE OR REPLACE TABLE t1 (
  dt DATETIME NOT NULL
)
  ENGINE = InnoDB
  PARTITION BY RANGE (YEAR(dt))
  (
  PARTITION p0 VALUES LESS THAN (2013),
  PARTITION p1 VALUES LESS THAN (2014),
  PARTITION p2 VALUES LESS THAN (2015),
  PARTITION p3 VALUES LESS THAN (2016),
  PARTITION p4 VALUES LESS THAN MAXVALUE
);

ALTER TABLE t1 REORGANIZE PARTITION p4 INTO (
    PARTITION p4 VALUES LESS THAN (2017),
    PARTITION p5 VALUES LESS THAN MAXVALUE
);
```

### Merging Partitions

A number of existing partitions can be merged into a new partition, for example:

```sql
CREATE OR REPLACE TABLE t1 (
  dt DATETIME NOT NULL
)
  ENGINE = InnoDB
  PARTITION BY RANGE (YEAR(dt))
  (
  PARTITION p0 VALUES LESS THAN (2013),
  PARTITION p1 VALUES LESS THAN (2014),
  PARTITION p2 VALUES LESS THAN (2015),
  PARTITION p3 VALUES LESS THAN (2016)
);

ALTER TABLE t1 REORGANIZE PARTITION p2,p3 INTO (
    PARTITION p2 VALUES LESS THAN (2016)
);
```

### Changing Ranges

```sql
CREATE OR REPLACE TABLE t1 (
  dt DATETIME NOT NULL
)
  ENGINE = InnoDB
  PARTITION BY RANGE (YEAR(dt))
  (
  PARTITION p0 VALUES LESS THAN (2013),
  PARTITION p1 VALUES LESS THAN (2014),
  PARTITION p2 VALUES LESS THAN (2015),
  PARTITION p3 VALUES LESS THAN (2016)
);

ALTER TABLE t1 REORGANIZE PARTITION p3 INTO (
  PARTITION p3 VALUES LESS THAN (2017)
);
```

### Renaming Partitions

The [ALTER TABLE REORGANIZE PARTITION](../../reference/sql-statements/data-definition/alter/alter-table/#reorganize-partition) statement can also be used for renaming partitions. Note that this creates a copy of the partition:

```sql
CREATE OR REPLACE TABLE t1 (
  dt DATETIME NOT NULL
)
  ENGINE = InnoDB
  PARTITION BY RANGE (YEAR(dt))
  (
  PARTITION p0 VALUES LESS THAN (2013),
  PARTITION p1 VALUES LESS THAN (2014),
  PARTITION p2 VALUES LESS THAN (2015),
  PARTITION p3 VALUES LESS THAN (2016)
);

ALTER TABLE t1 REORGANIZE PARTITION p3 INTO (
  PARTITION p3_new VALUES LESS THAN (2016)
);
```

### Truncating Partitions

```sql
TRUNCATE PARTITION partition_names
```

`[ALTER TABLE](../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md) ... TRUNCATE PARTITION` 

[ALTER TABLE TRUNCATE PARTITION](../../reference/sql-statements/data-definition/alter/alter-table/#truncate-partition) removes all data from the specified partition/s, leaving the table and partition structure unchanged. Partitions don't need to be contiguous:

```sql
CREATE OR REPLACE TABLE t1 (
  dt DATETIME NOT NULL
)
  ENGINE = InnoDB
  PARTITION BY RANGE (YEAR(dt))
  (
  PARTITION p0 VALUES LESS THAN (2013),
  PARTITION p1 VALUES LESS THAN (2014),
  PARTITION p2 VALUES LESS THAN (2015),
  PARTITION p3 VALUES LESS THAN (2016)
);

INSERT INTO t1 VALUES ('2012-11-01'),('2013-11-02'),('2014-11-03'),('2015-11-04');

SELECT * FROM t1;
+--------------+
| dt           |
+--------------+
| 2012-11-01 00:00:00 |
| 2013-11-02 00:00:00 |
| 2014-11-03 00:00:00 |
| 2015-11-04 00:00:00 |
+---------------------+

ALTER TABLE t1 TRUNCATE PARTITION p0,p2;

SELECT * FROM t1;
+--------------+
| dt           |
+--------------+
| 2013-11-02 00:00:00 |
| 2015-11-04 00:00:00 |
+---------------------+
```

### Analyzing Partitions

Similar to [ANALYZE TABLE](../../reference/sql-statements/table-statements/analyze-table.md), key distributions for specific partitions can also be analyzed and stored, for example:

```sql
ALTER TABLE t1 ANALYZE PARTITION p0,p1,p3;
+---------+---------+----------+----------+
| Table   | Op      | Msg_type | Msg_text |
+---------+---------+----------+----------+
| test.t1 | analyze | status   | OK       |
+---------+---------+----------+----------+
```

### Checking Partitions

```sql
CHECK PARTITION {ALL | PARTITION [,partition2 ...]}
```

Similar to [CHECK TABLE](../../reference/sql-statements/table-statements/check-table.md), specific partitions can be checked for errors, for example:

```sql
ALTER TABLE t1 CHECK PARTITION p1,p3;
+---------+-------+----------+----------+
| Table   | Op    | Msg_type | Msg_text |
+---------+-------+----------+----------+
| test.t1 | check | status   | OK       |
+---------+-------+----------+----------+
```

The `ALL` keyword can be used in place of the list of partition names, and the check operation are performed on all partitions.

### Repairing Partitions

```sql
REPAIR PARTITION {ALL | partition [,partition2 ...]} [QUICK] [EXTENDED]
```

Similar to [REPAIR TABLE](../../reference/sql-statements/table-statements/repair-table.md), specific partitions can be repaired:

```sql
ALTER TABLE t1 REPAIR PARTITION p0,p3;
+---------+--------+----------+----------+
| Table   | Op     | Msg_type | Msg_text |
+---------+--------+----------+----------+
| test.t1 | repair | status   | OK       |
+---------+--------+----------+----------+
```

As with [REPAIR TABLE](../../reference/sql-statements/table-statements/repair-table.md), the `QUICK` and `EXTENDED` options are available. However, the `USE_FRM` option cannot be used with this statement on a partitioned table.

`REPAIR PARTITION` fails if there are duplicate key errors. `ALTER IGNORE TABLE ... REPAIR PARTITION` can be used in this case.

The `ALL` keyword can be used in place of the list of partition names, and the repair operation are performed on all partitions.

### Optimizing Partitions

```sql
OPTIMIZE PARTITION {ALL | PARTITION [,partition2 ...]}
```

Similar to [OPTIMIZE TABLE](../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md), specific partitions can be checked for errors:

```sql
ALTER TABLE t1 OPTIMIZE PARTITION p0,p3;
+---------+----------+----------+----------+
| Table   | Op       | Msg_type | Msg_text |
+---------+----------+----------+----------+
| test.t1 | optimize | status   | OK       |
+---------+----------+----------+----------+
```

`OPTIMIZE PARTITION` does not support per-partition optimization on InnoDB tables, and will issue a warning and cause the entire table to rebuilt and analyzed. `ALTER TABLE ... REBUILD PARTITION` and `ALTER TABLE ... ANALYZE PARTITION` can be used instead.

The `ALL` keyword can be used in place of the list of partition names, and the optimize operation are performed on all partitions.

### Partitioning for Specific Storage Engines

Some MariaDB [storage engines](../storage-engines/) allow more interesting uses for partitioning.

The [MERGE](../storage-engines/merge.md) storage engine allows one to:

* Treat a set of identical defined [MyISAM](../storage-engines/myisam-storage-engine/) tables as one.
* A MyISAM table can be in many different `MERGE` sets and also used separately.

[SPIDER](../storage-engines/spider/) allows one to:

* Move partitions of the same table on different servers. In this way, the workload can be distributed on more physical or virtual machines (data sharding).
* All partitions of a `SPIDER` table can also live on the same machine. In this case there are a small overhead (`SPIDER` uses connections to localhost), but queries that read multiple partitions will use parallel threads.

[CONNECT](../storage-engines/connect/) allows one to:

* Build a table whose partitions are tables using different storage engines (like InnoDB, MyISAM, or even engines that do not support partitioning).
* Build an indexable, writeable table on several data files. These files can be in different formats.

See also: [Using CONNECT - Partitioning and Sharding](../storage-engines/connect/using-connect/using-connect-partitioning-and-sharding.md)

## See Also

* [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/)
* [INFORMATION\_SCHEMA.PARTITIONS](../../reference/system-tables/information-schema/information-schema-tables/information-schema-partitions-table.md) contains information about existing partitions.
* [Partition Maintenance](partition-maintenance.md) for suggestions on using partitions

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
