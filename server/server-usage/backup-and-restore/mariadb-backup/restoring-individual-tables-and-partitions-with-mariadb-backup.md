---
description: >-
  Restore specific tables from a backup. Learn the process of importing
  individual .ibd files to recover specific tables without restoring the whole
  database.
---

# Restoring Individual Tables and Partitions with mariadb-backup

{% include "../../../.gitbook/includes/mariadb-backup-was-previous....md" %}

When using `mariadb-backup`, you don't necessarily need to restore every table and/or partition that was backed up. Even if you're starting from a full backup, it is certainly possible to restore only certain tables and/or partitions from the backup, as long as the table or partition involved is in an [InnoDB file-per-table tablespace](../../storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md). This page documents how to restore individual tables and partitions.

{% include "../../../.gitbook/includes/for-a-complete-list-of-mari....md" %}

### Preparing the Backup

Before you can restore from a backup, you first need to **prepare** it to make the data files consistent. You can do so with the `--prepare` option.

The ability to restore individual tables and partitions relies on InnoDB's transportable tablespaces. For MariaDB to import tablespaces like these, InnoDB looks for a file with a `.cfg` extension. For mariadb`-backup` to create these files, you also need to add the `--export` option during the prepare step.

For example, you might execute the following command:

```
$ mariadb-backup --prepare --export \
   --target-dir=/var/mariadb/backup/ \
   --user=mariadb-backup --password=mypassword
```

If this operation completes without error, then the backup is ready to be restored.

**Note**

`mariadb-backup` did not support the --export option to begin with. See [MDEV-13466](https://jira.mariadb.org/browse/MDEV-13466) about that. In earlier versions of MariaDB, this means that mariadb-backup could not create `.cfg` files for InnoDB file-per-table tablespaces during the `--prepare` stage. You can still import file-per-table tablespaces without the `.cfg` files in many cases, so it may still be possible in those versions to restore partial backups or to restore individual tables and partitions with just the `.ibd` files. If you have a full backup and you need to create `.cfg` files for InnoDB file-per-table tablespaces, then you can do so by preparing the backup as usual without the `--export` option, and then restoring the backup, and then starting the server. At that point, you can use the server's built-in features to copy the transportable tablespaces.

### Restoring the Backup

The restore process for restoring individual tables and/or partitions is quite different than the process for full backups.

Rather than using the `--copy-back` or the `--move-back`, each individual InnoDB file-per-table tablespace file will have to be manually imported into the target server. The process that is used to restore the backup will depend on whether partitioning is involved.

#### Restoring Individual Non-Partitioned Tables

To restore individual non-partitioned tables from a backup, find the `.ibd` and `.cfg` files for the table in the backup, and then import them using the Importing Transportable Tablespaces for Non-partitioned Tables process.

#### Restoring Individual Partitions and Partitioned Tables

To restore individual partitions or partitioned tables from a backup, find the `.ibd` and `.cfg` files for the partitions in the backup, and then import them using the [Importing Transportable Tablespaces for Partitioned Tables](../../storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#importing-transportable-tablespaces-for-partitioned-tables) process.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
