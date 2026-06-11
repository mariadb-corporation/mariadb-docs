# IS

## Syntax

```bnf
IS boolean_value
```

## Description

Tests a value against a boolean value, where `boolean_value` can be `TRUE`, `FALSE`, or `UNKNOWN`.

There is an important difference between using `IS TRUE` or comparing a value with `TRUE` using `=`. When using `=`, only `1` equals to `TRUE`. But when using `IS TRUE`, all values which are logically true (like a number > 1) return `TRUE`.

## Examples

```sql
SELECT 1 IS TRUE, 0 IS FALSE, NULL IS UNKNOWN;
+-----------+------------+-----------------+
| 1 IS TRUE | 0 IS FALSE | NULL IS UNKNOWN |
+-----------+------------+-----------------+
|         1 |          1 |               1 |
+-----------+------------+-----------------+
```

Difference between `=` and `IS TRUE`:

```sql
SELECT 2 = TRUE, 2 IS TRUE;
+----------+-----------+
| 2 = TRUE | 2 IS TRUE |
+----------+-----------+
|        0 |         1 |
+----------+-----------+
```

## See Also

* [Boolean Literals](../../sql-language-structure/sql-language-structure-boolean-literals.md)
* [BOOLEAN Data Type](../../../data-types/numeric-data-types/boolean.md)
* [Operator Precedence](../operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
