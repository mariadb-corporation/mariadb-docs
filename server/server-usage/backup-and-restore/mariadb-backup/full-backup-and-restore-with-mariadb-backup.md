---
description: >-
  Perform complete server backups and restores. This guide covers creating a
  full physical backup, preparing the data, and restoring it to the server.
---

# Full Backup and Restore with mariadb-backup

{% include "../../../.gitbook/includes/mariadb-backup-was-previous....md" %}

When using mariadb-backup, you have the option of performing a full or an incremental backup. Full backups create a complete backup of the database server in an empty directory while incremental backups update a previous backup with whatever changes to the data have occurred since the backup. This page documents how to perform full backups.

{% include "../../../.gitbook/includes/for-a-complete-list-of-mari....md" %}

### Backing up the Database Server

In order to back up the database, you need to run mariadb-backup with the `--backup` option to tell it to perform a backup and with the `--target-dir` option to tell it where to place the backup files. When taking a full backup, the target directory must be empty or it must not exist.

To take a backup, run the following command:

```bash
$ mariadb-backup --backup \
   --target-dir=/var/mariadb/backup/ \
   --user=mariadb-backup --password=mypassword
```

The time the backup takes depends on the size of the databases or tables you're backing up. You can cancel the backup if you need to, as the backup process does not modify the database.

`mariadb-backup` writes the backup files the target directory. If the target directory doesn't exist, it creates it. If the target directory exists and contains files,  it raises an error and aborts.

Here is an example backup directory:

```bash
$ ls /var/mariadb/backup/

aria_log.0000001  mysql                   xtrabackup_checkpoints
aria_log_control  performance_schema      xtrabackup_info
backup-my.cnf     test                    xtrabackup_logfile
ibdata1           xtrabackup_binlog_info
```

### Preparing the Backup for Restoration

The data files that `mariadb-backup` creates in the target directory are not point-in-time consistent, given that the data files are copied at different times during the backup operation. If you try to restore from these files, InnoDB notices the inconsistencies and crashes to protect you from corruption

Before you can restore from a backup, you first need to **prepare** it to make the data files consistent. You can do so with the `--prepare` option.

```bash
$ mariadb-backup --prepare \
   --target-dir=/var/mariadb/backup/
```

#### Backup Preparation Steps

1. Run `mariadb-backup --backup`. You must use a version of `mariadb-backup` that is compatible with the server version you are planning to upgrade from. For instance, when upgrading from MariaDB 10.4 to 10.5, you must use the 10.4 version of `mariadb-backup`, Another example: When upgrading from MariaDB 10.6 to 10.11, you must use the 10.6 version of `mariadb-backup`.
2. Run `mariadb-backup --prepare`, again using a compatible version of `mariadb-backup`, as described in the previous step.

### Restoring the Backup

Once the backup is complete and you have prepared the backup for restoration (previous step), you can restore the backup using either the `--copy-back` or the `--move-back` options. The `--copy-back` option allows you to keep the original backup files. The `--move-back` option actually moves the backup files to the datadir, so the original backup files are lost.

* First, stop the MariaDB Server process.
* Then, ensure that `datadir` is empty.
* Then, run `mariadb-backup` with one of the options mentioned above:

```bash
$ mariadb-backup --copy-back \
   --target-dir=/var/mariadb/backup/
```

* Then, you may need to fix the file permissions.

When `mariadb-backup` restores a database, it preserves the file and directory privileges of the backup. However, it writes the files to disk as the user and group restoring the database. As such, after restoring a backup, you may need to adjust the owner of the data directory to match the user and group for the MariaDB Server, typically `mysql` for both. For example, to recursively change ownership of the files to the `mysql` user and group, you could execute:

```bash
$ chown -R mysql:mysql /var/lib/mysql/
```

* Finally, start the MariaDB Server process.

#### Restoring with Other Tools

Once a full backup is prepared, it is a fully functional MariaDB data directory. Therefore, as long as the MariaDB Server process is stopped on the target server, you can technically restore the backup using any file copying tool, such as `cp` or `rsync`. For example, you could also execute the following to restore the backup:

```bash
$ rsync -avrP /var/mariadb/backup /var/lib/mysql/
$ chown -R mysql:mysql /var/lib/mysql/
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
