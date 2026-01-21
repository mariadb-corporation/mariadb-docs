---
description: >-
  The Information Schema INNODB_METRICS table contains a wide range of low-level
  performance metrics and counters for the InnoDB storage engine.
---

# Information Schema INNODB\_METRICS Table

The [Information Schema](../../) `INNODB_METRICS` table contains a list of useful InnoDB performance metrics. Each row in the table represents an instrumented counter that can be stopped, started and reset, and which can be grouped together by module.

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Column            | Description                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NAME              | Unique counter name.                                                                                                                                                                                                                                                                                                                                                                                 |
| SUBSYSTEM         | InnoDB subsystem. See below for the matching module to use to enable/disable monitoring this subsytem with the [innodb\_monitor\_enable](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_monitor_enable) and [innodb\_monitor\_disable](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_monitor_disable) system variables. |
| COUNT             | Count since being enabled.                                                                                                                                                                                                                                                                                                                                                                           |
| MAX\_COUNT        | Maximum value since being enabled.                                                                                                                                                                                                                                                                                                                                                                   |
| MIN\_COUNT        | Minimum value since being enabled.                                                                                                                                                                                                                                                                                                                                                                   |
| AVG\_COUNT        | Average value since being enabled.                                                                                                                                                                                                                                                                                                                                                                   |
| COUNT\_RESET      | Count since last being reset.                                                                                                                                                                                                                                                                                                                                                                        |
| MAX\_COUNT\_RESET | Maximum value since last being reset.                                                                                                                                                                                                                                                                                                                                                                |
| MIN\_COUNT\_RESET | Minimum value since last being reset.                                                                                                                                                                                                                                                                                                                                                                |
| AVG\_COUNT\_RESET | Average value since last being reset.                                                                                                                                                                                                                                                                                                                                                                |
| TIME\_ENABLED     | Time last enabled.                                                                                                                                                                                                                                                                                                                                                                                   |
| TIME\_DISABLED    | Time last disabled                                                                                                                                                                                                                                                                                                                                                                                   |
| TIME\_ELAPSED     | Time since enabled                                                                                                                                                                                                                                                                                                                                                                                   |
| TIME\_RESET       | Time last reset.                                                                                                                                                                                                                                                                                                                                                                                     |
| ENABLED           | 1 if enabled, 0 otherwise                                                                                                                                                                                                                                                                                                                                                                            |
| TYPE              | Item type; one of counter, value, status\_counter, set\_owner, set\_member.                                                                                                                                                                                                                                                                                                                          |
| COMMENT           | Counter description.                                                                                                                                                                                                                                                                                                                                                                                 |

Note: In MariaDB 10.4 and earlier the `ENABLED` column was called `STATUS`.

## Enabling and Disabling Counters

Most of the counters are disabled by default. To enable them, use the [innodb\_monitor\_enable](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_monitor_enable) system variable. You can either enable a variable by its name, for example:

```sql
SET GLOBAL innodb_monitor_enable = icp_match;
```

or enable a number of counters grouped by module. The `SUBSYSTEM` field indicates which counters are grouped together, but the following module names need to be used:

| Module Name            | Subsytem Field                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| module\_metadata       | metadata                                                                                                                                                                                                                                                                                                                                                                        |
| module\_lock           | lock                                                                                                                                                                                                                                                                                                                                                                            |
| module\_buffer         | buffer                                                                                                                                                                                                                                                                                                                                                                          |
| module\_buf\_page      | buffer\_page\_io                                                                                                                                                                                                                                                                                                                                                                |
| module\_os             | os                                                                                                                                                                                                                                                                                                                                                                              |
| module\_trx            | transaction                                                                                                                                                                                                                                                                                                                                                                     |
| module\_purge          | purge                                                                                                                                                                                                                                                                                                                                                                           |
| module\_compress       | compression                                                                                                                                                                                                                                                                                                                                                                     |
| module\_file           | file\_system                                                                                                                                                                                                                                                                                                                                                                    |
| module\_index          | index                                                                                                                                                                                                                                                                                                                                                                           |
| module\_adaptive\_hash | adaptive\_hash\_index From [MariaDB 10.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1062-release-notes), if [innodb\_adaptive\_hash\_index](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index) is disabled (the default), adaptive\_hash\_index will not be updated. |
| module\_ibuf\_system   | change\_buffer                                                                                                                                                                                                                                                                                                                                                                  |
| module\_srv            | server                                                                                                                                                                                                                                                                                                                                                                          |
| module\_ddl            | ddl                                                                                                                                                                                                                                                                                                                                                                             |
| module\_dml            | dml                                                                                                                                                                                                                                                                                                                                                                             |
| module\_log            | recovery                                                                                                                                                                                                                                                                                                                                                                        |
| module\_icp            | icp                                                                                                                                                                                                                                                                                                                                                                             |

