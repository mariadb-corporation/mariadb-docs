---
description: >-
  Synonym for DOUBLE. This keyword declares a normal-size (8-byte)
  floating-point number with double precision.
---

# DOUBLE PRECISION

## Syntax

```sql
DOUBLE PRECISION[(M,D)] [SIGNED | UNSIGNED | ZEROFILL]
REAL[(M,D)] [SIGNED | UNSIGNED | ZEROFILL]
```

## Description

`REAL` and `DOUBLE PRECISION` are synonyms for [DOUBLE](double.md).

Exception: If the `REAL_AS_FLOAT` [SQL mode](../../../server-management/variables-and-modes/sql_mode.md) is enabled, `REAL` is a synonym for [FLOAT](float.md) rather than [DOUBLE](double.md).

## EXAMPLES

```sql
CREATE TABLE double_precision_example (
  example DOUBLE PRECISION
);
```

```sql
SHOW CREATE TABLE double_precision_example\G
<</code>>

<<sql>>

*************************** 1. row ***************************
       Table: double_precision_example
Create Table: CREATE TABLE `double_precision_example` (
  `example` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
