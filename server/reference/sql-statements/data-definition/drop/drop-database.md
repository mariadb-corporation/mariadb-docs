---
description: >-
  Delete a database and all its contents. This command permanently removes the
  database directory and all tables, routines, and data within it.
---

# DROP DATABASE

## Syntax

```sql
DROP {DATABASE | SCHEMA} [IF EXISTS] db_name
```

## Description

`DROP DATABASE` drops all tables in the database and deletes the database. Be very careful with this statement! To use DROP DATABASE, you need the [DROP privilege](../../account-management-sql-statements/grant.md#table-privileges) on the database. `DROP SCHEMA` is a synonym for `DROP DATABASE`.

**Important:** When a database is dropped, user privileges on the database are not automatically dropped. See [GRANT](../../account-management-sql-statements/grant.md).

#### IF EXISTS

Use `IF EXISTS` to prevent an error from occurring for databases that do not exist. A `NOTE` is generated for each non-existent database when using `IF EXISTS`. See [SHOW WARNINGS](../../administrative-sql-statements/show/show-warnings.md).

### Atomic DDL

{% tabs %}
{% tab title="Current" %}
[MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1061-release-notes) supports [Atomic DDL](../atomic-ddl.md).`DROP DATABASE` is implemented as

```sql
LOOP OVER ALL tables
  DROP TABLE tbl
```

Each individual [DROP TABLE](drop-table.md) is atomic while `DROP DATABASE` as a whole is crash-safe.
{% endtab %}

{% tab title="< 10.6.1" %}
Atomic `DROP` is not available.
{% endtab %}
{% endtabs %}

## Examples

```sql
DROP DATABASE bufg;
Query OK, 0 rows affected (0.39 sec)

DROP DATABASE bufg;
ERROR 1008 (HY000): Can't drop database 'bufg'; database doesn't exist

 \W
SHOW warnings enabled.

DROP DATABASE IF EXISTS bufg;
Query OK, 0 rows affected, 1 warning (0.00 sec)
Note (Code 1008): Can't DROP DATABASE 'bufg'; DATABASE doesn't exist
```

## See Also

* [CREATE DATABASE](../create/create-database.md)
* [ALTER DATABASE](../alter/alter-database.md)
* [SHOW DATABASES](../../administrative-sql-statements/show/show-databases.md)
* [Information Schema SCHEMATA Table](../../../system-tables/information-schema/information-schema-tables/information-schema-schemata-table.md)
* [SHOW CREATE DATABASE](../../administrative-sql-statements/show/show-create-database.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
