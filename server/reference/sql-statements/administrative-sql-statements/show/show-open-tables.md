---
description: >-
  List currently open tables. View the database, table name, and lock status for
  tables in the table cache.
---

# SHOW OPEN TABLES

## Syntax

```bnf
SHOW OPEN TABLES [FROM db_name]
    [LIKE 'pattern' | WHERE expr]
```

## Description

`SHOW OPEN TABLES` lists the non-`TEMPORARY` tables that are currently open in the table cache. See [table-cache.html](https://dev.mysql.com/doc/refman/5.1/en/table-cache.html).

The `FROM` and `LIKE` clauses may be used.

The `FROM` clause, if present, restricts the tables shown to those present in the`db_name` database.

The `LIKE` clause, if present on its own, indicates which table names to match. The `WHERE` and `LIKE` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).

The following information is returned:

| Column       | Description                                                                         |
| ------------ | ----------------------------------------------------------------------------------- |
| Database     | Database name.                                                                      |
| Name         | Table name.                                                                         |
| In\_use      | Number of table instances being used.                                               |
| Name\_locked | 1 if the table is name-locked, e.g. if it is being dropped or renamed, otherwise 0. |

`LOCK TABLE... WRITE` acquires a strong MDL lock, and concurrent connections will wait on this MDL lock, so any subsequent `LOCK TABLE... WRITE` will not increment `In_use`.

## Example

```sql
SHOW OPEN TABLES;
+----------+---------------------------+--------+-------------+
| Database | Table                     | In_use | Name_locked |
+----------+---------------------------+--------+-------------+
...
| test     | xjson                     |      0 |           0 |
| test     | jauthor                   |      0 |           0 |
| test     | locks                     |      1 |           0 |
...
+----------+---------------------------+--------+-------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
