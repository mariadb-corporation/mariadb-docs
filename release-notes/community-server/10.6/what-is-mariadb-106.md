# MariaDB 10.6 Changes & Improvements

{% include "../../.gitbook/includes/latest-10-6.md" %}

[MariaDB 10.6](what-is-mariadb-106.md) is a long-term maintenance stable version. The first stable release was in July 2021, and it will be [maintained until](https://mariadb.org/about/#maintenance-policy) July 2026.

## Upgrading

* See [Upgrading Between Major MariaDB Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions) and [Upgrading from MariaDB 10.5 to MariaDB 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-from-mariadb-10-5-to-mariadb-10-6).

## New Features & Improvements

See the [Differences in MariaDB Enterprise Server 10.6](../../enterprise-server/mariadb-enterprise-server-differences/differences-in-mariadb-enterprise-server-10-6.md) page for items that are different between MariaDB Community Server 10.6 and MariaDB Enterprise Server 10.6.

### Atomic DDL

* [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table), [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table), [RENAME TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/rename-table), [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table), [DROP DATABASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-database) and related DDL statements [are now atomic](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/atomic-ddl). Either the statement is fully completed, or everything is reverted to it's original state. Note that when deleting multiple tables with DROP TABLE, only each individual drop is atomic, not the full list of tables). ([MDEV-23842](https://jira.mariadb.org/browse/MDEV-23842)).

### SQL Syntax

* Implement SQL-standard [SELECT ... OFFSET ... FETCH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select-offset-fetch) ([MDEV-23908](https://jira.mariadb.org/browse/MDEV-23908))
* Add [SELECT ... SKIP LOCKED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select#skip-locked) syntax (InnoDB only) ([MDEV-13115](https://jira.mariadb.org/browse/MDEV-13115))
* [Indexes can be ignored](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes/ignored-indexes) ([MDEV-7317](https://jira.mariadb.org/browse/MDEV-7317), [MDEV-25075](https://jira.mariadb.org/browse/MDEV-25075))
* [JSON\_TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_table), used to extract JSON data based on a JSON path expression and to return it as a relational table ([MDEV-17399](https://jira.mariadb.org/browse/MDEV-17399))

#### Oracle Compatibility

* Anonymous [subqueries in a FROM clause](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/subqueries/subqueries-in-a-from-clause-derived-tables) (no AS clause) are permitted in [ORACLE mode](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/mariadb-10-6-series/broken-reference/README.md) ([MDEV-19162](https://jira.mariadb.org/browse/MDEV-19162))
* [ADD\_MONTHS()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/add_months) added ([MDEV-20025](https://jira.mariadb.org/browse/MDEV-20025))
* [TO\_CHAR()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/to_char) added ([MDEV-20017](https://jira.mariadb.org/browse/MDEV-20017))
* [SYS\_GUID()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/sys_guid) added ([MDEV-24285](https://jira.mariadb.org/browse/MDEV-24285))
* MINUS is mapped to [EXCEPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/except) in UNION ([MDEV-20021](https://jira.mariadb.org/browse/MDEV-20021))
* [ROWNUM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/rownum) function returns the current number of accepted rows in the current context ([MDEV-24089](https://jira.mariadb.org/browse/MDEV-24089))

### InnoDB

* Optimization to speed up inserts into an empty table ([MDEV-515](https://jira.mariadb.org/browse/MDEV-515))
* We intended to deprecate and eventually remove the [InnoDB's COMPRESSED row format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-row-formats/innodb-compressed-row-format). The first step was to make the tables [read-only by default](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-row-formats/innodb-compressed-row-format#read-only), but this plan was abandoned from [MariaDB 10.6.6](10.6.6.md) ([MDEV-23497](https://jira.mariadb.org/browse/MDEV-23497)) ([MDEV-27736](https://jira.mariadb.org/browse/MDEV-27736))
* [Information Schema SYS\_TABLESPACES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tablespaces-table) now directly reflects the filesystem, and [SYS\_DATAFILES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_datafiles-table) has been removed ([MDEV-22343](https://jira.mariadb.org/browse/MDEV-22343))
* Defer writes to the InnoDB temporary tablespace ([MDEV-12227](https://jira.mariadb.org/browse/MDEV-12227))
* The old [MariaDB 5.5](../old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)-compatible `innodb` checksum is no longer supported, only `crc32`. Removed the `*innodb` and `*none` options from [innodb\_checksum\_algorithm](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_checksum_algorithm), and the `--strict-check`/`-C` and `--write`/`-w` options from [innochecksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/innochecksum) ([MDEV-25105](https://jira.mariadb.org/browse/MDEV-25105))

### Replication, Galera and Binlog

* Increase [master\_host](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to#master_host) limit to 255, user to 128 ([MDEV-24312](https://jira.mariadb.org/browse/MDEV-24312))
* The [wsrep\_mode](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_mode) system variable, for turning on WSREP features which are not part of default behavior (including the experimental Aria replication) ([MDEV-20008](https://jira.mariadb.org/browse/MDEV-20008), [MDEV-20715](https://jira.mariadb.org/browse/MDEV-20715), [MDEV-24946](https://jira.mariadb.org/browse/MDEV-24946))
* The delay between binary log purges can now be specified with much greater precision. The system variable [binlog\_expire\_logs\_seconds](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_expire_logs_seconds) is introduced as a form of alias for [expire\_logs\_days](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#expire_logs_days), which now accepts a precision of 1/1000000 days ([MDEV-19371](https://jira.mariadb.org/browse/MDEV-19371))
* Allow transition from unencrypted to TLS [Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) cluster communication without cluster downtime ([MDEV-22131](https://jira.mariadb.org/browse/MDEV-22131))

### Sys Schema

* Bundle [sys-schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/sys-schema), a collection of views, functions and procedures to help administrators get insight into database usage. ([MDEV-9077](https://jira.mariadb.org/browse/MDEV-9077))

### Performance Schema

* Merged replication instrumentation and tables ([MDEV-16437](https://jira.mariadb.org/browse/MDEV-16437), [MDEV-20220](https://jira.mariadb.org/browse/MDEV-20220))

### Information Schema

* The views [INFORMATION\_SCHEMA.KEYWORDS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-keywords-table) and [INFORMATION\_SCHEMA.SQL\_FUNCTIONS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-sql_functions-table) have been added to the information schema ([MDEV-25129](https://jira.mariadb.org/browse/MDEV-25129))

### Storage Engines

* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) has been removed ([MDEV-19780](https://jira.mariadb.org/browse/MDEV-19780))
* [CassandraSE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/cassandra) has been removed ([MDEV-23024](https://jira.mariadb.org/browse/MDEV-23024))

### Character Sets

* The `utf8` [character set](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets) (and related collations) is now by default an alias for `utf8mb3` rather than the other way around. It can be set to imply `utf8mb4` by changing the value of the [old\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#old_mode) system variable ([MDEV-8334](https://jira.mariadb.org/browse/MDEV-8334))

### General

* Bundle sys schema ([MDEV-9077](https://jira.mariadb.org/browse/MDEV-9077))
* Do not resend unchanged resultset metadata for prepared statements ([MDEV-19237](https://jira.mariadb.org/browse/MDEV-19237))
* [--bind-address=hostname](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#bind_address) now listens on both IPv6 and IPv4 addresses ([MDEV-6536](https://jira.mariadb.org/browse/MDEV-6536))
* Support systemd socket activation ([MDEV-5536](https://jira.mariadb.org/browse/MDEV-5536))
* For the [GSSAPI plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi), support AD or local group name, and SIDs on Windows ([MDEV-23959](https://jira.mariadb.org/browse/MDEV-23959))
* Check for $MARIADB\_HOME/my.cnf ([MDEV-21365](https://jira.mariadb.org/browse/MDEV-21365))

### Variables

* For a list of all new variables, see [System Variables Added in MariaDB 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-variables-added-in-mariadb-10-6) and [Status Variables Added in MariaDB 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/status-variables-added-in-mariadb-106).
* [max\_recursive\_iterations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_recursive_iterations) has been reduced to 1000 ([MDEV-17239](https://jira.mariadb.org/browse/MDEV-17239))

#### InnoDB Variables

The following deprecated variables have been removed ([MDEV-23397](https://jira.mariadb.org/browse/MDEV-23397)):

* [innodb\_adaptive\_max\_sleep\_delay](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_adaptive_max_sleep_delay)
* [innodb\_background\_scrub\_data\_check\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_check_interval)
* [innodb\_background\_scrub\_data\_compressed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_compressed)
* [innodb\_background\_scrub\_data\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_interval)
* [innodb\_background\_scrub\_data\_uncompressed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_background_scrub_data_uncompressed)
* [innodb\_buffer\_pool\_instances](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_instances)
* [innodb\_commit\_concurrency](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_commit_concurrency)
* [innodb\_concurrency\_tickets](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_concurrency_tickets)
* [innodb\_file\_format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_file_format)
* [innodb\_large\_prefix](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_large_prefix)
* [innodb\_lock\_schedule\_algorithm](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_lock_schedule_algorithm)
* [innodb\_log\_checksums](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_checksums)
* [innodb\_log\_compressed\_pages](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_compressed_pages)
* [innodb\_log\_files\_in\_group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_files_in_group)
* [innodb\_log\_optimize\_ddl](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_optimize_ddl)
* [innodb\_page\_cleaners](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_page_cleaners)
* [innodb\_replication\_delay](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_replication_delay)
* [innodb\_scrub\_log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_scrub_log)
* [innodb\_scrub\_log\_speed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_scrub_log_speed)
* [innodb\_sync\_array\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_sync_array_size)
* [innodb\_thread\_concurrency](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_thread_concurrency)
* [innodb\_thread\_sleep\_delay](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_thread_sleep_delay)
* [innodb\_undo\_logs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_undo_logs)

## Security Vulnerabilities Fixed in [MariaDB 10.6](what-is-mariadb-106.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security)\
page.

* [CVE-2025-21490](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21490): [MariaDB 10.6.21](10.6.21.md)
* [CVE-2024-21096](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21096): [MariaDB 10.6.18](10.6.18.md)
* [CVE-2023-5157](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5157): [MariaDB 10.6.9](10.6.9.md)
* [CVE-2023-22084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22084): [MariaDB 10.6.16](10.6.16.md)
* [CVE-2022-47015](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47015): [MariaDB 10.6.13](10.6.13.md)
* [CVE-2022-38791](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-38791): [MariaDB 10.6.9](10.6.9.md)
* [CVE-2022-32091](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32091): [MariaDB 10.6.9](10.6.9.md)
* [CVE-2022-32089](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32089): [MariaDB 10.6.9](10.6.9.md)
* [CVE-2022-32088](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32088): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-32087](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32087): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-32086](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32086): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-32085](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32085): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-32084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32084): [MariaDB 10.6.9](10.6.9.md)
* [CVE-2022-32083](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32083): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-32082](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32082): [MariaDB 10.6.9](10.6.9.md)
* [CVE-2022-32081](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32081): [MariaDB 10.6.9](10.6.9.md)
* [CVE-2022-31624](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31624): [MariaDB 10.6.5](10.6.5.md)
* [CVE-2022-27458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27458): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27457](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27457): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27456): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27455](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27455): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27452](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27452): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27451](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27451): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27449](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27449): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27448](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27448): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27447](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27447): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27446](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27446): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27445](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27445): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27444](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27444): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27387): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27386): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27385): [MariaDB 10.6.5](10.6.5.md)
* [CVE-2022-27384](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27384): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27383](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27383): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27382](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27382): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27381](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27381): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27380](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27380): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27379](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27379): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27378](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27378): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27377](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27377): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-27376](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27376): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2022-24052](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24052): [MariaDB 10.6.6](10.6.6.md)
* [CVE-2022-24051](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24051): [MariaDB 10.6.6](10.6.6.md)
* [CVE-2022-24050](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24050): [MariaDB 10.6.6](10.6.6.md)
* [CVE-2022-24048](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24048): [MariaDB 10.6.6](10.6.6.md)
* [CVE-2022-21595](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21595): [MariaDB 10.6.6](10.6.6.md)
* [CVE-2022-0778](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0778): [MariaDB 10.6.6](10.6.6.md)
* [CVE-2021-46669](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46669): [MariaDB 10.6.8](10.6.8.md)
* [CVE-2021-46668](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46668): [MariaDB 10.6.7](10.6.7.md)
* [CVE-2021-46667](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46667): [MariaDB 10.6.5](10.6.5.md)
* [CVE-2021-46665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46665): [MariaDB 10.6.7](10.6.7.md)
* [CVE-2021-46664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46664): [MariaDB 10.6.7](10.6.7.md)
* [CVE-2021-46663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46663): [MariaDB 10.6.7](10.6.7.md)
* [CVE-2021-46662](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46662): [MariaDB 10.6.5](10.6.5.md)
* [CVE-2021-46661](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46661): [MariaDB 10.6.7](10.6.7.md)
* [CVE-2021-46659](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46659): [MariaDB 10.6.6](10.6.6.md)
* [CVE-2021-46658](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46658): [MariaDB 10.6.3](10.6.3.md)
* [CVE-2021-35604](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-35604): [MariaDB 10.6.3](10.6.3.md)
* [CVE-2021-2389](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2389): [MariaDB 10.6.4](10.6.4.md) \[[2](10.6.4.md)]
* [CVE-2021-2372](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2372): [MariaDB 10.6.4](10.6.4.md) \[[2](10.6.4.md)]
* [CVE-2018-25032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-25032): [MariaDB 10.6.9](10.6.9.md)

## List of All [MariaDB 10.6](what-is-mariadb-106.md) Releases

| Date        | Release         | Status      | Release Notes               | Changelog                                  |
| ----------- | --------------- | ----------- | --------------------------- | ------------------------------------------ |
| 6 Nov 2025  | MariaDB 10.6.24 | Stable (GA) | [Release Notes](10.6.24.md) | [Changelog](../changelogs/10.6/10.6.24.md) |
| 6 Aug 2025  | MariaDB 10.6.23 | Stable (GA) | [Release Notes](10.6.23.md) | [Changelog](../changelogs/10.6/10.6.23.md) |
| 8 May 2025  | MariaDB 10.6.22 | Stable (GA) | [Release Notes](10.6.22.md) | [Changelog](../changelogs/10.6/10.6.22.md) |
| 4 Feb 2025  | MariaDB 10.6.21 | Stable (GA) | [Release Notes](10.6.21.md) | [Changelog](../changelogs/10.6/10.6.21.md) |
| 1 Nov 2024  | MariaDB 10.6.20 | Stable (GA) | [Release Notes](10.6.20.md) | [Changelog](../changelogs/10.6/10.6.20.md) |
| 8 Aug 2024  | MariaDB 10.6.19 | Stable (GA) | [Release Notes](10.6.19.md) | [Changelog](../changelogs/10.6/10.6.19.md) |
| 16 May 2024 | MariaDB 10.6.18 | Stable (GA) | [Release Notes](10.6.18.md) | [Changelog](../changelogs/10.6/10.6.18.md) |
| 7 Feb 2024  | MariaDB 10.6.17 | Stable (GA) | [Release Notes](10.6.17.md) | [Changelog](../changelogs/10.6/10.6.17.md) |
| 13 Nov 2023 | MariaDB 10.6.16 | Stable (GA) | [Release Notes](10.6.16.md) | [Changelog](../changelogs/10.6/10.6.16.md) |
| 14 Aug 2023 | MariaDB 10.6.15 | Stable (GA) | [Release Notes](10.6.15.md) | [Changelog](../changelogs/10.6/10.6.15.md) |
| 7 Jun 2023  | MariaDB 10.6.14 | Stable (GA) | [Release Notes](10.6.14.md) | [Changelog](../changelogs/10.6/10.6.14.md) |
| 10 May 2023 | MariaDB 10.6.13 | Stable (GA) | [Release Notes](10.6.13.md) | [Changelog](../changelogs/10.6/10.6.13.md) |
| 6 Feb 2023  | MariaDB 10.6.12 | Stable (GA) | [Release Notes](10.6.12.md) | [Changelog](../changelogs/10.6/10.6.12.md) |
| 7 Nov 2022  | MariaDB 10.6.11 | Stable (GA) | [Release Notes](10.6.11.md) | [Changelog](../changelogs/10.6/10.6.11.md) |
| 19 Sep 2022 | MariaDB 10.6.10 | Stable (GA) | [Release Notes](10.6.10.md) | [Changelog](../changelogs/10.6/10.6.10.md) |
| 15 Aug 2022 | MariaDB 10.6.9  | Stable (GA) | [Release Notes](10.6.9.md)  | [Changelog](../changelogs/10.6/10.6.9.md)  |
| 20 May 2022 | MariaDB 10.6.8  | Stable (GA) | [Release Notes](10.6.8.md)  | [Changelog](../changelogs/10.6/10.6.8.md)  |
| 12 Feb 2022 | MariaDB 10.6.7  | Stable (GA) | [Release Notes](10.6.7.md)  | [Changelog](../changelogs/10.6/10.6.7.md)  |
| 9 Feb 2022  | MariaDB 10.6.6  | Stable (GA) | [Release Notes](10.6.6.md)  | [Changelog](../changelogs/10.6/10.6.6.md)  |
| 8 Nov 2021  | MariaDB 10.6.5  | Stable (GA) | [Release Notes](10.6.5.md)  | [Changelog](../changelogs/10.6/10.6.5.md)  |
| 6 Aug 2021  | MariaDB 10.6.4  | Stable (GA) | [Release Notes](10.6.4.md)  | [Changelog](../changelogs/10.6/10.6.4.md)  |
| 6 Jul 2021  | MariaDB 10.6.3  | Stable (GA) | [Release Notes](10.6.3.md)  | [Changelog](../changelogs/10.6/10.6.3.md)  |
| 18 Jun 2021 | MariaDB 10.6.2  | RC          | [Release Notes](10.6.2.md)  | [Changelog](../changelogs/10.6/10.6.2.md)  |
| 21 May 2021 | MariaDB 10.6.1  | Beta        | [Release Notes](10.6.1.md)  | [Changelog](../changelogs/10.6/10.6.1.md)  |
| 26 Apr 2021 | MariaDB 10.6.0  | Alpha       | [Release Notes](10.6.0.md)  | [Changelog](../changelogs/10.6/10.6.0.md)  |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
