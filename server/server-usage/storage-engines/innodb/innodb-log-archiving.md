# InnoDB Log Archiving

{% hint style="info" %}
This functionality is available from MariaDB 13.0.
{% endhint %}

## Overview

By default, the InnoDB write-ahead log is managed as a ring buffer in a single file (`ib_logfile0`). This is efficient for write performance, but log records are eventually overwritten as the ring wraps, which limits the options for [point-in-time recovery (PITR)](../../backup-and-restore/innodb-log-archive-pitr.md) and [incremental backups](../../backup-and-restore/mariadb-backup/incremental-backup-and-restore-with-mariadb-backup.md).

InnoDB log archiving replaces the ring buffer with a sequence of pre-allocated, sequentially-named log files. When one file fills up, the server creates the next. Once a checkpoint completes in a new file, the previous file is marked read-only — at which point you can safely move it to long-term storage. The result is a continuous log history for the period archiving was active.

{% hint style="warning" %}
No shipped backup tool yet generates or restores backups in the `innodb_log_archive=ON` format. [`mariadb-backup`](../../backup-and-restore/mariadb-backup/README.md) only supports the legacy `ib_logfile0` format and fails when the server is running with `innodb_log_archive=ON`. A backup tool that uses this format is being worked on.
{% endhint %}

## Enabling Log Archiving

To enable log archiving, set the [`innodb_log_archive`](innodb-system-variables.md#innodb_log_archive) system variable to `ON`. This variable is dynamic and can be changed while the server is running:

```sql
SET GLOBAL innodb_log_archive=ON;
```

When archiving is active, the server creates files in the data directory using the naming convention `ib_`_`lsn`_`.log`, where _lsn_ is a 16-character hexadecimal value identifying the log sequence number that maps to file offset `0x3000` (12288) — the start of record payload within each file.

### File format

Each archive log file has a 12 KiB header. Completed checkpoints in the file are recorded in this header as 64-bit big-endian offsets to a `FILE_MODIFY` / `FILE_CHECKPOINT` mini-transaction within the file. With `innodb_encrypt_log=OFF`, the header can hold up to 1536 checkpoint slots; if a file produces more checkpoints than that, further checkpoints overwrite the last slot until the next log file is started.

### Technical constraints

* **Log file size:** When `innodb_log_archive` is `ON`, changes to [`innodb_log_file_size`](innodb-system-variables.md#innodb_log_file_size) take effect when the current log file fills up and a new file is created. There is no special upper bound on `innodb_log_file_size` in this mode.
* **Encryption:** While `innodb_log_archive` is `ON`, [`innodb_encrypt_log`](innodb-system-variables.md#innodb_encrypt_log) and related encryption parameters cannot be changed. Each `ib_`_`lsn`_`.log` file must use the same encryption parameters. To change encryption, set `innodb_log_archive=OFF` and restart the server — this permanently discards the archived log history.
* **Startup:** With `innodb_log_archive=ON`, the server refuses to start if `ib_logfile0` exists in the data directory.
* **Data Dictionary:** Log archiving tracks changes to InnoDB tables. It does not cover `.frm` files or other non-InnoDB metadata, which means point-in-time recovery of DDL operations is limited.

## Monitoring Archiving Progress

You can monitor the status of the log archiving process by querying the `INFORMATION_SCHEMA.GLOBAL_STATUS` table. The [`Innodb_lsn_archived`](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_lsn_archived) status variable reports the LSN since which a complete InnoDB log archive is available.

```sql
SELECT @@GLOBAL.innodb_log_archive AS archiving,
       VARIABLE_VALUE              AS lsn_archived
FROM   INFORMATION_SCHEMA.GLOBAL_STATUS
WHERE  VARIABLE_NAME = 'INNODB_LSN_ARCHIVED';
```

## Managing Archived Log Files

Once a checkpoint completes in a new log file, the previous file is marked read-only. You can safely move read-only `ib_`_`lsn`_`.log` files to offline storage.

{% hint style="warning" %}
Before _deleting_ an archived log file, check that [`Innodb_lsn_last_checkpoint`](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_lsn_last_checkpoint) is not older than the start LSN embedded in the first writable `ib_`_`lsn`_`.log` file. If it is, crash recovery still requires the previous log file — deleting it leaves the server unable to recover.
{% endhint %}

## Performing Recovery from Archived Logs

The startup parameters [`innodb_log_recovery_start`](innodb-system-variables.md#innodb_log_recovery_start) and [`innodb_log_recovery_target`](innodb-system-variables.md#innodb_log_recovery_target) define the range of the log replay. Both default to `0`:

* `innodb_log_recovery_start=0` means start from the latest completed checkpoint (always present in one of the last two `ib_`_`lsn`_`.log` files).
* `innodb_log_recovery_target=0` means replay to the end of the available log.

See [Point-In-Time Recovery (InnoDB log archiving)](../../backup-and-restore/innodb-log-archive-pitr.md) for the full procedure.
