# DROP VIEW

## Syntax

```sql
DROP VIEW [IF EXISTS]
    view_name [, view_name] ...
    [RESTRICT | CASCADE]
```

## Description

`DROP VIEW` removes one or more [views](./). You must have the DROP privilege for\
each view. If any of the views named in the argument list do not exist, MariaDB\
returns an error indicating by name which non-existing views it was unable to\
drop, but it also drops all of the views in the list that do exist.

The `IF EXISTS` clause prevents an error from occurring for views that don't\
exist. When this clause is given, a `NOTE` is generated for each non-existent\
view. See [SHOW WARNINGS](../../reference/sql-statements/administrative-sql-statements/show/show-warnings.md).

`RESTRICT` and `CASCADE`, if given, are parsed and ignored.

It is possible to specify view names as `db_name`.`view_name`. This is useful to delete views from multiple databases with one statement. See [Identifier Qualifiers](../../reference/sql-structure/sql-language-structure/identifier-qualifiers.md) for details.

The [DROP privilege](../../reference/sql-statements/account-management-sql-statements/grant.md#table-privileges) is required to use `DROP TABLE` on non-temporary tables. For temporary tables, no privilege is required, because such tables are only visible for the current session.

If a view references another view, it are possible to drop the referenced view. However, the other view will reference a view which does not exist any more. Thus, querying it will produce an error similar to the following:

```sql
ERROR 1356 (HY000): View 'db_name.view_name' references invalid table(s) or 
column(s) or function(s) or definer/invoker of view lack rights to use them
```

This problem is reported in the output of [CHECK TABLE](../../reference/sql-statements/table-statements/check-table.md).

Note that it is not necessary to use `DROP VIEW` to replace an existing view, because [CREATE VIEW](create-view.md) has an `OR REPLACE` clause.

### Atomic DDL

**MariaDB starting with** [**10.6.1**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1061-release-notes)

[MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1061-release-notes) supports [Atomic DDL](../../reference/sql-statements/data-definition/atomic-ddl.md) and `DROP VIEW` for a singular view is atomic. Dropping multiple views is crash-safe.

## Examples

```sql
DROP VIEW v,v2;
```

Given views `v` and `v2`, but no view `v3`

```sql
DROP VIEW v,v2,v3;
ERROR 1051 (42S02): Unknown table 'v3'
```

```sql
DROP VIEW IF EXISTS v,v2,v3;
Query OK, 0 rows affected, 1 warning (0.01 sec)

SHOW WARNINGS;
+-------+------+-------------------------+
| Level | Code | Message                 |
+-------+------+-------------------------+
| Note  | 1051 | Unknown table 'test.v3' |
+-------+------+-------------------------+
```

## See Also

* [CREATE VIEW](create-view.md)
* [ALTER VIEW](alter-view.md)
* [SHOW CREATE VIEWS](../../reference/sql-statements/administrative-sql-statements/show/show-create-view.md)
* [INFORMATION SCHEMA VIEWS Table](information-schema-views-table.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
