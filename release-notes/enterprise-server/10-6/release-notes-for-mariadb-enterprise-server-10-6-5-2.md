# Release Notes for MariaDB Enterprise Server 10.6.5-2

MariaDB Enterprise Server 10.6.5-2 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-enterprise-server/README.md) 10.6. This release includes a variety of fixes.

MariaDB Enterprise Server 10.6.5-2 was released on 2021-12-13.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-6/cve.org) link) | CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-6/cve.org) link) | CVSS base score |
| [CVE-2022-27385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27385)                                                                                               | 7.5             |
| [CVE-2021-46667](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46667)                                                                                               | 7.5             |
| [CVE-2022-31624](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31624)                                                                                               | 6.5             |
| [CVE-2021-46662](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46662)                                                                                               | 5.5             |

## Notable Changes

* Galera updated to 26.4.10.
* Debian 11 support added.
* [Enterprise Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) no longer enables pushdown of UDFs and Stored Functions to the Data Node by default: ([MDEV-26545](https://jira.mariadb.org/browse/MDEV-26545))
  * The default value of [spider\_use\_pushdown\_udf](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) has changed from -1 to 0
  * In previous releases, Enterprise Spider pushed UDFs and Stored Functions down to the Data Node by default, which could cause query results to be inconsistent.
  * Starting with this release, all UDFs and stored functions are evaluated on the Spider Node by default. If desired, pushdown of UDFs and Stored Functions can be explicitly enabled by setting `spider_use_pushdown_udf=1`. Testing is recommended to confirm that query results are consistent.
* [Performance Schema tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/list-of-performance-schema-tables) provide descriptions of each column in the `COMMENT` column option. ([MDEV-25325](https://jira.mariadb.org/browse/MDEV-25325))
* In the Spider ODBC Topology, [Enterprise Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) automatically sets the appropriate transaction isolation level for the ODBC data source. (MENT-1328)
* The InnoDB Force Recovery procedure has changed to differentiate between rollback of DDL and DML operations. The changes are: ([MDEV-25683](https://jira.mariadb.org/browse/MDEV-25683))
  * The behavior of [innodb\_force\_recovery](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_force_recovery) is no longer identical when `innodb_force_recovery=3` and `innodb_force_recovery=4`
  * When `innodb_force_recovery=3` is set, InnoDB skips rollback of DML operations, but DDL operations will still be rolled back using the DDL log.
  * When `innodb_force_recovery=4` is set, InnoDB skips rollback of both DML and DDL operations. This behavior is equivalent to setting `innodb_force_recovery=3` in versions earlier than MariaDB Enterprise Server 10.6.5.

## Issues Fixed

### Can result in data loss

* InnoDB tables with `ROW_FORMAT=COMPRESSED` could be corrupted. (MENT-1367)

### Can result in a hang or crash

* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera-cluster/README.md), powered by Galera, can crash on [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) if the table does not have a primary key and if the data for a field exceeds 4096 bytes. ([MDEV-24978](https://jira.mariadb.org/browse/MDEV-24978))
* When an InnoDB tablespace (`.ibd`) file is imported using [ALTER TABLE .. IMPORT TABLESPACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) without a corresponding .cfg file, InnoDB causes a server crash. ([MDEV-26131](https://jira.mariadb.org/browse/MDEV-26131), [MDEV-20931](https://jira.mariadb.org/browse/MDEV-20931))
* When [OPTIMIZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table) (or [mariadb-check -o](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/table-tools/mariadb-check)) is executed against an InnoDB table with a `FULLTEXT` index, InnoDB can cause a server crash. ([MDEV-25702](https://jira.mariadb.org/browse/MDEV-25702), MENT-1198)
* Resolving aggregate functions that are used in a view can cause in a crash. ([MDEV-24454](https://jira.mariadb.org/browse/MDEV-24454))
* Executing [CREATE OR REPLACE TABLE AS SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) under [LOCK TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/lock-tables) can cause in a crash. ([MDEV-23391](https://jira.mariadb.org/browse/MDEV-23391))
* If two InnoDB tables have a [foreign key](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys) and an operation cascades from the parent table to the child table, an index on a virtual generated column in the child table can become corrupt. ([MDEV-26866](https://jira.mariadb.org/browse/MDEV-26866))
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera-cluster/README.md), powered by Galera, crashes with errors like: \[ERROR] WSREP: Trx 236236 tries to abort slave trx 236238 ([MDEV-25835](https://jira.mariadb.org/browse/MDEV-25835))
* Server crashes when a table uses a sequence as a column default [(DEFAULT NEXT\_VALUE(my\_seq))](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/sequence-functions/nextval) and the table is used concurrently by both a prepared statement and a normal statement. ([MDEV-22785](https://jira.mariadb.org/browse/MDEV-22785))
* InnoDB causes server crash when a table is converted from `utf8mb3` to `utf8mb4` ([MDEV-25951](https://jira.mariadb.org/browse/MDEV-25951))
* When enabling [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin), server crash can occur. (MENT-1307)
* [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) occasionally hangs when rotating logs. (MENT-1339)
* On 64-bit Microsoft Windows when MyISAM accesses key buffer and [key\_buffer\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myisam-storage-engine/myisam-system-variables#key_buffer_size) is greater than 4 GB, the server crashes. ([MDEV-26533](https://jira.mariadb.org/browse/MDEV-26533))
* Using [SET GLOBAL innodb\_purge\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_purge_threads) to increase `innodb_purge_threads`, may cause a hang. (MENT-1331)
* [Enterprise Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) causes server crash when an [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) operation requires access to a Data Node. ([MDEV-26539](https://jira.mariadb.org/browse/MDEV-26539))
* InnoDB persistent statistics causes server to hang. ([MDEV-15020](https://jira.mariadb.org/browse/MDEV-15020))
* On an InnoDB table, when a DDL statement rebuilds the parent table in a [foreign key](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys) relationship, a concurrent `INSERT` into the child table sometimes causes a crash. ([MDEV-26554](https://jira.mariadb.org/browse/MDEV-26554))
* On an InnoDB table, when the server crashes or is killed while a [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table) or table-rebuilding [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) operation is being executed, InnoDB causes a server crash during crash recovery, which occurs after the server has restarted. (MENT-1368)
* InnoDB sometimes causes server crash during [ALTER TABLE .. IMPORT TABLESPACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) when the imported tablespace contains columns that have been instantly reordered or dropped. The MariaDB error log contains the following error message: ([MDEV-18543](https://jira.mariadb.org/browse/MDEV-18543)) `Schema mismatch (Index field name newcol doesn't match tablespace metadata field name for field position...`
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera-cluster/README.md) causes server crash when `wsrep_on=OFF` is set and transactions are in progress. (MENT-1236)

### Can result in unexpected behavior

* `skip_networking` does not prevent replication. ([MDEV-24969](https://jira.mariadb.org/browse/MDEV-24969))
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera-cluster/README.md) joiner node incorrectly uses `localhost` for TLS certificate verification and fails to join cluster when [wsrep\_sst\_method=mariadb-backup](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) and `encrypt=3` are configured. ([MDEV-26360](https://jira.mariadb.org/browse/MDEV-26360))
* [mariadb --binary-mode](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) is not able to replay some [mysqlbinlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) outputs if `0` is in the data. ([MDEV-25444](https://jira.mariadb.org/browse/MDEV-25444))
* Memory leak with row-based replication can lead to high memory usage on replica servers. ([MDEV-26712](https://jira.mariadb.org/browse/MDEV-26712))
* [SHOW CREATE VIEW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-view) and [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) generate invalid SQL for some complex views. ([MDEV-26299](https://jira.mariadb.org/browse/MDEV-26299))
* When statement-based or mixed replication is used and a DML statement encounters an error in a transaction that creates or drops a temporary table, non-committed writes to transactional tables can be incorrectly replicated to replica servers. ([MDEV-26833](https://jira.mariadb.org/browse/MDEV-26833))
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera-cluster/README.md) joiner node fails to join cluster when [wsrep\_sst\_method=mariadb-backup](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) and [Backward Compatible SST TLS Mode](broken-reference) is configured. ([MDEV-26211](https://jira.mariadb.org/browse/MDEV-26211))
* Spider does not work correctly for UDF and stored functions if used in a query's `WHERE` conditions. ([MDEV-26545](https://jira.mariadb.org/browse/MDEV-26545))
* If an `INVISIBLE` column has a computed default value, an `INSERT` statement that doesn't specify a value for the column causes the default value to be ignored. ([MDEV-25891](https://jira.mariadb.org/browse/MDEV-25891))
* Password validation plugins (including [simple\_password\_check](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin)) cause a user's existing password hash to be removed from the server's in-memory privilege cache when the user tries to change their password to an invalid password. ([MDEV-26650](https://jira.mariadb.org/browse/MDEV-26650))
* With [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera-cluster/README.md), a [TRUNCATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/truncate) on a table with a Foreign Key Constraint is not replicated to other nodes. ([MDEV-26053](https://jira.mariadb.org/browse/MDEV-26053))
* InnoDB's adaptive purging can decrease throughput by starving user threads after `dict_sys.mutex` removal. ([MDEV-26356](https://jira.mariadb.org/browse/MDEV-26356))
* `CONNECTION_ID` column is `NULL` in [information\_schema.THREAD\_POOL\_QUEUES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_queues-table) ([MDEV-26440](https://jira.mariadb.org/browse/MDEV-26440))
* The server in some cases shows decreasing performance with notes `InnoDB: Cannot close file...` in the error log. This issue occurs only when `open-files-limit` is reached and a `log-checkpoint` is triggered. ([MDEV-25215](https://jira.mariadb.org/browse/MDEV-25215))
* `XA PREPARE` sometimes leads to lock wait timeouts on replica servers. ([MDEV-26682](https://jira.mariadb.org/browse/MDEV-26682))
* Replica server does not invalidate query cache after replicating table updates. (MENT-1360)
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera-cluster/README.md), powered by Galera, shows inconsistent values for `wsrep_apply_window` and `wsrep_commit_window` when comparing `performance_schema.galera_group_members` and `information_schema.GLOBAL_STATUS` (MENT-1333)
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera-cluster/README.md) incorrectly streams XA transactions when `wsrep_trx_fragment_unit=statements` is set, which causes errors when the fragment is applied. (MENT-1344)
* With [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera-cluster/README.md), a replica server replicating from a [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera-cluster/README.md) node incorrectly uses the primary server's [server\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) and [wsrep\_gtid\_domain\_id](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_gtid_domain_id) values to generate GTIDs for local transactions. ([MDEV-26250](https://jira.mariadb.org/browse/MDEV-26250))
* MariaDB Enterprise Backup does not write the current GTID to `xtrabackup_binlog_info` when a [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera-cluster/README.md) node is backed up and `wsrep_gtid_mode=ON` is set. ([MDEV-26237](https://jira.mariadb.org/browse/MDEV-26237))
* When a new [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera-cluster/README.md) node is bootstrapped with `wsrep_gtid_mode=ON` set, the node's configured `server_id` and [wsrep\_gtid\_domain\_id](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_gtid_domain_id) values are overridden by the values present in the node's binary logs. ([MDEV-26223](https://jira.mariadb.org/browse/MDEV-26223))
* With [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera-cluster/README.md), changes to [wsrep\_gtid\_domain\_id](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_gtid_domain_id) in `my.cnf` are ignored on node restart. ([MDEV-25115](https://jira.mariadb.org/browse/MDEV-25115))

### Related to install and upgrade

* On CentOS 7, `auth_pam_tool` has incorrect permissions. ([MDEV-26380](https://jira.mariadb.org/browse/MDEV-26380))
* Running [mariadb-upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/deployment-tools/mariadb-upgrade) with no `'root'@'localhost'` user may fail with the message `The user specified as a definer ('root'@'localhost') does not exist FATAL ERROR: Upgrade failed`. ([MDEV-26925](https://jira.mariadb.org/browse/MDEV-26925))

## Changes in Storage Engines

* This release originally incorporated MariaDB [ColumnStore storage engine version 6.2.2](../../columnstore/mariadb-columnstore-6-release-notes/mariadb-columnstore-6-2-2-release-notes.md).
* This release now incorporates [MariaDB ColumnStore storage engine version 6.2.3](../../columnstore/mariadb-columnstore-6-release-notes/mariadb-columnstore-6-2-3-release-notes.md).

## Platforms

In alignment to the [enterprise lifecycle](../enterprise-server-lifecycle.md), MariaDB Enterprise Server 10.6.5-2 is provided for:

* CentOS 7 (x86\_64)
* Debian 9 (x86\_64, ARM64)
* Debian 10 (x86\_64, ARM64)
* Debian 11 (x86\_64, ARM64)
* Microsoft Windows (x86\_64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 18.04 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see [MariaDB Corporation Engineering Policies".](https://mariadb.com/engineering-policies)

## Installation Instructions

* [MariaDB Enterprise Server ](../11-4/whats-new-in-mariadb-enterprise-server-11-4.md)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.6](../11-4/whats-new-in-mariadb-enterprise-server-11-4.md)
* [Enterprise Cluster Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)[6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [ColumnStore Object Storage Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)[6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[ and MariaDB Enterprise ColumnStore 23.02](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[ and MariaDB Enterprise ColumnStore 23.02](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)
* [HTAP Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)[6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[ and MariaDB Enterprise ColumnStore 23.02](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)
* [Single-Node Enterprise ColumnStore 23.02 with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)[6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[ and Object Storage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)
* [Single-Node Enterprise ColumnStore 23.02 with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies)[6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/sharded-mariadb-enterprise-spider-topology)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/sharded-mariadb-enterprise-spider-topology)[6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server 10.](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-from-to-specific-versions/upgrading-from-mariadb-10-5-to-mariadb-10-6)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-between-major-mariadb-versions)

##

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
