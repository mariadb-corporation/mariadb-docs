---
description: >-
  Compare two values for equality. The = operator returns 1 if they are
  equal, 0 if not, and NULL if either is NULL, converting types when they
  differ.
---

# =

## Syntax

```bnf
left_expr = right_expr
```

## Description

Equal operator. Evaluates both SQL expressions and returns `1` if they are equal, `0` if they are not equal, or [NULL](../../../data-types/null-values.md) if either expression is `NULL`. If the expressions return different data types (for example, a number and a string), a type conversion is performed.

String comparisons follow the collation. With the default collation, `=` is case- and accent-insensitive, so `'abc' = 'ABC'` returns `1`. To compare strings byte by byte, use the [BINARY](../../../sql-functions/string-functions/binary-operator.md) operator.

When a string is compared with a number, the string is converted to a number. A string that doesn't start with a number converts to `0`, and trailing non-numeric characters are dropped. Both produce warning 1292.

When used in row comparisons these two queries are synonymous and return the same results:

```sql
SELECT (t1.a, t1.b) = (t2.x, t2.y) FROM t1 INNER JOIN t2;

SELECT (t1.a = t2.x) AND (t1.b = t2.y) FROM t1 INNER JOIN t2;
```

To perform a `NULL`-safe comparison, use the [<=>](null-safe-equal.md) operator.

`=` can also be used as an [assignment operator](../assignment-operators/assignment-operators-assignment-operator.md).

## Examples

```sql
SELECT 1 = 0;
+-------+
| 1 = 0 |
+-------+
|     0 |
+-------+

SELECT '0' = 0;
+---------+
| '0' = 0 |
+---------+
|       1 |
+---------+

SELECT '0.0' = 0;
+-----------+
| '0.0' = 0 |
+-----------+
|         1 |
+-----------+

SELECT '0.01' = 0;
+------------+
| '0.01' = 0 |
+------------+
|          0 |
+------------+

SELECT '.01' = 0.01;
+--------------+
| '.01' = 0.01 |
+--------------+
|            1 |
+--------------+

SELECT (5 * 2) = CONCAT('1', '0');
+----------------------------+
| (5 * 2) = CONCAT('1', '0') |
+----------------------------+
|                          1 |
+----------------------------+

SELECT 1 = NULL;
+----------+
| 1 = NULL |
+----------+
|     NULL |
+----------+

SELECT NULL = NULL;
+-------------+
| NULL = NULL |
+-------------+
|        NULL |
+-------------+
```

Case and accents, with the default collation and with `BINARY`:

```sql
SELECT 'abc' = 'ABC', BINARY 'abc' = 'ABC', 'resume' = 'résumé';
+---------------+----------------------+-----------------------+
| 'abc' = 'ABC' | BINARY 'abc' = 'ABC' | 'resume' = 'résumé'   |
+---------------+----------------------+-----------------------+
|             1 |                    0 |                     1 |
+---------------+----------------------+-----------------------+
```

Strings that aren't fully numeric, compared with numbers:

```sql
SELECT 'abc' = 0, 99 = '99a';
+-----------+------------+
| 'abc' = 0 | 99 = '99a' |
+-----------+------------+
|         1 |          1 |
+-----------+------------+
1 row in set, 2 warnings (0.00 sec)

Warning (Code 1292): Truncated incorrect DECIMAL value: 'abc'
Warning (Code 1292): Truncated incorrect DECIMAL value: '99a'
```

## See Also

* [<=>](null-safe-equal.md)
* [Type Conversion](../../../sql-functions/string-functions/type-conversion.md)
* [Operator Precedence](../operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
