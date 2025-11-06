# MariaDB 11.0.1 Release Notes

[Download](https://downloads.mariadb.org/mariadb/11.0.1) | [Release Notes](mariadb-11-0-1-release-notes.md) | [Changelog](../../changelogs/11.0/mariadb-11-0-1-changelog.md) | [Overview of 11.0](what-is-mariadb-110.md)

**Release date:** 22 Feb 2023

**Do not use non-stable (non-GA) releases in production!**

[MariaDB 11.0](what-is-mariadb-110.md) is the current development series of MariaDB. It is an evolution of [MariaDB 10.11](../../10.11/what-is-mariadb-1011.md) with several entirely new features.

[MariaDB 11.0](what-is-mariadb-110.md) is a [_**Release Candidate (RC)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 11.0**](what-is-mariadb-110.md) **see the**[**What is MariaDB 11.0?**](what-is-mariadb-110.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

### InnoDB

* Remove the global sequence DICT\_HDR\_ROW\_ID for DB\_ROW\_ID ([MDEV-19506](https://jira.mariadb.org/browse/MDEV-19506))
* Remove the [InnoDB change buffer](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-change-buffering) ([MDEV-29694](https://jira.mariadb.org/browse/MDEV-29694))
* Deprecate [innodb\_file\_per\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_file_per_table) ([MDEV-29983](https://jira.mariadb.org/browse/MDEV-29983))
* Set [innodb\_undo\_tablespaces=3](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_undo_tablespaces) by default ([MDEV-29986](https://jira.mariadb.org/browse/MDEV-29986))
* Deprecate [innodb\_flush\_method](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_flush_method) ([MDEV-30136](https://jira.mariadb.org/browse/MDEV-30136))
* Deprecate [innodb\_defragment](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_defragment) and [related parameters](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizing-tables/defragmenting-innodb-tablespaces#innodb-defragmentation) ([MDEV-30544](https://jira.mariadb.org/browse/MDEV-30544))
* InnoDB read-ahead may cause page writes ([MDEV-26790](https://jira.mariadb.org/browse/MDEV-26790))
* Read-ahead unnecessarily allocates and frees pages when a page is in the buffer pool ([MDEV-30216](https://jira.mariadb.org/browse/MDEV-30216))
* [Full-text index](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes) corruption with [system versioning](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables) ([MDEV-25004](https://jira.mariadb.org/browse/MDEV-25004))
* [innodb\_undo\_log\_truncate=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_undo_log_truncate) recovery and backup fixes ([MDEV-29999](https://jira.mariadb.org/browse/MDEV-29999), [MDEV-30179](https://jira.mariadb.org/browse/MDEV-30179), [MDEV-30438](https://jira.mariadb.org/browse/MDEV-30438))
* Upgrade after a crash is not supported ([MDEV-24412](https://jira.mariadb.org/browse/MDEV-24412))
* Remove [InnoDB buffer pool](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-buffer-pool) load throttling ([MDEV-25417](https://jira.mariadb.org/browse/MDEV-25417))
* InnoDB shutdown hangs when the change buffer is corrupted ([MDEV-30009](https://jira.mariadb.org/browse/MDEV-30009))
* `innodb_fast_shutdown=0` fails to report change buffer merge progress ([MDEV-29984](https://jira.mariadb.org/browse/MDEV-29984))
* `mariadb-backup --backup --incremental --throttle=...` hangs ([MDEV-29896](https://jira.mariadb.org/browse/MDEV-29896))
* Crash after recovery, with InnoDB: Tried to read ([MDEV-30132](https://jira.mariadb.org/browse/MDEV-30132))
* Trying to write ... bytes at ... outside the bounds ([MDEV-30069](https://jira.mariadb.org/browse/MDEV-30069))
* TRUNCATE breaks FOREIGN KEY locking ([MDEV-29504](https://jira.mariadb.org/browse/MDEV-29504), [MDEV-29849](https://jira.mariadb.org/browse/MDEV-29849))
* `INFORMATION_SCHEMA.INNODB_TABLESPACES_ENCRYPTION.NAME` is NULL for undo tablespaces ([MDEV-30119](https://jira.mariadb.org/browse/MDEV-30119))
* Fixed hangs and error handling in B-tree operations ([MDEV-29603](https://jira.mariadb.org/browse/MDEV-29603), [MDEV-30400](https://jira.mariadb.org/browse/MDEV-30400))
* InnoDB bulk insert fixes ([MDEV-30047](https://jira.mariadb.org/browse/MDEV-30047), [MDEV-30321](https://jira.mariadb.org/browse/MDEV-30321))
* InnoDB fails to start on `innodb_undo_tablespaces` mismatch ([MDEV-30158](https://jira.mariadb.org/browse/MDEV-30158))
* `mariadb-backup.skip_innodb` crashes when `innodb_undo_tablespaces > 0` ([MDEV-30122](https://jira.mariadb.org/browse/MDEV-30122))

### Galera

* Fixes for cluster wide write conflict resolving ([MDEV-29684](https://jira.mariadb.org/browse/MDEV-29684))

### Replication

* Parallel slave applying in binlog order is corrected for admin class of commands including ANALYZE ([MDEV-30323](https://jira.mariadb.org/browse/MDEV-30323))
* `Seconds_Behind_Master` is showed now more precisely at the slave applier start, including in the delayed mode ([MDEV-29639](https://jira.mariadb.org/browse/MDEV-29639))
* [mariadb-binlog --verbose](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) is made to show the type of compressed columns ([MDEV-25277](https://jira.mariadb.org/browse/MDEV-25277))
* Deadlock is resolved on replica involving `BACKUP STAGE BLOCK_COMMIT` and a committing user XA ([MDEV-30423](https://jira.mariadb.org/browse/MDEV-30423))

### Docker Official Images

* 11.0, unlike previous version, no longer includes mysql named compatible executable symlinks inside the container.

### Packaging

* mysql compatible symlinks are no longer installed in core package, but are delegated to a -compat package ([MDEV-30203](https://jira.mariadb.org/browse/MDEV-30203))
* Use of mysql named executables (except for Windows) will result in a deprecation warning ([MDEV-29582](https://jira.mariadb.org/browse/MDEV-29582))

### General

* Infinite sequence of recursive calls when processing embedded [CTE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions) ([MDEV-30248](https://jira.mariadb.org/browse/MDEV-30248))
* Crash with a query containing nested WINDOW clauses ([MDEV-30052](https://jira.mariadb.org/browse/MDEV-30052))
* Json Range only affects first row of the result set ([MDEV-30304](https://jira.mariadb.org/browse/MDEV-30304))
* In this release repositories for Fedora 37 and Ubuntu 22.10 Kinetic have been added.

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

## Changelog

For a complete list of changes made in [MariaDB 11.0.1](mariadb-11-0-1-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/11.0/mariadb-11-0-1-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 11.0.1](mariadb-11-0-1-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-7-1-rc-and-mariadb-10-6-5-10-5-13-10-4-22-10-3-32-and-10-2-41-now-available/).

**Do not use non-stable (non-GA) releases in production!**

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
