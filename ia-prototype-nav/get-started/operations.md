---
title: Operations
description: >-
  Back up and restore your data with the mariadb-backup tool, keep the database available through a failed node, and tune it against measurements.
icon: gauge-high
---

# Operations

Once the `shop.products` table holds data your app depends on, the next jobs are about keeping it. Do them in order: make sure you can recover the data, then make the database survive a failed node, then make it fast. Tuning a server whose backups you've never restored solves the wrong problem first.

## Back Up, Restore, and Prove It

The `mariadb-backup` tool takes a physical copy of the data files while MariaDB Server keeps running, so a restore doesn't replay every SQL statement the way a dump does. A backup you've never restored is a guess. Run all three steps on a test server before you rely on them.

{% stepper %}
{% step %}
### Take a Physical Backup

Create a backup user with the privileges the `mariadb-backup` tool needs, then point the tool at an empty target directory. If the directory doesn't exist, the tool creates it.

```sql
CREATE USER 'mariadb-backup'@'localhost' IDENTIFIED BY 'mypassword';
GRANT RELOAD, PROCESS, LOCK TABLES, BINLOG MONITOR ON *.* TO 'mariadb-backup'@'localhost';
```

```bash
mariadb-backup --backup \
   --target-dir=/var/mariadb/backup/ \
   --user=mariadb-backup --password=mypassword
```

The [mariadb-backup overview]({server}/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview) lists the privileges for older versions and for options such as `--galera-info`.
{% endstep %}

{% step %}
### Prepare and Restore It

The files in the backup directory were copied at different moments, so prepare them first to make them consistent. To restore, stop the server, empty the data directory (`/var/lib/mysql` by default), copy the backup back, and give the files to the `mysql` user that MariaDB Server runs as.

```bash
mariadb-backup --prepare --target-dir=/var/mariadb/backup/

sudo systemctl stop mariadb
sudo mv /var/lib/mysql /var/lib/mysql.old
sudo mkdir /var/lib/mysql

sudo mariadb-backup --copy-back --target-dir=/var/mariadb/backup/
sudo chown -R mysql:mysql /var/lib/mysql/
```

Use the same version of the `mariadb-backup` tool for both the backup and the prepare step. [Full backup and restore]({server}/server-usage/backup-and-restore/mariadb-backup/full-backup-and-restore-with-mariadb-backup) covers the `--move-back` alternative and restoring with `rsync`.
{% endstep %}

{% step %}
### Confirm the Restore Worked

Start the server and query a table you know the contents of. The row count in the `shop.products` table should match what you had when you took the backup.

```bash
sudo systemctl start mariadb
sudo mariadb -e "SELECT COUNT(*) FROM shop.products;"
```

When the numbers match, remove the old data directory at `/var/lib/mysql.old`. To keep backups small between full copies, see [incremental backup and restore]({server}/server-usage/backup-and-restore/mariadb-backup/incremental-backup-and-restore-with-mariadb-backup).
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Need a backup you can load into a different MariaDB version or edit by hand? The `mariadb-dump` tool writes SQL instead of data files. The [backup quickstart]({server}/mariadb-quickstart-guides/mariadb-backup-guide) and the [restore quickstart]({server}/mariadb-quickstart-guides/mariadb-restore-guide) walk through it.
{% endhint %}

## Stay Available

With recovery in place, replicate the data and route around failures so your application doesn't notice when a node goes down.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Galera Cluster Quickstart</strong></td><td>Set up synchronous replication where every node can take writes.</td><td><a href="{galera}/galera-cluster-quickstart-guides/mariadb-galera-cluster-guide">mariadb-galera-cluster-guide</a></td></tr><tr><td><strong>MaxScale Quickstart</strong></td><td>Put MaxScale in front of your servers to route queries, split reads from writes, and handle failover for the application.</td><td><a href="{maxscale}/maxscale-quickstart-guides/maxscale-beginner-guide">maxscale-beginner-guide</a></td></tr><tr><td><strong>High Availability on MariaDB Cloud</strong></td><td>Get a replicated topology with automatic failover on the managed service.</td><td><a href="{mariadb-cloud}/high-availability-dr/ha-and-replicated-topology">ha-and-replicated-topology</a></td></tr></tbody></table>

## Measure and Manage

Tune against a baseline. Change one setting at a time, and measure before and after each change.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Benchmarking</strong></td><td>Put a realistic load on the database so you can judge every change against the same numbers.</td><td><a href="{server}/ha-and-performance/benchmarking">benchmarking</a></td></tr><tr><td><strong>Backup and Restore Overview</strong></td><td>Compare logical dumps, physical backups, and point-in-time recovery, and choose a schedule that fits your data.</td><td><a href="{server}/server-usage/backup-and-restore">backup-and-restore</a></td></tr><tr><td><strong>MariaDB Enterprise Manager</strong></td><td>Monitor and administer a fleet of MariaDB servers from one console.</td><td><a href="{tools}/mariadb-enterprise-manager">mariadb-enterprise-manager</a></td></tr></tbody></table>
