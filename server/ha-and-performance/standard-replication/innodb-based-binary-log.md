---
description: >-
  From MariaDB 12.3, the binary log can be stored in InnoDB-managed,
  page-structured files integrated with InnoDB crash recovery, instead of
  traditional flat binary log files.
---

# InnoDB-Based Binary Log

{% hint style="info" %}
This feature is available from MariaDB 12.3.
{% endhint %}

## Description

Traditionally, MariaDB treated the [binary log](../../server-management/server-monitoring-logs/binary-log/) (binlog) and the [InnoDB storage engine](../../server-usage/storage-engines/innodb/) as separate components, requiring a complex two-phase commit (2PC) protocol to keep them synchronized. With this new binlog implementation, binlog events are written to InnoDB-managed, page-structured files that are integrated with the InnoDB redo log and crash recovery. This change eliminates the need for an expensive 2PC between the binlog and InnoDB, allowing significant performance improvements and simplified crash recovery behavior.

The binlog files remain separate files on disk (with the `.ibb` extension), but instead of the traditional flat, sequential format they use InnoDB's page format and durability machinery.

InnoDB-based binary logs entirely replace traditional file-based binary logs. When enabled, the server stops writing traditional binlog files, and the new format becomes the only binary log implementation in use.

Additionally, this feature is limited to the binary log on the server. Replicas continue to use the traditional relay log implementation, therefore it does not affect them.

## Benefits

The InnoDB-based binlog offers these key performance advantages:

1. **Crash-safe recovery integrated with InnoDB**: The binlog integrates with InnoDB's crash recovery mechanism, so the binary log and InnoDB always recover to a mutually consistent state without a separate sync of the binlog. You can therefore set `--innodb-flush-log-at-trx-commit=0` or `--innodb-flush-log-at-trx-commit=2` for better performance. As with regular InnoDB tables, those settings trade durability of the most recently committed transactions for speed — but the binlog and InnoDB stay consistent with each other after a crash.
2. **Efficient commits with reduced** `fsync` **operations**: When using the `--innodb-flush-log-at-trx-commit=1` setting, the system performs only a single coordinated `fsync` per commit, instead of the multiple syncs required by the traditional 2PC.
3. The `sync_binlog` option is no longer required, as binlog files are now crash-safe without separate syncing.

## Comparison: Traditional vs. New Binlog

| Feature | Traditional Binlog | New InnoDB-Based Binlog |
|---|---|---|
| Files on Disk | Numbered files (e.g. `binlog.000001`) plus a `.index` listing file | `.ibb` files (e.g. `binlog-000001.ibb`) |
| Crash Safety | Requires `sync_binlog=1` | Native — inherited from InnoDB crash recovery |
| Commit Protocol | Two-Phase Commit (slower) | Integrated (faster) |
| Positioning | Filename/Offset or GTID | GTID only |
| File Allocation | Incremental | Pre-allocated (`max_binlog_size`) |

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

* The `log_bin` option must be specified without any value; it is not an on/off switch.
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

Binary log files are written to InnoDB-managed, page-structured files using the .ibb extension. Files follow this naming pattern:

```
binlog-000000.ibb
binlog-000001.ibb
```

**Characteristics**

* Binlog files are pre-allocated for efficiency. When binlog file N is filled up, event data continues in file N+1, and an empty file N+2 is    pre-allocated in the background. Binlog files are therefore always exactly `--max-binlog-size` bytes long; if the server restarts, binlog writing continues at the point reached before shutdown.
* The file size is managed by `max_binlog_size` (by default 1GB).
* Files are page-based (16 KB pages) with a CRC32 checksum at the end of each page.
* There are no binlog index files (`.index`)_,_ GTID index files (`.idx`)_,_ or GTID state files (`.state`)_._
* The `--binlog-checksum` option is no longer used. Binlog files are always checksummed with a CRC32 at the end of each page. To checksum data sent over the network between master and replica, use the `MASTER_SSL` option in `CHANGE MASTER` to enable SSL.

