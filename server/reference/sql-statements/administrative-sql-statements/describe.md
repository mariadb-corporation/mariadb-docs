---
description: >-
  Provides information about a table's columns. Acts as a shortcut for SHOW
  COLUMNS, displaying field names, types, and other attributes.
---

# DESCRIBE

## Syntax

```sql
{DESCRIBE | DESC} tbl_name [col_name | wild]
```

## Description

`DESCRIBE` provides information about the columns in a table.It is a shortcut for [SHOW COLUMNS FROM](show/show-columns.md).These statements also display information for [views](../../../server-usage/views/).

`col_name` can be a column name, or a string containing theSQL "`%`" and "`_`" wildcard characters toobtain output only for the columns with names matching the string. There is noneed to enclose the string within quotes unless it contains spaces or otherspecial characters.

```sql
DESCRIBE city;
+------------+----------+------+-----+---------+----------------+
| Field      | Type     | Null | Key | Default | Extra          |
+------------+----------+------+-----+---------+----------------+
| Id         | int(11)  | NO   | PRI | NULL    | auto_increment |
| Name       | char(35) | YES  |     | NULL    |                |
| Country    | char(3)  | NO   | UNI |         |                |
| District   | char(20) | YES  | MUL |         |                |
| Population | int(11)  | YES  |     | NULL    |                |
+------------+----------+------+-----+---------+----------------+
```

The description for [SHOW COLUMNS](show/show-columns.md) providesmore information about the output columns.

## See Also

* [SHOW COLUMNS](show/show-columns.md)
* [INFORMATION\_SCHEMA.COLUMNS Table](../../system-tables/information-schema/information-schema-tables/information-schema-columns-table.md)
* [mysqlshow](../../../clients-and-utilities/legacy-clients-and-utilities/mysqlshow.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
