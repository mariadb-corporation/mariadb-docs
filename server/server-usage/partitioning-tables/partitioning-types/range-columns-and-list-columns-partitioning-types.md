# RANGE COLUMNS and LIST COLUMNS Partitioning Types

`RANGE COLUMNS` and `LIST COLUMNS` are variants of, respectively, [RANGE](range-partitioning-type.md) and [LIST](list-partitioning-type.md). With these partitioning types, there is not a single partitioning expression; instead, a list of one or more columns is accepted. The following rules apply:

* The list can contain one or more columns.
* Columns can be of any [integer](../../../reference/data-types/numeric-data-types/int.md), [string](../../../reference/data-types/string-data-types/), [DATE](../../../reference/data-types/date-and-time-data-types/date.md), and [DATETIME](../../../reference/data-types/date-and-time-data-types/datetime.md) types.
* Only bare columns are permitted; no expressions.

All the specified columns are compared to the specified values to determine which partition should contain a specific row. See below for details.

## Syntax

The last part of a [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) statement can be definition of the new table's partitions. In the case of `RANGE COLUMNS` partitioning, the syntax is as follows:

```sql
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

With `RANGE COLUMNS`, a row matches a partition if all row values are less than the specified values. The first partition that matches the row values are used.

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
