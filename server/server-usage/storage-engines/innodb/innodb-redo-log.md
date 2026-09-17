---
description: >-
  The redo log is a disk-based transaction log used during crash recovery to
  replay incomplete transactions and ensure data durability.
---

# InnoDB Redo Log

Directly editing or moving the redo logs can cause corruption, and should never normally be attempted.

## Overview

The InnoDB storage engine in MariaDB Enterprise Server employs a **Redo Log** to ensure data is written to disk reliably, even in the event of a crash. This is achieved by the Redo Log acting as a transaction log.

Redo Log records are uniquely identified by a **Log Sequence Number (LSN)**. The Redo Log consists of circular log files of a fixed size, where older records are routinely overwritten by newer ones.

InnoDB periodically performs **checkpoints**. During a checkpoint operation, InnoDB writes (flushes) the Redo Log records to the InnoDB tablespace files.

In the event of a server crash, InnoDB utilizes the Redo Log for **crash recovery** during the subsequent server startup. It locates the last checkpoint within the Redo Log and then replays the Redo Log records generated since that checkpoint, effectively flushing these pending changes to the InnoDB tablespace files.

The redo log is a single file named `ib_logfile0`. Its location is determined by the `innodb_log_group_home_dir` system variable, if configured. If this variable is not set, the file is created in the directory specified by the `datadir` system variable. Before [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), the log was spread over several files named `ib_logfileN`, where `N` is an integer, which InnoDB treated as one large circular file. A second file, `ib_logfile101`, appears only while the log is being resized, rebuilt, or upgraded; InnoDB renames it over `ib_logfile0` once the replacement is complete. The redo log plays a crucial role during crash recovery and in the background process of flushing transactions to the tablespaces.

## Feature Summary

