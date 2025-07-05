# MariaDB 10.5.25 Release Notes

The most recent release of [MariaDB 10.5](what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](mariadb-10-5-28-release-notes.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download 10.5.25](https://downloads.mariadb.org/mariadb/10.5.25/)[Release Notes](mariadb-10-5-25-release-notes.md)[Changelog](../changelogs/changelogs-mariadb-105-series/mariadb-10-5-25-changelog.md)[Overview of 10.5](what-is-mariadb-105.md)

**Release date:** 16 May 2024

[MariaDB 10.5](what-is-mariadb-105.md) is a previous _stable_ series of MariaDB, [maintained until](https://mariadb.org/about/#maintenance-policy) June 2025. It is an evolution of [MariaDB 10.4](../../../mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) with several entirely new features not found anywhere else and with backported and reimplemented features from MySQL.

[MariaDB 10.5.25](mariadb-10-5-25-release-notes.md) is a [_**Stable (GA)**_](../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.5**](what-is-mariadb-105.md) **see the**[**What is MariaDB 10.5?**](what-is-mariadb-105.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

From this version, the [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) tool adds a new [sandbox](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mariadb-command-line-client#-sandbox) command to the top of every dump file. This command cannot be interpreted by MariaDB command line client versions that do not have the sandbox command, or by MySQL command line clients, and an error will be generated in these clients. Other methods of importing the dump will work not have this issue.

### Storage Engines

#### InnoDB

* Fix adaptive hash index corruption after [ALTER TABLE…DISCARD TABLESPACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#discard-tablespace) ([MDEV-33400](https://jira.mariadb.org/browse/MDEV-33400))
* Fix fatal InnoDB error or assertion \`\`!is\_v'\` failure upon multi-update with indexed virtual column ([MDEV-31154](https://jira.mariadb.org/browse/MDEV-31154))
* Fix InnoDB: Failing assertion on UPDATE ([MDEV-32346](https://jira.mariadb.org/browse/MDEV-32346))
* Fix fatal error InnoDB: Clustered record field for column x not found ([MDEV-33558](https://jira.mariadb.org/browse/MDEV-33558))
* Fix alter operation hang when encryption thread works on the same tablespace ([MDEV-33770](https://jira.mariadb.org/browse/MDEV-33770))
* Fix MariaDB segfault on rowid filter query involving generated column ([MDEV-33795](https://jira.mariadb.org/browse/MDEV-33795))
* Fix discard/import tablespace, restart, index corruption ([MDEV-33512](https://jira.mariadb.org/browse/MDEV-33512))
* Fix alter table corruption while applying the modification log ([MDEV-19044](https://jira.mariadb.org/browse/MDEV-19044))
* Fix weird read view after ROLLBACK of other transactions ([MDEV-33802](https://jira.mariadb.org/browse/MDEV-33802))
* Read only server no longer throws error when running a create temporary table as select statement ([MDEV-33889](https://jira.mariadb.org/browse/MDEV-33889))
* Change buffer index no longer fails to delete the records ([MDEV-32489](https://jira.mariadb.org/browse/MDEV-32489))
* Fix InnoDB include OS error information when failing to write to iblogfile0 ([MDEV-33397](https://jira.mariadb.org/browse/MDEV-33397))
* In-place migration from MySQL 5.7 no longer causes invalid AUTO\_INCREMENT values ([MDEV-33277](https://jira.mariadb.org/browse/MDEV-33277))
* Fix InnoDB log corruption before upgrading it on startup ([MDEV-32445](https://jira.mariadb.org/browse/MDEV-32445))
* Table no longer gets rebuilt with ALTER TABLE ADD COLUMN ([MDEV-33214](https://jira.mariadb.org/browse/MDEV-33214))

#### [Federated](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/federatedx-storage-engine)

* Fix wrong result on 2nd execution of prepared statement for query with derived table ([MDEV-31361](https://jira.mariadb.org/browse/MDEV-31361))

#### [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider)

* Improve Spider performance by pushing down [TIMESTAMPDIFF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/timestampdiff) function ([MDEV-28992](https://jira.mariadb.org/browse/MDEV-28992)) and [CASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/case-statement) statement ([MDEV-28993](https://jira.mariadb.org/browse/MDEV-28993)) to data nodes
* Fix server crash when deleting partitions from a table with spider engine ([MDEV-33731](https://jira.mariadb.org/browse/MDEV-33731))
* Fix spider plugin init failure with no\_zero\_date sql\_mode ([MDEV-33494](https://jira.mariadb.org/browse/MDEV-33494))
* Fix sql plugin init failure with traditional sql\_mode ([MDEV-33584](https://jira.mariadb.org/browse/MDEV-33584))
* Fix parsing failure on valid left join select by translating the on expression to () ([MDEV-33679](https://jira.mariadb.org/browse/MDEV-33679))
* Fix Spider: ERROR 12710 (HY000): Invalid information from remote table when using [MariaDB 10.5](what-is-mariadb-105.md) local and [MariaDB 10.6](../mariadb-10-6-series/what-is-mariadb-106.md) remote ([MDEV-33777](https://jira.mariadb.org/browse/MDEV-33777))
* Fix Spider: @@insert\_id 128 to TINYINT: Assertion \`\`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())'\` failed. ([MDEV-28105](https://jira.mariadb.org/browse/MDEV-28105))
* Fix bug where [Spider variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) were not available if Spider was loaded upon server startup ([MDEV-33441](https://jira.mariadb.org/browse/MDEV-33441))

### Backup

* [mariadb-backup](broken-reference/) now preserves [innodb\_encrypt\_tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_encrypt_tables) ([MDEV-33334](https://jira.mariadb.org/browse/MDEV-33334))
* Fix [mariadb-backup](broken-reference/) problem on older mariadb (opendir(NULL)) caused by [MDEV-30968](https://jira.mariadb.org/browse/MDEV-30968) ([MDEV-31251](https://jira.mariadb.org/browse/MDEV-31251))
* Fix [mariadb-backup --backup](broken-reference/) FATAL ERROR: ... Can't open datafile cool\_down/t3 ([MDEV-33011](https://jira.mariadb.org/browse/MDEV-33011))
* [mariadb-backup --backup](broken-reference/) now includes retry logic for undo tablespaces ([MDEV-33980](https://jira.mariadb.org/browse/MDEV-33980))
* Fix crash recovery in [mariadb-backup --prepare](broken-reference/) due to insufficient [innodb\_log\_file\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_file_size) ([MDEV-33540](https://jira.mariadb.org/browse/MDEV-33540))
* Fix crash in [mariadb-backup --prepare --export](broken-reference/) after `--prepare` ([MDEV-33023](https://jira.mariadb.org/browse/MDEV-33023))
* [mariadb-backup](broken-reference/) now considers O/S user when `--user` option is omitted ([MDEV-32893](https://jira.mariadb.org/browse/MDEV-32893))

### [Character Sets](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets), [Data Types](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types)

* Fixed improper application of [ORDER BY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/order-by) COLLATE to non-character columns ([MDEV-33318](https://jira.mariadb.org/browse/MDEV-33318))
* Default charset now works with PHP MySQLi extension ([MDEV-32975](https://jira.mariadb.org/browse/MDEV-32975))
* Fixed Bad SEPARATOR value in [GROUP\_CONCAT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/aggregate-functions/group_concat) on character set conversion ([MDEV-33772](https://jira.mariadb.org/browse/MDEV-33772))
* Fixed out of range error in [AVG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/aggregate-functions/avg)([YEAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/year)([datetime](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/datetime))) due to a wrong data type ([MDEV-33496](https://jira.mariadb.org/browse/MDEV-33496))
* Fixed [GREATEST()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/operators/comparison-operators/greatest) and [LEAST()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/operators/comparison-operators/least) problems with [NULLs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/null-values) ([MDEV-21034](https://jira.mariadb.org/browse/MDEV-21034))

#### JSON

* View created via [JSON\_ARRAYAGG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_arrayagg) now returns correct json object ([MDEV-30646](https://jira.mariadb.org/browse/MDEV-30646))
* [JSON\_TYPE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_type) now detects the type of String Values and correctly returns Date/DateTime values ([MDEV-19487](https://jira.mariadb.org/browse/MDEV-19487))
* [JSON\_REMOVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_remove) no longer returns NULL on valid arguments ([MDEV-22141](https://jira.mariadb.org/browse/MDEV-22141))
* [JSON\_EXTRACT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_extract) no longer returns multiple values for same path ([MDEV-32287](https://jira.mariadb.org/browse/MDEV-32287))

### Encryption, TLS, SSL

* WolfSSL's math is unnecessarily slow ([MDEV-33482](https://jira.mariadb.org/browse/MDEV-33482))

### Optimization & Tuning

* Server crashes in JOIN\_CACHE::write\_record\_data upon EXPLAIN with subqueries and constant tables ([MDEV-21102](https://jira.mariadb.org/browse/MDEV-21102))
* Wrong result with cross Join given join order ([MDEV-30975](https://jira.mariadb.org/browse/MDEV-30975))
* Wrong warnings on 2-nd execution of PS for query with GROUP\_CONCAT ([MDEV-31276](https://jira.mariadb.org/browse/MDEV-31276))
* Wrong result with semi-join and splittable derived table ([MDEV-23878](https://jira.mariadb.org/browse/MDEV-23878))
* Aggregation functions fail to leverage uniqueness property ([MDEV-30660](https://jira.mariadb.org/browse/MDEV-30660))

### Plugins

* The [audit plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) now reports the user and host in all cases ([MDEV-33393](https://jira.mariadb.org/browse/MDEV-33393))

### Replication

* \--gtid-ignore-duplicate can double-apply event in case of parallel replication retry ([MDEV-33475](https://jira.mariadb.org/browse/MDEV-33475))
* Server crash in Rows\_log\_event::update\_sequence upon replaying binary log ([MDEV-31779](https://jira.mariadb.org/browse/MDEV-31779))
* Slave crashed:reload\_acl\_and\_cache during shutdown ([MDEV-30260](https://jira.mariadb.org/browse/MDEV-30260))
* When binlog\_annotate\_row\_events on , event of binlog file is truncated ([MDEV-9179](https://jira.mariadb.org/browse/MDEV-9179))

### Galera

* [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) updated to 26.4.18
  * NOTE: Includes increasing the GCS protocol version, which prevents downgrades of individual nodes in the cluster as soon as all nodes have been updated

### SQL, Data Definition, and Data Manipulation

* Transportable Tablespaces no longer leave [AUTO\_INCREMENT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/auto_increment) in a mismatched state ([MDEV-18288](https://jira.mariadb.org/browse/MDEV-18288))
* Fix wrong row targeted with "insert ... on duplicate" and "replace", leading to data corruption ([MDEV-30046](https://jira.mariadb.org/browse/MDEV-30046))
* Fix incorrect DEFAULT expression evaluated in [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) ([MDEV-33790](https://jira.mariadb.org/browse/MDEV-33790))
* Fix incorrect handling of [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) in PS mode when a table's column declared as NOT NULL ([MDEV-33549](https://jira.mariadb.org/browse/MDEV-33549))
* Fix crash in EXECUTE IMMEDIATE 'CREATE OR REPLACE TABLE t1 (a INT DEFAULT ?)' USING DEFAULT ([MDEV-15703](https://jira.mariadb.org/browse/MDEV-15703))
* Fix wrong result on 2nd execution of PS to select from view using derived ([MDEV-31277](https://jira.mariadb.org/browse/MDEV-31277))
* [TIMESTAMP](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/timestamp) value of '1970-01-01 00:00:00' can no longer be indirectly inserted in [strict mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql-mode#strict-mode) ([MDEV-34088](https://jira.mariadb.org/browse/MDEV-34088))
* Fix zero datetime reinterpreting as '1970-01-01 00:00:00' on field\_datetime=field\_timestamp ([MDEV-34069](https://jira.mariadb.org/browse/MDEV-34069))
* unix\_timestamp(coalesce(timestamp\_column)) no longer returns NULL on '1970-01-01 00:00:00.000001' ([MDEV-34061](https://jira.mariadb.org/browse/MDEV-34061))
* Fix crash using UDF in WHERE clause of VIEW ([MDEV-24507](https://jira.mariadb.org/browse/MDEV-24507))
* Fix update for portion changes autoincrement key in period table ([MDEV-25370](https://jira.mariadb.org/browse/MDEV-25370))
* Fix SIGABRT resulting from CREATE TABLE with generated column and RLIKE ([MDEV-21058](https://jira.mariadb.org/browse/MDEV-21058))

### General

#### Scripts & Clients

* It's now possible to disable system commands with the [mariadb --sandbox](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mariadb-command-line-client#-sandbox) option. ([MDEV-21778](https://jira.mariadb.org/browse/MDEV-21778))
* [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) now exports the data with sandbox mode enable, so that the mariadb client will not execute potentially dangerous cli commands.([MDEV-33727](https://jira.mariadb.org/browse/MDEV-33727))
* [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) commands such as `mariadb-dump --dump-slave=2 --master-data=2` now record both positions ([MDEV-4827](https://jira.mariadb.org/browse/MDEV-4827))
* Loading [time zones](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets/internationalization-and-localization/time-zones) now works with [alter\_algorithm](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#alter_algorithm) INPLACE ([MDEV-33044](https://jira.mariadb.org/browse/MDEV-33044)) )

#### Server

* Original IP not shown in network related error messages when proxy\_protocol is in use ([MDEV-33506](https://jira.mariadb.org/browse/MDEV-33506))
* Server incorrectly describes known variables as UNKNOWN if invalid values are specified at startup ([MDEV-33469](https://jira.mariadb.org/browse/MDEV-33469))
* update case insensitive (large) unique key with insensitive change of value - duplicate key ([MDEV-29345](https://jira.mariadb.org/browse/MDEV-29345))
* MariaDB will abort server startup if it finds an invalid parameter, but won't check for other invalid params ([MDEV-26923](https://jira.mariadb.org/browse/MDEV-26923))

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2024-21096](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21096)

## Changelog

For a complete list of changes made in [MariaDB 10.5.25](mariadb-10-5-25-release-notes.md), with links to detailed\
information on each push, see the [changelog](../changelogs/changelogs-mariadb-105-series/mariadb-10-5-25-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.5.25](mariadb-10-5-25-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-11-2-4-11-1-5-11-0-6-10-11-8-10-6-18-10-5-25-10-4-34-now-available/).

{% include "../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
