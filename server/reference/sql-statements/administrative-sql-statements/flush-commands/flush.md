# FLUSH

## Syntax

```sql
FLUSH [NO_WRITE_TO_BINLOG | LOCAL]
    flush_option [, flush_option] ...
```

or when flushing tables:

```sql
FLUSH [NO_WRITE_TO_BINLOG | LOCAL] TABLES [table_list]  [table_flush_option]
```

where `table_list` is a list of tables separated by `,` (comma).

## Description

The `FLUSH` statement clears or reloads various internal caches used by MariaDB. To execute `FLUSH`, you must have the `RELOAD` privilege. See [GRANT](../../account-management-sql-statements/grant.md).

The `RESET` statement is similar to `FLUSH`. See [RESET](../reset.md).

You cannot issue a FLUSH statement from within a [stored function](../../../../server-usage/stored-routines/stored-functions/) or a [trigger](../../../../server-usage/triggers-events/triggers/). Doing so within a stored procedure is permitted, as long as it is not called by a stored function or trigger. See [Stored Routine Limitations](../../../../server-usage/stored-routines/stored-routine-limitations.md), [Stored Function Limitations](../../../../server-usage/stored-routines/stored-functions/stored-function-limitations.md) and [Trigger Limitations](../../../../server-usage/triggers-events/triggers/trigger-limitations.md).

If a listed table is a view, an error like the following will be produced:

```
ERROR 1347 (HY000): 'test.v' is not BASE TABLE
```

By default, `FLUSH` statements are written to the [binary log](../../../../server-management/server-monitoring-logs/binary-log/) and will be [replicated](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/sql-statements/administrative-sql-statements/flush-commands/broken-reference/README.md). The `NO_WRITE_TO_BINLOG` keyword (`LOCAL` is an alias) will ensure the statement is not written to the binary log.

The different flush options are:

