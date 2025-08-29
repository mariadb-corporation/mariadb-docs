# USE

## Syntax

```sql
USE db_name
```

## Description

The `'USE db_name'` statement tells MariaDB to use the`db_name` database as the default (current) database forsubsequent statements. The database remains the default until the end of thesession or another `USE` statement is issued:

```sql
USE db1;
SELECT COUNT(*) FROM mytable;   # selects FROM db1.mytable
USE db2;
SELECT COUNT(*) FROM mytable;   # selects FROM db2.mytable
```

The [DATABASE()](../../sql-functions/secondary-functions/information-functions/database.md) function ([SCHEMA()](../../sql-functions/secondary-functions/information-functions/schema.md) is a synonym) returns the default database.

Another way to set the default database is specifying its name at [mariadb](../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) command line client startup.

One cannot use `USE` to a database one has no privileges to. The reason is thata user with no privileges to a database should not be able to know if a database exists or not.

## See Also

* [Identifier Qualifiers](../../sql-structure/sql-language-structure/identifier-qualifiers.md)
* [USE CATALOG](../../../security/user-account-management/catalogs/use-catalog.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
