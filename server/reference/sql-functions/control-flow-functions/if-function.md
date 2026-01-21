---
description: >-
  Return one of two values based on a condition. This function evaluates a
  boolean expression and returns the first value if true, or the second if
  false.
---

# IF Function

## Syntax

```sql
IF(expr1,expr2,expr3)
```

## Description

If `expr1` is `TRUE` (`expr1 <> 0` and `expr1 <> NULL`) then `IF()` returns `expr2`; otherwise it returns `expr3`. `IF()` returns a numeric or string value, depending on the context in which it is used.

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

## See Also

There is also an [IF statement](../../sql-statements/programmatic-compound-statements/if.md), which differs from the `IF()` function described above.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
