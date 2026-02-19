---
description: >-
  MariaDB 12.3 introduces a new binary log implementation that stores binlog
  events directly into InnoDB-managed tablespaces instead of separate flat files
  on disk.
---

# InnoDB-Based Binary Log

{% hint style="info" %}
This feature is available from MariaDB 12.3.
{% endhint %}

## Description

Traditionally, MariaDB treated the [binary log](../../server-management/server-monitoring-logs/binary-log/) (binlog) and the [InnoDB storage engine](../../server-usage/storage-engines/innodb/) as separate components, requiring a complex two-phase commit (2PC) protocol to keep them synchronized. With this new binlog implementation, binlog transactions are stored within InnoDB-managed pages. This change eliminates the need for an expensive 2PC between the binlog and InnoDB, allowing significant performance improvements and simplified crash recovery behavior.

## Enabling the InnoDB Binlog

```bash
--binlog-storage-engine
```

## Benefits

The InnoDB-based binlog offers two key performance advantages:

1. **Crash-safe recovery without sync operations**: The binlog seamlessly integrates with InnoDB's crash recovery mechanism. This enables you to set `--innodb-flush-log-at-trx-commit=0` or `--innodb-flush-log-at-trx-commit=2` for better performance while maintaining crash safety and consistency.
2. **Efficient commits with reduced** `fsync` **operations**: When using the `--innodb-flush-log-at-trx-commit=1` setting, the system performs only a single coordinated `fsync` per commit, instead of the multiple syncs required by the traditional 2PC.
3. The `sync_binlog` option is no longer required as the binlog files are now crash-safe.

## Comparison: Traditional vs. New Binlog

| Feature         | Traditional Binlog                                         | New InnoDB-Based Binlog               |
| --------------- | ---------------------------------------------------------- | ------------------------------------- |
| File Extension  | `.idx`, `.index` files                                     | `.ibb`                                |
| Crash Safety    | Needs `sync_binlog=1`                                      | Native / Inherited from InnoDB engine |
| Commit Protocol | Two-Phase Commit (Slow)                                    | Integrated (Fast)                     |
| Positioning     | Filename/Offset or [Global Transaction ID](gtid.md) (GTID) | GTID Only                             |
| File Allocation | Incremental                                                | Pre-allocated (`max_binlog_size`)     |

## When to Use InnoDB-Based Binlogs

Use **InnoDB-based binlogs** when:

* The system requires high transactional throughput with strict durability guarantees.
* Replication topologies are already using GTIDs.
* You are running MariaDB 12.3 or later with GTID replication enabled.

Stay with **traditional binlogs** when:

* The system requires Galera Cluster support.
* Applications depend on filename/offset-based replication positions.
* The environment uses third-party tools that read binlog files directly.

## Enabling the InnoDB Binary Log

### Configuration

To enable the InnoDB-based binlog, add these options to your MariaDB configuration file:

```ini
[mariadb]
log_bin
binlog_storage_engine=innodb
```

* The `log_bin` option must be specified without any value.
* The new binlog format is mutually exclusive with the traditional file-based binlog. Old binlog files are ignored after switching to the new format.

For additional configuration options, see [Replication and Binary Log System Variables](replication-and-binary-log-system-variables.md).

### Optional Configuration

#### Custom Binlog Directory

The directory for binary log files can be configured with:

```ini
[mariadb]
binlog_directory=/path/to/binlog
```

If not specified, the data directory is used by default.

#### Binary Log Files

Binary log files are stored as InnoDB tablespace files and use the `.ibb` extension. Binlog files are stored with naming pattern:

```
binlog-000000.ibb
binlog-000001.ibb
```

**Characteristics**

* The binlog files are pre-allocated.
* The file size is managed by `max_binlog_size` (by default 1GB).
* Files are page-based (16KB pages) with CRC32 checksum.
* There are no binlog index files (`.index`)_,_ GTID index files (`.idx`)_,_ or GTID state files (`.state`)_._

#### GTID Handling

The new binlog implementation requires GTID-based replication. The GTID state is written to the binary log on a regular basis. The following regulates the interval:

```ini
[mariadb]
innodb-binlog-state-interval
```

The binary log from the last GTID state record is scanned when a replica connects in order to find the determined location.

For additional configuration options, see [Replication and Binary Log System Variables](replication-and-binary-log-system-variables.md).

#### Replication

