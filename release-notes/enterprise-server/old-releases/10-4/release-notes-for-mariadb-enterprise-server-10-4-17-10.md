# Release Notes for MariaDB Enterprise Server 10.4.17-10

This tenth release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.4 is a maintenance release. This release includes security fixes.

MariaDB Enterprise Server 10.4.17-10 was released on 2020-12-14.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/cve.org) link) | CVSS base score                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [CVE-2020-14765](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14765)                                                                                               | 6.5                                                                             |
| [CVE-2020-14812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14812)                                                                                               | 4.9                                                                             |
| [CVE-2020-14789](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14789)                                                                                               | 4.9                                                                             |
| [CVE-2020-14776](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14776)                                                                                               | 4.9                                                                             |
| [CVE-2020-28912](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-28912)                                                                                               | N/A (Critical)[#1](release-notes-for-mariadb-enterprise-server-10-4-17-10.md#1) |

`#1`:\
MariaDB CVEs are assigned a word rating instead of a CVSS base score. See the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies) for details.

## Notable Changes

* Galera wsrep library updated to 26.4.6 in [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md).
* In alignment with the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies), this release does not include CentOS 6.x and RHEL 6.x packages.
* The audit plugin (not [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin)) did not log proxy users. The new plugin version 2.0.3 introduces an event sub-type `PROXY_CONNECT` for event type CONNECT. ([MDEV-19443](https://jira.mariadb.org/browse/MDEV-19443))
  * On connect, if a proxy user is used, an extra line will be logged: `TIME,HOSTNAME,user,localhost,ID,0,PROXY_CONNECT,test,plug_dest@%,0`
* Better MariaDB GTID support for the [mariadb-backup](../../10-4/broken-reference/) [--slave-info](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) option. ([MDEV-19264](https://jira.mariadb.org/browse/MDEV-19264))
* New global [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) variable [innodb\_max\_purge\_lag\_wait](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_max_purge_lag_wait) ([MDEV-16952](https://jira.mariadb.org/browse/MDEV-16952))
* The new parameter --include-unsupported for the script mariadb\_es\_repo\_setup can be used to enable a repository of unsupported packages in the repository configuration. The repository currently includes the `CONNECT` Storage Engine. The storage engine can be installed by `yum install MariaDB-connect-engine` or `apt-get install mariadb-plugin-connect-engine` (MENT-1003)
* Back port of a MariaDB Server 10.5 feature to not acquire [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) record locks when covering table locks exist. (MENT-403)
* Change [innodb\_log\_optimize\_ddl=OFF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_optimize_ddl) by default. ([MDEV-23720](https://jira.mariadb.org/browse/MDEV-23720))

[MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) did not log proxy users. The new plugin version 2.0.3 introduces an event sub-type `PROXY_CONNECT` for event type [CONNECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables#system-variables). (MENT-977)

* On connect, if a proxy user is used, an extra line will be logged: `TIME,HOSTNAME,user,localhost,ID,0,PROXY_CONNECT,test,plug_dest@%,0`
* The event type can also be used in filters `"connect_event": ["CONNECT","DISCONNECT","PROXY_CONNECT"]`
* Performance improvements for comparisons of temporal data types with temporal literals. ([MDEV-23551](https://jira.mariadb.org/browse/MDEV-23551))
* Performance improvements for comparisons of temporal data types. ([MDEV-23537](https://jira.mariadb.org/browse/MDEV-23537))

## Issues Fixed

### Can result in data loss

* Data corruption possible for encrypted [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) tables if the non-default option [innodb\_background\_scrub\_data\_uncompressed=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_uncompressed) is used. (MENT-910)
* Temporary tables created by the user or the system can overwrite existing files on creation. ([MDEV-23569](https://jira.mariadb.org/browse/MDEV-23569))
* Table can disappear after [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) command if [SET FOREIGN\_KEY\_CHECKS=0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#foreign_key_checks) is used before altering a child table to remove a primary key. ([MDEV-22934](https://jira.mariadb.org/browse/MDEV-22934))
* Server crashes on an instant `ALTER TABLE .. MODIFY` of a column from `"not null" to "null"`. A virtual column must exist in the table. ([MDEV-23672](https://jira.mariadb.org/browse/MDEV-23672))
* One instant [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) including multiple RENAME for indexes can corrupt the index cache. ([MDEV-23356](https://jira.mariadb.org/browse/MDEV-23356))
* A rolling upgrade for [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) from 10.3 to 10.4 can result in data loss. ([MDEV-22723](https://jira.mariadb.org/browse/MDEV-22723))
* `DELETE .. FOR PORTION OF` statement accepts non-constant `FROM .. TO` clause. This contradicts the documentation and is inconsistent with the behavior of the [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) statement. ([MDEV-22596](https://jira.mariadb.org/browse/MDEV-22596))

### Can result in a hang or crash

* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) persistent stats analyze forces full scan which results in a lock crash. (MENT-1024)
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) hang on [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) with error message `Semaphore wait has lasted > 300 seconds`. (MENT-1007)
* Server crash can happen on filesort with a setting for [max\_sort\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_sort_length) to a value lower than the default of `64` ([MDEV-24033](https://jira.mariadb.org/browse/MDEV-24033))
* Potential stack overflow in [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) fulltext search with a complex `MATCH .. AGAINST` string. ([MDEV-23999](https://jira.mariadb.org/browse/MDEV-23999))
* mariadb-backup can hang if the server goes idle after a particular kind of redo log write. ([MDEV-23982](https://jira.mariadb.org/browse/MDEV-23982))
* A server crash can occur when encryption is enabled for temporary tables ([encrypt\_tmp\_files=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#encrypt_tmp_files)) and queries use window functions. ([MDEV-23867](https://jira.mariadb.org/browse/MDEV-23867))
* A crash of MariaDB Server is possible when binary logging is activated, caused by improper raising of an error or replication checksum. ([MDEV-23832](https://jira.mariadb.org/browse/MDEV-23832))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) assertion on [TRUNCATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/truncate) after `ALTER-TABLE|ALTER TABLE .. DISCARD TABLESPACE` ([MDEV-23705](https://jira.mariadb.org/browse/MDEV-23705))
* Server crashes after failed attempt to create unique key on virtual column. ([MDEV-23685](https://jira.mariadb.org/browse/MDEV-23685))
* Possible server crash when using an index on a spatial data type with InnoDB. ([MDEV-23600](https://jira.mariadb.org/browse/MDEV-23600))
* Possible server crash when a string function is used for a column of type [DATETIME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/datetime) and the string function is used in a subquery which is returning a row. ([MDEV-23535](https://jira.mariadb.org/browse/MDEV-23535))
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) node can crash on high [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert), [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete), or [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) load from many connections executed on the same table with foreign keys. ([MDEV-23557](https://jira.mariadb.org/browse/MDEV-23557))
* Server crashes if a query is executed on an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table with a foreign key where the foreign key was removed while using [FOREIGN\_KEY\_CHECKS=0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#foreign_key_checks). This case should result in an SQL error. ([MDEV-23470](https://jira.mariadb.org/browse/MDEV-23470))
* Recursive procedure call ends with a crash instead of SQL error. ([MDEV-23463](https://jira.mariadb.org/browse/MDEV-23463))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) fails to open the table during removal of VIRTUAL column DDL while using [FOREIGN\_KEY\_CHECKS=0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/SET_server-system-variables/README.md#foreign_key_checks), due to lack of referenced index. ([MDEV-23387](https://jira.mariadb.org/browse/MDEV-23387))
* Server crash when altering a table after its tablespace has been discarded already. ([MDEV-22939](https://jira.mariadb.org/browse/MDEV-22939))
* [SHOW BINLOG EVENTS FROM ...](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-events) caused a variety of non-determinism failures if the given position did not exist. ([MDEV-22473](https://jira.mariadb.org/browse/MDEV-22473))
* SET GLOBAL \`\`replicate\_do\_db `= DEFAULT` causes a crash. ([MDEV-20744](https://jira.mariadb.org/browse/MDEV-20744))
* `JSON_MERGE_PATCH(json_doc, json_doc [, json_doc] ...)` can crash if the first parameter is set to NULL and the second is not valid JSON. ([MDEV-20593](https://jira.mariadb.org/browse/MDEV-20593))
* Server crashes after [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) with `ON DELETE SET NULL` for foreign key and a virtual column in index. ([MDEV-20396](https://jira.mariadb.org/browse/MDEV-20396))
* Server can crash on a prepared [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statement executed via [MariaDB MariaDB Connector/ODBC](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc). ([MDEV-19838](https://jira.mariadb.org/browse/MDEV-19838))
* Crash on [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) on a table that contains indexed virtual columns. ([MDEV-18366](https://jira.mariadb.org/browse/MDEV-18366))
* Possible server crash for queries using the window function [NTH\_VALUE()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/nth_value) ([MDEV-15180](https://jira.mariadb.org/browse/MDEV-15180))
* Server crash can occur when [SET GLOBAL replicate\_do\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is used. ([MDEV-23534](https://jira.mariadb.org/browse/MDEV-23534))
* Possible crash when using Spider Tables and partitions. ([MDEV-20100](https://jira.mariadb.org/browse/MDEV-20100))
* [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) crashes. (MENT-1011)
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) node crash with Galera message `Assertion` server\_state\_.rollback\_mode() == wsrep::server\_state::rm\_async' failed\`. in the error log. (MENT-937)
* Galera node crashes or hangs during IST if the connection between donor and joiner is unstable or if cluster configuration changes take place at the same time. (MENT-514)
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) crash if bulk updates are executed on Galera. ([MDEV-23872](https://jira.mariadb.org/browse/MDEV-23872))
* Possible server crash with [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) executed on a system versioned table, if variable system\_versioning\_asof was set to a value of type [DATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/date) instead of [DATETIME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/datetime). ([MDEV-23562](https://jira.mariadb.org/browse/MDEV-23562))
* Server crash when `SELECT WSREP_LAST_SEEN_GTID()` while Galera replication is not enabled (`wsrep-on=OFF`). ([MDEV-23466](https://jira.mariadb.org/browse/MDEV-23466))
* Server crash if function `FORMAT(`num, decimal\_position\[, locale]`) is used with a decimal_position > 30. ([MDEV-23415](https://jira.mariadb.org/browse/MDEV-23415))`
* Multiple calls to a Stored Procedure from another Stored Procedure crashes server. ([MDEV-23094](https://jira.mariadb.org/browse/MDEV-23094))
* Server crash when an invalid [wsrep\_provider](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_provider) is set. ([MDEV-23092](https://jira.mariadb.org/browse/MDEV-23092))
* Server hang if `TABLE LOCK` is used after `BACKUP LOCK` was used. ([MDEV-22879](https://jira.mariadb.org/browse/MDEV-22879))
* Server crash on table updates using `FOR PORTION OF` ([MDEV-22805](https://jira.mariadb.org/browse/MDEV-22805))
* Assertion on executing [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) with a prepared statement using [EXECUTE IMMEDIATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/prepared-statements/execute-immediate) when [wsrep\_on](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_on) is `on` and [wsrep\_osu\_method](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_osu_method) is `TOI` ([MDEV-22681](https://jira.mariadb.org/browse/MDEV-22681))
* Server crash if a transaction is started with `SET SESSION wsrep_on=1`, but the global [wsrep\_on](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_on) is `0` ([MDEV-22443](https://jira.mariadb.org/browse/MDEV-22443))
* [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) crash when used with sharding and XA, and [spider\_internal\_xa=OFF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) (default). ([MDEV-19794](https://jira.mariadb.org/browse/MDEV-19794))
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) node can crash with an error message `WSREP: MDL BF-BF conflict` in the error log. The error is related to tables with foreign keys and running [OPTIMIZE](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/OPTIMIZE/README.md) or [REPAIR](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/REPAIR/README.md) on them. ([MDEV-21577](https://jira.mariadb.org/browse/MDEV-21577))

### Can result in unexpected behavior

* Defining a view with SQL syntax `ISNULL(ID)=0` incorrectly returns a syntax error. (MENT-1015)
* [MariaDB Enterprise Backup](../../10-4/broken-reference/) reports an error that it cannot find an Aria log file `'./aria_log.00000000'` (MENT-907)
* [MariaDB Enterprise Backup](../../10-4/broken-reference/) failure for incremental backups. ([MDEV-24026](https://jira.mariadb.org/browse/MDEV-24026))
* Aborting a query on an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table with [KILL QUERY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/kill) does not show an SQL error message, if the query could not be aborted. ([MDEV-23938](https://jira.mariadb.org/browse/MDEV-23938))
* Optimizer has chosen an inefficient plan, if a multi-component index, a second index, and a WHERE or ON clause with conditions over these indexes are used. ([MDEV-23811](https://jira.mariadb.org/browse/MDEV-23811))
* Some rounding has been done in an unexpected way for decimal numbers. ([MDEV-23702](https://jira.mariadb.org/browse/MDEV-23702))
* Server crashes after changing [innodb\_buffer\_pool\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_size) at runtime via a [SET](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set) statement. ([MDEV-23693](https://jira.mariadb.org/browse/MDEV-23693))
* Creating a view removes parentheses on expressions from the [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select), which results in wrong results. ([MDEV-23656](https://jira.mariadb.org/browse/MDEV-23656))
* `mysql_tzinfo_to_sql` under [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) is slow. ([MDEV-23440](https://jira.mariadb.org/browse/MDEV-23440))
* UDF cannot be uninstalled if the UDF library file doesn't exist. ([MDEV-23327](https://jira.mariadb.org/browse/MDEV-23327))
* [CAST(expr AS type)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/cast) with type [DECIMAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/decimal) can return an unexpected result, if the given value for "expr" includes many leading zeros. ([MDEV-23105](https://jira.mariadb.org/browse/MDEV-23105))
* [Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) replication broken if only one timezone is loaded. ([MDEV-22626](https://jira.mariadb.org/browse/MDEV-22626))
* [Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) SST donation fails, `FLUSH TABLES WITH READ LOCK` times out. ([MDEV-22543](https://jira.mariadb.org/browse/MDEV-22543))
* Memory leaks possible after [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) with `FOREIGN KEY` ([MDEV-22277](https://jira.mariadb.org/browse/MDEV-22277))
* [MariaDB Enterprise Backup](../../10-4/broken-reference/) SST fails for [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) if data-directory has `lost+found` directory. ([MDEV-21951](https://jira.mariadb.org/browse/MDEV-21951))
* [SHOW BINLOG EVENTS FROM ...](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-events) caused a variety of non-determinism failures if the given position did not exist. ([MDEV-21839](https://jira.mariadb.org/browse/MDEV-21839))
* Linux AIO returned OS `error 22` if parameters set to `innodb_flush_method O_DIRECT` and [innodb\_use\_native\_aio=1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_use_native_aio) (default). ([MDEV-21584](https://jira.mariadb.org/browse/MDEV-21584))
* `CREATE OR REPLACE TRIGGER` in [Galera cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) not replicating, if a trigger with the same name already exists. ([MDEV-21578](https://jira.mariadb.org/browse/MDEV-21578))
* `mysqld_multi` no longer works with different server binaries. ([MDEV-21526](https://jira.mariadb.org/browse/MDEV-21526))
* Possible error for incremental backup [--prepare](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) for encrypted tablespaces. ([MDEV-20755](https://jira.mariadb.org/browse/MDEV-20755))
* Possible slow server start and stop if full text indexes are used. ([MDEV-18867](https://jira.mariadb.org/browse/MDEV-18867))
* The parentheses in a `VIEW` can be defined incorrectly for a combination of = and BETWEEN ([MDEV-17408](https://jira.mariadb.org/browse/MDEV-17408))
* `ER_BASE64_DECODE_ERROR` upon replaying binary log. ([MDEV-16372](https://jira.mariadb.org/browse/MDEV-16372))
* Several IPv6 issues with [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) powered by Galera. ([MDEV-21770](https://jira.mariadb.org/browse/MDEV-21770), [MDEV-23576](https://jira.mariadb.org/browse/MDEV-23576), [MDEV-23580](https://jira.mariadb.org/browse/MDEV-23580), [MDEV-23581](https://jira.mariadb.org/browse/MDEV-23581), [MDEV-23574](https://jira.mariadb.org/browse/MDEV-23574))
* Subquery on [information\_schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema) fails with error message. (MENT-1016)
* A `AUTO_INCREMENT` does not increment with compound primary key on partitioned table. (MENT-997)
* `CREATE TEMPORARY TABLE .. LIKE` ([system versioned table|](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/system-versioned-table/README.md)) returns error if unique index is defined in the table. ([MDEV-23968](https://jira.mariadb.org/browse/MDEV-23968))
* `CREATE .. SELECT` can result in empty result on join versioned table. ([MDEV-23799](https://jira.mariadb.org/browse/MDEV-23799))
* Error`ERROR 4142 (HY000): SYSTEM_TIME partitions in table` t1 `does not support historical query` upon querying a view, when that view is selecting from the versioned table with partitions. It only happens if the view itself was created using FOR SYSTEM\_TIME ALL ([MDEV-23779](https://jira.mariadb.org/browse/MDEV-23779))
* Disk space not reused for Blob in data file. ([MDEV-23072](https://jira.mariadb.org/browse/MDEV-23072))
* [mysqldump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump) will not dump sequence definition details on `--no-data` dump. ([MDEV-21786](https://jira.mariadb.org/browse/MDEV-21786))
* [CHECK TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/check-table) fails to validate corruption on a table that was corrupted by a bug related to instant `ADD` or `DROP` (fixed in MariaDB Enterprise Server 10.3.17, 10.4.7). ([MDEV-21251](https://jira.mariadb.org/browse/MDEV-21251))
* Subquery execution not terminated after `LIMIT ROWS EXAMINED` is exceeded. ([MDEV-18335](https://jira.mariadb.org/browse/MDEV-18335))
* Deadlock between `BACKUP STAGE BLOCK_COMMIT` and parallel replication. ([MDEV-23586](https://jira.mariadb.org/browse/MDEV-23586))
* Possible memory leak in galera library. ([MDEV-23559](https://jira.mariadb.org/browse/MDEV-23559))
* Wrong result of `MIN(time_expr)` and `MAX(time_expr)` with `GROUP BY` ([MDEV-23525](https://jira.mariadb.org/browse/MDEV-23525))
* Syntax error results in misleading message on [SHOW CREATE PROCEDURE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-procedure) about missing system table mysql.proc ([MDEV-23518](https://jira.mariadb.org/browse/MDEV-23518))
* `FORMAT(num, decimal_position [, locale])` where decimal position is 0 or 38 and num is DECIMAL(38,38) returns incorrect results. ([MDEV-23118](https://jira.mariadb.org/browse/MDEV-23118))
* A query result includes a data row twice depending on the `WHERE` clause used, if partitioning is used. ([MDEV-22246](https://jira.mariadb.org/browse/MDEV-22246))
* Assertion after `ROLLBACK AND CHAIN` ([MDEV-22055](https://jira.mariadb.org/browse/MDEV-22055))
* `mariadb_es_repo_setup` curl failed on Ubuntu Focal if `ca-certificates` is not installed. Now it will prompt an error about missing `ca-certificates` (MENT-971)

## Interface Changes

* [innodb\_log\_optimize\_ddl](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_optimize_ddl) system variable default value changed from ON to OFF
* [innodb\_max\_purge\_lag\_wait](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_max_purge_lag_wait) system variable added
* [mariadbd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd) [--innodb-max-purge-lag-wait](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_max_purge_lag_wait) command-line option added
* [performance\_schema\_digests\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-system-variables#performance_schema_digests_size) system variable maximum value changed from 200 to 1048576 to 1048576

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.4.17-10 is provided for:

* Red Hat Enterprise Linux 7
* Red Hat Enterprise Linux 8
* CentOS 7
* CentOS 8
* Debian 9
* Debian 10
* SUSE Linux Enterprise Server 12
* SUSE Linux Enterprise Server 15
* Ubuntu 16.04
* Ubuntu 18.04
* Ubuntu 20.04
* Microsoft Windows

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see [MariaDB Corporation Engineering Policies".](https://mariadb.com/engineering-policies)

#### Note

In alignment with the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies), this release does not include CentOS 6.x and RHEL 6.x packages.

## Installation Instructions

* [MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server)
* [Enterprise Cluster Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/sharded-mariadb-enterprise-spider-topology)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-4-to-mariadb-10-5)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-between-major-mariadb-versions)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