There are four counters in the `icp` subsystem:

```sql
SELECT NAME, SUBSYSTEM FROM INNODB_METRICS WHERE SUBSYSTEM='icp';
+------------------+-----------+
| NAME             | SUBSYSTEM |
+------------------+-----------+
| icp_attempts     | icp       |
| icp_no_match     | icp       |
| icp_out_of_range | icp       |
| icp_match        | icp       |
+------------------+-----------+
```

To enable them all, use the associated module name from the table above, `module_icp`.

```sql
SET GLOBAL innodb_monitor_enable = module_icp;
```

The `%` wildcard, used to represent any number of characters, can also be used when naming counters, for example:

```sql
SET GLOBAL innodb_monitor_enable = 'buffer%'
```

To disable counters, use the [innodb\_monitor\_disable](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_monitor_disable) system variable, using the same naming rules as described above for enabling.

Counter status is not persistent, and will be reset when the server restarts. It is possible to use the options on the command line, or the `innodb_monitor_enable` option only in a configuration file.

## Resetting Counters

Counters can also be reset. Resetting sets all the `*_COUNT_RESET` values to zero, while leaving the `*_COUNT` values, which perform counts since the counter was enabled, untouched. Resetting is performed with the [innodb\_monitor\_reset](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_monitor_reset) (for individual counters) and [innodb\_monitor\_reset\_all](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_monitor_reset_all) (for all counters) system variables.

## Simplification from MariaDB 10.6

From MariaDB 10.6, the interface was simplified by removing the following variables:

* buffer\_LRU\_batches\_flush
* buffer\_LRU\_batch\_flush\_pages
* buffer\_LRU\_batches\_evict
* buffer\_LRU\_batch\_evict\_pages

And by making the following reflect the status variables:

* buffer\_LRU\_batch\_flush\_total\_pages: [innodb\_buffer\_pool\_pages\_LRU\_flushed](../../../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_buffer_pool_pages_lru_flushed)
* buffer\_LRU\_batch\_evict\_total\_pages: [innodb\_buffer\_pool\_pages\_LRU\_freed](../../../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_buffer_pool_pages_lru_freed)

The intention is to eventually remove the interface entirely (see [MDEV-15706](https://jira.mariadb.org/browse/MDEV-15706)).

## Examples

```sql
SELECT name,subsystem,type,comment FROM INFORMATION_SCHEMA.INNODB_METRICS\G
*************************** 1. row ***************************
     name: metadata_table_handles_opened
subsystem: metadata
     type: counter
  comment: Number of table handles opened
*************************** 2. row ***************************
     name: lock_deadlocks
subsystem: lock
     type: value
  comment: Number of deadlocks
*************************** 3. row ***************************
     name: lock_timeouts
subsystem: lock
     type: value
  comment: Number of lock timeouts
*************************** 4. row ***************************
     name: lock_rec_lock_waits
subsystem: lock
     type: counter
  comment: Number of times enqueued into record lock wait queue
*************************** 5. row ***************************
     name: lock_table_lock_waits
subsystem: lock
     type: counter
  comment: Number of times enqueued into table lock wait queue
*************************** 6. row ***************************
     name: lock_rec_lock_requests
subsystem: lock
     type: counter
  comment: Number of record locks requested
*************************** 7. row ***************************
     name: lock_rec_lock_created
subsystem: lock
     type: counter
  comment: Number of record locks created
*************************** 8. row ***************************
     name: lock_rec_lock_removed
subsystem: lock
     type: counter
  comment: Number of record locks removed from the lock queue
*************************** 9. row ***************************
     name: lock_rec_locks
subsystem: lock
     type: counter
  comment: Current number of record locks on tables
*************************** 10. row ***************************
     name: lock_table_lock_created
subsystem: lock
     type: counter
  comment: Number of table locks created

...

*************************** 207. row ***************************
     name: icp_attempts
subsystem: icp
     type: counter
  comment: Number of attempts for index push-down condition checks
*************************** 208. row ***************************
     name: icp_no_match
subsystem: icp
     type: counter
  comment: Index push-down condition does not match
*************************** 209. row ***************************
     name: icp_out_of_range
subsystem: icp
     type: counter
  comment: Index push-down condition out of range
*************************** 210. row ***************************
     name: icp_match
subsystem: icp
     type: counter
  comment: Index push-down condition matches
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