#### GTID Handling

The new binlog implementation requires GTID-based replication. Instead of GTID index and state files, the binlog periodically writes GTID state records into the binlog itself. When a replica connects (or the server starts up), the binlog is scanned from the last GTID state record to find or recover the correct GTID position.

The interval between state records is controlled by:

```ini
[mariadb]
innodb-binlog-state-interval
```

The interval is specified in bytes (default: 2 MB) and must be a power-of-two multiple of the binlog page size (16 KB). This option can be increased to reduce the overhead of state records, or decreased to speed up finding the initial GTID position at replica connect. The overhead is small either way, so normally there is little reason to change the default.

**Note:** The status variables `binlog_gtid_index_hit` and `binlog_gtid_index_miss` are not used with the new binlog implementation.

For additional configuration options, see [Replication and Binary Log System Variables](replication-and-binary-log-system-variables.md).

#### Replication

[Replication](./) configuration from the master can be performed as usual. Requirements:

* Replicas must use GTID to connect to the master (this is the default). The old filename/offset-based replication position is not available when using the new binlog on the master.
* Replicas should be upgraded to at least MariaDB 12.3 before switching the master to the new binlog format.
* The master and replica can independently use either the traditional or new binlog format.

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

**Note:** Event offsets are generally reported as zero; GTID positions should be used instead for navigation.

#### Using the `mariadb-binlog` Utility

The `mariadb-binlog` utility allows inspection of binary log files either locally or remotely:

```bash
# Read binary log from a remote server
mariadb-binlog --read-from-remote-server \
               --host=master.example.com --user=repl binlog-000001.ibb

# Read a local binary log file
mariadb-binlog /path/to/binlog-000000.ibb

# Read multiple binary log files (pass all at once, in order)
mariadb-binlog /path/to/binlog-000000.ibb \
               /path/to/binlog-000001.ibb \
               /path/to/binlog-000002.ibb
```

When viewing events across multiple binlog files, all binlog files should be passed to the `mariadb-binlog` at once in the correct order; this ensures that events that cross file boundaries are included in the output exactly once.

When using `--start-position` and `--stop-position`, it is recommended to use GTID positions. File offsets used in the traditional binlog format are not used in the new binlog and will mostly be reported as zero.

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

* `FLUSH BINARY LOGS` pads the current file to the next page boundary, truncates it, and switches to the next file. This can leave a binlog file smaller than `--max-binlog-size` (but always a multiple of the binlog page size).
* `FLUSH BINARY LOGS DELETE_DOMAIN_ID=N` removes an old domain ID from `@@gtid_binlog_pos`. This requires the domain not be in use in any existing binlog files. If the domain ID is already deleted, a warning is issued but the `FLUSH BINARY LOGS` operation still runs.

**Note:** This behavior differs from the old binlog implementation, where FLUSH is skipped if the domain ID was already deleted.

### Automatic Purging

Binlog files can be automatically removed based on age or disk usage, provided they are no longer needed by active replication replicas or for crash recovery:

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

Binlog files are only purged when limits are exceeded and files are not required for crash recovery or by active replicas.

## Backup using mariadb-backup

### Default Behavior

By default, binlog files are included in backups, resolving a long-standing limitation of the traditional binlog.

Key features:

* Binlog files are backed up in a transactionally consistent way, just like other [InnoDB](../../server-usage/storage-engines/innodb/) data.
* Backups are non-blocking, meaning the server continues running normally. By default, only `RESET MASTER`**,** `PURGE BINARY LOGS`, and `FLUSH BINARY LOGS` are blocked during the backup. This blocking can be disabled with the `--no-lock` option.
* Restored backups can serve as replicas using `MASTER_DEMOTE_TO_SLAVE=1` in `CHANGE MASTER`.

### Setting Up a Replica from Backup

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
```

```bash
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

