---
description: >-
  Return the server version. This function outputs a string indicating the
  version number and distribution of the MariaDB server.
---

# VERSION

## Syntax

```sql
VERSION()
```

## Description

Returns a string that indicates the MariaDB server version. The string uses the utf8 [character set](../../../data-types/string-data-types/character-sets/).

## Examples

```sql
SELECT VERSION();
+----------------+
| VERSION()      |
+----------------+
| 10.4.7-MariaDB |
+----------------+
```

The `VERSION()` string may have one or more of the following suffixes:

| Suffix    | Description                                                               |
| --------- | ------------------------------------------------------------------------- |
| -embedded | The server is an embedded server (libmariadbd).                           |
| -log      | General logging, slow logging or binary (replication) logging is enabled. |
| -debug    | The server is compiled for debugging.                                     |
| -valgrind | The server is compiled to be instrumented with valgrind.                  |

## Changing the Version String

Some old legacy code may break because they are parsing the`VERSION` string and expecting a MySQL string or a simple version string like Joomla til API17, see [MDEV-7780](https://jira.mariadb.org/browse/MDEV-7780).

You can fool these applications by setting the version string from the command line or the `my.cnf` files with [--version=...](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#version).

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
