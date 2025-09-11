# Release Notes for MariaDB Enterprise Server 10.3.37-18

MariaDB Enterprise Server 10.3.37-18 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.3. This release includes a variety of fixes.

MariaDB Enterprise Server 10.3.37-18 was released on 2022-12-21.

## Notable Changes

* The [information\_schema.INNODB\_SYS\_TABLESPACES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tablespaces-table) view shows details about the InnoDB temporary tablespace, which is the tablespace where InnoDB temporary tables are stored. ([MDEV-29479](https://jira.mariadb.org/browse/MDEV-29479))
  * Starting with this release, the details about the InnoDB temporary tablespace can be shown by querying for the name innodb\_temporary:

```sql
SELECT * FROM information_schema.INNODB_SYS_TABLESPACES
 WHERE name LIKE 'innodb_temporary';
```

* When a table's default collation is set to the default collation for the table's character set, [SHOW CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-table) shows the `COLLATE` clause. ([MDEV-29446](https://jira.mariadb.org/browse/MDEV-29446))
  * In previous releases, MariaDB Enterprise Server reduced the size of `SHOW CREATE TABLE` output by excluding the `COLLATE` clause if the table's default collation was set to the default collation for the table's character set.

## Issues Fixed

### Can result in data loss

* When a column is renamed in a partitioned table with [ALTER TABLE .. RENAME COLUMN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) using the [NOCOPY algorithm](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-nocopy-alter-algorithm), the table can be corrupted. ([MDEV-28576](https://jira.mariadb.org/browse/MDEV-28576))
* When the InnoDB storage engine performs change buffer operations, the [InnoDB Redo Log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-redo-log) can overflow, which can cause table corruption. (MENT-1661, [MDEV-29905](https://jira.mariadb.org/browse/MDEV-29905))

### Can result in a hang or crash

* When a query contains an `IN/ALL/ANY` predicand and the subquery contains a `GROUP BY` clause with an `IN/ALL/ANY` predicand with a single-value subquery as the left operand, the server can crash. ([MDEV-29350](https://jira.mariadb.org/browse/MDEV-29350))
* If an InnoDB table contains a foreign key constraint and the child table's `DATABASE_NAME/TABLE_NAME.ibd` is longer than 330 characters, when the parent table is renamed, the server can crash. ([MDEV-29409](https://jira.mariadb.org/browse/MDEV-29409))
* When a DDL statement is executed using the [INPLACE algorithm](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-inplace-alter-algorithm) and [innodb\_adaptive\_hash\_index=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-system-variables#innodb_adaptive_hash_index) is set, the server can hang. ([MDEV-27700](https://jira.mariadb.org/browse/MDEV-27700), [MDEV-29384](https://jira.mariadb.org/browse/MDEV-29384))
* When renaming a table to a long name, the server can crash. ([MDEV-29258](https://jira.mariadb.org/browse/MDEV-29258))
* When an [ALTER TABLE statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) causes InnoDB to rebuild a table with a spatial index, the server can crash. ([MDEV-29520](https://jira.mariadb.org/browse/MDEV-29520))
* When an InnoDB temporary table contains a spatial index, the server can crash if the temporary table is dropped due to `DROP TEMPORARY TABLE` or client disconnect. ([MDEV-29507](https://jira.mariadb.org/browse/MDEV-29507))
* When querying a partitioned table using the `PARTITION` syntax, if the `WHERE` clause results in an index merge, the server can crash. ([MDEV-21134](https://jira.mariadb.org/browse/MDEV-21134))
* When detecting CTE dependencies of nested CTEs that includes one or more recursive CTEs, infinite recursion can occur until the server crashes. ([MDEV-29361](https://jira.mariadb.org/browse/MDEV-29361))
* When the [wsrep\_notify\_cmd system variable](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_notify_cmd) is configured to use the bundled `wsrep_notify.sh` script, the server can hang during startup. ([MDEV-27682](https://jira.mariadb.org/browse/MDEV-27682))
* When selecting from InnoDB's [information\_schema views](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema) (such as [INNODB\_TRX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables#INNODB_TRX), [INNODB\_LOCKS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables#INNODB_LOCKS), and [INNODB\_LOCK\_WAITS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables#INNODB_LOCK_WAITS)), if connections with open XA transactions are disconnected or killed at the same time, the server can crash. ([MDEV-29575](https://jira.mariadb.org/browse/MDEV-29575))
* For some queries that involve tables with different but convertible character sets for columns taking part in the query, a repeatable execution of such queries in the prepared statement mode or as part of a stored routine can crash the server. ([MDEV-16128](https://jira.mariadb.org/browse/MDEV-16128))
* When executing a `SELECT .. UNION .. SELECT or [EXPLAIN EXTENDED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain) statement, the server can crash. ([MDEV-23160](https://jira.mariadb.org/browse/MDEV-23160))`
* When [optimizer\_switch='condition\_pushdown\_for\_derived=on](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_switch)' is set and a view that includes a subquery is queried, the server crashes. ([MDEV-16549](https://jira.mariadb.org/browse/MDEV-16549))
* When the rolling upgrade procedure for MariaDB Enterprise Cluster (powered by Galera) is used to upgrade from ES 10.3 to ES 10.4, the joiner nodes can crash after the upgrade to ES 10.4. ([MDEV-29375](https://jira.mariadb.org/browse/MDEV-29375))
  * In previous releases, the MariaDB Error Log on the joiner node could contain the following error about the crash:

```
[Note] WSREP: 

####### Assign initial position for certification: 5c410a36-23a8-11ed-a44c-f6f37823dd10:3, protocol version: -1

[ERROR] WSREP: Corrupt buffer header: addr: 0x7f722bd5b530, seqno: 7019267256999739392, size: 825111097, ctx: 0x559652a28678, flags: 14391. store: 46, type: 49
[ERROR] mysqld got signal 6 ;
```

* When the global value of the [wsrep\_on system variable](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_on) is changed dynamically on a node that does not have MariaDB Enterprise Cluster (powered by Galera) configured, the server crashes when DDL is executed in TOI mode. ([MDEV-29706](https://jira.mariadb.org/browse/MDEV-29706))
  * In previous releases, the following statements could cause the crash on a node without Enterprise Cluster configured:

```sql
SET GLOBAL wsrep_on=ON;
CREATE TABLE t (c INT) ENGINE=InnoDB;
```

### Can result in unexpected behavior

* In the presence of replication filters, revoking privileges from a non-existing user on a primary (master) breaks replication on the replica (slave). ([MDEV-28530](https://jira.mariadb.org/browse/MDEV-28530))
* When [replicate\_wild\_ignore\_table='mysql.%'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is set on a replica node, the replica node does not skip replicated [SET DEFAULT ROLE statements](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/set-default-role). ([MDEV-28294](https://jira.mariadb.org/browse/MDEV-28294))
* When a Spider table has a prefix index, query results can be incorrect. ([MDEV-27172](https://jira.mariadb.org/browse/MDEV-27172))
* InnoDB can extend tablespace files when additional capacity is not required. ([MDEV-13013](https://jira.mariadb.org/browse/MDEV-13013))
* When an InnoDB table is being rebuilt and a [BLOB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/blob) is updated during the online rebuild, a memory leak can occur. ([MDEV-29600](https://jira.mariadb.org/browse/MDEV-29600))
* When a view is queried using a prepared statement, the query fails with the [ER\_NEED\_REPREPARE error code](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-1600-to-1699/e1615). ([MDEV-17124](https://jira.mariadb.org/browse/MDEV-17124))
  * In previous releases, the following error would occur:

```
ERROR 1615 (HY000): Prepared statement needs to be re-prepared
```

* When an InnoDB table contains virtual generated columns that are indexed, InnoDB fails to purge secondary index records. ([MDEV-29666](https://jira.mariadb.org/browse/MDEV-29666))
* When using the InnoDB adaptive hash index, non-locking reads can return wrong results due to a potential ACID violation. ([MDEV-28709](https://jira.mariadb.org/browse/MDEV-28709), [MDEV-29635](https://jira.mariadb.org/browse/MDEV-29635), [MDEV-27927](https://jira.mariadb.org/browse/MDEV-27927))
* When [SHOW COLUMNS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-columns) is used on a temporary table, an empty result set is returned. ([MDEV-28455](https://jira.mariadb.org/browse/MDEV-28455))
* When a sequence is used as the default value in a table, rows inserted by an `INSERT ... SELECT` statement can be assigned the wrong values. ([MDEV-29540](https://jira.mariadb.org/browse/MDEV-29540))
* When a column has both a [UNIQUE index](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-3/UNIQUE/README.md) and a [FULLTEXT index](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes/building-the-best-index-for-a-given-select#fulltext), full-text search using `MATCH(..) AGAINST(..)` does not work properly. ([MDEV-29778](https://jira.mariadb.org/browse/MDEV-29778))
* If the server is started with the [--ssl option](../../10-3/broken-reference/) enabled, but the TLS certificates and keys are not configured, the server will advertise the TLS support in the handshake, but will not actually be able to use it. ([MDEV-29811](https://jira.mariadb.org/browse/MDEV-29811))
* With MariaDB Enterprise Cluster, when [wsrep\_sst\_method='mariadb-backup'](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) is configured, the joiner node ignores custom values for the [innodb\_buffer\_pool\_filename system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_filename), and the SST copies the buffer pool file to the default location instead. ([MDEV-28968](https://jira.mariadb.org/browse/MDEV-28968))

### Related to install and upgrade

* When MyRocks is installed from a Debian package, the `rocksdb.cnf` configuration file gets installed to `/etc/mysql/mariadb.conf.d/` instead of `/etc/mysql/conf.d/.` ([MDEV-28605](https://jira.mariadb.org/browse/MDEV-28605))

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server-lifecycle.md), MariaDB Enterprise Server 10.3.37-18 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64, ARM64)
* Microsoft Windows (x86\_64) (MariaDB Enterprise Cluster excluded)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 18.04 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see ["MariaDB Corporation Engineering Policies"](https://mariadb.com/engineering-policies*).

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
