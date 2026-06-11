# ISNULL

## Syntax

```bnf
ISNULL(expr)
```

## Description

If _`expr`_ is `NULL`, `ISNULL()` returns `1`, otherwise it returns 0.

See also [NULL Values in MariaDB](../../../data-types/null-values.md).

## Examples

```sql
SELECT ISNULL(1+1);
+-------------+
| ISNULL(1+1) |
+-------------+
|           0 |
+-------------+

SELECT ISNULL(1/0);
+-------------+
| ISNULL(1/0) |
+-------------+
|           1 |
+-------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
