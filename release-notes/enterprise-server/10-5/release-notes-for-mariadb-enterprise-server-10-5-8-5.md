# Release Notes for MariaDB Enterprise Server 10.5.8-5

This fifth release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.5 is a maintenance release. This release includes security fixes.

MariaDB Enterprise Server 10.5.8-5 was released on 2020-12-14.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/cve.org) link) | CVSS base score                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [CVE-2020-14765](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14765)                                                                                               | 6.5                                                                           |
| [CVE-2022-21427](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21427)                                                                                               | 4.9                                                                           |
| [CVE-2020-14812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14812)                                                                                               | 4.9                                                                           |
| [CVE-2020-14789](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14789)                                                                                               | 4.9                                                                           |
| [CVE-2020-14776](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14776)                                                                                               | 4.9                                                                           |
| [CVE-2020-28912](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28912)                                                                                               | N/A (Critical)[#1](release-notes-for-mariadb-enterprise-server-10-5-8-5.md#1) |

`#1`:\
MariaDB CVEs are assigned a word rating instead of a CVSS base score. See the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies) for details.

## Notable Changes

* A new privilege [REPLICA MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replica-monitor) has been introduced with this version to fix a problem when upgrading to 10.5. A replica user couldn't run [SHOW REPLICA STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status). Upgrades from 10.4 to 10.5 now adjust the privileges automatically. The new privilege needs to be added manually for a replica user when updating from an earlier 10.5 version. For more information on MariaDB Enterprise Server 10.5 privileges, see "Privileges Comparison ES10.4 and ES10.5.8-5".
  * Users of MariaDB MaxScale's MariaDB Monitor upgrading from a prior version of MariaDB Enterprise Server 10.5 who have used the new 10.5 privileges must ensure the updated privilege has been granted to the MaxScale user and Replication user. For detailed privilege information, see Configuring MariaDB Monitor's User Account.
