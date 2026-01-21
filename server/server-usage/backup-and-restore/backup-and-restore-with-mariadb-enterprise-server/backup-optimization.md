---
description: >-
  Discover techniques to optimize your backup processes, including
  multithreading, incremental backups, and leveraging storage snapshots.
---

# Backup Optimization

## Overview

Backup and restore implementations can help overcome specific technical challenges that would otherwise pose a barrier to meeting business requirements.

Each of these practices represents a trade-off. Understand risks before implementing any of these practices.

## Scheduling of Restore Preparation

**Technical challenge: restore time**

**Trade-off: increased ongoing overhead for backup processing**

Backup data can be prepared for restore any time after it is produced and before it is used for restore. To expedite recovery, incremental backups can be pre-applied to the prior full backup to enable faster recovery. This may be done at the expense of recovery points, or at the expense of storage by maintaining copies of unmerged full and incremental backup directories.

## Moving Restored Data

**Technical challenge: disk space limitations**

**Trade-off: modification of backup directory contents**

Suggested method for moving restored data is to use `--copy-back` as this method provides added safety. Where you might instead optimize for disk space savings, system resources, and time you may choose to instead use MariaDB Enterprise Backup's `--move-back` option. Speed benefits are only present when backup files are on the same disk partition as the destination data directory.

The `--move-back` option will result in the removal of all data files from the backup directory, so it is best to use this option only when you have an additional copy of your backup data in another location.

To restore from a backup by moving files, use the `--move-back` option:

```bash
mariadb-backup --move-back --target-dir=/data/backups/full
```

## Multithreading

**Technical challenge:: CPU bottlenecks**

**Trade-off: Increased workload during backups**

MariaDB Enterprise Backup is a multi-threaded application that by default runs on a single thread. In cases where you have a host with multiple cores available, you can specify the number of threads you want it to use for parallel data file transfers using the `--parallel` option:

```bash
mariadb-backup --backup \
      --target-dir=/data/backups/full \
      --user=mariadb-backup \
      --password=mbu_passwd \
      --parallel=12
```

## Incrementing an Incremental Backup

**Technical challenge: Backup resource overhead, backup duration**

**Trade-off: Increased restore complexity, restore process duration**

Under normal operation an incremental backup is taken against an existing full backup. This allows you to further shorten the amount of time MariaDB Enterprise Backup locks MariaDB Enterprise Server while copying tablespaces. You can then apply the changes in the increment to the full backup with a `--prepare` operation at leisure, without disrupting database operations.

MariaDB Enterprise Backup also supports incrementing from an incremental backup. In this operation, the `--incremental-basedir` option points not to the full backup directory but rather to the previous incremental backup.

```bash
mariadb-backup --backup \
      --incremental-basedir=/data/backups/inc1 \
      --target-dir=/data/backups/inc2 \
      --user=mariadb-backup \
      --password=mbu_passwd
```

In preparing a backup to restore the data directory, apply the chain of incremental backups to the full backup in order. That is, first `inc1/, then inc2/`, and so on:

```bash
mariadb-backup --prepare \
      --target-dir=/data/backups/full \
      --incremental-dir=/data/backups/inc1
```

```bash
mariadb-backup --prepare \
      --target-dir=/data/backups/full \
      --incremental-dir=/data/backups/inc2
```

Continue to apply all the incremental changes until you have applied all available to the backup. Then restore as usual:

```bash
mariadb-backup --copy-back --target-dir=/data/backups/full
chown -R mysql:mysql /var/lib/mysql
```

Start MariaDB Enterprise Server on the restored data directory.

## Storage Snapshots

**Technical challenge: Backup resource overhead, backup duration.**

**Trade-off: Limited to platforms with volume-level snapshots, may require crash recovery.**

While MariaDB Enterprise Backups produces file-level backups, users on storage solutions may prefer to instead perform volume-level snapshots to minimize resource impact. This storage capability exists with some SAN, NAS, and volume manager platforms.

Snapshots occur point-in-time, so no preparation step is needed to ensure data is internally consistent. Snapshots occur while tablespaces are open, and a restored snapshot may need to undergo crash recovery.

Just as traditional full, incremental, and partial backups should be tested, so too should recovery from snapshots be tested on an ongoing basis.

## Taking Snapshots

{% tabs %}
{% tab title="Current" %}
MariaDB Server includes [advanced backup](mariadb-enterprise-backup.md#non-blocking-backups) functionality to reduce the impact of backup operations:

1. Connect with a client and issue a `BACKUP STAGE START` statement and then a `BACKUP STAGE BLOCK_COMMIT` statement.
2. Take the snapshot.
3. Issue a `BACKUP STAGE END` statement.
4. Once the backup has been completed, remove all files which begin with the `#sql prefix`. These files are generated when `ALTER TABLE` occurs during a staged backup.
5. Retrieve, copy, or store the snapshot as is typical for your storage platform and as per business requirements to make the backup durable. This may require mounting the snapshot in some manner.
{% endtab %}

{% tab title="< 10.11" %}
It is recommended to briefly prevent writes while snapshotting. Specific commands vary depending on storage platform, business requirements, and setup, but a general approach is to:

1. Connect with a client and issue a `FLUSH TABLES WITH READ LOCK` statement, leaving the client connected.
2. Take the snapshot.
3. Issue an `UNLOCK TABLES` statement, to remove the read lock.
4. Retrieve, copy, or store the snapshot as is typical for your storage platform and as per business requirements to make the backup durable. This may require mounting the snapshot in some manner.
{% endtab %}
{% endtabs %}

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
