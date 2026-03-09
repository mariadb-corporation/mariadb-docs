---
description: >-
  Complete DROP TABLE syntax: TEMPORARY, IF EXISTS, WAIT/NOWAIT,
  RESTRICT/CASCADE options, metadata locks, atomic DROP, and replication
  behavior.
---

# DROP TABLE

## Syntax

```sql
DROP [TEMPORARY] TABLE [IF EXISTS] [/*COMMENT TO SAVE*/]
    tbl_name [, tbl_name] ...
    [WAIT n|NOWAIT]
    [RESTRICT | CASCADE]
```

## Description

`DROP TABLE` removes one or more tables. You must have the `DROP` privilege for each table. All table data and the table definition are removed, as well as [triggers](../../../../server-usage/triggers-events/triggers/) associated to the table, so be careful with this statement! If any of the tables named in the argument list do not exist, MariaDB returns an error indicating by name which non-existing tables it was unable to drop, but it also drops all of the tables in the list that do exist.

**Important**: When a table is dropped, user privileges on the table are not automatically dropped. See [GRANT](../../account-management-sql-statements/grant.md).

If another thread is using the table in an explicit transaction or an autocommit transaction, then the thread acquires a [metadata lock (MDL)](../../transactions/metadata-locking.md) on the table. The `DROP TABLE` statement will wait in the "Waiting for table metadata lock" [thread state](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-states/) until the MDL is released. MDLs are released in the following cases:

* If an MDL is acquired in an explicit transaction, then the MDL will be released when the transaction ends.
* If an MDL is acquired in an autocommit transaction, then the MDL will be released when the statement ends.
* Transactional and non-transactional tables are handled the same.

Note that for a partitioned table, `DROP TABLE` permanently removes the table definition, all of its partitions, and all of the data which was stored in those partitions. It also removes the partitioning definition (.par) file associated with the dropped table.

For each referenced table, `DROP TABLE` drops a temporary table with that name, if it exists. If it does not exist, and the `TEMPORARY` keyword is not used, it drops a non-temporary table with the same name, if it exists. The `TEMPORARY` keyword ensures that a non-temporary table will not accidentally be dropped.

Use `IF EXISTS` to prevent an error from occurring for tables that do not\
exist. A `NOTE` is generated for each non-existent table when using`IF EXISTS`. See [SHOW WARNINGS](../../administrative-sql-statements/show/show-warnings.md).

If a [foreign key](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md) references this table, the table cannot be dropped. In this case, it is necessary to drop the foreign key first.

`RESTRICT` and `CASCADE` are allowed to make porting from other database systems easier. In MariaDB, they do nothing.

The comment before the table names (`/*COMMENT TO SAVE*/`) is stored in the [binary log](../../../../server-management/server-monitoring-logs/binary-log/). That feature can be used by replication tools to send their internal messages.

It is possible to specify table names as `db_name`.`tab_name`. This is useful to delete tables from multiple databases with one statement. See [Identifier Qualifiers](../../../sql-structure/sql-language-structure/identifier-qualifiers.md) for details.

