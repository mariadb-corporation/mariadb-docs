# Old MySQL Versions

[MariaDB 5.1](release-notes-mariadb-5-1-series/changes-improvements-in-mariadb-5-1.md) was the first release of MariaDB. It was based on MySQL 5.1.

In a sense, users can think about MySQL 5.0 and older releases (or even older releases of the MySQL 5.1 tree) as old versions of MariaDB.

This page lists the main features that were added in very old MySQL trees, before MariaDB was created. This is done for historical purpose, and can also be useful for users who still run those versions.

## MySQL 3.22

* Configuration files
* Compressed protocol
* HAVING
* [FLUSH TABLES, LOGS, PRIVILEGES, HOSTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush)
* [GRANT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant) and [REVOKE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/revoke)
* [KILL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/kill)
* [CREATE INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-index), [DROP INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-index)
* [HIGH\_PRIORITY and LOW\_PRIORITY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/high_priority-and-low_priority), [DELAYED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert-delayed)

## MySQL 3.23

* [Replication](https://mariadb.com/docs/server/server-usage/storage-engines/myrocks/myrocks-and-replication) (only statement-based, no SSL).
* Temporary tables
* Portable tables through different machines
* [SQL\_MODE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode)
* [User defined functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/user-defined-functions)
* [Procedure ANALYSE()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/procedure-analyse)
* New storage engines:
  * HEAP (now called [MEMORY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/memory-storage-engine))
  * [MyISAM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myisam-storage-engine) (which replaced ISAM)
  * InnoDB
  * [bdb](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#skip-bdb) (removed in MySQL 5.1; no version of MariaDB included it)
* [COUNT(DISTINCT)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/aggregate-functions/count-distinct)
* Table comments
* ...

## MySQL 4.0

* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) enabled by default.
* Dynamic configuration variables.
* [FULLTEXT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/full-text-index-overview) for MyISAM.
* [UNION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/union).
* [TRUNCATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/truncate-table).
* Multi-table DELETE and UPDATE.
* [Query cache](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache).
* Embedded server.

## MySQL 4.1

* [Subqueries](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/subqueries) (not optimized).
* Faster protocol.
* [Prepared statements](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/prepared-statements).
* [GIS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/geometry) support for MyISAM
* B-TREE for MEMORY tables.
* Replication over [SSL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview).
* UTF-8 character set.
* New storage engines:
  * [ARCHIVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/archive)
  * [CSV](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/csv)
  * [BLACKHOLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/blackhole)

## MySQL 5.0

* [Views](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/views).
* [Stored Procedures](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-procedures)
* [Stored Functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-functions)
* [Triggers](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/triggers-events/triggers)
* [XA Transactions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/xa-transactions)

## MySQL 5.1 (older releases)

* [Events](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/triggers-events/event-scheduler)
* Partitioning.
* Storage engines API.
* Plugins API.
* [Row-based and mixed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log/binary-log-formats) replication.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
