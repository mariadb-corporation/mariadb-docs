---
description: >-
  A RANGE COLUMNS variant that adds new partitions automatically, by a fixed
  time interval, as data is written.
---

# RANGE COLUMNS INTERVAL Partitioning Type

{% hint style="info" %}
`INTERVAL` for [RANGE COLUMNS](range-columns-and-list-columns-partitioning-types.md) partitioning was added in MariaDB 13.1.
{% endhint %}

Adding an `INTERVAL` clause to a [RANGE COLUMNS](range-columns-and-list-columns-partitioning-types.md) partitioned table makes the server extend the table's partitions automatically. You define one starting partition; whenever a write reaches the table, MariaDB adds as many partitions of the given interval as it takes for the newest partition to cover the current date and time.

This removes the routine maintenance that a time-ranged table normally needs, where a scheduled job or a person has to run [ALTER TABLE ... ADD PARTITION](../../../reference/sql-statements/data-definition/alter/alter-table/) before the data catches up with the last defined partition.

In every other respect the table behaves like an ordinary `RANGE COLUMNS` partitioned table.

## Syntax

```bnf
PARTITION BY RANGE COLUMNS (col_name)
INTERVAL interval_expression time_unit [AUTO]
(
	PARTITION partition_name VALUES LESS THAN (value)
	[, PARTITION partition_name VALUES LESS THAN (value) ... ]
)
```

Oracle's interval functions are accepted as an alternative spelling of the interval:

```bnf
PARTITION BY RANGE COLUMNS (col_name)
INTERVAL ( NUMTODSINTERVAL(number, 'DAY' | 'HOUR' | 'MINUTE' | 'SECOND') )
(
	PARTITION partition_name VALUES LESS THAN (value)
	[, PARTITION partition_name VALUES LESS THAN (value) ... ]
)

PARTITION BY RANGE COLUMNS (col_name)
INTERVAL ( NUMTOYMINTERVAL(number, 'YEAR' | 'MONTH') )
(
	PARTITION partition_name VALUES LESS THAN (value)
	[, PARTITION partition_name VALUES LESS THAN (value) ... ]
)
```

The `AUTO` keyword is optional and has no effect — automatic partition creation is always enabled when an `INTERVAL` clause is present. `SHOW CREATE TABLE` does not report it.

## Requirements and Restrictions

* Exactly one partitioning column, of type [DATE](../../../reference/data-types/date-and-time-data-types/date.md), [DATETIME](../../../reference/data-types/date-and-time-data-types/datetime.md) or [TIMESTAMP](../../../reference/data-types/date-and-time-data-types/timestamp.md). `TIMESTAMP` is permitted only in combination with `INTERVAL`; plain `RANGE COLUMNS` partitioning rejects it.
* At least one partition must be defined. `PARTITION BY RANGE COLUMNS (col) INTERVAL 1 DAY` on its own fails with `For RANGE partitions each partition must be defined`.
* No partition may use `MAXVALUE`, at table creation or later through `ALTER TABLE ... ADD PARTITION`. A `MAXVALUE` partition would swallow every future row and make automatic creation pointless.
* The interval must be positive and must not carry a sub-second component. `INTERVAL 1.1 SECOND_MICROSECOND` is rejected, as are `INTERVAL 0 DAY` and `INTERVAL -1 DAY`.
* For a `DATE` column, the interval must be at least one day.
* `NUMTODSINTERVAL()` accepts only `DAY`, `HOUR`, `MINUTE` and `SECOND`; `NUMTOYMINTERVAL()` accepts only `YEAR` and `MONTH`. In both forms the number must be greater than zero.
* The interval may be an expression, but not a subquery or a stored function call.
* `LIST COLUMNS` partitioning does not accept `INTERVAL`.
* Subpartitioning is allowed, restricted as usual to `[LINEAR] KEY` and `[LINEAR] HASH`.
* The 8192-partition limit still applies. A short interval combined with an old starting partition can reach it in a single statement, which fails with `Too many partitions (including subpartitions) were defined`.

