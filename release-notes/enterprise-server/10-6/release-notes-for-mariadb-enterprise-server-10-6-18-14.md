# Release Notes for MariaDB Enterprise Server 10.6.18-14

MariaDB Enterprise Server 10.6.18-14 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-enterprise-server/README.md) 10.6.

MariaDB Enterprise Server 10.6.18-14 was released on 2024-06-11.

## Fixed Security Vulnerabilities

| CVE (with [cve.org](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-6/cve.org) link) | CVSS base score |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [CVE-2024-21096](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21096)                                                                                               | 4.9             |

## Notable Changes

* Galera has been updated to `26.4.18`
  * The GCS protocol version has been changed, preventing a downgrade of individual nodes of a MariaDB Enterprise Cluster
* Changes to the use of the variable `optimizer_adjust_secondary_index_costs` ([MDEV-33306](https://jira.mariadb.org/browse/MDEV-33306))
  * The default of the variable `optimizer_adjust_secondary_index_costs` changed from "0" to "" and is now of type `ENUM`
  * The variable can now be set to a combination of the following values separated by a ',':
    * `adjust_secondary_key_cost`: Update secondary key costs for ranges to be at least 5x of clustered primary key costs.
    * `disable_max_seek`: Disable 'max\_seek optimization' for secondary keys and slight adjustment of filter cost.
    * `disable_forced_index_in_group_by`: Disable automatic forced index in `GROUP BY` and make `GROUP BY` cost based instead of rule based. ALL Sets all of the above values.
  * Without changes in configuration or using the old integer values `0, 1, 2` for `optimizer_adjust_secondary_key_costs` this system variable works as before. This is to ensure that we do not break any existing applications.

## Changes in Storage Engines

* This release originally incorporated MariaDB ColumnStore engine version 23.10.1.
* This release now incorporates MariaDB ColumnStore engine version 23.10.2.

## Issues Fixed

### Can result in data loss

* With `--gtid-ignore-duplicate` set a transaction can be double-applied from another replication source if at applying the transaction from the initial source required retrying in parallel execution. ([MDEV-33475](https://jira.mariadb.org/browse/MDEV-33475))
* Backups of server with `innodb_encrypt_tables=1` can become corrupted in `mariadb-backup --prepare` ([MDEV-33334](https://jira.mariadb.org/browse/MDEV-33334))
* With multiple GTID domains, optimistic parallel slave conflicts involving XA-PREPARE event group could not be resolved correctly which might cause unnecessary stop of the slave serve. ([MDEV-34042](https://jira.mariadb.org/browse/MDEV-34042))
* The `TIMESTAMP` value of `'1970-01-01 00:00:00'` can be inserted via a `INSERT ...FROM ... SELECT` in strict mode although it should result in an error ([MDEV-34088](https://jira.mariadb.org/browse/MDEV-34088))
* Galera-replicated events can in some cases contain the wrong time when versioning is used ([MDEV-18590](https://jira.mariadb.org/browse/MDEV-18590))
* wrong row targeted with `insert ... on duplicate` and `replace`, leading to data corruption ([MDEV-30046](https://jira.mariadb.org/browse/MDEV-30046))

## Can result in hang or crash

* Using current MariaDB Enterprise Backup against an older server can result in a crash, as the system variable `@@aria_log_dir_path` does not exist ([MDEV-31251](https://jira.mariadb.org/browse/MDEV-31251))
* When using a non-default setting for `innodb_change_buffering`, the server can crash ([MDEV-33332](https://jira.mariadb.org/browse/MDEV-33332))
* When a fulltext search query with more than 4G inserted or updated rows is executed, the server can crash ([MDEV-33383](https://jira.mariadb.org/browse/MDEV-33383))
* InnoDB is holding shared `dict_sys.latch` while waiting for `FOREIGN KEY` child table lock on DDL ([MDEV-32899](https://jira.mariadb.org/browse/MDEV-32899))
* InnoDB may hang when temporarily running out of buffer pool ([MDEV-33613](https://jira.mariadb.org/browse/MDEV-33613))
* For encrypted table spaces an `ALTER` operation can hang when an encryption thread works on the same tablespace ([MDEV-33770](https://jira.mariadb.org/browse/MDEV-33770))
* `EXPLAIN` statement that uses a subquery which has a query plan that A) will examine less than `@@expensive_subquery_limit` rows and B) will use join buffer could cause a crash. ([MDEV-21102](https://jira.mariadb.org/browse/MDEV-21102))
* For a SPIDER table, when deleting partitions from a table, the server can crash ([MDEV-33731](https://jira.mariadb.org/browse/MDEV-33731))
* After an unsuccessful ALTER TABLE on an ARIA table due to a full temp space, any subsequent query results in the following error if it involves using temp: ([MDEV-33813](https://jira.mariadb.org/browse/MDEV-33813))

```
ERROR 1021 (HY000): Disk full (./org/test1.MAI); waiting for someone to free some space... (errno: 28 "No space left on device")
```

* When replaying a binary log with mariadb-binlog, the tool can crash if the binary log includes statements related to sequences, like `SELECT NEXTVAL(s)` ([MDEV-31779](https://jira.mariadb.org/browse/MDEV-31779))
* MariaDB Enterprise Backup fails with the following error message if the prepare step of the backup encounters a data directory which happens to store wsrep xid position in TRX SYS page: ([MDEV-33540](https://jira.mariadb.org/browse/MDEV-33540))

```
InnoDB: Crash recovery is broken due to insufficient innodb_log_file_size
```

* Assertion failure when a client disconnected during transaction that is in the XA PREPARE state or when incomplete transaction was recovered from undo logs on server startup and not yet rolled back ([MDEV-33278](https://jira.mariadb.org/browse/MDEV-33278))
* Failure with the following error message when streaming transaction in idle state is BF aborted: ([MDEV-33509](https://jira.mariadb.org/browse/MDEV-33509))

```
WSREP: Failed to apply write set with flags = (rollback | pa_unsafe)
```

* Assertion when user commits an empty transaction for DDL that was killed during certification: ([MDEV-32787](https://jira.mariadb.org/browse/MDEV-32787))

```
!wsrep_has_changes(thd) || (thd->lex->sql_command == SQLCOM_CREATE_TABLE && !thd->is_current_stmt_binlog_format_row()) || thd->wsrep_cs().transaction().state() == wsrep::transaction::s_aborted
```

* MDL lock conflict can occur if the transactions acquire explicit MDL locks from the InnoDB level when persistent statistics is re-read for a table and such a transaction is subject to BF-abort ([MDEV-33136](https://jira.mariadb.org/browse/MDEV-33136))
* Graceful node shutdown can crash garbd and MariaDB Enterprise Cluster can go non-primary when SSL is used ([MDEV-33495](https://jira.mariadb.org/browse/MDEV-33495))

### Can result in unexpected behavior

* Wrong result sets are returned by the second execution of prepared statements from selects using mergeable derived tables pushed into external engine ([MDEV-31361](https://jira.mariadb.org/browse/MDEV-31361))
* `IMPORT TABLESPACE` fails with column count or index count mismatch: ([MDEV-30655](https://jira.mariadb.org/browse/MDEV-30655))

```
ERROR 1808 (HY000): Schema mismatch (Number of columns don't match, table has x columns but the tablespace meta-data file has y columns)
```

* A query that uses a derived table that employs constructs with side-effects, like `(SELECT @var:=... ) as derived_tbl`, could produce wrong results ([MDEV-30975](https://jira.mariadb.org/browse/MDEV-30975))
* `ORDER BY COLLATE` improperly applied to non-character columns which is resulting in an unordered result set ([MDEV-33318](https://jira.mariadb.org/browse/MDEV-33318))
* Inconsistent behaviors of UPDATE under Read Uncommitted & Read Committed isolation level ([MDEV-26643](https://jira.mariadb.org/browse/MDEV-26643))
* When two transactions modify the data at the same time with isolation level REPEATABLE-READ, the latter transaction does take the change from the first transaction into account ([MDEV-26642](https://jira.mariadb.org/browse/MDEV-26642))
* Spider/ODBC passed double quotes for names, in ANSI style (MENT-958)
* Default charset doesn't work with PHP MySQLi extension ([MDEV-32975](https://jira.mariadb.org/browse/MDEV-32975))
* Bad `SEPARATOR` value in `GROUP_CONCAT` on character set conversion can lead to a wrong result ([MDEV-33772](https://jira.mariadb.org/browse/MDEV-33772))
* Spider returns parsing failure on valid left join select by translating the on expression to `()` ([MDEV-33679](https://jira.mariadb.org/browse/MDEV-33679))
* When creating a temporary InnoDB table with `CREATE TEMPORARY TABLE ... AS SELECT ...` from an InnoDB table as a non SUPER / READ ONLY ADMIN user, the following error is shown instead of creating the table: ([MDEV-33889](https://jira.mariadb.org/browse/MDEV-33889))

```
ERROR 1290 (HY000): The MariaDB server is running with the --read-only option so it cannot execute this statement
```

* `CREATE TEMPORARY TABLE (without SELECT), INSERT ... SELECT, and CREATE ... LIKE` are not affected by this bug
* Phantom rows caused by `UPDATE` of `PRIMARY KEY` ([MDEV-32898](https://jira.mariadb.org/browse/MDEV-32898))
* Mariadb-dump trusts the server and does not validate the data. A modified dump file can include system commands used by the mariadb-client. Dumps are now loaded in the sandbox mode by default, a system call will result in an error ([MDEV-33727](https://jira.mariadb.org/browse/MDEV-33727))
* Updating a case insensitive large unique key with an insensitive change of the value can result in a duplicate key error ([MDEV-29345](https://jira.mariadb.org/browse/MDEV-29345))
* When setting `binlog_annotate_row_events=1`, an event of binlog file can be truncated ([MDEV-9179](https://jira.mariadb.org/browse/MDEV-9179))
* Wrong result with semi-join and split-table derived table from queries with an IN subquery predicate in the `WHERE` clause and a derived table in the `FROM` clause to which split materialized optimization could be applied. ([MDEV-23878](https://jira.mariadb.org/browse/MDEV-23878))
* With galera, correct transactions could not be committed with the following error when accessing system tables for read, and write to innodb tables in the same transaction: ([MDEV-33828](https://jira.mariadb.org/browse/MDEV-33828))

```
Transactional commit not supported by involved engine
```

* A wrong result on 2-nd execution of a prepared statement is possible when selecting from a view using a merged derived table ([MDEV-31277](https://jira.mariadb.org/browse/MDEV-31277))
* Original IP not shown in network related error messages when proxy\_protocol is in use ([MDEV-33506](https://jira.mariadb.org/browse/MDEV-33506))
* Incorrect `DEFAULT` expression evaluated in UPDATE ([MDEV-33790](https://jira.mariadb.org/browse/MDEV-33790))
* group by optimization incorrectly removing subquery where subject buried in a function ([MDEV-28621](https://jira.mariadb.org/browse/MDEV-28621))

### Related to performance

* Replication with XA events can show decreased performance. Adapt parallel slave's round-robin scheduling to XA events ([MDEV-33668](https://jira.mariadb.org/browse/MDEV-33668))
* Row locks for non-modified rows are not released at `XA PREPARE` ([MDEV-33454](https://jira.mariadb.org/browse/MDEV-33454))
* Optimizer is sometimes choosing an index for queries with `GROUP BY` when it shouldn't, resulting in decreased performance. To protect compatibility to the current behavior `@@optimizer_adjust_secondary_key_costs="disable_forced_index_in_group_by"` has to be set to enable the fix ([MDEV-33306](https://jira.mariadb.org/browse/MDEV-33306))
* Table is getting rebuild with `ALTER TABLE ADD COLUMN` although it should be an instant operation not requiring a rebuild ([MDEV-33214](https://jira.mariadb.org/browse/MDEV-33214))
* Semi-sync Wait Point `AFTER_COMMIT` Slow on Workloads with Heavy Concurrency ([MDEV-33551](https://jira.mariadb.org/browse/MDEV-33551))
* Aggregation functions fail to leverage uniqueness property ([MDEV-30660](https://jira.mariadb.org/browse/MDEV-30660))
  * Generally, computing aggregate function with DISTINCT argument: `aggregate_func(DISTINCT col1, col2, ...)` requires producing a de-duplicated set of its arguments, which can be CPU-intensive
  * When we select from one table the argument list includes the table's PRIMARY (or UNIQUE) key:

```
SELECT aggregate_func(DISTINCT t1.primary_key, ...) FROM t1;
```

then the arguments are guaranteed not to have duplicates. Such cases are now detected allowing the optimizer to skip de-duplication.

## Changelog

For the complete list of changes in this release, see the [changelog](changelog-for-mariadb-enterprise-server-10-6-18-14.md).

## Platforms

In alignment to the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.6.18-14 is provided for:

* AlmaLinux 8 (x86\_64, ARM64)
* AlmaLinux 9 (x86\_64, ARM64)
* CentOS 7 (x86\_64)
* Debian 10 (x86\_64)
* Debian 11 (x86\_64, ARM64)
* Debian 12 (x86\_64, ARM64)
* Microsoft Windows (x86\_64) (MariaDB Enterprise Cluster excluded)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, ARM64, PPC64LE)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)
* Ubuntu 22.04 (x86\_64, ARM64)

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see [MariaDB Corporation Engineering Policies".](https://mariadb.com/engineering-policies)

### Installation Instructions

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

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
