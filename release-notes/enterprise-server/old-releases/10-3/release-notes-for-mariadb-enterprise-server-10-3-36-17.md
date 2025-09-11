# Release Notes for MariaDB Enterprise Server 10.3.36-17

MariaDB Enterprise Server 10.3.36-17 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.3. This release includes a variety of fixes.

MariaDB Enterprise Server 10.3.36-17 was released on 2022-09-12.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-3/cve.org) link) | CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [CVE-2018-25032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-25032)                                                                                               | 7.5             |
| [CVE-2022-32091](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32091)                                                                                               | 6.5             |
| [CVE-2022-32084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32084)                                                                                               | 6.5             |

## Notable Changes

* Debian 9 support has been discontinued.
* The [--max-statement-time command-line option](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump#options) has been added for [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) with a default value of `0`. ([MDEV-18702](https://jira.mariadb.org/browse/MDEV-18702))

## Issues Fixed

### Can result in data loss

* When [mariadb-backup](../../10-3/broken-reference/) is executed with the [--rsync command-line option](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md), the backup tries to copy the InnoDB buffer pool dump file, which is located at the path defined by the [innodb\_buffer\_pool\_filename system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_filename). ([MDEV-28781](https://jira.mariadb.org/browse/MDEV-28781))
  * Starting with this release, [mariadb-backup](../../10-3/broken-reference/) only copies the InnoDB buffer pool dump file during State Snapshot Transfers (SSTs) for MariaDB Enterprise Cluster, powered by Galera.
* When [ALTER TABLE .. IMPORT TABLESPACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) is executed against an encrypted InnoDB tablespace file, the table can be corrupted. ([MDEV-28779](https://jira.mariadb.org/browse/MDEV-28779))

### Can result in a hang or crash

* When `INSERT .. SELECT .. GROUP BY` is executed and the `GROUP BY` clause contains a derived table, the server can crash. ([MDEV-28617](https://jira.mariadb.org/browse/MDEV-28617))
* When a query contains an `ANY(SELECT .. GROUP BY(SELECT ..))` predicand with a redundant subquery in the GROUP BY clause, the server can crash. ([MDEV-29139](https://jira.mariadb.org/browse/MDEV-29139))
* When [ALTER TABLE .. ADD](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) is used to add a column with the `INSTANT` algorithm, the server can crash if the `ROW_FORMAT` in the `.frm` file does not match the actual row format used by the data file. ([MDEV-26577](https://jira.mariadb.org/browse/MDEV-26577))
  * For tables created prior to MariaDB Server 10.2, the `ROW_FORMAT` in the `.frm` file could be inconsistent with the actual row format used by the data file. If the server were upgraded to MariaDB Enterprise Server 10.6, the inconsistency could remain.
* When `INSERT .. SELECT` is executed and the SELECT query calls an aggregate or window function, the server can crash with a segmentation fault. ([MDEV-26427](https://jira.mariadb.org/browse/MDEV-26427))
* When the [JSON\_EXTRACT() function](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_extract) is called, the server can crash with a segmentation fault. ([MDEV-29188](https://jira.mariadb.org/browse/MDEV-29188))
* When a query uses the `DISTINCT` keyword and calls an aggregate function as an argument for an always-constant function, the server can crash. ([MDEV-23809](https://jira.mariadb.org/browse/MDEV-23809))
  * An always-constant function is a function that always returns a constant value, even if the function's arguments are not constant.
  * For example, the [COLLATION() function](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/collation) is an always-constant function.
* When [mariadb-backup](../../10-3/broken-reference/) is executed with the [--compress](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md) and [--parallel](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md) options, the backup can hang due to a race condition between threads. ([MDEV-29043](https://jira.mariadb.org/browse/MDEV-29043))
* When an `EXISTS` predicate or an `IN`, `ALL`, or `ANY` predicand is used in an eliminated `GROUP BY` clause, the server can crash. (MENT-1606, [MDEV-29350](https://jira.mariadb.org/browse/MDEV-29350))

### Can result in unexpected behavior

* For multi-table \[UPDATE|\[`UPDATE`]] or [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) queries, the optimizer fails to apply partition pruning optimization for the table that is updated or deleted from. ([MDEV-28246](https://jira.mariadb.org/browse/MDEV-28246))
* When an `IN` condition contains a mixture of numeric and string values, results can be inconsistent. ([MDEV-21445](https://jira.mariadb.org/browse/MDEV-21445))
* When a sequence event is written to the binary log with [binlog\_format=ROW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#binlog_format), the value of [binlog\_row\_image](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#binlog_row_image) is not respected. ([MDEV-28487](https://jira.mariadb.org/browse/MDEV-28487))
* When a transaction can't be fully written to the binary log, but the transaction can be safely rolled back, a `LOST_EVENTS` incident event is written to the binary log. ([MDEV-21443](https://jira.mariadb.org/browse/MDEV-21443))
  * In previous releases, this problem could cause replica servers to encounter the following error:

```
Last_SQL_Errno	1590
Last_SQL_Error	The incident LOST_EVENTS occurred on the master. Message: error writing to the binary log
```

* Starting with this release, a `LOST_EVENTS` incident is only written to the binary log when safe rollback is not possible.
* When a replica server replicates an incident event, the details about the failure are not in the primary server's error log, the replica server's error log, or the output of [SHOW REPLICA STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status). ([MDEV-21087](https://jira.mariadb.org/browse/MDEV-21087))
* When a backup is performed with [mariadb-backup](../../10-3/broken-reference/), the backup includes binary logs. ([MDEV-28758](https://jira.mariadb.org/browse/MDEV-28758))
* When a table is created from a [SELECT statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) that uses a recursive CTE, the table can use unexpected data types and contain truncated data if the calculated values from the recursive part of the CTE do not fit in the column types that are taken from the non-recursive part of the CTE. ([MDEV-12325](https://jira.mariadb.org/browse/MDEV-12325))
  * Starting with this release, the CTE calculation is aborted when the calculated values do not fit in the column types. When this occurs, a warning or error (depending on [sql\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql-mode) is raised with the [ER\_WARN\_DATA\_OUT\_OF\_RANGE error code](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-3/broken-reference/README.md) and the following error message:

```
Out of range value for column 'COLUMN_NAME' at row ROW_NUM
```

* When [mariadb client](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb/README.md) uses `EditLine` instead of `readline` (such as on Debian and Ubuntu), Unicode characters are not accepted. ([MDEV-28197](https://jira.mariadb.org/browse/MDEV-28197))
* When the optimizer chooses a semi-join optimization for a subquery, the LooseScan and FirstMatch strategies are not considered for certain queries where they would be appropriate, and they are considered for certain queries where they would be inappropriate. ([MDEV-28749](https://jira.mariadb.org/browse/MDEV-28749))
* When `FULLTEXT` search is performed on an InnoDB table, the results are incorrect when the search term contains an apostrophe ('). ([MDEV-20797](https://jira.mariadb.org/browse/MDEV-20797))
  * Starting with this release, when a search term contains an apostrophe ('), InnoDB tokenizes the word at the apostrophe, ignores the first token, and matches against the second token.

## Interface Changes

* mariadb-backup [--sst-max-binlogs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog/mariadb-binlog-options) command-line option removed
* mysql [--enable-cleartext-plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam#pam_use_cleartext_plugin) command-line option added
* mysqldump [--max-statement-time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump#options) command-line option added

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server-lifecycle.md), MariaDB Enterprise Server 10.3.36-17 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64, ARM64)
* Microsoft Windows (x86\_64)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 18.04 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies/)".

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
