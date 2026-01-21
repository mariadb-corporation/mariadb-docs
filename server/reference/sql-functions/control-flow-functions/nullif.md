---
description: >-
  Compare two expressions and return NULL if they are equal. If the expressions
  differ, the function returns the first expression.
---

# NULLIF

## Syntax

```sql
NULLIF(expr1,expr2)
```

## Description

Returns `NULL` if expr1 = expr2 is true, otherwise returns expr1. This is the same as [CASE](case-operator.md) `WHEN` expr1 = expr2 `THEN NULL ELSE` expr1 `END`.

## Examples

```sql
SELECT NULLIF(1,1);
+-------------+
| NULLIF(1,1) |
+-------------+
|        NULL |
+-------------+

SELECT NULLIF(1,2);
+-------------+
| NULLIF(1,2) |
+-------------+
|           1 |
+-------------+
```

## See Also

* [NULL values](../../data-types/null-values.md)
* [IS NULL operator](../../sql-structure/operators/comparison-operators/is-null.md)
* [IS NOT NULL operator](../../sql-structure/operators/comparison-operators/is-not-null.md)
* [COALESCE function](../../sql-structure/operators/comparison-operators/coalesce.md)
* [IFNULL function](ifnull.md)
* [CONNECT data types](../../../server-usage/storage-engines/connect/connect-data-types.md#null-handling)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
