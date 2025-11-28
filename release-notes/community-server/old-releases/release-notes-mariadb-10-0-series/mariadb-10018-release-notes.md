# MariaDB 10.0.18 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.18) | [Release Notes](mariadb-10018-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10018-changelog.md) | [Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 7 May 2015

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is the current stable series of MariaDB. It is an evolution of [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) with several entirely new features not found anywhere else and with\
backported and reimplemented features from MySQL 5.6.

[MariaDB 10.0.18](mariadb-10018-release-notes.md) is a [_**Stable**_](../../about/release-criteria.md) (_GA_) release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

In addition to the [MariaDB-5.5.43](../release-notes-mariadb-5-5-series/mariadb-5543-release-notes.md) fixes and improvements, the following fixes and improvements have been made to [MariaDB 10.0.18](mariadb-10018-release-notes.md).

* [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) updated to 5.6.24
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to XtraDB-5.6.23-72.1
* [Innodb](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) updated to InnoDB-5.6.24
* [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) updated to 3.2.21
* [Mroonga](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/mroonga) updated to 5.02
* [Audit Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) upgraded to 1.3.0, including the QUERY\_DCL filter option.

### Parser

* Fixed unrecognised column quoted with backticks in a function in a HAVING clause ([MDEV-7301](https://jira.mariadb.org/browse/MDEV-7301)).
* [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) with conflicting CHARACTER SET and CONVERT TO CHARACTER SET arguments now reports error ([MDEV-7386](https://jira.mariadb.org/browse/MDEV-7386)).
* Fixed Regression (from 10.0.14): Bit and hex string literals changed column names ([MDEV-7629](https://jira.mariadb.org/browse/MDEV-7629)).

### Optimizer

* Merged [derived tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimizations-for-derived-tables)/VIEWs incorrectly increment [created\_tmp\_tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-status-variables#created_tmp_tables) ([MDEV-7586](https://jira.mariadb.org/browse/MDEV-7586)).

### Alter Table

* Some symbols in table name can cause to Error Code: 1050 when created FK. Table name is on filename charset but foreign key identifiers are not. This lead incorrect foreign key identifier number to be used ([MDEV-7627](https://jira.mariadb.org/browse/MDEV-7627)).
* [ALTER \[ONLINE\] TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) with no options no longer requires a table copy ([MDEV-7390](https://jira.mariadb.org/browse/MDEV-7390)).
* Fixed a case where it was impossible to create copy of a table if the table contained a default value for timestamp field in [sql\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode)="NO\_ZERO\_DATE" ([MDEV-7778](https://jira.mariadb.org/browse/MDEV-7778)).

### Other SQL Commands

* [INSTALL PLUGIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin) can now be done in bootstrap mode where authentication is disabled ([MDEV-7781](https://jira.mariadb.org/browse/MDEV-7781)).
* Corrected error handing in [AES\_ENCRYPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_encrypt)/[AES\_DECRYPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/aes_decrypt) where incorrect data could result in a SSL client connection being terminated ([MDEV-7697](https://jira.mariadb.org/browse/MDEV-7697)).
* Corrected Assertion \`status\_var.memory\_used == 0' failed in THD::THD() on disconnect after executing [EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain) for multi-table [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) ([MDEV-7038](https://jira.mariadb.org/browse/MDEV-7038)).
* Fixed crash when dropping user within rebuild\_role\_grants which occurs in some cases in [SHOW GRANTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-grants) and [DROP ROLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/drop-role) ([MDEV-7774](https://jira.mariadb.org/browse/MDEV-7774)).
* [SHOW GRANTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-grants) now shows the password for users that have the password field set, auth\_string field empty, plugin=mysql\_native\_password ([MDEV-7985](https://jira.mariadb.org/browse/MDEV-7985)).

### Innodb

* In Debug builds, an assertion could be triggered on really large blobs ([MDEV-7754](https://jira.mariadb.org/browse/MDEV-7754)).
* Fixed segfault when a virtual column used on an Innodb table and an index was created on a field after the virtual column ([MDEV-7367](https://jira.mariadb.org/browse/MDEV-7367)).
* Fixed server crash when inserting more rows than available space on disk ([MDEV-7685](https://jira.mariadb.org/browse/MDEV-7685)).
* Now possible to get Innodb internal primary key for wrapper type storage engines ([MDEV-7714](https://jira.mariadb.org/browse/MDEV-7714)).

### Replication

* Starting with this release, commits in certain instances in parallel replication complete immediately, avoiding losing throughput when many transactions need conflicting locks. See [binlog\_commit\_wait\_count](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) ([MDEV-7847](https://jira.mariadb.org/browse/MDEV-7847) / [MDEV-7882](https://jira.mariadb.org/browse/MDEV-7882)).
* Fixed parallel replication worker threads that hung in some cases with non-transactional event groups ([MDEV-7929](https://jira.mariadb.org/browse/MDEV-7929)).
* Fixed parallel replication error where deadlock was incorrectly handled ([MDEV-8031](https://jira.mariadb.org/browse/MDEV-8031)).
* Fixed replication aborting on [DROP /\*!40005 TEMPORARY \*/ TABLE IF EXISTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table) ([MDEV-8016](https://jira.mariadb.org/browse/MDEV-8016)).
* Fixed replication of temporary tables in statement mode that are grouped - fix [MDEV-7668](https://jira.mariadb.org/browse/MDEV-7668) wasn't sufficient ([MDEV-7936](https://jira.mariadb.org/browse/MDEV-7936)).
* Fixed [ANALYZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/analyze-table) which was ordered incorrectly in the binlog ([MDEV-7888](https://jira.mariadb.org/browse/MDEV-7888)).
* Added more detailed information about errors when GTID mode IO threads fail to connect ([MDEV-7975](https://jira.mariadb.org/browse/MDEV-7975)).
* Fixed temporary tables lost at [STOP SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica) in GTID mode if master has not rotated binlog since restart ([MDEV-6403](https://jira.mariadb.org/browse/MDEV-6403)).
* Fixed incorrect relay log start position when restarting SQL thread after error in parallel replication ([MDEV-6589](https://jira.mariadb.org/browse/MDEV-6589)).
* Fixed problem where slave was 10x slower to execute a set of statements compared to the master when using RBR ([MDEV-7578](https://jira.mariadb.org/browse/MDEV-7578)).
* Parallel replication worker threads are not spawned until needed (when an SQL thread is started), and they will be de-spawned if all SQL threads are stopped ([MDEV-5289](https://jira.mariadb.org/browse/MDEV-5289)).
* Multilevel slaves with parallel replication - better logic resulted in performance increase to group more transactions at the first slave level resulting in increased parallelism at the second replication level ([MDEV-7249](https://jira.mariadb.org/browse/MDEV-7249)).
* Fixed problem where Intermediate master groups using [CREATE TEMPORARY TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) with [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) could cause the [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) to occur before the TEMPORARY TABLE it operates on, causing parallel replication failure ([MDEV-7668](https://jira.mariadb.org/browse/MDEV-7668)).
* Slave SQL: stopping replication on a non-last RBR event with annotations no longer results in segfaults ([MDEV-7864](https://jira.mariadb.org/browse/MDEV-7864)).
* [MASTER\_POS\_WAIT(log\_name,log\_pos,timeout,"connection\_name")](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/master_pos_wait) when connection name is specified now respects the timeout ([MDEV-7130](https://jira.mariadb.org/browse/MDEV-7130)).
* New status variables [binlog\_group\_commit\_trigger\_count](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-status-variables#binlog_group_commit_trigger_count), [binlog\_group\_commit\_trigger\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-status-variables#binlog_group_commit_trigger_timeout), and [binlog\_group\_commit\_trigger\_lock\_wait](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-status-variables#binlog_group_commit_trigger_lock_wait) used to examine which triggers caused a group commit to be made ([MDEV-7802](https://jira.mariadb.org/browse/MDEV-7802)).
* Fixed seconds\_behind\_master display in [SHOW SLAVE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status) which occasionally returned 0 when it really was much higher ([MDEV-5114](https://jira.mariadb.org/browse/MDEV-5114)).

### Platforms

* PowerPC - fixed Innodb locking issue under high load - ([MDEV-7148](https://jira.mariadb.org/browse/MDEV-7148)).
* BigEndian now builds in [Cassandra](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/cassandra) storage engine ([MDEV-7839](https://jira.mariadb.org/browse/MDEV-7839)).
* Fixed crash when running MariaDB Debug with InnoDB on Windows ([MDEV-8079](https://jira.mariadb.org/browse/MDEV-8079)).

### Connect Engine

* [CONNECT Engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect) Column names are now retrieved properly when field values are not latin1 characters ([MDEV-7521](https://jira.mariadb.org/browse/MDEV-7521)).
* Fixed problem where connecting to missing remote table caused error that was re-reported when [SHOW TABLE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-table-status) on a correctly formed table ([MDEV-7636](https://jira.mariadb.org/browse/MDEV-7636)).
* Fixed problem where CONNECT returned error 174 on query to MS SQL Server 2012 involving [timestamp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/timestamp) column when the condition is given as a [date literal](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sql-language-structure/date-and-time-literals) ([MDEV-7840](https://jira.mariadb.org/browse/MDEV-7840)).
* CONNECT now works with if(exists(select \* from test)) statement in procedures ([MDEV-7852](https://jira.mariadb.org/browse/MDEV-7852)).
* Fixed user variable assignment with SET @var = that resulted in ERROR 1148 (42000): CONNECT Unsupported command ([MDEV-7616](https://jira.mariadb.org/browse/MDEV-7616)).
* Removed assertion in delete\_or\_rename\_table that caused crashes on (XML) HTML tables ([MDEV-7935](https://jira.mariadb.org/browse/MDEV-7935)).
* Added UDF [Json\_Array\_Delete](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect/connect-table-types/connect-json-table-type) ([MDEV-7935](https://jira.mariadb.org/browse/MDEV-7935)).
* Fixed a problem where defining indexes on a connect engine caused wrong results ([MDEV-8090](https://jira.mariadb.org/browse/MDEV-8090)).

### OQ Graph Engine

* Fixed issue with incorrect handling of multiple threads ([MDEV-6282](https://jira.mariadb.org/browse/MDEV-6282), [MDEV-6345](https://jira.mariadb.org/browse/MDEV-6345) and [MDEV-6784](https://jira.mariadb.org/browse/MDEV-6784)).

### Other

* SSL connections increased from 512 to 1024 bits in Diffie-Hellman exchange to support fips ([MDEV-7794](https://jira.mariadb.org/browse/MDEV-7794)).
* Fixed problem where SSL read/write timeouts were 1000 times too high due to seconds/milliseconds error ([MDEV-8096](https://jira.mariadb.org/browse/MDEV-8096)).
* OpenSSL now uses MD5 even if FIPS prohibited it, fixing a previous crash. This is fine as MD5 is not used for cryptographical\
  purposes (md5 is used internally for P\_S message digests and for view checksums) ([MDEV-7788](https://jira.mariadb.org/browse/MDEV-7788)).
* Fixed problem where Initialization of status variables was not invoked for embedded (no bug reference. [code change](https://github.com/MariaDB/server/commit/e6d918cacba8c5f3b002c4eb0244f44c3c941818))
* Corrected wrong results with bigint when compiled with gcc 5.0 ([MDEV-7973](https://jira.mariadb.org/browse/MDEV-7973)).
* Fixed assertion in Protocol::end\_statement where [CREATE VIEW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/views/create-view) occured after another connection aborted ([MDEV-8045](https://jira.mariadb.org/browse/MDEV-8045)).

### Client

* Fixed MariaDB client where it could hang in an infinite loop based on no IO data returned ([MDEV-8014](https://jira.mariadb.org/browse/MDEV-8014)).

### Security Fixes

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2014-8964](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-8964) / [CVE-2015-2325](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-2325) / [CVE-2015-2326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-2326) bundled PCRE contained heap-based buffer overflow vulnerability that allowed the server to crash or have other unspecified impact via a crafted regular expression made possible with the [REGEXP\_SUBSTR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/regexp_substr) function ([MDEV-8006](https://jira.mariadb.org/browse/MDEV-8006)).
  * [CVE-2015-0501](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-0501)
  * [CVE-2015-2571](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-2571)
  * [CVE-2015-0505](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-0505)
  * [CVE-2015-0499](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-0499)
  * [CVE-2015-4757](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4757)
  * [CVE-2015-4866](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4866)

### New and Deprecated Distributions

As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will\
be the final release of [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) for Fedora 19 "Schrödinger's Cat", Ubuntu\
10.04 LTS "Lucid", and Mint 9 LTS "Isadora". When the next\
version of [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is released, repositories for these distributions will\
go away.

We have also added a couple of new Linux distributions with this release. Both\
Fedora 21 and Ubuntu 15.04 "Vivid" repositories are now available. As this is\
the first release with these repositories, they are considered experimental.\
Please [let us know](https://mariadb.org/jira) if you run into any issues with\
them.

For a complete list of changes made in [MariaDB 10.0.18](mariadb-10018-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10018-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