Note that when binlog files are omitted from the backup (`--skip-binlog`), the restored server behaves as if `RESET MASTER` was run at the point of the backup. Any transactions that were prepared but not yet committed at backup time will be rolled back on first startup.

## Performance Characteristics

The InnoDB-based binary log eliminates the traditional 2PC protocol between the binary log and the InnoDB storage engine, which results in:

* Reduced commit latency.
* Removal of `sync_binlog` overhead.
* When `--innodb-flush-log-at-trx-commit=1` is set, a single synchronized flush occurs for both table data and binlog.

Commit durability is now controlled solely by [--innodb-flush-log-at-trx-commit](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_flush_log_at_trx_commit), which now applies to both binlog files and InnoDB table data.

### Flush Policy

* `--innodb-flush-log-at-trx-commit=1`: Performs a single coordinated flush of both table data and binary log, offering greater efficiency compared to the traditional binlog implementation
* `--innodb-flush-log-at-trx-commit=0`or `=2`: Provides higher throughput. As with regular InnoDB tables, these settings trade durability of the most recently committed transactions for speed, but the binlog and InnoDB remain consistent with each other after a crash.

The `sync_binlog` option is effectively ignored when using the InnoDB-based binary log.

### GTID State Interval

The `--innodb-binlog-state-interval` configuration option controls how often GTID state records are written to the binary log (default: 2 MB). Lowering this value helps replicas reconnect faster during high traffic. The overhead is small in either direction, so the default is usually appropriate.

## Migration and Upgrades

### New Installations

For new MariaDB 12.3 and later installations, add the following to your configuration file:

```ini
[mariadb]
log-bin 
binlog-storage-engine=innodb
```

When you enable the InnoDB-based binary log on a new installation, no more migration steps are required.

### Migration from Traditional Binlog

When switching an existing server to the new binlog format, the old binlog files will not be available after the switch, as the two formats are mutually exclusive. Choose the method that best suits your environment.

#### Method 1: Direct Restart Migration (Simple)

This is the simplest approach, suitable when maintaining old binary log files for point-in-time recovery is unnecessary.

1. Stop the MariaDB server.
2. &#x20;Add `--log-bin` and `--binlog-storage-engine=innodb` to your configuration.
3. Start the server. The new binlog starts empty.
4. Remove the old binlog files from the data directory manually.

#### Method 2: Replication State Migration (GTID Preservation)

This approach is used to switch a master server while ensuring connected replicas can continue replicating without full reconfiguration.

1. Stop all writes to the master.
2. Wait for all replicas to catch up to the master's current position.
3. Capture the current GTID state by noting down the value of `@@gtid_binlog_state`.
4. Restart the master with the following configuration:

```ini
[mariadb]
log-bin 
binlog-storage-engine=innodb
```

5. Immediately execute `SET GLOBAL gtid_binlog_state=<old value>` using the value saved in step 3.
6. Allow replicas to reconnect; they will continue from where they left off.

#### Method 3: Live Migration (Zero downtime)

This is the most robust method for production environments, as it avoids master downtime during the format transition.

1. Ensure that all replicas are upgraded to at least MariaDB version 12.3 before switching the master.
2. Choose a replica and restart it with `--binlog-storage-engine=innodb`.
3. Allow the replica to replicate from the old-format master until it has enough binlog data.
4. Promote this replica to be the new master.
5. Stop the remaining replicas one at a time, update their configuration to the new binlog format, and restart them.

## Using the New Binlog with 3rd-Party Programs

The new binlog uses a different on-disk format than the traditional binlog. The format of individual replication events is the same; however, the files stored on disk are page-based, and each page encapsulates event data to support splitting events into multiple pieces.

Existing 3rd-party programs that read binlog files directly will need to be modified to support the new format. Until then, such programs require using the traditional binlog format.

The protocol for reading binlog data from a running server (e.g., for a connecting replica) is mostly unchanged. Existing programs that read binlog events from a running server may be able to function unmodified. Similarly, `mariadb-binlog --read-from-remote-server` works as usual.

