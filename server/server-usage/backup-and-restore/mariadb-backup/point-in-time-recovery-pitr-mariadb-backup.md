---
description: >-
  Explains how to restore (recover) to a specific point in time. Point-in-time
  recovery is often referred to as PITR.
hidden: true
---

# Point-In-Time Recovery (PITR, mariadb-backup)

Recovering from a backup can restore the data directory at a specific point in time, but it does not restore the binary log. In a point-in-time recovery, start by restoring the data directory from a full or incremental backup, then use the [mysqlbinlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/mariadb-binlog-mysqlbinlog.md) utility to restore the binary log data to a specific point in time.

{% hint style="warning" %}
Run the following commands as root unless indicated otherwise.
{% endhint %}

{% stepper %}
{% step %}
### Find the binary log position to restore to.

When MariaDB Backup runs on a MariaDB Server with binary logs is enabled (which is a prerequisite for PITR), it stores binary log information in the `xtrabackup_binlog_info` file. Consult this file to find the name of the binary log position to use. In the following example, the log position is 321:

```bash
cat /data/backups/full/xtraback_binlog_info

mariadb-node4.00001     321
```
{% endstep %}

{% step %}
### Configure a new data directory.

Update the configuration file (for instance, `my.cnf`) to use a new data directory.

```ini
[mysqld]
datadir=/var/lib/mysql_new
```
{% endstep %}

{% step %}
### Restore the backup.

Restore from the backup [as explained here](full-backup-and-restore-with-mariadb-backup.md).
{% endstep %}

{% step %}
### Start the database server.

Start MariaDB Server.

```bash
systemctl start mariadb
```
{% endstep %}

{% step %}
### Create a script using mysqlbinlog.

Use the mysqlbinlog utility to create an SQL script, using the binary log file in the _old_ data directory, the start position in the `xtrabackup_binlog_info` file, and the date and time you want to restore to. Issue the following command _as a regular user_:

```bash
$ mysqlbinlog --start-position=321 \
      --stop-datetime="2019-06-28 12:00:00" \
      /var/lib/mysql/mariadb-node4.00001 \
      > mariadb-binlog.sql
```
{% endstep %}

{% step %}
### Run the script.

In the _new_ data directory, run the script created in the previous step:

```bash
$ mariadb < mariadb-binlog.sql
```
{% endstep %}
{% endstepper %}

