---
description: >-
  Explains how to restore (recover) to a specific point in time. Point-in-time
  recovery is often referred to as PITR.
---

# Point-In-Time Recovery (PITR, mariadb-backup)

Recovering from a backup can restore the data directory at a specific point in time, but it does not restore the binary log. In a point-in-time recovery, start by restoring the data directory from a full or incremental backup, then use the [mysqlbinlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/mariadb-binlog-mysqlbinlog.md) utility to restore the binary log data to a specific point in time.

{% hint style="warning" %}
Run the following commands as root unless indicated otherwise.
{% endhint %}

{% stepper %}
{% step %}
#### Find the binary log position to restore to.

When MariaDB Backup runs on a MariaDB Server with binary logs is enabled (which is a prerequisite for PITR), it stores binary log information in the `xtrabackup_binlog_info` file. Consult this file to find the name of the binary log position to use. In the following example, the log position is 321:

```bash
cat /data/backups/full/xtraback_binlog_info

mariadb-node4.00001     321
```
{% endstep %}

{% step %}
#### Configure a new data directory.

Update the configuration file (for instance, `my.cnf`) to use a new data directory.

```ini
[mysqld]
datadir=/var/lib/mysql_new
```
{% endstep %}

{% step %}
#### Restore the backup.

Restore from the backup [as explained here](full-backup-and-restore-with-mariadb-backup.md).
{% endstep %}

{% step %}
#### Start the database server.

Start MariaDB Server.

```bash
systemctl start mariadb
```
{% endstep %}

{% step %}
#### Create a script using mysqlbinlog.

Use the mysqlbinlog utility to create an SQL script, using the binary log file in the _old_ data directory, the start position in the `xtrabackup_binlog_info` file, and the date and time you want to restore to. Issue the following command _as a regular user_:

```bash
$ mysqlbinlog --start-position=321 \
      --stop-datetime="2019-06-28 12:00:00" \
      /var/lib/mysql/mariadb-node4.00001 \
      > mariadb-binlog.sql
```
{% endstep %}

{% step %}
#### Run the script.

In the _new_ data directory, run the script created in the previous step:

```bash
$ mariadb < mariadb-binlog.sql
```
{% endstep %}
{% endstepper %}

## Point-in-Time Recovery Using InnoDB Log Archiving

{% hint style="info" %}
This functionality is available from MariaDB 13.0.
{% endhint %}

While binary logs are the standard method for point-in-time recovery, you can also use InnoDB log archiving. This feature allows for recovery to a specific Log Sequence Number (LSN) by replaying archived InnoDB write-ahead logs. This is particularly useful for InnoDB-only deployments or for recovery scenarios where binary logs may not be available.

To perform a point-in-time recovery using archived logs:

{% stepper %}
{% step %}
#### Enable log archiving.

Before a recovery is necessary, ensure that log archiving is active. This is done by setting the [`innodb_log_archive`](../../storage-engines/innodb/innodb-system-variables.md#innodb_log_archive) system variable to `ON` :

```sql
SET GLOBAL innodb_log_archive=ON;
```
{% endstep %}

{% step %}
#### Identify the recovery target.

Determine the target _LSN_ you wish to recover to. You can find the latest archived LSN by checking the `INNODB_LSN_ARCHIVED` status variable:

```sql
SELECT VARIABLE_VALUE
FROM INFORMATION_SCHEMA.GLOBAL_STATUS
WHERE VARIABLE_NAME = 'INNODB_LSN_ARCHIVED';
```
{% endstep %}

{% step %}
#### Stop the MariaDB Server.

Terminate the `mariadbd` process before initiating the recovery – for example:

```bash
$ sudo systemctl stop mariadb
```
{% endstep %}

{% step %}
#### Start the server with recovery parameters.

Invoke the server with the [`innodb_log_recovery_start`](../../storage-engines/innodb/innodb-system-variables.md#innodb_log_recovery_start) and [`innodb_log_recovery_target`](../../storage-engines/innodb/innodb-system-variables.md#innodb_log_recovery_target) parameters to define the recovery window.

* `innodb_log_recovery_start`: Set this to the _LSN_ of your last known good backup.
* `innodb_log_recovery_target`: Set this to the _LSN_ of your recovery point objective.

```bash
$ mariadbd --innodb_log_recovery_start=12288 --innodb_log_recovery_target=4194304
```
{% endstep %}

{% step %}
#### Verify the state.

Once the server reaches the target _LSN_, the recovery process stops. You can then verify the data integrity.

{% hint style="info" %}
Point-in-time recovery for DDL (Data Definition Language) operations may be limited as `.frm` files are not tracked by the InnoDB log.
{% endhint %}
{% endstep %}
{% endstepper %}
