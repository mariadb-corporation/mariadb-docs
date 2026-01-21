---
description: >-
  Explains how to use the Flashback feature (via `mysqlbinlog --flashback`) to
  rollback transactions by reversing the binary log events, useful for
  recovering from accidental data modifications.
---

# Flashback

Flashback is a feature that allows instances, databases or tables to be rolled back to an old snapshot.

Flashback is currently supported only over DML statements ([INSERT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md), [DELETE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md), [UPDATE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md)). An upcoming version of MariaDB will add support for flashback over DDL statements ([DROP](../../../reference/sql-statements/data-definition/drop/drop-table.md), [TRUNCATE](../../../reference/sql-statements/table-statements/truncate-table.md), [ALTER](../../../reference/sql-statements/data-definition/alter/alter-table/), etc.) by copying or moving the current table to a reserved and hidden database, and then copying or moving back when using flashback. See [MDEV-10571](https://jira.mariadb.org/browse/MDEV-10571).

Flashback is achieved in MariaDB Server using existing support for full image format binary logs ([binlog\_row\_image=FULL](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_row_image)), so it supports all engines.

The real work of Flashback is done by [mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/) with `--flashback`. This causes events to be translated: `INSERT` to `DELETE`, `DELETE` to `INSERT`, and for `UPDATE` statements, the before and after images are swapped.

When executing `mariadb-binlog` with `--flashback`, the Flashback events are stored in memory. You must make sure your server has enough memory for this feature.

## Arguments

* [mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/) has the option `--flashback` or `-B` that lets it work in flashback mode.
* [mariadbd](../../starting-and-stopping-mariadb/mariadbd-options.md) has the option [--flashback](../../starting-and-stopping-mariadb/mariadbd-options.md#-flashback) that enables the binary log and sets `binlog_format=ROW`. It is not mandatory to use this option if you have already enabled those options directly.

Do not use `-v` `-vv` options, as this adds verbose information to the binary log which can cause problems when importing. See [MDEV-12066](https://jira.mariadb.org/browse/MDEV-12066) and [MDEV-12067](https://jira.mariadb.org/browse/MDEV-12067).

## Example

With a table "mytable" in database "test", you can compare the output with `--flashback` and without.

```
mariadb-binlog /var/lib/mysql/mysql-bin.000001 -vv -d test -T mytable \
    --start-datetime="2013-03-27 14:54:00" > review.sql
```

```
mariadb-binlog /var/lib/mysql/mysql-bin.000001 -vv -d test -T mytable \
    --start-datetime="2013-03-27 14:54:00" --flashback > flashback.sql
```

If you know the exact position, `--start-position` can be used instead of `--start-datetime`.

Then, by importing the output file (`mariadb < flashback.sql`), you can flash your database/table back to the specified time or position.

## Common Use Case

A common use case for Flashback is the following scenario:

* You have one primary and two replicas, one started with `--flashback` (i.e. with binary logging enabled, using [binlog\_format=ROW](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format), and [binlog\_row\_image=FULL](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_row_image)).
* Something goes wrong on the primary (like a wrong update or delete) and you would like to revert to a state of the database (or just a table) at a certain point in time.
* Remove the flashback-enabled replica from replication.
* Invoke [mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/) to find the exact log position of the first offending operation after the state you want to revert to.
* Run `mariadb-binlog --flashback --start-position=xyz | mariadb` to pipe the output of `mariadb-binlog` directly to the `mariadb` client, or save the output to a file and then direct the file to the command-line client.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
