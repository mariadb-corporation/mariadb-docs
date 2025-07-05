# Aria FAQ

This FAQ provides information on the [Aria](./) storage engine.

The _**Aria**_ storage engine was previously known as _**Maria**_, (see, the [Aria Name](the-aria-name.md)). In current releases of [MariaDB](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/mariadb/README.md), you can refer to the engine as Maria or Aria. As this will change in future releases, please update references in your scripts and automation to use the correct name.

### What is Aria?

Aria is a storage engine for MySQL® and MariaDB. It was originally developed with the goal of becoming the default transactional **and** non-transactional storage engine for MariaDB and MySQL.

It has been in development since 2007 and was first announced on Monty's [blog](https://monty-says.blogspot.com/2008/01/maria-engine-is-released.html). The same core MySQL engineers who developed the MySQL server and the [MyISAM](../myisam-storage-engine/), [MERGE](../merge.md), and [MEMORY](../memory-storage-engine.md) storage engines are also working on Aria.

### Why is the engine called Aria?

Originally, the storage engine was called **Maria**, after Monty's younger daughter. Monty named MySQL after his first child, **My** and his second child **Max** gave his name to MaxDB and the MySQL-Max distributions.

In practice, having both _MariaDB_ the database server and _Maria_ the storage engine with such similar names proved confusing. To mitigate this, the decision was made to change the name. A Rename Maria contest was held during the first half of 2010 and names were submitted from around the world. Monty picked the name _**Aria**_ from a short list of finalist. Chris Tooley, who suggested it, received the prize of a Linux-powered[System 76 Meerkat NetTop](https://www.system76.com/product_info.php?cPath=27\&products_id=91) from Monty Program.

For more information, see the [Aria Name](the-aria-name.md).

### What's the goal for the current version?

The current version of Aria is 1.5. The goal of this release is to develop a crash-safe alternative to MyISAM. That is, when MariaDB restarts after a crash, Aria recovers all tables to the state as of the start of a statement or at the start of the last `LOCK TABLES` statement.

The current goal is to keep the code stable and fix all bugs.

### What's the goal for the next version?

The next version of Aria is 2.0. The goal for this release is to develop a fully transactional storage engine with at least all the major features of InnoDB.

Currently, Aria 2.0 is on hold as its developers are focusing on improving MariaDB. However, they are interested in working with interested customers and partners to add more features to Aria and eventually release 2.0.

These are some of the goals for Aria 2.0:

* ACID compliant
* Commit/Rollback
* Concurrent updates/deletes
* Row locking
* Group commit (Already in [MariaDB 5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2))
* Faster lookup in index pages (Page directory)

Beginning in Aria 2.5, the plan is to focus on improving performance.

### What is the ultimate goal of Aria?

Long term, we have the following goals for Aria:

* To create a new, ACID and Multi-Version Concurrency Control (MVCC), transactional storage engine that can function as both the default non-transactional and transactional storage engine for MariaDB and MySQL®.
* To be a MyISAM replacement. This is possible because Aria can also be run in non-transactional mode, supports the same row formats as MyISAM, and supports or will support all major features of MyISAM.
* To be the default non-transactional engine in MariaDB (instead of MyISAM).

### What are the design goals in Aria?

* Multi-Version Concurrency Control (MVCC) and ACID storage engine.
* Optionally non-transactional tables that should be 'as fast and as compact' as MyISAM tables.
* Be able to use Aria for internal temporary tables in MariaDB (instead of MyISAM).
* All indexes should have equal speed (clustered index is not on our current road map for Aria. If you need clustered index, you should use XtraDB).
* Allow 'any' length transactions to work (Having long running transactions will cause more log space to be used).
* Allow log shipping; that is, you can do incremental backups of Aria tables just by copying the Aria logs.
* Allow copying of Aria tables between different Aria servers (under some well-defined constraints).
* Better blob handling (than is currently offered in MyISAM, at a minimum).
* No memory copying or extra memory used for blobs on insert/update.
* Blobs allocated in big sequential blocks - Less fragmentation over time.
* Blobs are stored so that Aria can easily be extended to have access to any part of a blob with a single fetch in the future.
* Efficient storage on disk (that is, low row data overhead, low page data overhead and little lost space on pages). Note: There is still some more work to succeed with this goal. The disk layout is fine, but we need more in-memory caches to ensure that we get a higher fill factor on the pages.
* Small footprint, to make MariaDB + Aria suitable for desktop and embedded applications.
* Flexible memory allocation and scalable algorithms to utilize large amounts of memory efficiently, when it is available.

### Where can I find documentation and help about Aria?

Documentation is available at [Aria](./) and related topics. The project is maintained on [GitHub](https://github.com/MariaDB/server).

If you want to know what happens or be part of developing Aria, you can subscribe to the [developers](https://lists.mariadb.org/postorius/lists/developers.lists.mariadb.org/), [docs](https://lists.mariadb.org/postorius/lists/docs.lists.mariadb.org/), or [discuss](https://lists.mariadb.org/postorius/lists/discuss.lists.mariadb.org/) mailing lists.

To report and check bugs in Aria, see [Reporting Bugs](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/community/bug-tracking/reporting-bugs).

You can usually find some of the Maria developers on our Zulip instance at [mariadb.zulipchat.com](https://mariadb.zulipchat.com) or on the IRC channel #maria at.

### Who develops Aria?

The Core Team who develop Aria are:

**Technical lead**

* Michael "Monty" Widenius - Creator of MySQL and MyISAM

**Core Developers (in alphabetical order)**

* Guilhem Bichot - Replication expert, on line backup for MyISAM, etc.
* Kristian Nielsen - MySQL build tools, NDB, MySQL server
* Oleksandr Byelkin - Query cache, sub-queries, views.
* Sergei Golubchik - Server Architect, Full text search, keys for MyISAM-Merge, Plugin architecture, etc.

All except Guilhem Bichot are working for [MariaDB Corporation Ab](https://mariadb.com).

### What is the release policy/schedule of Aria?

Aria follows the same [release criteria](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-release-criteria) as for [MariaDB](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/mariadb/README.md). Some clarifications, unique for the Aria storage engine:

* Aria index and data file formats should be backwards and forwards compatible to ensure easy upgrades and downgrades.
* The [log file](aria-storage-engine.md#aria-log-files) format should also be compatible, but we don't make any guarantees yet. In some cases when upgrading, you must remove the old `aria_log.%` and `maria_log.%` files before restarting MariaDB. (So far, this has only occurred in the upgrade from [MariaDB 5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1) and [MariaDB 5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2)).

#### Extended commitment for Beta 1.5

* Aria is now feature complete according to specification.

### How does Aria 1.5 Compare to MyISAM?

Aria 1.0 was basically a crash-safe non-transactional version of MyISAM. Aria 1.5 added more concurrency (multiple inserter) and some optimizations.

Aria supports all aspects of MyISAM, except as noted below. This includes external and internal check/repair/compressing of rows, different row formats, different index compress formats, [aria_chk](../../../clients-and-utilities/aria-clients-and-utilities/aria_chk.md) etc. After a normal shutdown you can copy Aria files between servers.

### Advantages of Aria compared to MyISAM

* Data and indexes are crash safe.
* On a crash, changes will be rolled back to state of the start of a statement or a last `LOCK TABLES` statement.
* Aria can replay almost everything from the log. (Including `CREATE`, `DROP`, `RENAME`, `TRUNCATE` tables). Therefore, you make a backup of Aria by just copying the log. The things that can't be replayed (yet) are:
  * Batch `INSERT` into an empty table (This includes `LOAD DATA INFILE`, `SELECT... INSERT` and `INSERT` (many rows)).
  * `ALTER TABLE`. Note that `.frm` tables are NOT recreated!
* `LOAD INDEX` can skip index blocks for unwanted indexes.
* Supports all MyISAM `ROW` formats and new `PAGE` format where data is stored in pages. (default size is 8K).
* Multiple concurrent inserters into the same table.
* When using `PAGE` format (default) row data is cached by page cache.
* Aria has unit tests of most parts.
* Supports both crash-safe (soon to be transactional) and not transactional tables. (Non-transactional tables are not logged and rows uses less space): `CREATE TABLE foo (...) TRANSACTIONAL=0|1 ENGINE=Aria`.
* `PAGE` is the only crash-safe/transactional row format.
* `PAGE` format should give a notable speed improvement on systems which have bad data caching. (For example Windows).
* From [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105), max key length is 2000 bytes, compared to 1000 bytes in MyISAM.

### Differences between Aria and MyISAM

* Aria uses BIG (1G by default) [log files](aria-storage-engine.md#aria-log-files).
* Aria has a log control file (`aria_log_control`) and log files (`aria_log.%`). The log files can be automatically purged when not needed or purged on demand (after backup).
* Aria uses 8K pages by default (MyISAM uses 1K). This makes Aria a bit faster when using keys of fixed size, but slower when using variable-length packed keys (until we add a directory to index pages).

### Disadvantages of Aria compared to MyISAM

* Aria doesn't support `INSERT DELAYED`.
* Aria does not support multiple key caches.
* Storage of very small rows (< 25 bytes) are not efficient for `PAGE` format.
* `MERGE` tables don't support Aria (should be very easy to add later).
* Aria data pages in block format have an overhead of 10 bytes/page and 5 bytes/row. Transaction and multiple concurrent-writer support will use an extra overhead of 7 bytes for new rows, 14 bytes for deleted rows and 0 bytes for old compacted rows.
* No external locking (MyISAM has external locking, but this is a rarely used feature).
* Aria has one page size for both index and data (defined when Aria is used the first time). MyISAM supports different page sizes per index.
* Small overhead (15 bytes) per index page.
* Aria doesn't support MySQL internal RAID (disabled in MyISAM too, it's a deprecated feature).
* Minimum data file size for PAGE format is 16K (with 8K pages).
* Aria doesn't support indexes on virtual fields.

### Differences between [MariaDB 5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1) release and the normal MySQL-5.1 release?

See:

* [Aria storage engine](aria-storage-engine.md)
* [MariaDB versus MySQL](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/broken-reference/README.md)

### Why do you use the `TRANSACTIONAL` keyword now when Aria is not yet transactional?

In the current development phase Aria tables created with `TRANSACTIONAL=1` are crash safe and atomic but not transactional because changes in Aria tables can't be rolled back with the `ROLLBACK` command. As we planned to make Aria tables fully transactional, we decided it was better to use the `TRANSACTIONAL` keyword from the start so that applications don't need to be changed later.

### What are the known problems with the MySQL-5.1-Maria release?

* See `KNOWN_BUGS.txt` for open/design bugs.
* See jira.mariadb.org for newly reported bugs. Please report anything you can't find here!
* If there is a bug in the Aria recovery code or in the code that generates the logs, or if the logs become corrupted, then mysqld may fail to start because Aria can't execute the logs at start up.
* Query cache and concurrent insert using page row format have a bug, please disable query cache while using page row format and [MDEV-6817](https://jira.mariadb.org/browse/MDEV-6817) isn't complete

If Aria doesn't start or you have an unrecoverable table (shouldn't happen):

* Remove the `aria_log.%` files from the data directory.
* Restart `mysqld` and run [CHECK TABLE](../../../reference/sql-statements/table-statements/check-table.md), [REPAIR TABLE](../../../reference/sql-statements/table-statements/repair-table.md) or [mariadb-check](../../../clients-and-utilities/table-tools/mariadb-check.md) on your Aria tables.

Alternatively,

* Remove logs and run [aria\_chk](../../../clients-and-utilities/aria-clients-and-utilities/aria_chk.md) on your `*.MAI` files.

### What is going to change in later Aria main releases?

The `LOCK TABLES` statement will not start a crash-safe segment. You should use [begin](https://github.com/mariadb-corporation/docs-server/blob/test/server/reference/storage-engines/aria/begin/README.md) and [COMMIT](../../../reference/sql-statements/transactions/commit.md) instead.

To make things future safe, you could do this:

```
BEGIN;
LOCK TABLES ....
UNLOCK TABLES;
COMMIT;
```

And later you can just remove the `LOCK TABLES` and `UNLOCK TABLES` statements.

### How can I create a MyISAM-like (non-transactional) table in Aria?

Example:

```
CREATE TABLE t1 (a int) ROW_FORMAT=FIXED TRANSACTIONAL=0 PAGE_CHECKSUM=0;
CREATE TABLE t2 (a int) ROW_FORMAT=DYNAMIC TRANSACTIONAL=0 PAGE_CHECKSUM=0;
SHOW CREATE TABLE t1;
SHOW CREATE TABLE t2;
```

Note that the rows are not cached in the page cache for `FIXED` or `DYNAMIC` format. If you want to have the data cached (something MyISAM doesn't support) you should use `ROW_FORMAT=PAGE`:

```
CREATE TABLE t3 (a int) ROW_FORMAT=PAGE TRANSACTIONAL=0 PAGE_CHECKSUM=0;
SHOW CREATE TABLE t3;
```

You can use `PAGE_CHECKSUM=1` also for non-transactional tables; This puts a page checksums on all index pages. It also puts a checksum on data pages if you use `ROW_FORMAT=PAGE`.

You may still have a speed difference (may be slightly positive or negative) between MyISAM and Aria because of different page sizes. You can change the page size for MariaDB with `--aria-block-size=\`#, where `\`

## is 1024, 2048, 4096, 8192, 16384 or 32768.

Note that if you change the page size you have to dump all your old tables into text (with [mariadb-dump](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md)) and remove the old Aria log and files:

```
# rm datadir/aria_log*
```

### What are the advantages/disadvantages of the new `PAGE` format compared to the old MyISAM-like row formats (`DYNAMIC` and `FIXED`)

The MyISAM-like `DYNAMIC` and `FIXED` format are extremely simple and have very little space overhead, so it's hard to beat them for when it comes to simple scanning of unmodified data. The `DYNAMIC` format does however get notably worse over time if you update the row a lot in a manner that increases the size of the row.

The advantages of the `PAGE` format (compared to `DYNAMIC` or `FIXED`) for non-transactional tables are:

* It's cached by the Page Cache, which gives better random performance (as it uses less system calls).
* Does not fragment as easily as the `DYNAMIC` format during `UPDATE` statements. The maximum number of fragments are very low.
* Code can easily be extended to only read the accessed columns (for example to skip reading blobs).
* Faster updates (compared to `DYNAMIC`).

The disadvantages are:

* Slight storage overhead (should only be notable for very small row sizes)
* Slower full table scan time.
* When using `row_format=PAGE`, (the default), Aria first writes the row, then the keys, at which point the check for duplicate keys happens. This makes `PAGE` format slower than `DYNAMIC` (or MyISAM) if there is a lot of duplicated keys because of the overhead of writing and removing the row. If this is a problem, you can use `row_format=DYNAMIC` to get same behavior as MyISAM.

### What's the proper way to copy a Aria table from one place to another?

An Aria table consists of 3 files:

```
XXX.frm : The definition for the table, used by MySQL.
XXX.MYI : Aria internal information about the structure of the data and index and data for all indexes.
XXX.MAD : The data.
```

It's safe to copy all the Aria files to another directory or MariaDB instance if any of the following holds:

* If you shutdown the MariaDB Server properly with [mariadb-admin shutdown](../../../clients-and-utilities/administrative-tools/mariadb-admin.md), so that there is nothing for Aria to recover when it starts.

or

* If you have run a [FLUSH TABLES](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) statement and not accessed the table using SQL from that time until the tables have been copied.

In addition, you must adhere the following rule for transactional tables:

You can't copy the table to a location within the same MariaDB server if the new table has existed before and the new table is still active in the Aria recovery log (that is, Aria may need to access the old data during recovery). If you are unsure whether the old name existed, run [aria\_chk --zerofill](../../../clients-and-utilities/aria-clients-and-utilities/aria_chk.md) on the table before you use it.

After copying a transactional table and before you use the table, we recommend that you run the command:

```
$ aria_chk --zerofill table_name
```

This will overwrite all references to the logs (LSN), all transactional references (TRN) and all unused space with 0. It also marks the table as 'movable'. An additional benefit of zerofill is that the Aria files will compress better. No real data is ever removed as part of zerofill.

Aria will automatically notice if you have copied a table from another system and do 'zerofill' for the first access of the table if it was not marked as 'movable'. The reason for using [aria\_chk --zerofill](../../../clients-and-utilities/aria-clients-and-utilities/aria_chk.md) is that you avoid a delay in the MariaDB server for the first access of the table.

Note that this automatic detection doesn't work if you copy tables within the same MariaDB server!

### When is it safe to remove old log files?

If you want to remove the [Aria log files](aria-storage-engine.md#aria-log-files) (`aria_log.%`) with `rm` or delete, then you must first shut down MariaDB cleanly (for example, with [mariadb-admin shutdown](../../../clients-and-utilities/administrative-tools/mariadb-admin.md)) before deleting the old files.

The same rules apply when upgrading MariaDB; When upgrading, first take down MariaDB in a clean way and then upgrade. This will allow you to remove the old log files if there are incompatible problems between\
releases.

Don't remove the `aria_log_control` file! This is not a log file, but a file that contains information about the Aria setup (current transaction id, unique id, next log file number etc.).

If you do, Aria will generate a new `aria_log_control` file at startup and will regard all old Aria files as files moved from another system. This means that they have to be 'zerofilled' before they can be used. This will happen automatically at next access of the Aria files, which can take some time if the files are big.

If this happens, you will see things like this in your mysqld.err file:

```
[Note] Zerofilling moved table: '.\database\xxxx'
```

As part of zerofilling no vital data is removed.

### How does one solve the Missing valid id error?

See [Aria Log Files](aria-storage-engine.md#aria-log-files) for details.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
