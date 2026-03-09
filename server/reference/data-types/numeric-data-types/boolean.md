---
description: >-
  Complete BOOLEAN type reference: TINYINT(1) synonym, TRUE/FALSE aliases,
  CREATE TABLE/SHOW CREATE TABLE output, and IF()/IS operator evaluation.
---

# BOOLEAN

## Syntax

```sql
BOOL, BOOLEAN
```

## Description

These types are synonyms for [TINYINT(1)](tinyint.md). A value of zero is considered false. Non-zero values are considered true.

However, the values `TRUE` and `FALSE` are merely aliases for 1 and 0. See [Boolean Literals](../../sql-structure/sql-language-structure/sql-language-structure-boolean-literals.md), as well as the [IS operator](../../sql-structure/operators/comparison-operators/is.md) for testing values against a boolean.

## Examples

```sql
CREATE TABLE boolean_example (
  example BOOLEAN
);
```

```sql
SHOW CREATE TABLE boolean_example\G
```

```
*************************** 1. row ***************************
       Table: boolean_example
Create Table: CREATE TABLE `boolean_example` (
  `example` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

```sql
CREATE TABLE boo (i BOOLEAN);

DESC boo;
+-------+------------+------+-----+---------+-------+
| Field | Type       | Null | Key | Default | Extra |
+-------+------------+------+-----+---------+-------+
| i     | tinyint(1) | YES  |     | NULL    |       |
+-------+------------+------+-----+---------+-------+
```

```sql
SELECT IF(0, 'true', 'false');
+------------------------+
| IF(0, 'true', 'false') |
+------------------------+
| false                  |
+------------------------+

SELECT IF(1, 'true', 'false');
+------------------------+
| IF(1, 'true', 'false') |
+------------------------+
| true                   |
+------------------------+

SELECT IF(2, 'true', 'false');
+------------------------+
| IF(2, 'true', 'false') |
+------------------------+
| true                   |
+------------------------+
```

`TRUE` and `FALSE` as aliases for 1 and 0:

```sql
SELECT IF(0 = FALSE, 'true', 'false');

+--------------------------------+
| IF(0 = FALSE, 'true', 'false') |
+--------------------------------+
| true                           |
+--------------------------------+

SELECT IF(1 = TRUE, 'true', 'false');
+-------------------------------+
| IF(1 = TRUE, 'true', 'false') |
+-------------------------------+
| true                          |
+-------------------------------+

SELECT IF(2 = TRUE, 'true', 'false');
+-------------------------------+
| IF(2 = TRUE, 'true', 'false') |
+-------------------------------+
| false                         |
+-------------------------------+

SELECT IF(2 = FALSE, 'true', 'false');
+--------------------------------+
| IF(2 = FALSE, 'true', 'false') |
+--------------------------------+
| false                          |
+--------------------------------+
```

The last two statements display the results shown because 2 is equal to neither 1 nor 0.

## See Also

* [Boolean Literals](../../sql-structure/sql-language-structure/sql-language-structure-boolean-literals.md)
* [IS operator](../../sql-structure/operators/comparison-operators/is.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
