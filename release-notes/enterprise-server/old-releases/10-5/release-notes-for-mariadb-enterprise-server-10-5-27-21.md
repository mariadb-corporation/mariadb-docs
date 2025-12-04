# Release Notes for MariaDB Enterprise Server 10.5.27-21

MariaDB Enterprise Server 10.5.27-21 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-enterprise-server/README.md) 10.5. This release includes a variety of fixes.

MariaDB Enterprise Server 10.5.27-21 was released on 2024-12-10.

## Notable Changes

* A new parameter `--quick-max-column-width` is now available in the mariadb client to limit the field width when used with the `--quick` mode ([MDEV-34704](https://jira.mariadb.org/browse/MDEV-34704))

## Changes in Storage Engines

* This release incorporates MariaDB ColumnStore engine version 5.6.8

## Issues Fixed

### Can result in data loss

* Using `group_concat` with a compressed or GIS column can lead to a server crash and potential data corruption for users performing `group_concat` operations on tables containing these data types ([MDEV-16699](https://jira.mariadb.org/browse/MDEV-16699))

### Can result in hang or crash

* A query could cause a crash if it has a HAVING clause with a construct tblX.column=column\_or\_constant and the optimizer was able to infer that table tblX is a constant table. Note that HAVING clause may be from the original query or may come from [Condition Pushdown optimization](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimizations-for-derived-tables/condition-pushdown-into-derived-table-optimization)) ([MDEV-23983](https://jira.mariadb.org/browse/MDEV-23983))
* Calling a UDF for the engine SPIDER results in a crash if the SPIDER storage engine plugin could not be loaded ([MDEV-34682](https://jira.mariadb.org/browse/MDEV-34682))
* Under Windows Subsystem for Linux, InnoDB crashes on ALTER TABLE or OPTIMIZE TABLE ([MDEV-34938](https://jira.mariadb.org/browse/MDEV-34938))
* Server crashes when setting `wsrep_cluster_address` after adding invalid value to `wsrep_allowlist` table ([MDEV-31173](https://jira.mariadb.org/browse/MDEV-31173))
* mariadbd hangs on startup when `--init-file` target does not exist ([MDEV-34814](https://jira.mariadb.org/browse/MDEV-34814))
* Possible server crash in cases where the function `DEFAULT()` is part of a query ([MDEV-35276](https://jira.mariadb.org/browse/MDEV-35276))
* Possible unique hash index corruption for system-versioned tables after DML including DELETE HISTORY statement. This can lead to data corruption, crashes, and incorrect query results ([MDEV-33470](https://jira.mariadb.org/browse/MDEV-33470))
  * Possible error log entry

```
[ERROR] InnoDB: Record in index `c` of table `test`.`t` was not found on update...
```

* In some situations, where a MariaDB Enterprise cluster (Galera) node crashes, some threads are still working. This is visible via the error log, which is still getting errors written by the node. As the node stops interacting correctly with other cluster nodes and is blocking them from taking over the primary state, the whole cluster hangs ([MDEV-32363](https://jira.mariadb.org/browse/MDEV-32363))

### Can result in unexpected behavior

* When a user runs mariadb-binlog with `--stop-position`, they would expect the output to contain events up to that event. If the output did not contain events up to that event, this may result in various unexpected behaviors, e.g., an incomplete database state if they piped the output to the mariadb client and expected certain transactions to have executed in the database, yet never were run ([MDEV-27037](https://jira.mariadb.org/browse/MDEV-27037))
* Changing a data type of a field used in a foreign key constraint fails with Error "Cannot change column '...': used in a foreign key constraint '...'" ([MDEV-34392](https://jira.mariadb.org/browse/MDEV-34392))
  * This ALTER only fails if the type of field is changed in a multi-ALTER statement, where types of other fields are changed with the ALTER
* Creation of a view with UNION and SELECT ... FOR UPDATE in the definition fails with error "ER\_PARSE\_ERROR (1064): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near..." ([MDEV-29537](https://jira.mariadb.org/browse/MDEV-29537))
* INSERT...SELECT on MyISAM or ARIA tables are replicated by MariaDB Enterprise Cluster (Galera) ([MDEV-34647](https://jira.mariadb.org/browse/MDEV-34647))
* SELECT MIN on Spider table returns more rows than expected ([MDEV-26345](https://jira.mariadb.org/browse/MDEV-26345))
* Can't selectively restore sequences using innodb tables from backup ([MDEV-32350](https://jira.mariadb.org/browse/MDEV-32350))
* LOAD DATA INFILE with geometry data fails ([MDEV-34883](https://jira.mariadb.org/browse/MDEV-34883))
* Executing an UPDATE statement in prepared statement mode having positional parameter bound with an array can result in an incorrect number of updated rows in case there is a BEFORE UPDATE trigger that executes yet another UPDATE statement to change a table ([MDEV-34718](https://jira.mariadb.org/browse/MDEV-34718))
* Recovery fails to note some log corruption, resulting in "log sequence number in the future" error messages, and possibly adds more corruption ([MDEV-34802](https://jira.mariadb.org/browse/MDEV-34802))
  * When log corruption is noted, the server can now only be started when using the option `innodb_force_recovery`
* Unexpected error "Row size too large (> 8123)..." for a correct INSERT after a instantly dropped BLOB column ([MDEV-35122](https://jira.mariadb.org/browse/MDEV-35122))
* Wrong binlog timestamps on secondary nodes of MariaDB Enterprise Cluster (MENT-2164)
* When the MariaDB Enterprise Audit Plugin is configured to log ACL queries, a statement CREATE USER .. IDENTIFIED VIA ed25519 USING PASSWORD(...) is logged including the password (MENT-2181)
* When the MariaDB Enterprise Audit Plugin is configured to log ACL queries, passwords are masked for CREATE USER .. IDENTIFIED BY, but not for CREATE OR REPLACE USER, or SET STATEMENT ... FOR CREATE USER (MENT-2188)

### Related to performance

* Unnecessary copying of log records by MariaDB Enterprise Backup when further transaction commits are blocked by BACKUP STAGE BLOCK\_COMMIT (MENT-2133)
  * It also would cause further effort of rolling back incomplete transactions after the backup is restored
* Aria internal temporary tables unnecessarily write all changed blocks to disk when the table is closed at end of query (MENT-2182)

## Changelog

For the complete list of changes in this release, see the [changelog](changelog-for-mariadb-enterprise-server-10-5-27-21.md).

## Platforms

In alignment to the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.5.27-21 is provided for:

* AlmaLinux 8 (x86\_64, ARM64)
* AlmaLinux 9 (x86\_64, ARM64)
* Debian 11 (x86\_64, ARM64)
* Microsoft Windows (x86\_64) (MariaDB Enterprise Cluster excluded)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see "[MariaDB Corporation Engineering Policies](https://mariadb.com/engineering-policies)".

## nstallation Instructions

* [MariaDB Enterprise Server ](../../11.4/whats-new.md)[10](broken-reference)[.5](../../11.4/whats-new.md)
* [Enterprise Cluster Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[10](broken-reference)[.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)
* [ColumnStore Object Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage) [and MariaDB Enterprise ColumnStore 23.02](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)[ and MariaDB Enterprise ColumnStore 23.02](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)
* [HTAP Topology with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)[ and MariaDB Enterprise ColumnStore 23.02](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)
* [Single-Node Enterprise ColumnStore 23.02 with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)[and Object Storage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)
* [Single-Node Enterprise ColumnStore 23.02 with MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server 10.5](broken-reference)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server 10.5](broken-reference)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-from-mariadb-10-5-to-mariadb-10-6)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