The [DROP privilege](../../account-management-sql-statements/grant.md#table-privileges) is required to use `DROP TABLE` on non-temporary tables. For temporary tables, no privilege is required, because such tables are only visible for the current session.

**Note:** `DROP TABLE` automatically commits the current active transaction, unless you use the `TEMPORARY` keyword.

{% tabs %}
{% tab title="Current" %}
`DROP TABLE` reliably deletes table remnants inside a storage engine even if the `.frm` file is missing.
{% endtab %}

{% tab title="< 10.5.4" %}
`DROP TABLE` does **not** reliably delete table remnants inside a storage engine even if the `.frm` file is missing. A missing `.frm` file will result in the statement failing.
{% endtab %}
{% endtabs %}

### WAIT/NOWAIT

Set the lock wait timeout. See [WAIT and NOWAIT](../../transactions/wait-and-nowait.md).

## DROP TABLE in replication

`DROP TABLE` has the following characteristics in [replication](../../../../server-usage/storage-engines/myrocks/myrocks-and-replication.md):

* `DROP TABLE IF EXISTS` are always logged.
* `DROP TABLE` without `IF EXISTS` for tables that don't exist are not written to the [binary log](../../../../server-management/server-monitoring-logs/binary-log/).
* Dropping of `TEMPORARY` tables are prefixed in the log with `TEMPORARY`. These drops are only logged when running [statement](../../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based) or [mixed mode](../../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#mixed) replication.
* One `DROP TABLE` statement can be logged with up to 3 different `DROP` statements:
  * `DROP TEMPORARY TABLE list_of_non_transactional_temporary_tables`
  * `DROP TEMPORARY TABLE list_of_transactional_temporary_tables`
  * `DROP TABLE list_of_normal_tables`

`DROP TABLE` on the primary is treated on the replica as `DROP TABLE IF EXISTS`. You can change that by setting [slave-ddl-exec-mode](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) to `STRICT`.

## Dropping an Internal #sql-... Table

{% tabs %}
{% tab title="Current" %}
[DROP TABLE is atomic.](drop-table.md#atomic-drop-table)
{% endtab %}

{% tab title="< 10.6" %}
if the [mariadbd process](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) is killed during an [ALTER TABLE](../alter/alter-table/), you may find a table named #sql-... in your data directory. These temporary tables will always be deleted automatically.

If you want to delete one of these tables explicitly you can do so by using the following syntax:

```
DROP TABLE `#mysql50##sql-...`;
```

When running an `ALTER TABLE…ALGORITHM=INPLACE` that rebuilds the table, InnoDB will create an internal `#sql-ib` table.

The same name as the .frm file is used for the intermediate copy of the table. The #sql-ib names are used by TRUNCATE and delayed DROP.

The #sql-ib tables will be deleted automatically.
{% endtab %}
{% endtabs %}

## Dropping All Tables in a Database

The best way to drop all tables in a database is by executing [DROP DATABASE](drop-database.md), which will drop the database itself, and all tables in it.

However, if you want to drop all tables in the database, but you also want to keep the database itself and any other non-table objects in it, then you would need to execute `DROP TABLE` to drop each individual table. You can construct these `DROP TABLE` commands by querying the [TABLES](../../../system-tables/information-schema/information-schema-tables/information-schema-tables-table.md) table in the [information\_schema](../../../system-tables/information-schema/information-schema-tables/) database. For example:

```
SELECT CONCAT('DROP TABLE IF EXISTS `', TABLE_SCHEMA, '`.`', TABLE_NAME, '`;')
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'mydb';
```

## Atomic DROP TABLE

**MariaDB starting with** [**10.6.1**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1061-release-notes)

{% tabs %}
{% tab title="Current" %}
`DROP TABLE` for a single table is atomic ([MDEV-25180](https://jira.mariadb.org/browse/MDEV-25180)) for most engines, including InnoDB, MyRocks, MyISAM and Aria. This means that if there is a crash (server down or power outage) during `DROP TABLE`, all tables that have been processed so far will be completely dropped, including related trigger files and status entries, and the [binary log](../../../../server-management/server-monitoring-logs/binary-log/) will include a `DROP TABLE` statement for the dropped tables. Tables for which the drop had not started will be left intact.`DROP TABLE` was extended to be able to delete a table that was only partly dropped ([MDEV-11412](https://jira.mariadb.org/browse/MDEV-11412)), as explained above. Atomic `DROP TABLE` is the final piece to make `DROP TABLE` fully reliable. Dropping multiple tables is crash-safe. See [Atomic DDL](../atomic-ddl.md) for more information.
{% endtab %}

{% tab title="< 10.6.1" %}
There is a small chance that, during a server crash happening in the middle of `DROP TABLE`, some storage engines that were using multiple storage files, like [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/), could have only a part of its internal files dropped. In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), `DROP TABLE` was extended to be able to delete a table that was only partly dropped ([MDEV-11412](https://jira.mariadb.org/browse/MDEV-11412)) as explained above. Atomic `DROP TABLE` is the final piece to make `DROP TABLE` fully reliable. Dropping multiple tables is crash-safe. See [Atomic DDL](../atomic-ddl.md) for more information.
{% endtab %}
{% endtabs %}

## Examples

```sql
DROP TABLE Employees, Customers;
```

## Notes

Beware that `DROP TABLE` can drop both tables and [sequences](../../../sql-structure/sequences/create-sequence.md). This is mainly done to allow old tools like [mariadb-dump](../../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) (previously mysqldump) to work with sequences.

## See Also

* [CREATE TABLE](../create/create-table.md)
* [ALTER TABLE](../alter/alter-table/)
* [SHOW CREATE TABLE](../../administrative-sql-statements/show/show-create-table.md)
* [DROP SEQUENCE](../../../sql-structure/sequences/drop-sequence.md)
* Variable [slave-ddl-exec-mode](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md).

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
