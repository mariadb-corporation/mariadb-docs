---
description: >-
  An overview of Aria, a storage engine designed as a crash-safe alternative to
  MyISAM, featuring transactional capabilities and improved caching.
---

# Aria Storage Engine

The [Aria](./) storage engine is compiled in by default from [MariaDB 5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.1/changes-improvements-in-mariadb-5-1) and it is required to be 'in use' when MariaDB is started.

All [system tables](../../../reference/system-tables/) are Aria.

Additionally, internal on-disk tables are in the Aria table format instead of the [MyISAM](../myisam-storage-engine/) table format. This should speed up some [GROUP BY](../../../reference/sql-statements/data-manipulation/selecting-data/group-by.md) and [DISTINCT](../../../reference/sql-functions/aggregate-functions/count-distinct.md) queries because Aria has better caching than MyISAM.

Note: The _**Aria**_ storage engine was previously called _Maria_ (see [The Aria Name](the-aria-name.md) for details on the rename) and in previous versions of [MariaDB](../storage-engines-storage-engines-overview.md) the engine was still called Maria.

The following table options to Aria tables in [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) and [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/):

* `TRANSACTIONAL= 0 | 1` : If the `TRANSACTIONAL` table option is set for an Aria table, then the table are crash-safe. This is implemented by logging any changes to the table to Aria's transaction log, and syncing those writes at the end of the statement. This will marginally slow down writes and updates. However, the benefit is that if the server dies before the statement ends, all non-durable changes will roll back to the state at the beginning of the statement. This also needs up to 6 bytes more for each row and key to store the transaction id (to allow concurrent insert's and selects).
  * `TRANSACTIONAL=1` is not supported for partitioned tables.
  * An Aria table's default value for the `TRANSACTIONAL` table option depends on the table's value for the `ROW_FORMAT` table option. See below for more details.
  * If the `TRANSACTIONAL` table option is set for an Aria table, the table does not actually support transactions. See [MDEV-21364](https://jira.mariadb.org/browse/MDEV-21364) for more information. In this context, transactional just means crash-safe.
* `PAGE_CHECKSUM= 0 | 1` : If index and data should use\
  page checksums for extra safety.
* `TABLE_CHECKSUM= 0 | 1` :\
  Same as `CHECKSUM` in MySQL 5.1
* `ROW_FORMAT=PAGE | FIXED | DYNAMIC` : The table's [row format](aria-storage-formats.md).
  * The default value is `PAGE`.
  * To emulate MyISAM, set `ROW_FORMAT=FIXED` or `ROW_FORMAT=DYNAMIC`

The `TRANSACTIONAL` and `ROW_FORMAT` table options interact as follows:

* If `TRANSACTIONAL=1` is set, then the only supported row format is `PAGE`. If `ROW_FORMAT` is set to some other value, then Aria issues a warning, but still forces the row format to be `PAGE`.
* If `TRANSACTIONAL=0` is set, then the table are not be crash-safe, and any row format is supported.
* If `TRANSACTIONAL` is not set to any value, then any row format is supported. If `ROW_FORMAT` is set, then the table will use that row format. Otherwise, the table will use the default `PAGE` row format. In this case, if the table uses the `PAGE` row format, then it are crash-safe. If it uses some other row format, then it will not be crash-safe.

Some other improvements are:

* [CHECKSUM TABLE](../../../reference/sql-statements/table-statements/checksum-table.md) now ignores values in `NULL` fields. This makes `CHECKSUM TABLE` faster and fixes some cases where same table definition could give different checksum values depending on [row format](aria-storage-formats.md). The disadvantage is that the value is now different compared to other MySQL installations. The new checksum calculation is fixed for all table engines that uses the default way to calculate and MyISAM which does the\
  calculation internally. Note: Old MyISAM tables with internal checksum returns the same checksum as before. To fix them to calculate according to new rules you have to do an [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/). You can use the old ways to calculate checksums by using the option `--old` to mariadbdmysqld or set the system variable '`@@old`' to `1` when you\
  do `CHECKSUM TABLE ... EXTENDED;`
* At startup Aria will check the Aria logs and automatically recover the tables from the last checkpoint if the server was not taken down correctly. See [Aria Log Files](aria-storage-engine.md#aria-log-files)

## Startup Options for Aria

For a full list, see [Aria System Variables](aria-system-variables.md).

In normal operations, the only variables you have to consider are:

* [aria-pagecache-buffer-size](aria-system-variables.md)
  * This is where all index and data pages are cached. The bigger this is, the faster\
    Aria will work.
* [aria-block-size](aria-system-variables.md#aria_block_size)
  * The default value 8192, should be ok for most cases. The only problem with a higher value is that it takes longer to find a packed key in the block as one has to\
    search roughly 8192/2 to find each key. We plan to fix this by adding a\
    dictionary at the end of the page to be able to do a binary search within the block before starting a scan. Until this is done and key lookups takes too long time even if you are not hitting disk, then you should consider making this smaller.
  * Possible values to try are `2048`, `4096` or `8192`
  * Note that you can't change this without dumping, deleting old tables and\
    deleting all log files and then restoring your Aria tables. (This is the only option that requires a dump and load.)
* [aria-log-purge-type](aria-system-variables.md)
  * Set this to "`at_flush`" if you want to keep a copy of the transaction logs (good as an extra backup). The logs will stay around until you execute [FLUSH ENGINE LOGS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).

## Aria Log Files

`aria_log_control` file is a very short log file (52 bytes) that contains the current state of all Aria tables related to logging and checkpoints. In particular, it contains the following information:

```
Aria file version: 1
Block size: 8192
maria_uuid: ee948482-6cb7-11ed-accb-3c7c3ff16468
last_checkpoint_lsn: (1,0x235a)
last_log_number: 1
trid: 28
recovery_failures: 0
```

* The `uuid` is a unique identifier per system. All Aria files created will have a copy of this in their .MAI headers. This is mainly used to check if someone has copied an Aria file between MariaDB servers.
* `last_checkpoint_lsn` and `last_log_number` are information about the current aria\_log files.
* `trid` is the highest transaction number seen so far. Used by recovery.

`aria_log.*` files contain the log of all operations that change Aria files (including create table, drop table, insert etc..) This is a 'normal' WAL (Write Ahead Log), similar to the InnoDB log file, except that aria\_logs contain both redo and undo. Old aria\_log files are automatically deleted when they are not needed anymore (Neither the last checkpoint or any running transaction need to refer to the old data anymore).

### Missing valid id

The error `Missing valid id at start of file. File is not a valid aria control file` means that something overwrote at least the first 4 bytes in the file. This can happen due to a problem with the file system (hardware or software), or a bug in which a thread inside MariaDB wrote on the wrong file descriptor (in which case you should [report the bug](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/community/bug-tracking/reporting-bugs), attaching a copy of the control file to assist).

In the case of a corrupted log file, with the server shut down, one should be able to fix that by deleting all aria\_log files.\
If the control\_file is corrupted, then one has to delete the aria\_control\_file and all aria\_log.\* files.\
The effect of this is that on table open of an Aria table, the server will think that it has been moved from another system and do an automatic check and repair of it. If there was no issues, the table are opened and can be used as normal. See also [When is it safe to remove old log files](aria-faq.md#when-is-it-safe-to-remove-old-log-files).

## See Also

* [Aria FAQ](aria-faq.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
