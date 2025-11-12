# LIST Partitioning Type

`LIST` partitioning is conceptually similar to [RANGE partitioning](range-partitioning-type.md). In both cases you decide a partitioning expression (a column, or a slightly more complex calculation) and use it to determine which partitions will contain each row. However, with the `RANGE` type, partitioning is done by assigning a range of values to each partition. With the `LIST` type, we assign a set of values to each partition. This is usually preferred if the partitioning expression can return a limited set of values.

A variant of this partitioning method, [LIST COLUMNS](range-columns-and-list-columns-partitioning-types.md), allows us to use multiple columns and more datatypes.

## Syntax

The last part of a [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) statement can be the definition of the new table's partitions. In the case of `LIST` partitioning, the syntax is as follows:

```sql
PARTITION BY LIST (partitioning_expression)
(
	PARTITION partition_name VALUES IN (value_list),
	[ PARTITION partition_name VALUES IN (value_list), ... ]
        [ PARTITION partition_name DEFAULT ]
)
```

`PARTITION BY LIST` indicates that the partitioning type is `LIST`.

The _`partitioning_expression`_ is an SQL expression that returns a value from each row. In the simplest cases, it is a column name. This value is used to determine which partition should contain a row.

`partition_name` is the name of a partition.

_`value_list`_ is a list of values. If _`partitioning_expression`_ returns one of these values, the row are stored in this partition. If we try to insert something that does not belong to any of these value lists, the row are rejected with an error.

The `DEFAULT` partition catches all records which do not fit into other partitions.

## Use Cases

`LIST` partitioning can be useful when we have a column that can only contain a limited set of values. Even in that case, `RANGE` partitioning could be used instead; but `LIST` partitioning allows us to equally distribute the rows by assigning a proper set of values to each partition.

## Example

```sql
CREATE OR REPLACE TABLE t1 (
  num TINYINT(1) NOT NULL
)
  ENGINE = InnoDB
  PARTITION BY LIST (num) (
    PARTITION p0 VALUES IN (0,1),
    PARTITION p1 VALUES IN (2,3),
    PARTITION p2 DEFAULT
  );
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
