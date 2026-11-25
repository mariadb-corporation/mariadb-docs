---
description: >-
  Discover these variants that allow partitioning based on multiple columns and
  non-integer types, offering greater flexibility than standard RANGE/LIST.
---

# RANGE COLUMNS and LIST COLUMNS Partitioning Types

`RANGE COLUMNS` and `LIST COLUMNS` are variants of, respectively, [RANGE](range-partitioning-type.md) and [LIST](list-partitioning-type.md). With these partitioning types, there is not a single partitioning expression; instead, a list of one or more columns is accepted. The following rules apply:

* The list can contain one or more columns.
* Columns can be of any [integer](../../../reference/data-types/numeric-data-types/int.md), [string](../../../reference/data-types/string-data-types/), [DATE](../../../reference/data-types/date-and-time-data-types/date.md), and [DATETIME](../../../reference/data-types/date-and-time-data-types/datetime.md) types.
* [TIMESTAMP](../../../reference/data-types/date-and-time-data-types/timestamp.md) columns are accepted only in combination with an `INTERVAL` clause. See [RANGE COLUMNS INTERVAL Partitioning Type](range-columns-interval-partitioning.md).
* Only bare columns are permitted; no expressions.

All the specified columns are compared to the specified values to determine which partition should contain a specific row. See below for details.

A `RANGE COLUMNS` table can also extend its own partitions as data is written, by adding an `INTERVAL` clause. See [RANGE COLUMNS INTERVAL Partitioning Type](range-columns-interval-partitioning.md).

## Syntax

The last part of a [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) statement can be definition of the new table's partitions. In the case of `RANGE COLUMNS` partitioning, the syntax is as follows:

```bnf
PARTITION BY RANGE COLUMNS (col1, col2, ...)
(
	PARTITION partition_name VALUES LESS THAN (value1, value2, ...),
	[ PARTITION partition_name VALUES LESS THAN (value1, value2, ...), ... ]
)
```

The syntax for `LIST COLUMNS` is as follows:

```sql
PARTITION BY LIST COLUMNS (partitioning_expression)
(
	PARTITION partition_name VALUES IN (value1, value2, ...),
	[ PARTITION partition_name VALUES IN (value1, value2, ...), ... ]
        [ PARTITION partititon_name DEFAULT ]
)
```

_`partition_name`_ is the name of a partition.

## Comparisons

To determine which partition should contain a row, all specified columns are compared to each partition definition.

With `LIST COLUMNS`, a row matches a partition if all row values are identical to the specified values. At most one partition can match the row.

With `RANGE COLUMNS`, a row matches a partition if it is less than the specified value tuple in lexicographic order. The first partition that matches the row values is used. The comparison is the same one that the [<](../../../reference/sql-structure/operators/comparison-operators/less-than.md) operator makes between two rows. To compare the row `(a, b)` with a partition's `VALUES LESS THAN (x, y)`:

1. Compare the first column. If `a` is less than `x`, the row is less than the tuple, and the partition matches. If `a` is greater than `x`, it doesn't match.
2. Only if `a` equals `x`, compare the second column the same way: the partition matches if `b` is less than `y`.
3. Continue like this for any further columns. If all the values are equal, the row is not less than the tuple, so the partition doesn't match.

Partitions are checked in the order they are defined, and the first match wins. So a later column is only compared when every earlier column is equal. A large value in the second column doesn't push a row to a later partition when its first column is already smaller.

The `DEFAULT` partition catches all records which do not fit in other partitions. Only one `DEFAULT` partition is allowed.

## Examples

`RANGE COLUMNS` partition:

```sql
CREATE OR REPLACE TABLE t1 (
  date1 DATE NOT NULL,
  date2 DATE NOT NULL
)
  ENGINE = InnoDB
  PARTITION BY RANGE COLUMNS (date1,date2) (
    PARTITION p0 VALUES LESS THAN ('2013-01-01', '1994-12-01'),
    PARTITION p1 VALUES LESS THAN ('2014-01-01', '1995-12-01'),
    PARTITION p2 VALUES LESS THAN ('2015-01-01', '1996-12-01')
);
```

Where rows land in a `RANGE COLUMNS` table with two columns:

```sql
CREATE OR REPLACE TABLE t2 (
  a INT NOT NULL,
  b DATE NOT NULL
)
  ENGINE = InnoDB
  PARTITION BY RANGE COLUMNS (a, b) (
    PARTITION p0 VALUES LESS THAN (2, '2015-01-01'),
    PARTITION p1 VALUES LESS THAN (2, '2016-01-01'),
    PARTITION p2 VALUES LESS THAN (3, '2015-01-01'),
    PARTITION p3 VALUES LESS THAN (3, '2016-01-01')
);

INSERT INTO t2 VALUES
  (1, '2015-02-01'),
  (1, '2016-06-01'),
  (2, '2014-06-01'),
  (2, '2015-06-01'),
  (2, '2016-06-01'),
  (3, '2015-06-01');
```

Each row goes to the first partition whose tuple is greater than the row:

| Row                | Why                                                                                           | Partition |
| ------------------ | --------------------------------------------------------------------------------------------- | --------- |
| `(1, '2015-02-01')` | `1 < 2`, so `b` is never compared, even though `b` is after `'2015-01-01'`.                   | p0        |
| `(1, '2016-06-01')` | `1 < 2`, so it also matches p0.                                                               | p0        |
| `(2, '2014-06-01')` | `a` equals 2, so compare `b`: `'2014-06-01'` is before `'2015-01-01'`.                        | p0        |
| `(2, '2015-06-01')` | p0: `a` equals 2, and `b` is not before `'2015-01-01'`. p1: `b` is before `'2016-01-01'`.     | p1        |
| `(2, '2016-06-01')` | p0 and p1: `a` equals 2, and `b` is not before their dates. p2: `2 < 3`.                      | p2        |
| `(3, '2015-06-01')` | p2: `a` equals 3, and `b` is not before `'2015-01-01'`. p3: `b` is before `'2016-01-01'`.     | p3        |

```sql
SELECT * FROM t2 PARTITION (p0) ORDER BY a, b;
+---+------------+
| a | b          |
+---+------------+
| 1 | 2015-02-01 |
| 1 | 2016-06-01 |
| 2 | 2014-06-01 |
+---+------------+

SELECT * FROM t2 PARTITION (p1);
+---+------------+
| a | b          |
+---+------------+
| 2 | 2015-06-01 |
+---+------------+
```

`LIST COLUMNS` partition:

```sql
CREATE OR REPLACE TABLE t1 (
  num TINYINT(1) NOT NULL
)
  ENGINE = InnoDB
  PARTITION BY LIST COLUMNS (num) (
    PARTITION p0 VALUES IN (0,1),
    PARTITION p1 VALUES IN (2,3),
    PARTITION p2 DEFAULT
  );
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