* Galera `wsrep` library updated to 26.4.6 in [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md).
* The [audit plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) (not MariaDB Enterprise Audit) did not log proxy users. The new plugin version 2.0.3 introduces an event sub-type PROXY\_CONNECT for event type CONNECT. ([MDEV-19443](https://jira.mariadb.org/browse/MDEV-19443))
  * On connect, if a proxy user is used, an extra line will be logged: `TIME,HOSTNAME,user,localhost,ID,0,PROXY_CONNECT,test,plug_dest@%,0`
* Better MariaDB GTID support for the [mariadb-backup](broken-reference/) [--slave-info](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-5/broken-reference/README.md) option. ([MDEV-19264](https://jira.mariadb.org/browse/MDEV-19264))
* New global [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) variable [innodb\_max\_purge\_lag\_wait](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_max_purge_lag_wait) ([MDEV-16952](https://jira.mariadb.org/browse/MDEV-16952))
* The new parameter --include-unsupported for the script mariadb\_es\_repo\_setup can be used to enable a repository of unsupported packages in the repository configuration. The repository currently includes the CONNECT Storage Engine. The storage engine can be installed by `yum install MariaDB-connect-engine or apt-get install mariadb-plugin-connect-engine` (MENT-1003)
* MariaDB Enterprise Audit did not log proxy users. The new plugin version 2.0.3 introduces an event sub-type PROXY\_CONNECT for event type CONNECT. (MENT-977)
  * On connect, if a proxy user is used, an extra line will be logged: `TIME,HOSTNAME,user,localhost,ID,0,PROXY_CONNECT,test,plug_dest@%,0`
  * The event type can also be used in filters `"connect_event"`: `["CONNECT","DISCONNECT","PROXY_CONNECT"]`
* Performance improvements for comparisons of temporal data types with temporal literals. ([MDEV-23551](https://jira.mariadb.org/browse/MDEV-23551))
* Performance improvements for comparisons of temporal data types. ([MDEV-23537](https://jira.mariadb.org/browse/MDEV-23537))
* For MariaDB Enterprise Server on MS Windows, NTFS file metadata on NTFS is not flushed anymore, reducing the write workload I/O. ([MDEV-24037](https://jira.mariadb.org/browse/MDEV-24037))
* Improved write performance for InnoDB. ([MDEV-23855](https://jira.mariadb.org/browse/MDEV-23855), [MDEV-23399](https://jira.mariadb.org/browse/MDEV-23399))
* The [S3 storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine) now allows you to specify a port ([--s3-port](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine/s3-storage-engine-system-variables#s3_port)) to connect to and to force to use HTTP ([--s3-use-http](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine/s3-storage-engine-system-variables#s3_use_http)). So it is now possible to connect to other solutions which provide the same open API used for Amazon S3. ([MDEV-23662](https://jira.mariadb.org/browse/MDEV-23662))
* Performance improvements for conversions from temporal data types to string. ([MDEV-23568](https://jira.mariadb.org/browse/MDEV-23568))
* Performance improvements for handling numeric data. ([MDEV-23478](https://jira.mariadb.org/browse/MDEV-23478))
* Default changed from `1` to `0` for command line option [--temp-pool](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options). Benchmarking showed that the old default causes a heavy mutex contention. ([MDEV-22278](https://jira.mariadb.org/browse/MDEV-22278))

## Issues Fixed

### Can result in data loss

* Data corruption possible for encrypted [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) tables if the non-default option [innodb\_background\_scrub\_data\_uncompressed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_uncompressed)=ON is used. (MENT-910)
* Temporary tables created by the user or the system can overwrite existing files on creation. ([MDEV-23569](https://jira.mariadb.org/browse/MDEV-23569))
* Table can disappear after [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) command if SET [FOREIGN\_KEY\_CHECKS=0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#foreign_key_checks) is used before altering a child table to remove a primary key. ([MDEV-22934](https://jira.mariadb.org/browse/MDEV-22934))
* Server crashes on an instant `ALTER TABLE .. MODIFY` of a column from `"not null"` to `"null"`. A virtual column must exist in the table. ([MDEV-23672](https://jira.mariadb.org/browse/MDEV-23672))
* One instant [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) including multiple RENAME for indexes can corrupt the index cache. ([MDEV-23356](https://jira.mariadb.org/browse/MDEV-23356))
* `DELETE .. FOR PORTION OF` statement accepts non-constant `FROM .. TO` clause. This contradicts the documentation and is inconsistent with the behavior of the [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) statement. ([MDEV-22596](https://jira.mariadb.org/browse/MDEV-22596))
* Change buffer corruption when reallocating a recently freed page. ([MDEV-23973](https://jira.mariadb.org/browse/MDEV-23973))
* [S3 storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine) delayed replication can drop a table when running a master-replica setup where both master and replica are pointed at the same S3 storage. ([MDEV-23691](https://jira.mariadb.org/browse/MDEV-23691))
* An [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) which is changing multiple rows can result in corrupted data if a `WITHOUT OVERLAPS` key will be modified. ([MDEV-22714](https://jira.mariadb.org/browse/MDEV-22714))
* Memory corruption for tables using a column of type [BIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/bit) in a `WITHOUT OVERLAPS` key. ([MDEV-22608](https://jira.mariadb.org/browse/MDEV-22608))

### Can result in a hang or crash

* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) persistent stats analyze forces full scan which results in a lock crash. (MENT-1024)
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) hang on [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) with error message `Semaphore wait has lasted > 300 seconds`. (MENT-1007)
* Server crash can happen on filesort with a setting for [max\_sort\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#max_sort_length) to a value lower than the default of `64` ([MDEV-24033](https://jira.mariadb.org/browse/MDEV-24033))
* Potential stack overflow in [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) fulltext search with a complex `MATCH .. AGAINST` string. ([MDEV-23999](https://jira.mariadb.org/browse/MDEV-23999))
* [mariadb-backup](broken-reference/) can hang if the server goes idle after a particular kind of redo log write. ([MDEV-23982](https://jira.mariadb.org/browse/MDEV-23982))
* A server crash can occur when encryption is enabled for temporary tables ([encrypt\_tmp\_files=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#encrypt_tmp_files)) and queries use window functions. ([MDEV-23867](https://jira.mariadb.org/browse/MDEV-23867))
* A crash of MariaDB Server is possible when binary logging is activated, caused by improper raising of an error or replication checksum. ([MDEV-23832](https://jira.mariadb.org/browse/MDEV-23832))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) assertion on [TRUNCATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/truncate) after `[ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-table) .. DISCARD TABLESPACE` ([MDEV-23705](https://jira.mariadb.org/browse/MDEV-23705))
* Server crashes after failed attempt to create unique key on virtual column. ([MDEV-23685](https://jira.mariadb.org/browse/MDEV-23685))
* Possible server crash when using an index on a spatial data type with InnoDB. ([MDEV-23600](https://jira.mariadb.org/browse/MDEV-23600))
* Possible server crash when a string function is used for a column of type [DATETIME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/datetime) and the string function is used in a subquery which is returning a row. ([MDEV-23535](https://jira.mariadb.org/browse/MDEV-23535))
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) node can crash on high [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert), [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete), or [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) load from many connections executed on the same table with foreign keys. ([MDEV-23557](https://jira.mariadb.org/browse/MDEV-23557))
* Server crashes if a query is executed on an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table with a foreign key where the foreign key was removed while using [SET FOREIGN\_KEY\_CHECKS=0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#foreign_key_checks). This case should result in an SQL error. ([MDEV-23470](https://jira.mariadb.org/browse/MDEV-23470))
* Recursive procedure call ends with a crash instead of SQL error. ([MDEV-23463](https://jira.mariadb.org/browse/MDEV-23463))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) fails to open the table during removal of `VIRTUAL` column DDL while using [SET FOREIGN\_KEY\_CHECKS=0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#foreign_key_checks), due to lack of referenced index. ([MDEV-23387](https://jira.mariadb.org/browse/MDEV-23387))
* Server crash when altering a table after its tablespace has been discarded already. ([MDEV-22939](https://jira.mariadb.org/browse/MDEV-22939))
* [SHOW BINLOG EVENTS FROM ...](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-events) caused a variety of non-determinism failures if the given position did not exist. ([MDEV-22473](https://jira.mariadb.org/browse/MDEV-22473))
* `SET GLOBAL` replicate\_do\_db `= DEFAULT` causes a crash. ([MDEV-20744](https://jira.mariadb.org/browse/MDEV-20744))
* `JSON_MERGE_PATCH(json_doc, json_doc [, json_doc] ...)` can crash if the first parameter is set to NULL and the second is not valid JSON. ([MDEV-20593](https://jira.mariadb.org/browse/MDEV-20593))
* Server crashes after [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) with `ON DELETE SET NULL` for foreign key and a virtual column in index. ([MDEV-20396](https://jira.mariadb.org/browse/MDEV-20396))
* Server can crash on a prepared [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statement executed via [MariaDB MariaDB Connector/ODBC](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc). ([MDEV-19838](https://jira.mariadb.org/browse/MDEV-19838))
* Crash on SELECT on a table that contains indexed virtual columns. ([MDEV-18366](https://jira.mariadb.org/browse/MDEV-18366))
* Possible server crash for queries using the window function NTH\_VALUE() ([MDEV-15180](https://jira.mariadb.org/browse/MDEV-15180))
* Possible crash when using [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) Tables and partitions. ([MDEV-20100](https://jira.mariadb.org/browse/MDEV-20100))
* MariaDB Enterprise Audit crashes. (MENT-1011)
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) node crash with Galera message `Assertion` server\_state\_.rollback\_mode() == wsrep::server\_state::rm\_async' failed\`. in the error log. (MENT-937)
* [Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) node crashes or hangs during IST if the connection between donor and joiner is unstable or if cluster configuration changes take place at the same time. (MENT-514)
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) crash if bulk updates are executed on Galera. ([MDEV-23872](https://jira.mariadb.org/browse/MDEV-23872))
* Server crash when [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) [WSREP\_LAST\_SEEN\_GTID()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/galera-functions/wsrep_last_seen_gtid) while [Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) replication is not enabled (wsrep-on=OFF). ([MDEV-23466](https://jira.mariadb.org/browse/MDEV-23466))
* Server crash if function [FORMAT(num, decimal\_position\[, locale\])](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/format) is used with a decimal\_position > 30. ([MDEV-23415](https://jira.mariadb.org/browse/MDEV-23415))
* Multiple calls to a Stored Procedure from another Stored Procedure crashes server. ([MDEV-23094](https://jira.mariadb.org/browse/MDEV-23094))
* Server crash when an invalid [wsrep\_provider](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_provider) is set. ([MDEV-23092](https://jira.mariadb.org/browse/MDEV-23092))
* Server hang if `TABLE LOCK` is used after `BACKUP LOCK` was used. ([MDEV-22879](https://jira.mariadb.org/browse/MDEV-22879))
* Server crash on table updates using `FOR PORTION OF` ([MDEV-22805](https://jira.mariadb.org/browse/MDEV-22805))
* Assertion on executing [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) with a prepared statement using [EXECUTE IMMEDIATE](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/EXECUTE/README.md) when [wsrep\_on](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_on) is on and wsrep\_osu\_method is `TOI` ([MDEV-22681](https://jira.mariadb.org/browse/MDEV-22681))
* Server crash if a transaction is started with `SET SESSION wsrep_on=1`, but the global [wsrep\_on](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_on) is `0` ([MDEV-22443](https://jira.mariadb.org/browse/MDEV-22443))
* [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) crash when used with sharding and XA, and [spider\_internal\_xa=OFF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) (default). ([MDEV-19794](https://jira.mariadb.org/browse/MDEV-19794))
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) node can crash with an error message `WSREP: MDL BF-BF conflict` in the error log. The error is related to running [OPTIMIZE](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/OPTIMIZE/README.md) or [REPAIR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/repair-table) on tables with foreign keys. ([MDEV-21577](https://jira.mariadb.org/browse/MDEV-21577))
* If resizing the redo log to be triggered immediately before a server shutdown is initiated, and if innodb\_flush\_sync=0 (non default setting), the shutdown may hang because the page cleaner thread fails to finish its job. (MENT-1031)
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) hangs with [innodb\_flush\_sync=OFF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_flush_sync) (MENT-992)
* Crash recovery fails with Error `InnoDB: Missing FILE_CHECKPOINT at ... between the checkpoint ... and the end ...` after restart, if the redo log size has been changed with `SET GLOBAL` (MENT-795)
* Replica crashes upon rename of a view. ([MDEV-23764](https://jira.mariadb.org/browse/MDEV-23764))
* The server can crash when an [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) is executed on a `HEAP` table using `WITHOUT OVERLAPS`, and the [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) is done for a value of a compound key which is included in the `WITHOUT OVERLAPS` definition. ([MDEV-22677](https://jira.mariadb.org/browse/MDEV-22677))

### Can result in unexpected behavior

* [SHOW RELAYLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-relaylog-events) can return incorrect [BEGIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/begin-end) event information from the binary log, prepended with set [foreign\_key\_checks=1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#foreign_key_checks), [check\_constraint\_checks=1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#check_constraint_checks);
* Defining a view with SQL syntax `ISNULL(ID)=0` incorrectly returns a syntax error. (MENT-1015)
* [MariaDB Enterprise Backup](broken-reference/) reports an error that it cannot find an [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) log file `'./aria_log.00000000'` (MENT-907)
* [MariaDB Enterprise Backup](broken-reference/) failure for incremental backups. ([MDEV-24026](https://jira.mariadb.org/browse/MDEV-24026))
* Aborting a query on an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table with [KILL QUERY](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/KILL-QUERY/README.md) does not show an SQL error message, if the query could not be aborted. ([MDEV-23938](https://jira.mariadb.org/browse/MDEV-23938))
* Optimizer has chosen an inefficient plan, if a multi-component index, a second index, and a `WHERE` or `ON` clause with conditions over these indexes are used. ([MDEV-23811](https://jira.mariadb.org/browse/MDEV-23811))
* Some rounding has been done in an unexpected way for decimal numbers. ([MDEV-23702](https://jira.mariadb.org/browse/MDEV-23702))
* Server crashes after changing [innodb\_buffer\_pool\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_size) at runtime via a [SET](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set) statement. ([MDEV-23693](https://jira.mariadb.org/browse/MDEV-23693))
* Creating a view removes parentheses on expressions from the [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select), which results in wrong results. ([MDEV-23656](https://jira.mariadb.org/browse/MDEV-23656))
* `mysql_tzinfo_to_sql` under InnoDB is slow. ([MDEV-23440](https://jira.mariadb.org/browse/MDEV-23440))
* UDF cannot be uninstalled if the UDF library file doesn't exist. ([MDEV-23327](https://jira.mariadb.org/browse/MDEV-23327))
* [CAST(expr AS type)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/cast) with type `DECIMAL` can return an unexpected result, if the given value for "expr" includes many leading zeros. ([MDEV-23105](https://jira.mariadb.org/browse/MDEV-23105))
* [Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) replication broken if only one timezone is loaded. ([MDEV-22626](https://jira.mariadb.org/browse/MDEV-22626))
* [Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) SST donation fails, `FLUSH TABLES WITH READ LOCK` times out. ([MDEV-22543](https://jira.mariadb.org/browse/MDEV-22543))
* Memory leaks possible after [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) with `FOREIGN KEY` ([MDEV-22277](https://jira.mariadb.org/browse/MDEV-22277))
* [MariaDB Enterprise Backup](broken-reference/) SST fails for [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) if data-directory has `lost+found` directory. ([MDEV-21951](https://jira.mariadb.org/browse/MDEV-21951))
* [SHOW BINLOG EVENTS FROM ...](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-events) caused a variety of non-determinism failures if the given position did not exist. ([MDEV-21839](https://jira.mariadb.org/browse/MDEV-21839))
* Linux AIO returned OS `error 22` if parameters set to [innodb\_flush\_method O\_DIRECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_flush_method) and [innodb\_use\_native\_aio=1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_use_native_aio) (default). ([MDEV-21584](https://jira.mariadb.org/browse/MDEV-21584))
* `CREATE OR REPLACE TRIGGER` in [Galera cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) not replicating, if a trigger with the same name already exists. ([MDEV-21578](https://jira.mariadb.org/browse/MDEV-21578))
* `mysqld_multi` no longer works with different server binaries. ([MDEV-21526](https://jira.mariadb.org/browse/MDEV-21526))
* Possible error for incremental backup [--prepare](broken-reference/) for encrypted tablespaces. ([MDEV-20755](https://jira.mariadb.org/browse/MDEV-20755))
* Possible slow server start and stop if full text indexes are used. ([MDEV-18867](https://jira.mariadb.org/browse/MDEV-18867))
* The parentheses in a `VIEW` can be defined incorrectly for a combination of `= and BETWEEN` ([MDEV-17408](https://jira.mariadb.org/browse/MDEV-17408))
* `ER_BASE64_DECODE_ERROR` upon replaying binary log. ([MDEV-16372](https://jira.mariadb.org/browse/MDEV-16372))
* Several IPv6 issues with [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) powered by Galera. ([MDEV-21770](https://jira.mariadb.org/browse/MDEV-21770), [MDEV-23576](https://jira.mariadb.org/browse/MDEV-23576), [MDEV-23580](https://jira.mariadb.org/browse/MDEV-23580), [MDEV-23581](https://jira.mariadb.org/browse/MDEV-23581), [MDEV-23574](https://jira.mariadb.org/browse/MDEV-23574))
* Subquery on `information_schema` fails with an error message. (MENT-1016)
* `AUTO_INCREMENT` does not increment with compound primary key on partitioned table. (MENT-997)
* `CREATE TEMPORARY TABLE .. LIKE` ([system versioned table](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/system-versioned-table/README.md)) returns error if unique index is defined in the table. ([MDEV-23968](https://jira.mariadb.org/browse/MDEV-23968))
* `CREATE .. SELECT` can result in empty result on join versioned table. ([MDEV-23799](https://jira.mariadb.org/browse/MDEV-23799))
* Error `ERROR 4142 (HY000): SYSTEM_TIME partitions in table` t1 `does not support historical query` upon querying a view, when that view is selecting from the versioned table with partitions. It only happens if the view itself was created using FOR SYSTEM\_TIME ALL ([MDEV-23779](https://jira.mariadb.org/browse/MDEV-23779))
* Disk space not reused for Blob in data file. ([MDEV-23072](https://jira.mariadb.org/browse/MDEV-23072))
* [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) will not dump sequence definition details on `--no-data` dump. ([MDEV-21786](https://jira.mariadb.org/browse/MDEV-21786))
* [CHECK TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/check-table) fails to validate corruption on a table that was corrupted by a bug related to instant `ADD` or `DROP` (fixed in MariaDB Enterprise Server 10.3.17, 10.4.7). ([MDEV-21251](https://jira.mariadb.org/browse/MDEV-21251))
* Subquery execution not terminated after `LIMIT ROWS EXAMINED` is exceeded. ([MDEV-18335](https://jira.mariadb.org/browse/MDEV-18335))
* Deadlock between `BACKUP STAGE BLOCK_COMMIT` and parallel replication. ([MDEV-23586](https://jira.mariadb.org/browse/MDEV-23586))
* Possible memory leak in galera library. ([MDEV-23559](https://jira.mariadb.org/browse/MDEV-23559))
* Wrong result of [MIN(time\_expr)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/aggregate-functions/min) and [MAX(time\_expr)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/aggregate-functions/max) with `GROUP BY` ([MDEV-23525](https://jira.mariadb.org/browse/MDEV-23525))
* Syntax error results in misleading message on [SHOW CREATE PROCEDURE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-procedure) about missing system table `mysql.proc` ([MDEV-23518](https://jira.mariadb.org/browse/MDEV-23518))
* [FORMAT(num, decimal\_position\[, locale\])](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/format) where decimal position is 0 or 38 and num is `DECIMAL(38,38)` returns incorrect results. ([MDEV-23118](https://jira.mariadb.org/browse/MDEV-23118))
* A query result includes a data row twice depending on the WHERE clause used, if partitioning is used. ([MDEV-22246](https://jira.mariadb.org/browse/MDEV-22246))
* Assertion after `ROLLBACK AND CHAIN` ([MDEV-22055](https://jira.mariadb.org/browse/MDEV-22055))
* Replica user can't run [SHOW REPLICA STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status) after upgrade to 10.5. (MENT-995)
* `galera_new_cluster` starts server as standalone instance with no warnings or errors when [wsrep\_on=OFF](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_on), although the expectation is to bootstrap a cluster. (MENT-979)
* Wrong value `#wsrep_provider_options="gcache.size=1024Mb"` in `server.cnf` for wsrep\_provider\_options The server would not start after removing the comment. (MENT-970)
* Wrongly reported `SQL Error (1038): Out of sort memory` for queries, where dependent subqueries use the `ORDER BY` clause. ([MDEV-24015](https://jira.mariadb.org/browse/MDEV-24015))
* An `[ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-table) .. RENAME` to change a column to uppercase doesn't work. ([MDEV-23852](https://jira.mariadb.org/browse/MDEV-23852))
* IN-to-subquery conversion is not visible in optimizer trace. ([MDEV-23767](https://jira.mariadb.org/browse/MDEV-23767))
* [DROP TRIGGER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-trigger) is not replicated in [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) with Galera Replication. ([MDEV-23638](https://jira.mariadb.org/browse/MDEV-23638))

### Related to install and upgrade

* mariadb\_es\_repo\_setup curl failed on Ubuntu Focal if `ca-certificates` is not installed. Now it will prompt an error about missing `ca-certificates` (MENT-971)
* Upgrade wizard not offered during 10.5 MSI installation on Windows. ([MDEV-23462](https://jira.mariadb.org/browse/MDEV-23462))

## Changes in Storage Engines

* This release incorporates MariaDB ColumnStore storage engine version 5.5.1.

## Interface Changes

* [innodb\_lru\_flush\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_lru_flush_size) system variable added
* [innodb\_lru\_scan\_depth](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_lru_scan_depth) system variable default value changed from `1024` to `1536`
* [innodb\_max\_dirty\_pages\_pct](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_max_dirty_pages_pct) system variable default value changed from `75.000000` to `90.000000`
* [innodb\_max\_purge\_lag\_wait](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_max_purge_lag_wait) system variable added
* mariadbd --innodb-lru-flush-size command-line option added
* mariadbd --innodb-max-purge-lag-wait command-line option added
* mariadbd --s3-port command-line option added
* mariadbd --s3-use-http command-line option added
* [performance\_schema\_digests\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-system-variables#performance_schema_digests_size) system variable maximum value changed from `200` to `1048576`
* [REPLICA MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replica-monitor) user privileges added
* [s3\_port](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine/s3-storage-engine-system-variables#s3_port) system variable added
* [s3\_use\_http](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine/s3-storage-engine-system-variables#s3_use_http) system variable added

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.5.8-5 is provided for:

* AlmaLinux 8 (x86\_64, ARM64)
* AlmaLinux 9 (x86\_64, ARM64)
* Debian 11 (x86\_64, ARM64)
* Debian 12 (x86\_64, ARM64)
* Microsoft Windows (x86\_64) (MariaDB Enterprise Cluster excluded)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies)".

## Installation Instructions

* [MariaDB Enterprise Server ](../11-4/whats-new-in-mariadb-enterprise-server-11-4.md)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.5](../11-4/whats-new-in-mariadb-enterprise-server-11-4.md)
* [Enterprise Cluster Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)
* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage) [and MariaDB Enterprise ColumnStore 23.02](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[ and MariaDB Enterprise ColumnStore 23.02](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)
* [HTAP Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)[ and MariaDB Enterprise ColumnStore 23.02](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)
* [Single-Node Enterprise ColumnStore 23.02 with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)[and Object Storage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)
* [Single-Node Enterprise ColumnStore 23.02 with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/sharded-mariadb-enterprise-spider-topology)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-from-to-specific-versions/upgrading-from-mariadb-10-5-to-mariadb-10-6)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-between-major-mariadb-versions)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
