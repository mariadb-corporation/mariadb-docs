---
description: >-
  Queue inserts for later execution. This MyISAM-specific extension returns
  control immediately to the client while the server inserts rows when the table
  is free.
---

# INSERT DELAYED

## Syntax

```
INSERT DELAYED ...
```

## Description

The `DELAYED` option for the [INSERT](insert.md) statement is a MariaDB/MySQL extension to standard SQL that is very useful if you have clients that cannot or need not wait for the `INSERT` to complete. This is a common situation when you use MariaDB for logging and you also periodically run `SELECT` and `UPDATE` statements that take a long time to complete.

When a client uses `INSERT DELAYED`, it gets an okay from the server at once, and the row is queued to be inserted when the table is not in use by any other thread.

Another major benefit of using `INSERT DELAYED` is that inserts from many clients are bundled together and written in one block. This is much faster than performing many separate inserts.

Note that `INSERT DELAYED` is slower than a normal`INSERT` if the table is not otherwise in use. There is also the additional overhead for the server to handle a separate thread for each table for which there are delayed rows. This means that you should use`INSERT DELAYED` only when you are really sure that you need it.

The queued rows are held only in memory until they are inserted into the table. This means that if you terminate mariadbd forcibly (for example, with kill -9) or if mariadbd dies unexpectedly, any queued rows that have not been written to disk are lost.

The number of concurrent `INSERT DELAYED` threads is limited by the [max\_delayed\_threads](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#max_delayed_threads) server system variables. If it is set to 0, `INSERT DELAYED` is disabled. The session value can be equal to the global value, or 0 to disable this statement for the current session. If this limit has been reached, the `DELAYED` clause will be silently ignore for subsequent statements (no error will be produced).

### Limitations

There are some limitations on the use of `DELAYED`:

* `INSERT DELAYED` works only with [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/), [MEMORY](../../../../server-usage/storage-engines/memory-storage-engine.md), [ARCHIVE](../../../../server-usage/storage-engines/archive.md),\
  and [BLACKHOLE](../../../../server-usage/storage-engines/blackhole.md) tables. If you execute INSERT DELAYED with another storage engine, you will get an error like this: `ERROR 1616 (HY000): DELAYED option not supported for table 'tab_name'`
* For MyISAM tables, if there are no free blocks in the middle of the data file, concurrent SELECT and INSERT statements are supported. Under these circumstances, you very seldom need to use `INSERT DELAYED` with MyISAM.
* `INSERT DELAYED` should be used only for`INSERT` statements that specify value lists. The server\
  ignores `DELAYED` for `INSERT ... SELECT` or `INSERT ... ON DUPLICATE KEY UPDATE` statements.
* Because the `INSERT DELAYED` statement returns immediately, before the rows are inserted, you cannot use`LAST_INSERT_ID()` to get the`AUTO_INCREMENT` value that the statement might generate.
* `DELAYED` rows are not visible to `SELECT` statements until they actually have been inserted.
* After `INSERT DELAYED`, [ROW\_COUNT()](../../../sql-functions/secondary-functions/information-functions/row_count.md) returns the number of the rows you tried to insert, not the number of the successful writes.
* `DELAYED` is ignored on slave replication servers, so that`INSERT DELAYED` is treated as a normal `INSERT` on slaves. This is because`DELAYED` could cause the slave to have different data than\
  the master. `INSERT DELAYED` statements are not [safe for replication](../../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).
* Pending `INSERT DELAYED` statements are lost if a table is write locked and ALTER TABLE is used to modify the table structure.
* `INSERT DELAYED` is not supported for views. If you try, you will get an error like this: `ERROR 1347 (HY000): 'view_name' is not BASE TABLE`
* `INSERT DELAYED` is not supported for [partitioned tables](../../../../server-usage/partitioning-tables/).
* `INSERT DELAYED` is not supported within [stored programs](../../../../server-usage/stored-routines/).
* `INSERT DELAYED` does not work with [triggers](../../../../server-usage/triggers-events/triggers/).
* `INSERT DELAYED` does not work if there is a check constraint in place.
* `INSERT DELAYED` does not work if [skip-new](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-skip-new) mode is active.

## See Also

* [INSERT](insert.md)
* [INSERT SELECT](insert-select.md)
* [HIGH\_PRIORITY and LOW\_PRIORITY](../changing-deleting-data/high_priority-and-low_priority.md)
* [Concurrent Inserts](concurrent-inserts.md)
* [INSERT - Default & Duplicate Values](insert-default-duplicate-values.md)
* [INSERT IGNORE](insert-ignore.md)
* [INSERT ON DUPLICATE KEY UPDATE](insert-on-duplicate-key-update.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
