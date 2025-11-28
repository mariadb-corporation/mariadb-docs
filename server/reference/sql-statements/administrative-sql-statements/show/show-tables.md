---
description: >-
  List tables in a database. This statement displays the names of all
  non-temporary tables in the current or specified database.
---

# SHOW TABLES

## Syntax

```sql
SHOW [FULL] TABLES [FROM db_name]
    [LIKE 'pattern' | WHERE expr]
```

## Description

{% tabs %}
{% tab title="Current" %}
`SHOW TABLES` lists the tables, [sequences](../../../sql-structure/sequences/) and [views](../../../../server-usage/views/) in a given database.
{% endtab %}

{% tab title="< 11.2.0" %}
`SHOW TABLES` lists the tables (only non-`TEMPORARY` tables are shown), [sequences](../../../sql-structure/sequences/) and [views](../../../../server-usage/views/) in a given database.
{% endtab %}
{% endtabs %}

The `LIKE` clause, if present on its own, indicates which table names to match. The `WHERE` and `LIKE` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md). For example, when searching for tables in the `test` database, the column name for use in the `WHERE` and `LIKE` clauses will be `Tables_in_test`

The `FULL` modifier is supported such that `SHOW FULL TABLES` displays a second output column. Values for the second column, `Table_type`, are `BASE TABLE` for a table, `VIEW` for a [view](../../../../server-usage/views/) and `SEQUENCE` for a [sequence](../../../sql-structure/sequences/).

You can also get this information using:

```bash
mariadb-show db_name
```

See [mariadb-show](../../../../clients-and-utilities/administrative-tools/mariadb-show.md) for more details.

If you have no privileges for a base table or view, it does not show up in the output from `SHOW TABLES` or `mariadb-show db_name`.

The [information\_schema.TABLES](../../../system-tables/information-schema/information-schema-tables/information-schema-tables-table.md) table, as well as the [SHOW TABLE STATUS](show-table-status.md) statement, provide extended information about tables.

## Examples

```sql
SHOW TABLES;
+----------------------+
| Tables_in_test       |
+----------------------+
| animal_count         |
| animals              |
| are_the_mooses_loose |
| aria_test2           |
| t1                   |
| view1                |
+----------------------+
```

Showing the tables beginning with _a_ only.

```sql
SHOW TABLES WHERE Tables_in_test LIKE 'a%';
+----------------------+
| Tables_in_test       |
+----------------------+
| animal_count         |
| animals              |
| are_the_mooses_loose |
| aria_test2           |
+----------------------+
```

Showing tables and table types:

```sql
SHOW FULL TABLES;
+----------------+------------+
| Tables_in_test | Table_type |
+----------------+------------+
| s1             | SEQUENCE   |
| student        | BASE TABLE |
| v1             | VIEW       |
+----------------+------------+
```

Showing temporary tables: <= [MariaDB 11.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/what-is-mariadb-111)

```sql
CREATE TABLE t (t INT(11));
CREATE TEMPORARY TABLE t (t INT(11));
CREATE TEMPORARY TABLE te (t INT(11));

SHOW TABLES;
+----------------+
| Tables_in_test |
+----------------+
| t              |
+----------------+
```

From [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes):

```sql
CREATE TABLE t (t INT(11));
CREATE TEMPORARY TABLE t (t INT(11));
CREATE TEMPORARY TABLE te (t INT(11));

SHOW TABLES;
+----------------+
| Tables_in_test |
+----------------+
| te             |
| t              |
| t              |
+----------------+
```

## See Also

* [SHOW TABLE STATUS](show-table-status.md)
* The [information\_schema.TABLES](../../../system-tables/information-schema/information-schema-tables/information-schema-tables-table.md) table

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
