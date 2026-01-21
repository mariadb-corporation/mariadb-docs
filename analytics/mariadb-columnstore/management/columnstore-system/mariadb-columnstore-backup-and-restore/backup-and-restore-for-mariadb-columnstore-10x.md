# Backup and Restore for MariaDB ColumnStore 1.0.x

## Backup and Restore for MariaDB ColumnStore 1.0.x

1. [Backup/Restore Process for MariaDB ColumnStore 1.0.x "Backup/Restore Process for MariaDB ColumnStore 1.0.x"](backup-and-restore-for-mariadb-columnstore-10x.md#backuprestore-process-for-mariadb-columnstore-10x)
2. [Backup Overview "Backup Overview"](backup-and-restore-for-mariadb-columnstore-10x.md#backup-overview)
3. [Suspend Write Activity "Suspend Write Activity"](backup-and-restore-for-mariadb-columnstore-10x.md#suspend-write-activity)
4. [Backup the MariaDB Server data files "Backup the MariaDB Server data files"](backup-and-restore-for-mariadb-columnstore-10x.md#backup-the-mariadb-server-data-files)

```sql
1. [Using mysqldump "Using mysqldump"](#using-mysqldump)
```

```sql
1. [Server Data File Directory Backup "Server Data File Directory Backup"](#server-data-file-directory-backup)
```

1. [Backup ColumnStore Data Files "Backup ColumnStore Data Files"](backup-and-restore-for-mariadb-columnstore-10x.md#backup-columnstore-data-files)
2. [Resume Write Activity "Resume Write Activity"](backup-and-restore-for-mariadb-columnstore-10x.md#resume-write-activity)
3. [Restore Overview "Restore Overview"](backup-and-restore-for-mariadb-columnstore-10x.md#restore-overview)
4. [Restoring the MariaDB Instance "Restoring the MariaDB Instance"](backup-and-restore-for-mariadb-columnstore-10x.md#restoring-the-mariadb-instance)

```sql
1. [mysqldump "mysqldump"](#mysqldump)
```

```sql
1. [Restoring the Server Data Files "Restoring the Server Data Files"](#restoring-the-server-data-files)
```

1. [Restoring the ColumnStore Data Files "Restoring the ColumnStore Data Files"](backup-and-restore-for-mariadb-columnstore-10x.md#restoring-the-columnstore-data-files)

## Backup/Restore Process for MariaDB ColumnStore 1.0.x

## Backup Overview

The high level steps involved in performing a full backup of MariaDB ColumnStore are:

* Suspend write activity on the system.
* Backup the MariaDB Server data files.
* Backup the ColumnStore data files.
* Resume write activity on the system.

### Suspend Write Activity

To suspend data writes to ColumnStore, issue the following command in the admin console:

```sql
mcsadmin> suspendDatabaseWrites
suspenddatabasewrites   Thu Oct 13 13:18:40 2016

This command suspends the DDL/DML writes to the MariaDB Columnstore Database
           Do you want to proceed: (y or n) [n]: y

Suspend Calpont Database Writes Request successfully completed
```

Optionally, `y` can be appended as an argument to `suspendDatabaseWrites` to avoid the confirmation prompt.

### Backup the MariaDB Server Data Files

The MariaDB Server should be backed up using one of the available backup methods described in the [server backup and restore overview](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/backup-and-restore-overview). Since the column store data is not stored within the MariaDB Server backup should run very quickly. Utilizing either [mysqldump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump) or just backing up the directory are straightforward options.

#### Using mysqldump

For example:

```sql
> /usr/local/mariadb/columnstore/mysql/bin/mysqldump --skip-lock-tables --no-data loansdb > mariadb_bkp.sql
```

Note the `--no-data` option since only the ddl is required for column store tables. The next step will backup the data files. If tables exist using other storage engines, then this is likely not appropriate for these.

#### Server Data File Directory Backup

Backup can be achieved by simply copying the Server data directories under `/usr/local/mariadb/columnstore/`.

```sql
> cp -rp /usr/local/mariadb/columnstore/mysql/db .
```

### Backup ColumnStore Data Files

Backup can be achieved by simply copying the data directories or using vendor supplied backup or snapshot utilities for those directories. A files and directories in the data directories where N represents a unique directory such as data1, data2, etc for each PM server.

```sql
> cp -rp /usr/local/mariadb/columnstore/data? .
```

### Resume Write Activity

To resume data writes to columnstore the following command can be issued in the admin console:

```sql
mcsadmin> resumeDatabaseWrites
resumedatabasewrites   Thu Oct 13 13:58:55 2016

This command resumes the DDL/DML writes to the MariaDB Columnstore Database
           Do you want to proceed: (y or n) [n]: y

Resume MariaDB Columnstore Database Writes Request successfully completed
```

Optionally y can be appended as an argument to `resumeDatabaseWrites` to avoid the confirmation prompt.

## Restore Overview

The high-level steps involved in restoring a backup are:

* Restore the MariaDB Instance
* Restore the ColumnStore data files.

### Restoring the MariaDB Instance

The appropriate restoration method corresponding to the backup utility used should be performed first to restore the MariaDB server instance.

#### mysqldump

If `mysqldump` was utilized, then the backup script is run:

```sql
> mcsmysql

MariaDB [(none)]> create database loansdb;
Query OK, 1 row affected (0.00 sec)

MariaDB [(none)]> use loansdb;
Database changed
MariaDB [loansdb]> source mariadb_bkp.sql
Query OK, 0 rows affected (0.00 sec)
...
MariaDB [loansdb]> exit
```

#### Restoring the Server Data Files

Backup can be achieved by simply copying the Server data directories under `/usr/local/mariadb/columnstore/`.

```sql
> rm -rf /usr/local/mariadb/columnstore/mysql/db
> cp -rpf db /usr/local/mariadb/columnstore/mysql
```

### Restoring the ColumnStore Data Files

The data directories should simply be copied from the backup location or restored via an appropriate backup or snapshot utility. 

For example:

```sql
> rm -rf /usr/local/mariadb/columnstore/data?
> cp -rpf data? /usr/local/mariadb/columnstore
> mcsadmin startSystem
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
