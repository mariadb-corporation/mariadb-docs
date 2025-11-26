---
description: >-
  Reference guide for mariadb-backup command-line options. Explore parameters
  for backup, prepare, copy-back, and restore operations.
---

# mariadb-backup Options

{% include "../../../.gitbook/includes/mariadb-backup-was-previous....md" %}

## List of `mariadb-backup` Options

### `--apply-log`

Prepares an existing backup to restore to the MariaDB Server. This is only valid in `innobackupex` mode, which can be enabled with the [--innobackupex](mariadb-backup-options.md#innobackupex) option.

Files that `mariadb-backup` generates during [--backup](mariadb-backup-options.md#backup) operations in the target directory are not ready for use on the Server. Before you can restore the data to MariaDB, you first need to prepare the backup.

In the case of full backups, the files are not point in time consistent, since they were taken at different times. If you try to restore the database without first preparing the data, InnoDB rejects the new data as corrupt. Running `mariadb-backup` with the [--prepare](mariadb-backup-options.md#prepare) command readies the data so you can restore it to MariaDB Server. When working with incremental backups, you need to use the `--prepare` command and the [--incremental-dir](mariadb-backup-options.md#incremental-dir) option to update the base backup with the deltas from an incremental backup.

```bash
mariadb-backup --innobackupex --apply-log
```

Once the backup is ready, you can use the [--copy-back](mariadb-backup-options.md#copy-back) or the [--move-back](mariadb-backup-options.md#move-back) commands to restore the backup to the server.

### `--apply-log-only`

If this option is used when preparing a backup, then only the redo log apply stage are performed, and other stages of crash recovery are ignored. This option is used with incremental backups.

{% hint style="danger" %}
**Note:** This option is not needed or supported anymore.
{% endhint %}

### `--backup`

Backs up your databases.

Using this command option, `mariadb-backup` performs a backup operation on your database or databases. The backups are written to the target directory, as set by the [--target-dir](mariadb-backup-options.md#target-dir) option.

```bash
mariadb-backup --backup 
      --target-dir /path/to/backup \
      --user user_name --password user_passwd
```

`mariadb-backup` can perform full and incremental backups. A full backup creates a snapshot of the database in the target directory. An incremental backup checks the database against a previously taken full backup, (defined by the [--incremental-basedir](mariadb-backup-options.md#incremental-basedir) option) and creates delta files for these changes.

In order to restore from a backup, you first need to run `mariadb-backup` with the `--prepare` option, to make a full backup point-in-time consistent or to apply incremental backup deltas to base. Then you can run `mariadb-backup` again with either the [--copy-back](mariadb-backup-options.md#copy-back) or [--move-back](mariadb-backup-options.md#move-back) commands to restore the database.

For more information, see [Full Backup and Restore](full-backup-and-restore-with-mariadb-backup.md) and [Incremental Backup and Restore](incremental-backup-and-restore-with-mariadb-backup.md).

### `--binlog-info`

Defines how `mariadb-backup` retrieves the binary log coordinates from the server.

```bash
--binlog-info[=OFF | ON | LOCKLESS | AUTO]
```

The `--binlog-info` option supports the following retrieval methods. When no retrieval method is provided, it defaults to `AUTO`.

| Option     | Description                                                                                             |
| ---------- | ------------------------------------------------------------------------------------------------------- |
| `OFF`      | Disables the retrieval of binary log information                                                        |
| `ON`       | Enables the retrieval of binary log information, performs locking where available to ensure consistency |
| `LOCKLESS` | Unsupported option                                                                                      |
| `AUTO`     | Enables the retrieval of binary log information using `ON` or `LOCKLESS` where supported                |

Using this option, you can control how `mariadb-backup` retrieves the server's binary log coordinates corresponding to the backup.

When enabled, whether using `ON` or `AUTO`, `mariadb-backup` retrieves information from the binlog during the backup process. When disabled with `OFF`, `mariadb-backup` runs without attempting to retrieve binary log information. You may find this useful when you need to copy data without metadata like the binlog or replication coordinates.

```bash
mariadb-backup --binlog-info --backup
```

Currently, the `LOCKLESS` option depends on features unsupported by MariaDB Server. See the description of the [xtrabackup\_binlog\_pos\_innodb](files-created-by-mariadb-backup.md#xtrabackup_binlog_pos_innodb) file for more information. If you attempt to run `mariadb-backup` with this option, then it causes the utility to exit with an error.

### `--close-files`

Defines whether you want to close file handles.

Using this option, you can tell `mariadb-backup` that you want to close file handles. Without this option, `mariadb-backup` keeps files open in order to manage DDL operations. When working with particularly large tablespaces, closing the file can make the backup more manageable. However, it can also lead to inconsistent backups. Use at your own risk.

```bash
mariadb-backup --close-files --prepare
```

### `--compress`

{% hint style="warning" %}
This option was deprecated as it relies on the no longer maintained [QuickLZ](https://github.com/RT-Thread-packages/quicklz/) library. It are removed in a future release - versions supporting this function will not be affected. It is recommended to instead backup to a stream (stdout), and use a 3rd party compression library to compress the stream, as described in [Using Encryption and Compression Tools With mariadb-backup](using-encryption-and-compression-tools-with-mariadb-backup.md).
{% endhint %}

Defines the compression algorithm for backup files.

```bash
--compress[=compression_algorithm]
```

The `--compress` option only supports the now deprecated `quicklz` algorithm.

| Option    | Description                            |
| --------- | -------------------------------------- |
| `quicklz` | Uses the QuickLZ compression algorithm |

```bash
mariadb-backup --compress --backup
```

If a backup is compressed using this option, then `mariadb-backup` will record that detail in the [xtrabackup\_info](files-created-by-mariadb-backup.md#xtrabackup_info) file.

### `--compress-chunk-size`

{% hint style="warning" %}
Deprecated, for details see the [--compress](mariadb-backup-options.md#compress) option.
{% endhint %}

Defines the working buffer size for compression threads.

```bash
--compress-chunk-size=#
```

`mariadb-backup` can perform compression operations on the backup files before writing them to disk. It can also use multiple threads for parallel data compression during this process. Using this option, you can set the chunk size each thread uses during compression. It defaults to `64K`.

```bash
mariadb-backup --backup --compress \
     --compress-threads=12 --compress-chunk-size=5M
```

To further configure backup compression, see the [--compress](mariadb-backup-options.md#compress) and [--compress-threads](mariadb-backup-options.md#compress-threads) options.

### `--compress-threads`

{% hint style="warning" %}
Deprecated, for details see the [--compress](mariadb-backup-options.md#compress) option.
{% endhint %}

Defines the number of threads to use in compression.

```
--compress-threads=#
```

`mariadb-backup` can perform compression operations on the backup files before writing them to disk. Using this option, you can define the number of threads you want to use for this operation. You may find this useful in speeding up the compression of particularly large databases. It defaults to single-threaded.

```
mariadb-backup --compress --compress-threads=12 --backup
```

To further configure backup compression, see the [--compress](mariadb-backup-options.md#compress) and [--compress-chunk-size](mariadb-backup-options.md#compress-chunk-size) options.

### `--copy-back`

Restores the backup to the data directory.

Using this command, `mariadb-backup` copies the backup from the target directory to the data directory, as defined by the `--datadir` option. You must stop the MariaDB Server before running this command. The data directory must be empty. If you want to overwrite the data directory with the backup, use the `--force-non-empty-directories` option.

Bear in mind, before you can restore a backup, you first need to run mariadb-backup with the --prepare option. In the case of full backups, this makes the files point-in-time consistent. With incremental backups, this applies the deltas to the base backup. Once the backup is prepared, you can run `--copy-back` to apply it to MariaDB Server.

```bash
mariadb-backup --copy-back --force-non-empty-directories
```

Running the `--copy-back` command copies the backup files to the data directory. Use this command if you want to save the backup for later. If you don't want to save the backup for later, use the `--move-back` option.

### `--core-file`

Defines whether to write a core file.

Using this option, you can configure `mariadb-backup` to dump its core to file in the event that it encounters fatal signals. You may find this useful for review and debugging purposes.

```bash
mariadb-backup --core-file --backup
```

### `--databases`

Defines the databases and tables you want to back up.

```
--databases="database[.table][ database[.table] ...]"
```

Using this option, you can define the specific database or databases you want to back up. In cases where you have a particularly large database or otherwise only want to back up a portion of it, you can optionally also define the tables on the database.

```bash
mariadb-backup --backup \
      --databases="example.table1 example.table2"
```

In cases where you want to back up most databases on a server or tables on a database, but not all, you can set the specific databases or tables you don't want to back up using the `--databases-exclude` option.

If a backup is a partial backup, then mariadb-backup will record that detail in the `xtrabackup_info` file.

In `innobackupex` mode, which can be enabled with the `--innobackupex` option, the `--databases` option can be used as described above, or it can be used to refer to a file, just as the [--databases-file](https://mariadb.com/kb/en/-databases-file) option can in the normal mode.

### `--databases-exclude`

Defines the databases you don't want to back up.

```
--databases-exclude="database[.table][ database[.table] ...]"
```

Using this option, you can define the specific database or databases you want to exclude from the backup process. You may find it useful when you want to back up most databases on the server or tables on a database, but would like to exclude a few from the process.

```bash
mariadb-backup --backup \
      --databases="example" \
      --databases-exclude="example.table1 example.table2"
```

To include databases in the backup, see the `--databases` option option.

If a backup is a partial backup, then `mariadb-backup` records that detail in the `xtrabackup_info` file.

### `--databases-file`

Defines the path to a file listing databases and/or tables you want to back up.

```bash
--databases-file="/path/to/database-file"
```

Format the databases file to list one element per line, with the following syntax:

```bash
database[.table]
```

In cases where you need to back up a number of databases or specific tables in a database, you may find the syntax for the `--databases` and `--databases-exclude` options a little cumbersome. Using this option you can set the path to a file listing the databases or databases and tables you want to back up.

For instance, listing the databases and tables for a backup in a file called `main-backup`:

```bash
cat main-backup
```

```
example1
example2.table1
example2.table2
```

```bash
mariadb-backup --backup --databases-file=main-backup
```

If a backup is a partial backup, `mariadb-backup` records that detail in the `xtrabackup_info` file.

### `-h, --datadir`

Defines the path to the database root.

```bash
--datadir=PATH
```

Using this option, you can define the path to the source directory. This is the directory that `mariadb-backup` reads for the data it backs up. It should be the same as the MariaDB Server `datadir` system variable.

```
mariadb-backup --backup -h /var/lib64/mysql
```

### `--debug-sleep-before-unlock`

This is a debug-only option used by the Xtrabackup test suite.

### `--decompress`

Deprecated, for details see the `--compress` option.

This option requires that you have the `qpress` utility installed on your system.

Defines whether you want to decompress previously compressed backup files.

When you run mariadb-backup with the `--compress` option, it compresses the subsequent backup files, using the QuickLZ algorithm. Using this option, `mariadb-backup` decompresses the compressed files from a previous backup.

For instance, run a backup with compression:

```bash
mariadb-backup --compress --backup
```

Then, decompress the backup:

```bash
mariadb-backup --decompress
```

You can enable the decryption of multiple files at a time using the `--parallel` option. By default, mariadb-backup does not remove the compressed files from the target directory. To delete these files, use the `--remove-original` option.

### `--debug-sync`

Defines the debug sync point. This option is only used by the `mariadb-backup` test suite.

### `--defaults-extra-file`

Defines the path to an extra default option file.

```
--defaults-extra-file=/path/to/config
```

Using this option, you can define an extra default option file for `mariadb-backup`. Unlike `--defaults-file`, this file is read after the default option files are read, allowing you to only overwrite the existing defaults.

```bash
mariadb-backup --backup \
      --defaults-file-extra=addition-config.cnf \
      --defaults-file=config.cnf
```

### `--defaults-file`

Defines the path to the default option file.

```
--defaults-file=/path/to/config
```

Using this option, you can define a default option file for `mariadb-backup`. Unlike the `--defaults-extra-file` option, when this option is provided, it completely replaces all default option files.

```bash
mariadb-backup --backup \
     --defaults-file=config.cnf
```

### `--defaults-group`

Defines the option group to read in the option file.

```bash
--defaults-group="name"
```

In situations where you find yourself using certain `mariadb-backup` options consistently every time you call it, you can set the options in an option file. The `--defaults-group` option defines what option group `mariadb-backup` reads for its options.

Options you define from the command-line can be set in the configuration file using minor formatting changes. For instance, if you find yourself perform compression operations frequently, you might set `--compress-threads` and `--compress-chunk-size` options in this way:

```
[mariadb-backup]
compress_threads = 12
compress_chunk_size = 64K
```

Now whenever you run a backup with the `--compress` option, it always performs the compression using 12 threads and 64K chunks.

```bash
mariadb-backup --compress --backup
```

See [mariadb-backup Overview: Server Option Groups](mariadb-backup-overview.md#server-option-groups) and [mariadb-backup Overview: Client Option Groups](mariadb-backup-overview.md#client-option-groups) for a list of the option groups read by `mariadb-backup` by default.

### `--encrypted-backup`

When this option is used with `--backup`, if `mariadb-backup` encounters a page that has a non-zero `key_version` value, then mariadb-backup assumes that the page is encrypted.

Use `--skip-encrypted-backup` instead to allow mariadb-backup to copy unencrypted tables that were originally created before MySQL 5.1.48.

### `--export`

If this option is provided during the `--prepare` stage, then it tells `mariadb-backup` to create `.cfg` files for each InnoDB file-per-table tablespace. These `.cfg` files are used to import transportable tablespaces in the process of restoring partial backups and restoring individual tables and partitions.

The `--export` option could require rolling back incomplete transactions that had modified the table. This will likely create a "new branch of history" that does not correspond to the server that had been backed up, which makes it impossible to apply another incremental backup on top of such additional changes. The option should only be applied when doing a `--prepare` of the last incremental.

```bash
mariadb-backup --prepare --export
```

`mariadb-backup` did not support the `--export` option. See [MDEV-13466](https://jira.mariadb.org/browse/MDEV-13466) about that. In earlier versions of MariaDB, this means that mariadb-backup could not create `.cfg` files for InnoDB file-per-table tablespaces during the `--prepare` stage. You can still import file-per-table tablespaces without the `.cfg` files in many cases, so it may still be possible in those versions to restore partial backups or to restore individual tables and partitions with just the `.ibd` files. If you have a full backup and you need to create `.cfg` files for InnoDB file-per-table tablespaces, then you can do so by preparing the backup as usual without the `--export` option, and then restoring the backup, and then starting the server. At that point, you can use the server's built-in features to copy the transportable tablespaces.

### `--extra-lsndir`

Saves an extra copy of the `xtrabackup_checkpoints` and `xtrabackup_info` files into the given directory.

```bash
--extra-lsndir=PATH
```

When using the `--backup` option, `mariadb-backup` produces a number of backup files in the target directory. Using this option, you can have `mariadb-backup` produce additional copies of the `xtrabackup_checkpoints` and `xtrabackup_info` files in the given directory.

```bash
mariadb-backup --extra-lsndir=extras/ --backup
```

This is especially useful when using `--stream` for streaming output, e.g. for compression and/or encryption using external tools in combination with incremental backups, as the `xtrabackup_checkpoints` file necessary to determine the LSN to continue the incremental backup from is still accessible without uncompressing / decrypting the backup file first. Pass in the `--extra-lsndir` of the previous backup as `--incremental-basedir` .

### `--force-non-empty-directories`

Allows `--copy-back` or `--move-back` options to use non-empty target directories.

When using `mariadb-backup` with the `--copy-back` or `--move-back` options, they normally require a non-empty target directory to avoid conflicts. Using this option with either of command allows `mariadb-backup` to use a non-empty directory.

```bash
mariadb-backup --force-non-empty-directories --copy-back
```

Bear in mind that this option does not enable overwrites. When copying or moving files into the target directory, if `mariadb-backup` finds that the target file already exists, it fails with an error.

### `--ftwrl-wait-query-type`

Defines the type of query allowed to complete before `mariadb-backup` issues the global lock.

```bash
--ftwrl-wait-query-type=[ALL | UPDATE | SELECT]
```

The `--ftwrl-wait-query-type` option supports the following query types. The default value is `ALL`.

| Option | Description                                                           |
| ------ | --------------------------------------------------------------------- |
| ALL    | Waits until all queries complete before issuing the global lock       |
| SELECT | Waits until SELECT statements complete before issuing the global lock |
| UPDATE | Waits until UPDATE statements complete before issuing the global lock |

When `mariadb-backup` runs, it issues a global lock to prevent data from changing during the backup process. When it encounters a statement in the process of executing, it waits until the statement is finished before issuing the global lock. Using this option, you can modify this default behavior to ensure that it waits only for certain query types, such as for `SELECT` and `UPDATE` statements.

```bash
mariadb-backup --backup  \
      --ftwrl-wait-query-type=UPDATE
```

### `--ftwrl-wait-threshold`

Defines the minimum threshold for identifying long-running queries for FTWRL.

```bash
--ftwrl-wait-threshold=#
```

When `mariadb-backup` runs, it issues a global lock to prevent data from changing during the backup process and ensure a consistent record. If it encounters statements still in the process of executing, it waits until they complete before setting the lock. Using this option, you can set the threshold at which mariadb-backup engages FTWRL[^1]. When it `--ftwrl-wait-timeout` is not 0 and a statement has run for at least the amount of time given this argument, mariadb-backup waits until the statement completes or until the `--ftwrl-wait-timeout` expires before setting the global lock and starting the backup.

```bash
mariadb-backup --backup \
     --ftwrl-wait-timeout=90 \
     --ftwrl-wait-threshold=30
```

### `--ftwrl-wait-timeout`

Defines the timeout to wait for queries before trying to acquire the global lock. The global lock refers to `BACKUP STAGE BLOCK_COMMIT`. The global lock refers to `FLUSH TABLES WITH READ LOCK` (FTWRL).

```bash
--ftwrl-wait-timeout=#
```

When `mariadb-backup` runs, it acquires a global lock to prevent data from changing during the backup process and ensure a consistent record. If it encounters statements still in the process of executing, it can be configured to wait until the statements complete before trying to acquire the global lock.

If the `--ftwrl-wait-timeout` is set to 0, `mariadb-backup` tries to acquire the global lock immediately without waiting. This is the default value.

If the `--ftwrl-wait-timeout` is set to a non-zero value, then `mariadb-backup` waits for the configured number of seconds until trying to acquire the global lock.

`mariadb-backup` exits if it can't acquire the global lock after waiting for the configured number of seconds.

```bash
mariadb-backup --backup \
      --ftwrl-wait-query-type=UPDATE \
      --ftwrl-wait-timeout=5
```

The `--ftwrl-wait-timeout` option specifies the maximum time that `mariadb-backup` will wait to obtain the global lock required to begin a consistent backup.

{% tabs %}
{% tab title="From MariaDB 10.4" %}
this lock is acquired with **`BACKUP STAGE BLOCK_COMMIT`**.
{% endtab %}

{% tab title="Before 10.4" %}
this lock is acquired with **`FLUSH TABLES WITH READ LOCK (FTWRL)`**.
{% endtab %}
{% endtabs %}

If the lock cannot be obtained within the configured timeout, the backup process fails.

This option helps avoid failures caused by long-running MariaDB queries that block backup locks.

**Example Errors**

When the timeout is not set appropriately, backups may fail with messages such as:

```vbnet
Unable to obtain lock. Please try again later.
```

or

```vbnet
FATAL ERROR: failed to execute query BACKUP STAGE START:
Lock wait timeout exceeded; try restarting transaction
```

Example log excerpt:

```vbnet
[00] 2022-02-08 15:43:25 Unable to obtain lock. Please try again later.
[00] 2022-02-08 15:43:25 Error on BACKUP STAGE START query execution
mariabackup: Stopping log copying thread.
```

Originally, `mariadb-backup` could wait indefinitely for the lock. Starting with the fix for MDEV-20230:

* The `--ftwrl-wait-timeout` option also ensures mariadb backup exits gracefully if the lock cannot be obtained within the timeout period.
* This prevents backups from hanging when lock acquisition is blocked by long-running queries.

**When to Use**

Use `--ftwrl-wait-timeout` when:

* Your workload includes long-running queries (for example, `ALTER TABLE` or large `INSERT` batches).
* Backups sometimes fail with lock wait timeout errors.
* You want `mariadb-backup` to either wait longer for the lock or exit cleanly if it cannot be obtained.

### `--galera-info`

Defines whether you want to back up information about a Galera Cluster node's state.

When this option is used, mariadb-backup creates an additional file called `xtrabackup_galera_info`, which records information about a Galera Cluster node's state. It records the values of the [wsrep\_local\_state\_uuid](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_local_state_uuid) and [wsrep\_last\_committed](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_last_committed) status variables.

You should only use this option when backing up a Galera Cluster node. If the server is not a Galera Cluster node, then this option has no effect.

This option, when enabled and used with GTID replication, will rotate the binary logs at backup time.

```bash
mariadb-backup --backup --galera-info
```

### `--history`

{% tabs %}
{% tab title="Current" %}
Defines whether you want to track backup history in the `mysql.mariadb_backup_history` table.

```
--history[=name]
```

When using this option, `mariadb-backup` records its operation in a table on the MariaDB Server. Passing a name to this option allows you group backups under arbitrary terms for later processing and analysis.

```bash
mariadb-backup --backup --history=backup_all
```

Information is written to `mysql.mariadb_backup_history`.

`mariadb-backup` also records this in the [mariadb\_backup\_info](files-created-by-mariadb-backup.md#mariadb_backup_info) file.
{% endtab %}

{% tab title="< 10.11" %}
Defines whether you want to track backup history in the `PERCONA_SCHEMA.xtrabackup_history` table.

```
--history[=name]
```

When using this option, `mariadb-backup` records its operation in a table on the MariaDB Server. Passing a name to this option allows you group backups under arbitrary terms for later processing and analysis.

```bash
mariadb-backup --backup --history=backup_all
```

Information is written to  `PERCONA_SCHEMA.xtrabackup_history`.

`mariadb-backup`  also records this in the [xtrabackup\_info](files-created-by-mariadb-backup.md#xtrabackup_info) file.
{% endtab %}
{% endtabs %}

### `-H, --host`

Defines the host for the MariaDB Server you want to backup.

```bash
--host=name
```

Using this option, you can define the host to use when connecting to a MariaDB Server over TCP/IP. By default, `mariadb-backup` attempts to connect to the local host.

```bash
mariadb-backup --backup \
      --host="example.com"
```

### `--include`

This option is a regular expression to be matched against table names in _`databasename.tablename`_ format. It is equivalent to the `--tables` option. This is only valid in `innobackupex` mode, which can be enabled with the `--innobackupex` option.

### `--incremental`

Defines whether you want to take an increment backup, based on another backup. This is only valid in `innobackupex` mode, which can be enabled with the `--innobackupex` option.

```bash
mariadb-backup --innobackupex --incremental
```

Using this option with the `--backup` option makes the operation incremental rather than a complete overwrite. When this option is specified, either the `--incremental-lsn` or `--incremental-basedir` options can also be given. If neither option is given, `--incremental-basedir` is used by default, set to the first timestamped backup directory in the backup base directory.

```bash
mariadb-backup --innobackupex --backup --incremental \
     --incremental-basedir=/data/backups \
     --target-dir=/data/backups
```

If a backup is a incremental backup, then `mariadb-backup` records that detail in the `xtrabackup_info` file.

### `--incremental-basedir`

Defines whether you want to take an incremental backup, based on another backup.

```
--incremental-basedir=PATH
```

Using this option with the `--backup` option makes the operation incremental rather than a complete overwrite. `mariadb-backup` only copies pages from `.ibd` files if they are newer than the backup in the specified directory.

```bash
mariadb-backup --backup \
     --incremental-basedir=/data/backups \
     --target-dir=/data/backups
```

If a backup is a incremental backup, then `mariadb-backup` records that detail in the `xtrabackup_info` file.

### `--incremental-dir`

Defines whether you want to take an incremental backup, based on another backup.

```
--increment-dir=PATH
```

Using this option with `--prepare` command option makes the operation incremental rather than a complete overwrite. mariadb-backup will apply `.delta` files and log files into the target directory.

```bash
mariadb-backup --prepare \
      --increment-dir=backups/
```

If a backup is a incremental backup, then `mariadb-backup` records that detail in the `xtrabackup_info` file.

### `--incremental-force-scan`

Defines whether you want to force a full scan for incremental backups.

When using `mariadb-backup` to perform an incremental backup, this option forces it to also perform a full scan of the data pages being backed up, even when there's bitmap data on the changes. MariaDB does not support changed page bitmaps, so this option is useless in those versions. See [MDEV-18985](https://jira.mariadb.org/browse/MDEV-18985) for more information.

```bash
mariadb-backup --backup \
     --incremental-basedir=/path/to/target \
     --incremental-force-scan
```

### `--incremental-history-name`

Defines a logical name for the backup.

```bash
--incremental-history-name=name
```

`mariadb-backup` can store data about its operations on the MariaDB Server. Using this option, you can define the logical name it uses in identifying the backup.

```bash
mariadb-backup --backup \
     --incremental-history-name=morning_backup
```

The table it uses by default is named `mysql.mariadb_backup_history`. Prior to [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/what-is-mariadb-1011), the default table was `PERCONA_SCHEMA.xtrabackup_history`.

`mariadb-backup` also records this in the `xtrabackup_info` file.

### `--incremental-history-uuid`

Defines a UUID for the backup.

```bash
--incremental-history-uuid=name
```

`mariadb-backup` can store data about its operations on the MariaDB Server. Using this option, you can define the UUID it uses in identifying a previous backup to increment from. It checks `--incremental-history-name`, `--incremental-basedir`, and `--incremental-lsn`. If mariadb-backup fails to find a valid lsn, it generates an error.

```bash
mariadb-backup --backup \
      --incremental-history-uuid=main-backup012345678
```

The table it uses is named `PERCONA_SCHEMA.xtrabackup_history`, but expect that name to change in future releases. See [MDEV-19246](https://jira.mariadb.org/browse/MDEV-19246) for more information.

Table Name and Schema Changes (MariaDB 10.11):

* MariaDB 10.11 and later: Uses mysql.mariadb\_backup\_history (InnoDB).
* MariaDB 10.10 and earlier: Uses PERCONA\_SCHEMA.xtrabackup\_history (CSV).

`mariadb-backup` also records this in the `xtrabackup_info` file.

### `--incremental-lsn`

Defines the sequence number for incremental backups.

```bash
--incremental-lsn=name
```

Using this option, you can define the sequence number (LSN) value for `--backup` operations. During backups, `mariadb-backup` only copies `.ibd` pages newer than the specified values.

{% hint style="warning" %}
Incorrect LSN values can make the backup unusable. It is impossible to diagnose this issue.
{% endhint %}

### `--innobackupex`

{% hint style="info" %}
Deprecated option.
{% endhint %}

Use to enable `innobackupex` mode, which is a compatibility mode.

```bash
mariadb-backup --innobackupex
```

### `--innodb`

This option has no effect. Set only for MySQL option compatibility.

### `--innodb-adaptive-hash-index`

Enables InnoDB Adaptive Hash Index.

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option you can explicitly enable the InnoDB Adaptive Hash Index. This feature is enabled by default for mariadb-backup. If you want to disable it, use `--skip-innodb-adaptive-hash-index`.

```bash
mariadb-backup --backup \
      --innodb-adaptive-hash-index
```

### `--innodb-autoextend-increment`

Defines the increment in megabytes for auto-extending the size of tablespace file.

```bash
--innodb-autoextend-increment=36
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set the increment in megabytes for automatically extending the size of tablespace data file in InnoDB.

```bash
mariadb-backup --backup \
     --innodb-autoextend-increment=35
```

### `--innodb-buffer-pool-filename`

Using this option has no effect. It is available to provide compatibility with the MariaDB Server.

### `--innodb-buffer-pool-size`

Defines the memory buffer size InnoDB uses the cache data and indexes of the table.

```bash
--innodb-buffer-pool-size=124M
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can configure the buffer pool for InnoDB operations.

```bash
mariadb-backup --backup \
      --innodb-buffer-pool-size=124M
```

### `--innodb-checksum-algorithm`

`innodb_checksum_algorithm` has been removed.

### `--innodb-data-file-path`

Defines the path to individual data files.

```bash
--innodb-data-file-path=/path/to/file
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option you can define the path to InnoDB data files. Each path is appended to the `--innodb-data-home-dir` option.

```bash
mariadb-backup --backup \
     --innodb-data-file-path=ibdata1:13M:autoextend \
     --innodb-data-home-dir=/var/dbs/mysql/data
```

### `--innodb-data-home-dir`

Defines the home directory for InnoDB data files.

```bash
--innodb-data-home-dir=PATH
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option you can define the path to the directory containing InnoDB data files. You can specific the files using the `--innodb-data-file-path` option.

```bash
mariadb-backup --backup \
     --innodb-data-file-path=ibdata1:13M:autoextend \
     --innodb-data-home-dir=/var/dbs/mysql/data
```

### `--innodb-doublewrite`

Enables doublewrites for InnoDB tables.

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. When using this option, `mariadb-backup` improves fault tolerance on InnoDB tables with a doublewrite buffer. By default, this feature is enabled. Use this option to explicitly enable it. To disable doublewrites, use the `--skip-innodb-doublewrite` option.

```bash
mariadb-backup --backup \
     --innodb-doublewrite
```

### `--innodb-encrypt-log`

Defines whether you want to encrypt InnoDB logs.

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can tell mariadb-backup that you want to encrypt logs from its InnoDB activity.

### `--innodb-file-io-threads`

Defines the number of file I/O threads in InnoDB.

```bash
--innodb-file-io-threads=#
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the number of file I/O threads mariadb-backup uses on InnoDB tables.

```bash
mariadb-backup --backup \
     --innodb-file-io-threads=5
```

### `--innodb-file-per-table`

Defines whether you want to store each InnoDB table as an `.ibd` file.

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option causes mariadb-backup to store each InnoDB table as an `.ibd` file in the target directory.

### `--innodb-flush-method`

Defines the data flush method. Ignored from [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110).

```bash
--innodb-flush-method=fdatasync 
                     | O_DSYNC 
                     | O_DIRECT 
                     | O_DIRECT_NO_FSYNC 
                     | ALL_O_DIRECT
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the data flush method `mariadb-backup` uses with InnoDB tables.

```bash
mariadb-backup --backup \
      --innodb-flush-method==_DIRECT_NO_FSYNC
```

### `--innodb-io-capacity`

Defines the number of IOP's the utility can perform.

```bash
--innodb-io-capacity=#
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can limit the I/O activity for InnoDB background tasks. It should be set around the number of I/O operations per second that the system can handle, based on drive or drives being used.

```bash
mariadb-backup --backup \
     --innodb-io-capacity=200
```

### `--innodb-log-checksums`

Defines whether to include checksums in the InnoDB logs.

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can explicitly set `mariadb-backup` to include checksums in the InnoDB logs. The feature is enabled by default. To disable it, use the `--skip-innodb-log-checksums` option.

```bash
mariadb-backup --backup \
      --innodb-log-checksums
```

### `--innodb-log-buffer-size`

This option has no functionality in `mariadb-backup`. It exists for MariaDB Server compatibility.

### `--innodb-log-files-in-group`

This option has no functionality in `mariadb-backup`. It exists for MariaDB Server compatibility.

### `--innodb-log-group-home-dir`

Defines the path to InnoDB log files.

```bash
--innodb-log-group-home-dir=PATH
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the path to InnoDB log files.

```bash
mariadb-backup --backup \
     --innodb-log-group-home-dir=/path/to/logs
```

### `--innodb-max-dirty-pages-pct`

Defines the percentage of dirty pages allowed in the InnoDB buffer pool.

```bash
--innodb-max-dirty-pages-pct=#
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the maximum percentage of dirty, (that is, unwritten) pages that mariadb-backup allows in the InnoDB buffer pool.

```bash
mariadb-backup --backup \
     --innodb-max-dirty-pages-pct=80
```

### `--innodb-open-files`

Defines the number of files kept open at a time.

```bash
--innodb-open-files=#
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set the maximum number of files InnoDB keeps open at a given time during backups.

```bash
mariadb-backup --backup \
      --innodb-open-files=10
```

### `--innodb-page-size`

Defines the universal page size.

```bash
--innodb-page-size=#
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the universal page size in bytes for `mariadb-backup`.

```bash
mariadb-backup --backup \
     --innodb-page-size=16k
```

### `--innodb-read-io-threads`

Defines the number of background read I/O threads in InnoDB.

```bash
--innodb-read-io-threads=#
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set the number of I/O threads MariaDB uses when reading from InnoDB.

```bash
mariadb-backup --backup \
      --innodb-read-io-threads=4
```

### `--innodb-undo-directory`

Defines the directory for the undo tablespace files.

```bash
--innodb-undo-directory=PATH
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the path to the directory where you want MariaDB to store the undo tablespace on InnoDB tables. The path can be absolute.

```bash
mariadb-backup --backup \
     --innodb-undo-directory=/path/to/innodb_undo
```

### `--innodb-undo-tablespaces`

Defines the number of undo tablespaces to use.

```bash
--innodb-undo-tablespaces=#
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can define the number of undo tablespaces you want to use during the backup.

```bash
mariadb-backup --backup \
      --innodb-undo-tablespaces=10
```

### `--innodb-use-native-aio`

Defines whether you want to use native AI/O.

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can enable the use of the native asynchronous I/O subsystem. It is only available on Linux operating systems.

```bash
mariadb-backup --backup \
      --innodb-use-native-aio
```

### `--innodb-write-io-threads`

Defines the number of background write I/O threads in InnoDB.

```bash
--innodb-write-io-threads=#
```

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set the number of background write I/O threads `mariadb-backup` uses.

```bash
mariadb-backup --backup \
     --innodb-write-io-threads=4
```

### `--kill-long-queries-timeout`

Defines the timeout for blocking queries.

```bash
--kill-long-queries-timeout=#
```

When `mariadb-backup` runs, it issues a `FLUSH TABLES WITH READ LOCK` statement. It then identifies blocking queries. Using this option you can set a timeout in seconds for these blocking queries. When the time runs out, `mariadb-backup` kills the queries.

The default value is `0`, which causes `mariadb-backup` to not attempt killing any queries.

```bash
mariadb-backup --backup \
      --kill-long-queries-timeout=10
```

### `--kill-long-query-type`

Defines the query type the utility can kill to unblock the global lock.

```bash
--kill-long-query-type=ALL | UPDATE | SELECT
```

When `mariadb-backup` encounters a query that sets a global lock, it can kill the query in order to free up MariaDB Server for the backup. Using this option, you can choose the types of query it kills: `SELECT`, `UPDATE`, or both set with `ALL`. The default is `ALL`.

```bash
mariadb-backup --backup \
      --kill-long-query-type=UPDATE
```

### `--lock-ddl-per-table`

Prevents DDL for each table to be backed up by acquiring MDL lock on that.

{% hint style="info" %}
Unless the `--no-lock` option is also specified, conflicting DDL queries are killed at the end of backup This is done to avoid a deadlock between `FLUSH TABLE WITH READ LOCK`, user's DDL query (`ALTER`, `RENAME`), and MDL lock on table.
{% endhint %}

### `--log`

This option has no functionality. It is set to ensure compatibility with MySQL.

### `--log-bin`

Defines the base name for the log sequence.

```bash
--log-bin[=name]
```

Using this option you, you can set the base name for `mariadb-backup` to use in log sequences.

### `--log-copy-interval`

Defines the copy interval between checks done by the log copying thread.

```bash
--log-copy-interval=#
```

Using this option, you can define the copy interval mariadb-backup uses between checks done by the log copying thread. The given value is in milliseconds.

```bash
mariadb-backup --backup \
      --log-copy-interval=50
```

### `--log-innodb-page-corruption`

Continue backup if InnoDB corrupted pages are found. The pages are logged in `innodb_corrupted_pages` and backup is finished with error. `--prepare` will try to fix corrupted pages. If `innodb_corrupted_pages` exists after --prepare in base backup directory, backup still contains corrupted pages and can not be considered as consistent.

### `--move-back`

Restores the backup to the data directory.

Using this command, `mariadb-backup` moves the backup from the target directory to the data directory, as defined by the `--datadir` option. You must stop the MariaDB Server before running this command. The data directory must be empty. If you want to overwrite the data directory with the backup, use the `--force-non-empty-directories` option.

Bear in mind, before you can restore a backup, you first need to run `mariadb-backup` with the `--prepare` option. In the case of full backups, this makes the files point-in-time consistent. With incremental backups, this applies the deltas to the base backup. Once the backup is prepared, you can run `--move-back` to apply it to MariaDB Server.

```bash
mariadb-backup --move-back \
      --datadir=/var/mysql
```

Running the `--move-back` command moves the backup files to the data directory. Use this command if you don't want to save the backup for later. If you do want to save the backup for later, use the `--copy-back` option.

### `--mysqld`

Used internally to prepare a backup.

### `--no-backup-locks`

`mariadb-backup` locks the database by default when it runs. This option disables support for Percona Server's backup locks.

When backing up Percona Server, mariadb-backup would use backup locks by default. To be specific, backup locks refers to the `LOCK TABLES FOR BACKUP` and `LOCK BINLOG FOR BACKUP` statements. This option can be used to disable support for Percona Server's backup locks. This option has no effect when the server does not support Percona's backup locks.

Deprecated and has no effect from [MariaDB 10.11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-8-release-notes), [MariaDB 11.0.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes), [MariaDB 11.1.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes) and [MariaDB 11.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes) as MariaDB now always uses backup locks for better performance. See [MDEV-32932](https://jira.mariadb.org/browse/MDEV-32932).

```bash
mariadb-backup --backup --no-backup-locks
```

### `--no-lock`

Disables table locks with the `FLUSH TABLE WITH READ LOCK` statement.

Using this option causes mariadb-backup to disable table locks with the `FLUSH TABLE WITH READ LOCK` statement. Only use this option if:

* You are not executing DML statements on non-InnoDB tables during the backup. This includes the `mysql` database system tables (which are MyISAM).
* You are not executing any DDL statements during the backup.
* You are _not_ using the file `xtrabackup_binlog_info`, which is not consistent with the data when `--no-lock` is used. Use the file `xtrabackup_binlog_pos_innodb` instead.
* All tables you're backing up use the InnoDB storage engine.

```bash
mariadb-backup --backup --no-lock
```

If you're considering `--no-lock` due to backups failing to acquire locks, this may be due to incoming replication events preventing the lock. Consider using the `--safe-slave-backup` option to momentarily stop the replica thread. This alternative may help the backup to succeed without resorting to `--no-lock`.

The `--no-lock` option only provides a consistent backup if the user ensures that no DDL or non-transactional table updates occur during the backup. The `--no-lock` option is not supported by MariaDB plc.

### `--no-timestamp`

This option prevents creation of a time-stamped subdirectory of the `BACKUP-ROOT-DIR` given on the command line. When it is specified, the backup is done in `BACKUP-ROOT-DIR` instead. This is only valid in `innobackupex` mode, which can be enabled with the `--innobackupex` option.

### `--no-version-check`

Disables version check.

Using this option, you can disable mariadb-backup version check.

```bash
mariadb-backup --backup --no-version-check
```

### `--open-files-limit`

Defines the maximum number of file descriptors.

```bash
--open-files-limit=#
```

Using this option, you can define the maximum number of file descriptors mariadb-backup reserves with `setrlimit()`.

```bash
mariadb-backup --backup \
      --open-files-limit=
```

### `--parallel`

Defines the number of threads to use for parallel data file transfer.

```bash
--parallel=#
```

Using this option, you can set the number of threads mariadb-backup uses for parallel data file transfers. By default, it is set to 1.

### `-p, --password`

Defines the password to use to connect to MariaDB Server.

```bash
--password=passwd
```

When you run `mariadb-backup`, it connects to MariaDB Server in order to access and back up the databases and tables. Using this option, you can set the password mariadb-backup uses to access the server. To set the user, use the `--user` option.

```bash
mariadb-backup --backup \
      --user=root \
      --password=root_password
```

### `--plugin-dir`

Defines the directory for server plugins.

```bash
--plugin-dir=PATH
```

Using this option, you can define the path `mariadb-backup` reads for MariaDB Server plugins. It only uses it during the `--prepare` phase to load the encryption plugin. It defaults to the `plugin_dir` server system variable.

```bash
mariadb-backup --backup \
      --plugin-dir=/var/mysql/lib/plugin
```

### `--plugin-load`

The option has been removed.

### `-P, --port`

Defines the server port to connect to.

```bash
--port=#
```

When you run `mariadb-backup`, it connects to MariaDB Server in order to access and back up your databases and tables. Using this option, you can set the port the utility uses to access the server over TCP/IP. To set the host, see the `--host` option. Use `mysql --help` for more details.

```bash
mariadb-backup --backup \
      --host=192.168.11.1 \
      --port=3306
```

### `--prepare`

Prepares an existing backup to restore to the MariaDB Server.

Files that `mariadb-backup` generates during `--backup` operations in the target directory are not ready for use on the Server. Before you can restore the data to MariaDB, you first need to prepare the backup.

In the case of full backups, the files are not point in time consistent, since they were taken at different times. If you try to restore the database without first preparing the data, InnoDB rejects the new data as corrupt. Running mariadb-backup with the `--prepare` command readies the data so you can restore it to MariaDB Server. When working with incremental backups, you need to use the `--prepare` command and the `--incremental-dir` option to update the base backup with the deltas from an incremental backup.

```bash
mariadb-backup --prepare
```

Once the backup is ready, you can use the `--copy-back` or the `--move-back` options to restore the backup to the server.

### `--print-defaults`

Prints the utility argument list, then exits.

Using this argument, MariaDB prints the argument list to stdout and then exits. You may find this useful in debugging to see how the options are set for the utility.

```bash
mariadb-backup --print-defaults
```

### `--print-param`

Prints the MariaDB Server options needed for `copy-back`.

Using this option, `mariadb-backup` prints to stdout the MariaDB Server options that the utility requires to run the `--copy-back` command option.

```bash
mariadb-backup --print-param
```

### `--rollback-xa`

By default, mariadb-backup will not commit or rollback uncommitted XA transactions, and when the backup is restored, any uncommitted XA transactions must be manually committed using `XA COMMIT` or manually rolled back using `XA ROLLBACK`.

**MariaDB starting with** [**10.5**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-5-series/what-is-mariadb-105)

mariadb-backup's `--rollback-xa` option is not present because the server has more robust ways of handling uncommitted XA transactions.

This is an experimental option. Do not use this option in older versions. Older implementation can cause corruption of InnoDB data.

### `--rsync`

Defines whether to use rsync.

During normal operation, mariadb-backup transfers local non-InnoDB files using a separate call to `cp` for each file. Using this option, you can optimize this process by performing this transfer with rsync, instead.

```bash
mariadb-backup --backup --rsync
```

This option is not compatible with the `--stream` option.

Deprecated and has no effect from [MariaDB 10.11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-8-release-notes), [MariaDB 11.0.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes), [MariaDB 11.1.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes) and [MariaDB 11.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes) as rsync will not work on tables that are in use. See [MDEV-32932](https://jira.mariadb.org/browse/MDEV-32932).

### `--safe-slave-backup`

Stops replica SQL threads for backups.

When running `mariadb-backup` on a server that uses replication, you may occasionally encounter locks that block backups. Using this option, it stops replica SQL threads and waits until the `Slave_open_temp_tables` in the `SHOW STATUS` statement is zero. If there are no open temporary tables, the backup runs, otherwise the SQL thread starts and stops until there are no open temporary tables.

```bash
mariadb-backup --backup \
      --safe-slave-backup \
      --safe-slave-backup-timeout=500
```

The backup fails if the `Slave_open_temp_tables` doesn't reach zero after the timeout period set by the `--safe-slave-backup-timeout` option.

### `--safe-slave-backup-timeout`

Defines the timeout for replica backups.

```bash
--safe-slave-backup-timeout=#
```

When running mariadb-backup on a server that uses replication, you may occasionally encounter locks that block backups. With the `--safe-slave-backup` option, it waits until the `Slave_open_temp_tables` in the `SHOW STATUS` statement reaches zero. Using this option, you set how long it waits. It defaults to 300.

```bash
mariadb-backup --backup \
      --safe-slave-backup \
      --safe-slave-backup-timeout=500
```

### `--secure-auth`

Refuses client connections to servers using the older protocol.

Using this option, you can set it explicitly to refuse client connections to the server when using the older protocol, from before 4.1.1. This feature is enabled by default. Use the `--skip-secure-auth` option to disable it.

```bash
mariadb-backup --backup --secure-auth
```

### `--skip-innodb-adaptive-hash-index`

Disables InnoDB Adaptive Hash Index.

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option you can explicitly disable the InnoDB Adaptive Hash Index. This feature is enabled by default for mariadb-backup. If you want to explicitly enable it, use `--innodb-adaptive-hash-index`.

```bash
mariadb-backup --backup \
      --skip-innodb-adaptive-hash-index
```

### `--skip-innodb-doublewrite`

Disables doublewrites for InnoDB tables.

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. When doublewrites are enabled, InnoDB improves fault tolerance with a doublewrite buffer. By default this feature is turned on. Using this option you can disable it for mariadb-backup. To explicitly enable doublewrites, use the `--innodb-doublewrite` option.

```bash
mariadb-backup --backup \
     --skip-innodb-doublewrite
```

### `--skip-innodb-log-checksums`

Defines whether to exclude checksums in the InnoDB logs.

`mariadb-backup` initializes its own embedded instance of InnoDB using the same configuration as defined in the configuration file. Using this option, you can set mariadb-backup to exclude checksums in the InnoDB logs. The feature is enabled by default. To explicitly enable it, use the `--innodb-log-checksums` option.

### `--skip-secure-auth`

Refuses client connections to servers using the older protocol.

Using this option, you can set it accept client connections to the server when using the older protocol, from before 4.1.1. By default, it refuses these connections. Use the `--secure-auth` option to explicitly enable it.

```bash
mariadb-backup --backup --skip-secure-auth
```

### `--slave-info`

Prints the binary log position and the name of the primary server.

If the server is a replica, then this option causes `mariadb-backup` to print the hostname of the replica's replication primary and the binary log file and position of the replica's SQL thread to `stdout`.

This option also causes `mariadb-backup` to record this information as a `CHANGE MASTER` statement that can be used to set up a new server as a replica of the original server's primary after the backup has been restored. This information are written to the `xtrabackup_slave_info` file.

`mariadb-backup` does **not** check if GTIDs are being used in replication. It takes a shortcut and assumes that if the `gtid_slave_pos` system variable is non-empty, then it writes the `CHANGE MASTER` statement with the `MASTER_USE_GTID` option set to `slave_pos`. Otherwise, it writes the `CHANGE MASTER` statement with the `MASTER_LOG_FILE` and `MASTER_LOG_POS` options using the primary's binary log file and position. See [MDEV-19264](https://jira.mariadb.org/browse/MDEV-19264) for more information.

```bash
mariadb-backup --slave-info
```

### `-S, --socket`

Defines the socket for connecting to local database.

```bash
--socket=name
```

Using this option, you can define the UNIX domain socket you want to use when connecting to a local database server. The option accepts a string argument. For more information, see the `mysql --help` command.

```bash
mariadb-backup --backup \
      --socket=/var/mysql/mysql.sock
```

### `--ssl`

Enables TLS. By using this option, you can explicitly configure `mariadb-backup` to encrypt its connection with TLS when communicating with the server. You may find this useful when performing backups in environments where security is extra important or when operating over an insecure network.

TLS is also enabled even without setting this option when certain other TLS options are set. For example, see the descriptions of the following options:

* \--ssl-ca
* \--ssl-capath
* \--ssl-cert
* \--ssl-cipher
* \--ssl-key

### `--ssl-ca`

Defines a path to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for TLS. This option requires that you use the absolute path, not a relative path. For example:

```bash
--ssl-ca=/etc/my.cnf.d/certificates/ca.pem
```

This option is usually used with other TLS options. For example:

```bash
mariadb-backup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem
```

See Secure Connections Overview: Certificate Authorities (CAs) for more information.

This option implies the `--ssl` option.

### `--ssl-capath`

Defines a path to a directory that contains one or more PEM files that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use for TLS. This option requires that you use the absolute path, not a relative path. For example:

```bash
--ssl-capath=/etc/my.cnf.d/certificates/ca/
```

This option is usually used with other TLS options. For example:

```bash
mariadb-backup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem \
   --ssl-capath=/etc/my.cnf.d/certificates/ca/
```

The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command.

See Secure Connections Overview: Certificate Authorities (CAs) for more information

This option implies the `--ssl` option.

### `--ssl-cert`

Defines a path to the X509 certificate file to use for TLS. This option requires that you use the absolute path, not a relative path. For example:

```bash
--ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem
```

This option is usually used with other TLS options. For example:

```bash
mariadb-backup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem
```

This option implies the `--ssl` option.

### `--ssl-cipher`

Defines the list of permitted ciphers or cipher suites to use for TLS. For example:

```
--ssl-cipher=name
```

This option is usually used with other TLS options. For example:

```bash
mariadb-backup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem \
   --ssl-cipher=TLSv1.2
```

To determine if the server restricts clients to specific ciphers, check the ssl\_cipher system variable.

This option implies the `--ssl` option.

### `--ssl-crl`

Defines a path to a PEM file that should contain one or more revoked X509 certificates to use for TLS. This option requires that you use the absolute path, not a relative path. For example:

```bash
--ssl-crl=/etc/my.cnf.d/certificates/crl.pem
```

This option is usually used with other TLS options. For example:

```bash
mariadb-backup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem \
   --ssl-crl=/etc/my.cnf.d/certificates/crl.pem
```

See Secure Connections Overview: Certificate Revocation Lists (CRLs) for more information.

This option is only supported if `mariadb-backup` was built with OpenSSL. If `mariadb-backup` was built with yaSSL, then this option is not supported. See TLS and Cryptography Libraries Used by MariaDB for more information about which libraries are used on which platforms.

### `--ssl-crlpath`

Defines a path to a directory that contains one or more PEM files that should each contain one revoked X509 certificate to use for TLS. This option requires that you use the absolute path, not a relative path. For example:

```bash
--ssl-crlpath=/etc/my.cnf.d/certificates/crl/
```

This option is usually used with other TLS options. For example:

```bash
mariadb-backup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem \
   --ssl-crlpath=/etc/my.cnf.d/certificates/crl/
```

The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command.

See Secure Connections Overview: Certificate Revocation Lists (CRLs) for more information.

This option is only supported if mariadb-backup was built with OpenSSL. If `mariadb-backup` was built with yaSSL, then this option is not supported. See TLS and Cryptography Libraries Used by MariaDB for more information about which libraries are used on which platforms.

### `--ssl-key`

Defines a path to a private key file to use for TLS. This option requires that you use the absolute path, not a relative path. For example:

```bash
--ssl-key=/etc/my.cnf.d/certificates/client-key.pem
```

This option is usually used with other TLS options. For example:

```bash
mariadb-backup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem
```

This option implies the `--ssl` option.

### `--ssl-verify-server-cert`

Enables server certificate verification. This option is disabled by default.

This option is usually used with other TLS options. For example:

```bash
mariadb-backup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem \
   --ssl-verify-server-cert
```

### `--stream`

Streams backup files to stdout.

```bash
--stream=xbstream
```

Using this command option, you can set `mariadb-backup` to stream the backup files to `stdout` in the given format. Currently, the supported format is `xbstream`.

```bash
mariadb-backup --stream=xbstream > backup.xb
```

To extract all files from the xbstream archive into a directory use the `mbstream` utility

```bash
mbstream  -x < backup.xb
```

If a backup is streamed, then `mariadb-backup`  records the format in the `xtrabackup_info` file.

### `--tables`

Defines the tables you want to include in the backup.

```bash
--tables=REGEX
```

Using this option, you can define what tables you want `mariadb-backup` to back up from the database. The table values are defined using Regular Expressions. To define the tables you want to exclude from the backup, see the `--tables-exclude` option.

```bash
mariadb-backup --backup \
     --databases=example \
     --tables=nodes_* \
     --tables-exclude=nodes_tmp
```

In the example, _`nodes_*`_ matches tables named _`nodes`_, _`nodes_`_, _`nodes__`_, and so forth, because `*` means _zero or more occurrences of the previous character_ (`_`).&#x20;

If instead you want to back up all tables whose names start with _`nodes`_, the regular expression is `^nodes.`, and to exclude tables starting with _`nodes_tmp`_, the expression is _`^nodes_tmp.`_.  (Notice the trailing period (`.`); it means _zero or more occurrences of characters following `nodes`_.) The command looks like this:

```bash
mariadb-backup --backup \
     --databases=example \
     --tables=^nodes. \
     --tables-exclude=^nodes_tmp.
```

In that example, some of the tables included via the `--tables` option are excluded by `--tables-excludes`. That works because `--tables-exclude` takes precedence over `--tables`.

You can specify multiple table name regex[^2] patterns as a comma-separated list, for both the `--tables` and the `--tables-exclude` options.

{% hint style="warning" %}
The [`--databases`](mariadb-backup-options.md#databases) and [`--databases-exclude`](mariadb-backup-options.md#databases-exclude) options, if used, take precedence over `--tables` and `--tables-exclude`. That is, they can filter out tables, which are then not "visible" to the latter mentioned options.
{% endhint %}

If a backup is a partial backup, `mariadb-backup` records that detail in the `xtrabackup_info` file.

### `--tables-exclude`

Defines the tables you want to exclude from the backup.

```bash
--tables-exclude=REGEX
```

Using this option, you can define what tables you want `mariadb-backup` to exclude from the backup. The table values are defined using Regular Expressions. To define the tables you want to include from the backup, see the `--tables` option.

{% hint style="info" %}
See [the `--tables` option](mariadb-backup-options.md#tables) for examples and hints regarding regular expressions.
{% endhint %}

If a backup is a partial backup, `mariadb-backup` records that detail in the `xtrabackup_info` file.

### `--tables-file`

Defines path to file with tables for backups.

```bash
--tables-file=/path/to/file
```

Using this option, you can set a path to a file listing the tables you want to back up. `mariadb-backup` iterates over each line in the file. The format is `database.table`.

```bash
mariadb-backup --backup \
     --databases=example \
     --tables-file=/etc/mysql/backup-file
```

If a backup is a partial backup, then mariadb-backup will record that detail in the `xtrabackup_info` file.

### `--target-dir`

Defines the destination directory.

```bash
--target-dir=/path/to/target
```

Using this option you can define the destination directory for the backup. `mariadb-backup` writes all backup files to this directory. mariadb-backup will create the directory, if it does not exist (but it does not create the full path recursively, i.e. at least parent directory if the `--target-dir` must exist.

```bash
mariadb-backup --backup \
       --target-dir=/data/backups
```

### `--throttle`

Defines the limit for I/O operations per second in IOS values.

```bash
--throttle=#
```

Using this option, you can set a limit on the I/O operations mariadb-backup performs per second in IOS values. It is only used during the `--backup` option.

### `--tls-version`

This option accepts a comma-separated list of TLS protocol versions. A TLS protocol version is only enabled if it is present in this list. All other TLS protocol versions will not be permitted. For example:

```bash
--tls-version="TLSv1.2,TLSv1.3"
```

This option is usually used with other TLS options. For example:

```bash
mariadb-backup --backup \
   --ssl-cert=/etc/my.cnf.d/certificates/client-cert.pem \
   --ssl-key=/etc/my.cnf.d/certificates/client-key.pem \
   --ssl-ca=/etc/my.cnf.d/certificates/ca.pem \
   --tls-version="TLSv1.2,TLSv1.3"
```

See Secure Connections Overview: TLS Protocol Versions for more information.

### `-t, --tmpdir`

Defines path for temporary files.

```bash
--tmpdir=/path/tmp[;/path/tmp...]
```

Using this option, you can define the path to a directory `mariadb-backup` uses in writing temporary files. If you want to use more than one, separate the values by a semicolon (that is, `;`). When passing multiple temporary directories, it cycles through them using round-robin.

```bash
mariadb-backup --backup \
     --tmpdir=/data/tmp;/tmp
```

### `--use-memory`

Defines the buffer pool size that is used during the prepare stage.

```bash
--use-memory=124M
```

Using this option, you can define the buffer pool size for `mariadb-backup`. Use it instead of `buffer_pool_size`.

```bash
mariadb-backup --prepare \
      --use-memory=124M
```

### `--user`

Defines the username for connecting to the MariaDB Server.

```bash
--user=name
-u name
```

When `mariadb-backup` runs, it connects to the specified MariaDB Server to get its backups. Using this option, you can define the database user used for authentication. Starting from [MariaDB 10.6.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-17-release-notes), [MariaDB 10.11.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-7-release-notes), [MariaDB 11.0.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-5-release-notes), [MariaDB 11.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-4-release-notes), [MariaDB 11.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-3-release-notes), [MariaDB 11.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-2-release-notes), [MariaDB 11.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-1-release-notes), if the `--user` option is omitted, the user name is detected from the OS.

```bash
mariadb-backup --backup \
      --user=root \
      --password=root_passwd
```

### `--verbose`

Displays verbose output.

```bash
mariadb-backup --verbose
```

### `--version`

Prints the `mariadb-backup` version information to `stdout`.

```bash
mariadb-backup --version
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}

[^1]: FLUSH TABLES WITH READ LOCK

[^2]: regular expression
