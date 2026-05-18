# Point-In-Time Recovery (InnoDB log archiving)

{% hint style="info" %}
This functionality is available from MariaDB 13.0.
{% endhint %}

When [InnoDB log archiving](../storage-engines/innodb/innodb-log-archiving.md) is enabled, the server retains a continuous history of write-ahead log records across multiple `ib_`_`lsn`_`.log` files. You can use this history to perform point-in-time recovery (PITR) to a specific Log Sequence Number (LSN), by replaying the archived InnoDB write-ahead logs at server startup.

This is an alternative to [PITR via mariadb-backup and binary logs](mariadb-backup/point-in-time-recovery-pitr-mariadb-backup.md), useful in InnoDB-only deployments or in recovery scenarios where binary logs are not available.

{% hint style="warning" %}
No shipped backup tool yet generates or restores backups in the `innodb_log_archive=ON` format — [`mariadb-backup`](mariadb-backup/README.md) does not support it and fails when the server is running with `innodb_log_archive=ON`. A backup tool that uses this format is being worked on. Until it ships, this procedure assumes you already have an externally-prepared restore that contains a consistent set of `ib_`_`lsn`_`.log` files alongside the InnoDB data files.
{% endhint %}

## Recovery Parameters

Two startup parameters define the range of the log replay:

* [`innodb_log_recovery_start`](../storage-engines/innodb/innodb-system-variables.md#innodb_log_recovery_start) — the LSN at which recovery begins. Set this to the end LSN of the previous restore when applying an incremental restore. The default `0` starts from the latest completed checkpoint, which is guaranteed to live in one of the last two `ib_`_`lsn`_`.log` files.
* [`innodb_log_recovery_target`](../storage-engines/innodb/innodb-system-variables.md#innodb_log_recovery_target) — the LSN at which recovery ends (the recovery point objective). When this is non-zero, persistent InnoDB tables become read-only and no log writes are allowed during the recovery session. The default `0` replays the log to its end.

You can identify candidate LSNs from the [`Innodb_lsn_archived`](../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_lsn_archived) status variable on the source server, and from the file names in the data directory (each `ib_`_`lsn`_`.log` file name encodes the LSN at file offset `0x3000`).

## Procedure

{% stepper %}
{% step %}
#### Prepare the restore.

Place the restored InnoDB data files and the corresponding `ib_`_`lsn`_`.log` archive files in the data directory. With `innodb_log_archive=ON`, the server refuses to start if a legacy `ib_logfile0` exists, so make sure it is not present.
{% endstep %}

{% step %}
#### Stop the MariaDB Server (if it is running).

```bash
$ sudo systemctl stop mariadb
```
{% endstep %}

{% step %}
#### Start the server with recovery parameters.

Pass `innodb_log_recovery_start` and `innodb_log_recovery_target` either on the command line or in the configuration file, alongside `innodb_log_archive=ON`. While `innodb_log_recovery_target` is non-zero, the server replays the archived log up to the target LSN and then keeps the InnoDB tables read-only.
{% endstep %}

{% step %}
#### Verify the state.

Once the server reaches the target LSN, the recovery process stops. Inspect [`Innodb_lsn_archived`](../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_lsn_archived), `Innodb_lsn_current`, and the contents of the recovered tables to confirm the data is at the expected logical point.
{% endstep %}

{% step %}
#### Resume normal operation.

To return to normal read-write operation, restart the server without `innodb_log_recovery_target` set.
{% endstep %}
{% endstepper %}

{% hint style="warning" %}
The server cannot validate every impossible value of `innodb_log_recovery_target`. If you set the target after the recovery checkpoint but before the LSN at which a data page has already been written, recovery completes in an inconsistent state where some pages carry an LSN past the requested target. See [`innodb_log_recovery_target`](../storage-engines/innodb/innodb-system-variables.md#innodb_log_recovery_target) for details.
{% endhint %}

{% hint style="info" %}
Point-in-time recovery of DDL operations is limited even for an InnoDB-only deployment, because part of the data dictionary is stored in `.frm` files whose creation is not covered by the InnoDB write-ahead log.
{% endhint %}

## See Also

* [InnoDB Log Archiving](../storage-engines/innodb/innodb-log-archiving.md) — feature overview, file format, monitoring, and managing archived log files.
* [`innodb_log_archive`](../storage-engines/innodb/innodb-system-variables.md#innodb_log_archive), [`innodb_log_recovery_start`](../storage-engines/innodb/innodb-system-variables.md#innodb_log_recovery_start), [`innodb_log_recovery_target`](../storage-engines/innodb/innodb-system-variables.md#innodb_log_recovery_target).
* [Point-In-Time Recovery (PITR, mariadb-backup)](mariadb-backup/point-in-time-recovery-pitr-mariadb-backup.md) — the binary-log-based PITR procedure.
