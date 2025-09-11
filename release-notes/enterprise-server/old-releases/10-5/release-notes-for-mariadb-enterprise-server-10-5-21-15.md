# Release Notes for MariaDB Enterprise Server 10.5.21-15

MariaDB Enterprise Server 10.5.21-15 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.5. This release includes a variety of fixes.

MariaDB Enterprise Server 10.5.21-15 was released on 2023-06-13.

## Fixed Security Vulnerabilities

| CVE (with cve.org link)                                                         | CVSS base score                                                               |
| ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [CVE-2022-47015](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47015) | N/A (Medium)[#1](release-notes-for-mariadb-enterprise-server-10-5-21-15.md#1) |

`#1`:\
MariaDB CVEs are assigned a word rating instead of a CVSS base score. See the MariaDB Engineering Policy for details.

## Notable Changes

* For compatibility, [JSON\_PRETTY()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_pretty) has been added as an alias to JSON\_DETAILED(). ([MDEV-19160](https://jira.mariadb.org/browse/MDEV-19160))
* InnoDB's internal performance has been improved. ([MDEV-30567](https://jira.mariadb.org/browse/MDEV-30567))
* The [aria\_log\_dir\_path system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/aria/aria-system-variables) is added as read-only. ([MDEV-30971](https://jira.mariadb.org/browse/MDEV-30971))
* The default value for the [core\_file system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#core_file) has been changed from None to OFF. ([MDEV-11356](https://jira.mariadb.org/browse/MDEV-11356))
* Starting with this release, the [innodb\_buffer\_pool\_filename system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_filename) is read-only and can't be changed dynamically. ([MDEV-30453](https://jira.mariadb.org/browse/MDEV-30453))
  * In previous releases, when `innodb_buffer_pool_dump_at_shutdown` was enabled, users with the `SUPER` privilege were able to dynamically change the value of the [innodb\_buffer\_pool\_filename system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_filename):

```sql
SET GLOBAL innodb_buffer_pool_filename='SOME_FILE_PATH';
```

* Starting with this release, the [innodb\_buffer\_pool\_filename system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_filename) must be configured in a configuration file prior to starting up the server:

```
[mariadb]
innodb_buffer_pool_filename=SOME_FILE_PATH
```

* The [aria\_log\_dir\_path system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/aria/aria-system-variables) is added as read-only. ([MDEV-26153](https://jira.mariadb.org/browse/MDEV-26153))
  * The `--aria-log-dir-path` command-line option is added to `mariadb-backup`.
* By default, [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup) no longer prints messages about log scanning. ([MDEV-25765](https://jira.mariadb.org/browse/MDEV-25765))
  * In previous releases, messages like the following could be printed excessively:

```
log scanned up to (LSN)
```

* Starting with this release, the messages about log scanning are only printed when [--verbose](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup/mariadb-backup-options#-verbose) is enabled.

## Issues Fixed

### Can result in data loss

* When a backup is created with [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup) and [aria\_log\_dir\_path](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/aria/aria-system-variables) is configured, the Aria logs are not copied to the backup. ([MDEV-30968](https://jira.mariadb.org/browse/MDEV-30968))
* When system versioning is enabled for a table without a primary key, changes to the table are not properly replicated. ([MDEV-30430](https://jira.mariadb.org/browse/MDEV-30430))
* When a partitioned table contains a prefix index on a column that uses a `NOPAD` collation, queries with `ORDER BY` can return rows in the wrong order. ([MDEV-30072](https://jira.mariadb.org/browse/MDEV-30072))
* For some collations, when a unique constraint is defined with `UNIQUE(..) USING HASH`, duplicate values are accepted. ([MDEV-30034](https://jira.mariadb.org/browse/MDEV-30034))
* When an InnoDB table with `ROW_FORMAT=REDUNDANT` is being rebuilt due to a DDL statement, the server can crash while trying to apply cached DML operations to the rebuilt table. ([MDEV-26198](https://jira.mariadb.org/browse/MDEV-26198))
* Long uniques don't work correctly with `Unicode` collations. Equal strings (in terms of the collation) are compared as unequal if the length of the strings are different. ([MDEV-27653](https://jira.mariadb.org/browse/MDEV-27653), [MDEV-28190](https://jira.mariadb.org/browse/MDEV-28190))
* When [innodb\_buffer\_pool\_filename](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_filename) is set to the empty string, the server tries to delete the [datadir](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#datadir) during shutdown. ([MDEV-30453](https://jira.mariadb.org/browse/MDEV-30453))
  * Starting with this release, the [innodb\_buffer\_pool\_filename system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_filename) is read-only and can't be changed dynamically.
* When [slave\_parallel\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is `optimistic` and [slave\_parallel\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is greater than `0`, [ALTER SEQUENCE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/alter-sequence) can fail with an out-of-order binlog error if the sequence uses InnoDB. ([MDEV-31077](https://jira.mariadb.org/browse/MDEV-31077))
  * In previous releases, the following error can be raised:

```
Last_Error: Error 'An attempt was made to binlog GTID 0-1-100 which would create an out-of-order sequence number with existing GTID 0-1-100 and gtid stric mode is enabled' on query. Default database: 'test'. Query: 'alter sequence s1 restart with 1' will be shown.
```

* When a [UNIQUE](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/UNIQUE/README.md) index includes a `PERIOD` in its definition, a duplicate key error can be incorrectly raised when the table uses the [utf8mb4\_unicode\_nopad\_ci collation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-collation). ([MDEV-30415](https://jira.mariadb.org/browse/MDEV-30415))

### Can result in a hang or crash

* When an `UPDATE` or `DELETE` is rolled back from an InnoDB table with ROW\_FORMAT=COMPRESSED, the server can crash. ([MDEV-30882](https://jira.mariadb.org/browse/MDEV-30882))
* When the [LEFT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/left) function is called on a string that has no character set defined, the server can crash. ([MDEV-30351](https://jira.mariadb.org/browse/MDEV-30351))
* With Galera, when [wsrep\_sst\_method=mariadb-backup](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) is set and `encrypt=4` is enabled for State Snapshot Transfers (SSTs), SSTs can fail if the version of socat installed on the donor node is 1.7.4.0 or later. ([MDEV-30402](https://jira.mariadb.org/browse/MDEV-30402))
  * In previous releases, SSTs could fail with the following error in the donor node's MariaDB error log if the version of `socat` installed is 1.7.4.0 or later:

```
E Failed to set SNI host ""
```

* Starting with this release, when the SST script starts the `socat` listener on the donor node, the error is prevented by setting `no-sni=1` if the version of `socat` installed is 1.7.4.0 or later.
* When optimizer trace is enabled, if a view is part of a multi-table update, the server can crash. ([MDEV-31085](https://jira.mariadb.org/browse/MDEV-31085))
* When a view definition contains a `UNION` and the view is queried using server-side prepared statements, if the optimizer pushes down a condition into the execution of the view, the server can crash during character set conversions. ([MDEV-31102](https://jira.mariadb.org/browse/MDEV-31102))
* When a replica server connects to a primary server with `MASTER_USE_GTID=slave_pos`, if the primary server has encrypted binary logs that it can no longer decrypt, the primary server crashes due to a segmentation fault. ([MDEV-28798](https://jira.mariadb.org/browse/MDEV-28798))
  * In previous releases, the primary node would iterate over all of its binary logs to look for the requested GTID. When one of the binary logs could not be decrypted, the server would crash.
  * Starting with this release, when the primary node fails to decrypt a binary log in this scenario, it stops iterating over the binary logs and raises an error with the [ER\_MASTER\_FATAL\_ERROR\_READING\_BINLOG error code](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-1200-to-1299/e1236) with the following error message:

```
Got fatal error 1236 from master when reading data from binary log: 'Could not set up decryption for binlog.'
```

* With Galera, when streaming replicating is enabled by setting the [wsrep\_trx\_fragment\_size system variable](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_trx_fragment_size), the server can crash when certain fragment sizes are specified. ([MDEV-30838](https://jira.mariadb.org/browse/MDEV-30838))
* When `EXPLAIN EXTENDED` is executed for a single-table `DELETE` that contains an `IN(..)` predicand, the server can crash. ([MDEV-31181](https://jira.mariadb.org/browse/MDEV-31181))
* When parallel replication is enabled by setting [slave\_parallel\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) greater than 0, the replica's parallel replication worker threads could hang after hitting an error. ([MDEV-30780](https://jira.mariadb.org/browse/MDEV-30780))
* In previous releases, when the server was hung in this scenario, the output of `SHOW SLAVE STATUS` would show that an error occurred, but the output would indicate that both the I/O and SQL threads were running.

```sql
SHOW SLAVE STATUS\G
```

```
*************************** 1. row ***************************
                Slave_IO_State: Waiting for master to send event
..
              Slave_IO_Running: Yes
             Slave_SQL_Running: Yes
..
                    Last_Errno: 1062
                    Last_Error: Could not execute Write_rows_v1 event on table TABLE_NAME; Duplicate entry 'VALUE' for key 'KEY_NAME', Error_code: 1062; handler error HA_ERR_FOUND_DUPP_KEY; the event's master log LOG_FILE, end_log_pos END_LOG_POS
..
```

* In this scenario, this issue causes one of the parallel replication worker threads to hang in the `closing tables` state, so the output of `SHOW PROCESSLIST` would show one worker thread in that state indefinitely:

```sql
SHOW PROCESSLIST;
```

```
+------+--------------+--------------------+------+--------------+-------+-----------------------------------------------+------------------+----------+
| Id   | User         | Host               | db   | Command      | Time  | State                                         | Info             | Progress |
+------+--------------+--------------------+------+--------------+-------+-----------------------------------------------+------------------+----------+
..
| 2394 | system user  |                    | NULL | Slave_worker | 50852 | closing tables                                | NULL             |    0.000 |
..
+------+--------------+--------------------+------+--------------+-------+-----------------------------------------------+------------------+----------+
```

* When the optimizer chooses how to split a semi-join, the server can crash. ([MDEV-31403](https://jira.mariadb.org/browse/MDEV-31403))
* With Galera, when `CREATE TEMPORARY SEQUENCE` is executed on a cluster node and binary logging is enabled, the server crashes. ([MDEV-25045](https://jira.mariadb.org/browse/MDEV-25045))
* With Galera, when a write set fails certification and binary logging is enabled, the WSREP sequence numbers (cluster-wide transaction IDs) used by a WSREP applier thread can become out of sync with the node's XIDs (internal transaction IDs) due to a race condition, which can cause the node to crash. ([MDEV-27317](https://jira.mariadb.org/browse/MDEV-27317))
  * In previous releases, when a write set failed certification and binary logging was enabled, a WSREP applier thread could sync the WSREP sequence number out-of-order, because the commit order could be released too early.
* With Galera, when streaming replicating is enabled by setting the [wsrep\_trx\_fragment\_size system variable](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_trx_fragment_size) and `CREATE TABLE .. SELECT` is executed, the server can crash. The following assertion is written to the MariaDB error log during the crash: ([MDEV-30862](https://jira.mariadb.org/browse/MDEV-30862))

```
Assertion `mode_ == m_high_priority' failed in void wsrep::client_state::after_applying()
```

* Starting with this release, the server prohibits `CREATE TABLE .. SELECT` in this scenario and raises the [ER\_NOT\_ALLOWED\_COMMAND error code](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-1100-to-1199/e1148) with the following error message:

```
ERROR 42000: CREATE TABLE AS SELECT is not supported with streaming replication
```

* With Galera, when a connection uses the handler interface to start a transaction on a table, the server can crash when the client disconnects. ([MDEV-30955](https://jira.mariadb.org/browse/MDEV-30955))\
  In previous releases, when the client disconnected, the server would rollback the transaction and release all locks, including the locks that the handler interface expected to survive after the transaction ended, which would cause the server to crash.
  * In previous releases, the following assertion is written to the MariaDB error log during the crash:

```
void close_thread_table(THD*, TABLE**): Assertion `thd->mdl_context.is_lock_owner(MDL_key::TABLE, table->s->db.str, table->s->table_name.str, MDL_SHARED)' failed.
```

* With Galera, when an SST donor changes to the non-primary state, the SST is not terminated properly, and the donor node crashes. (MENT-1708)
  * In previous releases, the following error message and assertion is written to the MariaDB error log during the crash:

```
[Warning] WSREP: server: NODE_NAME unallowed state transition: connected -> joined
void wsrep::server_state::state(wsrep::unique_lock<wsrep::mutex>&, wsrep::server_state::state): Assertion `0' failed.
```

* When a query is executed that uses `DISTINCT` and an aggregate function on a group, the server can crash. ([MDEV-31113](https://jira.mariadb.org/browse/MDEV-31113))
* When a server-side prepared statement is used to execute a query that references views and contains a `HAVING` clause, the server can crash upon second execution of the query. ([MDEV-31189](https://jira.mariadb.org/browse/MDEV-31189))
* When the InnoDB purge thread tries to use the change buffer for an uncommitted index, the server aborts with an assertion. ([MDEV-30076](https://jira.mariadb.org/browse/MDEV-30076))
* When the `rowid_filtering` optimization is used with a partitioned table, the server aborts with an assertion. ([MDEV-30596](https://jira.mariadb.org/browse/MDEV-30596))
* With Galera, a hang can occur in "starting" commit state due a deadlock between a KILL command and an abort issued by an applier. (MENT-1855)
  * Starting with this release, Total Order Isolation (TOI) is not used for the KILL command.
* When [binlog\_row\_image=FULL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is set and [slave\_parallel\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is greater than 0, replica servers can hang if data is inserted into tables with a sequence. ([MDEV-29621](https://jira.mariadb.org/browse/MDEV-29621))
* When a backup is prepared with [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup), the utility can hang due to a race condition between the thread flushing the buffer pool and the thread deleting the redo log file. ([MDEV-30860](https://jira.mariadb.org/browse/MDEV-30860))
* With Galera, when a transaction changes multiple tables that use different storage engines, some of which support the server's internal 2-phase commit protocol and some of which don't support it, the node crashes with an assertion failure. ([MDEV-30804](https://jira.mariadb.org/browse/MDEV-30804))
  * In previous releases, the following assertion failure is written to the MariaDB error log during the crash in this scenario:

```
int wsrep::transaction::ordered_commit(): Assertion `state() == s_committing' failed.
```

* Starting with this release, when Galera is enabled, mixed transactions are rejected in with the following error message:

```
ERROR HY000: Transactional commit not supported by involved engine(s)
```

* When InnoDB uses a lot of memory during crash recovery, the server can hang due to a race condition between the thread flushing the buffer pool and the thread performing the recovery. ([MDEV-30551](https://jira.mariadb.org/browse/MDEV-30551))
* With Galera, when streaming replicating is enabled by setting the [wsrep\_trx\_fragment\_size system variable](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_trx_fragment_size), the server can crash when backup locks or user-level locks are released. ([MDEV-25037](https://jira.mariadb.org/browse/MDEV-25037))
* With Galera, when one session is terminated using the [KILL statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/kill) and another session's transaction is aborted by the WSREP applier threads due to a conflict, the two operations use a conflicting mutex locking order, which can cause the node to hang. ([MDEV-28460](https://jira.mariadb.org/browse/MDEV-28460))
* With Galera, when many sessions are aborted by a WSREP applier thread due to conflicts, the sessions can hang due to a deadlock. (MENT-1693)
  * In previous releases, the output of [SHOW PROCESSLIST](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-processlist) could show sessions hang in the `acquiring total order isolation` state with queries like `KILL QUERY n`:

```
12345678	myuser	127.0.0.1:45071	mydb	Query	1058	acquiring total order isolation	KILL QUERY 20254887	0.000
```

### Can result in unexpected behavior

* When `EXPLAIN EXTENDED` is executed for a multi-table UPDATE that uses the system join type, the output can be incorrect. ([MDEV-31224](https://jira.mariadb.org/browse/MDEV-31224))
* When a query specifies `DISTINCT` and contains expressions using the `SUM()` function, the wrong results are returned. ([MDEV-20057](https://jira.mariadb.org/browse/MDEV-20057))
* When a view's definition contains a `HAVING` clause, selecting from the view can fail with an error. ([MDEV-28570](https://jira.mariadb.org/browse/MDEV-28570))
  * In previous releases, queries could raise an error with the [ER\_VIEW\_INVALID error code](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-1300-to-1399/e1356) and the following error message:

```
View 'test.v1' references invalid table(s) or column(s) or function(s) or definer/invoker of view lack rights to use them
```

* When a view's definition contains an aggregate function, selecting from the view can fail with an error. ([MDEV-28571](https://jira.mariadb.org/browse/MDEV-28571))
  * In previous releases, queries could raise an error with the [ER\_INVALID\_GROUP\_FUNC\_USE error code](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-1100-to-1199/e1111) and the following error message:

```
ERROR 1111 (HY000): Invalid use of group function
```

* When a view's definition contains a table-value constructor (TVC) as a single-value subquery, selecting from the view can fail with an error. ([MDEV-28603](https://jira.mariadb.org/browse/MDEV-28603))
  * In previous releases, queries could raise an error with the [ER\_VIEW\_INVALID error code](broken-reference) and the following error message:

```
View 'test.v1' references invalid table(s) or column(s) or function(s) or definer/invoker of view lack rights to use them
```

* When a view's definition contains an aggregate function in an uncorrelated subquery, the wrong result is returned. ([MDEV-29224](https://jira.mariadb.org/browse/MDEV-29224))
* When a `DELETE` statement contains a subquery with a `HAVING` clause or an aggregate function in the `WHERE` clause, the statement can fail with an error. ([MDEV-30586](https://jira.mariadb.org/browse/MDEV-30586))
  * In previous releases, queries could raise an error with the `ER_INVALID_GROUP_FUNC_USE` error code and the following error message:

```
ERROR 1111 (HY000): Invalid use of group function
```

* When an InnoDB tablespace has been discarded, selecting from [information\_schema.INNODB\_SYS\_INDEXES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_indexes-table) fails with an error. ([MDEV-30615](https://jira.mariadb.org/browse/MDEV-30615))
  * In previous releases, an error with the [ER\_UNKNOWN\_ERROR error code](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-1100-to-1199/e1105) is raised:

```
ERROR 1105 (HY000): Unknown error
```

* Starting with this release, no error is returned, and the results contain `NULL` for the `PAGE_NO` and `SPACE` columns for discarded tablespaces.
* When [innodb\_undo\_directory](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-system-variables#innodb_undo_directory) is set to a relative path, the path is not properly used by [mariadb-backup --copy-back](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup/mariadb-backup-options#-copy-back). ([MDEV-28187](https://jira.mariadb.org/browse/MDEV-28187))
  * In previous releases, the undo logs would be copied to the relative path compared to the current working directory.
  * Starting with this release, the undo logs are copied to the relative path compared to the [datadir](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#datadir).
* When `UNIX_TIMESTAMP(CURRENT_TIME())` is executed, the incorrect value is returned. ([MDEV-26765](https://jira.mariadb.org/browse/MDEV-26765))
  * In previous releases, `NULL` is returned.
* With Galera, when [wsrep\_sst\_method='mariadb-backup'](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) is set, systemd raises an error about a mismatched PID. ([MDEV-25887](https://jira.mariadb.org/browse/MDEV-25887))
  * In previous releases, systemd could raise the following error, where `BACKUP_PID` is the PID of MariaDB Enterprise Backup and `SERVER_PID` is the PID of MariaDB Enterprise Server:

```
Got notification message from PID BACKUP_PID, but reception only permitted for main PID SERVER_PID
```

* When an `UPDATE` contains a `WHERE` clause that contains a range condition over a non-indexed VARCHAR column, an error is raised. ([MDEV-20773](https://jira.mariadb.org/browse/MDEV-20773))
  * In previous releases, an error with the [ER\_DATA\_TOO\_LONG error code](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-1400-to-1499/e1406) is raised with the following error message:

```
ERROR 1406 (22001): Data too long for column 'COLUMN_NAME' at row 1
```

* When `slave_parallel_threads` is greater than `0` and `SHOW SLAVE STATUS` is executed, the connection can try to acquire an uninitialized mutex. ([MDEV-30620](https://jira.mariadb.org/browse/MDEV-30620))
  * In previous releases, a race condition could cause the mutexes of parallel replication worker threads to be acquired before they are initialized.
* The `ucs2_general_mysql500_ci` collation, which is intended for compatibility with older versions of MySQL, incorrectly sorts 'ß' after 's'. ([MDEV-30746](https://jira.mariadb.org/browse/MDEV-30746))
* When `EXPLAIN EXTENDED` is executed with an `INSERT`, `UPDATE`, `DELETE`, or `REPLACE`, a warning containing the query text is not printed. ([MDEV-30539](https://jira.mariadb.org/browse/MDEV-30539))
* The `rowid_filtering` optimization is applied incorrectly in some cases. ([MDEV-30218](https://jira.mariadb.org/browse/MDEV-30218))
* When preparing a partial backup, MariaDB Enterprise Backup raises error messages about missing InnoDB tablespace files that are expected to be missing, because they were excluded from the backup. ([MDEV-29050](https://jira.mariadb.org/browse/MDEV-29050))
* For certain data distributions, the optimizer histogram code can produce wrong selectivity, which can lead to performance degradation. ([MDEV-31067](https://jira.mariadb.org/browse/MDEV-31067))
* When InnoDB writes data from the doublewrite buffer to the redo log file, the [Innodb\_data\_written status variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables#innodb_data_written) is not properly incremented. ([MDEV-31124](https://jira.mariadb.org/browse/MDEV-31124))
* Parallel replication breaks if `XA PREPARE` fails updating replica GTID State ([MDEV-31038](https://jira.mariadb.org/browse/MDEV-31038))
* When InnoDB has opened more data files than [innodb\_open\_files](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-system-variables#innodb_open_files), opening additional data files takes longer than expected due to a performance regression. ([MDEV-30775](https://jira.mariadb.org/browse/MDEV-30775))
* When the [JSON\_OBJECTAGG function](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_objectagg) is called with a key value that includes a double quote, the double quote character is not escaped. ([MDEV-30412](https://jira.mariadb.org/browse/MDEV-30412))
* With `optimizer_switch='not_null_range_scan=on'`, when a `LEFT JOIN` is executed on an empty table, the results can be incorrect. ([MDEV-30333](https://jira.mariadb.org/browse/MDEV-30333))
* When a query contains a `GROUP BY` clause and the query calls an aggregate function on a table's primary key, the results can be incorrect if the `GROUP BY` clause is evaluated using an index. ([MDEV-30605](https://jira.mariadb.org/browse/MDEV-30605))
* With Galera, when a cluster node has the query cache enabled and the node has regular MariaDB replication configured, query cache entries are not properly invalidated when tables are changed due to replication. ([MDEV-28641](https://jira.mariadb.org/browse/MDEV-28641))
* When a backup is created with [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup), the utility opens the `aria_log_control` file in read/write mode instead of in read-only mode. (MENT-1794)

## Changes in Storage Engines

* This release incorporates MariaDB ColumnStore engine version 5.6.8-2.

## Interface Changes

* [aria\_log\_dir\_path](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/aria/aria-system-variables) system variable added.
* [core\_file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#core_file) system variable default value changed from None to OFF
* [innodb\_buffer\_pool\_filename](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_filename) system variable dynamic changed from Yes to No
* For compatibility, [JSON\_PRETTY()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_pretty) has been added as an alias to JSON\_DETAILED().
* `mariadb-backup` --aria-log-dir-path command-line option added.

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.5.21-15 is provided for:

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

* [Upgrade to MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-from-to-specific-versions/upgrading-from-mariadb-10-5-to-mariadb-10-6)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.5](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-between-major-mariadb-versions)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
