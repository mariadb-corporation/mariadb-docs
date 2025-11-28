---
description: >-
  Add an index to an existing table. This statement improves query performance
  by creating a data structure for rapid lookups on specific columns.
---

# CREATE INDEX

## Syntax

```sql
CREATE [OR REPLACE] [UNIQUE|FULLTEXT|SPATIAL] INDEX 
  [IF NOT EXISTS] index_name
    [index_type]
    ON tbl_name (index_col_name,...)
    [WAIT n | NOWAIT]
    [index_option]
    [algorithm_option | lock_option] ...

index_col_name:
    col_name [(length)] [ASC | DESC]

index_type:
    USING {BTREE | HASH | RTREE}

index_option:
    [ KEY_BLOCK_SIZE [=] value
  | index_type
  | WITH PARSER parser_name
  | COMMENT 'string'
  | CLUSTERING={YES| NO} ]
  [ IGNORED | NOT IGNORED ]

algorithm_option:
    ALGORITHM [=] {DEFAULT|INPLACE|COPY|NOCOPY|INSTANT}

lock_option:
    LOCK [=] {DEFAULT|NONE|SHARED|EXCLUSIVE}
```

## Description

The `CREATE INDEX` statement is used to add indexes to a table. Indexes can be created at the same as the table, with the [CREATE TABLE](create-table.md) statement. In some cases, such as for InnoDB primary keys, doing so during creation is preferable, as adding a primary key will involve rebuilding the table.

The statement is mapped to an `ALTER TABLE` statement to create [indexes](../../../../server-usage/tables/mariadb-indexes-guide-1.md). See [ALTER TABLE](../alter/alter-table/). `CREATE INDEX` cannot be used to create a [PRIMARY KEY](../../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#primary-key); use `ALTER TABLE` instead.

If another connection is using the table, a [metadata lock](../../transactions/metadata-locking.md) is active, and this statement will wait until the lock is released. This is also true for non-transactional tables.

Another shortcut, [DROP INDEX](../drop/drop-index.md), allows the removal of an index.

For valid identifiers to use as index names, see [Identifier Names](../../../sql-structure/sql-language-structure/identifier-names.md).

For limits on InnoDB indexes, see [InnoDB Limitations](../../../../server-usage/storage-engines/innodb/innodb-limitations.md).

Note that `KEY_BLOCK_SIZE` is currently ignored in `CREATE INDEX`, although it is included in the output of [SHOW CREATE TABLE](../../administrative-sql-statements/show/show-create-table.md).

## Privileges

Executing the `CREATE INDEX` statement requires the [INDEX](../../account-management-sql-statements/grant.md) privilege for the table or the database.

## Online DDL

Online DDL is supported with the [ALGORITHM](create-index.md#algorithm) and [LOCK](create-index.md#lock) clauses.

See [InnoDB Online DDL Overview](../../../../server-usage/storage-engines/innodb/innodb-online-ddl/) for more information on online DDL with InnoDB.

## CREATE OR REPLACE INDEX

If the `OR REPLACE` clause is used and if the index already exists, then instead of returning an error, the server will drop the existing index and replace it with the newly defined index.

## CREATE INDEX IF NOT EXISTS

If the `IF NOT EXISTS` clause is used, then the index will only be created if an index with the same name does not already exist. If the index already exists, then a warning will be triggered by default.

## Index Definitions

See [CREATE TABLE: Index Definitions](create-table.md#index-definitions) for information about index definitions.

## WAIT/NOWAIT

Set the lock wait timeout. See [WAIT and NOWAIT](../../transactions/wait-and-nowait.md).

## ALGORITHM

See [ALTER TABLE: ALGORITHM](../alter/alter-table/#algorithm) for more information.

## LOCK

See [ALTER TABLE: LOCK](../alter/alter-table/#lock) for more information.

## Progress Reporting

MariaDB provides progress reporting for `CREATE INDEX` statement for clients that support the new progress reporting protocol. For example, if you were using the [mariadb](../../../../clients-and-utilities/mariadb-client/) client, then the progress report might look like this::

```sql
CREATE INDEX i ON tab (num);
Stage: 1 of 2 'copy to tmp table'    46% of stage
```

The progress report is also shown in the output of the [SHOW PROCESSLIST](../../administrative-sql-statements/show/show-processlist.md) statement and in the contents of the [information\_schema.PROCESSLIST](../../../system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) table.

See [Progress Reporting](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting) for more information.

## WITHOUT OVERLAPS

{% tabs %}
{% tab title="Current" %}
The `WITHOUT OVERLAPS` clause allows you to constrain a primary or unique index such that [application-time periods](../../../sql-structure/temporal-tables/application-time-periods.md) cannot overlap. It can be used like this:

```sql
CREATE UNIQUE INDEX u ON rooms (room_number, p WITHOUT OVERLAPS);
```
{% endtab %}

{% tab title="< 10.5.3" %}
`WITHOUT OVERLAPS` is not available.
{% endtab %}
{% endtabs %}

## Examples

Creating a unique index:

```sql
CREATE UNIQUE INDEX HomePhone ON Employees(Home_Phone);
```

OR REPLACE and IF NOT EXISTS:

```sql
CREATE INDEX xi ON xx5 (x);
Query OK, 0 rows affected (0.03 sec)

CREATE INDEX xi ON xx5 (x);
ERROR 1061 (42000): Duplicate key name 'xi'

CREATE OR REPLACE INDEX xi ON xx5 (x);
Query OK, 0 rows affected (0.03 sec)

CREATE INDEX IF NOT EXISTS xi ON xx5 (x);
Query OK, 0 rows affected, 1 warning (0.00 sec)

SHOW WARNINGS;
+-------+------+-------------------------+
| Level | Code | Message                 |
+-------+------+-------------------------+
| Note  | 1061 | Duplicate key name 'xi' |
+-------+------+-------------------------+
```

## See Also

* [Identifier Names](../../../sql-structure/sql-language-structure/identifier-names.md)
* [Getting Started with Indexes](../../../../mariadb-quickstart-guides/mariadb-indexes-guide.md)
* [ALTER TABLE](../alter/alter-table/)
* [DROP INDEX](../drop/drop-index.md)
* [SHOW INDEX](../../administrative-sql-statements/show/show-index.md)
* [SPATIAL INDEX](../../../sql-structure/geometry/spatial-index.md)
* [Full-text Indexes](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/)
* [WITHOUT OVERLAPS](create-index.md#without-overlaps)
* [Ignored Indexes](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/ignored-indexes.md)
* [InnoDB Limitations](../../../../server-usage/storage-engines/innodb/innodb-limitations.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