Using the new binlog, [replication](./) configuration from the master can be performed as usual. For that:

* Replicas must use GTID to connect to the master (default).
* Replicas should run MariaDB 12.3 or later when replicating from master.
* The master and slave can independently use either the traditional or new binlog format.

### Viewing Binlog Events

Binary log events can be verified from within the server using SQL statements, or from outside the server using the `mariadb-binlog` client utility.

#### Within the Server

To inspect binary log events directly from a running server instance, use SQL statements:

```sql
-- View all binlog events
SHOW BINLOG EVENTS;

-- View events from a specific file
SHOW BINLOG EVENTS IN 'binlog-000001.ibb';

-- View events from a GTID position
SHOW BINLOG EVENTS FROM GTID_POS('0-1-1024');
```

Note that event offsets are generally reported as zero; GTID positions can be used instead for navigation.

#### Using the `mariadb-binlog` Utility

The `mariadb-binlog` utility allows inspection of binary log files either locally or remotely:

```bash
# Read binary log from a remote server
mariadb-binlog --read-from-remote-server \

# Read a local binary log file
mariadb-binlog /path/to/binlog-000000.ibb

# Read multiple binary log files
mariadb-binlog /path/to/binlog-000000.ibb \
               /path/to/binlog-000001.ibb \
               /path/to/binlog-000002.ibb
```

When viewing events across multiple binlog files, all binlog files should be passed to the `mariadb-binlog` program at once in correct order; this ensures that events that cross file boundaries are included in the output exactly once.

## Flushing and Rotating Binary Log Files

To regulate the file size and disk use, binary log files can be manually rotated or purged:

```sql
-- Flush the current binary log file and create a new one
FLUSH BINARY LOGS;

-- Flush the current binary log and remove a specific GTID domain
FLUSH BINARY LOGS DELETE_DOMAIN_ID=N;

-- Remove binary log files up to a specific file
PURGE BINARY LOGS TO 'binlog-000001.ibb';
```

* Pads current file to next page boundary.
* `FLUSH BINARY LOGS` creates new `.ibb` files and terminates the existing one.
* `PURGE BINARY LOGS TO` removes older files that are no longer required.

### Automatic Purging

Binary log files can be automatically removed according to disk consumption or age.

```sql
-- Retain binary logs for 7 days (in seconds)
SET GLOBAL binlog_expire_log_seconds = 604800;

-- Retain binary logs for 14 days 
SET GLOBAL binlog_expire_log_days = 14;

-- Limit total binary log disk usage to 100 GB
SET GLOBAL max_binlog_total_size = 107374182400;

-- Purge even with slave
slave_connections_needed_for_purge=0
```

Note that binary log files are only deleted when:

* Limits on time and size are exceeded.
* Files are not required for crash recovery or by active replicas.

## Backup using mariadb-backup

### Default Behavior

By default, binlog files are included in backups, resolving a long-standing issue with the traditional binlog.

Key features:

* Consistent transactional backup for binlog files, similar to other [InnoDB](../../server-usage/storage-engines/innodb/) data.
* Backups are non-blocking, meaning the server continues running normally. By default, only `RESET MASTER`**,** `PURGE BINARY LOGS`, and `FLUSH BINARY LOGS` are blocked during backup. This blocking can be disabled with the `--no-lock` option.
* Restored backups can serve as replicas for replication.

### Setting Up Replica from Backup

```bash
# Default backup includes binlog files
mariadb-backup --backup --target-dir=/backup/path

# Exclude binlog files (save space)
mariadb-backup --backup --target-dir=/backup/path --skip-binlog

# Restore on replica
mariadb-backup --prepare --target-dir=/backup/path
mariadb-backup --copy-back --target-dir=/backup/path

# Start MariaDB server
systemctl start mariadb

# Configure replication
CHANGE MASTER TO 
   MASTER_HOST='master.example.com', 
   MASTER_USER='repl', 
   MASTER_PASSWORD='secret', 
   MASTER_USE_GTID=slave_pos, 
   MASTER_DEMOTE_TO_SLAVE=1; 
START SLAVE;  
```

When the `MASTER_DEMOTE_TO_SLAVE=1` option is set, the restored backup can replicate from the original location.

Note that the restored server will behave as if `RESET MASTER` was executed at backup time. Also, any number of prepared transactions will be rolled back on the first startup.

## Migration and Upgrades

