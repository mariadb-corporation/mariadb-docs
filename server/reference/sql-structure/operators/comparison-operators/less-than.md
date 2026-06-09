# <

## Syntax

```bnf
<
```

## Description

Less than operator. Evaluates both SQL expressions and returns `1` if the left value is less than the right value and `0` if it is not, or `NULL` if either expression is `NULL`. If the expressions return different data types, (for instance, a number and a string), performs type conversion.

When used in row comparisons, these two queries return the same results:

```sql
SELECT (t1.a, t1.b) < (t2.x, t2.y) 
FROM t1 INNER JOIN t2;

SELECT (t1.a < t2.x) OR ((t1.a = t2.x) AND (t1.b < t2.y))
FROM t1 INNER JOIN t2;
```

## Examples

```sql
SELECT 2 < 2;
+-------+
| 2 < 2 |
+-------+
|     0 |
+-------+
```

Type conversion:

```sql
SELECT 3<'4';
+-------+
| 3<'4' |
+-------+
|     1 |
+-------+
```

Case insensitivity - see [Character Sets and Collations](../../../data-types/string-data-types/character-sets/):

```sql
SELECT 'a'<'A';
+---------+
| 'a'<'A' |
+---------+
|       0 |
+---------+
```

## See Also

* [Operator Precedence](../operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
