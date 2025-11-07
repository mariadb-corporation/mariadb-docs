# MariaDB 11.7.1 Release Notes

{% include "../../../.gitbook/includes/latest-11-7.md" %}

<a href="https://downloads.mariadb.org/mariadb/11.7.1/" class="button primary">Download</a> <a href="mariadb-11-7-1-release-notes.md" class="button secondary">Release Notes</a> <a href="../../changelogs/11.7/mariadb-11-7-1-changelog.md" class="button secondary">Changelog</a> <a href="what-is-mariadb-117.md" class="button secondary">Overview of 11.7</a>

**Release date:** 21 Nov 2024

{% include "../../../.gitbook/includes/non-stable.md" %}

[MariaDB 11.7](what-is-mariadb-117.md) is a [rolling release](../../about/release-model.md). It is an evolution of [MariaDB 11.6](../release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116.md) with several entirely new features.

[MariaDB 11.7.1](mariadb-11-7-1-release-notes.md) is a [_**Release Candidate (RC)**_](../../about/release-criteria.md) release.

Thanks, and enjoy MariaDB!

## Notable Items

### Vectors

* [Vectors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/vectors) are a feature that allow MariaDB Server to perform as a relational vector database. Previously available in the special [Vector preview release](../release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-0-vector-release-notes.md), it has now been added to MariaDB Community Server 11.7.1 with various enhancements ([MDEV-34939](https://jira.mariadb.org/browse/MDEV-34939))
  * Data type VECTOR ([MDEV-33410](https://jira.mariadb.org/browse/MDEV-33410))
  * Conversion functions VEC\_FromText and VEC\_ToText ([MDEV-32886](https://jira.mariadb.org/browse/MDEV-32886))
  * Configuration options ([MDEV-35244](https://jira.mariadb.org/browse/MDEV-35244))
    * [mhnsw\_max\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/vectors/vector-system-variables#mhnsw_max_cache_size) Upper limit for one MHNSW vector index cache
    * [mhnsw\_default\_distance](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/vectors/vector-system-variables#mhnsw_default_distance) Default value for the DISTANCE vector index option
    * [mhnsw\_default\_m](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/vectors/vector-system-variables#mhnsw_default_m) Default value for the M vector index option
    * [mhnsw\_ef\_search](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/vectors/vector-system-variables#mhnsw_ef_search) Defines the minimal number of result candidates to look for in the vector index for ORDER BY … LIMIT N queries.

### Storage Engines

#### InnoDB

* Defaults change - the [innodb\_snapshot\_isolation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_snapshot_isolation) system variable now defaults to ON, previously was OFF ([MDEV-35124](https://jira.mariadb.org/browse/MDEV-35124))
* Fix attempt to read outside the bounds of the file: ./ibdata1 ([MDEV-34453](https://jira.mariadb.org/browse/MDEV-34453))
* Fix MariaDB crash with SIGILL because the OS does not support AVX512 ([MDEV-34565](https://jira.mariadb.org/browse/MDEV-34565))
* Fix deadlock caused by lock\_rec\_unlock\_unmodified() ([MDEV-34690](https://jira.mariadb.org/browse/MDEV-34690))
* Fix duplicate key error in table 'mysql.innodb\_table\_stats' ([MDEV-34207](https://jira.mariadb.org/browse/MDEV-34207))
* Fix possible adaptive hash index corruption with ALTER TABLE...IMPORT TABLESPACE and FULLTEXT SEARCH ([MDEV-35059](https://jira.mariadb.org/browse/MDEV-35059))
* XA prepare now correctly releases unmodified records in non-blocking mode ([MDEV-34466](https://jira.mariadb.org/browse/MDEV-34466))
* Fix contention between secondary index UPDATE and purge due to large innodb\_purge\_batch\_size ([MDEV-34515](https://jira.mariadb.org/browse/MDEV-34515))
* Fix redundant page lookups that hurt performance ([MDEV-34791](https://jira.mariadb.org/browse/MDEV-34791))
* Implement [innodb\_log\_file\_mmap](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_file_mmap) on 64-bit systems for improving ib\_logfile0 reads ([MDEV-34062](https://jira.mariadb.org/browse/MDEV-34062))

#### [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider)

* Fix server crash when calling [spider UDF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-functions) after [aria\_encrypt\_tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria/aria-system-variables#aria_encrypt_tables) is enabled ([MDEV-34682](https://jira.mariadb.org/browse/MDEV-34682))
* SELECT MIN on Spider table no longer returns more rows than expected ([MDEV-26345](https://jira.mariadb.org/browse/MDEV-26345))
* Fix Spider group by handler wrong result on order by aggregate ([MDEV-29546](https://jira.mariadb.org/browse/MDEV-29546))

#### [S3](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine)

* Fix Storage Engine S3 that caused 500 error when using Huawai Cloud S3 and possibly other S3 providers ([MDEV-34867](https://jira.mariadb.org/browse/MDEV-34867))
  * A new option [s3-provider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine/s3-storage-engine-system-variables#s3_provider) has been added. `s3-provider=Huawai` needs to be set for Huawai Cloud S3

### Optimizer

* Fix crash caused by query containing constant having clause ([MDEV-23983](https://jira.mariadb.org/browse/MDEV-23983))
* Fix assertion with optimizer\_join\_limit\_pref\_ratio and 1-table select ([MDEV-35072](https://jira.mariadb.org/browse/MDEV-35072))

### Data Definition - Alter Table

* Fix InnoDB crash under Windows Subsystem for Linux on ALTER TABLE or OPTIMIZE TABLE ([MDEV-34938](https://jira.mariadb.org/browse/MDEV-34938))
* Fix case where modification of the column incorrectly checked foreign key constraint ([MDEV-34392](https://jira.mariadb.org/browse/MDEV-34392))
* Fix incorrect NULL value handling for instantly dropped BLOB columns ([MDEV-35122](https://jira.mariadb.org/browse/MDEV-35122))

### Galera

* Galera updated to 26.4.20
* Fix server crash when setting wsrep\_cluster\_address after adding invalid value to wsrep\_allowlist table ([MDEV-31173](https://jira.mariadb.org/browse/MDEV-31173))
* TOI (ALTER) no longer hangs on a parent table if SR transaction is in progress on a child table ([MDEV-34836](https://jira.mariadb.org/browse/MDEV-34836))
* Fix INSERT...SELECT' on MyISAM table suddenly replicated by alera ([MDEV-34647](https://jira.mariadb.org/browse/MDEV-34647))
* Fix case where with wsrep\_mode=REPLICATE\_ARIA, only part of the mixed-engine transactions was replicated ([MDEV-30653](https://jira.mariadb.org/browse/MDEV-30653))
* Fix galera\_ssl\_reload failure with warning message ([MDEV-32778](https://jira.mariadb.org/browse/MDEV-32778))
* When InnoDB gets an assertion failure, WSREP layer is now handled gracefully ([MDEV-32363](https://jira.mariadb.org/browse/MDEV-32363))

### Backup

* Recovery now correctly notes some log corruption ([MDEV-34802](https://jira.mariadb.org/browse/MDEV-34802))
* InnoDB now correctly merges the change buffer to ROW\_FORMAT=COMPRESSED tables ([MDEV-34879](https://jira.mariadb.org/browse/MDEV-34879))
* Can now selectively restore sequences using innodb tables from backup ([MDEV-32350](https://jira.mariadb.org/browse/MDEV-32350))

### JSON

* [JSON\_TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_table) now properly unquotes strings ([MDEV-27412](https://jira.mariadb.org/browse/MDEV-27412))
* [JSON\_TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_table) default values now allows non-string literals ([MDEV-25822](https://jira.mariadb.org/browse/MDEV-25822))

### UUID

* New function for generating version 4 UUIDs [UUIDv4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/uuid_v4) ([MDEV-11339](https://jira.mariadb.org/browse/MDEV-11339))
* New function for generating version 7 UUIDs [UUIDv7](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/uuid_v7) ([MDEV-32637](https://jira.mariadb.org/browse/MDEV-32637))

### General

* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the last release of [MariaDB 11.7](what-is-mariadb-117.md) for Windows 11 22H2
* [mariadbd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) no longer hangs on startup when --init-file target does not exist ([MDEV-34814](https://jira.mariadb.org/browse/MDEV-34814))
* LOAD DATA INFILE with geometry data no longer fails ([MDEV-34883](https://jira.mariadb.org/browse/MDEV-34883))
* Fix heap-use-after-free in group\_concat with compressed or GIS columns ([MDEV-16699](https://jira.mariadb.org/browse/MDEV-16699))
* Fix assertion \`!is\_cond()' failed in Item\_bool\_func::val\_int / do\_select ([MDEV-35135](https://jira.mariadb.org/browse/MDEV-35135))
* Trigger now works correctly with bulk update ([MDEV-34718](https://jira.mariadb.org/browse/MDEV-34718))
* Fix assertion failure in find\_producing\_item upon a query from a view ([MDEV-35276](https://jira.mariadb.org/browse/MDEV-35276))
* Add new setting, [--quick-max-column-width](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mariadb-command-line-client#-quick-max-column-widthn) to the mariadb client for use in --quick mode ([MDEV-34704](https://jira.mariadb.org/browse/MDEV-34704))

## Changelog

For a complete list of changes made in [MariaDB 11.7.1](mariadb-11-7-1-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/11.7/mariadb-11-7-1-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 11.7.1](mariadb-11-7-1-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-11-6-2-and-mariadb-11-7-1-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