## How Partitions Are Added

The upper bound of the highest partition is the transition point. When a write arrives, the server repeatedly adds the interval to that bound until it passes the current date and time, and creates one partition per step. New partitions are named `pN`, where `N` is chosen from the first gap in the existing `pN` names that is large enough to hold all of them.

Automatic creation happens for these statements:

* [INSERT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) and `INSERT ... SELECT`
* [REPLACE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/replace.md) and `REPLACE ... SELECT`
* [UPDATE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md), including multi-table `UPDATE`
* [LOAD DATA INFILE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md)

It also happens when one of those statements runs inside a [trigger](../../triggers-events/triggers/) body, and on a replica when it applies the corresponding row events. Read-only statements and DDL never create partitions.

{% hint style="warning" %}
Partitions are created up to the current time, not up to the value being written. A row dated further in the future than the newest partition's bound still fails with `Table has no partition for value from column_list` — and the partitions covering the present are created anyway, because the statement is rolled back but the partition changes are not.
{% endhint %}

Rows earlier than the lowest partition are not accommodated either; partitions are only ever added at the top. Automatic creation happens only in DML, so an `ALTER TABLE` that introduces an `INTERVAL` clause whose starting partition does not already cover the existing rows fails.

## Transactions and Replication

Adding partitions does not cause the implicit commit that DDL normally would, so the surrounding transaction stays open. If that transaction is rolled back, the rows are undone but the new partitions remain.

The implicit `ADD PARTITION` is not written to the binary log. A replica creates the same partitions itself while applying the row events, so primary and replica converge without a separate DDL event.

## Examples

Start from a single partition covering everything before 20 April 2026, and add a day's worth at a time:

```sql
CREATE TABLE t1 (c DATETIME)
  ENGINE = InnoDB
  PARTITION BY RANGE COLUMNS (c)
  INTERVAL 1 DAY (
    PARTITION p0 VALUES LESS THAN ('2026-04-20')
  );
```

With the server clock at 2 May 2026, a single insert fills in the missing days:

```sql
INSERT INTO t1 VALUES ('2026-05-01');

SELECT partition_name, partition_description
  FROM information_schema.partitions WHERE table_name = 't1';
+----------------+-----------------------+
| partition_name | partition_description |
+----------------+-----------------------+
| p0             | '2026-04-20'          |
| p1             | '2026-04-21 00:00:00' |
| p2             | '2026-04-22 00:00:00' |
...
| p12            | '2026-05-02 00:00:00' |
| p13            | '2026-05-03 00:00:00' |
+----------------+-----------------------+
```

The same table using Oracle's interval spelling, and a `TIMESTAMP` column:

```sql
CREATE TABLE t2 (c TIMESTAMP)
  ENGINE = InnoDB
  PARTITION BY RANGE COLUMNS (c)
  INTERVAL (NUMTOYMINTERVAL(1, 'MONTH')) (
    PARTITION p0 VALUES LESS THAN ('2026-01-01')
  );
```

Subpartitioned by `KEY`:

```sql
CREATE TABLE t3 (c DATE, d INT)
  ENGINE = InnoDB
  PARTITION BY RANGE COLUMNS (c)
  INTERVAL 3 DAY
  SUBPARTITION BY KEY (d) SUBPARTITIONS 2 (
    PARTITION p0 VALUES LESS THAN ('2026-04-25')
  );
```

`INTERVAL` can be added to or removed from an existing table by repartitioning it:

```sql
ALTER TABLE t1
  PARTITION BY RANGE COLUMNS (c)
  INTERVAL 1 WEEK (
    PARTITION p0 VALUES LESS THAN ('2026-04-20')
  );
```

## See Also

* [RANGE COLUMNS and LIST COLUMNS Partitioning Types](range-columns-and-list-columns-partitioning-types.md)
* [RANGE Partitioning Type](range-partitioning-type.md)
* [Partitioning Overview](../partitioning-overview.md)
* [Partitioning Limitations](../partitioning-limitations.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
