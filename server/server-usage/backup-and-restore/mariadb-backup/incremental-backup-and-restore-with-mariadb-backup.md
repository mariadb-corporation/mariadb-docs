# Incremental Backup and Restore with mariadb-backup

{% include "../../../.gitbook/includes/mariadb-backup-was-previous....md" %}

When using mariadb-backup, you have the option of performing a full or incremental backup. Full backups create a complete copy in an empty directory while incremental backups update a previous backup with new data. This page documents incremental backups.

InnoDB pages contain log sequence numbers, or LSN's. Whenever you modify a row on any InnoDB table on the database, the storage engine increments this number. When performing an incremental backup, mariadb-backup checks the most recent LSN for the backup against the LSN's contained in the database. It then updates any of the backup files that have fallen behind.

### Backing up the Database Server

In order to take an incremental backup, you first need to take a full backup. In order to back up the database, you need to run mariadb-backup with the --backup option to tell it to perform a backup and with the --target-dir option to tell it where to place the backup files. When taking a full backup, the target directory must be empty or it must not exist.

To take a backup, run the following command:

```bash
$ mariadb-backup --backup \
   --target-dir=/var/mariadb/backup/ \
   --user=mariadb-backup --password=mypassword
```

This backs up all databases into the target directory `/var/mariadb/backup`. If you look in that directory at the xtrabackup\_checkpoints file, you can see the LSN data provided by InnoDB.

For example:

```bash
backup_type = full-backuped
from_lsn = 0
to_lsn = 1635102
last_lsn = 1635102
recover_binlog_info = 0
```

### Backing up the Incremental Changes

Once you have created a full backup on your system, you can also back up the incremental changes as often as you would like.

In order to perform an incremental backup, you need to run mariadb-backup with the --backup option to tell it to perform a backup and with the --target-dir option to tell it where to place the incremental changes. The target directory must be empty. You also need to run it with the --incremental-basedir option to tell it the path to the full backup taken above. For example:

```bash
$ mariadb-backup --backup \
   --target-dir=/var/mariadb/inc1/ \
   --incremental-basedir=/var/mariadb/backup/ \
   --user=mariadb-backup --password=mypassword
```

This command creates a series of delta files that store the incremental changes in `/var/mariadb/inc1`. You can find a similar xtrabackup\_checkpoints file in this directory, with the updated LSN values.

For example:

```bash
backup_type = incremental
from_lsn = 1635102
to_lsn = 1635114
last_lsn = 1635114
recover_binlog_info = 0
```

To perform additional incremental backups, you can then use the target directory of the previous incremental backup as the incremental base directory of the next incremental backup. For example:

```bash
$ mariadb-backup --backup \
   --target-dir=/var/mariadb/inc2/ \
   --incremental-basedir=/var/mariadb/inc1/ \
   --user=mariadb-backup --password=mypassword
```

### Combining with `--stream` output

When using --stream, e.g for compression or encryption using external tools, the xtrabackup\_checkpoints file containing the information where to continue from on the next incremental backup will also be part of the compressed/encrypted backup file, and so not directly accessible by default.

A directory containing an extra copy of the file can be created using the --extra-lsndir=... option though, and this directory can then be passed to the next incremental backup --incremental-basedir=..., for example:

```bash
# initial full backup
$ mariadb-backup --backup --stream=mbstream \
  --user=mariadb-backup --password=mypassword \
  --extra-lsndir=backup_base | gzip > backup_base.gz

# incremental backup
$ mariadb-backup --backup --stream=mbstream \
  --incremental-basedir=backup_base \
  --user=mariadb-backup --password=mypassword \
  --extra-lsndir=backup_inc1 | gzip > backup-inc1.gz
```

### Preparing the Backup

Following the above steps, you have three backups in `/var/mariadb`: The first is a full backup, the others are increments on this first backup. In order to restore a backup to the database, you first need to apply the incremental backups to the base full backup. This is done using the --prepare command option. In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1), you would also have to use the --apply-log-only option.

In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) and later, perform the following process:

First, prepare the base backup:

```bash
$ mariadb-backup --prepare \
   --target-dir=/var/mariadb/backup
```

Running this command brings the base full backup, that is, `/var/mariadb/backup`, into sync with the changes contained in the InnoDB redo log collected while the backup was taken.

Then, apply the incremental changes to the base full backup:

```bash
$ mariadb-backup --prepare \
   --target-dir=/var/mariadb/backup \
   --incremental-dir=/var/mariadb/inc1
```

Running this command brings the base full backup, that is, `/var/mariadb/backup`, into sync with the changes contained in the first incremental backup.

For each remaining incremental backup, repeat the last step to bring the base full backup into sync with the changes contained in that incremental backup.

### Restoring the Backup

Once you've applied all incremental backups to the base, you can restore the backup using either the --copy-back or the --move-back options. The --copy-back option allows you to keep the original backup files. The --move-back option actually moves the backup files to the datadir, so the original backup files are lost.

* First, [stop the MariaDB Server process](https://mariadb.com/kb/en/).
* Then, ensure that the datadir is empty.
* Then, run mariadb-backup with one of the options mentioned above:

```
$ mariadb-backup --copy-back \
   --target-dir=/var/mariadb/backup/
```

* Then, you may need to fix the file permissions.

When mariadb-backup restores a database, it preserves the file and directory privileges of the backup. However, it writes the files to disk as the user and group restoring the database. As such, after restoring a backup, you may need to adjust the owner of the data directory to match the user and group for the MariaDB Server, typically `mysql` for both. For example, to recursively change ownership of the files to the `mysql` user and group, you could execute:

```bash
$ chown -R mysql:mysql /var/lib/mysql/
```

* Finally, [start the MariaDB Server process](https://mariadb.com/kb/en/).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
