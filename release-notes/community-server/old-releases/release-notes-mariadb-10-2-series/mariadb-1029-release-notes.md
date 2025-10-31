# MariaDB 10.2.9 Release Notes

The most recent release of [MariaDB 10.2](what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.9) | [Release Notes](mariadb-1029-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1029-changelog.md) | [Overview of 10.2](what-is-mariadb-102.md)

**Release date:** 27 Sep 2017

[MariaDB 10.2](what-is-mariadb-102.md) is the current stable series of MariaDB. It is an evolution\
of [MariaDB 10.1](../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.2.9](mariadb-1029-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 10.2**](what-is-mariadb-102.md) **see the**[**What is MariaDB 10.2?**](what-is-mariadb-102.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

### Updates

* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to 5.6.37-82.2

### Bug Fixes

* [MDEV-13899](https://jira.mariadb.org/browse/MDEV-13899): IMPORT TABLESPACE may corrupt ROW\_FORMAT=REDUNDANT tables
* [MDEV-13847](https://jira.mariadb.org/browse/MDEV-13847): Allow ALTER TABLE…ADD SPATIAL INDEX…ALGORITHM=INPLACE
* [MDEV-13678](https://jira.mariadb.org/browse/MDEV-13678): DELETE with CASCADE takes a long time when Galera is enabled
* [MDEV-13826](https://jira.mariadb.org/browse/MDEV-13826): CREATE FULLTEXT INDEX on encrypted table fails
* [MDEV-13318](https://jira.mariadb.org/browse/MDEV-13318): Crash recovery failure after the server is killed during innodb\_encrypt\_log startup
* [MDEV-13488](https://jira.mariadb.org/browse/MDEV-13488): InnoDB writes CRYPT\_INFO even though encryption is not enabled (fixes upgrades from 5.5 to 10.1)
* [MDEV-13437](https://jira.mariadb.org/browse/MDEV-13437): InnoDB fails to return error for XA COMMIT or XA ROLLBACK in read-only mode
* [MDEV-13637](https://jira.mariadb.org/browse/MDEV-13637): InnoDB change buffer housekeeping can cause redo log overrun and possibly deadlocks
* [MDEV-13534](https://jira.mariadb.org/browse/MDEV-13534): InnoDB STATS\_PERSISTENT fails to ignore garbage delete-mark flag on node pointer pages (caused by [MDEV-12698](https://jira.mariadb.org/browse/MDEV-12698))
* [MDEV-13606](https://jira.mariadb.org/browse/MDEV-13606): XA PREPARE transactions should survive innodb\_force\_recovery=1 or 2
* [MDEV-13167](https://jira.mariadb.org/browse/MDEV-13167): InnoDB key rotation is not skipping unused pages
* [MDEV-12988](https://jira.mariadb.org/browse/MDEV-12988): mariadb-backup fails if innodb\_undo\_tablespaces>0
* [MDEV-13471](https://jira.mariadb.org/browse/MDEV-13471): Test failure on innodb.log\_file\_size,4k (fixes Galera when using innodb\_page\_size=4k)
* [MDEV-13684](https://jira.mariadb.org/browse/MDEV-13684): InnoDB race condition between fil\_crypt\_thread and btr\_scrub\_init

### Backup

* `--export` option implemented for [MariaDB backup](https://mariadb.com/docs/server/server-usage/backup-and-restore/mariadb-backup) ([MDEV-13466](https://jira.mariadb.org/browse/MDEV-13466))

### Encryption

* Temporary files created by merge sort and row log are encrypted if [innodb\_encrypt\_log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) is set to `1`, regardless of whether the table encrypted or not ([MDEV-12634](https://jira.mariadb.org/browse/MDEV-12634)).

### Variables

The following variables have been deprecated, and will be removed in a future release ([MDEV-13674](https://jira.mariadb.org/browse/MDEV-13674)):

* [innodb\_mtflush\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables)
* [innodb\_use\_mtflush](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables)

### Security Fixes

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

## Notes

For a complete list of changes made in [MariaDB 10.2.9](mariadb-1029-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1029-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
