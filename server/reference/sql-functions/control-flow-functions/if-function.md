---
description: >-
  Complete IF() function reference: IF(expr1,expr2,expr3) conditional syntax,
  TRUE/NULL evaluation rules, return type context (numeric/string), and
  examples.
---

# IF Function

## Syntax

```bnf
IF(expr1,expr2,expr3)
```

## Description

If `expr1` is `TRUE` (`expr1 <> 0` and `expr1 <> NULL`) then `IF()` returns `expr2`; otherwise it returns `expr3`. `IF()` returns a numeric or string value, depending on the context in which it is used.

`expr1` is evaluated as a number. A string that doesn't start with a number evaluates to `0`, so it counts as false, and a string with trailing non-numeric characters is truncated to its leading number. Both produce warning 1292.

**Note:** There is also an [IF statement](../../sql-statements/programmatic-compound-statements/if.md) which differs from the`IF()` function described here.

## Examples

```sql
SELECT IF(1>2,2,3);
+-------------+
| IF(1>2,2,3) |
+-------------+
|           3 |
+-------------+
```

```sql
SELECT IF(1<2,'yes','no');
+--------------------+
| IF(1<2,'yes','no') |
+--------------------+
| yes                |
+--------------------+
```

```sql
SELECT IF(STRCMP('test','test1'),'no','yes');
+---------------------------------------+
| IF(STRCMP('test','test1'),'no','yes') |
+---------------------------------------+
| no                                    |
+---------------------------------------+
```

A string condition is converted to a number:

```sql
SELECT IF('abc',1,2), IF('1abc',1,2);
+---------------+----------------+
| IF('abc',1,2) | IF('1abc',1,2) |
+---------------+----------------+
|             2 |              1 |
+---------------+----------------+
1 row in set, 2 warnings (0.00 sec)

Warning (Code 1292): Truncated incorrect DOUBLE value: 'abc'
Warning (Code 1292): Truncated incorrect DOUBLE value: '1abc'
```

## See Also

There is also an [IF statement](../../sql-statements/programmatic-compound-statements/if.md), which differs from the `IF()` function described above.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
