# Release Notes for MariaDB Enterprise Server 10.4.26-17

MariaDB Enterprise Server 10.4.26-17 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-enterprise-server/README.md) 10.4. This release includes a variety of fixes.

MariaDB Enterprise Server 10.4.26-17 was released on 2022-09-12.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-4/cve.org) link) | CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [CVE-2023-5157](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5157)                                                                                                 | 7.5             |
| [CVE-2018-25032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-25032)                                                                                               | 7.5             |
| [CVE-2022-32091](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32091)                                                                                               | 6.5             |
| [CVE-2022-32089](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32089)                                                                                               | 6.5             |
| [CVE-2022-32084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32084)                                                                                               | 6.5             |
| [CVE-2022-32081](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32081)                                                                                               | 6.5             |

## Notable Changes

* Galera has been updated to 26.4.13-1
* Debian 9 support has been discontinued.
* The [--max-statement-time command-line option](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump#options) has been added for [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) with a default value of 0. ([MDEV-18702](https://jira.mariadb.org/browse/MDEV-18702))

## Issues Fixed

### Can result in data loss

* When [mariadb-backup](../../10-4/broken-reference/) is executed with the [--rsync](../../10-4/broken-reference/) command-line option, the backup tries to copy the InnoDB buffer pool dump file, which is located at the path defined by the [innodb\_buffer\_pool\_filename](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_filename) system variable. ([MDEV-28781](https://jira.mariadb.org/browse/MDEV-28781))
  * Starting with this release, [mariadb-backup](../../10-4/broken-reference/) only copies the InnoDB buffer pool dump file during State Snapshot Transfers (SSTs) for MariaDB Enterprise Cluster, powered by Galera.
* When [ALTER TABLE .. IMPORT TABLESPACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) is executed against an encrypted InnoDB tablespace file, the table can be corrupted. ([MDEV-28779](https://jira.mariadb.org/browse/MDEV-28779))
* With MariaDB Enterprise Cluster, when [read\_only](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#read_only) is enabled on a node, users without the [SUPER privilege](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#super) can still write to the node. ([MDEV-28546](https://jira.mariadb.org/browse/MDEV-28546))
* With MariaDB Enterprise Cluster, when a value is retrieved from an InnoDB sequence using the [NEXTVAL() function](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/sequence-functions/nextval), the change is not replicated. ([MDEV-27862](https://jira.mariadb.org/browse/MDEV-27862))
  * Starting with this release, InnoDB sequences are properly replicated when they are defined with `NOCACH`.
* When an InnoDB table's collation is changed using [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) with the `INPLACE` or `NOCOPY` algorithms, duplicate entries in unique indexes are not detected. ([MDEV-26294](https://jira.mariadb.org/browse/MDEV-26294))

### Can result in a hang or crash

* When `INSERT .. SELECT .. GROUP BY` is executed and the GROUP BY clause contains a derived table, the server can crash. ([MDEV-28617](https://jira.mariadb.org/browse/MDEV-28617))
* When a query contains an `ANY(SELECT .. GROUP BY(SELECT ..))` predicand with a redundant subquery in the `GROUP BY` clause, the server can crash. ([MDEV-29139](https://jira.mariadb.org/browse/MDEV-29139))
* When `ALTER TABLE .. ADD` is used to add a column with the `INSTANT` algorithm, the server can crash if the `ROW_FORMAT` in the `.frm` file does not match the actual row format used by the data file. ([MDEV-26577](https://jira.mariadb.org/browse/MDEV-26577))
* For tables created prior to MariaDB Server 10.2, the `ROW_FORMAT` in the `.frm` file could be inconsistent with the actual row format used by the data file. If the server were upgraded to MariaDB Enterprise Server 10.6, the inconsistency could remain.
* When `INSERT .. SELECT` is executed and the `SELECT` query calls an aggregate or window function, the server can crash with a segmentation fault. ([MDEV-26427](https://jira.mariadb.org/browse/MDEV-26427))
* When the [JSON\_EXTRACT() function](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_extract) is called, the server can crash with a segmentation fault. ([MDEV-29188](https://jira.mariadb.org/browse/MDEV-29188))
* When a query uses the `DISTINCT` keyword and calls an aggregate function as an argument for an always-constant function, the server can crash. ([MDEV-23809](https://jira.mariadb.org/browse/MDEV-23809))
  * An always-constant function is a function that always returns a constant value, even if the function's arguments are not constant.
  * For example, the [COLLATION() function](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/collation) is an always-constant function.
* When [mariadb-backup](../../10-4/broken-reference/) is executed with the [--compress](../../10-4/broken-reference/) and [--parallel](../../10-4/broken-reference/) options, the backup can hang due to a race condition between threads. ([MDEV-29043](https://jira.mariadb.org/browse/MDEV-29043))
* When an `EXISTS` predicate or an `IN`, `ALL`, or `ANY` predicand is used in an eliminated GROUP BY clause, the server can crash. (MENT-1606, [MDEV-29350](https://jira.mariadb.org/browse/MDEV-29350))
* When an `IN` subquery is used outside the context of a regular query (such as in a stored procedure), the server can crash. ([MDEV-22001](https://jira.mariadb.org/browse/MDEV-22001))
* When MariaDB Enterprise Cluster is used and the Galera replication TCP port receives non-Galera network traffic, the server can crash. ([MDEV-25068](https://jira.mariadb.org/browse/MDEV-25068))
  * In previous releases, when the crash occurred, the following messages would appear in the [MariaDB error log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/error-log):

```
terminate called after throwing an instance of 'boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<std::system_error> >'
what(): remote_endpoint: Transport endpoint is not connected
[ERROR] mysqld got signal 6 ;
```

* When a generated column is added to an InnoDB table with the `INSTANT` algorithm, the server can crash due to a buffer overflow. ([MDEV-26420](https://jira.mariadb.org/browse/MDEV-26420))
* When [CREATE VIEW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/views/create-view) is executed with a view definition that contains an unknown column in an ON condition, the server can crash instead of raising an error with the [ER\_BAD\_FIELD\_ERROR](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) error code. ([MDEV-29088](https://jira.mariadb.org/browse/MDEV-29088))

### Can result in unexpected behavior

For multi-table [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) or [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) queries, the optimizer fails to apply partition pruning optimization for the table that is updated or deleted from. ([MDEV-28246](https://jira.mariadb.org/browse/MDEV-28246))

* When an `IN` condition contains a mixture of numeric and string values, results can be inconsistent. ([MDEV-21445](https://jira.mariadb.org/browse/MDEV-21445))
* When a sequence event is written to the binary log with [binlog\_format=ROW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables), the value of [binlog\_row\_image](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is not respected. ([MDEV-28487](https://jira.mariadb.org/browse/MDEV-28487))
* When a transaction can't be fully written to the binary log, but the transaction can be safely rolled back, a LOST\_EVENTS incident event is written to the binary log. ([MDEV-21443](https://jira.mariadb.org/browse/MDEV-21443))
  * In previous releases, this problem could cause replica servers to encounter the following error:

```
Last_SQL_Errno	1590
Last_SQL_Error	The incident LOST_EVENTS occurred on the master. Message: error writing to the binary log
```

* Starting with this release, a `LOST_EVENTS` incident is only written to the binary log\
  when safe rollback is not possible.
* When a replica server replicates an incident event, the details about the failure are not in the primary server's error log, the replica server's error log, or the output of [SHOW REPLICA STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status). ([MDEV-21087](https://jira.mariadb.org/browse/MDEV-21087))
* When a backup is performed with [mariadb-backup](../../10-4/broken-reference/), the backup includes binary logs. ([MDEV-28758](https://jira.mariadb.org/browse/MDEV-28758))
* When a table is created from a [SELECT statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) that uses a recursive CTE, the table can use unexpected data types and contain truncated data if the calculated values from the recursive part of the CTE do not fit in the column types that are taken from the non-recursive part of the CTE. ([MDEV-12325](https://jira.mariadb.org/browse/MDEV-12325))
  * Starting with this release, the CTE calculation is aborted when the calculated values do not fit in the column types. When this occurs, a warning or error (depending on [sql\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode) is raised with the [ER\_WARN\_DATA\_OUT\_OF\_RANGE](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) error code and the following error message:

```
Out of range value for column 'COLUMN_NAME' at row ROW_NUM
```

* When [mariadb client](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) uses `EditLine` instead of `readline` (such as on Debian and Ubuntu), Unicode characters are not accepted. ([MDEV-28197](https://jira.mariadb.org/browse/MDEV-28197))
* When the optimizer chooses a semi-join optimization for a subquery, the LooseScan and FirstMatch strategies are not considered for certain queries where they would be appropriate, and they are considered for certain queries where they would be inappropriate. ([MDEV-28749](https://jira.mariadb.org/browse/MDEV-28749))
* When `FULLTEXT` search is performed on an InnoDB table, the results are incorrect when the search term contains an apostrophe ('). ([MDEV-20797](https://jira.mariadb.org/browse/MDEV-20797))
  * Starting with this release, when a search term contains an apostrophe ('), InnoDB tokenizes the word at the apostrophe, ignores the first token, and matches against the second token.
* After upgrading from old versions of MariaDB Server, some [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) operations fail if `ALGORITHM=NOCOPY` is specified. ([MDEV-28727](https://jira.mariadb.org/browse/MDEV-28727))
  * In previous releases, the following error could be raised:

```
ERROR 1845 (0A000): ALGORITHM=NOCOPY is not supported for this operation. Try ALGORITHM=INPLACE
```

## Interface Changes

* `mariadb-backup` [--sst-max-binlogs](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-4/broken-reference/README.md) command-line option removed
* `mysql` [--enable-cleartext-plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables) command-line option added
* `mysqld` [--spider-direct-aggregate](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/spider-status-variables) command-line option added
* `mysqldump` [--max-statement-time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump#options) command-line option added
* [spider\_direct\_aggregate](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/spider-status-variables) system variable added

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.4.26-17 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64, ARM64)
* Microsoft Windows (x86\_64) (MariaDB Enterprise Cluster excluded)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64 Red Hat Enterprise Linux 8 packages)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see [MariaDB Corporation Engineering Policies".](https://mariadb.com/engineering-policies).

## Installation Instructions

* [MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server)
* [Enterprise Cluster Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[10](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)[.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/sharded-mariadb-enterprise-spider-topology)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-architecture/mariadb-enterprise-spider-topologies/federated-mariadb-enterprise-spider-topology)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-4-to-mariadb-10-5)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
