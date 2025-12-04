# Release Notes for MariaDB Enterprise Server 10.4.33-23

MariaDB Enterprise Server 10.4.33-23 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.4. This release includes a variety of fixes.

MariaDB Enterprise Server 10.4.33-23 was released on 2024-03-11.

## Notable Changes

* Galera has been updated to `26.4.17`

## Issues Fixed

### Can result in data loss

* `BLO`B corruption on `UPDATE` of `PRIMARY KEY` with `FOREIGN KEY` ([MDEV-31441](https://jira.mariadb.org/browse/MDEV-31441))
* Corrupted table after instant `ADD COLUMN` failed due to attempting to exceed the maximum record length ([MDEV-18322](https://jira.mariadb.org/browse/MDEV-18322))
* ALTER command, before entering TOI, tries to collect foreign keys of a table. For this it opens the main table with SHARED\_HIGH\_PRIO MDL lock which disregards any waiting queued lock requests. If there is a DML operation running on the same table, and a real TOI operation as well, this TOI operation tries to BF-abort DML operation. At the same time, because ALTER is not yet TOI, and it runs with HIGH\_PRIO MDL lock, it disregards waiting TOI operation, and gets the lock and immediately gets BF-aborted either by TOI directly or by aborted DML operation. Since there is no wsrep transaction for ALTER, it gets BF-aborted by setting killed state for the tread. But before entering TOI, ALTER doesn't check killed state, so it replicates, and applies on the other nodes successfully, but then it rolls back on the local node, causing inconsistency ([MDEV-32938](https://jira.mariadb.org/browse/MDEV-32938))

### Can result in hang or crash

* Crash while trying to complain "unsupported meta-data version" on `ALTER TABLE...IMPORT TABLESPACE` with MySQL 8.0 files ([MDEV-29972](https://jira.mariadb.org/browse/MDEV-29972))
* Wrong table attribute `PAGE_COMPRESSED=1` shown for tables in the InnoDB system tablespace ([MDEV-31000](https://jira.mariadb.org/browse/MDEV-31000))
* MariaDB crashes with foreign\_key\_checks=0 when changing a column and adding a foreign key at the same time ([MDEV-32638](https://jira.mariadb.org/browse/MDEV-32638))
* Sometimes node has been dropped from the cluster on startup `Shutdown with async replica` ([MDEV-31413](https://jira.mariadb.org/browse/MDEV-31413)) with diagnostics like:

```
[ERROR] Slave SQL: Error 'WSREP has not yet prepared node for application use' on query
```

and

```
[ERROR] Slave SQL: Node has dropped from cluster, Gtid 1-1-1, Internal MariaDB error code: 1047" in the server log
```

* `GTIDs` may diverge in Galera cluster after `CREATE TABLE` AS ([MDEV-27806](https://jira.mariadb.org/browse/MDEV-27806))\
  This can subsequently lead to diagnostics like:

```
[ERROR] mariadbd: Error writing file '/opt/maria10.1/binlog/BINLOG' (errno: 1950 "Unknown error 1950")"
```

and node crash:

```
wsrep::transaction::before_rollback(): Assertion state() == s_executing || state() == s_preparing || state() == s_prepared || state() == s_must_abort || state() == s_aborting || state() == s_cert_failed || state() == s_must_replay` failed
```

* `SHOW SLAVE STATUS` can deadlock an errored replica when a parallel replica worker gets killed at about when SHOW is issued ([MDEV-10653](https://jira.mariadb.org/browse/MDEV-10653))
* When executing `SELECT BINLOG_GTID_POS(@binlog_file...)` with the user variable being NULL, the server can crash ([MDEV-33045](https://jira.mariadb.org/browse/MDEV-33045))
* A Query that uses a specific SQL construct can cause a server crash. The construct is an equality comparison of table-less row subquery and a subquery that has a UNION operation at the top level: (`SELECT 'foo', 'bar'`) = (`SELECT col1, col2 FROM t1 ... UNION ...`) ([MDEV-29070](https://jira.mariadb.org/browse/MDEV-29070))
* A `DELETE` with `ORDER BY` and semijoin optimization can cause a crash ([MDEV-32212](https://jira.mariadb.org/browse/MDEV-32212))
* Possible crash when lateral derived in a query is guaranteed to return no rows ([MDEV-31279](https://jira.mariadb.org/browse/MDEV-31279))
* When using `EXCHANGE PARTITION` to replace a partition with a table, the server can crash if the to be exchanged table is using a virtual column which is not matching the partitioning key ([MDEV-28127](https://jira.mariadb.org/browse/MDEV-28127))
* When using `INSERT DELAYED` with a table using virtual columns, the server can crash ([MDEV-29932](https://jira.mariadb.org/browse/MDEV-29932))
* When using `SELECT` from a derived table with using AS OF, the server can crash ([MDEV-32082](https://jira.mariadb.org/browse/MDEV-32082))
* When using `JSON_CONTAINS_PATH` in a comparison in a prepared statement, the server can crash on execution of the statement ([MDEV-32867](https://jira.mariadb.org/browse/MDEV-32867))
* Server hangs on `DROP DATABASE` after a failing LOCK TABLES on Spider table : ([MDEV-29667](https://jira.mariadb.org/browse/MDEV-29667))
* When using two temporary tables in `OPTIMIZE TABLE`, executed as a prepared statement, the server can crash ([MDEV-31523](https://jira.mariadb.org/browse/MDEV-31523))
* When calling SP invoking another SP with a parameter requiring a type conversion, the server can crash ([MDEV-33270](https://jira.mariadb.org/browse/MDEV-33270))

### Can result in unexpected behavior

* `SHOW WARNINGS` can show wrong foreign key related warnings/errors from an earlier transaction for InnoDB ([MDEV-32833](https://jira.mariadb.org/browse/MDEV-32833))
* `LeakSanitizer` errors in `mem_heap_create_block_func` upon query from I\_S.INNODB\_SYS\_TABLES with LIMIT ROWS EXAMINED ([MDEV-32890](https://jira.mariadb.org/browse/MDEV-32890))
* Query from `I_S.INNODB_SYS_INDEXES` exceeding `LIMIT ROWS EXAMINED` causes `ER_UNKNOWN_ERROR` and `LeakSanitizer` errors in `rec_copy_prefix_to_buf_old` ([MDEV-28613](https://jira.mariadb.org/browse/MDEV-28613))
* Unexpected `ER_ERROR_ON_RENAME` upon DROP non-existing `FOREIGN KEY` with `ALGORITHM=COPY` ([MDEV-22230](https://jira.mariadb.org/browse/MDEV-22230))
* `FOREIGN_KEY_CHECKS` does not prevent non-copy alter from creating invalid FK structure ([MDEV-29092](https://jira.mariadb.org/browse/MDEV-29092))
* Secondary indexes on `VARCHAR` columns may be corrupted when the VARCHAR is extended so much that a column prefix index must be used ([MDEV-21245](https://jira.mariadb.org/browse/MDEV-21245))
* Spider: Valid `LEFT JOIN` results in `ERROR 1064` ([MDEV-26247](https://jira.mariadb.org/browse/MDEV-26247))
* Syntax error upon query with subquery from Spider table ([MDEV-30392](https://jira.mariadb.org/browse/MDEV-30392))
* Spider doesn't recognize `SEMI-JOIN` ([MDEV-31645](https://jira.mariadb.org/browse/MDEV-31645))
* `wsrep_provider_options` can be truncated on deep and long directory paths with diagnostics like: "Warning 1265 Data truncated for column 'VARIABLE\_VALUE' at row 1" in the server log ([MDEV-32634](https://jira.mariadb.org/browse/MDEV-32634))
* Mariadb-dump option `--delete-master-logs` is ignored ([MDEV-32953](https://jira.mariadb.org/browse/MDEV-32953))
* multi source replication filters breaking GTID semantic ([MDEV-26632](https://jira.mariadb.org/browse/MDEV-26632))
* `wsrep_gtid_domain_id` is ignored on any node other than bootstrapped node when the wsrep\_gtid\_mode is set to ON ([MDEV-32740](https://jira.mariadb.org/browse/MDEV-32740))
* A connection can control `RAND()` in following connection if used in conjunction with set `rand_seed1, rand_seed2` ([MDEV-33148](https://jira.mariadb.org/browse/MDEV-33148))
* mariadb-upgrade does not remove mysql.plugin entries for plugins that became bundled. Error message `"[ERROR] mariadbd: Plugin 'unix_socket' is already installed."` is shown when upgrading ([MDEV-32043](https://jira.mariadb.org/browse/MDEV-32043))
* TaskMax not set to infinity in the MariaDB systemd unit, therefor a lower number than defined in `max_connections` might be possible for the number of connections ([MDEV-30236](https://jira.mariadb.org/browse/MDEV-30236))
* If storage engine Spider is loaded upon server startup, Spider related system, and status variables are not available (MENT-2043)
* Regular expressions cannot be used in queries on tables of type SPIDER ([MDEV-32986](https://jira.mariadb.org/browse/MDEV-32986))
* MariaDB Enterprise Backup sometimes shows the error `Can't open shared library '/file_key_management.so' (errno: 2, cannot open shared object file: No such file, or directory)` when the option `--target-dir` is not used with `--prepare` ([MDEV-29110](https://jira.mariadb.org/browse/MDEV-29110))
* The database part is not case sensitive in Stored Procedure names. This can lead to using the wrong stored procedure, if the same database name is used as lower, and uppercase. ([MDEV-33019](https://jira.mariadb.org/browse/MDEV-33019))
* `CREATE UNIQUE INDEX` can fail with an incorrect `"ERROR 1286 (42000): Unknown storage engine 'partition'"` ([MDEV-21618](https://jira.mariadb.org/browse/MDEV-21618))
* After successful connection, server sets `SERVER_STATUS_AUTOCOMMIT` in server\_status in the OK packet although the global variable `autocommit=0 is set` ([MDEV-32875](https://jira.mariadb.org/browse/MDEV-32875))
* In some cases it is possible to create a Spider table which is referencing to a table on the same instance although `spider_same_server_link=0` is set ([MDEV-29718](https://jira.mariadb.org/browse/MDEV-29718))
* Spider fails to auto-discover a table structure with `ERROR 12500 (HY000): unknown` ([MDEV-33008](https://jira.mariadb.org/browse/MDEV-33008))
* REGEXP\_REPLACE treats empty strings different than `REPLACE in ORACLE` mode ([MDEV-29095](https://jira.mariadb.org/browse/MDEV-29095))
* The Enterprise Audit Plugin does not always report the user name (MENT-2035)

### Related to performance

* An `ALTER` using `ALGORITHM=INPLACE` or adding new indexes can increase the table space file size ([MDEV-26740](https://jira.mariadb.org/browse/MDEV-26740))
* Operations that involve extending InnoDB files can be extremely slow when the data directory resides on an NFS server that uses a smaller block size than 4096 bytes ([MDEV-32268](https://jira.mariadb.org/browse/MDEV-32268))

## \* Platforms

In alignment to the enterprise lifecycle, MariaDB Enterprise Server 10.4.33-23 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64, ARM64)
* Microsoft Windows (x86\_64) (MariaDB Enterprise Cluster excluded)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)

Some components of MariaDB Enterprise Server are supported on a subset of platforms. See MariaDB Engineering Policies for details.

## Installation Instructions

* [MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server)
* [Enterprise Cluster Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[10](broken-reference)[.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server 10.4](broken-reference)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server 10.4](broken-reference)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-4-to-mariadb-10-5)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
