# Release Notes for MariaDB Enterprise Server 10.5.25-19

MariaDB Enterprise Server 10.5.25-19 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.5. This release includes a variety of fixes.

MariaDB Enterprise Server 10.5.25-19 was released on 2024-06-11.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/cve.org) link) | CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [CVE-2024-21096](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21096)                                                                                               | 4.9             |

## Notable Changes

* Galera has been updated to `26.4.18`
  * The GCS protocol version has been changed, preventing a downgrade of individual nodes of a MariaDB Enterprise Cluster

## Changes in Storage Engines

This release incorporates MariaDB ColumnStore engine version 5.6.8.

## Issues Fixed

### Can result in data loss

* With `--gtid-ignore-duplicate` set a transaction can be double-applied from another replication source if at applying the transaction from the initial source required retrying in parallel execution. ([MDEV-33475](https://jira.mariadb.org/browse/MDEV-33475))
* Backups of server with `innodb_encrypt_tables=1` can become corrupted in mariadb-backup `--prepare` ([MDEV-33334](https://jira.mariadb.org/browse/MDEV-33334))
* The TIMESTAMP value of `'1970-01-01 00:00:00'` can be inserted via a `INSERT ...FROM ... SELECT` in strict mode although it should result in an error ([MDEV-34088](https://jira.mariadb.org/browse/MDEV-34088))
* Galera-replicated events can in some cases contain the wrong time when versioning is used ([MDEV-18590](https://jira.mariadb.org/browse/MDEV-18590))
* wrong row targeted with `"insert ... on duplicate"` and `"replace"`, leading to data corruption ([MDEV-30046](https://jira.mariadb.org/browse/MDEV-30046))

### Can result in hang or crash

* Using current MariaDB Enterprise Backup against an older server can result in a crash, as the system variable `@@aria_log_dir_path` does not exist ([MDEV-31251](https://jira.mariadb.org/browse/MDEV-31251))
* When using a non-default setting for `"innodb_change_buffering"`, the server can crash ([MDEV-33332](https://jira.mariadb.org/browse/MDEV-33332))
* When a fulltext search query with more than 4G inserted or updated rows is executed, the server can crash ([MDEV-33383](https://jira.mariadb.org/browse/MDEV-33383))
* For encrypted table spaces an ALTER operation can hang when an encryption thread works on the same tablespace ([MDEV-33770](https://jira.mariadb.org/browse/MDEV-33770))
* `EXPLAIN` statement that uses a subquery which has a query plan that A) will examine less than `@@expensive_subquery_limit` rows and B) will use join buffer could cause a crash. ([MDEV-21102](https://jira.mariadb.org/browse/MDEV-21102))
* For a `SPIDER` table, when deleting partitions from a table, the server can crash ([MDEV-33731](https://jira.mariadb.org/browse/MDEV-33731))
* When replaying a binary log with mariadb-binlog, the tool can crash if the binary log includes statements related to sequences, like `SELECT NEXTVAL(s)` ([MDEV-31779](https://jira.mariadb.org/browse/MDEV-31779))
* MariaDB Enterprise Backup fails with the following error message if the prepare step of the backup encounters a data directory which happens to store wsrep xid position in TRX SYS page: ([MDEV-33540](https://jira.mariadb.org/browse/MDEV-33540))

```
InnoDB: Crash recovery is broken due to insufficient innodb_log_file_size
```

* Assertion when user commits an empty transaction for DDL that was killed during certification: ([MDEV-32787](https://jira.mariadb.org/browse/MDEV-32787))

```
!wsrep_has_changes(thd) || (thd->lex->sql_command == SQLCOM_CREATE_TABLE && !thd->is_current_stmt_binlog_format_row()) || thd->wsrep_cs().transaction().state() == wsrep::transaction::s_aborted
```

* Graceful node shutdown can crash garbd and MariaDB Enterprise Cluster can go non-primary when SSL is used ([MDEV-33495](https://jira.mariadb.org/browse/MDEV-33495))

### Can result in unexpected behavior

* Wrong result sets are returned by the second execution of prepared statements from selects using mergeable derived tables pushed into external engine ([MDEV-31361](https://jira.mariadb.org/browse/MDEV-31361))
* A query that uses a derived table that employs constructs with side-effects, like `(SELECT @var:=... )` as derived\_tbl, could produce wrong results ([MDEV-30975](https://jira.mariadb.org/browse/MDEV-30975))
* `ORDER BY COLLATE` improperly applied to non-character columns which is resulting in an unordered result set ([MDEV-33318](https://jira.mariadb.org/browse/MDEV-33318))
* Spider/ODBC passed double quotes for names, in ANSI style (MENT-958)
* Default charset doesn't work with PHP MySQLi extension ([MDEV-32975](https://jira.mariadb.org/browse/MDEV-32975))
* Bad `SEPARATOR` value in `GROUP_CONCAT` on character set conversion can lead to a wrong result ([MDEV-33772](https://jira.mariadb.org/browse/MDEV-33772))
* Spider returns parsing failure on valid left join select by translating the on expression to () ([MDEV-33679](https://jira.mariadb.org/browse/MDEV-33679))
* When creating a temporary InnoDB table with `CREATE TEMPORARY TABLE ... AS SELECT ...` from an InnoDB table as a non SUPER / READ ONLY ADMIN user, the following error is shown instead of creating the table: ([MDEV-33889](https://jira.mariadb.org/browse/MDEV-33889))

```
ERROR 1290 (HY000): The MariaDB server is running with the --read-only option so it cannot execute this statement
```

* `CREATE TEMPORARY TABLE (without SELECT), INSERT ... SELECT, and CREATE ... LIKE` are not affected by this bug
* A view created via `JSON_ARRAYAGG` returns an incorrect JSON object ([MDEV-30646](https://jira.mariadb.org/browse/MDEV-30646))
* Mariadb-dump trusts the server and does not validate the data. A modified dump file can include system commands used by the mariadb-client. Dumps are now loaded in the sandbox mode by default, a system call will result in an error ([MDEV-33727](https://jira.mariadb.org/browse/MDEV-33727))
* Updating a case insensitive large unique key with an insensitive change of the value can result in a duplicate key error ([MDEV-29345](https://jira.mariadb.org/browse/MDEV-29345))
* When setting `binlog_annotate_row_events=1`, an event of binlog file can be truncated ([MDEV-9179](https://jira.mariadb.org/browse/MDEV-9179))
* Wrong result with semi-join and split-table derived table from queries with an `IN` subquery predicate in the `WHERE` clause and a derived table in the `FROM` clause to which split materialized optimization could be applied. ([MDEV-23878](https://jira.mariadb.org/browse/MDEV-23878))
* With galera, correct transactions could not be committed with the following error when accessing system tables for read, and write to innodb tables in the same transaction: ([MDEV-33828](https://jira.mariadb.org/browse/MDEV-33828))

```
Transactional commit not supported by involved engine
```

* A wrong result on 2-nd execution of a prepared statement is possible when selecting from a view using a merged derived table ([MDEV-31277](https://jira.mariadb.org/browse/MDEV-31277))
* Original IP not shown in network related error messages when proxy\_protocol is in use ([MDEV-33506](https://jira.mariadb.org/browse/MDEV-33506))
* Incorrect `DEFAULT` expression evaluated in `UPDATE` ([MDEV-33790](https://jira.mariadb.org/browse/MDEV-33790))
* group by optimization incorrectly removing subquery where subject buried in a function ([MDEV-28621](https://jira.mariadb.org/browse/MDEV-28621))

### Related to performance

* Table is getting rebuild with `ALTER TABLE ADD COLUMN` although it should be an instant operation not requiring a rebuild ([MDEV-33214](https://jira.mariadb.org/browse/MDEV-33214))
* Aggregation functions fail to leverage uniqueness property ([MDEV-30660](https://jira.mariadb.org/browse/MDEV-30660))
  * Generally, computing aggregate function with DISTINCT argument: `aggregate_func(DISTINCT col1, col2, ...)` requires producing a de-duplicated set of its arguments, which can be CPU-intensive
  * When we select from one table the argument list includes the table's PRIMARY (or UNIQUE) key:

```
SELECT aggregate_func(DISTINCT t1.primary_key, ...) FROM t1;
```

then the arguments are guaranteed not to have duplicates. Such cases are now detected allowing the optimizer to skip de-duplication.

## Changelog

For the complete list of changes in this release, see the [changelog](changelog-for-mariadb-enterprise-server-10-5-25-19.md).

## Platforms

*   In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.5.26-20 is provided for:

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
