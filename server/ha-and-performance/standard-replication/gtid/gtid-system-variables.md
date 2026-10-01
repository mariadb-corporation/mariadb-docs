---
description: >-
  Reference for the GTID system variables, including gtid_slave_pos, gtid_binlog_pos, gtid_current_pos, gtid_strict_mode, and gtid_domain_id.
---

# GTID System Variables

These system variables control how the server assigns, records, and enforces global transaction IDs. The replication-wide variables that also affect GTID, such as `binlog_format`, are described in [Replication and Binary Log System Variables](../replication-and-binary-log-system-variables.md).

## [binlog\_gtid\_index](../replication-and-binary-log-system-variables.md#binlog_gtid_index)

Enables/disables [binlog indexing](README.md#binlog-indexing).

## [binlog\_gtid\_index\_page\_size](../replication-and-binary-log-system-variables.md#binlog_gtid_index_page_size)

Adjusts the size of the pages.

## [binlog\_gtid\_index\_span\_min](../replication-and-binary-log-system-variables.md#binlog_gtid_index_span_min)

Adjusts the sparseness of the index.

## `gtid_slave_pos`

This system variable contains the GTID of the last transaction applied to the database by the server's [replica threads](../replication-threads.md#threads-on-the-replica) for each replication domain. This system variable's value is automatically updated whenever a [replica thread](../replication-threads.md#threads-on-the-replica) applies an event group. This system variable's value can also be manually changed by users, so that the user can change the GTID position of the [replica threads](../replication-threads.md#threads-on-the-replica).

When using [multi-source replication](../multi-source-replication.md), the same GTID position is shared by all replica connections. In this case, different primaries should use different replication domains by configuring different [gtid\_domain\_id](#gtid_domain_id) values. If one primary was using a [gtid\_domain\_id](#gtid_domain_id) value of `1`, and if another primary was using a [gtid\_domain\_id](#gtid_domain_id) value of `2`, then any replicas replicating from both primaries would have GTIDs with both [gtid\_domain\_id](#gtid_domain_id) values in `gtid_slave_pos`.

This system variable's value can be manually changed by executing [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session), but all replica threads to be stopped with [STOP REPLICA](../../../reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica.md) first. For example:

```sql
STOP ALL SLAVES;
SET GLOBAL gtid_slave_pos = "1-10-100,2-20-500";
START ALL SLAVES;
```

This system variable's value can be reset by manually changing its value to the empty string. For example:

```sql
SET GLOBAL gtid_slave_pos = '';
```

The GTID position defined by `gtid_slave_pos` can be used as a replica's starting replication position by setting [MASTER\_USE\_GTID=slave\_pos](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_use_gtid) when the replica is configured with the [CHANGE MASTER TO](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) statement. As an alternative, the [gtid\_current\_pos](#gtid_current_pos) system variable can also be used as a replica's starting replication position.

If a user sets the value of the `gtid_slave_pos` system variable, and [gtid\_binlog\_pos](#gtid_binlog_pos) contains later GTIDs for certain replication domains, then [gtid\_current\_pos](#gtid_current_pos) will contain the GTIDs from [gtid\_binlog\_pos](#gtid_binlog_pos) for those replication domains. To protect users in this scenario, if a user sets the `gtid_slave_pos` system variable to a GTID position that is behind the GTID position in [gtid\_binlog\_pos](#gtid_binlog_pos), then the server will give the user a warning.

This can help protect the user when the replica is configured to use [gtid\_current\_pos](#gtid_current_pos) as its replication position. This can also help protect the user when a server has been rolled back to restart replication from an earlier point in time, but the user has forgotten to reset [gtid\_binlog\_pos](#gtid_binlog_pos) with [RESET MASTER](../../../reference/sql-statements/administrative-sql-statements/replication-statements/reset-master.md).

The [mysql.gtid\_slave\_pos](../../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) system table is used to store the contents of global.gtid\_slave\_pos and preserve it over restarts.

* Command line: None
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default: Null

## `gtid_binlog_pos`

This variable is the GTID of the last event group written to the binary log, for each replication domain.

Note that when the binlog is empty (such as on a fresh install with [--skip-test-db](../../../clients-and-utilities/deployment-tools/mariadb-install-db.md#not-creating-the-test-database-and-anonymous-user), or after [RESET MASTER](../../../reference/sql-statements/administrative-sql-statements/replication-statements/reset-master.md)), there are no event groups written in any replication domain, so in this case the value of `gtid_binlog_pos` will be the empty string.

The value is read-only, but it is updated whenever a DML or DDL statement is written to the binary log. The value can be reset by executing [RESET MASTER](../../../reference/sql-statements/administrative-sql-statements/replication-statements/reset-master.md), which will also delete all binary logs. However, note that [RESET MASTER](../../../reference/sql-statements/administrative-sql-statements/replication-statements/reset-master.md) does not also reset [gtid\_slave\_pos](#gtid_slave_pos). Since [gtid\_current\_pos](#gtid_current_pos) is the union of [gtid\_slave\_pos](#gtid_slave_pos) and `gtid_binlog_pos`, that means that new GTIDs added to `gtid_binlog_pos` can lag behind those in [gtid\_current\_pos](#gtid_current_pos) if [gtid\_slave\_pos](#gtid_slave_pos) contains GTIDs in the same domain with higher sequence numbers. If you want to reset [gtid\_current\_pos](#gtid_current_pos) for a specific GTID domain in cases like this, then you will also have to change [gtid\_slave\_pos](#gtid_slave_pos) in addition to executing [RESET MASTER](../../../reference/sql-statements/administrative-sql-statements/replication-statements/reset-master.md). See [gtid\_slave\_pos](#gtid_slave_pos) for notes on how to change its value.

* Command line: None
* Scope: Global
* Dynamic: Read-only
* Data Type: `string`
* Default: Null

## `gtid_binlog_state`

This variable holds the internal state of the binlog. The state consists of the last GTID ever logged to the binary log for every combination of `domain_id` and `server_id`. This information is used by the primary to determine whether a given GTID has been logged to the binlog in the past, even if it has later been deleted due to binlog purge. For each domain\_id, the last entry in `@@gtid_binlog_state` is the last GTID logged into binlog, for instance, this is the value that appears in `@@gtid_binlog_pos`.

Normally this internal state is not needed by users, as `@@gtid_binlog_pos` is more useful in most cases. The main usage of `@@gtid_binlog_state` is to restore the state of the binlog after `RESET MASTER` (or equivalently if the binlog files are lost). If the value of `@@gtid_binlog_state` is saved before `RESET MASTER` and restored afterwards, the primary will retain information about past history, same as if `PURGE BINARY LOGS` had been used (of course the actual events in the binary logs are still deleted).

{% hint style="info" %}
To set the value of `@@gtid_binlog_state`, the binary log must be empty, that is, it must not contain any GTID events and the previous value of `@@gtid_binlog_state` must be the empty string. If not, then `RESET MASTER` must be used first to erase the binary log first.
{% endhint %}

The value of `@@gtid_binlog_state` is preserved by the server across restarts by writing a file `MASTER-BIN.state`, where `MASTER-BIN` is the base name of the binlog set with the `--log-bin` option. This file is written at server shutdown, and re-read at next server start. (In case of a server crash, the data in the `MASTER-BIN.state` is not correct, and the server instead recovers the correct value during binlog crash recovery by scanning the binlog files and recording each GTID found). When using the InnoDB-based binary log (`--binlog-storage-engine=innodb`), the value of `@@gtid_binlog_state` is preserved internally by the InnoDB binlog implementation, and the file `MASTER-BIN.state` is not used.

For completeness, note that setting @@gtid\_binlog\_state internally executes a `RESET MASTER`. This is normally not noticeable as it can only be changed when the binlog is empty of GTID events.

* Command line: None
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default: Null

## `gtid_current_pos`

This system variable contains the GTID of the last transaction applied to the database for each replication domain.

The value of this system variable is constructed from the values of the [gtid\_binlog\_pos](#gtid_binlog_pos) and [gtid\_slave\_pos](#gtid_slave_pos) system variables. It gets GTIDs of transactions executed locally from the value of the [gtid\_binlog\_pos](#gtid_binlog_pos) system variable. It gets GTIDs of replicated transactions from the value of the [gtid\_slave\_pos](#gtid_slave_pos) system variable.

For each replication domain, if the [server\_id](../replication-and-binary-log-system-variables.md#server_id) of the corresponding GTID in [gtid\_binlog\_pos](#gtid_binlog_pos) is equal to the servers own [server\_id](../replication-and-binary-log-system-variables.md#server_id),_and_ the sequence number is higher than the corresponding GTID in [gtid\_slave\_pos](#gtid_slave_pos), then the GTID from [gtid\_binlog\_pos](#gtid_binlog_pos) will be used. Otherwise the GTID from [gtid\_slave\_pos](#gtid_slave_pos) will be used for that domain.

GTIDs from [gtid\_binlog\_pos](#gtid_binlog_pos) in which the [server\_id](../replication-and-binary-log-system-variables.md#server_id) of the GTID is **not** equal to the server's own [server\_id](../replication-and-binary-log-system-variables.md#server_id) are effectively ignored. If [gtid\_binlog\_pos](#gtid_binlog_pos) contains a GTID for a given replication domain, but the [server\_id](../replication-and-binary-log-system-variables.md#server_id) of the GTID is **not** equal to the server's own [server\_id](../replication-and-binary-log-system-variables.md#server_id), and [gtid\_slave\_pos](#gtid_slave_pos) does **not** contain a GTID for that given replication domain, then `gtid_current_pos` will **not** contain any GTID for that replication domain.

Thus, `gtid_current_pos` contains the most recent GTID executed on the server, whether this was done as a primary or as a replica.

The GTID position defined by `gtid_current_pos` can be used as a replica's starting replication position by setting [MASTER\_USE\_GTID=current\_pos](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_use_gtid) when the replica is configured with the [CHANGE MASTER TO](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) statement. As an alternative, the [gtid\_slave\_pos](#gtid_slave_pos) system variable can also be used as a replica's starting replication position.

The value of `gtid_current_pos` is read-only, but it is updated whenever a transaction is written to the binary log and/or replicated by a replica thread, and that transaction's GTID is considered _newer_ than the current GTID for that domain. See above for the rules on how to determine if a GTID would be considered _newer_.

If you need to reset the value, see the notes on resetting [gtid\_slave\_pos](#gtid_slave_pos) and [gtid\_binlog\_pos](#gtid_binlog_pos), since `gtid_current_pos` is formed from the values of those variables.

* Command line: None
* Scope: Global
* Dynamic: Read-only
* Data Type: `string`
* Default: Null

## `gtid_strict_mode`

The GTID strict mode is an optional setting that can be used to help DBAs enforce a strict discipline about keeping binlogs identical across multiple servers replicating using global transaction ID.

When GTID strict mode is enabled, some additional errors are enabled for situations that could otherwise cause differences between binlogs on different servers in a replication hierarchy:

1. If a replica server tries to replicate a GTID with a sequence number lower than what is already in the binlog for that replication domain, the SQL thread stops with an error (this indicates an extra transaction in the replica binlog not present on the primary).
2. Similarly, an attempt to manually binlog a GTID with a lower sequence number (by setting `@@SESSION.gtid_seq_no`) is rejected with an error.
3. If the replica tries to connect starting at a GTID that is missing in the primary's binlog, this is an error in GTID strict mode even if a GTID exists with a higher sequence number (this indicates a GTID on the replica missing on the primary). Note that this error is controlled by the setting of GTID strict mode on the connecting replica server.

GTID strict mode is off by default; this is needed to preserve backwards compatibility with existing replication setups (older versions of the server did not enforce any strict mode for binlog order). Global transaction ID is designed to work correctly even when strict mode is not enabled. However, with strict mode enforced, the semantics is simpler and thus easier to understand, because binlog order is always identical across servers and sequence numbers are always strictly increasing within each replication domain. This can also make automated scripting of large replication setups easier to implement correctly.

When GTID strict mode is enabled, the replica will stop with an error when a problem is encountered. This allows the DBA to become aware of the problem and take corrective actions to avoid similar issues in the future. One way to recover from such an error is to temporarily disable GTID strict mode on the offending replica, to be able to replicate past the problem point (perhaps using `START SLAVE UNTIL master_gtid_pos=XXX`).

* Command line: `--gtid-strict-mode[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default: `Off`

## `gtid_domain_id`

* Description: This variable is used to decide which replication domain new GTIDs are logged in for a primary server. See [Use with multi-source replication and other multi-primary setups](gtid-multi-primary.md) for details. This variable can also be set on the session level by a user with the SUPER privilege. This is used by [mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/) to preserve the domain ID of GTID events.
* Command line: `--gtid-domain-id=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric (32-bit unsigned integer)`
* Default Value: `0`
* Range: `0` to `4294967295`

## `last_gtid`

* Description: Holds the GTID that was assigned to the last transaction, or statement that was logged to the [binary log](../../../server-management/server-monitoring-logs/binary-log/). If the binary log is disabled, or if no transaction or statement was executed in the session yet, then the value is an empty string.
* Scope: Session
* Dynamic: Read-only
* Data Type: `string`

## `server_id`

* Description: Server\_id can be set on the session level to change which server\_id value is logged in binlog events (both GTID and other events). This is used by mariadb-binlog to preserve the server ID of GTID events.
* Scope: Global, Session
* Dynamic: Yes
* Data Type: numeric (32-bit unsigned integer)

## `gtid_seq_no`

* Description: The `gtid_seq_no` session variable can be set to manually override the sequence number for the following transaction's Global Transaction ID (GTID).\
  By default, the server internally maintains an increasing counter where each committing transaction uses the next value from this counter as its sequence number when writing its GTID event to the binary log (along with `@@gtid_domain_id` and `@@server_id`).\
  When `gtid_seq_no` is specified, it overrides this counter for the next committing transaction in the respective session; this value is then used as the sequence number when writing the GTID event to the binary log. Crucially, the server’s internal counter also resets to this specified value, ensuring that subsequent transactions increment from this new value when generating their sequence numbers.\
  This variable is typically used internally and by tools like `mariadb-binlog` to maintain GTID consistency when applying events across different servers (e.g., from a primary to a replica).
* Command line: None
* Scope: Session
* Dynamic: Yes
* Data Type: `numeric (64-bit unsigned integer)`
* Default: Null

## `gtid_ignore_duplicates`

* Description: When set, different primary connections in multi-source replication are allowed to receive and process event groups with the same GTID (when using GTID mode). Only one will be applied, any others will be ignored. Within a given replication domain, just the sequence number will be used to decide whether a given GTID has been already applied; this means it is the responsibility of the user to ensure that GTID sequence numbers are strictly increasing. With `gtid_ignore_duplicates=OFF`, a duplicate event based on domain id and sequence number, will be executed. When `--gtid-ignore-duplicate` is set, a replica is allowed to connect at a GTID position that does not exist on the primary. The replica starts receiving events once a GTID with a higher sequence number is available on the primary (within that domain). This can be used to allow a replica to connect at a GTID position that was filtered on the primary, eg. using [`--replicate-ignore-table`](../replication-and-binary-log-system-variables.md#replicate_ignore_table). See also [Multiple Redundant Replication Paths](gtid-multi-primary.md#multiple-redundant-replication-paths).
* Command line: `--gtid-ignore-duplicates=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default: `OFF`

## `gtid_pos_auto_engines`

This variable is used to enable multiple versions of the [mysql.gtid\_slave\_pos](../../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) table, one for each transactional storage engine in use. This can improve replication performance if a server is using multiple different storage engines in different transactions.

The value is a list of engine names, separated by commas (`,`). Replication of transactions using these engines will automatically create new versions of the `mysql.gtid_slave_pos` table in the same engine and use that for future transactions (table creation takes place in a background thread). This avoids introducing a cross-engine transaction to update the GTID position. Only transactional storage engines are supported for `gtid_pos_auto_engines` (such as [InnoDB](../../../server-usage/storage-engines/innodb/README.md) or [MyRocks](../../../server-usage/storage-engines/myrocks/README.md)).

The variable can be changed dynamically, but replica SQL threads should be stopped when changing it, and it will take effect when the replicas are running again.

When setting the variable on the command line or in a configuration file, it is possible to specify engines that are not enabled in the server. The server will then still start if, for example, that engine is no longer used. Attempting to set a non-enabled engine dynamically in a running server (with `SET GLOBAL gtid_pos_auto_engines`) still results in an error.

Removing a storage engine from the variable will have no effect once the new tables have been created – as long as these tables are detected, they are used.

* Command line: `--gtid-pos-auto-engines=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string` (comma-separated list of engine names)
* Default: empty

## `gtid_cleanup_batch_size`

* Description: Normally does not need tuning. How many old rows must accumulate in the [mysql.gtid\_slave\_pos table](../../../reference/system-tables/the-mysql-database-tables/mysqlgtid_slave_pos-table.md) before a background job is run to delete them. Can be increased to reduce number of commits if using many different engines with [gtid\_pos\_auto\_engines](#gtid_pos_auto_engines), or to reduce CPU overhead if using a huge number of different [gtid\_domain\_ids](#gtid_domain_id). Can be decreased to reduce number of old rows in the table.
* Command line: `--gtid-cleanup-batch-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default: `64`
* Range: `0` to `2147483647`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
