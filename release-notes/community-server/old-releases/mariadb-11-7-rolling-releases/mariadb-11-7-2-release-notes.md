# MariaDB 11.7.2 Release Notes

<a href="https://downloads.mariadb.org/mariadb/11.7.2/" class="button primary">Download</a> <a href="mariadb-11-7-2-release-notes.md" class="button secondary">Release Notes</a> <a href="../../changelogs/changelogs-mariadb-11-7-series/mariadb-11-7-2-changelog.md" class="button secondary">Changelog</a> <a href="what-is-mariadb-117.md" class="button secondary">Overview of 11.7</a>

**Release date:** 13 Feb 2025

[MariaDB 11.7.2](mariadb-11-7-2-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release. It is an evolution of [MariaDB 11.6](../release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116.md) with several entirely new features.

[MariaDB 11.7](what-is-mariadb-117.md) is a [rolling release](../../about/release-model.md). One is expected to upgrade to [MariaDB 11.8.2](../../mariadb-11-8-series/mariadb-11-8-2-release-notes.md), there will be no 11.7.3.

Thanks, and enjoy MariaDB!

## Notable Items

### Storage Engines

#### [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb)

* Fix possible InnoDB hang while running out of buffer pool ([MDEV-35409](https://jira.mariadb.org/browse/MDEV-35409))
* Fix assertion failure on cascading foreign key update of table with vcol index in parent ([MDEV-29182](https://jira.mariadb.org/browse/MDEV-29182))
* Fix potential issue in secondary Index with ROW\_FORMAT=COMPRESSED and Change buffering enabled ([MDEV-35679](https://jira.mariadb.org/browse/MDEV-35679))
* Fix issue where ON UPDATE SET NULL could not be specified on a NOT NULL column ([MDEV-35445](https://jira.mariadb.org/browse/MDEV-35445))
* New parameter --skip-freed-pages for [Innochecksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/innochecksum). Use this parameter to not get freed undo logs reported as existing undo log pages. ([MDEV-35394](https://jira.mariadb.org/browse/MDEV-35394))
* Cloning of table statistics while saving the InnoDB table stats is now avoided ([MDEV-35363](https://jira.mariadb.org/browse/MDEV-35363))
* InnoDB deadlock output query length increased to improve visibility of deadlocked statements. ([MDEV-32576](https://jira.mariadb.org/browse/MDEV-32576))
* [ALTER TABLE...IMPORT TABLESPACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#import-tablespace) now works with INDEX DESC ([MDEV-35169](https://jira.mariadb.org/browse/MDEV-35169))
* Fix occasional failure of recovery of a multi-batch operation with InnoDB on startup ([MDEV-35699](https://jira.mariadb.org/browse/MDEV-35699))

#### [Memory](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/memory-storage-engine)

* Fix possible crash on DELETE from a HEAP table ([MDEV-22695](https://jira.mariadb.org/browse/MDEV-22695))

#### [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider)

* Fix possible Spider thread hang in 'Update' state on 2nd INSERT ([MDEV-35064](https://jira.mariadb.org/browse/MDEV-35064))
* Fix possible crash on bootup in spider\_sys\_open\_table «ext-issue»«[MDEV-32822](https://jira.mariadb.org/browse/MDEV-32822)», «ext-issue»«[MDEV-34302](https://jira.mariadb.org/browse/MDEV-34302)» ([MDEV-34925](https://jira.mariadb.org/browse/MDEV-34925))

### [Character Sets and Collations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets)

* 44 new [collations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations#collations) added. These are aliases for MySQL collations to make it easier to replicate from MySQL to MariaDB ([MDEV-35256](https://jira.mariadb.org/browse/MDEV-35256))
  * The [Information Schema Collations table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-collations-table) includes a new column, `COMMENT` which contains information about which collation the alias refers to.
* Fix assertion falilure and possible index corruption with unique key and nopad collation without DESC or HASH keys ([MDEV-30111](https://jira.mariadb.org/browse/MDEV-30111))
* Fix client crash the command after client sets character set to utf32 ([MDEV-34090](https://jira.mariadb.org/browse/MDEV-34090))
* Fix possible runtime error caused by XA RECOVER applying a zero offset to a null pointer ([MDEV-35549](https://jira.mariadb.org/browse/MDEV-35549))
* Fix issue where functions in default values in tables with certain character sets could break SHOW CREATE and mariadb-dump ([MDEV-29968](https://jira.mariadb.org/browse/MDEV-29968))

### [Replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication)

* Fix incorrect formatting of timestamp during [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) parsing of a binary log, causing point in time recovery discrepancies ([MDEV-31761](https://jira.mariadb.org/browse/MDEV-31761))
* [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog/mariadb-binlog-options) can now correctly process more than one logfile when --stop-datetime is specified ([MDEV-35528](https://jira.mariadb.org/browse/MDEV-35528))
* Setting `pseudo_thread_id` to a value exceeding 4 bytes previously resulted in truncation when written to the binary log ([MDEV-35646](https://jira.mariadb.org/browse/MDEV-35646))
* MariaDB now supports MySQL 8.0 binlog events, including PARTIAL\_UPDATE\_ROWS\_EVENT, TRANSACTION\_PAYLOAD\_EVENT, and HEARTBEAT\_LOG\_EVENT\_V2. ([MDEV-35643](https://jira.mariadb.org/browse/MDEV-35643))
* [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) no longer ignores binary log events written with system timestamp 4294967295 and possibly all following events, avoiding potential data loss during recovery from binlogs ([MDEV-33239](https://jira.mariadb.org/browse/MDEV-33239))
* Table flags, preserved from the old storage engine after changing the storage engine of a table, can no longer break replication ([MDEV-31794](https://jira.mariadb.org/browse/MDEV-31794))
* Fix issue where [START](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/start-replica)/[STOP](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica) ALL REPLICAS errors without returning an error if the command could be executed due to wrong privileges. ([MDEV-21858](https://jira.mariadb.org/browse/MDEV-21858))

### Optimizer

* Fix server crash in get\_sort\_by\_table/make\_join\_statistics after INSERT into a view with ORDER BY ([MDEV-29935](https://jira.mariadb.org/browse/MDEV-29935))
* Fix failing assertion causing disruption and replication failure ([MDEV-24035](https://jira.mariadb.org/browse/MDEV-24035))
* Conditions with SP local variables are now pushed into derived table. Previous behaviour caused slow performance and table scans instead of using the pushed down condition ([MDEV-35910](https://jira.mariadb.org/browse/MDEV-35910))
* NULL-aware materialization with IN predicate and single column no longer skips building sorted Ordered\_key structures ([MDEV-34665](https://jira.mariadb.org/browse/MDEV-34665))
* Fix possibly wrong result using a degenerated subquery (SELECT ) with window function ([MDEV-35869](https://jira.mariadb.org/browse/MDEV-35869))

### [Partitioning](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/partitioning-tables)

* History is now stored on the same partitions on different Galera nodes when system versioning is enabled ([MDEV-35096](https://jira.mariadb.org/browse/MDEV-35096))
* Fix possible hang or crash during InnoDB purge with HASH indexes during ALTER TABLE ([MDEV-25654](https://jira.mariadb.org/browse/MDEV-25654))
* EXCHANGE PARTITION now works for tables with unique blobs ([MDEV-35612](https://jira.mariadb.org/browse/MDEV-35612))
* algorithm = instant can now correctly be used if a table has partitions and one tries to change a column with an index which is not the partitions key. This previously gave the error "ERROR 1846 (0A000): ALGORITHM=INSTANT is not supported. Reason: ADD INDEX. Try ALGORITHM=NOCOPY". ([MDEV-34813](https://jira.mariadb.org/browse/MDEV-34813))

### [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/)

* [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) updated to 26.4.21
  * NOTE: Includes increasing the GCS protocol version, which prevents downgrades of individual nodes in the cluster as soon as all nodes have been updated
* Fix streaming replication transaction crash with innodb\_snapshot\_isolation ([MDEV-35281](https://jira.mariadb.org/browse/MDEV-35281))
* Fix sporadic failure of async replication on Galera async replica nodes with parallel replication enabled ([MDEV-35465](https://jira.mariadb.org/browse/MDEV-35465))
* Fix possible failure of wsrep\_sst\_rsync SST script if user specified aria\_log\_dir\_path different from default data directory ([MDEV-35387](https://jira.mariadb.org/browse/MDEV-35387))
* Fix cluster node hang during shutdown if threadpool is used ([MDEV-35710](https://jira.mariadb.org/browse/MDEV-35710))
* MariaDB Cluster and ALTER INPLACE running in Total Order Isolation (wsrep\_OSU\_method=TOI) now correctly abort a DML INSERT operation in InnoDB ([MDEV-33064](https://jira.mariadb.org/browse/MDEV-33064))
* Fix possible crash in wsrep\_check\_sequence ([MDEV-33245](https://jira.mariadb.org/browse/MDEV-33245))
* Fix sporadic reporting of success when a deadlock error occurs under --ps-protocol BF aborted transaction ([MDEV-35446](https://jira.mariadb.org/browse/MDEV-35446))
* Rows in table mysql.gtid\_slave\_pos are now correctly deleted on Galera nodes when wsrep\_gtid\_mode = 1 is used, which previously lead to wrong information about replica delays ([MDEV-34924](https://jira.mariadb.org/browse/MDEV-34924))
* Undefined behavior could occur when attempting to perform INSERT DELAYED on a Galera cluster node. ([MDEV-35852](https://jira.mariadb.org/browse/MDEV-35852))
* Fix issue where DROP TABLE on child and UPDATE of parent table can cause a metadata lock BF-BF\
  conflict when applied concurrently. ([MDEV-35018](https://jira.mariadb.org/browse/MDEV-35018))
* Galera protocol versions are now shown by show status - change available with installation of galera library 26.4.21+ ([MDEV-35505](https://jira.mariadb.org/browse/MDEV-35505))
* Fix possible crash in wsrep\_sst\_mariadb-backup script when upgrading node in cluster from 10.11.9 to 10.11.10. ([MDEV-35526](https://jira.mariadb.org/browse/MDEV-35526))
* wsrep\_sst\_mariadb-backup.sh no longer uses --use-memory default (100MB) resulting in prepare stage which could take hours ([MDEV-35749](https://jira.mariadb.org/browse/MDEV-35749))

### [Audit Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin)

* For an authentication with the [ed25519 authentication plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-ed25519) the password of the CREATE USER statement is now masked in the audit log ([MDEV-35507](https://jira.mariadb.org/browse/MDEV-35507))
* MariaDB Audit now detects all DCLs forms for masking a password ([MDEV-35522](https://jira.mariadb.org/browse/MDEV-35522))

### [Vector search](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/vectors)

* Adding a regular index on a vector column leads to invalid table structure ([MDEV-35792](https://jira.mariadb.org/browse/MDEV-35792))
* Vector values become zero after [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) / restore, impacting data integrity for vector columns. ([MDEV-35221](https://jira.mariadb.org/browse/MDEV-35221))
* Server can crash when a SELECT query is including a DISTINCT and ORDER BY, and a vector index is used ([MDEV-35793](https://jira.mariadb.org/browse/MDEV-35793))

### General

* Fix possible crash where server could not construct a geomery object from the input ([MDEV-33987](https://jira.mariadb.org/browse/MDEV-33987))
* Fix trigger created with "[CREATE TRIGGER `table1_after_insert` AFTER INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/triggers-events/triggers/create-trigger)" which is adding rows to another table using "FOR EACH ROW insert into table2(`id`, `name`) values (NEW.`id`, NEW.`name`);" that did not work correctly when if bulk inserts are used by the application. Only the first row of the bulk insert would be added to the table ([MDEV-34958](https://jira.mariadb.org/browse/MDEV-34958))
* After changing the table definition for the system table 'mysql.servers', a following execution of CREATE SERVER would previously lead to a server crash.
  * NOTE: System tables should never be modified by a user anyhow ([MDEV-33783](https://jira.mariadb.org/browse/MDEV-33783))
* Fix connection hang after query on a partitioned table with UNION and LIMIT ROWS EXAMINED ([MDEV-35571](https://jira.mariadb.org/browse/MDEV-35571))
* Fix possible crash during index traversal using `tree_search_next`. ([MDEV-28130](https://jira.mariadb.org/browse/MDEV-28130))
* FIx assertion failure where CURRENT\_USER was not correctly copied during condition pushdown\
  ([MDEV-35090](https://jira.mariadb.org/browse/MDEV-35090))
* START TRANSACTION, when triggering an implicit commit as a COMMIT or ROLLBACK has not been executed before, now resets optional characteristics added to the last START TRANSACTION command ([MDEV-35335](https://jira.mariadb.org/browse/MDEV-35335))
* sql\_mode='NO\_UNSIGNED\_SUBTRACTION' now works for multiple unsigned integers ([MDEV-35651](https://jira.mariadb.org/browse/MDEV-35651))
* The "Failed to write to mysql.slow\_log" error no longer shown without a detailed reason for the error ([MDEV-20281](https://jira.mariadb.org/browse/MDEV-20281))
* Fix doublewrite recovery of innodb\_checksum\_algorithm=full\_crc32 encrypted pages ([MDEV-34898](https://jira.mariadb.org/browse/MDEV-34898))
* Can now correctly add a foreign key on a table with a long UNIQUE multi-column index that contains a foreign key as a prefix ([MDEV-33658](https://jira.mariadb.org/browse/MDEV-33658))
* During an online table rebuild of an InnoDB statistics table, opt\_search\_plan\_for\_table() no longer sometimes degrades to full table scan ([MDEV-35443](https://jira.mariadb.org/browse/MDEV-35443))
* Fix debian-start script failure when using non-standard socket path ([MDEV-35907](https://jira.mariadb.org/browse/MDEV-35907))
* Fix possible hang or crash where zero offset applied to null pointer ([MDEV-35864](https://jira.mariadb.org/browse/MDEV-35864))
* Fixed issue where ST\_PointFromWKB ignored SRID parameter and returned 0 ([MDEV-32619](https://jira.mariadb.org/browse/MDEV-32619))
* Fix possible hang during CREATE TABLE…SELECT error handling, especially with innodb\_snapshot\_isolation enabled ([MDEV-35647](https://jira.mariadb.org/browse/MDEV-35647))
* Fix incorrect locking order of LOCK\_log/LOCK\_commit\_ordered and LOCK\_global\_system\_variables ([MDEV-29744](https://jira.mariadb.org/browse/MDEV-29744))
* Fix rare cases where binlog entries could receive incorrect timestamps on secondary nodes of a Galera cluster, potentially impacting replication accuracy ([MDEV-35157](https://jira.mariadb.org/browse/MDEV-35157))
* Fix possible memory leak on SHUTDOWN ([MDEV-35326](https://jira.mariadb.org/browse/MDEV-35326))
* Fix possible memory leak while shutting down server after installing the auth\_gssapi plugin ([MDEV-35575](https://jira.mariadb.org/browse/MDEV-35575))
* Fix possible server crash when using INSERT DELAYED on tables with virtual columns. ([MDEV-26891](https://jira.mariadb.org/browse/MDEV-26891))
* Fix possible Spider crash or hang when the first byte of a connection key is changed ([MDEV-34849](https://jira.mariadb.org/browse/MDEV-34849))
* A BEFORE INSERT Trigger previously returned with error ""Field 'xxx' doesn't have a default value", if a NULL value is added for a column defined NOT NULL without explicit value and no DEFAULT specified ([MDEV-19761](https://jira.mariadb.org/browse/MDEV-19761))
* Calling a stored routine that executes a join on three or more tables and referencing not-existent column name in the USING clause could previously result in a crash on its second invocation. ([MDEV-24935](https://jira.mariadb.org/browse/MDEV-24935))
* Fix rare cases where binlog entries could receive incorrect timestamps on secondary nodes of a Galera cluster, potentially impacting replication accuracy ([MDEV-35157](https://jira.mariadb.org/browse/MDEV-35157))
* Comparison of UUID v1 and V6 could return incorrect results ([MDEV-35468](https://jira.mariadb.org/browse/MDEV-35468))
* INSERT SELECT on NOT NULL columns with BEFORE UPDATE trigger can fail with error 1048 (23000) ([MDEV-36026](https://jira.mariadb.org/browse/MDEV-36026))
* It was not possible to use a package body variable as a fetch target, instead error "Undeclared variable" was returned. ([MDEV-36047](https://jira.mariadb.org/browse/MDEV-36047))
* Validation of SSL certificate fails for mariadb-backup. For a MariaDB Cluster (Galera) SST operations can be affected ([MDEV-35368](https://jira.mariadb.org/browse/MDEV-35368))

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2025-21490](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21490)

## Changelog

For a complete list of changes made in [MariaDB 11.7.2](mariadb-11-7-2-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-11-7-series/mariadb-11-7-2-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 11.7.2](mariadb-11-7-2-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-11-7-2-and-mariadb-11-8-1-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
