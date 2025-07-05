# Release Notes for MariaDB Enterprise Server 10.6.20-16

MariaDB Enterprise Server 10.6.20-16 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-enterprise-server/README.md) 10.6.

MariaDB Enterprise Server 10.6.20-16 was released on 2024-12-10.

## Backports

* New, Detailed Replication Lag Representation (MENT-2095)
  * The Seconds\_Behind\_Master field of SHOW REPLICA STATUS can be complex and confusing, especially when parallel replication, delayed replication, or the option sql\_slave\_skip\_counter is used. To help provide a consistent view of replication lag, three new fields have been added to the statement's output to provide specific timing information about the state of the IO and SQL threads.
  * Three new values have been added to the replica status:
    * `Master_last_event_time`
      * Timestamp of the last event read from the primary by the IO thread
    * `Slave_last_event_time`
      * Timestamp from the primary of the last event committed on the replica
    * `Master_Slave_time_diff`
      * The difference of the above two timestamps
* New Information Schema Table For Password Related Data (MENT-2145)\
  A new information Schema view, USERS, has been added, which DBAs can use to get insights about password related information for a user. This information can be used:
  * by an application to inform a user about a password about to expire or an account which is at risk of being blocked due to the number of wrong passwords entered
  * by DBAs to query users which have been blocked because of too many invalid passwords entered
  * The new view includes the fields:
    * `USER` – A string including user name and host
    * `PASSWORD_ERRORS` – A counter with the current number of wrong passwords entered
      * Reset to 0 when a correct password has been entered
      * An account is blocked, if `max_password_errors` is reached
      * `NULL` for accounts with privilege `CONNECTION ADMIN`
    * `PASSWORD_EXPIRATION_TIME` – The date and time when the password expires or NULL, if the password never expires
* GTID binlog events now include the thread ID (MENT-2180)
  * The thread ID and the corresponding statement can now be retrieved from binary logs
  * The output of mariadb-binlog also includes the thread ID

## Notable Changes

