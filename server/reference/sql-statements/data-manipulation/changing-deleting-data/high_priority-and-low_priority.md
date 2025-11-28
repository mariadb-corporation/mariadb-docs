---
description: >-
  Control locking priority for table access. These modifiers determine whether
  read or write operations take precedence when multiple threads access a table.
---

# HIGH\_PRIORITY and LOW\_PRIORITY

The [InnoDB](../../../../server-usage/storage-engines/innodb/) storage engine uses row-level locking to ensure data integrity. However some storage engines (such as [MEMORY](../../../../server-usage/storage-engines/memory-storage-engine.md), [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/), [Aria](../../../../server-usage/storage-engines/aria/) and [MERGE](../../../../server-usage/storage-engines/merge.md)) lock the whole table to prevent conflicts. These storage engines use two separate queues to remember pending statements; one is for [SELECTs](../selecting-data/select.md) and the other one is for write statements ([INSERT](../inserting-loading-data/insert.md), [DELETE](delete.md), [UPDATE](update.md)). By default, the latter has a higher priority.

To give write operations a lower priority, the [low\_priority\_updates](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#low_priority_updates) server system variable can be set to `ON`. The option is available on both the global and session levels, and it can be set at startup or via the [SET](../../administrative-sql-statements/set-commands/set.md) statement.

When too many table locks have been set by write statements, some pending SELECTs are executed. The maximum number of write locks that can be acquired before this happens is determined by the [max\_write\_lock\_count](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_write_lock_count) server system variable, which is dynamic.

If write statements have a higher priority (default), the priority of individual write statements ([INSERT](../inserting-loading-data/insert.md), [REPLACE](replace.md), [UPDATE](update.md), [DELETE](delete.md)) can be changed via the `LOW_PRIORITY` attribute, and the priority of a `SELECT` statement can be raised via the `HIGH_PRIORITY` attribute. Also, [LOCK TABLES](../../transactions/lock-tables.md) supports a `LOW_PRIORITY` attribute for `WRITE` locks.

If read statements have a higher priority, the priority of an `INSERT` can be changed via the `HIGH_PRIORITY` attribute. However, the priority of other write statements cannot be raised individually.

The use of `LOW_PRIORITY` or `HIGH_PRIORITY` for an `INSERT` prevents [Concurrent Inserts](../inserting-loading-data/concurrent-inserts.md) from being used.

## See Also

* [INSERT](../inserting-loading-data/insert.md)
* [INSERT DELAYED](../inserting-loading-data/insert-delayed.md)
* [INSERT SELECT](../inserting-loading-data/insert-select.md)
* [Concurrent Inserts](../inserting-loading-data/concurrent-inserts.md)
* [INSERT - Default & Duplicate Values](../inserting-loading-data/insert-default-duplicate-values.md)
* [INSERT IGNORE](../inserting-loading-data/insert-ignore.md)
* [INSERT ON DUPLICATE KEY UPDATE](../inserting-loading-data/insert-on-duplicate-key-update.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
