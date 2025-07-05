# Release Notes for MariaDB Enterprise Server 10.3.27-10

This tenth release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.3 is a maintenance release. This release includes security fixes.

MariaDB Enterprise Server 10.3.27-10 was released on 2020-12-14.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-3/cve.org) link) | CVSS base score                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-3/cve.org) link) | CVSS base score                                                                 |
| [CVE-2020-14765](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14765)                                                                                               | 6.5                                                                             |
| [CVE-2020-14812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14812)                                                                                               | 4.9                                                                             |
| [CVE-2020-14789](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14789)                                                                                               | 4.9                                                                             |
| [CVE-2020-14776](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14776)                                                                                               | 4.9                                                                             |
| [CVE-2020-28912](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28912)                                                                                               | N/A (Critical)[#1](release-notes-for-mariadb-enterprise-server-10-3-27-10.md#1) |

`#1`:\
MariaDB CVEs are assigned a word rating instead of a CVSS base score. See the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies/) for details.

## Notable Changes

* Galera wsrep library updated to 25.3.31 in [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md).
* In alignment with the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies), this release does not include CentOS 6.x and RHEL 6.x packages.
* The audit plugin (not MariaDB Enterprise Audit) did not log proxy users. The new plugin version 2.0.3 introduces an event sub-type PROXY\_CONNECT for event type CONNECT ([MDEV-19443](https://jira.mariadb.org/browse/MDEV-19443))
  * On connect, if a proxy user is used, an extra line will be logged:
    1. TIME,HOSTNAME,user,localhost,ID,0,PROXY\_CONNECT,test,plug\_dest@%,0\`\`
* Better MariaDB GTID support for the [mariadb-backup](broken-reference) [--slave-info](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md) option. ([MDEV-19264](https://jira.mariadb.org/browse/MDEV-19264))
* New global [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) variable [innodb\_max\_purge\_lag\_wait](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_max_purge_lag_wait) ([MDEV-16952](https://jira.mariadb.org/browse/MDEV-16952))
* The new parameter [--include-unsupported](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage) for the script [mariadb\_es\_repo\_setup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage) can be used to enable a repository of unsupported packages in the repository configuration. The repository currently includes the CONNECT Storage Engine. The storage engine can be installed by `yum install MariaDB-connect-engine` or `apt-get install mariadb-plugin-connect-engine` (MENT-1003)
* Back port of a MariaDB Server 10.5 feature to not acquire [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) record locks when covering table locks exist. (MENT-403)
* Change [innodb\_log\_optimize\_ddl=OFF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_optimize_ddl) by default. ([MDEV-23720](https://jira.mariadb.org/browse/MDEV-23720))

## Issues Fixed

### Can result in data loss

* Data corruption possible for encrypted [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) tables if the non-default option [innodb\_background\_scrub\_data\_uncompressed=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_uncompressed) is used. (MENT-910)
* Temporary tables created by the user or the system can overwrite existing files on creation. ([MDEV-23569](https://jira.mariadb.org/browse/MDEV-23569))
* Table can disappear after ALTER TABLE command if \[\[[server-system-variables/#foreign\_key\_checks|SET FOREIGN\_KEY\_CHECKS=0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#foreign_key_checks)]] is used before altering a child table to remove a primary key. ([MDEV-22934](https://jira.mariadb.org/browse/MDEV-22934))

### Can result in a hang or crash

* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) persistent stats analyze forces full scan which results in a lock crash. (MENT-1024)
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) hang on [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) with error message `Semaphore wait has lasted > 300 seconds`. (MENT-1007)
* Server crash can happen on filesort with a setting for [max\_sort\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#max_sort_length) to a value lower than the default of 64 ([MDEV-24033](https://jira.mariadb.org/browse/MDEV-24033))
* Potential stack overflow in [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) fulltext search with a complex `MATCH .. AGAINST` string. ([MDEV-23999](https://jira.mariadb.org/browse/MDEV-23999))
* mariadb-backup can hang if the server goes idle after a particular kind of redo log write. ([MDEV-23982](https://jira.mariadb.org/browse/MDEV-23982))
* A server crash can occur when encryption is enabled for temporary tables (`encrypt-tmp-files`=ON) and queries use window functions. ([MDEV-23867](https://jira.mariadb.org/browse/MDEV-23867))
* A crash of MariaDB Server is possible when binary logging is activated, caused by improper raising of an error or replication checksum. ([MDEV-23832](https://jira.mariadb.org/browse/MDEV-23832))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) assertion on [TRUNCATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/truncate) after `ALTER TABLE .. DISCARD TABLESPACE` ([MDEV-23705](https://jira.mariadb.org/browse/MDEV-23705))
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
* [JSON\_MERGE\_PATCH(json\_doc, json\_doc\[, json\_doc\] ...)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_merge_patch) can crash if the first parameter is set to NULL and the second is not valid JSON. ([MDEV-20593](https://jira.mariadb.org/browse/MDEV-20593))
* Server crashes after [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) with ON `DELETE SET NULL` for foreign key and a virtual column in index. ([MDEV-20396](https://jira.mariadb.org/browse/MDEV-20396))
* Server can crash on a prepared [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statement executed via MariaDB Connector/ODBC. ([MDEV-19838](https://jira.mariadb.org/browse/MDEV-19838))
* Crash on [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) on a table that contains indexed virtual columns. ([MDEV-18366](https://jira.mariadb.org/browse/MDEV-18366))
* Possible server crash for queries using the window function [NTH\_VALUE()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/nth_value) ([MDEV-15180](https://jira.mariadb.org/browse/MDEV-15180))
* [Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) got stuck after [FLUSH TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) ([MDEV-22707](https://jira.mariadb.org/browse/MDEV-22707))
* Server crash can occur when `SET GLOBAL` [replicate\_do\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is used. ([MDEV-23534](https://jira.mariadb.org/browse/MDEV-23534))
* Possible crash when using [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) Tables and partitions. ([MDEV-20100](https://jira.mariadb.org/browse/MDEV-20100))

### Can result in unexpected behavior

* Defining a view with SQL syntax [ISNULL(ID)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/operators/comparison-operators/isnull) =0 incorrectly returns a syntax error. (MENT-1015)
* [MariaDB Enterprise Backup](broken-reference) reports an error that it cannot find an [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) log file './aria\_log.00000000' (MENT-907)
* [MariaDB Enterprise Backup](broken-reference) failure for incremental backups. ([MDEV-24026](https://jira.mariadb.org/browse/MDEV-24026))
* Aborting a query on an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table with [KILL QUERY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/kill) does not show an SQL error message, if the query could not be aborted. ([MDEV-23938](https://jira.mariadb.org/browse/MDEV-23938))
* Optimizer has chosen an inefficient plan, if a multi-component index, a second index, and a `WHERE` or `ON` clause with conditions over these indexes are used. ([MDEV-23811](https://jira.mariadb.org/browse/MDEV-23811))
* Some rounding has been done in an unexpected way for decimal numbers. ([MDEV-23702](https://jira.mariadb.org/browse/MDEV-23702))
* Server crashes after changing [innodb\_buffer\_pool\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_size) at runtime via a [SET](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set) statement. ([MDEV-23693](https://jira.mariadb.org/browse/MDEV-23693))
* Creating a view removes parentheses on expressions from the [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) , which results in wrong results. ([MDEV-23656](https://jira.mariadb.org/browse/MDEV-23656))
* `mysql_tzinfo_to_sql` under [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) is slow. ([MDEV-23440](https://jira.mariadb.org/browse/MDEV-23440))
* UDF cannot be uninstalled if the UDF library file doesn't exist. ([MDEV-23327](https://jira.mariadb.org/browse/MDEV-23327))
* [CAST(expr AS type)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/cast) with type [DECIMAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/decimal) can return an unexpected result, if the given value for "expr" includes many leading zeros. ([MDEV-23105](https://jira.mariadb.org/browse/MDEV-23105))
* [Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) replication broken if only one timezone is loaded. ([MDEV-22626](https://jira.mariadb.org/browse/MDEV-22626))
* [Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) SST donation fails, `FLUSH TABLES WITH READ LOCK` times out. ([MDEV-22543](https://jira.mariadb.org/browse/MDEV-22543))
* Memory leaks possible after [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) with FOREIGN KEY ([MDEV-22277](https://jira.mariadb.org/browse/MDEV-22277))
* [MariaDB Enterprise Backup](broken-reference) SST fails for [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) if data-directory has `lost+found` directory. ([MDEV-21951](https://jira.mariadb.org/browse/MDEV-21951))
* [SHOW BINLOG EVENTS FROM ...](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-events) caused a variety of non-determinism failures if the given position did not exist. ([MDEV-21839](https://jira.mariadb.org/browse/MDEV-21839))
* Linux AIO returned `OS error 22` if parameters set to [innodb\_flush\_method](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_flush_method) O\_DIRECT and `innodb_use_native_aio=1` (default). ([MDEV-21584](https://jira.mariadb.org/browse/MDEV-21584))
* `CREATE OR REPLACE TRIGGER` in [Galera cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) not replicating, if a trigger with the same name already exists. ([MDEV-21578](https://jira.mariadb.org/browse/MDEV-21578))
* `mysqld_multi` no longer works with different server binaries. ([MDEV-21526](https://jira.mariadb.org/browse/MDEV-21526))
* Possible error for incremental backup [--prepare](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md) for encrypted tablespaces. ([MDEV-20755](https://jira.mariadb.org/browse/MDEV-20755))
* Possible slow server start and stop if full text indexes are used. ([MDEV-18867](https://jira.mariadb.org/browse/MDEV-18867))
* The parentheses in a `VIEW` can be defined incorrectly for a combination of = and BETWEEN ([MDEV-17408](https://jira.mariadb.org/browse/MDEV-17408))
* [ER\_BASE64\_DECODE\_ERROR](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md) upon replaying binary log. ([MDEV-16372](https://jira.mariadb.org/browse/MDEV-16372))
* Several IPv6 issues with [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) powered by Galera. ([MDEV-21770](https://jira.mariadb.org/browse/MDEV-21770), [MDEV-23576](https://jira.mariadb.org/browse/MDEV-23576), [MDEV-23580](https://jira.mariadb.org/browse/MDEV-23580), [MDEV-23581](https://jira.mariadb.org/browse/MDEV-23581), [MDEV-23574](https://jira.mariadb.org/browse/MDEV-23574))
* Subquery on `information_schema` fails with error message. (MENT-1016)
* `AUTO_INCREMENT` does not increment with compound primary key on partitioned table. (MENT-997)
* `CREATE TEMPORARY TABLE .. LIKE` ([system versioned table](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-3/system-versioned-table/README.md)) returns error if unique index is defined in the table. ([MDEV-23968](https://jira.mariadb.org/browse/MDEV-23968))
* `CREATE .. SELECT` can result in empty result on join versioned table. ([MDEV-23799](https://jira.mariadb.org/browse/MDEV-23799))
* Error `ERROR 4142 (HY000): SYSTEM_TIME partitions in table` t1 `does not support historical query` upon querying a view, when that view is selecting from the versioned table with partitions. It only happens if the view itself was created using FOR `SYSTEM_TIME ALL` ([MDEV-23779](https://jira.mariadb.org/browse/MDEV-23779))
* Disk Space not reused for Blob in data file. ([MDEV-23072](https://jira.mariadb.org/browse/MDEV-23072))
* [mysqldump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump) will not dump sequence definition details on `--no-data` dump. ([MDEV-21786](https://jira.mariadb.org/browse/MDEV-21786))
* [CHECK TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/check-table) fails to validate corruption on a table that was corrupted by a bug related to instant `ADD` or `DROP` (fixed in MariaDB Enterprise Server 10.3.17, 10.4.7). ([MDEV-21251](https://jira.mariadb.org/browse/MDEV-21251))
* Subquery execution not terminated after `LIMIT ROWS EXAMINED` is exceeded. ([MDEV-18335](https://jira.mariadb.org/browse/MDEV-18335))

### Related to install and upgrade

* `mariadb_es_repo_setup` curl failed on Ubuntu Focal if `ca-certificates` is not installed. Now it will prompt an error about missing `ca-certificates` (MENT-971)

## Interface Changes

* [innodb-system-variables/#innodb\_log\_optimize\_ddlinnodb\_log\_optimize\_ddl](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_optimize_ddlinnodb_log_optimize_ddl) system variable default value changed from ON to OFF
* [innodb\_max\_purge\_lag\_wait](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_max_purge_lag_wait) system variable added
* [mysqld](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) [--innodb-max-purge-lag-wait](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_max_purge_lag_wait) command-line option added
* [performance\_schema\_digests\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-system-variables#performance_schema_digests_size)

## Platforms

In alignment to the [enterprise lifecycle](../enterprise-server-lifecycle.md), MariaDB Enterprise Server 10.3.27-10 is provided for:

* Red Hat Enterprise Linux 7
* Red Hat Enterprise Linux 8
* CentOS 7
* CentOS 8
* Ubuntu 16.04
* Ubuntu 18.04
* Ubuntu 20.04
* Debian 9
* Debian 10
* SUSE Linux Enterprise Server 12
* SUSE Linux Enterprise Server 15
* Microsoft Windows

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies/)".

#### Note

In alignment with the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies/), this release does not include CentOS 6.x and RHEL 6.x packages.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
