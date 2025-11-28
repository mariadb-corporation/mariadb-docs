# KEY Partitioning Type

## Syntax

```sql
PARTITION BY KEY ([column_names])
[PARTITIONS (number_of_partitions)]
```

## Description

Partitioning by key is a type of partitioning that is similar to and can be used in a similar way as [partitioning by hash](hash-partitioning-type.md).

`KEY` takes an optional list of _`column_names`_, and the hashing function is given by the server.

Just like `HASH` partitioning, in `KEY` partitioning the server takes care of the partition and ensures an even distribution among the partitions. However, the largest difference is that KEY partitioning makes use of _column\_names_, and cannot accept a _partitioning\_expression_ which is based on _column\_names_, in contrast to `HASH` partitioning, which can.

If no _`column_names`_ are specified, the table's primary key is used if present, or not null unique key if no primary key is present. If neither of these keys are present, not specifying any _column\_names_ will result in an error:

```
 ERROR 1488 (HY000): Field in list of fields for partition function not found in table
```

Unlike other partitioning types, columns used for partitioning by `KEY` are not limited to integer or `NULL` values.

`KEY` partitions do not support column index prefixes. Any columns in the partitioning key that make use of column prefixes are not used.

## Examples

```sql
CREATE OR REPLACE TABLE t1 (v1 INT)
  PARTITION BY KEY (v1)
  PARTITIONS 2;
```

```sql
CREATE OR REPLACE TABLE t1 (v1 INT, v2 INT)
  PARTITION BY KEY (v1,v2)
  PARTITIONS 2;
```

```sql
CREATE OR REPLACE TABLE t1 (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(5)
)
PARTITION BY KEY()
PARTITIONS 2;
```

```sql
CREATE OR REPLACE TABLE t1 (
    id INT NOT NULL UNIQUE KEY,
    name VARCHAR(5)
)
PARTITION BY KEY()
PARTITIONS 2;
```

The unique key must be `NOT NULL`:

```sql
CREATE OR REPLACE TABLE t1 (
    id INT NULL UNIQUE KEY,
    name VARCHAR(5)
)
PARTITION BY KEY()
PARTITIONS 2;
ERROR 1488 (HY000): Field in list of fields for partition function not found in table
```

`KEY` requires _`column_values`_ if no primary key or not null unique key is present:

```sql
CREATE OR REPLACE TABLE t1 (
    id INT NULL UNIQUE KEY,
    name VARCHAR(5)
)
PARTITION BY KEY()
PARTITIONS 2;
ERROR 1488 (HY000): Field in list of fields for partition function not found in table
```

```sql
CREATE OR REPLACE TABLE t1 (
    id INT NULL UNIQUE KEY,
    name VARCHAR(5)
)
PARTITION BY KEY(name)
PARTITIONS 2;
```

Primary key columns with index prefixes are silently ignored, so the following two queries are equivalent:

```sql
CREATE OR REPLACE TABLE t1 (
    a VARCHAR(10),
    b VARCHAR(10),
    c VARCHAR(10),
    PRIMARY KEY (a(5), b, c(5))
) PARTITION BY KEY() PARTITIONS 2;

CREATE OR REPLACE TABLE t1 (
    a VARCHAR(10),
    b VARCHAR(10),
    c VARCHAR(10),
    PRIMARY KEY (b)
) PARTITION BY KEY() PARTITIONS 2;
```

`a(5)` and `c(5)` are silently ignored in the former.

If all columns use index prefixes, the statement fails with a slightly misleading error:

```sql
CREATE OR REPLACE TABLE t1 (
    a VARCHAR(10),
    b VARCHAR(10),
    c VARCHAR(10),
    PRIMARY KEY (a(5), b(5), c(5))
) PARTITION BY KEY() PARTITIONS 2;
ERROR 1503 (HY000): A PRIMARY KEY must include all columns in the table's partitioning function
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
