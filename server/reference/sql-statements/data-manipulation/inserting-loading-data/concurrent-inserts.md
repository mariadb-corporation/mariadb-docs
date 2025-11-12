# Concurrent Inserts

The [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/) storage engine supports concurrent inserts. This feature allows [SELECT](../selecting-data/select.md) statements to be executed during [INSERT](insert.md) operations, reducing contention.

Whether concurrent inserts can be used or not depends on the value of the [concurrent\_insert](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#concurrent_insert) server system variable:

* `NEVER` (0) disables concurrent inserts.
* `AUTO` (1) allows concurrent inserts only when the target table has no free blocks (no data in the middle of the table has been deleted after the last [OPTIMIZE TABLE](../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md)). This is the default.
* `ALWAYS` (2) always enables concurrent inserts, in which case new rows are added at the end of a table if the table is being used by another thread.

If the [binary log](../../../../server-management/server-monitoring-logs/binary-log/) is used, [CREATE TABLE ... SELECT](../../data-definition/create/create-table.md#create-table-select) and [INSERT ... SELECT](insert-select.md) statements cannot use concurrent inserts. These statements acquire a read lock on the table, so concurrent inserts will need to wait. This way, the log can be safely used to restore data.

Concurrent inserts are not used by replicas with the row-based [replication](../../../../ha-and-performance/standard-replication/) (see [binary log formats](../../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md)).

If an [INSERT](insert.md) statement contains the [HIGH\_PRIORITY](../changing-deleting-data/high_priority-and-low_priority.md) clause, concurrent inserts cannot be used. [INSERT ... DELAYED](insert-delayed.md) is usually unneeded if concurrent inserts are enabled.

[LOAD DATA INFILE](load-data-into-tables-or-index/load-data-infile.md) uses concurrent inserts if the `CONCURRENT` keyword is specified and [concurrent\_insert](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#concurrent_insert) is not `NEVER`. This makes the statement slower (even if no other sessions access the table) but reduces contention.

[LOCK TABLES](../../transactions/lock-tables.md) allows non-conflicting concurrent inserts if a `READ LOCAL` lock is used. Concurrent inserts are not allowed if the `LOCAL` keyword is omitted.

## Notes

The decision to enable concurrent insert for a table is done when the table is opened. If you change the value of [concurrent\_insert](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#concurrent_insert), it will only affect newly opened tables. If you want it to work for also for tables in use or cached, you should do [FLUSH TABLES](../../administrative-sql-statements/flush-commands/flush.md) after setting the variable.

## See Also

* [INSERT](insert.md)
* [INSERT DELAYED](insert-delayed.md)
* [INSERT SELECT](insert-select.md)
* [HIGH\_PRIORITY and LOW\_PRIORITY](../changing-deleting-data/high_priority-and-low_priority.md)
* [INSERT - Default & Duplicate Values](insert-default-duplicate-values.md)
* [INSERT IGNORE](insert-ignore.md)
* [INSERT ON DUPLICATE KEY UPDATE](insert-on-duplicate-key-update.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
