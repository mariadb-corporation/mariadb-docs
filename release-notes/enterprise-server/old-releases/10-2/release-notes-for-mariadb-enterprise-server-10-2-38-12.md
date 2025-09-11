# Release Notes for MariaDB Enterprise Server 10.2.38-12

This twelfth release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.2 is a maintenance release. This release includes a variety of fixes.

MariaDB Enterprise Server 10.2.38-12 was released on 2021-06-14.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-2/cve.org) link) | CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [CVE-2021-2166](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2166)                                                                                                 | 4.9             |
| [CVE-2021-2154](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-2154)                                                                                                 | 4.9             |

## Notable Changes

* New function [ST\_DISTANCE\_SPHERE()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-relations/st_distance_sphere) calculates the spherical distance between two geometries (point or multipoint) on a sphere. ([MDEV-13467](https://jira.mariadb.org/browse/MDEV-13467))
* [Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) updated to 25.3.3

## Issues Fixed

### Can result in data loss

* [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter) fails to rename a column in [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table and causes server to crash. [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table is not accessible after restart. ([MDEV-24763](https://jira.mariadb.org/browse/MDEV-24763))
* Table corruption [ER\_NO\_SUCH\_TABLE\_IN\_ENGINE](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md) or [ER\_CRASHED\_ON\_USAGE](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md) after [ALTER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter) on [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table with foreign key. ([MDEV-24532](https://jira.mariadb.org/browse/MDEV-24532))
* [MariaDB Enterprise Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-enterprise-backup) deletes the current source file after a `No space left on device` error, before exiting. Only the incomplete target file is still available. ([MDEV-25221](https://jira.mariadb.org/browse/MDEV-25221))

### Can result in a hang or crash

* Possible hang when [KILL CONNECTION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/kill) or [KILL QUERY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/kill) is used with [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) and a multi-master setup. ([MDEV-18874](https://jira.mariadb.org/browse/MDEV-18874))
* Possible memory corruption with [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) when inserting values bigger than 4096 bytes into variable-length fields ([BLOB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/blob), [TEXT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/text), [VARCHAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/varchar), and related types). ([MDEV-24978](https://jira.mariadb.org/browse/MDEV-24978))
* [innodb\_flush\_method=O\_DIRECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#innodb_flush_methodb) fails on compressed tables. ([MDEV-25121](https://jira.mariadb.org/browse/MDEV-25121))
* Server crashes in `check_grant` upon invoking function with [userstat](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#userstat) enabled. ([MDEV-25242](https://jira.mariadb.org/browse/MDEV-25242))
* [MariaDB Client](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb/README.md) crashes when --default-character-set is set and --character-sets-dir is undefined. ([MDEV-24879](https://jira.mariadb.org/browse/MDEV-24879))
* Possible Server crash when [dropping a table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table). Only seen when using a table space per table and if the tablespace size is increased at the time of the drop. ([MDEV-20648](https://jira.mariadb.org/browse/MDEV-20648))
* Possible server hang with [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) and indexed virtual columns after an error with [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update), [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert), [REPLACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/replace) on virtual columns. ([MDEV-24786](https://jira.mariadb.org/browse/MDEV-24786))
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) conflict resolution issues. ([MDEV-24923](https://jira.mariadb.org/browse/MDEV-24923))
* Index count mismatch due to aborted `FULLTEXT INDEX` ([MDEV-25200](https://jira.mariadb.org/browse/MDEV-25200))
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) node crashes when inserting a row into a table that contains a virtual column and does not have a primary key. ([MDEV-25047](https://jira.mariadb.org/browse/MDEV-25047))
* Server crashes when [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) fails to add a new index on a new virtual column and a concurrent connection executes a query that accesses the freed virtual column. ([MDEV-24971](https://jira.mariadb.org/browse/MDEV-24971))
* `EXISTS` subquery with correlation in ON expression crashes. ([MDEV-25407](https://jira.mariadb.org/browse/MDEV-25407))
* Server crashes in `row_undo_mod_clust_low` upon rollback of read-only transaction. ([MDEV-25457](https://jira.mariadb.org/browse/MDEV-25457))
* Server crashes on the second execution of a stored procedure when the stored procedure uses an invalid multi-table [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) statement to update a view. ([MDEV-24823](https://jira.mariadb.org/browse/MDEV-24823))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) startup hangs when a recovered transaction exists for the [mysql.innodb\_index\_stats](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#innodb_table_stats) or [mysql.innodb\_table\_stats](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#innodb_table_stat) system tables and a DDL transaction needs to be rolled back. ([MDEV-25503](https://jira.mariadb.org/browse/MDEV-25503))
* Server crashes when [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) tries to fetch data from table containing a FULLTEXT INDEX and the table's tablespace was discarded. ([MDEV-25536](https://jira.mariadb.org/browse/MDEV-25536))
* Server crashes on [SHOW TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-tables) when a WHERE condition references a derived table. ([MDEV-21603](https://jira.mariadb.org/browse/MDEV-21603))
* Potential hang in [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) purge when virtual indexed columns exist. (MENT-1203)
* After [DROP INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-index) or [CREATE INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-index), change buffer entries for secondary indexes are lost on InnoDB restart. (MENT-1217)

### Can result in unexpected behavior

* `SUM` column from a derived table returns invalid values. ([MDEV-23291](https://jira.mariadb.org/browse/MDEV-23291))
* [CAST('0e1111111111' AS DECIMAL(38,0))](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/cast) returns an incorrect result. ([MDEV-24790](https://jira.mariadb.org/browse/MDEV-24790))
* Incorrect behavior of [SET STATEMENT](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-2/SET_STATEMENT/README.md) when it is executed as a prepared statement. ([MDEV-24860](https://jira.mariadb.org/browse/MDEV-24860))
* Query returns a [ER\_BAD\_FIELD\_ERROR](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md) error when a subquery contains a JOIN with an ON clause that references an outer column. ([MDEV-25002](https://jira.mariadb.org/browse/MDEV-25002))
* Query returns a [ER\_BAD\_FIELD\_ERROR](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-2/broken-reference/README.md) error when a Common Table Expression (CTE) contains a `UNION` ([MDEV-24597](https://jira.mariadb.org/browse/MDEV-24597))
* Query returns wrong result when the [MIN()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/aggregate-functions/min) or [MAX()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/aggregate-functions/max) aggregate functions are used and the aggregated column is indexed. ([MDEV-25112](https://jira.mariadb.org/browse/MDEV-25112))
* Wrong result (extra rows and wrong values) with incremental block nested loop hash. ([MDEV-21104](https://jira.mariadb.org/browse/MDEV-21104))
* Query returns wrong results when a `JOIN` is evaluated using the Block Nested Loop Hash (BLNH) optimization with a compound index. ([MDEV-24767](https://jira.mariadb.org/browse/MDEV-24767))
* Server fails to start using `mysqld_multi` with `mysqld_safe` options. ([MDEV-21039](https://jira.mariadb.org/browse/MDEV-21039))
* Duplicate key may be generated during [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) configuration change. ([MDEV-24853](https://jira.mariadb.org/browse/MDEV-24853))
* State snapshot transfer (SST) for [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) using [MariaDB Enterprise Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-enterprise-backup) fails when the --log-bin option was set on the command-line with no value at server startup. ([MDEV-24903](https://jira.mariadb.org/browse/MDEV-24903))
* Race condition between persistent statistics and [RENAME TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/rename-table) or [TRUNCATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/truncate) ([MDEV-25051](https://jira.mariadb.org/browse/MDEV-25051))
* Race condition between [ANALYZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/analyze-table) and `STATS_AUTO_RECALC` ([MDEV-10682](https://jira.mariadb.org/browse/MDEV-10682))
* Incorrect message about field length is written to the [error log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/error-log) when [CHECK TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/check-table) is executed on an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table. ([MDEV-24748](https://jira.mariadb.org/browse/MDEV-24748))
* No error is returned when the optimizer removes a redundant part of a subquery that contains an unknown table alias. For example, if the optimizer removes a redundant `GROUP BY` clause from an [IN()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/operators/comparison-operators/in) subquery, unknown table aliases in the redundant part are ignored. ([MDEV-23449](https://jira.mariadb.org/browse/MDEV-23449))
* Selectivity shown with [EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain) in field `"filter"` is incorrect for [BIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/numeric-data-types/bit) columns. ([MDEV-22583](https://jira.mariadb.org/browse/MDEV-22583))
* Histogram statistics are used even with [optimizer\_use\_condition\_selectivity=3](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_use_condition_selectivity) ([MDEV-19474](https://jira.mariadb.org/browse/MDEV-19474))
* [EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain) shows nonsensical value for `key_len` with `type=index` ([MDEV-11172](https://jira.mariadb.org/browse/MDEV-11172))
* SSL connection fails when server and client certs are signed by same CA. ([MDEV-23740](https://jira.mariadb.org/browse/MDEV-23740))
* Wrong function name in error messages upon [ST\_GeomFromGeoJSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-constructors/st_geomfromgeojson) call. ([MDEV-25272](https://jira.mariadb.org/browse/MDEV-25272))
* [MariaDB Enterprise Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-enterprise-backup) fails [--prepare](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/prepared-statements/prepare-statement) on large backup. ([MDEV-24197](https://jira.mariadb.org/browse/MDEV-24197))
* State snapshot transfer (SST) for [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) using [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) fails when the password for the backup user is set via the `MYSQL_PWD` environment variable. ([MDEV-25321](https://jira.mariadb.org/browse/MDEV-25321))
* State snapshot transfer (SST) for [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) using [MariaDB Enterprise Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-enterprise-backup) fails when the [--innodb](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) option was set on the command-line at server startup. ([MDEV-25328](https://jira.mariadb.org/browse/MDEV-25328))
* An extra warning is returned when the [EXPLAIN EXTENDED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain) statement is executed in a prepared statement. ([MDEV-25108](https://jira.mariadb.org/browse/MDEV-25108))
* Complex query in stored procedure returns wrong results. ([MDEV-25182](https://jira.mariadb.org/browse/MDEV-25182))
* [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) wrongly checks for field's default value if AFTER is used. ([MDEV-25403](https://jira.mariadb.org/browse/MDEV-25403))
* Incorrect name resolution for subqueries in ON expressions. ([MDEV-25362](https://jira.mariadb.org/browse/MDEV-25362))
* When [FLUSH LOGS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) is executed, a race condition between [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) group commit and binary log rotation causes the old binary log file to become obsolete before the [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) group commit has been written to it. ([MDEV-24526](https://jira.mariadb.org/browse/MDEV-24526))
* [MariaDB Enterprise Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-enterprise-backup) logs an error instead of a warning when it reads an invalid log block checksum during a [--backup](../../10-2/broken-reference/). ([MDEV-25456](https://jira.mariadb.org/browse/MDEV-25456))
* Rows are wrongly omitted when an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) index is read using Multiversion Concurrency Control (MVCC). ([MDEV-25459](https://jira.mariadb.org/browse/MDEV-25459))
* [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) aborts after failed [REPLACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/replace) into table with virtual column. ([MDEV-24583](https://jira.mariadb.org/browse/MDEV-24583))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) fails to fetch index type when index mismatch happens. ([MDEV-22928](https://jira.mariadb.org/browse/MDEV-22928))
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) silently enables InnoDB Monitor output and never disables it when a wsrep slave thread tries to perform a brute-force (BF) kill, but fails due to a long lock wait. ([MDEV-25319](https://jira.mariadb.org/browse/MDEV-25319))
* [RENAME TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/rename-table) causes `"Ignoring data file ... with space ID xxxx, since the redo log references ... with space ID xxxx."` for [MariaDB Enterprise Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-enterprise-backup). ([MDEV-25568](https://jira.mariadb.org/browse/MDEV-25568))
* The Replication Heartbeat binary log event (`Heartbeat_log_event`) uses 4 bytes to store the log position within the current binary log file, so the log position overflows when the binary log file size exceeds 4 GB. ([MDEV-16146](https://jira.mariadb.org/browse/MDEV-16146))
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) spatial indexes miss large geometry fields. (MENT-1205)
* Table alias from previous statement interferes with later commands. (MENT-1200)
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) fails to replicate [SET PASSWORD](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/set-password) statement when [strict\_password\_validation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#strict_password_validation) is enabled. ([MDEV-25258](https://jira.mariadb.org/browse/MDEV-25258))

### Related to install and upgrade

* Missing `libsepol` dependency on SLES 12 and SLES 15. (MENT-1163)
* `caching_sha2_password.so` isn't included in Debian packages. ([MDEV-24728](https://jira.mariadb.org/browse/MDEV-24728))
* Minor version upgrade does not perform server restart. ([MDEV-25240](https://jira.mariadb.org/browse/MDEV-25240))

## Interface Changes

* [mariadb-backup --innodb-force-recovery](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_force_recovery) command-line option added
* [mariadb\_repo\_setup --skip-check-installed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage#options) command-line option added
* [ST\_DISTANCE\_SPHERE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-relations/st_distance_sphere) function added

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server-lifecycle.md), MariaDB Enterprise Server 10.2.38-12 is provided for:

* CentOS 7
* CentOS 8
* Debian 9
* Red Hat Enterprise Linux 7
* Red Hat Enterprise Linux 8
* SUSE Linux Enterprise Server 12
* SUSE Linux Enterprise Server 15
* Ubuntu 18.04
* Microsoft Windows

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see ["MariaDB Corporation Engineering Policies".](https://mariadb.com/engineering-policies/)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