Key differences for client programs:

* File offsets and file boundaries are no longer meaningful and are no longer reported to connecting clients.
* There are no rotate events at the end of a file specifying the name of the next file.
* There is no new format description event at the start of each new file.
* Effectively, the binlog appears as a single unbroken stream of events to clients.
* The starting position for receiving binlog events must be specified using a GTID position; specifying a filename and file offset is not available.

## Binlog File Format Reference

This section describes the on-disk format of binlog files for developers building tools that interact with binlog files directly.

A binlog file consists of a sequence of pages. The page size is currently fixed at 16 KB. The file size is set with `--max-binlog-size`. Each page has a CRC32 in the last 4 bytes; all remaining bytes are used for data.

Numbers are stored in little-endian format. Some numbers are stored as compressed integers consisting of 1–9 bytes. The lower 3 bits determine the number of bytes used (one more than the value in the lower 3 bits, except that a value of 7 means 9 bytes are used). The stored value is the little-endian value of the used bytes, right-shifted by 3.

### File Header Page

The first page in each binlog file is a file header page:

| Offset | Size | Description |
|---|---|---|
| 0 | 4 | Magic value `0x010dfefe` identifying the file as a binlog file |
| 4 | 4 | Log-2 of the page size (currently fixed at 14 for 16 KB) |
| 8 | 4 | Major file version (currently 1). A new major version is not readable by older server versions |
| 12 | 4 | Minor file version (currently 0). New minor versions are backwards-compatible |
| 16 | 8 | File number (same as the number in the `binlog-NNNNNN.ibb` filename), for consistency check |
| 24 | 8 | Size of the file, in pages |
| 32 | 8 | InnoDB LSN corresponding to the start of the file, used for crash recovery |
| 40 | 8 | Value of `--innodb-binlog-state-interval` used in the file |
| 48 | 8 | File number of the earliest file this file may reference (used to prevent purging files still needed for large split events) |
| 56 | 8 | File number of the earliest file containing pending XA transactions that may still be active |
| 64 | 448 | Unused |
| 512 | 4 | Extra CRC32 (the header can be read as a 512-byte page to determine the real page size) |

### Data Pages and Chunks

Remaining pages are data pages. Data is structured as a sequence of records; each record consists of one or more chunks. A page contains one or more chunks; a record can span multiple pages, but a chunk always fits within one page. Chunks are a minimum of 4 bytes; any remaining 1–3 bytes of a page are filled with `0xff`. Unused bytes are set to `0x00`.

A chunk consists of a type byte, two length bytes (little-endian, counting only data bytes), and the data bytes.

The high two bits of the type byte collect chunks into records:

* Bit 7 is clear for the first chunk in a record, and set for all following chunks.
* Bit 6 is set for the last chunk in a record, and clear for all prior chunks.

### Chunk Types

| Type | Description |
|---|---|
| 0 | Not a real type. `0x00` is an unused byte and denotes end-of-data in the current binlog file. |
| 1 | **Commit record** — contains binlog event data. Starts with a compressed integer for the count of out-of-band (oob) records referenced; if non-zero, four more compressed integers give the file number and offset of the first and last oob reference. A second similar group follows for mixed transactional/non-transactional event groups. The remainder is payload data. |
| 2 | **GTID state record** — written every `--innodb-binlog-state-interval` bytes. Contains: the number of GTIDs in the state (compressed int); one more than the earliest file number with possibly active XA transactions (or 0 for none); then N×3 compressed integers, each representing one GTID in the state. |
| 3 | **Out-of-band (oob) data record** — used to split large event groups into smaller pieces organized as a forest of perfect binary trees. Starts with 5 compressed integers: node index; file number and offset of the left child oob node; file number and offset of the right child oob node. The remainder is payload event data. |
| 4 | **Filler record** — pads out the last page of a binlog file truncated by `FLUSH BINARY LOGS`. |
| 5 | **XA PREPARE record** — for consistent crash recovery of user XA transactions. Starts with 1 byte counting the number of participating storage engines, then the XID (4-byte formatID; 1-byte gtrid length; 1-byte bqual length; XID name characters). Followed by 5 compressed integers: oob node count; file number and offset of first and last oob node. |
| 6 | **XA complete record** — for recovery of internal 2PC and user XA. First byte is type: `0` = commit, `1` = XA rollback. Followed by 6–134 bytes of XID in the same format as the XA PREPARE record. |

