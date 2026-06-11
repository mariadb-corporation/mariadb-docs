# >=

## Syntax

```bnf
>=
```

## Description

Greater than or equal operator. Evaluates both SQL expressions and returns `1` if the left value is greater than or equal to the right value and `0` if it is not, or `NULL` if either expression is `NULL`. If the expressions return different data types, (for instance, a number and a string), performs type conversion.

When used in row comparisons, these two queries return the same results:

```sql
SELECT (t1.a, t1.b) >= (t2.x, t2.y) 
FROM t1 INNER JOIN t2;

SELECT (t1.a > t2.x) OR ((t1.a = t2.x) AND (t1.b >= t2.y))
FROM t1 INNER JOIN t2;
```

## Examples

```sql
SELECT 2 >= 2;
+--------+
| 2 >= 2 |
+--------+
|      1 |
+--------+

SELECT 'A' >= 'a';
+------------+
| 'A' >= 'a' |
+------------+
|          1 |
+------------+
```

## See Also

* [Operator Precedence](../operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
