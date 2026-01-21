---
description: >-
  Return the default database name. This function outputs the name of the
  currently selected database for the session.
---

# DATABASE

## Syntax

```sql
DATABASE()
SCHEMA()
```

## Description

Returns the default (current) database name as a string in the utf8 [character set](../../../data-types/string-data-types/character-sets/). If there is no default database, `DATABASE()` returns `NULL`. Within a [stored routine](../../../../server-usage/stored-routines/), the default database is the database that the routine is associated with, which is not necessarily the same as the database that is the default in the calling context.

`SCHEMA()` is a synonym for `DATABASE()`.

To select a default database, the [USE](../../../sql-statements/administrative-sql-statements/use-database.md) statement can be run. Another way to set the default database is specifying its name at [mariadb](../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) command line client startup.

## Examples

```sql
SELECT DATABASE();
+------------+
| DATABASE() |
+------------+
| NULL       |
+------------+

USE test;
Database changed

SELECT DATABASE();
+------------+
| DATABASE() |
+------------+
| test       |
+------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
