# MariaDB 10.4.34 Release Notes

[Download](https://mariadb.com/downloads/)[Release Notes](mariadb-10-4-34-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10-4-34-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.4.34/)

**Release date:** 16 May 2024

[MariaDB 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series) is a previous _stable_ series of MariaDB, [maintained until](https://mariadb.org/about/#maintenance-policy) June 2024. It is an evolution of [MariaDB 10.3](../release-notes-mariadb-10-3-series/what-is-mariadb-103.md) with several entirely new features not found anywhere else and with backported and reimplemented features from MySQL.

[MariaDB 10.4.34](mariadb-10-4-34-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

[MariaDB 10.4.34](mariadb-10-4-34-release-notes.md) is the last release of the [MariaDB 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series) release series.

**For an overview of** [**MariaDB 10.4**](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series) **see the**[**What is MariaDB 10.4?**](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

### Storage Engines

#### InnoDB

* Fix adaptive hash index corruption after [ALTER TABLE…DISCARD TABLESPACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#discard-tablespace) ([MDEV-33400](https://jira.mariadb.org/browse/MDEV-33400))
* Fix InnoDB: Failing assertion on UPDATE ([MDEV-32346](https://jira.mariadb.org/browse/MDEV-32346))
* Fix fatal InnoDB error or assertion \`\`!is\_v'\` failure upon multi-update with indexed virtual column ([MDEV-31154](https://jira.mariadb.org/browse/MDEV-31154))
* Fix InnoDB fatal error: Clustered record field for column x not found ([MDEV-33558](https://jira.mariadb.org/browse/MDEV-33558))
* Fix alter operation hang when encryption thread works on the same tablespace ([MDEV-33770](https://jira.mariadb.org/browse/MDEV-33770))
* Fix MariaDB segfault on rowid filter query involving generated column ([MDEV-33795](https://jira.mariadb.org/browse/MDEV-33795))
* Fix discard/import tablespace, restart, index corruption ([MDEV-33512](https://jira.mariadb.org/browse/MDEV-33512))
* Fix alter table corruption while applying the modification log ([MDEV-19044](https://jira.mariadb.org/browse/MDEV-19044))
* Fix weird read view after ROLLBACK of other transactions ([MDEV-33802](https://jira.mariadb.org/browse/MDEV-33802))
* Table no longer gets rebuilt with ALTER TABLE ADD COLUMN ([MDEV-33214](https://jira.mariadb.org/browse/MDEV-33214))

#### RocksDB

* Unsafe use of LOCK\_thd\_kill in my\_malloc\_size\_cb\_func() ([MDEV-33443](https://jira.mariadb.org/browse/MDEV-33443))

#### [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider)

* Improve Spider performance by pushing down [TIMESTAMPDIFF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/timestampdiff) function ([MDEV-28992](https://jira.mariadb.org/browse/MDEV-28992)) and [CASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/case-statement) statement ([MDEV-28993](https://jira.mariadb.org/browse/MDEV-28993)) to data nodes
* Fix sql plugin init failure with traditional sql\_mode ([MDEV-33584](https://jira.mariadb.org/browse/MDEV-33584))
* Fix parsing failure on valid left join select by translating the on expression to () ([MDEV-33679](https://jira.mariadb.org/browse/MDEV-33679))
* Fix Spider: ERROR 12710 (HY000): Invalid information from remote table when using [MariaDB 10.5](../../mariadb-10-5-series/what-is-mariadb-105.md) local and [MariaDB 10.6](../../mariadb-10-6-series/what-is-mariadb-106.md) remote ([MDEV-33777](https://jira.mariadb.org/browse/MDEV-33777))
* Fix bug where [Spider variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) were not available if Spider was loaded upon server startup ([MDEV-33441](https://jira.mariadb.org/browse/MDEV-33441))

### Backup

* [MariaDB Backup](https://mariadb.com/docs/server/server-usage/backup-and-restore/mariadb-backup/) now preserves [innodb\_encrypt\_tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_encrypt_tables) ([MDEV-33334](https://jira.mariadb.org/browse/MDEV-33334))
* Fix [MariaDB Backup](https://mariadb.com/docs/server/server-usage/backup-and-restore/mariadb-backup/) problem on older mariadb (opendir(NULL)) caused by [MDEV-30968](https://jira.mariadb.org/browse/MDEV-30968) ([MDEV-31251](https://jira.mariadb.org/browse/MDEV-31251))
* [mariadb-backup --backup](https://mariadb.com/docs/server/server-usage/backup-and-restore/mariadb-backup) now includes retry logic for undo tablespaces ([MDEV-33980](https://jira.mariadb.org/browse/MDEV-33980))
* Fix crash recovery in mariadb-backup --prepare due to insufficient [innodb\_log\_file\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_file_size) ([MDEV-33540](https://jira.mariadb.org/browse/MDEV-33540))

### [Character Sets](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets), [Data Types](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types)

* Default charset now works with PHP MySQLi extension ([MDEV-32975](https://jira.mariadb.org/browse/MDEV-32975))

### Optimization & Tuning

* Server crashes in JOIN\_CACHE::write\_record\_data upon EXPLAIN with subqueries and constant tables ([MDEV-21102](https://jira.mariadb.org/browse/MDEV-21102))

### Replication

* \--gtid-ignore-duplicate can double-apply event in case of parallel replication retry ([MDEV-33475](https://jira.mariadb.org/browse/MDEV-33475))

### Galera

* [Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera-cluster/README.md) updated to 26.4.18
  * NOTE: Includes increasing the GCS protocol version, which prevents downgrades of individual nodes in the cluster as soon as all nodes have been updated

### SQL, Data Definition, and Data Manipulation

* Fix incorrect DEFAULT expression evaluated in [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) ([MDEV-33790](https://jira.mariadb.org/browse/MDEV-33790))

#### Prepared Statements

* Incorrect handling of UPDATE in PS mode in case a table's colum declared as NOT NULL ([MDEV-33549](https://jira.mariadb.org/browse/MDEV-33549))
* Crash in EXECUTE IMMEDIATE 'CREATE OR REPLACE TABLE t1 (a INT DEFAULT ?)' USING DEFAULT, UBSAN runtime error: member call on null pointer of type 'struct TABLE\_LIST' in Item\_param::save\_in\_field ([MDEV-15703](https://jira.mariadb.org/browse/MDEV-15703))

### General

#### Server

* Original IP not shown in network related error messages when proxy\_protocol is in use ([MDEV-33506](https://jira.mariadb.org/browse/MDEV-33506))

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-`-``#`

## Changelog

For a complete list of changes made in [MariaDB 10.4.34](mariadb-10-4-34-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-10-4-34-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.4.34](mariadb-10-4-34-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-11-2-4-11-1-5-11-0-6-10-11-8-10-6-18-10-5-25-10-4-34-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