## Limitations and Unsupported Features

The following list of features are not supported when using the InnoDB-based binary log implementation:

#### Replication Positioning

Old-style filename/offset replication positions are not supported. Replication must use GTID-based replication (the default). The following are not available with the new binlog:

- `MASTER_POS_WAIT()` — use `MASTER_GTID_WAIT()` instead.
- `BINLOG_GTID_POS()`
- `RESET MASTER TO` (plain `RESET MASTER` remains available)

#### Semi-Synchronous Replication

Semi-synchronous replication is not supported in the initial implementation. The `AFTER_SYNC` option cannot be supported because the traditional 2PC no longer exists. The `--init-rpl-role` option is also not supported.

#### Savepoints Inside Triggers

Using savepoints inside triggers is not supported, due to bugs and inconsistencies (see [MDEV-38465](https://jira.mariadb.org/browse/MDEV-38465)). Executing a `SAVEPOINT` or `ROLLBACK TO SAVEPOINT` statement inside a trigger will consistently error and roll back the entire statement.

#### Galera Cluster

The InnoDB-based binary log cannot be used with MariaDB Galera Cluster. Users running Galera must continue using the traditional binlog format.

#### XA Transaction Replication

External XA transactions are fully supported and crash-safe on the master. The new binlog stores `XA PREPARE` and `XA COMMIT`/`XA ROLLBACK` records internally (see chunk types 5 and 6 in the Binlog File Format Reference), and the server will always recover prepared transactions to a state consistent with the binlog after a crash.

However, replicating `XA PREPARE` to a replica is not supported. This means that if the master has transactions in a prepared-but-not-yet-committed state at the time of a failover, it is not possible to promote the replica and rescue those prepared transactions. In general, this is unlikely to cause issues, as external XA users typically do not rely on this failover path.

#### Binary Log Encryption

Binary log encryption (`--encrypt-binlog`) is not supported with the InnoDB-based binary log. Use full-disk encryption at the operating-system level instead, and/or SSL for the replica's connection to the master (use the `MASTER_SSL` option in `CHANGE MASTER`).

#### Heuristic Recovery

The `--tc-heuristic-recover` option is not supported. Any pending prepared transactions will always be rolled back or committed to be consistent with the binlog. If the binary log is empty (i.e., deleted manually), pending transactions will be rolled back.&#x20;

#### SHOW BINLOG EVENTS FROM Behavior

`SHOW BINLOG EVENTS FROM` does not return an error if the specified position falls in the middle of an event group. Instead, it starts from the first GTID event following the position, or returns empty if the position is past the end of the log.

### `sync_binlog` Option

The `sync_binlog` option is no longer needed and is effectively ignored. Durability of commits is now controlled solely by `--innodb-flush-log-at-trx-commit`, which applies to both binlog files and InnoDB table data.

#### Multiple Storage Engines

In the initial version, only InnoDB is available as a storage engine for the binlog (`--binlog-storage-engine=innodb`).&#x20;

## See Also

* [MariaDB Innovation: InnoDB-Based Binary Log](https://mariadb.org/mariadb-innovation-innodb-based-binary-log/) • Blog post • 4 minutes
* [Global Transaction IDs](gtid.md)
* [System Variables](../optimization-and-tuning/system-variables/server-system-variables.md)
* [CHANGE MASTER TO](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md)
* [InnoDB](../../server-usage/storage-engines/innodb/)

