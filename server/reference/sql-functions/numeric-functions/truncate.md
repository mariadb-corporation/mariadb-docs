---
description: >-
  Truncate a number. This function truncates a number to a specified number of
  decimal places.
---

# TRUNCATE

This page documents the `TRUNCATE` function. See [TRUNCATE TABLE](../../sql-statements/table-statements/truncate-table.md) for the DDL statement.

## Syntax

```sql
TRUNCATE(X,D)
```

## Description

Returns the number X, truncated to D decimal places. If D is 0, the result has no decimal point or fractional part. D can be negative to cause D digits left of the decimal point of the value X to become\
zero.

## Examples

```sql
SELECT TRUNCATE(1.223,1);
+-------------------+
| TRUNCATE(1.223,1) |
+-------------------+
|               1.2 |
+-------------------+

SELECT TRUNCATE(1.999,1);
+-------------------+
| TRUNCATE(1.999,1) |
+-------------------+
|               1.9 |
+-------------------+

SELECT TRUNCATE(1.999,0); 
+-------------------+
| TRUNCATE(1.999,0) |
+-------------------+
|                 1 |
+-------------------+

SELECT TRUNCATE(-1.999,1);
+--------------------+
| TRUNCATE(-1.999,1) |
+--------------------+
|               -1.9 |
+--------------------+

SELECT TRUNCATE(122,-2);
+------------------+
| TRUNCATE(122,-2) |
+------------------+
|              100 |
+------------------+

SELECT TRUNCATE(10.28*100,0);
+-----------------------+
| TRUNCATE(10.28*100,0) |
+-----------------------+
|                  1028 |
+-----------------------+
```

## See Also

* [TRUNCATE TABLE](../../sql-statements/table-statements/truncate-table.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
