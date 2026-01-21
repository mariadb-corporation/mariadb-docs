---
description: >-
  Replace NULL values with a fallback. This function returns the first argument
  if it's not NULL; otherwise, it returns the specified replacement value.
---

# IFNULL

## Syntax

```sql
IFNULL(expr1,expr2)
NVL(expr1,expr2)
```

## Description

If _`expr1`_ is not `NULL`, `IFNULL()` returns _`expr1`_; otherwise it returns\_`expr2`\_. `IFNULL()` returns a numeric or string value, depending on the context in which it is used.

`NVL()` is an alias for `IFNULL()`.

## Examples

```sql
SELECT IFNULL(1,0); 
+-------------+
| IFNULL(1,0) |
+-------------+
|           1 |
+-------------+

SELECT IFNULL(NULL,10);
+-----------------+
| IFNULL(NULL,10) |
+-----------------+
|              10 |
+-----------------+

SELECT IFNULL(1/0,10);
+----------------+
| IFNULL(1/0,10) |
+----------------+
|        10.0000 |
+----------------+

SELECT IFNULL(1/0,'yes');
+-------------------+
| IFNULL(1/0,'yes') |
+-------------------+
| yes               |
+-------------------+
```

## See Also

* [NULL values](../../data-types/null-values.md)
* [IS NULL operator](../../sql-structure/operators/comparison-operators/is-null.md)
* [IS NOT NULL operator](../../sql-structure/operators/comparison-operators/is-not-null.md)
* [COALESCE function](../../sql-structure/operators/comparison-operators/coalesce.md)
* [NULLIF function](nullif.md)
* [CONNECT data types](../../../server-usage/storage-engines/connect/connect-data-types.md#null-handling)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
