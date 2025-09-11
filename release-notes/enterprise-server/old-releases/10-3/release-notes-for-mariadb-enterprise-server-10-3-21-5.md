# Release Notes for MariaDB Enterprise Server 10.3.21-5

This sixth release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.3 is a maintenance release, including a variety of fixes.

MariaDB Enterprise Server 10.3.22-6 was released on 2020-03-02.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-3/cve.org) link) | \* CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [CVE-2020-2574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-2574)                                                                                                 | 5.9                |

## Notable Changes

* The systemd start and stop timeout for the MariaDB service is now set to 900 seconds (15 minutes). ([MDEV-17571](https://jira.mariadb.org/browse/MDEV-17571))
* For [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) (Galera Library 25.3.29):
  * Setting [socket.recv\_buf\_size](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_provider_options#socketrecv_buf_size) was not effective because it was done after the socket was connected or accepted. The default value also caused TCP receive buffer auto-tuning to be disabled. This lead to sub-optimal performance in high bandwidth WAN clusters. The default value for [socket.recv\_buf\_size](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_provider_options#socketrecv_buf_size) has been changed to `auto`, which lets the kernel tune the TCP receive buffer. A new variable [socket.recv\_buf\_size](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_provider_options#socketrecv_buf_size) with default value `auto` was added to allow send buffer tuning.

## Issues Fixed

### Can result in a hang or crash

* During a server restart [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) recovery could encounter an out-of-memory condition. A restart was only possible after increasing [innodb\_buffer\_pool\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_size) . ([MDEV-19176](https://jira.mariadb.org/browse/MDEV-19176))
* On a rollback of a large insert or update, or during a background task to purge transaction history after a large update or delete, the server could hang. ([MDEV-21509](https://jira.mariadb.org/browse/MDEV-21509))
* On a rollback or during a background task to purge transaction history due to a `SPATIAL INDEX`, the server could hang. ([MDEV-21512](https://jira.mariadb.org/browse/MDEV-21512))
* Crashes could occur rarely when using `ALTER TABLE ... IMPORT TABLESPACE` ([MDEV-21513](https://jira.mariadb.org/browse/MDEV-21513))
* Possible server crash if [binlog\_checksum=CRC32](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) (default) is set and if the value for parameter pos in [SHOW BINLOG EVENTS FROM pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-events) does not point to the beginning of an event in the binary log. ([MDEV-18046](https://jira.mariadb.org/browse/MDEV-18046))
* A replication primary (master) running in semi-sync mode could crash when [RESET MASTER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/reset-master) is executed and the replica reconnects using the GTID protocol. ([MDEV-19376](https://jira.mariadb.org/browse/MDEV-19376))
* [MariaDB Enterprise Backup](../../10-3/broken-reference/) could encounter a deadlock if a backup is taken from a replica with [slave-parallel-threads](release-notes-for-mariadb-enterprise-server-10-3-21-5.md#replication-and-binary-log-server-system-variables/) is set to a value greater than `0` ([MDEV-21255](https://jira.mariadb.org/browse/MDEV-21255))
* [MariaDB Enterprise Backup](../../10-3/broken-reference/) could crash when used in combination with `FLUSH TABLES``and``UNLOCK TABLES``(MENT-438)`
* The `aria_pack` utility crashed when running an offline datafile compress on a table. ([MDEV-14183](https://jira.mariadb.org/browse/MDEV-14183))
* Dropping a partition with [wsrep\_OSU\_method=RSU](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_osu_method) and SESSION [sql\_log\_bin=0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) caused the [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) (Galera) node to hang. ([MDEV-21189](https://jira.mariadb.org/browse/MDEV-21189))
* With active optimizer trace (`optimizer_trace='enabled=on'`) server could crash or the data of the optimizer trace could become corrupted. (MENT-614)

### Can result in unexpected behavior

* Executing [TRUNCATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/truncate) or [OPTIMIZE](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-3/OPTIMIZE/README.md) on [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) tables could lead to an unexpected `SQL Error (1118): Row size too large`, when [innodb\_strict\_mode=ON](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#innodb_strict_mode) (default). ([MDEV-21429](https://jira.mariadb.org/browse/MDEV-21429))
* Queries which use window functions and implicit grouping could return wrong results. ([MDEV-21318](https://jira.mariadb.org/browse/MDEV-21318))
* Queries which use `DISTINCT COUNT(*) OVER()` in the expression returned wrong results. ([MDEV-16579](https://jira.mariadb.org/browse/MDEV-16579))
* Inefficient thread handling in the thread pool, impacting any application that uses the thread pool. ([MDEV-21343](https://jira.mariadb.org/browse/MDEV-21343))
* The MariaDB Enterprise Server config file `mariadb-enterprise.cnf` was not registered as a config file in RPM packages. (MENT-591)
* `ALTER USER IF EXISTS` generated a SQL syntax error. (MENT-643)
* A query using `GROUP BY` with an expression containing a field of a view could return wrong results. ([MDEV-20922](https://jira.mariadb.org/browse/MDEV-20922))
* Running the script `mysql_tzinfo_to_sql` for [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) could result in inconsistent timezone information across different nodes. ([MDEV-21209](https://jira.mariadb.org/browse/MDEV-21209))
* Using the [--use-memory](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md) option with [mariadb-backup](../../10-3/broken-reference/) would cause it to run out of memory. ([MDEV-20679](https://jira.mariadb.org/browse/MDEV-20679))
* For [MariaDB Enterprise Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera-cluster/README.md) (Galera Library 25.3.29):
  * GCS delivered a JOIN message even if the node was in a DONOR state.
  * GCache could contain mixed histories from different clusters.
  * GComm socket timestamping/liveness checking produced false positives during replication of large transactions, which caused excessive amounts of broken connections.
  * Large transactions were able to monopolize bandwidth when segmentation was configured, causing delayed in messages relayed by segment representative. The fix implements fair queuing of messages.
  * Due to a bug in quorum computation, two primary conflicting primary components were formed when the group merged and partitioned again while the new primary view was forming.
* A range plan was not always used for multi-join queries. ([MDEV-21383](https://jira.mariadb.org/browse/MDEV-21383))

### Related to installation or upgrade

* Server could not be started when [lc\_messages](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#lc_messages) is set in a config file. (MENT-625)

## Interface Changes

* None

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.3.22-6 is provided for:

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

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies)".

#### Note

CentOS 6, Debian 8, and Red Hat Enterprise Linux 6 are no longer supported as per the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies). Older releases are available from the [MariaDB Downloads page](https://mariadb.com/downloads). Instructions for installation are included as a `README` file within the download.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
