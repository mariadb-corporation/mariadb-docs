# IS NOT

## Syntax

```bnf
IS NOT boolean_value
```

## Description

Tests a value against a boolean value, where `boolean_value` can be `TRUE`, `FALSE`, or `UNKNOWN`.

`IS NOT` always returns `1` or `0`, never `NULL`. When the value is `NULL`, `IS NOT TRUE` and `IS NOT FALSE` both return `1`. To test for a non-`NULL` value directly, use [IS NOT NULL](is-not-null.md).

## Examples

```sql
SELECT 1 IS NOT UNKNOWN, 0 IS NOT UNKNOWN, NULL IS NOT UNKNOWN;
+------------------+------------------+---------------------+
| 1 IS NOT UNKNOWN | 0 IS NOT UNKNOWN | NULL IS NOT UNKNOWN |
+------------------+------------------+---------------------+
|                1 |                1 |                   0 |
+------------------+------------------+---------------------+
```

```sql
SELECT NULL IS NOT TRUE, NULL IS NOT FALSE;
+------------------+-------------------+
| NULL IS NOT TRUE | NULL IS NOT FALSE |
+------------------+-------------------+
|                1 |                 1 |
+------------------+-------------------+
```

## See Also

* [IS](is.md)
* [IS NOT NULL](is-not-null.md)
* [Operator Precedence](../operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
