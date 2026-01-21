---
description: >-
  Implement conditional logic in SQL queries. This operator evaluates conditions
  and returns a specific value when the first true condition is met.
---

# CASE OPERATOR

## Syntax

```sql
CASE value WHEN [compare_value] THEN result [WHEN [compare_value] THEN
result ...] [ELSE result] END

CASE WHEN [condition] THEN result [WHEN [condition] THEN result ...]
[ELSE result] END
```

## Description

The first version returns the result for the first `value=compare_value` comparison that is true. The second version returns the result for the first condition that is true. If there was no matching result value, the result after ELSE is returned, or NULL if there is no ELSE part.

There is also a [CASE statement](../../sql-statements/programmatic-compound-statements/case-statement.md), which differs from the CASE operator described here.

## Examples

```sql
SELECT CASE 1 WHEN 1 THEN 'one' WHEN 2 THEN 'two' ELSE 'more' END;
+------------------------------------------------------------+
| CASE 1 WHEN 1 THEN 'one' WHEN 2 THEN 'two' ELSE 'more' END |
+------------------------------------------------------------+
| one                                                        |
+------------------------------------------------------------+

SELECT CASE WHEN 1>0 THEN 'true' ELSE 'false' END;
+--------------------------------------------+
| CASE WHEN 1>0 THEN 'true' ELSE 'false' END |
+--------------------------------------------+
| true                                       |
+--------------------------------------------+


SELECT CASE BINARY 'B' WHEN 'a' THEN 1 WHEN 'b' THEN 2 END;
+-----------------------------------------------------+
| CASE BINARY 'B' WHEN 'a' THEN 1 WHEN 'b' THEN 2 END |
+-----------------------------------------------------+
|                                                NULL |
+-----------------------------------------------------+
```

Only the first matching condition is processed:

```sql
SELECT 
  CASE true 
     WHEN (1=1) THEN '1=1' -- result is returned 
     WHEN (1=1 OR 2=2) THEN '1=1 OR 2=2' -- condition not processed
     ELSE 'else'
  END 
;
+-------------------------------------------------------------------------------------+
| CASE true WHEN (1=1) THEN '1=1' WHEN (1=1 OR 2=2) THEN '1=1 OR 2=2' ELSE 'else' END |
+-------------------------------------------------------------------------------------+
+ 1=1                                                                                 +
+-------------------------------------------------------------------------------------+
```

## See Also

* The [CASE statement](../../sql-statements/programmatic-compound-statements/case-statement.md), which differs from the CASE operator described above.
* The [IF() function](if-function.md).
* [Operator Precedence](../../sql-structure/operators/operator-precedence.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
