# InnoDB Log Archiving

{% hint style="info" %}
This functionality is available from MariaDB 13.0.
{% endhint %}

## Overview

By default, the InnoDB write-ahead log is managed as a ring buffer (typically `ib_logfile0`). While this is efficient for write performance, the logs are eventually overwritten, which can limit options for [point-in-time recovery (PITR)](../../backup-and-restore/mariadb-backup/point-in-time-recovery-pitr-mariadb-backup.md) and [incremental backups](../../backup-and-restore/mariadb-backup/incremental-backup-and-restore-with-mariadb-backup.md).

InnoDB log archiving allows the server to write a continuous, sequential stream of log files. When enabled, the server saves log data into individual files that are not overwritten, providing a complete history of changes for the period archiving was active.

## Enabling Log Archiving

To enable log archiving, set the [`innodb_log_archive`](innodb-system-variables.md#innodb_log_archive) system variable to `ON`. This variable is dynamic and can be changed while the server is running:

```sql
SET GLOBAL innodb_log_archive=ON
```

When archiving is active, the server generates files in the data directory using the naming convention `ib_`_`lsn`_`.log`. The _lsn_ represents the Log Sequence Number (LSN) at the start of that specific file.

### Technical Constraints

* Log File Size: When `innodb_log_archive` is `ON`, the [`innodb_log_file_size`](innodb-system-variables.md#innodb_log_file_size) is limited to a maximum of 4G. This ensures that 32-bit offsets within the archive headers remain functional.
* Encryption: If you use [`innodb_encrypt_log`](innodb-system-variables.md#innodb_encrypt_log), you cannot change the encryption state during a server restart while `innodb_log_archive` is `ON`.
* Data Dictionary: Log archiving tracks changes to InnoDB tables. Note that it does not cover `.frm` files or other non-InnoDB metadata.

## Monitoring Archiving Progress

You can monitor the status of the log archiving process by querying the `INFORMATION_SCHEMA.GLOBAL_STATUS` table. The `INNODB_LSN_ARCHIVED` status variable indicates the highest LSN that has been successfully written to the archive.

```sql
SELECT @@GLOBAL.innodb_log_archive, VARIABLE_VALUE
FROM INFORMATION_SCHEMA.GLOBAL_STATUS
WHERE VARIABLE_NAME = 'INNODB_LSN_ARCHIVED';
```

## Performing Recovery from Archived Logs

To recover a database using archived logs, use the [`innodb_log_recovery_start`](innodb-system-variables.md#innodb_log_recovery_start) and [`innodb_log_recovery_target`](innodb-system-variables.md#innodb_log_recovery_target) start-up parameters. These allow you to define a specific range of the log to replay, which is more efficient than replaying the entire archive.

{% stepper %}
{% step %}
#### Stop the server.
{% endstep %}

{% step %}
#### Configure the recovery range.

Start the server (via the command line or by modifying your configuration file) with the desired LSN range.

* `innodb_log_recovery_start`: The LSN where the recovery process begins.
* `innodb_log_recovery_target`: The LSN where the recovery process ends (your recovery point objective).

Example:

```bash
$ mariadbd --innodb_log_recovery_start=12288 --innodb_log_recovery_target=4194304
```

If you set an unreachable `innodb_log_recovery_target` (for example, a value higher than the available logs), the server terminates with an error. The error message displays the final available LSN, which you can then use as a valid target for a subsequent attempt.
{% endstep %}
{% endstepper %}

## Integration with Backup Tools

Log archiving is designed to facilitate external backup tools. A typical workflow involves:

1. Checking the current `INNODB_LSN_ARCHIVED` value.
2. Determining if an incremental backup is possible based on the LSN of the previous backup.
3. Enabling `innodb_log_archive` to capture changes during the backup process.
4. Disabling archiving once the backup is complete to conserve disk space, if indefinite point-in-time recovery is not required.
