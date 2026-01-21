---
description: >-
  Get an overview of MariaDB Backup. This section introduces the hot physical
  backup tool, explaining its capabilities for efficient and consistent backups
  of your MariaDB Server.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
---

# mariadb-backup

{% columns %}
{% column %}
{% content-ref url="mariadb-backup-overview.md" %}
[mariadb-backup-overview.md](mariadb-backup-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An introduction to the `mariadb-backup` utility, detailing its features, installation process, and support for hot online backups of InnoDB tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-backup-options.md" %}
[mariadb-backup-options.md](mariadb-backup-options.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A comprehensive reference for all command-line options available in mariadb-backup, covering backup, prepare, and restore operations.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="full-backup-and-restore-with-mariadb-backup.md" %}
[full-backup-and-restore-with-mariadb-backup.md](full-backup-and-restore-with-mariadb-backup.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Learn how to perform and restore full physical backups of MariaDB databases using the mariadb-backup tool, ensuring consistent data recovery.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="incremental-backup-and-restore-with-mariadb-backup.md" %}
[incremental-backup-and-restore-with-mariadb-backup.md](incremental-backup-and-restore-with-mariadb-backup.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
This guide explains how to create and apply incremental backups with `mariadb-backup`, saving storage space and reducing backup time.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="point-in-time-recovery-pitr-mariadb-backup.md" %}
[point-in-time-recovery-pitr-mariadb-backup.md](point-in-time-recovery-pitr-mariadb-backup.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Explains how to restore (recover) to a specific point in time. Point-in-time recovery is often referred to as PITR.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="partial-backup-and-restore-with-mariadb-backup.md" %}
[partial-backup-and-restore-with-mariadb-backup.md](partial-backup-and-restore-with-mariadb-backup.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Back up specific databases or tables. This guide explains how to filter your backup to include only the data you need.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="individual-database-restores-with-mariadb-backup-from-full-backup.md" %}
[individual-database-restores-with-mariadb-backup-from-full-backup.md](individual-database-restores-with-mariadb-backup-from-full-backup.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Restore a single database from a full backup. Learn the procedure to extract and recover a specific database schema from a larger backup set.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="restoring-individual-tables-and-partitions-with-mariadb-backup.md" %}
[restoring-individual-tables-and-partitions-with-mariadb-backup.md](restoring-individual-tables-and-partitions-with-mariadb-backup.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Restore specific tables from a backup. Learn the process of importing individual `.ibd` files to recover specific tables without restoring the whole database.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="setting-up-a-replica-with-mariadb-backup.md" %}
[setting-up-a-replica-with-mariadb-backup.md](setting-up-a-replica-with-mariadb-backup.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Initialize a replication slave using a backup. This guide shows how to use mariadb-backup to provision a new replica from a master server.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="files-backed-up-by-mariadb-backup.md" %}
[files-backed-up-by-mariadb-backup.md](files-backed-up-by-mariadb-backup.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
List of file types included in a backup. Understand which data files, logs, and configuration files are preserved during the backup process.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="files-created-by-mariadb-backup.md" %}
[files-created-by-mariadb-backup.md](files-created-by-mariadb-backup.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Reference of files generated during backup. This page explains the purpose of metadata files created by the `mariadb-backup`.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="using-encryption-and-compression-tools-with-mariadb-backup.md" %}
[using-encryption-and-compression-tools-with-mariadb-backup.md](using-encryption-and-compression-tools-with-mariadb-backup.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Secure and compress backup streams. Learn to pipe backup output to tools like GPG and GZIP for encryption and storage efficiency.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="how-mariadb-backup-works.md" %}
[how-mariadb-backup-works.md](how-mariadb-backup-works.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Deep dive into backup mechanics. Understand how the tool handles redo logs, locking, and file copying to ensure consistent backups.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-backup-and-backup-stage-commands.md" %}
[mariadb-backup-and-backup-stage-commands.md](mariadb-backup-and-backup-stage-commands.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Understand backup locking stages. This page explains how mariadb-backup uses `BACKUP STAGE` statements to minimize locking during operation.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/high-availability/state-snapshot-transfers-ssts-in-galera-cluster/mariadb-backup-sst-method" %}
[mariadb-backup SST Method](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/high-availability/state-snapshot-transfers-ssts-in-galera-cluster/mariadb-backup-sst-method)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Configure State Snapshot Transfers for Galera Cluster. Learn to use `mariadb-backup` for non-blocking data transfer when a new node joins a cluster.

<br>
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/high-availability/state-snapshot-transfers-ssts-in-galera-cluster/manual-sst-of-galera-cluster-node-with-mariadb-backup" %}
[Manual SST of Galera Cluster Node With mariadb-backup](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/high-availability/state-snapshot-transfers-ssts-in-galera-cluster/manual-sst-of-galera-cluster-node-with-mariadb-backup)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Perform a manual node provision. This guide details the steps to manually backup a donor and restore it to a joiner node in a Galera Cluster.

<br>
{% endcolumn %}
{% endcolumns %}
