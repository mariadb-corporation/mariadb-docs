# Release Notes for MariaDB Enterprise Server 10.5.17-12

MariaDB Enterprise Server 10.5.17-12 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.5. This release includes a variety of fixes.

MariaDB Enterprise Server 10.5.17-12 was released on 2022-09-12.

## Fixed Security Vulnerabilities

| CVE (with cve.org link)                                                         | CVSS base score |
| ------------------------------------------------------------------------------- | --------------- |
| [CVE-2023-5157](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5157)   | 7.5             |
| [CVE-2018-25032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-25032) | 7.5             |
| [CVE-2022-32091](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32091) | 6.5             |
| [CVE-2022-32089](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32089) | 6.5             |
| [CVE-2022-32084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32084) | 6.5             |
| [CVE-2022-32082](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32082) | 6.5             |
| [CVE-2022-32081](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32081) | 6.5             |

## Notable Changes

* Galera has been updated to 26.4.13-1
* Debian 9 support has been discontinued.
* Red Hat Enterprise Linux 9 support has been added.
* Rocky Linux 9 support has been added.
* The [--max-statement-time command-line option](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump#options) has been added for `mariadb-dump` with a default value of 0.
* Session scope has been added for the [explicit\_defaults\_for\_timestamp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#explicit_defaults_for_timestamp) system variable]], in addition to global scope.

## Issues Fixed

### Can result in data loss

* When [mariadb-backup](../../10-5/broken-reference/) is executed with the [--rsync](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-5/broken-reference/README.md) command-line option, the backup tries to copy the InnoDB buffer pool dump file, which is located at the path defined by the [innodb\_buffer\_pool\_filename system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_filename).
  * Starting with this release, [mariadb-backup](../../10-5/broken-reference/) only copies the InnoDB buffer pool dump file during State Snapshot Transfers (SSTs) for MariaDB Enterprise Cluster, powered by Galera.
* With MariaDB Enterprise Cluster, when [read\_only](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#read_only) is enabled on a node, users without the [SUPER privilege](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#super) can still write to the node.
* With MariaDB Enterprise Cluster, when a value is retrieved from an InnoDB sequence using the [NEXTVAL() function](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/sequence-functions/nextval), the change is not replicated.
  * Starting with this release, InnoDB sequences are properly replicated when they are defined with `NOCACHE`.
* When an InnoDB table's collation is changed using [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) with the `INPLACE` or `NOCOPY` algorithms, duplicate entries in unique indexes are not detected.

### Can result in a hang or crash

* When `INSERT .. SELECT .. GROUP BY` is executed and the `GROUP BY` clause contains a derived table, the server can crash.
* When a query contains an `ANY(SELECT .. GROUP BY(SELECT ..))` predicand with a redundant subquery in the `GROUP BY` clause, the server can crash.
* When [ALTER TABLE .. ADD](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) is used to add a column with the `INSTANT` algorithm, the server can crash if the `ROW_FORMAT` in the `.frm` file does not match the actual row format used by the data file.
  * For tables created prior to MariaDB Server 10.2, the `ROW_FORMAT` in the `.frm` file could be inconsistent with the actual row format used by the data file. If the server were upgraded to MariaDB Enterprise Server 10.6, the inconsistency could remain.
* When `INSERT .. SELECT` is executed and the `SELECT` query calls an aggregate or window function, the server can crash with a segmentation fault.
* When the [JSON\_EXTRACT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_extract) function is called, the server can crash with a segmentation fault.
* When a query uses the `DISTINCT` keyword and calls an aggregate function as an argument for an always-constant function, the server can crash.
  * An always-constant function is a function that always returns a constant value, even if the function's arguments are not constant.
  * For example, the [COLLATION() function](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/collation) is an always-constant function.
* When [mariadb-backup](../../10-5/broken-reference/) is executed with the [--compress](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-5/broken-reference/README.md) and [--parallel](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-5/broken-reference/README.md) options, the backup can hang due to a race condition between threads.
* When an `EXISTS` predicate or an `IN`, `ALL`, or `ANY` predicand is used in an eliminated `GROUP BY` clause, the server can crash.
* When an `IN` subquery is used outside the context of a regular query (such as in a stored procedure), the server can crash.
* When MariaDB Enterprise Cluster is used and the Galera replication TCP port receives non-Galera network traffic, the server can crash.
  * In previous releases, when the crash occurred, the following messages would appear in the [MariaDB error log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/error-log):

```
terminate called after throwing an instance of 'boost::exception_detail::clone_impl<boost::exception_detail::error_info_injector<std::system_error> >'
what(): remote_endpoint: Transport endpoint is not connected
[ERROR] mysqld got signal 6 ;
```

* When a generated column is added to an InnoDB table with the `INSTANT` algorithm, the server can crash due to a buffer overflow.
* When [CREATE VIEW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/views/create-view) is executed with a view definition that contains an unknown column in an ON condition, the server can crash instead of raising an error with the `ER_BAD_FIELD_ERROR` error code.
* When [FLUSH BINARY LOGS](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/FLUSH-BINARY-LOGS/README.md) is executed, the server can hang.
* When the [innodb\_open\_files system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_open_files) is too low, the server can crash if InnoDB accesses too many tables or partitions.

## Can result in unexpected behavior

* For multi-table [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) or [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) queries, the optimizer fails to apply partition pruning optimization for the table that is updated or deleted from.
* When an `IN` condition contains a mixture of numeric and string values, results can be inconsistent.
* When a sequence event is written to the binary log with [binlog\_format=ROW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables), the value of [binlog\_row\_image](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is not respected.
* When a transaction can't be fully written to the binary log, but the transaction can be safely rolled back, a `LOST_EVENTS` incident event is written to the binary log.
  * In previous releases, this problem could cause replica servers to encounter the following error:

```
Last_SQL_Errno	1590
Last_SQL_Error	The incident LOST_EVENTS occurred on the master. Message: error writing to the binary log
```

* Starting with this release, a `LOST_EVENTS` incident is only written to the binary log when safe rollback is not possible.
* When a replica server replicates an incident event, the details about the failure are not in the primary server's error log, the replica server's error log, or the output of `SHOW REPLICA STATUS`.
* When a backup is performed with [mariadb-backup](../../10-5/broken-reference/), the backup includes binary logs.
* When a table is created from a [SELECT statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) that uses a recursive CTE, the table can use unexpected data types and contain truncated data if the calculated values from the recursive part of the CTE do not fit in the column types that are taken from the non-recursive part of the CTE.
  * Starting with this release, the CTE calculation is aborted when the calculated values do not fit in the column types. When this occurs, a warning or error (depending on `sql_mode` is raised with the [ER\_WARN\_DATA\_OUT\_OF\_RANGE error code](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-5/broken-reference/README.md) and the following error message:

```
Out of range value for column 'COLUMN_NAME' at row ROW_NUM
```

* When [mariadb client](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb/README.md) uses `EditLine` instead of readline (such as on Debian and Ubuntu), Unicode characters are not accepted.
* When the optimizer chooses a semi-join optimization for a subquery, the LooseScan and FirstMatch strategies are not considered for certain queries where they would be appropriate, and they are considered for certain queries where they would be inappropriate.
* When `FULLTEXT` search is performed on an InnoDB table, the results are incorrect when the search term contains an apostrophe (').
  * Starting with this release, when a search term contains an apostrophe ('), InnoDB tokenizes the word at the apostrophe, ignores the first token, and matches against the second token.
* After upgrading from old versions of MariaDB Server, some [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) operations fail if `ALGORITHM=NOCOPY` is specified.
  * In previous releases, the following error could be raised:

```
ERROR 1845 (0A000): ALGORITHM=NOCOPY is not supported for this operation. Try ALGORITHM=INPLACE
```

* When [optimizer\_switch='not\_null\_range\_scan=on'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_switch) is set, queries that use table elimination can produce incorrect results.
  * Table elimination is used when the query performs a JOIN and has `const` tables.
* When a replica server is replicating from a primary server that is too old to write [explicit\_defaults\_for\_timestamp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#explicit_defaults_for_timestamp) to the binary log, the replica server ignores its own value and assumes that the value should be OFF.
  * Starting with this release, the replica server determines an optimal value for [explicit\_defaults\_for\_timestamp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#explicit_defaults_for_timestamp) based on the version of the primary server. If the primary server is too old to write its value to the binary log, the replica server uses its own value.
* When a `UUID` or `INET6` column is referenced in a `WHERE col IN(SELECT ..)` subquery of an [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) or [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) statement, the query does not affect the correct number of rows.
* When a [BINARY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/binary) column is used to store UUIDs and a [SELECT statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) filters the column with an `IN` clause, the query can be very slow if the UUIDs are specified in hexadecimal.

## Changes in Storage Engines

* This release incorporates MariaDB ColumnStore storage engine version 5.6.7.

## Interface Changes

* [explicit\_defaults\_for\_timestamp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#explicit_defaults_for_timestamp) system variable dynamic changed from `No` to `Yes`
* `mariadb` --enable-cleartext-plugin command-line option added
* [mariadb-backup](../../10-5/broken-reference/) --sst-max-binlogs command-line option removed
* `mariadb-dump` [--max-statement-time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump#options) command-line option added
* `mariadbd` --spider-direct-aggregate command-line option added
* [spider\_direct\_aggregate](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) system variable added

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.5.17-12 is provided for:

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
