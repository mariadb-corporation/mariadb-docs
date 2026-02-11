---
description: >-
  Detailed comparison of the three binary logging formats: Statement-based
  (SBR), Row-based (RBR), and Mixed, including their pros, cons, and
  configuration via binlog_format.
---

# Binary Log Formats

## Supported Binary Log Formats

There are three supported formats for [binary log](./) events:

* Statement-Based Logging
* Row-Based Logging
* Mixed Logging

Regardless of the format, [binary log](./) events are always stored in a binary format, rather than in plain text. MariaDB includes the [mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/) utility that can be used to output [binary log](./) events in a human-readable format.

You may want to set the binary log format in the following cases:

* If you execute single statements that update many rows, then statement-based logging will be more efficient than row-based logging for the replica to download.
* If you execute many statements that don't affect any rows, then row-based logging will be more efficient than statement-based logging for the replica to download.
* If you execute statements that take a long time to complete, but they ultimately only insert, update, or delete a few rows in the table, then row-based logging will be more efficient than statement-based logging for the replica to apply.

The default is [mixed logging](binary-log-formats.md#mixed-logging) which is replication-safe and requires less storage space than [row logging](binary-log-formats.md#row-based-logging).

The storage engine API also allows storage engines to set or limit the logging format, which helps reduce errors with replicating between primaries and replicas with different storage engines.

## Statement-Based Logging

When statement-based logging is enabled, statements are logged to the [binary log](./) exactly as they were executed. Temporary tables created on the primary will also be created on the replica.\
This mode is only recommended where one needs to keep the binary log as small as possible, the primary and replica have identical data (including using the same storage engines for all tables), and all functions being used are deterministic (repeatable with the same arguments).\
Statements and tables using timestamps or auto\_increment are safe to use with statement-based logging.

This mode can be enabled by setting the [binlog\_format](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format) system variable to `STATEMENT`.

In certain cases when it would be impossible to execute the statement on the replica, the server will switch to\
row-based logging for the statement. Some cases of this are:

* When replication has been changed from row-based to statement-based and a statement uses data from a temporary table created during row-based mode. In this case, the temporary tables are not stored on the replica, so row logging is the only alternative.
* [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/) of a table using a storage engine that stores data remotely, such as the [S3 storage engine](../../../server-usage/storage-engines/s3-storage-engine/), to another storage engine.
* One is using [SEQUENCEs](../../../reference/sql-structure/sequences/) in the statement or the [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) definition.

In certain cases, a statement may not be deterministic, and therefore not safe for [replication](../../../ha-and-performance/standard-replication/). If MariaDB determines that an unsafe statement has been executed, it issues a warning like this:

{% code overflow="wrap" %}
```
[Warning] Unsafe statement written to the binary log using statement format since BINLOG_FORMAT = STATEMENT. The statement is unsafe because it uses a LIMIT clause. This is unsafe because the set of rows included cannot be predicted.
```
{% endcode %}

See [Unsafe Statements for Statement-based Replication](../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md) for more information.

If you need to execute non-deterministic statements, then it is safer to use mixed logging or row-based.

### Caveats of Statement-Based Logging

Some tables, like temporary tables created in row mode, do not support statement-based logging (as the data is not in the binary log). Any statement that uses a table that does not support statement logging will use row based logging. This is to ensure that the data on master and the replica are consistent.

## Mixed Logging

Mixed logging is the default binary log format.

When mixed logging is enabled, the server uses a combination of statement-based logging and row-based logging. Statement-based logging is used where possible, but when the server determines a statement may not be safe for statement-based logging, it will use row-based logging instead. See [Unsafe Statements for Statement-based Replication: Unsafe Statements](../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md#unsafe-statements) for a list of unsafe statements.

During one transaction, some statements may be logged with row logging while others are logged with statement-based logging.

This mode can be enabled by setting the [binlog\_format](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format) system variable to `MIXED`.

## Row-Based Logging

When row-based logging is enabled, DML statements are **not** logged to the [binary log](./). Instead, each insert, update, or delete performed by the statement for each row is logged to the [binary log](./) separately. DDL statements are still logged to the [binary log](./).

Row-based logging uses more storage than the other log formats but is the safest to use. In practice [mixed logging](binary-log-formats.md#mixed-logging) should be as safe.

If you want to be able to see the original query that was logged, you can enable [annotated rows events](../../../reference/clientserver-protocol/replication-protocol/annotate_rows_event.md), that is shown with [mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/), with [--binlog-annotate-row-events](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_annotate_row_events). This option is on by default.

This mode can be enabled by setting the [binlog\_format](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format) system variable to `ROW`.

{% hint style="warning" %}
When the primary server (master) writes a transaction to the binary log that exceeds the  [`max_allowed_packet`](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_allowed_packet) size, replication breaks, issuing an error like this:

`Last_IO_Error: Got fatal error 1236 from master when reading data from binary log: 'log event entry exceeded max_allowed_packet; Increase max_allowed_packet on master; the first event 'mariadb-bin.109824' at 4, the last event read from 'mariadb-bin.109825' at 15113554, the last byte read from 'mariadb-bin.109825' at 15113573.'`

When that happens, the only way to recover is by manually extracting the transaction from the primary server's binary log, and manually applying it to the replica server.

**This issue has been addressed in MariaDB 12.3**, and is described in the following.
{% endhint %}

### Splitting Large Row-Format Replication Events

{% hint style="info" %}
This functionality is available from MariaDB 12.3.
{% endhint %}

The maximum value of the  [`max_allowed_packet`](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_allowed_packet) system variable is 1GB. It can be set to smaller values, but not values bigger than that. For row-based replication, this means that a `ROW`-format replication event bigger than the configured variable value cannot be written to the primary server's binary log. As a consequence, replication breaks. (See the warning above.)

To overcome this limitation (and breakage), a variable named [`binlog_row_event_fragment_threshold`](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_row_event_fragment_threshold) can be configured. The value should obviously be smaller than the value of `max_allowed_packet`.

Once configured, the primary (master) server behaves differently when encountering large `ROW`-format replication events: When writing a transaction to the binary log that exceeds `binlog_row_event_fragment_threshold`, it splits up the transaction event into smaller chunks. (Those chunks have a type of `Partial_rows_log_event`.) None of those chunks exceed the value of the variable, and so replica servers can read binary log entries without issues.

### Caveats of Row-Based Logging

When using row-based logging, some statements work different on the master.

* `DELETE FROM`` `_`table_name`_
  * In row-based mode, the table always uses deletion row-by-row, which can take a long time if the table is big. It can also use a lot of space in the binary log.
  * In `STATEMENT` or `MIXED` mode, [truncate](../../../reference/sql-functions/numeric-functions/truncate.md) is used, if possible (no triggers, no foreign keys etc). This is much faster and uses less space in the binary log.

## Compression of the Binary Log

[Compression of the binary log](compressing-events-to-reduce-size-of-the-binary-log.md) can be used with any of the binary log formats, but the best results come from using mixed or row-based logging. You can enable compression by using the [`--log_bin_compress`](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin_compress) startup option.

## Configuring the Binary Log Format

The format for [binary log](./) events can be configured by setting the [binlog\_format](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format) system variable. If you have the [SUPER](../../../reference/sql-statements/account-management-sql-statements/grant.md#global-privileges) privilege, then you can change it dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:

```sql
SET GLOBAL binlog_format='ROW';
```

You can also change it dynamically for just a specific session with [SET SESSION](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session). For example:

```sql
SET SESSION binlog_format='ROW';
```

It can also be set in a server [option group](../../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server. For example:

```ini
[mariadb]
...
binlog_format=ROW
```

{% hint style="warning" %}
Be careful when changing the binary log format when using [replication](../../../ha-and-performance/standard-replication/). When you change the binary log format on a server, it only changes the format for that server. Changing the binary log format on a primary has no effect on the replica's binary log format. This can cause replication to give inconsistent results or to fail.
{% endhint %}

Be careful changing the binary log format dynamically when the server is a replica and [parallel replication](../../../ha-and-performance/standard-replication/parallel-replication.md) is enabled. If you change the global value dynamically, then that does not also affect the session values of any currently running threads. This can cause problems with [parallel replication](../../../ha-and-performance/standard-replication/parallel-replication.md), because the [worker threads](../../../ha-and-performance/standard-replication/replication-threads.md#worker-threads) will remain running even after [STOP SLAVE](../../../reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica.md) is executed. This can be worked around by resetting the [slave\_parallel\_threads](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_parallel_threads) system variable. For example:

```sql
STOP SLAVE;
SET GLOBAL slave_parallel_threads=0;
SET GLOBAL binlog_format='ROW';
SET GLOBAL slave_parallel_threads=4;
START SLAVE
```

For considerations when replicating temporary tables, see [Replicating temporary tables](../../../reference/sql-statements/data-definition/create/create-table.md#replicating-temporary-tables).

## Effect of the Binary Log Format on Replicas

A replica will apply any events it gets from the primary, regardless of the binary log format. The [binlog\_format](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format) system variable only applies to normal (not replicated) updates.

If you are running MySQL or an older MariaDB than 10.0.22, you should be aware of that if you are running the replica in `binlog_format=STATEMENT` mode, the replica will stop if the primary is used with `binlog_format` set to anything else than `STATEMENT`.

The binary log format is upwards-compatible. This means replication should always work if the replica is the same or a newer version of MariaDB than the primary.

## The mysql Database

Statements that affect the `mysql` database can be logged in a different way to that expected.

If the mysql database is edited directly, logging is performed as expected according to the [binlog\_format](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format). Statements that directly edit the mysql database include [INSERT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md), [UPDATE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md), [DELETE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md), [REPLACE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/replace.md), [DO](../../../reference/sql-statements/stored-routine-statements/do.md), [LOAD DATA INFILE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md), [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md), and [TRUNCATE TABLE](../../../reference/sql-statements/table-statements/truncate-table.md).

If the `mysql` database is edited indirectly, statement logging is used regardless of [binlog\_format](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format) setting. Statements editing the `mysql` database indirectly include [GRANT](../../../reference/sql-statements/account-management-sql-statements/grant.md), [REVOKE](../../../reference/sql-statements/account-management-sql-statements/revoke.md), [SET PASSWORD](../../../reference/sql-statements/account-management-sql-statements/set-password.md), [RENAME USER](../../../reference/sql-statements/account-management-sql-statements/rename-user.md), [ALTER](../../../reference/sql-statements/data-definition/alter/), [DROP](../../../reference/sql-statements/data-definition/drop/) and [CREATE](../../../reference/sql-statements/data-definition/create/) (except for the situation described below).

`CREATE TABLE ... SELECT` can use a combination of logging formats. The [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) portion of the statement is logged using statement-based logging, while the [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) portion is logged according to the value of `binlog_format`.

### Metadata Field Definitions (mariadb-binlog Output)

When using the mariadb-binlog utility to view the binary log, events are presented with a standardized header and specific metadata tags. Understanding these is essential for building replication monitors or audit tools.

**Event Header Template:** `# at {Position}` `#YYMMDD HH:MM:SS server id {ID} end_log_pos {Pos} CRC32 {Value} {Event_Type}: ...`

| Field             | Component               | Description                                                                                                               |
| ----------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Timestamp**     | `YYMMDD HH:MM:SS`       | The time the event was recorded on the originating server.                                                                |
| **Server ID**     | `Unsigned Integer`      | The unique ID of the server where the event originated. This matches the `server_id` used in General and Slow Query logs. |
| **end\_log\_pos** | `Unsigned Integer`      | The byte offset (position) of the _next_ event in the log file.                                                           |
| **Thread ID**     | `at {ID}`               | (Positional) The connection identifier that executed the statement. Matches `Thread ID` in other logs.                    |
| **GTID**          | `Domain-ServerID-SeqNo` | Global Transaction ID (e.g., `0-1-100`). Uniquely identifies a transaction across a replication topology.                 |
| **Xid**           | `Unsigned Integer`      | The internal transaction ID used for 2-Phase Commit (2PC) between storage engines (e.g., InnoDB) and the binary log.      |
| **cid**           | `Unsigned Integer`      | Group Commit ID. Transactions with the same `cid` were flushed to disk in the same group.                                 |

#### Impact of Configuration on Log Structure

The structure and verbosity of `ROW` events are significantly altered by several system variables:

* **binlog\_row\_image**:
  * `FULL`: Logs all columns for both the "before" and "after" images.
  * `MINIMAL`: Logs only the changed columns in the after image and identifying columns (PK/Unique) in the before image. Parsers must handle variable column counts per event.
* **binlog\_row\_metadata**:
  * `MINIMAL`: Only logs data.
  * `FULL`: Includes column names and data types in the log. This is essential for parsers to decode the log without querying the live database schema.
* **encrypt\_binlog**:
  * If `ON`, events are encrypted on disk. `mariadb-binlog` will only display plain-text metadata if it has access to the encryption keys.

## See Also

* [Setting up replication](../../../ha-and-performance/standard-replication/setting-up-replication.md)
* [Compressing the binary log](compressing-events-to-reduce-size-of-the-binary-log.md)
* [Replicating temporary tables](../../../reference/sql-statements/data-definition/create/create-table.md#replicating-temporary-tables)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