| Option                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Option                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| CHANGED\_PAGE\_BITMAPS                                  | [XtraDB](../../../../server-usage/storage-engines/innodb/innodb-unmaintained/about-xtradb.md) only. Internal command used for backup purposes. See the [Information Schema CHANGED\_PAGE\_BITMAPS Table](../system-tables/information-schema/information-schema-tables/information-schema-xtradb-tables/information-schema-changed_page_bitmaps-table.md).                                                                                                                                                                                                                                                                                                                                                                                              |
| CLIENT\_STATISTICS                                      | Reset client statistics (see [SHOW CLIENT\_STATISTICS](../show/show-client-statistics.md)).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DES\_KEY\_FILE                                          | Reloads the DES key file (Specified with the [--des-key-file startup option](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md)).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| HOSTS                                                   | Flush the hostname cache (used for converting ip to host names and for unblocking blocked hosts. See [max\_connect\_errors](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_connect_errors) and [performance\_schema.host\_cache](../system-tables/performance-schema/performance-schema-tables/performance-schema-host_cache-table.md)                                                                                                                                                                                                                                                                                                                                                          |
| INDEX\_STATISTICS                                       | Reset index statistics (see [SHOW INDEX\_STATISTICS](../show/show-index-statistics.md)).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| \[ERROR                                                 | ENGINE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| BINARY LOGS                                             | FLUSH BINARY LOGS rotates the current [binary log](../../../../server-management/server-monitoring-logs/binary-log/).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| BINARY LOGS DELETE\_DOMAIN\_ID=(list-of-domains)        | FLUSH BINARY LOGS DELETE\_DOMAIN\_ID can be used to discard obsolete [GTID](../../../../ha-and-performance/standard-replication/gtid.md) domains from the server's [binary log](../../../../server-management/server-monitoring-logs/binary-log/) state. In order for this to be successful, no event group from the listed [GTID](../../../../ha-and-performance/standard-replication/gtid.md) domains can be present in existing [binary log](../../../../server-management/server-monitoring-logs/binary-log/) files. If some still exist, then they must be purged prior to executing this command. If the command completes successfully, then it also rotates the [binary log](../../../../server-management/server-monitoring-logs/binary-log/). |
| MASTER                                                  | Deprecated option, use [RESET MASTER](../reset.md) instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| PRIVILEGES                                              | Reload all privileges from the privilege tables in the mysql database. If the server is started with --skip-grant-table option, this will activate the privilege tables again.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [QUERY CACHE](flush-query-cache.md)                     | Defragment the [query cache](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md) to better utilize its memory. If you want to reset the query cache, you can do it with [RESET QUERY CACHE](../reset.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| QUERY\_RESPONSE\_TIME                                   | See the [QUERY\_RESPONSE\_TIME](../../../plugins/other-plugins/query-response-time-plugin.md) plugin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| QUERY\_RESPONSE\_TIME\_READ                             | See the [QUERY\_RESPONSE\_TIME](../../../plugins/other-plugins/query-response-time-plugin.md) plugin. From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115).                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| QUERY\_RESPONSE\_TIME\_READ\_WRITE                      | See the [QUERY\_RESPONSE\_TIME](../../../plugins/other-plugins/query-response-time-plugin.md) plugin. From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115).                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| QUERY\_RESPONSE\_TIME\_WRITE                            | See the [QUERY\_RESPONSE\_TIME](../../../plugins/other-plugins/query-response-time-plugin.md) plugin. From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115).                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| SLAVE                                                   | Deprecated option, use [RESET REPLICA or RESET SLAVE](../replication-statements/reset-replica.md) instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| SSL                                                     | Used to dynamically reinitialize the server's [TLS](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/) context by reloading the files defined by several [TLS system variables](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md). See [FLUSH SSL](flush.md#flush-ssl) for more information.                                                                                                                                                                                                                                                                                                                                         |
| \[ GLOBAL                                               | SESSION ] STATUS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| TABLE\[S]                                               | Close tables given as options or all open tables if no table list was used. Using without any table list will only close tables not in use, and tables not locked by the FLUSH TABLES connection. If there are no locked tables, FLUSH TABLES will be instant and will not cause any waits, as it no longer waits for tables in use. When a table list is provided, the server will wait for the end of any transactions that are using the tables. Previously, FLUSH TABLES only waited for the statements to complete.                                                                                                                                                                                                                                |
| [TABLE\[S\] ... FOR EXPORT](flush-tables-for-export.md) | For InnoDB tables, flushes table changes to disk to permit binary table copies while the server is running. See [FLUSH TABLES ... FOR EXPORT](flush-tables-for-export.md) for more.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| TABLE\[S] WITH READ LOCK                                | Closes all open tables. New tables are only allowed to be opened with read locks until an [UNLOCK TABLES](../../transactions/transactions-unlock-tables.md) is given.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| TABLE\[S] WITH READ LOCK AND DISABLE CHECKPOINT         | As TABLES WITH READ LOCK but also disable all checkpoint writes by transactional table engines. This is useful when doing a disk snapshot of all tables.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| TABLE\_STATISTICS                                       | Reset table statistics (see [SHOW TABLE\_STATISTICS](../show/show-table-statistics.md)).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| USER\_RESOURCES                                         | Resets all per hour [user resources](../../account-management-sql-statements/grant.md#setting-per-account-resources-limits). This enables clients that have exhausted their resources to connect again.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| USER\_STATISTICS                                        | Reset user statistics (see [SHOW USER\_STATISTICS](../show/show-user-statistics.md)).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| USER\_VARIABLES                                         | Reset user variables (see [User-defined variables](../../../sql-structure/sql-language-structure/user-defined-variables.md)).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

You can also use the [mariadb-admin](../../../../clients-and-utilities/administrative-tools/mariadb-admin.md) client to flush things. Use `mariadb-admin --help` to examine what flush commands it supports.

## `FLUSH RELAY LOGS`

```sql
FLUSH RELAY LOGS 'connection_name'
```

### Compatibility with MySQL

{% tabs %}
{% tab title="Current" %}
The `FOR CHANNEL` keyword was added for MySQL compatibility. This is identical to using the channel\_name directly after the `FLUSH command`. For example, one can now use:

```sql
FLUSH RELAY LOGS FOR CHANNEL 'connection_name';
```
{% endtab %}

{% tab title="< 10.7.0" %}
`FOR CHANNEL` isn't available.
{% endtab %}
{% endtabs %}

## FLUSH STATUS

[Server status variables](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md) can be reset by executing the following:

```sql
FLUSH STATUS
```

This statement requires the [RELOAD](../../account-management-sql-statements/grant.md#reload) privilege.

{% tabs %}
{% tab title="Current" %}
Specify FLUSH GLOBAL or FLUSH SESSION. Flushing of global status variables has been moved to `FLUSH GLOBAL STATUS` which is a synonym for `FLUSH STATUS`.\
You can use `old-mode=OLD_FLUSH_STATUS` to restore the old behavior of the `FLUSH STATUS` statement.
{% endtab %}

{% tab title="< 11.5" %}
The variables flushed are mainly session, but some are global. Not all session (or global) variables are flushed - the decision was made per variable.
{% endtab %}
{% endtabs %}

### Global Status Variables that Support `FLUSH STATUS`

Not all global status variables support being reset by `FLUSH STATUS`. Currently, the following is an incomplete list of status variables are reset by `FLUSH GLOBAL STATUS` in 11.5 or `FLUSH STATUS` in earlier versions:

* [Aborted\_clients](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#aborted_clients)
* [Aborted\_connects](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#aborted_connects)
* [Binlog\_cache\_disk\_use](../../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_cache_disk_use)
* [Binlog\_cache\_use](../../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_cache_use)
* [Binlog\_stmt\_cache\_disk\_use](../../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_stmt_cache_disk_use)
* [Binlog\_stmt\_cache\_use](../../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#binlog_stmt_cache_use)
* [Connection\_errors\_accept](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#connection_errors_accept)
* [Connection\_errors\_internal](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#connection_errors_internal)
* [Connection\_errors\_max\_connections](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#connection_errors_max_connections)
* [Connection\_errors\_peer\_address](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#connection_errors_peer_address)
* [Connection\_errors\_select](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#connection_errors_select)
* [Connection\_errors\_tcpwrap](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#connection_errors_tcpwrap)
* [Created\_tmp\_files](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#created_tmp_files)
* [Delayed\_errors](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#delayed_errors)
* [Delayed\_writes](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#delayed_writes)
* [Feature\_check\_constraint](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#feature_check_constraint)
* [Feature\_delay\_key\_write](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#feature_delay_key_write)
* [Max\_used\_connection\_time](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#max_used_connection_time)
* [Max\_used\_connections](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#max_used_connections)
* [Opened\_plugin\_libraries](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#opened_plugin_libraries)
* [Performance\_schema\_accounts\_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_accounts_lost)
* [Performance\_schema\_cond\_instances\_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_cond_instances_lost)
* [Performance\_schema\_digest\_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_digest_lost)
* [Performance\_schema\_file\_handles\_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_file_handles_lost)
* [Performance\_schema\_file\_instances\_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_file_instances_lost)
* [Performance\_schema\_hosts\_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_hosts_lost)
* [Performance\_schema\_locker\_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_locker_lost)
* [Performance\_schema\_mutex\_instances\_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_mutex_instances_lost)
* [Performance\_schema\_rwlock\_instances\_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_rwlock_instances_lost)
* [Performance\_schema\_session\_connect\_attrs\_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_session_connect_attrs_lost)
* [Performance\_schema\_socket\_instances\_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_socket_instances_lost)
* [Performance\_schema\_stage\_classes\_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_stage_classes_lost)
* [Performance\_schema\_statement\_classes\_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_statement_classes_lost)
* [Performance\_schema\_table\_handles\_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_table_handles_lost)
* [Performance\_schema\_table\_instances\_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_table_instances_lost)
* [Performance\_schema\_thread\_instances\_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_thread_instances_lost)
* [Performance\_schema\_users\_lost](../system-tables/performance-schema/performance-schema-status-variables.md#performance_schema_users_lost)
* [Qcache\_hits](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#qcache_hits)
* [Qcache\_inserts](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#qcache_inserts)
* [Qcache\_lowmem\_prunes](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#qcache_lowmem_prunes)
* [Qcache\_not\_cached](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#qcache_not_cached)
* [Rpl\_semi\_sync\_master\_no\_times](../../../../ha-and-performance/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_no_times)
* [Rpl\_semi\_sync\_master\_no\_tx](../../../../ha-and-performance/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_no_tx)
* [Rpl\_semi\_sync\_master\_timefunc\_failures](../../../../ha-and-performance/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_timefunc_failures)
* [Rpl\_semi\_sync\_master\_wait\_pos\_backtraverse](../../../../ha-and-performance/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_wait_pos_backtraverse)
* [Rpl\_semi\_sync\_master\_yes\_tx](../../../../ha-and-performance/optimization-and-tuning/system-variables/semisynchronous-replication-plugin-status-variables.md#rpl_semi_sync_master_yes_tx)
* [Rpl\_transactions\_multi\_engine](../../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#rpl_transactions_multi_engine)
* [Server\_audit\_writes\_failed](../../../plugins/mariadb-audit-plugin/mariadb-audit-plugin-status-variables.md#server_audit_writes_failed)
* [Slave\_retried\_transactions](../../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#slave_retried_transactions)
* [Slow\_launch\_threads](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#slow_launch_threads)
* [Ssl\_accept\_renegotiates](../../../../ha-and-performance/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_accept_renegotiates)
* [Ssl\_accepts](../../../../ha-and-performance/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_accepts)
* [Ssl\_callback\_cache\_hits](../../../../ha-and-performance/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_callback_cache_hits)
* [Ssl\_client\_connects](../../../../ha-and-performance/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_client_connects)
* [Ssl\_connect\_renegotiates](../../../../ha-and-performance/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_connect_renegotiates)
* [Ssl\_ctx\_verify\_depth](../../../../ha-and-performance/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_ctx_verify_depth)
* [Ssl\_ctx\_verify\_mode](../../../../ha-and-performance/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_ctx_verify_mode)
* [Ssl\_finished\_accepts](../../../../ha-and-performance/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_finished_accepts)
* [Ssl\_finished\_connects](../../../../ha-and-performance/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_finished_connects)
* [Ssl\_session\_cache\_hits](../../../../ha-and-performance/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_session_cache_hits)
* [Ssl\_session\_cache\_misses](../../../../ha-and-performance/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_session_cache_misses)
* [Ssl\_session\_cache\_overflows](../../../../ha-and-performance/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_session_cache_overflows)
* [Ssl\_session\_cache\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_session_cache_size)
* [Ssl\_session\_cache\_timeouts](../../../../ha-and-performance/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_session_cache_timeouts)
* [Ssl\_sessions\_reused](../../../../ha-and-performance/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_sessions_reused)
* [Ssl\_used\_session\_cache\_entries](../../../../ha-and-performance/optimization-and-tuning/system-variables/ssltls-status-variables.md#ssl_used_session_cache_entries)
* [Subquery\_cache\_hit](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#subquery_cache_hit)
* [Subquery\_cache\_miss](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#subquery_cache_miss)
* [Table\_locks\_immediate](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#table_locks_immediate)
* [Table\_locks\_waited](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#table_locks_waited)
* [Tc\_log\_max\_pages\_used](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#tc_log_max_pages_used)
* [Tc\_log\_page\_waits](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#tc_log_page_waits)
* [Transactions\_gtid\_foreign\_engine](../../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#transactions_gtid_foreign_engine)
* [Transactions\_multi\_engine](../../../../ha-and-performance/standard-replication/replication-and-binary-log-status-variables.md#transactions_multi_engine)

## FLUSH TABLES

**MariaDB starting with** [**10.11.12**](https://github.com/mariadb-corporation/docs-server/blob/test/en/mariadb-101112-release-notes/README.md)

{% tabs %}
{% tab title="Current" %}
`FLUSH TABLES` doesn't cause [InnoDB statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md) to be reloaded or recalculated. [RENAME TABLE](../../data-definition/rename-table.md), however, triggers a reload of the statistics.
{% endtab %}

{% tab title="< 11.8.2 / 11.4.6" %}
`FLUSH TABLES` causes [InnoDB statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md) to be reloaded or recalculated.
{% endtab %}

{% tab title="< 10.11.12" %}
`FLUSH TABLES` causes [InnoDB statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics.md) to be reloaded or recalculated.
{% endtab %}
{% endtabs %}

### Purpose of FLUSH TABLES

The purpose of `FLUSH TABLES` is to clean up the open table cache and table definition cache of tables that are not in use. This frees up memory and file descriptors. Normally this is not needed as the caches works on a first-in, first-out basis, but can be useful if the server seems to use too much memory for some reason.

### Purpose of FLUSH TABLES WITH READ LOCK

`FLUSH TABLES WITH READ LOCK` is useful if you want to take a backup of some tables. When `FLUSH TABLES WITH READ LOCK` returns, all write access to tables is blocked and all tables are marked as\
'properly closed' on disk. The tables can still be used for read operations.

### Purpose of FLUSH TABLES table\_list

`FLUSH TABLES` table\_list is useful if you want to copy a table object or files to or from the server. This command puts a lock that stops new users of the table and will wait until everyone has stopped using the table. The table is then removed from the table definition and table cache.

Note that it's up to the user to ensure that no one is accessing the table between `FLUSH TABLES` and the table is copied to or from the server. This can be secured by using [LOCK TABLES](../../transactions/lock-tables.md).

If there are any tables locked by the connection that is using `FLUSH TABLES` all the locked tables will be closed as part of the flush and reopened and relocked before `FLUSH TABLES` returns. This allows one to copy the table after `FLUSH TABLES` returns without having any writes on the table. For now this works with most tables, except InnoDB as InnoDB may do background purges on the table even while it's write locked.

### Purpose of FLUSH TABLES table\_list WITH READ LOCK

`FLUSH TABLES table_list WITH READ LOCK` should work as `FLUSH TABLES WITH READ LOCK`, but only those tables that are listed will be properly closed. However in practice this works exactly like `FLUSH  TABLES WITH READ LOCK` as the `FLUSH` command has anyway to wait for all WRITE operations to end because we are depending on a global read lock for this code. In the future we should consider fixing this to instead use meta data locks.

### Implementation of FLUSH TABLES

* Free memory and file descriptors not in use

### Implementation of FLUSH TABLES WITH READ LOCK

* Lock all tables read only for simple old style backup.
* All background writes are suspended and tables are marked as closed.
* No statement requiring table changes are allowed for any user until `UNLOCK TABLES`.

Instead of using `FLUSH TABLE WITH READ LOCK` one should in most cases instead use[BACKUP STAGE BLOCK\_COMMIT](../backup-commands/backup-stage.md).

### Implementation of FLUSH TABLES table\_list

* Free memory and file descriptors for tables not in use from table list.
* Lock given tables as read only.
* Wait until all translations has ended that uses any of the given tables.
* Wait until all background writes are suspended and tables are marked as closed.

### Implementation of FLUSH TABLES table\_list FOR EXPORT

* Free memory and file descriptors for tables not in use from table list.
* Lock given tables as read.
* Wait until all background writes are suspended and tables are marked as closed.
* Check that all tables supports `FOR EXPORT`.
* No changes to these tables allowed until `UNLOCK TABLES`.

This is basically the same behavior as in older MariaDB versions if you first lock the tables, then do `FLUSH TABLES`. The tables will be copyable until you issue `UNLOCK TABLES`.

## FLUSH SSL

The `FLUSH SSL` command can be used to dynamically reinitialize the server's [TLS](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/) context. This is most useful if you need to replace a certificate that is about to expire without restarting the server.

This operation is performed by reloading the files defined by the following [TLS system variables](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md):

* [ssl\_cert](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md#ssl_cert)
* [ssl\_key](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md#ssl_key)
* [ssl\_ca](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md#ssl_ca)
* [ssl\_capath](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md#ssl_capath)
* [ssl\_crl](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md#ssl_crl)
* [ssl\_crlpath](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md#ssl_crlpath)

These [TLS system variables](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md) are not dynamic, so their values can **not** be changed without restarting the server.

If you want to dynamically reinitialize the server's [TLS](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/) context, then you need to change the certificate and key files at the relevant paths defined by these [TLS system variables](../../../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/ssltls-system-variables.md), without actually changing the values of the variables. See [MDEV-19341](https://jira.mariadb.org/browse/MDEV-19341) for more information.

## Reducing Memory Usage

To flush some of the global caches that take up memory, you could execute the following command:

```sql
FLUSH LOCAL HOSTS,
   QUERY CACHE, 
   TABLE_STATISTICS, 
   INDEX_STATISTICS, 
   USER_STATISTICS;
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
