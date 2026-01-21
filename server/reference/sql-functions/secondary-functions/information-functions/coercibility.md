---
description: >-
  Determine collation coercibility. This function returns a numeric value
  indicating the priority of the argument's collation in comparison operations.
---

# COERCIBILITY

## Syntax

```sql
COERCIBILITY(str)
```

## Description

Returns the collation coercibility value of the string argument. Coercibility defines what will be converted to what in case of collation conflict, with an expression with higher coercibility being converted to the collation of an expression with lower coercibility.

| Coercibility | Description     | Example                                                     |
| ------------ | --------------- | ----------------------------------------------------------- |
| 0            | Explicit        | Value using a COLLATE clause                                |
| 1            | No collation    | Concatenated strings using different collations             |
| 2            | Implicit        | A string data type column value, CAST to a string data type |
| 3            | System constant | DATABASE(), USER() return value                             |
| 4            | Coercible       | Literal string                                              |
| 5            | Numeric         | Numeric and temporal values                                 |
| 6            | Ignorable       | NULL or derived from NULL                                   |

## Examples

```sql
SELECT COERCIBILITY(_latin1 'abc' COLLATE latin1_swedish_ci);
+-----------------------------------------------+
| COERCIBILITY(_latin1 'abc' COLLATE latin1_swedish_ci) |
+-----------------------------------------------+
|                                             0 |
+-----------------------------------------------+

CREATE TABLE t (a VARCHAR(30) COLLATE uca1400_swedish_ai_ci, b VARCHAR(30) COLLATE uca1400_german2_ai_ci) CHARSET utf8mb4;
INSERT INTO t VALUES ('abc', 'def'); /* a 2 coercibility */
SELECT COERCIBILITY(CONCAT(a, b)) FROM t;
+----------------------------+
| COERCIBILITY(CONCAT(a, b)) |
+----------------------------+
|                          1 |
+----------------------------+

SELECT COERCIBILITY(CAST(1 AS CHAR));
+-------------------------------+
| COERCIBILITY(CAST(1 AS CHAR)) |
+-------------------------------+
|                             2 |
+-------------------------------+

SELECT COERCIBILITY(USER());
+----------------------+
| COERCIBILITY(USER()) |
+----------------------+
|                    3 |
+----------------------+

SELECT COERCIBILITY('abc');
+---------------------+
| COERCIBILITY('abc') |
+---------------------+
|                   4 |
+---------------------+

SELECT COERCIBILITY(1);
+-----------------+
| COERCIBILITY(1) |
+-----------------+
|               5 |
+-----------------+

SELECT COERCIBILITY(NULL);
+--------------------+
| COERCIBILITY(NULL) |
+--------------------+
|                  6 |
+--------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
