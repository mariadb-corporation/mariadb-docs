---
description: >-
  The create_synonym_db stored procedure creates a new database that contains
  views mirroring all tables from a source database, useful for creating
  aliases.
---

# create\_synonym\_db

## Syntax

```
create_synonym_db(db_name,synonym)

# db_name (VARCHAR(64))
# synonym (VARCHAR(64))
```

## Description

`create_synonym_db` is a [stored procedure](../../../../server-usage/stored-routines/stored-procedures/) available with the [Sys Schema](../).

Takes a source database name _db\_name_ and _synonym_ name and creates a synonym database with views that point to all of the tables within the source database. Useful for example for creating a synonym for the [performance\_schema](../../performance-schema/) or [information\_schema](../../information-schema/) databases.

Returns an error if the source database doesn't exist, or the synonym already exists.

## Example

```sql
SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test               |
+--------------------+

CALL sys.create_synonym_db('performance_schema', 'perf');
+-----------------------------------------+
| summary                                 |
+-----------------------------------------+
| Created 81 views in the `perf` database |
+-----------------------------------------+

SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| perf               |
| performance_schema |
| sys                |
| test               |
+--------------------+

SHOW FULL TABLES FROM perf;
+------------------------------------------------------+------------+
| Tables_in_perf                                       | Table_type |
+------------------------------------------------------+------------+
| accounts                                             | VIEW       |
| cond_instances                                       | VIEW       |
| events_stages_current                                | VIEW       |
| events_stages_history                                | VIEW       |
| events_stages_history_long                           | VIEW       |
...
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