### New Installations (Simple)

For new MariaDB 12.3 and later installations, enable the below options in your configuration:

```ini
[mariadb]
--log-bin 
--binlog-storage-engine=innodb
```

When you enable the InnoDB-based binary log on a new installation, no more migration steps are required.

### Migration from Traditional Binlog

Starting with MariaDB 12.3, there are three primary methods to migrate from the Traditional Binlog to the New Binlog Format:

#### Method 1: Direct Restart Migration (Simple)

This is the simplest approach, appropriate for cases where point-in-time recovery does not require maintaining old binary log files.

1. Stop the MariaDB server.
2. &#x20;Add `--log-bin` and `--binlog-storage-engine=innodb` to your configuration.
3. The new binlog begins empty if the server is restarted.
4. Remove the old binlog files from the storage directory manually.

#### Method 2: Replication State Migration (GTID Preservation)

This approach is used to switch a master server while ensuring that connected replicas can continue replicating without the need for a full reconfiguration.

1. Stop all writing to the master.
2. Wait for all replicas to catch up to the master's current position.
3. Capture the current GTID state by noting down the value of `@@binlog_gtid_state`.
4. Restart the master with this configuration:

```ini
[mariadb]
--log_bin
--binlog-storage-engine=innodb
```

5. Immediately execute `SET GLOBAL binlog_gtid_state=<old value>` using the value saved in step 3.
6. Allow replicas to reconnect; they will continue from where they left off.

#### Method 3: Live Migration (Zero downtime)

This is the most robust method for production environments, as it avoids master downtime during the format transition.

1. Ensure that all replicas are upgraded to at least MariaDB version 12.3 before switching the master.
2. Choose a replica and restart it with `--binlog-storage-engine=innodb`.
3. Allow the replica to replicate from the old-format master until it has enough binlog data.
4. Promote this replica to be the new master.
5. Restart the remaining replicas to point to the new master after stopping them one at a time and changing their configuration to the new binlog format.

## Performance Characteristics

The InnoDB-based binary log eliminates the traditional 2PC protocol between the binary log and the InnoDB storage engine, which results in:

* Reduced commit latency.
* Removal of `sync_binlog` overhead.
* When `--innodb-flush-log-at-trx-commit=1` is set, a single synchronized flush occurs.

Commit durability is now controlled solely by the [--innodb-flush-log-at-trx-commit](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_flush_log_at_trx_commit) setting.

### Flush Policy

* `--innodb-flush-log-at-trx-commit=1`: Performs a single coordinated flush of both table data and binary log, offering greater efficiency compared to the traditional binlog implementation
* `--innodb-flush-log-at-trx-commit=2`: Provides higher throughput with acceptable crash trade-offs

The `sync_binlog` option is effectively ignored when using the InnoDB-based binary log.

### GTID State Interval

The `--innodb-binlog-state-interval` configuration option controls how often GTID state records are written to the binary log. Lowering this value helps replicas reconnect faster during high traffics.

## Limitations and Unsupported Features

The following list of features are not supported when using the InnoDB-based binary log implementation:

#### Replication Positioning

Old-style filename/offset replication positions are not supported. Replication must use GTID-based replication (default).

#### Semi-Synchronous Replication

Semi-synchronous replication is not supported in the initial implementation. Also, The `AFTER_SYNC` option cannot be supported because the traditional 2PC no longer exists.

#### Galera Cluster

The InnoDB-based binary log cannot be used with MariaDB Galera Cluster.

#### Heuristic Recovery

The `--tc-heuristic-recover` option is not supported with the InnoDB-based binary log. If the binary log is empty (i.e., deleted manually), pending transactions will be rolled back.&#x20;

#### SHOW BINLOG EVENTS FROM Behavior

If an event group starts in the middle of the provided position, `SHOW BINLOG EVENTS FROM` fails to produce an error.

Rather, the command begins at the first GTID event that comes after the designated point. An empty result is returned if the position is past the log's end.

#### Multiple Storage Engines

During the initial implementation, only InnoDB is available as an engine for the binlog (`--binlog-storage-engine=innodb`). The other engines can be added in future versions.

## See Also

* [Global Transaction IDs](gtid.md)
* [System Variables](../optimization-and-tuning/system-variables/server-system-variables.md)
* [CHANGE MASTER TO](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md)
* [InnoDB](../../server-usage/storage-engines/innodb/)

