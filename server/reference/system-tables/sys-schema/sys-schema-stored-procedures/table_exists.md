---
description: >-
  The table_exists procedure checks for the existence of a specific table, view,
  or temporary table within a given database.
---

# table\_exists

## Syntax

```
table_exists(in_db_name,in_table_name, out_table_type)

# in_db_name VARCHAR(64)
# in_table_name VARCHAR(64)
# out_table_type ENUM('', 'BASE TABLE', 'VIEW', 'TEMPORARY')
```

## Description

`table_exists` is a [stored procedure](../../../../server-usage/stored-routines/stored-procedures/) available with the [Sys Schema](../).

Given a database _in\_db\_name_ and table name _in\_table\_name_, returns the table type in the `OUT` parameter _out\_table\_type_. The return value is an `ENUM` field containing one of:

* '' - the table does not exist
* '`BASE TABLE`' - a regular table
* '`VIEW`' - a view
* '`TEMPORARY`' - a temporary table

## Examples

```sql
CALL sys.table_exists('mysql', 'time_zone', @table_type); SELECT @table_type;
+-------------+
| @table_type |
+-------------+
| BASE TABLE  |
+-------------+

CALL sys.table_exists('mysql', 'user', @table_type); SELECT @table_type;
+-------------+
| @table_type |
+-------------+
| VIEW        |
+-------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
