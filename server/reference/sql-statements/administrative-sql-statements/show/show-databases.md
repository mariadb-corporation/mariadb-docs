---
description: >-
  List databases on the MariaDB server. View the names of all databases
  available to the current user.
---

# SHOW DATABASES

## Syntax

```sql
SHOW {DATABASES | SCHEMAS}
    [LIKE 'pattern' | WHERE expr]
```

## Description

`SHOW DATABASES` lists the databases on the MariaDB server host.`SHOW SCHEMAS` is a synonym for`SHOW DATABASES`. The `LIKE` clause, if present on its own, indicates which database names to match. The `WHERE` and `LIKE` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).

You see only those databases for which you have some kind of privilege, unless you have the global [SHOW DATABASES privilege](../../account-management-sql-statements/grant.md). You can also get this list using the [mariadb-show](../../../../clients-and-utilities/administrative-tools/mariadb-show.md) command.

If the server was started with the `--skip-show-database` option, you cannot use this statement at all unless you have the [SHOW DATABASES privilege](../../account-management-sql-statements/grant.md).

The list of results returned by `SHOW DATABASES` is based on directories in the data directory, which is how MariaDB implements databases. It's possible that output includes directories that do not correspond to actual databases.

The [Information Schema SCHEMATA table](../../../system-tables/information-schema/information-schema-tables/information-schema-schemata-table.md) also contains database information.

## Examples

```sql
SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| test               |
+--------------------+
```

```sql
SHOW DATABASES LIKE 'm%';
+---------------+
| Database (m%) |
+---------------+
| mysql         |
+---------------+
```

## See Also

* [CREATE DATABASE](../../data-definition/create/create-database.md)
* [ALTER DATABASE](../../data-definition/alter/alter-database.md)
* [DROP DATABASE](../../data-definition/drop/drop-database.md)
* [SHOW CREATE DATABASE](show-create-database.md)
* [Character Sets and Collations](../../../data-types/string-data-types/character-sets/supported-character-sets-and-collations.md)
* [Information Schema SCHEMATA Table](../../../system-tables/information-schema/information-schema-tables/information-schema-schemata-table.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