| Feature         | Detail                                                                                                                                                                                                                        | Resources                                                                                                     |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Transaction Log | InnoDB Redo Log                                                                                                                                                                                                               |                                                                                                               |
| Storage Engine  | InnoDB                                                                                                                                                                                                                        |                                                                                                               |
| Purpose         | Crash Safety                                                                                                                                                                                                                  |                                                                                                               |
| Availability    | All ES and CS versions                                                                                                                                                                                                        | [MariaDB Enterprise Server](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/JqgUabdZsoY5EiaJmqgn/)           |
| Location        | Set by [innodb\_log\_group\_home\_dir](innodb-system-variables.md#innodb_log_group_home_dir) (Defaults to [datadir](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir)) |                                                                                                               |
| Quantity        | 1 (ES 10.5+, CS 10.5+)                                                                                                                                                                                                        | [Configure the InnoDB Redo Log](mariadb-enterprise-server-innodb-operations/configure-the-innodb-redo-log.md) |
| Size            | Set by [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size) (default varies)                                                                                                                            | [Configure the InnoDB Redo Log](mariadb-enterprise-server-innodb-operations/configure-the-innodb-redo-log.md) |

## Basic Configuration

```
[mariadb]
...
innodb_log_file_size=2G
```

```sql
SET GLOBAL innodb_log_file_size=(2 * 1024 * 1024 * 1024);

SHOW GLOBAL VARIABLES
   LIKE 'innodb_log_file_size';
```

```
+----------------------+------------+
| Variable_name        | Value      |
+----------------------+------------+
| innodb_log_file_size | 2147483648 |
+----------------------+------------+
```

## Flushing Effects on Performance and Consistency

The [innodb\_flush\_log\_at\_trx\_commit](innodb-system-variables.md#innodb_flush_log_at_trx_commit) system variable determines how often the transactions are flushed to the redo log, and it is important to achieve a good balance between speed and reliability.

### Binary Log Group Commit and Redo Log Flushing

When both [innodb\_flush\_log\_at\_trx\_commit=1](innodb-system-variables.md#innodb_flush_log_at_trx_commit) (the default) is set and the [binary log](../../../server-management/server-monitoring-logs/binary-log/) is enabled, there is one less sync to disk inside InnoDB during commit (2 syncs shared between a group of transactions instead of 3). See [Binary Log Group Commit and InnoDB Flushing Performance](binary-log-group-commit-and-innodb-flushing-performance.md) for more information.

## Redo Log Capacity

There is one redo log file, so the capacity of the redo log follows from [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size) alone. The first 12288 bytes of the file hold the header and the two checkpoint blocks (see [Redo Log File Format](#redo-log-file-format)) and cannot hold log records, and InnoDB reserves a further 10% of the remainder as a safety margin. The capacity available for log records is therefore:

`log capacity` = ([innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size) - 12288) \* 0.9

For example, with [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size) set to `2G`:

* `log capacity` = (`2147483648` - `12288`) \* `0.9`
* \= `1932720024` bytes
* \= approximately `1.8G`

InnoDB begins forcing checkpoints and flushing dirty pages well before the checkpoint age reaches that figure. The threshold at which it does so is derived from the same capacity, less a reserve proportional to [innodb\_page\_size](innodb-system-variables.md#innodb_page_size).

Before [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), the redo log was spread over `innodb_log_files_in_group` files and the capacity was the combined size of all of them. That system variable was deprecated and ignored in [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.2) and removed in [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.0).

### Sizing the Redo Log

A larger redo log defers page writes. InnoDB can leave a page dirty in the buffer pool across many changes and write it out once, instead of flushing it repeatedly to hold the checkpoint age down. On write-heavy workloads that modify the same pages over and over, that reduces write amplification and the storage wear which comes with it. Where the workload calls for it, the redo log can be set to several times the size of the buffer pool.

The cost of doing so is paid at crash recovery. Recovery buffers redo records in blocks taken from the [buffer pool](innodb-buffer-pool.md), so the amount of redo InnoDB can apply in one pass is bounded by the buffer pool size. When the redo left to apply is too large for that — roughly, when it would occupy more than a third of the buffer pool — InnoDB switches to multi-batch recovery, re-reading the log in several passes and taking correspondingly longer. It reports this in the error log:

```
InnoDB: Multi-batch recovery needed at LSN 123456789
```

Recovery still completes; it is only slower. Size [innodb\_buffer\_pool\_size](innodb-system-variables.md#innodb_buffer_pool_size) with that in mind, rather than for steady-state throughput alone.

### Changing the Redo Log Capacity

From [MariaDB 10.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.9/what-is-mariadb-109), [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size) is dynamic, and the redo log can be resized without restarting the server:

```sql
SET GLOBAL innodb_log_file_size=(2 * 1024 * 1024 * 1024);
```

The resize is performed asynchronously in the background, by writing a new `ib_logfile101` and renaming it over `ib_logfile0`. Set [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size) in a configuration file as well, so that the new size survives a restart. Before [MariaDB 10.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.9/what-is-mariadb-109), the size could only be changed in a configuration file and took effect on the next restart.

For the full procedure, see [Configure the InnoDB Redo Log](mariadb-enterprise-server-innodb-operations/configure-the-innodb-redo-log.md).

{% hint style="danger" %}
Do not delete `ib_logfile0` to resize the redo log. From [MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1), the server refuses to start when the file is missing. See [Redo Log File Requirements](#redo-log-file-requirements).
{% endhint %}

## Log Sequence Number (LSN)

Records within the InnoDB redo log are identified via a log sequence number (LSN).

## Checkpoints

When InnoDB performs a checkpoint, it writes the LSN of the oldest dirty page in the [InnoDB buffer pool](innodb-buffer-pool.md) to the InnoDB redo log. If a page is the oldest dirty page in the [InnoDB buffer pool](innodb-buffer-pool.md), then that means that all pages with lower LSNs have been flushed to the physical InnoDB tablespace files. If the server were to crash, then InnoDB would perform crash recovery by only applying log records with LSNs that are greater than or equal to the LSN of the oldest dirty page written in the last checkpoint.

Checkpoints are one of the tasks performed by the InnoDB master background thread. This thread schedules checkpoints 7 seconds apart when the server is very active, but checkpoints can happen more frequently when the server is less active.

Dirty pages are not actually flushed from the buffer pool to the physical InnoDB tablespace files during a checkpoint. That process happens asynchronously on a continuous basis by InnoDB's write I/O background threads configured by the [innodb\_write\_io\_threads](innodb-system-variables.md#innodb_write_io_threads) system variable. If you want to make this process more aggressive, then you can decrease the value of the [innodb\_max\_dirty\_pages\_pct](innodb-system-variables.md#innodb_max_dirty_pages_pct) system variable. You may also need to better tune InnoDB's I/O capacity on your system by setting the [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity) system variable.

### Determining the Checkpoint Age

The checkpoint age is the amount of data written to the InnoDB redo log since the last checkpoint.

#### Determining the Checkpoint Age in InnoDB

**MariaDB starting with** [**10.5**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105)

[MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105) reintroduced the [Innodb\_checkpoint\_age](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_checkpoint_age) status variable for determining the checkpoint age.

The checkpoint age can also be determined by the process shown below.

To determine the InnoDB checkpoint age, do the following:

* Query [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md).
* Find the `LOG` section:

```
---
LOG
---
Log sequence number 252794398789379
Log flushed up to 252794398789379
Pages flushed up to 252792767756840
Last checkpoint at 252792767756840
0 pending log flushes, 0 pending chkp writes
23930412 log i/o's done, 2.03 log i/o's/second
```

* Perform the following calculation:

`innodb_checkpoint_age` = `Log sequence number` - `Last checkpoint at`

In the example above, that would be:

* `innodb_checkpoint_age` = `Log sequence number` - `Last checkpoint at`
* \= 252794398789379 - 252792767756840
* \= 1631032539 bytes
* \= 1631032539 byes / (1024 \* 1024 \* 1024) (GB/bytes)
* \= 1.5 GB of redo log written since last checkpoint

## Determining the Redo Log Occupancy

The redo log occupancy is the percentage of the InnoDB redo log capacity that is taken up by dirty pages that have not yet been flushed to the physical InnoDB tablespace files in a checkpoint. Therefore, it's determined by the following calculation:

`innodb_log_occupancy` = [innodb\_checkpoint\_age](innodb-redo-log.md#determining-the-checkpoint-age) / [log capacity](innodb-redo-log.md#redo-log-capacity)

For example, if [innodb\_checkpoint\_age](innodb-redo-log.md#determining-the-checkpoint-age) is `1.5G` and the [log capacity](innodb-redo-log.md#redo-log-capacity) is `1.8G`, then we would have the following:

* `innodb_log_occupancy` = [innodb\_checkpoint\_age](innodb-redo-log.md#determining-the-checkpoint-age) / [log capacity](innodb-redo-log.md#redo-log-capacity)
* \= `1.5G` / `1.8G`
* \= `0.83`

If the calculated value for redo log occupancy is too close to `1.0`, then the InnoDB redo log capacity may be too small for the current workload.

## Redo Log File Format

**MariaDB starting with** [**10.8.1**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1)

[MDEV-14425](https://jira.mariadb.org/browse/MDEV-14425) replaced the InnoDB redo log format in [MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1) to reduce write amplification and to remove a scalability bottleneck.

Before the change, the log was written in fixed 512-byte blocks, each carrying a 12-byte header and a 4-byte footer — 12 and 8 bytes respectively with [innodb\_encrypt\_log=ON](innodb-system-variables.md#innodb_encrypt_log). Zero-filling, encrypting, and checksumming those blocks all happened while holding the global log mutex, which serialized commits. The current format has no block framing at all, so a transaction's log records are encrypted and checksummed in a thread-local buffer before the mutex is taken; the mutex then only covers a `memcpy()` into the shared log buffer.

The format is not backward compatible: [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/what-is-mariadb-107) and earlier cannot read it. See [Upgrading Across the Format Change](#upgrading-across-the-format-change) and [Downgrading Between Major Versions of MariaDB](../../../server-management/install-and-upgrade-mariadb/downgrading-between-major-versions-of-mariadb.md).

### File Layout

`ib_logfile0` opens with a fixed 12288-byte (`0x3000`) area, followed by the circular region that holds the log records:

| Offset   | Size             | Contents                                                                                                                                                                                                                                                                                                                       |
| -------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `0x0000` | 4096 bytes       | File header. The format identifier occupies the first 4 bytes, the LSN at which the file starts occupies 8 bytes at offset 8, and a creator string identifying what wrote the file (`MariaDB <version>`, or `Backup <version>` for a file written by [mariadb-backup](../../backup-and-restore/mariadb-backup/)) runs from offset 16 to 48. For an encrypted log, encryption information follows from offset 48. A CRC-32C of the first 508 bytes is stored at offset 508. |
| `0x1000` | 64 bytes         | First checkpoint block.                                                                                                                                                                                                                                                                                                        |
| `0x2000` | 64 bytes         | Second checkpoint block.                                                                                                                                                                                                                                                                                                       |
| `0x3000` | To end of file   | Log records, written circularly.                                                                                                                                                                                                                                                                                               |

A checkpoint block holds the checkpoint LSN (8 bytes), the LSN at which the log ended when the checkpoint was written (8 bytes), zero padding, and a CRC-32C of the preceding 60 bytes. InnoDB alternates between the two blocks, so a checkpoint write never overwrites the last known-good one. On startup, InnoDB reads both and uses whichever holds the higher valid checkpoint LSN.

Before [MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1), the two checkpoint blocks were 512 bytes each, at offsets `0x200` and `0x600`, and log records started at `0x800`. Moving them to 4096-byte boundaries allows InnoDB to use 4096-byte aligned I/O throughout the file, which matters on storage with a 4096-byte physical block size.

### Mini-Transaction Framing

Every change InnoDB makes to a page happens inside a mini-transaction. From [MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1), each mini-transaction is its own variable-length unit in the log, and effectively takes the place of the old fixed-size log block. Each one ends with:

* One byte holding a sequence bit, which is toggled every time writing wraps back around to offset `0x3000`. Crash recovery and [mariadb-backup](../../backup-and-restore/mariadb-backup/) use it to find where the circular log logically ends.
* A CRC-32C checksum covering the mini-transaction, excluding the sequence bit.

With [innodb\_encrypt\_log=ON](innodb-system-variables.md#innodb_encrypt_log), 8 bytes of initialization vector sit between the sequence bit and the checksum and are covered by it. File names, page identifiers, and checkpoint information are no longer encrypted — only the page-level payload is, with the tablespace ID and page number forming part of the initialization vector. This is what allows [mariadb-backup](../../backup-and-restore/mariadb-backup/) to copy an encrypted redo log without access to the encryption keys.

Because there is no mandatory block structure, InnoDB pads a write out to a block boundary with an `FILE_CHECKPOINT` record of whatever length is needed and an all-zero payload, instead of zero-filling the tail of a 512-byte block under a mutex.

### Format Identifiers

The first 4 bytes of `ib_logfile0` identify the format, as a big-endian unsigned integer:

| Value        | Format                                                                 |
| ------------ | ---------------------------------------------------------------------- |
| `0x00000000` | MariaDB 10.2.1 and earlier (the original, untagged InnoDB format)      |
| `0x00000001` | MySQL 5.7.9 / MariaDB 10.2.2                                           |
| `0x00000067` | MariaDB 10.3.2                                                         |
| `0x00000068` | MariaDB 10.4.0                                                         |
| `0x50485953` | MariaDB 10.5.1, the physical redo log format                           |
| `0x50687973` | MariaDB 10.8.1, the current format                                     |
| `0xf09f979d` | MariaDB 10.11.15, 11.4.9, 11.8.4 and 12.1.2, encrypted logs only       |

In the 10.4 and 10.5 formats, an encrypted log set the high bit of the identifier. The 10.8 format does not: encryption is indicated instead by the presence of encryption information after the creator field, so an encrypted log written by [MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1) still carries `0x50687973`.

[MDEV-36024](https://jira.mariadb.org/browse/MDEV-36024) then redesigned [innodb\_encrypt\_log=ON](innodb-system-variables.md#innodb_encrypt_log) to recover a performance regression, giving encrypted logs their own format identifier, `0xf09f979d`, from [MariaDB 10.11.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.15), [MariaDB 11.4.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.9), [MariaDB 11.8.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/11.8.4) and MariaDB 12.1.2. Those versions still read an encrypted log in the 10.8 format, and a log written with [innodb\_encrypt\_log=OFF](innodb-system-variables.md#innodb_encrypt_log) is unaffected.

### Minimum File Size

The smallest valid `ib_logfile0` is 12304 bytes (`0x3010`) — the 12288-byte fixed area plus the 16 bytes of a single `FILE_CHECKPOINT` record. A non-empty file smaller than that is rejected:

```
[ERROR] InnoDB: File ./ib_logfile0 is too small
```

This is also the size of the logically empty `ib_logfile0` that [mariadb-backup --prepare](../../backup-and-restore/mariadb-backup/mariadb-backup-options.md#prepare) leaves in the prepared backup directory. Before [MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1), that placeholder was a zero-length file.

## Redo Log File Requirements

**MariaDB starting with** [**10.8.1**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1)

From [MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1) ([MDEV-27199](https://jira.mariadb.org/browse/MDEV-27199)), InnoDB requires `ib_logfile0` to exist and to be valid in order to start. It no longer creates a replacement when the file is missing.

The reason is data safety. To make an automatic re-creation possible, earlier versions wrote the shutdown LSN to the `FIL_PAGE_FILE_FLUSH_LSN` field of the first page of the system tablespace, bypassing both the redo log and the doublewrite buffer. A server killed during that write could leave the first page of the system tablespace corrupted and the server unable to start at all. Because the log is no longer re-created automatically, that field is no longer written.

The practical consequences:

* Deleting `ib_logfile0` — a common way to resize the redo log on older versions — now makes the server fail to start, rather than silently discarding the log. Use `SET GLOBAL innodb_log_file_size` instead; see [Changing the Redo Log Capacity](#changing-the-redo-log-capacity).
* [mariadb-backup](../../backup-and-restore/mariadb-backup/) and the Galera state snapshot transfer scripts no longer delete `ib_logfile0` or leave a zero-length one behind.
* Additional `ib_logfileN` files alongside a 10.8-format `ib_logfile0` are an error:

```
[ERROR] InnoDB: Expecting only ib_logfile0
```

{% hint style="warning" %}
Creating a zero-length `ib_logfile0` by hand is not a way to discard the log. If the log is discarded while changes have already been written to data pages, any kind of corruption may follow, and errors such as "page LSN is in the future" are a typical symptom. A database initialized by [MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1) or later refuses such a startup, because `FIL_PAGE_FILE_FLUSH_LSN` was never written and so holds no valid LSN. If an older server did once write a valid LSN to that field, this safety check cannot help, and the server may rewind to an earlier LSN.
{% endhint %}

### Reading a Database Without a Valid Redo Log

[innodb\_force\_recovery=6](innodb-system-variables.md#innodb_force_recovery) is the only setting that starts InnoDB without a valid redo log, and it is a data-salvage tool, not a recovery procedure. It ignores the redo log entirely and forces the server into read-only mode, so that the contents of a possibly corrupted database can be dumped with [mariadb-dump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) and reloaded into a fresh instance.

## Upgrading Across the Format Change

[MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1) and later read the redo log formats of [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.2) through [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/what-is-mariadb-107), but only when the log is logically empty — that is, after a clean shutdown. On the first startup the old log is replaced with a new one in the current format, written as `ib_logfile101` and renamed over `ib_logfile0`.

Shut the old server down cleanly before upgrading. Upgrading on a log left dirty by a crash is not supported, and fails with:

```
[ERROR] InnoDB: Upgrade after a crash is not supported.
The redo log was created with MariaDB 10.6.23.
You must start up and shut down MariaDB 10.7 or earlier.
```

The same applies to [mariadb-backup --prepare](../../backup-and-restore/mariadb-backup/mariadb-backup-options.md#prepare), which reports that the prepare is not possible and that a `mariadb-backup` of 10.7 or earlier must be used. For the pre-[10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105) log formats, the version named in the message is 10.4 or earlier instead.

A log in a format the server does not recognize — including one written by a newer release — is refused outright:

```
[ERROR] InnoDB: Unsupported redo log format.
The redo log was created with MariaDB 12.3.1.
```

The log is also rebuilt at startup, in the same way, when [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size) or [innodb\_encrypt\_log](innodb-system-variables.md#innodb_encrypt_log) differs from what the existing file holds.

## Parameters and Counters Removed in MariaDB 10.8

With the block structure gone, the following were removed in [MariaDB 10.8.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.1):

| Removed                                                                                                                                                                                                                                                                            | Notes                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [innodb\_log\_write\_ahead\_size](innodb-system-variables.md#innodb_log_write_ahead_size)                                                                                                                                                                                          | Reintroduced in [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/10.11.9) and later series ([MDEV-33894](https://jira.mariadb.org/browse/MDEV-33894)). While it was absent, InnoDB detected the physical block size of the underlying storage on Linux and Windows and used that.                                     |
| [Innodb\_os\_log\_fsyncs](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_os_log_fsyncs), [Innodb\_os\_log\_pending\_fsyncs](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_os_log_pending_fsyncs) | Redo log fsyncs are counted by [Innodb\_data\_fsyncs](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_data_fsyncs). The pending count was limited to at most 1 by design.                                                                                                                             |
| `os_log_fsyncs`, `os_log_pending_fsyncs`, `log_pending_log_flushes`, `log_pending_checkpoint_writes`, `log_padded`                                                                                                                                                                  | [INFORMATION\_SCHEMA.INNODB\_METRICS](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) counters.                                                                                                                                                    |

The minimum value of [innodb\_log\_buffer\_size](innodb-system-variables.md#innodb_log_buffer_size) was also raised to 2 MiB.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
