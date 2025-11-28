---
description: >-
  Force a column name for an expression. This function is primarily used
  internally for replication to ensure consistent column naming.
---

# NAME\_CONST

## Syntax

```sql
NAME_CONST(name,value)
```

## Description

Returns the given value. When used to produce a result set column,`NAME_CONST()` causes the column to have the given name. The arguments should be constants.

This function is used internally when replicating stored procedures. It makes little sense to use it explicitly in SQL statements, and it was not supposed to be used like that.

```sql
SELECT NAME_CONST('myname', 14);
+--------+
| myname |
+--------+
|     14 |
+--------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
