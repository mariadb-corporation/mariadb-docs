# Release Notes for MariaDB Enterprise Server 10.4.12-6

This sixth release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.4 is a maintenance release, including a variety of fixes.

MariaDB Enterprise Server 10.4.12-6 was released on 2020-03-02.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/cve.org) link) | CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [CVE-2020-7221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-7221)                                                                                                 | 7.8             |
| [CVE-2020-2574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2574)                                                                                                 | 5.9             |

## Notable Changes

* The systemd start and stop timeout for the MariaDB service is now set to 900 seconds (15 minutes). ([MDEV-17571](https://jira.mariadb.org/browse/MDEV-17571))
* MariaDB ColumnStore 1.4.3 is included in this release. Specific details on this component may be found in the [ColumnStore 1.4.3 release notes](../../../columnstore/old-releases/columnstore-1-4/).
* For [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) (Galera Library 26.4.4):
  * Setting [socket.recv\_buf\_size](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_provider_options#socketrecv_buf_size) was not effective because it was done after the socket was connected or accepted. The default value also caused TCP receive buffer auto-tuning to be disabled. This lead to sub-optimal performance in high bandwidth WAN clusters. The default value for [socket.recv\_buf\_size](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_provider_options#socketrecv_buf_size) has been changed to auto, which lets the kernel tune the TCP receive buffer. A new variable `socket.send_buf_size` with default value `auto` was added to allow send buffer tuning.
* The `ENFORCE` option for parameter slave-run-triggers-for-rbr can now be used to assure that triggers defined on a table on the replica are executed for row based replication (RBR) when a trigger on a primary (master) exists for this table. The `LOGGING` option already exists, but only allows to execute triggers on the replica for row based replication if no trigger exists for this table on the primary (master). (MENT-607)
* On Windows: Removed a misleading `OS error 203` logged by [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) in the error log when the datadir is defined as a network resource. ([MDEV-21260](https://jira.mariadb.org/browse/MDEV-21260))

## Issues Fixed

### Can result in a hang or crash

* During a server restart [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) recovery could encounter an out-of-memory condition. A restart was only possible after increasing [innodb\_buffer\_pool\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_size) . ([MDEV-19176](https://jira.mariadb.org/browse/MDEV-19176))
* On a rollback of a large insert or update, or during a background task to purge transaction history after a large update or delete, the server could hang. ([MDEV-21509](https://jira.mariadb.org/browse/MDEV-21509))
* On a rollback or during a background task to purge transaction history due to a `SPATIAL INDEX`, the server could hang. ([MDEV-21512](https://jira.mariadb.org/browse/MDEV-21512))
* Crashes could occur rarely when using `ALTER TABLE ... IMPORT TABLESPACE` ([MDEV-21513](https://jira.mariadb.org/browse/MDEV-21513))
* Possible server crash if [binlog\_checksum=CRC32](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) (default) is set and if the value for parameter pos in [SHOW BINLOG EVENTS FROM pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-events) does not point to the beginning of an event in the binary log. ([MDEV-18046](https://jira.mariadb.org/browse/MDEV-18046))
* A replication primary (master) running in semi-sync mode could crash when [RESET MASTER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/reset-master) is executed and the replica reconnects using the GTID protocol. ([MDEV-19376](https://jira.mariadb.org/browse/MDEV-19376))
* [MariaDB Enterprise Backup](../../10-4/broken-reference/) could encounter a deadlock if a backup is taken from a replica with [slave-parallel-threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is set to a value greater than 0 ([MDEV-21255](https://jira.mariadb.org/browse/MDEV-21255))
* [MariaDB Enterprise Backup](../../10-4/broken-reference/) could crash when used in combination with FLUSH TABLES and UNLOCK TABLES (MENT-438)
* The aria\_pack utility crashed when running an offline datafile compress on a table. ([MDEV-14183](https://jira.mariadb.org/browse/MDEV-14183))
* Dropping a partition with wsrep\_OSU\_method=RSU and SESSION sql\_log\_bin=0 caused the [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) (Galera) node to hang. ([MDEV-21189](https://jira.mariadb.org/browse/MDEV-21189))
* Shutdown of a replica (slave) Server could hang when [slave-parallel-threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is set to a value greater than 0 ([MDEV-20821](https://jira.mariadb.org/browse/MDEV-20821))
* Using [SET STATEMENT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set-statement) [max\_statement\_time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_statement_time) to set a timeout for the statement resulted in a crash. (MENT-634)
* Querying the [wsrep\_on](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_on) system status variable after enabling Galera Cluster Replication in [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) for a running server could result in a crash. (MENT-633)

### Can result in unexpected behavior

* Executing [TRUNCATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/truncate) or [OPTIMIZE](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/OPTIMIZE/README.md) on [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) tables could lead to an unexpected `SQL Error (1118): Row size too large,` when [innodb\_strict\_mode=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_strict_mode) (default). ([MDEV-21429](https://jira.mariadb.org/browse/MDEV-21429))
* Queries which use window functions and implicit grouping could return wrong results. ([MDEV-21318](https://jira.mariadb.org/browse/MDEV-21318))
* Queries which use `DISTINCT COUNT(*) OVER()` in the expression returned wrong results. ([MDEV-16579](https://jira.mariadb.org/browse/MDEV-16579))
* Inefficient thread handling in the thread pool, impacting any application that uses the thread pool. ([MDEV-21343](https://jira.mariadb.org/browse/MDEV-21343))
* The MariaDB Enterprise Server config file `mariadb-enterprise.cnf` was not registered as a config file in RPM packages. (MENT-591)
* [ALTER USER IF EXISTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter) generated a SQL syntax error. (MENT-643)
* A query using `GROUP BY` with an expression containing a field of a view could return wrong results. ([MDEV-20922](https://jira.mariadb.org/browse/MDEV-20922))
* Running the script `mysql_tzinfo_to_sql` for [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) could result in inconsistent timezone information across different nodes. ([MDEV-21209](https://jira.mariadb.org/browse/MDEV-21209))
* Using the [--use-memory](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) option with [mariadb-backup](../../10-4/broken-reference/) would cause it to run out of memory. ([MDEV-20679](https://jira.mariadb.org/browse/MDEV-20679))
* For [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) (Galera Library 26.4.4):
  * GCS delivered a JOIN message even if the node was in a DONOR state.
  * GCache could contain mixed histories from different clusters.
  * GComm socket timestamping/liveness checking produced false positives during replication of large transactions, which caused excessive amounts of broken connections.
  * Large transactions were able to monopolize bandwidth when segmentation was configured, causing delayed in messages relayed by segment representative. The fix implements fair queuing of messages.
  * Due to a bug in quorum computation, two primary conflicting primary components were formed when the group merged and partitioned again while the new primary view was forming.
* A range plan was not always used for multi-join queries. ([MDEV-21383](https://jira.mariadb.org/browse/MDEV-21383))
* An [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) on an [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) table adding a new first column which is used to define system versioning period could lead to unexpected errors. This only happened when the transaction-based system version was used. ([MDEV-18865](https://jira.mariadb.org/browse/MDEV-18865), [MDEV-18875](https://jira.mariadb.org/browse/MDEV-18875))

### Related to installation or upgrade

* Server could not be started when [lc\_messages](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#lc_messages) is set in a config file. (MENT-625)

## Interface Changes

* [performance\_schema\_max\_cond\_classes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-system-variables#performance_schema_max_cond_classes) system variable default value changed from 80 to 90

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.4.12-6 is provided for:

* Red Hat Enterprise Linux 8
* Red Hat Enterprise Linux 7
* Red Hat Enterprise Linux 6
* CentOS 8
* CentOS 7
* CentOS 6
* Ubuntu 18.04
* Ubuntu 16.04
* Debian 10
* Debian 9
* Debian 8
* SUSE Linux Enterprise Server 15
* SUSE Linux Enterprise Server 12
* Microsoft Windows

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see [MariaDB Corporation Engineering Policies".](https://mariadb.com/engineering-policies)

#### Note

CentOS 6, Debian 8, and Red Hat Enterprise Linux 6 are no longer supported as per the [MariaDB Engineering Policies".](https://mariadb.com/engineering-policies). Older releases are available from the [MariaDB Downloads page](https://mariadb.com/downloads). Instructions for installation are included as a `README` file within the download.

## Installation Instructions

* [MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server)
* [Enterprise Cluster Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/sharded-mariadb-enterprise-spider-topology)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-4-to-mariadb-10-5)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
