---
description: >-
  Remove an existing index from a table. This command deletes the index
  structure, potentially impacting query performance but freeing storage.
---

# DROP INDEX

## Syntax

```sql
DROP INDEX [IF EXISTS] index_name ON tbl_name 
    [WAIT n |NOWAIT]
```

## Description

`DROP INDEX` drops the [index](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/) named `index_name` from the table `tbl_name`. This statement is mapped to an `ALTER TABLE` statement to drop the index.

If another connection is using the table, a [metadata lock](../../transactions/metadata-locking.md) is active, and this statement will wait until the lock is released. This is also true for non-transactional tables.

See [ALTER TABLE](../alter/alter-table/).

Another shortcut, [CREATE INDEX](../create/create-index.md), allows the creation of an index.

To remove the primary key, `PRIMARY` must be specified as index\_name. Note that [the quotes](../../../sql-structure/sql-language-structure/identifier-qualifiers.md) are necessary, because `PRIMARY` is a keyword.

## Privileges

Executing the `DROP INDEX` statement requires the [INDEX](../../account-management-sql-commands/grant.md#table-privileges) privilege for the table or the database.

## Online DDL

Online DDL is used by default with InnoDB, when the drop index operation supports it.

See [InnoDB Online DDL Overview](../../../../server-usage/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-overview.md) for more information on online DDL with [InnoDB](../../../../server-usage/storage-engines/innodb/).

## DROP INDEX IF EXISTS ...

If the `IF EXISTS` clause is used, then MariaDB will return a warning instead of an error if the index does not exist.

## WAIT/NOWAIT

Sets the lock wait timeout. See [WAIT and NOWAIT](../../transactions/wait-and-nowait.md).

## Progress Reporting

MariaDB provides progress reporting for `DROP INDEX` statement for clients\
that support the new progress reporting protocol. For example, if you were using the [mariadb](../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) client, then the progress report might look like this::

## See Also

* [Getting Started with Indexes](../../../../mariadb-quickstart-guides/mariadb-indexes-guide.md)
* [CREATE INDEX](../create/create-index.md)
* [ALTER TABLE](../alter/alter-table/)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
