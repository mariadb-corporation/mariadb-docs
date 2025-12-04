# Release Notes for MariaDB Enterprise Server 10.5.13-9

MariaDB Enterprise Server 10.5.13-9 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.5. This release includes a variety of fixes.

MariaDB Enterprise Server 10.5.13-9 was released on 2021-12-13.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/cve.org) link) | CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [CVE-2022-27385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27385)                                                                                               | 7.5             |
| [CVE-2021-46667](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46667)                                                                                               | 7.5             |
| [CVE-2022-31624](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-31624)                                                                                               | 6.5             |
| [CVE-2021-46662](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46662)                                                                                               | 5.5             |
| [CVE-2021-35604](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-35604)                                                                                               | 5.5             |

## Notable Changes

* Galera updated to 26.4.10
* Debian 11 support added
* [Enterprise Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) no longer enables pushdown of UDFs and Stored Functions to the Data Node by default: ([MDEV-26545](https://jira.mariadb.org/browse/MDEV-26545))
  * The default value of [spider\_use\_pushdown\_udf](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) has changed from `-1` to `0`
  * In previous releases, Enterprise Spider pushed UDFs and Stored Functions down to the Data Node by default, which could cause query results to be inconsistent.
  * Starting with this release, all UDFs and stored functions are evaluated on the Spider Node by default. If desired, pushdown of UDFs and Stored Functions can be explicitly enabled by setting `spider_use_pushdown_udf=1`. Testing is recommended to confirm that query results are consistent.
* [Performance Schema tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables) provide descriptions of each column in the `COMMENT` column option. ([MDEV-25325](https://jira.mariadb.org/browse/MDEV-25325))

## Issues Fixed

### Can result in data loss

* InnoDB tables with [ROW\_FORMAT=COMPRESSED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_default_row_format) could be corrupted. (MENT-1367)

### Can result in a hang or crash

* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md), powered by Galera, can crash on [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) if the table does not have a primary key and if the data for a field exceeds 4096 bytes. ([MDEV-24978](https://jira.mariadb.org/browse/MDEV-24978))
* When an InnoDB tablespace (`.ibd`) file is imported using [ALTER TABLE .. IMPORT TABLESPACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) without a corresponding `.cfg` file, InnoDB causes a server crash. ([MDEV-26131](https://jira.mariadb.org/browse/MDEV-26131), [MDEV-20931](https://jira.mariadb.org/browse/MDEV-20931))
* When [OPTIMIZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table) (or [mariadb-check -o](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/table-tools/mariadb-check)) is executed against an InnoDB table with a `FULLTEXT` index, InnoDB can cause a server crash. ([MDEV-25702](https://jira.mariadb.org/browse/MDEV-25702), MENT-1198)
* Resolving aggregate functions that are used in a view can cause in a crash. ([MDEV-24454](https://jira.mariadb.org/browse/MDEV-24454))
* Executing [CREATE OR REPLACE TABLE AS SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) under [LOCK TABLE](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/LOCK-TABLE/README.md) can cause in a crash. ([MDEV-23391](https://jira.mariadb.org/browse/MDEV-23391))
* If two InnoDB tables have a [foreign key](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys) and an operation cascades from the parent table to the child table, an index on a virtual generated column in the child table can become corrupt. ([MDEV-26866](https://jira.mariadb.org/browse/MDEV-26866))
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md), powered by Galera, crashes with errors like: `[ERROR] WSREP: Trx 236236 tries to abort slave trx 236238` ([MDEV-25835](https://jira.mariadb.org/browse/MDEV-25835))
* Server crashes when a table uses a sequence as a column default (`DEFAULT NEXT_VALUE(my_seq)`) and the table is used concurrently by both a prepared statement and a normal statement. ([MDEV-22785](https://jira.mariadb.org/browse/MDEV-22785))
* InnoDB causes server crash when a table is converted from `utf8mb3` to `utf8mb4` ([MDEV-25951](https://jira.mariadb.org/browse/MDEV-25951))
* When enabling [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin), server crash can occur. (MENT-1307)
* [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) occasionally hangs when rotating logs. (MENT-1339)
* InnoDB sometimes causes server crash during [ALTER TABLE .. IMPORT TABLESPACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) when the imported tablespace contains columns that have been instantly reordered or dropped. The MariaDB error log contains the following error message: ([MDEV-26621](https://jira.mariadb.org/browse/MDEV-26621), [MDEV-18543](https://jira.mariadb.org/browse/MDEV-18543))`Schema mismatch - (Index field name newcol doesn't match tablespace metadata field name for field position…`
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) hangs while it is executing `DELETE FROM mysql.wsrep_cluster`, which can be seen in the process list. ([MDEV-26760](https://jira.mariadb.org/browse/MDEV-26760), [MDEV-25883](https://jira.mariadb.org/browse/MDEV-25883))
* Server crashes on 64-bit Windows when MyISAM accesses key buffer and key\_buffer\_size is greater than 4 GB. ([MDEV-26533](https://jira.mariadb.org/browse/MDEV-26533))
* Using [SET GLOBAL innodb\_purge\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_purge_threads) to increase `innodb_purge_threads`, may cause a hang. (MENT-1331)
* Enterprise Spider causes server crash when an [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) operation requires access to a Data Node. ([MDEV-26539](https://jira.mariadb.org/browse/MDEV-26539))
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) can crash due to an incorrect conflict resolution on multi-master setup. ([MDEV-26099](https://jira.mariadb.org/browse/MDEV-26099), [MDEV-24294](https://jira.mariadb.org/browse/MDEV-24294), [MDEV-25114](https://jira.mariadb.org/browse/MDEV-25114))

### Related to install and upgrade

* On CentOS 7, `auth_pam_tool` has incorrect permissions. ([MDEV-26380](https://jira.mariadb.org/browse/MDEV-26380))

## Changes in Storage Engines

This release originally incorporated MariaDB ColumnStore storage engine version 5.6.3.

This release now incorporates MariaDB ColumnStore storage engine version 5.6.5.

## Can result in unexpected behavior

* [skip\_networking](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#skip_networking) does not prevent replication. ([MDEV-24969](https://jira.mariadb.org/browse/MDEV-24969))
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) joiner node incorrectly uses localhost for TLS certificate verification and fails to join cluster when [wsrep\_sst\_method=mariadb-backup](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) and `encrypt=3` are configured. ([MDEV-26360](https://jira.mariadb.org/browse/MDEV-26360))
* `mariadb --binary-mode` is not able to replay some [mysqlbinlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) outputs if `0` is in the data. ([MDEV-25444](https://jira.mariadb.org/browse/MDEV-25444))
* Memory leak with row-based replication can lead to high memory usage on replica servers. ([MDEV-26712](https://jira.mariadb.org/browse/MDEV-26712))
* [SHOW CREATE VIEW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-view) and [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) generate invalid SQL for some complex views. ([MDEV-26299](https://jira.mariadb.org/browse/MDEV-26299))
* When statement-based or mixed replication is used and a DML statement encounters an error in a transaction that creates or drops a temporary table, non-committed writes to transactional tables can be incorrectly replicated to replica servers. ([MDEV-26833](https://jira.mariadb.org/browse/MDEV-26833))
* [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) joiner node fails to join cluster when [wsrep\_sst\_method=mariadb-backup](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) and Backward Compatible SST TLS Mode is configured. ([MDEV-26211](https://jira.mariadb.org/browse/MDEV-26211))
* [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) does not work correctly for UDF and stored functions if used in a query's `WHERE` conditions. ([MDEV-26545](https://jira.mariadb.org/browse/MDEV-26545))
* `CONNECTION_ID` column is `NULL` in [information\_schema.THREAD\_POOL\_QUEUES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_queues-table) ([MDEV-26440](https://jira.mariadb.org/browse/MDEV-26440))
* The server in some cases shows decreasing performance with notes `InnoDB: Cannot close file...` in the error log. This issue occurs only when `open-files-limit` is reached and a `log-checkpoint` is triggered. ([MDEV-25215](https://jira.mariadb.org/browse/MDEV-25215))
* [XA PREPARE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/prepared-statements/prepare-statement) sometimes leads to lock wait timeouts on replica servers. ([MDEV-26682](https://jira.mariadb.org/browse/MDEV-26682))
* Replica server does not invalidate query cache after replicating table updates. (MENT-1360)
* With [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md), a [TRUNCATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/truncate) on a table with a Foreign Key Constraint is not replicated to other nodes. ([MDEV-26053](https://jira.mariadb.org/browse/MDEV-26053))
* Password validation plugins (including [simple\_password\_check](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin)) cause a user's existing password hash to be removed from the server's in-memory privilege cache when the user tries to change their password to an invalid password. ([MDEV-26650](https://jira.mariadb.org/browse/MDEV-26650))
* If an `INVISIBLE` column has a computed default value, an [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) statement that doesn't specify a value for the column causes the default value to be ignored. ([MDEV-25891](https://jira.mariadb.org/browse/MDEV-25891))
* In packets sent from the server, a column's "`Original Name`" field can contain the column's alias instead of original name of the column. This metadata mismatch can cause MariaDB Connectors to raise an exception. ([MDEV-23519](https://jira.mariadb.org/browse/MDEV-23519))
* With [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md), a replica server replicating from a [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) node incorrectly uses the primary server's [server\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) and [wsrep\_gtid\_domain\_id](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_gtid_domain_id) values to generate GTIDs for local transactions. ([MDEV-26250](https://jira.mariadb.org/browse/MDEV-26250))
* MariaDB Enterprise Backup does not write the current GTID to xtrabackup\_binlog\_info when a [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) node is backed up and [wsrep\_gtid\_mode=ON](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_gtid_mode) is set. ([MDEV-26237](https://jira.mariadb.org/browse/MDEV-26237))
* With [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md), changes to [wsrep\_gtid\_domain\_id](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_gtid_domain_id) in `my.cnf` are ignored on node restart. ([MDEV-25115](https://jira.mariadb.org/browse/MDEV-25115))
* When a new [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) node is bootstrapped with `wsrep_gtid_mode=ON` set, the node's configured `server_id` and [wsrep\_gtid\_domain\_id](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_gtid_domain_id) values are overridden by the values present in the node's binary logs. ([MDEV-26223](https://jira.mariadb.org/browse/MDEV-26223))

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.5.13-9 is provided for:

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

* [MariaDB Enterprise Server ](../../11.4/whats-new.md)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.5](../../11.4/whats-new.md)
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

* [Upgrade to MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-from-mariadb-10-5-to-mariadb-10-6)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