* A new parameter `--quick-max-column-width` is now available in the mariadb client to limit the field width when used with the `--quick mode` ([MDEV-34704](https://jira.mariadb.org/browse/MDEV-34704))
* JSON\_TABLE allows to specify default column values, but they had to be specified as string constants ([MDEV-25822](https://jira.mariadb.org/browse/MDEV-25822))
  * With this patch, one can specify default values as any literals (string, integer, decimal number, date literal, etc)\
    Example:

```sql
SELECT *
 FROM
json_table('{"a": "123"}',
 '$' columns(col1 INT path '$.a' DEFAULT 1 ON empty)) AS T;
SELECT *
 FROM
json_table('{"a": "123"}',
 '$' columns(col1 DATE path '$.DATE' DEFAULT DATE '2020-01-01' ON empty)) AS T;
```

* A new option `--skip-freed-pages` has been added to the innochecksum tool (MENT-2183)
  * This option can be used to skip reporting freed undo logs as existing undo log pages

## Changes in Storage Engines

* This release originally incorporated [MariaDB ColumnStore engine version 23.10.2](../../columnstore/mariadb-columnstore-23-10-release-notes/mariadb-columnstore-23-10-2-release-notes.md)
* This release now incorporates [MariaDB ColumnStore engine version 23.10.3](../../columnstore/mariadb-columnstore-23-10-release-notes/mariadb-columnstore-23-10-3-release-notes.md)

## Issues Fixed

### Can result in data loss

* Possible corruption due to a rare race condition between page creation and eviction ([MDEV-34453](https://jira.mariadb.org/browse/MDEV-34453))
  * An error like "\[ERROR] InnoDB: Trying to read ... bytes at ... outside the bounds of the file" will be shown in the error log
* Using `group_concat` with a compressed or GIS column can lead to a server crash and potential data corruption for users performing `group_concat` operations on tables containing these data types ([MDEV-16699](https://jira.mariadb.org/browse/MDEV-16699))
* Unique hash index corruption for system-versioned tables after DML including a DELETE HISTORY statement, causing data corruption and error 'Record in index not found on update' ([MDEV-33470](https://jira.mariadb.org/browse/MDEV-33470))

### Can result in hang or crash

* When using Total Order Isolation (TOI) executing ALTER TABLE while a SR transaction is in progress, the user encounters a freeze and a server error "InnoDB: WSREP: BF lock wait long for trx" ([MDEV-34836](https://jira.mariadb.org/browse/MDEV-34836))
* A query could cause a crash if it has a HAVING clause with a construct tblX.column=column\_or\_constant and the optimizer was able to infer that table tblX is a constant table. Note that the HAVING clause may be from the original query or may come from [Condition Pushdown optimization](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimizations-for-derived-tables/condition-pushdown-into-derived-table-optimization)) ([MDEV-23983](https://jira.mariadb.org/browse/MDEV-23983))
* Calling a UDF for the engine SPIDER results in a crash if the SPIDER storage engine plugin could not be loaded ([MDEV-34682](https://jira.mariadb.org/browse/MDEV-34682))
* The use of XA PREPARE may cause InnoDB to hang ([MDEV-34690](https://jira.mariadb.org/browse/MDEV-34690))
* Under Windows Subsystem for Linux, InnoDB crashes on ALTER TABLE or OPTIMIZE TABLE ([MDEV-34938](https://jira.mariadb.org/browse/MDEV-34938))
* Server crashes when setting `wsrep_cluster_address` after adding invalid value to `wsrep_allowlist` table ([MDEV-31173](https://jira.mariadb.org/browse/MDEV-31173))
* mariadbd hangs on startup when `--init-file` target does not exist ([MDEV-34814](https://jira.mariadb.org/browse/MDEV-34814))
* Possible server crash in cases where the function `DEFAULT()` is part of a query ([MDEV-35276](https://jira.mariadb.org/browse/MDEV-35276))
* Primary stalling when a DDL is executed using semi-sync replication with wait point = `AFTER_SYNC` (MENT-2162)
* Deadlock on Replica during BACKUP STAGE BLOCK\_COMMIT on XA transactions (MENT-2152)
* In some situations, where a MariaDB Enterprise cluster (Galera) node crashes, some threads are still working. This is visible via the error log, which is still getting errors written by the node. As the node stops interacting correctly with other cluster nodes and is blocking them from taking over the primary state, the whole cluster hangs ([MDEV-32363](https://jira.mariadb.org/browse/MDEV-32363))
* When switching to the SQL Mode EXTENDED\_ALIASES and selecting from a table of type SPIDER, the server can crash (MENT-2108)

### Can result in unexpected behavior

* When a user runs mariadb-binlog with `--stop-position`, they would expect the output to contain events up to that event. If the output did not contain events up to that event, this may result in various unexpected behaviors, e.g., an incomplete database state if they piped the output to the mariadb client and expected certain transactions to have executed in the database, yet never were run ([MDEV-27037](https://jira.mariadb.org/browse/MDEV-27037))
* A table name can not be reused when the table was changed using "ALTER TABLE...STATS\_PERSISTENT=0" and was dropped afterwards. This also results in the error "Can't write; duplicate key in table 'mysql.innodb\_table\_stats" in tsing ALTER TABLE...STATS\_PERSISTENT=0 fails to drop statistics" ([MDEV-34207](https://jira.mariadb.org/browse/MDEV-34207))
* Changing a data type of a field used in a foreign key constraint fails with Error "Cannot change column '...': used in a foreign key constraint '...'" ([MDEV-34392](https://jira.mariadb.org/browse/MDEV-34392))
  * This ALTER only fails if the type of field is changed in a multi-ALTER statement, where types of other fields are changed with the ALTER
* Creation of a view with UNION and SELECT ... FOR UPDATE in the definition fails with error "ER\_PARSE\_ERROR (1064): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near..." ([MDEV-29537](https://jira.mariadb.org/browse/MDEV-29537))
* In some contexts text strings containing numbers with the integer part equal to zero and the fractional part not equal to zero were erroneously evaluated as FALSE in WHERE condition ([MDEV-34123](https://jira.mariadb.org/browse/MDEV-34123))
* INSERT...SELECT on MyISAM or ARIA tables are replicated by MariaDB Enterprise Cluster (Galera) ([MDEV-34647](https://jira.mariadb.org/browse/MDEV-34647))
* Storage Engine S3 causes 500 error when using Huawai Cloud S3 and possibly other S3 providers ([MDEV-34867](https://jira.mariadb.org/browse/MDEV-34867))
  * A new option `S3-provider` has been added. `S3-provider=Huawai` needs to be set for Huawai Cloud S3
* JSON\_TABLE doesn't properly unquote strings ([MDEV-27412](https://jira.mariadb.org/browse/MDEV-27412))
* SELECT MIN on Spider table returns more rows than expected ([MDEV-26345](https://jira.mariadb.org/browse/MDEV-26345))
* Can't selectively restore sequences using innodb tables from backup ([MDEV-32350](https://jira.mariadb.org/browse/MDEV-32350))
* LOAD DATA INFILE with geometry data fails ([MDEV-34883](https://jira.mariadb.org/browse/MDEV-34883))
* Executing an UPDATE statement in prepared statement mode having positional parameter bound with an array can result in an incorrect number of updated rows in case there is a BEFORE UPDATE trigger that executes yet another UPDATE statement to change a table ([MDEV-34718](https://jira.mariadb.org/browse/MDEV-34718))
* Recovery fails to note some log corruption, resulting in "log sequence number in the future" error messages, and possibly adds more corruption ([MDEV-34802](https://jira.mariadb.org/browse/MDEV-34802))
  * When log corruption is noted, the server can now only be started when using the option `innodb_force_recovery`
* When SET GLOBAL innodb\_adaptive\_hash\_index=ON is set, ALTER TABLE...IMPORT TABLESPACE with FULLTEXT SEARCH may corrupt the adaptive hash index ([MDEV-35059](https://jira.mariadb.org/browse/MDEV-35059))
* InnoDB fails to merge the change buffer to ROW\_FORMAT=COMPRESSED tables. This can result in secondary indexes in ROW\_FORMAT=COMPRESSED tables becoming corrupted, which in turn would lead to wrong results for queries that use those secondary indexes ([MDEV-34879](https://jira.mariadb.org/browse/MDEV-34879))
* CHECK TABLE would notice the corruption
* OPTIMIZE TABLE would fix the corruption
* No error/warning returned when a transaction is executed, which includes transactional and non-transactional engines ([MDEV-30653](https://jira.mariadb.org/browse/MDEV-30653))
  * When using the experimental option `wsrep_mode=REPLICATE_ARIA` a transaction can possibly include changes to tables using transactional and non-transactional engines. But only the changes of the transactional engine will be rolled back in case of a conflict
  * NOTE: Experimental features should not be used on production
* Unexpected error "Row size too large (> 8123)..." for a correct INSERT after a instantly dropped BLOB column ([MDEV-35122](https://jira.mariadb.org/browse/MDEV-35122))
* Wrong binlog timestamps on secondary nodes of MariaDB Enterprise Cluster (MENT-2164)
* InnoDB fails to shrink the system tablespace when it contains leaked undo log pages. It fails to free the unused segment if a XA PREPARE transaction exist or if the previous shutdown was not done with `innodb_fast_shutdown=0` (MENT-2148)
  * The :autoshrink attribute needs to be set for the system tablespace to free disk space on startup
* When the MariaDB Enterprise Audit Plugin is configured to log ACL queries, a statement CREATE USER .. IDENTIFIED VIA ed25519 USING PASSWORD(...) is logged including the password (MENT-2181)
* When the MariaDB Enterprise Audit Plugin is configured to log ACL queries, passwords are masked for CREATE USER .. IDENTIFIED BY, but not for CREATE OR REPLACE USER, or SET STATEMENT ... FOR CREATE USER (MENT-2188)

### Related to performance

* Bug that causes blocking issues when other transactions attempt to acquire locks on records held by an XA transaction in the prepared state, even if those records haven't been modified ([MDEV-34466](https://jira.mariadb.org/browse/MDEV-34466))
  * This affects InnoDB storage engine, XA transactions, and non-blocking mode
* Unnecessary copying of log records by MariaDB Enterprise Backup when further transaction commits are blocked by BACKUP STAGE BLOCK\_COMMIT (MENT-2133)
  * It also would cause further effort of rolling back incomplete transactions after the backup is restored
* Aria internal temporary tables unnecessarily write all changed blocks to disk when the table is closed at end of query (MENT-2182)

## Changelog

For the complete list of changes in this release, see the [changelog](changelog-for-mariadb-enterprise-server-10-6-20-16.md).

## Platforms

In alignment to the [enterprise lifecycle](../enterprise-server-lifecycle.md), MariaDB Enterprise Server 10.6.20-16 is provided for:

* AlmaLinux 8 (x86\_64, ARM64)
* AlmaLinux 9 (x86\_64, ARM64)
* Debian 11 (x86\_64, ARM64)
* Debian 12 (x86\_64, ARM64)
* Microsoft Windows (x86\_64) (MariaDB Enterprise Cluster excluded)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, ARM64, PPC64LE)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)
* Ubuntu 22.04 (x86\_64, ARM64)
* Ubuntu 24.04 (x86\_64, ARM64)

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see [MariaDB Corporation Engineering Policies".](https://mariadb.com/engineering-policies)

* [MariaDB Enterprise Server 10.6.4-1](release-notes-for-mariadb-enterprise-server-10-6-4-1.md)

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
