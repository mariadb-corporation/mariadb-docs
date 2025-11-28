# MariaDB Backup

Regular and reliable backups are essential to successful recovery of mission critical applications. [MariaDB Server](https://mariadb.org/en/#mariadb-server) backup and restore operations are performed using MariaDB Backup, an [open source backup tool](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview).

## **Storage Engines and Backup Types**

MariaDB Backup creates a file-level backup of data from the MariaDB Server data directory. This backup includes [temporal data](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables), and the encrypted and unencrypted tablespaces of supported storage engines (e.g., [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb), [MyRocks](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks), [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria)).

MariaDB Server implements:

* Full backups, which contain all data in the database.
* Incremental backups, which contain modifications since the last backup.
* Partial backups, which contain a subset of the tables in the database.

Backup support is specific to storage engines. All supported storage engines enable full backup. The InnoDB storage engine additionally supports incremental backup.

## **Non-Blocking Backups**

A feature of MariaDB Backup and MariaDB Server, non-blocking backups minimize workload impact during backups. When MariaDB Backup connects to MariaDB Server, staging operations are initiated to protect data during read.

Non-blocking backup functionality differs from historical backup functionality in the following ways:

* MariaDB Backup includes optimizations to backup staging, including DDL statement tracking, which reduces lock-time during backups.
* MariaDB Backup in MariaDB Community Server 10.4 and later will block writes, log tables, and statistics.
* Older MariaDB Community Server releases used `FLUSH TABLES WITH READ LOCK`, which closed open tables and only allowed tables to be reopened with a read lock during the duration of backups.

## **Understanding Recovery**

MariaDB Backup creates complete or incremental backups of MariaDB Server data, and is also used to restore data from backups produced using MariaDB Backup.

### **Preparing Backups for Recovery**

Full backups produced using MariaDB Server are not initially point-in-time consistent, and an attempt to restore from a raw full backup will cause InnoDB to crash to protect the data.

Incremental backups produced using MariaDB Backup contain only the changes since the last backup and cannot be used standalone to perform a restore.

To restore from a backup, you first need to prepare the backup for point-in-time consistency using the `--prepare` command:

* Running the `--prepare` command on a _full backup_ synchronizes the tablespaces, ensuring that they are point-in-time consistent and ready for use in recovery.
* Running the `--prepare` command on an _incremental backup_ synchronizes the tablespaces and also applies the updated data into the previous full backup, making it a complete backup ready for use in recovery.
* Running the `--prepare` command on data that is to be used for a _partial restore_ (when restoring only one or more selected tables) requires that you also use the `--export` option to create the necessary `.cfg` files to use in recovery.

### **Restore Requires Empty Data Directory**

When MariaDB Backup restores from a backup, it copies or moves the backup files into the MariaDB Server data directory, as defined by the `datadir` system variable.

For MariaDB Backup to safely restore data from full and incremental backups, the data directory must be empty. One way to achieve this is to move the data directory aside to a unique directory name:

{% stepper %}
{% step %}
Make sure that the Server is stopped.
{% endstep %}

{% step %}
Move the data directory to a unique name (for example, `/var/lib/mysql-2020-01-01`) **or** remove the old data directory (depending on how much space you have available).
{% endstep %}

{% step %}
Create a new (empty) data directory (for example, `mkdir /var/lib/mysql`).
{% endstep %}

{% step %}
Run MariaDB Backup to restore the databases into that directory.
{% endstep %}

{% step %}
Change the ownership of all the restored files to the correct system user (for example, `chown -R mysql:mysql /var/lib/mysql`).
{% endstep %}

{% step %}
Start MariaDB Server, which now uses the restored data directory.
{% endstep %}

{% step %}
When ready, and if you have not already done so, delete the old data directory to free disk space.
{% endstep %}
{% endstepper %}

## **Creating the Backup User**

When MariaDB Backup performs a backup operation, it not only copies files from the data directory but also connects to the running MariaDB Server.

This connection to MariaDB Server is used to manage locks and backup staging that prevent the Server from writing to a file while being read for a backup.

MariaDB Backup establishes this connection based on the user credentials specified with the `--user` and `--password` options when performing a backup.

It is recommended that a dedicated user be created and authorized to perform backups.

### **User Privileges**

MariaDB Backup requires this user to have the `RELOAD`, `PROCESS`, `LOCK TABLES`, and `BINLOG MONITOR` privileges:

```sql
CREATE USER 'mariabackup'@'localhost'IDENTIFIED BY 'mbu_passwd';
GRANT RELOAD, PROCESS, LOCK TABLES, BINLOG MONITOR
      ON * 
      TO 'mariabackup'@'localhost';
```

In the above example, MariaDB Backup would run on the local system that runs MariaDB Server. Where backups may be run against a remote server, the user authentication and authorization should be adjusted.

While MariaDB Backup requires a user for backup operations, no user is required for restore operations since restores occur while MariaDB Server is not running.

## **Full Backup and Restore**

Full backups performed with MariaDB Backup contain all table data present in the database.

When performing a full backup, MariaDB Backup makes a file-level copy of the MariaDB Server data directory. This backup omits log data such as the binary logs (binlog), error logs, general query logs, and slow query logs.

### **Performing Full Backups**

When you perform a full backup, MariaDB Backup writes the backup to the `--target-dir` path. The directory must be empty or non-existent and the operating system user account must have permission to write to that directory. A database user account is required to perform the backup.

The version of `mariabackup` or `mariadb-backup` should be the same version as the MariaDB Server version. When the version does not match the server version, errors can sometimes occur, or the backup can sometimes be unusable.

To create a backup, execute `mariabackup` or `mariadb-backup` with the `--backup` option, and provide the database user account credentials using the `--user` and `--password` options:

`$ sudo mariabackup --backup \ --target-dir=/data/backups/full \ --user=mariabackup \ --password=mbu_passwd`

Subsequent to the above example, the backup is now available in the designated `--target-dir` path.

### **Preparing a Full Backup for Recovery**

A raw full backup is not [point-in-time consistent](mariadb-backup.md#point-in-time-recovery) and must be prepared before it can be used for a restore. The backup can be prepared any time after the backup is created and before the backup is restored. However, MariaDB recommends preparing a backup immediately after taking the backup to ensure that the backup is consistent.

The backup should be prepared with the same version of MariaDB Backup that was used to create the backup.

To prepare the backup, execute `mariabackup` or `mariadb-backup` with the `--prepare` option:

`$ sudo mariabackup --prepare \ --use-memory=34359738368 \ --target-dir=/data/backups/full`

For best performance, the `--use-memory option` should be set to the server's [innodb\_buffer\_pool\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_size) value.

### **Restoring from Full Backups**

Once a full backup has been [prepared](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview) to be point-in-time consistent, MariaDB Backup is used to copy backup data to the MariaDB Server data directory.

To restore from a full backup:

1. Stop the MariaDB Server.
2. [Empty](https://mariadb.com/docs/server/data-operations/backups/community-server/mariadb-backup/#Restore_Requires_Empty_Data_Directory) the data directory.
3.  Restore from the "full" directory using the `--copy-back` option:

    `$ sudo mariabackup --copy-back --target-dir=/data/backups/full`

MariaDB Backup writes to the data directory as the current user, which can be changed using `sudo`. To confirm that restored files are properly owned by the user that runs MariaDB Server, run a command like this (adapted for the correct user/group):

`$ sudo chown -R mysql:mysql /var/lib/mysql`

Once this is done, start MariaDB Server:

`$ sudo systemctl start mariadb`

When the Server starts, it works from the restored data directory.

## **Incremental Backup and Restore**

Full backups of large data-sets can be time-consuming and resource-intensive. MariaDB Backup supports the use of incremental backups to minimize this impact.

While full backups are resource-intensive at time of backup, the resource burden around incremental backups occurs when preparing for restore. First, the full backup is prepared for restore, then each incremental backup is applied.

### **Performing Incremental Backups**

When you perform an incremental backup, MariaDB Backup compares a previous full or incremental backup to what it finds on MariaDB Server. It then creates a new backup containing the incremental changes.

Incremental backup is supported for InnoDB tables. Tables using other storage engines receive full backups even during incremental backup operations.

To increment a full backup, use the `--incremental-basedir` option to indicate the path to the full backup and the `--target-dir` option to indicate where you want to write the incremental backup:

`$ sudo mariabackup --backup \ --incremental-basedir=/data/backups/full \ --target-dir=/data/backups/inc1 \ --user=mariabackup \ --password=mbu_passwd`

In this example, MariaDB Backup reads the `/data/backups/full` directory, and MariaDB Server then creates an incremental backup in the `/data/backups/inc1` directory.

### **Preparing an Incremental Backup**

An incremental backup must be applied to a prepared full backup before it can be used in a restore operation. If you have multiple full backups to choose from, pick the nearest full backup prior to the incremental backup that you want to restore. You may also want to back up your full-backup directory, as it will be modified by the updates in the incremental data.

If your full backup directory is not yet prepared, run this to make it consistent:

`$ sudo mariabackup --prepare --target-dir=/data/backups/full`

Then, using the prepared full backup, apply the first incremental backup's data to the full backup in an incremental preparation step:

`$ sudo mariabackup --prepare \ --target-dir=/data/backups/full \ --incremental-dir=/data/backups/inc1`

Once the incremental backup has been applied to the full backup, the full backup directory contains the changes from the incremental backup (that is, the `inc1/` directory). Feel free to remove `inc1/` to save disk space.

### **Restoring from Incremental Backups**

Once you have prepared the full backup directory with all the incremental changes you need (as described above), stop the MariaDB Server, [empty](https://mariadb.com/docs/server/data-operations/backups/community-server/mariadb-backup/#Restore_Requires_Empty_Data_Directory) its data directory, and restore from the original full backup directory using the `--copy-back` option:

`$ sudo mariabackup --copy-back --target-dir=/data/backups/full`

MariaDB Backup writes files into the data directory using either the current user or root (in the case of a sudo operation), which may be different from the system user that runs the database. Run the following to recursively update the ownership of the restored files and directories:

`$ sudo chown -R mysql:mysql /var/lib/mysql`

Then, start MariaDB Server. When the Server starts, it works from the restored data directory.

The details of the restore procedure depend on the characteristics of the table:

* [Partial Restore Non-partitioned Tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/partial-backup-and-restore-with-mariadb-backup#restoring-individual-non-partitioned-tables)
* [Partial Restore Partitioned Tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/partial-backup-and-restore-with-mariadb-backup#restoring-individual-partitions-and-partitioned-tables)
* [Partial Restore of Tables with Full-Text Indexes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/partial-backup-and-restore-with-mariadb-backup#restoring-the-backup)

As partial restores are performed while the server is running, not stopped, care should be taken to prevent production workloads during restore activity.

{% hint style="info" %}
You can also use data from a full backup in a partial restore operation if you have prepared the data using the `--export` option as described above.
{% endhint %}

### **Partial Restore Non-partitioned Tables**

To restore a non-partitioned table from a backup, first create a new table on MariaDB Server to receive the restored data. It should match the specifications of the table you're restoring.

Be extra careful if the backup data is from a server with a different version than the restore server, as some differences (such as a differing `ROW_FORMAT`) can cause an unexpected result.

{% stepper %}
{% step %}
Create an empty table for the data being restored:

```sql
CREATE TABLE test.address_book 
       (id INT PRIMARY KEY AUTO_INCREMENT, 
        name VARCHAR(255), 
        email VARCHAR(255));
```
{% endstep %}

{% step %}
Modify the table to discard the tablespace:

```sql
ALTER TABLE test.address_book DISCARD TABLESPACE;
```
{% endstep %}

{% step %}
You can copy or move the files for the table from the backup to the data directory:

```bash
$ sudo cp /data/backups/part_inc1/test/address_book.* /var/lib/mysql/test
```
{% endstep %}

{% step %}
Use a wildcard to include both the `.ibd` and `.cfg` files. Then, change the owner to the system user running MariaDB Server:

```bash
$ sudo chown mysql:mysql /var/lib/mysql/test/address_book.*
```
{% endstep %}

{% step %}
Import the new tablespace:

```sql
ALTER TABLE test.address_book IMPORT TABLESPACE;
```

MariaDB Server looks in the data directory for the tablespace you copied in, then imports it for use. If the table is encrypted, it also looks for the encryption key with the relevant key ID that the table data specifies.
{% endstep %}

{% step %}
Repeat this step for every table you wish to restore.
{% endstep %}
{% endstepper %}

### **Partial Restore Partitioned Tables**

Restoring a partitioned table from a backup requires a few extra steps compared to restoring a non-partitioned table.

To restore a partitioned table from a backup, first create a new table on MariaDB Server to receive the restored data. It should match the specifications of the table you're restoring, including the partition specification.

Be extra careful if the backup data is from a server with a different version than the restore server, as some differences (such as a differing `ROW_FORMAT`) can cause an unexpected result.

{% stepper %}
{% step %}
Create an empty table for the data being restored:

```sql
CREATE TABLE test.students 
      (id INT NOT NULL AUTO_INCREMENT,
       name VARCHAR(255), email VARCHAR(255),
       graduating_year YEAR)
       PRIMARY KEY (id, graduating_year)) 
       ENGINE = InnoDB
       PARTITION BY RANGE(graduating_year) 
                (PARTITION p0 VALUES LESS THAN (2019),
                 PARTITION p1 VALUES LESS THAN MAXVALUE);
```
{% endstep %}

{% step %}
Create a second empty table matching the column specification, but without partitions. This will be your working table:

```sql
CREATE TABLE test.students_work AS
       SELECT * FROM test.students WHERE NULL;
```
{% endstep %}

{% step %}
For each partition you want to restore, discard the working table's tablespace:

```sql
ALTER TABLE test.students_work DISCARD TABLESPACE;
```
{% endstep %}

{% step %}
Copy the table files from the backup, using the new name:

```bash
$ sudo cp /data/backups/part_inc1/test/students.ibd \
/var/lib/mysql/test/students_work.ibd $ 
sudo cp /data/backups/part_inc1/test/students.cfg \
/var/lib/mysql/test/students_work.cfg
```
{% endstep %}

{% step %}
Change the owner to that of the user running MariaDB Server:

```bash
$ sudo chown mysql:mysql /var/lib/mysql/test/students_work.*
```
{% endstep %}

{% step %}
Import the copied tablespace:

```sql
ALTER TABLE test.students_work IMPORT TABLESPACE;
```
{% endstep %}

{% step %}
Exchange the partition, copying the tablespace from the working table into the partition file for the target table:

```sql
ALTER TABLE test.students 
      EXCHANGE PARTITION p0 WITH TABLE test.students_work;
```
{% endstep %}

{% step %}
Repeat the above process for each partition until you have them all exchanged into the target table. Then delete the working table, as it's no longer necessary:

```sql
DROP TABLE test.students_work;
```

This restores a partitioned table.
{% endstep %}
{% endstepper %}

### **Partial Restore of Tables With Full-Text Indexes**

When restoring a table with a full-text search (FTS) index, InnoDB may throw a schema mismatch error.

In this case, to restore the table, it is recommended to:

* Remove the corresponding `.cfg` file.
* Restore data to a table without any secondary indexes including FTS.
* Add the necessary secondary indexes to the restored table.

For example, to restore table `t1` with FTS index from database `db1`:

{% stepper %}
{% step %}
In the [MariaDB Command-Line Client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mariadb-command-line-client), drop the table you are going to restore:

```sql
DROP TABLE IF EXISTS db1.t1;
```
{% endstep %}

{% step %}
Create an empty table for the data being restored:

```sql
CREATE TABLE db1.t1(f1 CHAR(10)) ENGINE=INNODB;
```
{% endstep %}

{% step %}
Modify the table to discard the tablespace:

```sql
ALTER TABLE db1.t1 DISCARD TABLESPACE;
```
{% endstep %}

{% step %}
In the operating system shell, copy the table files from the backup to the data directory of the corresponding database:

```bash
$ sudo cp /data/backups/part/db1/t1.* /var/lib/mysql/db1
```
{% endstep %}

{% step %}
Remove the `.cfg` file from the data directory:

```bash
$ sudo rm /var/lib/mysql/db1/t1.cfg
```
{% endstep %}

{% step %}
Change the owner of the newly copied files to the system user running MariaDB Server:

```
$ sudo chown mysql:mysql /var/lib/mysql/db1/t1.*
```
{% endstep %}

{% step %}
In the MariaDB Command-Line Client, import the copied tablespace:

```sql
ALTER TABLE  db1.t1 IMPORT TABLESPACE;
```
{% endstep %}

{% step %}
Verify that the data has been successfully restored:

```sql
SELECT * FROM db1.t1;
```
{% endstep %}

{% step %}
Add the necessary secondary indexes:

```sql
ALTER TABLE db1.t1 FORCE, ADD FULLTEXT INDEX f_idx(f1);
```
{% endstep %}

{% step %}
The table is now fully restored:

```sql
SHOW CREATE TABLE db1.t1\G
*************************** 1. row ***************************
       Table: t1
Create Table: CREATE TABLE `t1` (
  `f1` char(10) DEFAULT NULL,
  FULLTEXT KEY `f_idx` (`f1`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```
{% endstep %}
{% endstepper %}

## **Point-In-Time Recovery**

Recovering from a backup restores the data directory at a specific point-in-time, but it does not restore the binary log. In a point-in-time recovery, you begin by restoring the data directory from a full or incremental backup, then use the `mysqlbinlog` utility to recover the binary log data to a specific point in time.

{% stepper %}
{% step %}
Prepare the backup as you normally would for a [full](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/full-backup-and-restore-with-mariadb-backup) or [incremental](mariadb-backup.md#incremental-backup-and-restore) backup:

```bash
$ sudo mariabackup --prepare --target-dir=/data/backups/full
```
{% endstep %}

{% step %}
When MariaDB Backup runs on a MariaDB Server where binary logs are enabled, it stores binary log information in the `xtrabackup_binlog_info` file. Consult this file to find the name of the binary log position to use. In the following example, the log position is `321` :

```bash
$ sudo cat /data/backups/full/xtraback_binlog_info
mariadb-node4.00001 321`
```
{% endstep %}

{% step %}
Update the configuration file to use a new data directory:

```ini
[mariadbd]
datadir=/var/lib/mysql_new
```
{% endstep %}

{% step %}
Using [MariaDB Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup), restore from the backup to the new data directory:

```bash
$ sudo mariadb-backup --copy-back --target-dir=/data/backups/full
```
{% endstep %}

{% step %}
Change the owner to the MariaDB Server system user:

```bash
$ sudo chown -R mysql:mysql /var/lib/mysql_new
```
{% endstep %}

{% step %}
Start MariaDB Server:

```bash
$ sudo systemctl start mariadb
```
{% endstep %}

{% step %}
Using the binary log file in the old data directory, the start position in the binary log file, the date and time you want to restore to, and the [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) utility to create an SQL file with the binary log changes:

```bash
$ mariadb-binlog --start-position=321 \ 
              --stop-datetime="2019-06-28 12:00:00" \ 
              /var/lib/mysql/mariadb-node4.00001 > mariadb-binlog.sql
```
{% endstep %}

{% step %}
Run the binary log SQL to restore the databases:

```bash
$ mysql -u root -p < mariadb-binlog.sql
```
{% endstep %}
{% endstepper %}
