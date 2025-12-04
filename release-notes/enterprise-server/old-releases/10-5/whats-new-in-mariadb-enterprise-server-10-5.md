# What's New in MariaDB Enterprise Server 10.5?

MariaDB Enterprise Server 10.5 introduces the new features listed below.

## Notable Features

### Enterprise ColumnStore Storage Engine

The [ColumnStore storage engine](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) is a columnar storage engine that provides distributed, columnar storage for scalable analytical processing and smart transactions.

MariaDB Enterprise Server 10.5 includes an enterprise version of the [ColumnStore storage engine](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) as a plugin:

* It includes MariaDB Enterprise ColumnStore 5, which has many improvements.
* The installation process has been massively simplified.
* The multi-node implementation has been completely rebuilt to use a REST API for orchestration.
* See [What's New in MariaDB Enterprise ColumnStore 5](../../../columnstore/)? for more details.

## Other Features

### Embracing the MariaDB Name

MariaDB Enterprise Server 10.5 uses the "MariaDB" name in more places:

* It uses MariaDB in many error messages that previously referred to MySQL.
* It uses `DBD::MariaDB` for bundled Perl scripts that previously used DBD::mysql.
* It uses new MariaDB-based names as the primary names for many executables. The old names are still supported for backward compatibility using symbolic links. The new MariaDB-based names were first introduced in MariaDB Enterprise Server 10.4. However, in that version, the old names were still the primary names for the executables, and the new names were supported using symbolic links. See below for the new MariaDB-based names:

| Old Executable Name           | New Executable Name                                                                                                                     |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| mysql                         | [mariadb](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client)                                          |
| mysqld                        | [mariadbd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd)                     |
| mariadb-backup                | [mariadb-backup](../../10-5/broken-reference/)                                                                                          |
| mysql\_plugin                 | [mariadb-plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/mariadb-plugin)              |
| mysql\_upgrade                | [mariadb-upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/deployment-tools/mariadb-upgrade)                |
| mysql\_waitpid                | [mariadb-waitpid](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/mariadb-waitpid)            |
| mysqladmin                    | [mariadb-admin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/mariadb-admin)                |
| mysqlbinlog                   | [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog)                     |
| mysqlcheck                    | [mariadb-check](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/table-tools/mariadb-check)                         |
| mysqldump                     | [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump)     |
| mysqlimport                   | [mariadb-import](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-import) |
| mysqlshow                     | [mariadb-show](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/mariadb-show)                  |
| mysqlslap                     | [mariadb-slap](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/testing-tools/mariadb-slap)                         |
| mysql\_client\_test           | mariadb-client-test                                                                                                                     |
| mysql\_client\_test\_embedded | mariadb-client-test-embedded                                                                                                            |
| mysql\_config                 | mariadb-config                                                                                                                          |
| mysql\_convert\_table\_format | mariadb-convert-table-format                                                                                                            |
| mysql\_embedded               | mariadb-embedded                                                                                                                        |
| mysql\_find\_rows             | mariadb-find-rows                                                                                                                       |
| mysql\_fix\_extensions        | mariadb-fix-extensions                                                                                                                  |
| mysql\_install\_db            | mariadb-install-db                                                                                                                      |
| mysql\_ldb                    | mariadb-ldb.                                                                                                                            |
| mysql\_secure\_installation   | mariadb-secure-installation                                                                                                             |
| mysql\_setpermission          | mariadb-setpermission                                                                                                                   |
| mysql\_tzinfo\_to\_sql        | mariadb-tzinfo-to-sql                                                                                                                   |
| mysql\_upgrade\_service       | mariadb-upgrade-service                                                                                                                 |
| mysql\_upgrade\_wizard        | mariadb-upgrade-wizard                                                                                                                  |
| mysqld\_multi                 | mariadbd-multi                                                                                                                          |
| mysqld\_safe                  | mariadbd-safe                                                                                                                           |
| mysqld\_safe\_helper          | mariadbd-safe-helper                                                                                                                    |
| mysqldumpslow                 | mariadb-dumpslow                                                                                                                        |
| mysqlhotcopy                  | mariadb-hotcopy                                                                                                                         |
| mysqltest                     | mariadb-test                                                                                                                            |
| mysqltest\_embedded           | mariadb-test-embedded                                                                                                                   |

### Packaging

MariaDB Enterprise Server 10.5 includes some packaging improvements:

* It includes a new `mariadb-conv` command-line tool to encode/decode MariaDB-encoded file system names.
* Binary tarball packages have the following changes:
  * Embedded server (`libmysqld`) has been removed.
  * Debug symbols have been stripped from non-server binaries.
  * The server binary ([mariadbd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd)) retains its debug symbols, so that stack traces contain readable function names.
  * Binary tarball size has been reduced from over 1 GB to around 300 MB.
* It removes the TokuDB storage engine from packages.
* It removes the Cassandra storage engine from packages.
* It removes support for RHEL6 and CentOS 6.

### InnoDB Storage Engine

The [InnoDB storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) is an ACID-compliant storage engine that is very performant and reliable for general purpose transactional workloads.

MariaDB Enterprise Server 10.5 includes many significant improvements to the [InnoDB storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb):

* It implements a new thread pool for InnoDB background tasks, which allows for InnoDB to use system resources more efficiently.
  * It reduces semaphore contention in several areas to help the system perform better under high concurrency:
  * It reduces semaphore contention when accessing the buffer pool.
  * It removes the ability to configure multiple buffer pool instances, since it does not reduce contention.
  * It reduces semaphore contention when executing [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table) statements.
  * It uses table metadata locks instead of internal InnoDB semaphores for certain background operations.
  * It adds instrumentation that informs the server's thread pool about semaphore waits, so that the thread pool can let other client connections perform work while a client connection is waiting on a semaphore.
* It improves performance in several areas:
  * It uses a new InnoDB redo log format that is more efficient.
  * It removes the ability to configure multiple InnoDB redo log files, since it does not help performance.
  * It optimizes access to certain InnoDB page header fields.
  * It optimizes how the change buffer is merged.
  * It optimizes how InnoDB scrubs deleted data.
* It improves stability in several areas:
  * It improves how InnoDB scrubs deleted data by ensuring that scrubbing operations are properly written to the InnoDB redo log.
  * It receives foreign key metadata from the server, rather than relying on an internal SQL parser.
  * It allows prepared XA transactions to be properly recovered after a client disconnects.
* It allows the [number of InnoDB purge threads to be changed dynamically](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-purge#configuring-the-purge-threads) without a server restart. As a consequence, the innodb\_purge\_threads system variable can be changed dynamically with the [SET GLOBAL](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/setl) statement.
* It allows the [InnoDB redo log to be resized dynamically](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-redo-log) without a server restart. As a consequence, the innodb\_log\_file\_size system variable can be changed dynamically with the [SET GLOBAL](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/set-global/README.md) statement.
* It allows the [number of InnoDB I/O threads to be changed dynamically](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-purge#configuring-the-purge-threads) without a server restart. As a consequence, the [innodb\_read\_io\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_read_io_threads) and [innodb\_write\_io\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_write_io_threads) system variables can be changed dynamically with the [SET GLOBAL](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/set-global/README.md) statement.

### Spider Storage Engine

The [Spider storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) allows you to build complex and powerful distributed databases using federated and sharded tables.

MariaDB Enterprise Server 10.5 contains several enhancements for the [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) storage engine:

* It adds support for an [ODBC foreign data wrapper](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc). This feature has beta maturity.
* It adds the [information\_schema.SPIDER\_WRAPPER\_PROTOCOLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/information-schema-spider_wrapper_protocols-table) table.

### Aria Storage Engine

The [Aria storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) is a crash-safe storage engine that is incredibly fast for read-only workloads.

MariaDB Enterprise Server 10.5 contains several enhancements for the [Aria storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria):

* It handles the [BACKUP STAGE BLOCK\_COMMIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/backup-commands/backup-stage) statement by blocking commits to Aria tables, which allows for safer backups with [MariaDB Backup](../../10-5/broken-reference/).
* It increases the index length limit for Aria tables from 1000 bytes to 2000 bytes.

### S3 Storage Engine

MariaDB Enterprise Server 10.5 contains several enhancements to the [S3 storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/s3-storage-engine):

* The S3 storage engine allows tables to be archived in S3-compatible storage.
* Tables can be archived in S3 by executing [ALTER TABLE ... ENGINE=S3](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table).
* After the table has been archived, it becomes read-only.
* The S3 storage engine supports partitioning.
* The S3 storage engine supports replication.

## Privileges Comparison ES10.4 and ES10.5.8-5

MariaDB Enterprise Server 10.5 adds privileges that allow operations that previously required the [SUPER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#super). The following table is a summary of the **changes** between MariaDB Enterprise Server 10.4 and MariaDB Enterprise Server 10.5.8-5. More specific detail is found in [MariaDB Replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication), and in [MariaDB Reference](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb/README.md).

### [BINLOG ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-admin)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Allows the user to execute [PURGE BINARY LOGS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/purge-binary-logs) statements
* Allows the user to [SET](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set) the following system variables:
  * [binlog\_annotate\_row\_events](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_commit\_wait\_count](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_commit\_wait\_usec](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_direct\_non\_transactional\_updates](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_file\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_row\_image](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_row\_metadata](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_stmt\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [expire\_logs\_days](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [log\_bin\_compress](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [log\_bin\_compress\_min\_len](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [log\_bin\_trust\_function\_creators](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [max\_binlog\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_binlog_cache_size)
  * [max\_binlog\_stmt\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_binlog_stmt_cache_size)
  * [max\_binlog\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_binlog_size)
  * [sql\_log\_bin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [sync\_binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)

### [BINLOG MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-monitor)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* [Legacy REPLICATION CLIENT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-client) privilege is an alias for this new privilege, but the capabilities have changed
* Unlike legacy REPLICATION CLIENT privilege, [BINLOG MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-monitor) can no longer execute SHOW SLAVE STATUS, SHOW REPLICA STATUS in ES10.5
* BINLOG MONITOR allows the user to execute [SHOW BINLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-events) statements
* BINLOG MONITOR allows the user to execute [SHOW BINLOG STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-status) statements
* BINLOG MONITOR allows the user to execute [SHOW BINARY LOGS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binary-logs) statements
* BINLOG MONITOR allows the user to execute [SHOW MASTER STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-status) statements
* If a user upgrades from ES10.4 or earlier to ES10.5.8-5 or later, any users with REPLICATION CLIENT or REPLICATION SLAVE privileges will automatically be granted the REPLICA MONITOR privilege. This privilege upgrade happens upon server startup, so mysql\_upgrade is not required
* The upgrade behavior does not apply to minor release upgrades that upgrade from ES10.5.6-4 or earlier ES10.5.x to ES10.5.8-5 or later

### [BINLOG REPLAY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-replay)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Allows the user to execute [BINLOG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/binlog) statements, which are output by [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog)
* Allows the user to execute [SET TIMESTAMP](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/timestamp) statements when [secure\_timestamp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#secure_timestamp) is set to replication
* Allows the user to set the session values of several system variables that are usually included in [BINLOG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/binlog) statements:
  * [gtid\_domain\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_seq\_no](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [pseudo\_thread\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#pseudo_thread_id)
  * [server\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)

### [CONNECTION ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#connection-admi)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Skips the execution of [init\_connect](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#init_connect) when the user connects
* Ignores [max\_connections](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_connections) when the user connects
* Ignores [max\_user\_connections](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_user_connections) when the user connects
* Ignores [max\_password\_errors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_password_errors) when the user connects
* Allows the user to kill connections owned by other users with the [KILL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/kill) statement
* Allows the user to set system variables:
  * [connect\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#connect_timeout)
  * [disconnect\_on\_expired\_password](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#disconnect_on_expired_password)
  * [extra\_max\_connections](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#extra_max_connections)
  * [init\_connect](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#init_connect)
  * [max\_connections](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_connections)
  * [max\_connect\_errors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_connect_errors)
  * [max\_password\_errors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_password_errors)
  * [proxy\_protocol\_networks](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#proxy_protocol_networks)
  * [secure\_auth](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#secure_auth)
  * [slow\_launch\_time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#slow_launch_time)
  * [thread\_pool\_exact\_stats](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_dedicated\_listener](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_idle\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_max\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_min\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_oversubscribe](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_prio\_kickup\_timer](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_priority](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_stall\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)

### [FEDERATED ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#federated-admin)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Allows the user to execute [CREATE SERVER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-server) statements
* Allows the user to execute [ALTER SERVER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-server) statements
* Allows the user to execute [DROP SERVER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-server) statements

### [READ\_ONLY ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#readonly-admin)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Allows the user to write data even if the [read\_only](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#read_only) system variable is enabled
* Allows the user to execute [DROP TRIGGER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-trigger) statements even if the [read\_only](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#read_only) system variable is enabled
* Allows the user to execute [START TRANSACTION READ WRITE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/start-transaction) statements even if the [read\_only](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#read_only) system variable is enabled
* Allows the user to set system variables:[read\_only](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#read_only)

### [REPLICA MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replica-monitor)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* REPLICA MONITOR is a new privilege in ES10.5.8-5 and was not present in earlier releases
* REPLICA MONITOR can execute:
  * [SHOW SLAVE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status)
  * [SHOW REPLICA STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status)
  * [SHOW ALL SLAVES STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/legacy-replication-statements/legacy-commands-show-slave-status)
  * [SHOW ALL REPLICAS STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status)
  * [SHOW RELAYLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-relaylog-events)
* If a user upgrades from ES10.4 or earlier to ES10.5.8-5 or later, any users with REPLICATION CLIENT or REPLICATION SLAVE privileges will automatically be granted the REPLICA MONITOR privilege. This privilege upgrade happens upon server startup, so mysql\_upgrade is not required
* The upgrade behavior does not apply to minor release upgrades that upgrade from ES10.5.6-4 or earlier ES10.5.x to ES10.5.8-5 or later
* REPLICA MONITOR is an alias for SLAVE MONITOR which is also new in ES10.5.8-5

### [REPLICATION CLIENT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-client)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| yes                | no                     |

**Notes:**

* Replaced by [BINLOG MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-monitor) in 10.5
* REPLICATION CLIENT can be used as an alias for BINLOG MONITOR but the capabilities for BINLOG MONITOR are different than those of legacy REPLICATION CLIENT
  * Unlike legacy REPLICATION CLIENT privilege, [BINLOG MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-monitor) can no longer execute SHOW SLAVE STATUS, SHOW REPLICA STATUS in ES10.5
  * REPLICATION CLIENT as an alias for BINLOG MONITOR:
    * Allows the user to execute [SHOW BINLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-events) statements
    * Allows the user to execute [SHOW BINLOG STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-status) statements
    * Allows the user to execute [SHOW BINARY LOGS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binary-logs) statements
    * Allows the user to execute [SHOW MASTER STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-status) statements
* If a user upgrades from ES10.4 or earlier to ES10.5.8-5 or later, any users with REPLICATION CLIENT or REPLICATION SLAVE privileges will automatically be granted the REPLICA MONITOR privilege. This privilege upgrade happens upon server startup, so mysql\_upgrade is not required
* The upgrade behavior does not apply to minor release upgrades that upgrade from ES10.5.6-4 or earlier ES10.5.x to ES10.5.8-5 or later

### [REPLICATION MASTER ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-master-admin)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Allows the user to execute [SHOW REPLICA HOSTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-hosts) statements
* Allows the user to execute [SHOW SLAVE HOSTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-hosts) statements
* Allows the user to set system variables:
  * [gtid\_binlog\_state](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_domain\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [master\_verify\_checksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [server\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)

### [REPLICATION REPLICA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-replica)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Added in ES10.5 as an alias for [REPLICATION SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave)

### [REPLICATION SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| yes                | yes                    |

**Notes:**

* Can be used as an alias for [REPLICATION REPLICA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-replica)
* In ES10.5 REPLICATION SLAVE can no longer execute SHOW RELAYLOG EVENTS. In ES10.5 versions earlier than ES10.5.8-5, SHOW RELAYLOG EVENTS requires [REPLICATION REPLICA ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-replica-admin). In ES10.5.8-5, SHOW RELAYLOG EVENTS requires [REPLICA MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replica-monitor)
* In ES10.5 REPLICATION SLAVE can no longer execute [SHOW BINLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-events). SHOW BINLOG EVENTS requires [BINLOG MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-monitor)
* If a user upgrades from ES10.4 or earlier to ES10.5.8-5 or later, any users with REPLICATION CLIENT or REPLICATION SLAVE privileges will automatically be granted the REPLICA MONITOR privilege. This privilege upgrade happens upon server startup, so mysql\_upgrade is not required
* The upgrade behavior does not apply to minor release upgrades that upgrade from ES10.5.6-4 or earlier ES10.5.x to ES10.5.8-5 or later

### [REPLICATION REPLICA ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-master-admin)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Alias for [REPLICATION SLAVE ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave-admin)
* Capabilities changed in ES10.5.8-5 with the following abilities removed from REPLICATION SLAVE ADMIN and now granted with [REPLICA MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replica-monitor):
  * [SHOW SLAVE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status)
  * [SHOW REPLICA STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status)
  * [SHOW ALL SLAVES STATUS](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/show-all-slaves-status/README.md)
  * [SHOW ALL REPLICAS STATUS](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/show-all-replicas-status/README.md)
  * [SHOW RELAYLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-relaylog-events)
* Allows the user to execute [BINLOG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/binlog) statements, which are output by mariadb-binlog
* Allows the user to execute [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to) statements
* Allows the user to execute [START ALL REPLICAS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/start-replica#start-all-replicas) statements
* Allows the user to execute [START ALL SLAVES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/legacy-replication-statements/legacy-commands-start-slave) statements
* Allows the user to execute [START REPLICA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/start-replica) statements
* Allows the user to execute [START SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/start-replica) statements
* Allows the user to execute [STOP ALL REPLICAS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica) statements
* Allows the user to execute [STOP ALL SLAVES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica) statements
* Allows the user to execute [STOP REPLICA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica) statements
* Allows the user to execute [STOP SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica) statements
* Allows the user to set system variables:
  * [gtid\_cleanup\_batch\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_ignore\_duplicates](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_pos\_auto\_engines](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_slave\_pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_strict\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [init\_slave](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [relay\_log\_purge](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [relay\_log\_recovery](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_events\_marked\_for\_skip](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_do\_db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_do\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_ignore\_db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_ignore\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_wild\_do\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_wild\_ignore\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [read\_binlog\_speed\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_compressed\_protocol](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_ddl\_exec\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_domain\_parallel\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_exec\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_max\_allowed\_packet](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_net\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_parallel\_max\_queued](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_parallel\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_parallel\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_parallel\_workers](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_run\_triggers\_for\_rbr](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_sql\_verify\_checksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_transaction\_retry\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_type\_conversions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [sync\_master\_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [sync\_relay\_log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [sync\_relay\_log\_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)

### [REPLICATION SLAVE ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave-admin)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Alias for [REPLICATION REPLICA ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-replica-admin) see [REPLICATION REPLICA ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-replica-admin) for details

### [SET USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#set-user)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Allows the user to set the definer of views, triggers, stored procedures, stored functions, and events
* Allows the user to view the definer of an object, even if the user account no longer exists. |

### [SLAVE MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#slave-monitor)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* SLAVE MONITOR is a new privilege in ES10.5.8-5 and was not present in earlier releases
* SLAVE MONITOR can execute:
  * [SHOW SLAVE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status)
  * [SHOW REPLICA STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status)
  * [SHOW ALL SLAVES STATUS](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/show-all-slaves-status/README.md)
  * [SHOW ALL REPLICAS STATUS](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/show-all-replicas-status/README.md)
  * [SHOW RELAYLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-relaylog-events)
* If a user upgrades from ES10.4 or earlier to ES10.5.8-5 or later, any users with REPLICATION CLIENT or REPLICATION SLAVE privileges will automatically be granted the SLAVE MONITOR privilege. This privilege upgrade happens upon server startup, so mysql\_upgrade is not required.
* The upgrade behavior does not apply to minor release upgrades that upgrade from ES10.5.6-4 or earlier ES10.5.x to ES10.5.8-5 or later
* SLAVE MONITOR is an alias for REPLICA MONITOR which is also new in ES10.5.8-5

### [SUPER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#super)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| yes                | yes                    |

**Notes:**

* The SUPER privilege is present in ES10.4 and ES10.5 but the capabilities have changed. New privileges have been added in ES10.5 to provide finer grained control and reduce the need to grant SUPER privileges
* With the addition of the new privileges in ES10.5, SUPER:
  * no longer executes SHOW MASTER STATUS, SHOW BINLOG STATUS, and SHOW BINARY LOGS. Those require BINLOG MONITOR in ES10.5
  * no longer sets the definer for views, triggers, functions, procedures, and events in ES10.5. Those capabilities require SET USER in ES10.5
  * no longer ignores the read\_only system variable in ES10.5. That capability requires READ ONLY ADMIN in ES10.5
  * no longer kills threads owned by other users and bypass limits on connection and authentication failures. Those capabilities require CONNECTION ADMIN in ES10.5
  * no longer executes CREATE SERVER, ALTER SERVER, DROP SERVER in ES10.5. Those capabilities require FEDERATED ADMIN in ES10.5
  * no longer executes PURGE BINARY LOGS in ES10.5. PURGE BINARY LOGS requires BINLOG ADMIN in ES10.5.

## Privileges Comparison ES10.4 and ES10.5 before ES10.5.8-5

MariaDB Enterprise Server 10.5 adds privileges that allow operations that previously required the [SUPER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#super). The following table is a summary of the changes between MariaDB Enterprise Server 10.4 and MariaDB Enterprise Server 10.5 before MariaDB Enterprise Server 10.5.8-5. More specific detail is found in [MariaDB Replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication), and in [MariaDB Privileges Reference](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant).

### [BINLOG ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-admin)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Allows the user to execute [PURGE BINARY LOGS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/purge-binary-logs) statements
* Allows the user to [SET](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set) the following system variables:
  * [binlog\_annotate\_row\_events](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_commit\_wait\_count](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_commit\_wait\_usec](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_direct\_non\_transactional\_updates](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_file\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_row\_image](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_row\_metadata](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_stmt\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [expire\_logs\_days](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [log\_bin\_compress](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [log\_bin\_compress\_min\_len](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [log\_bin\_trust\_function\_creators](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [max\_binlog\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_binlog_cache_size)
  * [max\_binlog\_stmt\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_binlog_stmt_cache_size)
  * [max\_binlog\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_binlog_size)
  * [sql\_log\_bin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [sync\_binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)

### [BINLOG MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-monitor)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Legacy [grant/#replication-client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-client) privilege is an alias for this new privilege, but the capabilities have changed
* Unlike legacy REPLICATION CLIENT privilege, [BINLOG MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-monitor) can no longer execute SHOW SLAVE STATUS, SHOW REPLICA STATUS in ES10.5
* BINLOG MONITOR allows the user to execute [SHOW BINLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-events) statements
* BINLOG MONITOR allows the user to execute [SHOW BINLOG STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-status) statements
* BINLOG MONITOR allows the user to execute [SHOW BINARY LOGS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binary-logs) statements
* BINLOG MONITOR allows the user to execute [SHOW MASTER STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-status) statements
* If a user upgrades from ES10.4 or earlier to ES10.5.8-5 or later, any users with REPLICATION CLIENT or REPLICATION SLAVE privileges will automatically be granted the REPLICA MONITOR privilege. This privilege upgrade happens upon server startup, so mysql\_upgrade is not required
* The upgrade behavior does not apply to minor release upgrades that upgrade from ES10.5.6-4 or earlier ES10.5.x to ES10.5.8-5 or later

### [BINLOG REPLAY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-replay)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Allows the user to execute [BINLOG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/binlog) statements, which are output by [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog)
* Allows the user to execute [SET TIMESTAMP](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/set-timestamp/README.md) statements when [secure\_timestamp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#secure_timestamp) is set to replication
* Allows the user to set the session values of several system variables that are usually included in [BINLOG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/binlog) statements:
  * [gtid\_domain\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_seq\_no](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [pseudo\_thread\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#pseudo_thread_id)
  * [server\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)

### [CONNECTION ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#connection-admi)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Skips the execution of init\_connect when the user connects
* Ignores max\_connections when the user connects
* Ignores max\_user\_connections when the user connects
* Ignores max\_password\_errors when the user connects
* Allows the user to kill connections owned by other users with the KILL statement
* Allows the user to set system variables:
  * [connect\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#connect_timeout)
  * [disconnect\_on\_expired\_password](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#disconnect_on_expired_password)
  * [extra\_max\_connections](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#extra_max_connections)
  * [init\_connect](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#init_connect)
  * [max\_connections](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_connections)
  * [max\_connect\_errors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_connect_errors)
  * [max\_password\_errors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_password_errors)
  * [proxy\_protocol\_networks](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#proxy_protocol_networks)
  * [secure\_auth](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#secure_auth)
  * [slow\_launch\_time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#slow_launch_time)
  * [thread\_pool\_exact\_stats](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_dedicated\_listener](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_idle\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_max\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_min\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_oversubscribe](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_prio\_kickup\_timer](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_priority](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_stall\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)

### [FEDERATED ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#federated-admin)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Allows the user to execute [CREATE SERVER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-server) statements
* Allows the user to execute [ALTER SERVER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-server) statements
* Allows the user to execute [DROP SERVER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-server) statements

### [READ\_ONLY ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#readonly-admin)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Allows the user to write data even if the [read\_only](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#read_only) system variable is enabled
* Allows the user to execute [DROP TRIGGER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-trigger) statements even if the [read\_only](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#read_only) system variable is enabled
* Allows the user to execute [START TRANSACTION READ WRITE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/start-transaction) statements even if the [read\_only](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#read_only) system variable is enabled
* Allows the user to set system variables:[read\_only](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#read_only)

### [REPLICATION CLIENT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-client)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| yes                | no                     |

**Notes:**

* Replaced by [BINLOG MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-monitor) in 10.5
* REPLICATION CLIENT can be used as an alias for BINLOG MONITOR but the capabilities for BINLOG MONITOR are different than those of legacy REPLICATION CLIENT
* Unlike legacy REPLICATION CLIENT privilege, [BINLOG MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-monitor) can no longer execute SHOW SLAVE STATUS, SHOW REPLICA STATUS in ES10.5
* REPLICATION CLIENT as an alias for BINLOG MONITOR:
  * Allows the user to execute [SHOW BINLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-events) statements
  * Allows the user to execute [SHOW BINLOG STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-status) statements
  * Allows the user to execute [SHOW BINARY LOGS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binary-logs) statements
  * Allows the user to execute [SHOW MASTER STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-status) statements
  * If a user upgrades from ES10.4 or earlier to ES10.5.8-5 or later, any users with REPLICATION CLIENT or REPLICATION SLAVE privileges will automatically be granted the REPLICA MONITOR privilege. This privilege upgrade happens upon server startup, so mysql\_upgrade is not required
  * The upgrade behavior does not apply to minor release upgrades that upgrade from ES10.5.6-4 or earlier ES10.5.x to ES10.5.8-5 or later

### [REPLICATION MASTER ADMIN](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/replication-master-admin/README.md)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Allows the user to execute [SHOW REPLICA HOSTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-hosts) statements
* Allows the user to execute [SHOW SLAVE HOSTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-hosts) statements
* Allows the user to set system variables:
  * [gtid\_binlog\_state](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_domain\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [master\_verify\_checksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [server\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)

### [REPLICATION REPLICA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-replica)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Added in ES10.5 as an alias for [REPLICATION SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave)

### [REPLICATION SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| yes                | yes                    |

**Notes:**

* Can be used as an alias for [REPLICATION REPLICA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-replica)
* In ES10.5 REPLICATION SLAVE can no longer execute SHOW RELAYLOG EVENTS. In ES10.5 versions earlier than ES10.5.8-5, SHOW RELAYLOG EVENTS requires [REPLICATION REPLICA ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-replica-admin). In ES10.5.8-5, SHOW RELAYLOG EVENTS requires [REPLICA MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replica-monitor)
* In ES10.5 REPLICATION SLAVE can no longer execute [SHOW BINLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-events). SHOW BINLOG EVENTS requires [BINLOG MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-monitor)
* If a user upgrades from ES10.4 or earlier to ES10.5.8-5 or later, any users with REPLICATION CLIENT or REPLICATION SLAVE privileges will automatically be granted the REPLICA MONITOR privilege. This privilege upgrade happens upon server startup, so mysql\_upgrade is not required
* The upgrade behavior does not apply to minor release upgrades that upgrade from ES10.5.6-4 or earlier ES10.5.x to ES10.5.8-5 or later

### [REPLICATION REPLICA ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-replica-admin)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Alias for REPLICATION SLAVE ADMIN
* Capabilities changed in ES10.5.8-5 with the following abilities removed from REPLICATION SLAVE ADMIN and now granted with [REPLICA MONITOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replica-monitor):
  * [SHOW SLAVE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status)
  * [SHOW REPLICA STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status)
  * [SHOW ALL SLAVES STATUS](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/show-all-slaves-status/README.md)
  * [SHOW ALL REPLICAS STATUS](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/show-all-replicas-status/README.md)
  * [SHOW RELAYLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-relaylog-events)
* Allows the user to execute [BINLOG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/binlog) statements, which are output by [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog)
* Allows the user to execute CHANGE MASTER TO statements
* Allows the user to execute START ALL REPLICAS statements
* Allows the user to execute START ALL SLAVES statements
* Allows the user to execute START REPLICA statements
* Allows the user to execute START SLAVE statements
* Allows the user to execute STOP ALL REPLICAS statements
* Allows the user to execute STOP ALL SLAVES statements
* Allows the user to execute STOP REPLICA statements
* Allows the user to execute STOP SLAVE statements
* Allows the user to set system variables:
  * [gtid\_cleanup\_batch\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_ignore\_duplicates](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_pos\_auto\_engines](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_slave\_pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_strict\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [init\_slave](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [relay\_log\_purge](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [relay\_log\_recovery](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_events\_marked\_for\_skip](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_do\_db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_do\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_ignore\_db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_ignore\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_wild\_do\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_wild\_ignore\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [read\_binlog\_speed\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_compressed\_protocol](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_ddl\_exec\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_domain\_parallel\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_exec\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_max\_allowed\_packet](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_net\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_parallel\_max\_queued](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_parallel\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_parallel\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_parallel\_workers](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_run\_triggers\_for\_rbr](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_sql\_verify\_checksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_transaction\_retry\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_type\_conversions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [sync\_master\_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [sync\_relay\_log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [sync\_relay\_log\_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)

### [REPLICATION SLAVE ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-slave-admin)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Alias for [REPLICATION REPLICA ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-replica-admin) see [REPLICATION REPLICA ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#replication-replica-admin) for details

### [SET USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#set-user)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| no                 | yes                    |

**Notes:**

* Allows the user to set the definer of views, triggers, stored procedures, stored functions, and events
* Allows the user to view the definer of an object, even if the user account no longer exists.

### [SUPER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#super)

| Present in ES10.4? | Present in ES10.5.8-5? |
| ------------------ | ---------------------- |
| yes                | yes                    |

**Notes:**

* The SUPER privilege is present in ES10.4 and ES10.5 but the capabilities have changed. New privileges have been added in ES10.5 to provide finer grained control and reduce the need to grant SUPER privileges
* With the addition of the new privileges in ES10.5, SUPER:
  * no longer executes SHOW MASTER STATUS, SHOW BINLOG STATUS, and SHOW BINARY LOGS. Those require BINLOG MONITOR in ES10.5
  * no longer sets the definer for views, triggers, functions, procedures, and events in ES10.5. Those capabilities require SET USER in ES10.5
  * no longer ignores the read\_only system variable in ES10.5. That capability requires READ ONLY ADMIN in ES10.5
  * no longer kills threads owned by other users and bypass limits on connection and authentication failures. Those capabilities require CONNECTION ADMIN in ES10.5
  * no longer executes CREATE SERVER, ALTER SERVER, DROP SERVER in ES10.5. Those capabilities require FEDERATED ADMIN in ES10.5
  * no longer executes PURGE BINARY LOGS in ES10.5. PURGE BINARY LOGS requires BINLOG ADMIN in ES10.5

## MariaDB Replication

MariaDB Enterprise Server 10.5 improves [MariaDB Replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication):

* It allows extended table metadata to be written to the binary log by configuring the [binlog\_row\_metadata](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) system variable.
* It changes the default parallel replication mode from `conservative` to `optimistic`.
* It renames the `REPLICATION CLIENT` privilege to `BINLOG MONITOR`, but it still supports the old name.
* It allows replication-related operations that previously required the `SUPER` privilege to the `BINLOG MONITOR` (formerly `REPLICATION CLIENT`):

### BINLOG MONITOR (formerly REPLICATION CLIENT)

**Newly Granted Operations:**

* Allows the user to execute [SHOW BINLOG STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-status) statements
* Allows the user to execute [SHOW BINLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-events) statements
* Allows the user to execute [SHOW BINARY LOGS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binary-logs) statements
* Allows the user to execute [SHOW MASTER STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-status) statements
* It adds new replication-related privileges to allow operations that previously required the `SUPER` privilege:

### BINLOG ADMIN

\*\* Granted Operations:\*\*

* Allows the user to execute PURGE BINARY LOGS statements
* Allows the user to set system variables:
  * [binlog\_annotate\_row\_events](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_commit\_wait\_count](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_commit\_wait\_usec](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_direct\_non\_transactional\_updates](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_file\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_row\_image](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_row\_metadata](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_stmt\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [expire\_logs\_days](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [log\_bin\_compress](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [log\_bin\_compress\_min\_len](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [log\_bin\_trust\_function\_creators](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [max\_binlog\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_binlog_cache_size)
  * [max\_binlog\_stmt\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_binlog_stmt_cache_size)
  * [max\_binlog\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_binlog_size)
  * [sql\_log\_bin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [sync\_binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)

### BINLOG REPLAY

**Granted Operations:**

* Allows the user to execute [BINLOG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/binlog) statements, which are output by [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog)
* Allows the user to execute [SET TIMESTAMP](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/set-timestamp/README.md) statements when [secure\_timestamp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#secure_timestamp) is set to replication
* Allows the user to set the session values of several system variables that are usually included in [BINLOG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/binlog) statements:
  * [gtid\_domain\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_seq\_no](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [pseudo\_thread\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#pseudo_thread_id)
  * [server\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)

### REPLICATION MASTER ADMIN

**Granted Operations:**

* Allows the user to execute SHOW REPLICA HOSTS statements
* Allows the user to execute SHOW SLAVE HOSTS statements
* Allows the user to set system variables:
  * [gtid\_binlog\_state](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_domain\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [master\_verify\_checksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [server\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)

### REPLICATION SLAVE ADMIN

**Granted Operations:**

* Allows the user to execute [BINLOG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/binlog) statements, which are output by [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog)
* Allows the user to execute [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to) statements
* Allows the user to execute [SHOW ALL REPLICAS STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status) statements
* Allows the user to execute [SHOW ALL SLAVES STATUS](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/show-all-slaves-status/README.md) statements
* Allows the user to execute SHOW RELAYLOG EVENTS statements
* Allows the user to execute SHOW REPLICA STATUS statements
* Allows the user to execute SHOW SLAVE STATUS statements
* Allows the user to execute START ALL REPLICAS statements
* Allows the user to execute START ALL SLAVES statements
* Allows the user to execute START REPLICA statements
* Allows the user to execute START SLAVE statements
* Allows the user to execute STOP ALL REPLICAS statements
* Allows the user to execute STOP ALL SLAVES statements
* Allows the user to execute STOP REPLICA statements
* Allows the user to execute STOP SLAVE statements
* Allows the user to set system variables:
  * [gtid\_cleanup\_batch\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_ignore\_duplicates](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_pos\_auto\_engines](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_slave\_pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_strict\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [init\_slave](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [relay\_log\_purge](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [relay\_log\_recovery](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_events\_marked\_for\_skip](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_do\_db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_do\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_ignore\_db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_ignore\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_wild\_do\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_wild\_ignore\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [read\_binlog\_speed\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_compressed\_protocol](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_ddl\_exec\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_domain\_parallel\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_exec\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_max\_allowed\_packet](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_net\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_parallel\_max\_queued](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_parallel\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_parallel\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_parallel\_workers](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_run\_triggers\_for\_rbr](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_sql\_verify\_checksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_transaction\_retry\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_type\_conversions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [sync\_master\_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [sync\_relay\_log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [sync\_relay\_log\_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)

## Statement Aliases

* It adds aliases for statements that contain the word `SLAVE` that also allow the word `REPLICA`:

| Statement                                                                                                                                                                                             | New Statement Alias                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [START SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/start-replica)                                             | [START REPLICA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/start-replica)                                               |
| [START ALL SLAVES](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/start-all-slaves/README.md)             | [START ALL REPLICAS](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/start-all-replicas/README.md)             |
| [STOP SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica)                                               | [STOP REPLICA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica)                                                 |
| [STOP ALL SLAVES](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/stop-all-slaves/README.md)               | [STOP ALL REPLICAS](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/stop-all-replicas/README.md)               |
| [SHOW SLAVE STATUS](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/show-all-slaves-status/README.md)      | [SHOW REPLICA STATUS](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/show-all-replicas-status/README.md)      |
| [SHOW ALL SLAVES STATUS](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/show-all-slaves-status/README.md) | [SHOW ALL REPLICAS STATUS](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/show-all-replicas-status/README.md) |
| [RESET SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/reset-replica)                                             | [RESET REPLICA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/reset-replica)                                               |
| [SHOW SLAVE HOSTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-hosts)                                                     | [SHOW REPLICA HOSTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-hosts)                                                       |

* It adds the shutdown\_wait\_for\_slaves system variable to control whether a replication-aware shutdown is the default shutdown behavior.

## MariaDB Enterprise Cluster

MariaDB Enterprise Server 10.5 improves support for [Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md):

* It allows Galera Cluster to be configured to prohibit DDL replication to only the storage engines that support Galera Cluster by configuring the [wsrep\_strict\_ddl](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_strict_ddl) system variable.
* It adds full GTID support to Galera Cluster.
* It adds an inconsistency voting protocol to mitigate the harm of inconsistencies by choosing very carefully which inconsistent nodes need to abort.
* It adds support for [non-blocking operations](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/enterprise-server/10-5/broken-reference/README.md) when [wsrep\_OSU\_method](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_osu_method) is set to NBO, including:
  * [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) operations executed in `SHARED` or `EXCLUSIVE` locking mode.
  * [CREATE INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-index) operations executed in `SHARED` or `EXCLUSIVE` locking mode.
  * [DROP INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-index) operations.
  * [OPTIMIZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table) operations.
* It adds a "black box" for Galera troubleshooting. The black box holds debug log messages in memory, which can be analyzed in case of a crash.
* The default value for `gcache.size` in [wsrep\_provider\_options](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_provider_options) has been changed to 1 GB.

## Temporal Data

MariaDB Enterprise Server 10.5 improves support for [Temporal Data Tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables):

* It allows [system-versioned tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables) that are partitioned on an interval of SYSTEM\_TIME to be configured with a specific start date and time, which can make partition management more user-friendly.
* It allows [application-time period tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/application-time-periods) to be configured to prohibit overlapping time periods.

## SQL Functionality

MariaDB Enterprise Server 10.5 improves SQL functionality in several areas:

* It changes the behavior of the [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table) statement to forcefully drop the table, even if the storage engine can't find the table.
* It changes the behavior of the [ANALYZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/analyze-table) statement, so that it no longer flushes the table definition cache, so that it performs better under concurrency.
* It changes the behavior of the [ANALYZE](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/ANALYZE/README.md) statement to SHOW the time spent checking the WHERE clause.
* It adds support for [INSERT ... RETURNING](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) statements.
* It adds support for [REPLACE ... RETURNING](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/replace) statements.
* It adds support for the `EXCEPT ALL` clause in [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statements.
* It adds support for the `INTERSECT ALL` clause in [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statements.
* It adds support for the `CYCLE` clause in common table expressions (CTEs).
* It adds support for `COMMENT` option for [CREATE DATABASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-database) and [ALTER DATABASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-database) statements.
* It adds support for [ALTER TABLE IF EXISTS ....](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table)
* It adds support for [ALTER TABLE ... RENAME INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table).
* It adds support for [ALTER TABLE ... RENAME COLUMN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table).
* It adds support for defining foreign keys using `REFERENCE` clauses in column definitions.
* It adds support for the `VISIBLE` option in index definitions, which can be needed to import dumps from MySQL.
* It adds support for the `WITHOUT OVERLAP` option in index definitions that are defined for [application-time period tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/application-time-periods).
* It adds support for the `STARTS` option for system-versioned tables that are partitioned on an interval of `SYSTEM_TIME`.
* It adds support for the [JSON\_ARRAYAGG()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_arrayagg) function.
* It adds support for the [JSON\_OBJECTAGG()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_objectagg) function.
* It adds support for the `RELEASE_ALL_LOCKS()` function.
* It adds support for the [OVERLAPS()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/geometry-relations/overlaps) function.
* It adds support for a new Data Type API, so that plugins can define custom data types.
* It adds support for the [INET6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/inet6) data type, which can be used to represent IPv4 and IPv6 addresses.
* It changes the way that [TIMESTAMP](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/timestamp), [DATETIME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/datetime), and [TIME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/time) columns that use the pre-[MariaDB 10.0](../../../community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) format are displayed in the output of [SHOW CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-table) and [DESCRIBE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/describe) and in the value of the [information\_schema.COLUMNS.COLUMN\_TYPE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema) column. Columns using the older format will have a comment that says `/* mariadb-5.3 */`.

## Security

MariaDB Enterprise Server 10.5 includes several [security](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security) improvements:

* It allows a server to be configured to [require secure connections](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview) by configuring the [require\_secure\_transport](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#require_secure_transport) system variable.
  * If this mode is enabled, then all TCP connections must use TLS.
  * Local connections that connect using a Unix socket or a named pipe are also allowed.
* It adds the `CONNECTION_TYPE` column to the [performance\_schema.threads table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables), which can be used to determine which connections are using TLS.
* It renames the `REPLICATION CLIENT` privilege to `BINLOG MONITOR`, but it still supports the old name.
* It allows replication-related operations that previously required the `SUPER` privilege to the `BINLOG MONITOR` (formerly `REPLICATION CLIENT`):

### BINLOG MONITOR (formerly REPLICATION CLIENT)

**Newly Granted Operations:**

* Allows the user to execute [SHOW BINLOG STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-status) statements
* Allows the user to execute [SHOW BINARY LOGS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binary-logs) statements
* Allows the user to execute [SHOW MASTER STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-binlog-status) statements
* It adds new privileges to allow operations that previously required the `SUPER` privilege.

### [BINLOG ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-admin)

**Granted Operations:**

* Allows the user to execute [PURGE BINARY LOGS](broken-reference) statements
* Allows the user to set system variables:
  * [binlog\_annotate\_row\_events](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_commit\_wait\_count](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_commit\_wait\_usec](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_direct\_non\_transactional\_updates](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_file\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_row\_image](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_row\_metadata](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [binlog\_stmt\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [expire\_logs\_days](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [log\_bin\_compress](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [log\_bin\_compress\_min\_len](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [log\_bin\_trust\_function\_creators](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [max\_binlog\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_binlog_cache_size)
  * [max\_binlog\_stmt\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_binlog_stmt_cache_size)
  * [max\_binlog\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_binlog_size)
  * [sql\_log\_bin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [sync\_binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)

### [BINLOG REPLAY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#binlog-replay)

**Granted Operations:**

* Allows the user to execute BINLOG statements, which are output by mariadb-binlog
* Allows the user to execute SET TIMESTAMP statements when secure\_timestamp is set to replication
* Allows the user to set the session values of several system variables that are usually included in BINLOG statements:
  * [gtid\_domain\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_seq\_no](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [pseudo\_thread\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#pseudo_thread_id)
  * [server\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)

### CONNECTION ADMIN

**Granted Operations:**

* Skips the execution of init\_connect when the user connects
* Ignores max\_connections when the user connects
* Ignores max\_user\_connections when the user connects
* Ignores max\_password\_errors when the user connects
* Allows the user to kill connections owned by other users with the KILL statement
* Allows the user to set system variables:
  * [connect\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#connect_timeout)
  * [disconnect\_on\_expired\_password](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#disconnect_on_expired_password)
  * [extra\_max\_connections](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#extra_max_connections)
  * [init\_connect](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#init_connect)
  * [max\_connections](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_connections)
  * [max\_connect\_errors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_connect_errors)
  * [max\_password\_errors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_password_errors)
  * [proxy\_protocol\_networks](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#proxy_protocol_networks)
  * [secure\_auth](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#secure_auth)
  * [slow\_launch\_time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#slow_launch_time)
  * [thread\_pool\_exact\_stats](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_dedicated\_listener](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_idle\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_max\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_min\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_oversubscribe](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_prio\_kickup\_timer](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_priority](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)
  * [thread\_pool\_stall\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables) |

### FEDERATED ADMIN

**Granted Operations:**

* Allows the user to execute [CREATE SERVER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-server) statements
* Allows the user to execute [ALTER SERVER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-server) statements
* Allows the user to execute [DROP SERVER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-server) statements

### READ ONLY ADMIN

**Granted Operations:**

* Allows the user to write data even if the [read\_only](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#read_only) system variable is enabled
* Allows the user to execute DROP TRIGGER statements even if the [read\_only](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#read_only) system variable is enabled
* Allows the user to execute START TRANSACTION READ WRITE statements even if the [read\_only](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#read_only) system variable is enabled
* Allows the user to set system variables:
  * [read\_only](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#read_only)

### REPLICATION MASTER ADMIN

**Granted Operations:**

* Allows the user to execute [SHOW REPLICA HOSTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-hosts) statements
* Allows the user to execute [SHOW SLAVE HOSTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-hosts) statements
* Allows the user to set system variables:
  * [gtid\_binlog\_state](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_domain\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [master\_verify\_checksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [server\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)

### REPLICATION SLAVE ADMIN

**Granted Operations:**

* Allows the user to execute [BINLOG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/binlog) statements, which are output by [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog)
* Allows the user to execute [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to) statements
* Allows the user to execute [SHOW ALL REPLICAS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status)\
  STATUS statements
* Allows the user to execute [SHOW ALL SLAVES STATUS](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/show-all-slaves-status/README.md) statements
* Allows the user to execute [SHOW RELAYLOG EVENTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-relaylog-events) statements
* Allows the user to execute [SHOW REPLICA STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status) statements
* Allows the user to execute [SHOW SLAVE STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status) statements
* Allows the user to execute [START ALL REPLICAS](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/start-all-replicas/README.md) statements
* Allows the user to execute [START ALL SLAVES](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/start-all-slaves/README.md) statements
* Allows the user to execute [START REPLICA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/start-replica) statements
* Allows the user to execute START SLAVE statements
* Allows the user to execute [STOP ALL REPLICAS](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/stop-all-replicas/README.md) statements
* Allows the user to execute [STOP ALL SLAVES](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-enterprise-server-release-notes/mariadb-enterprise-server-10-5/stop-all-slaves/README.md) statements
* Alows the user to execute [STOP REPLICA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica) statements
* Allows the user to execute [STOP SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/stop-replica) statements
* Allows the user to set system variables:
  * [gtid\_cleanup\_batch\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_ignore\_duplicates](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_pos\_auto\_engines](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_slave\_pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [gtid\_strict\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
  * [init\_slave](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [relay\_log\_purge](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [relay\_log\_recovery](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_events\_marked\_for\_skip](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_do\_db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_do\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_ignore\_db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_ignore\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_wild\_do\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [replicate\_wild\_ignore\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [read\_binlog\_speed\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_compressed\_protocol](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_ddl\_exec\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_domain\_parallel\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_exec\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_max\_allowed\_packet](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_net\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_parallel\_max\_queued](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_parallel\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_parallel\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_parallel\_workers](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_run\_triggers\_for\_rbr](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_sql\_verify\_checksum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_transaction\_retry\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [slave\_type\_conversions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [sync\_master\_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [sync\_relay\_log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
  * [sync\_relay\_log\_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)

### SET USER

**Granted Operations:**

* Allows the user to set the definer of views, triggers, stored procedures, stored functions, and events.○ Allows the user to view the definer of an object, even if the user account no longer exists

## HashiCorp Vault Encryption Plugin

MariaDB Enterprise Server 10.5 introduces an encryption plugin to support for [HashiCorp Vault](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/automated-mariadb-deployment-and-administration/hashicorp-vault-and-mariadb):

* It allows HashiCorp Vault to manage encryption keys for [data-at-rest encryption](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption).
* It communicates with the remote KMS using TLS.
* It supports key rotation.

## Performance Schema

MariaDB Enterprise Server 10.5 includes several [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) improvements:

* It adds support for some of the instrumentation and tables included in MySQL 5.7.
* It adds the `CONNECTION_TYPE` column to the threads table, which can be used to determine which connections are using TLS.
* It adds new instrumentation for the following:
  * Memory
  * Metadata locks
  * Prepared statements
  * Stored procedures
  * Transactions
  * SX-Locks
  * Status variables
  * User variables
* It adds the following new tables:
  * [events\_statements\_summary\_by\_program](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-events_statements_summary_by_program-table)
  * [events\_transactions\_current](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-events_transactions_current-table)
  * [events\_transactions\_history](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-events_transactions_history-table)
  * [events\_transactions\_history\_long](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-events_transactions_history_long-table)
  * [events\_transactions\_summary\_by\_account\_by\_event\_name](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-events_transactions_summary_by_account_by_event_name-tab)
  * [events\_transactions\_summary\_by\_host\_by\_event\_name](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-events_transactions_summary_by_host_by_event_name-table)
  * [events\_transactions\_summary\_by\_thread\_by\_event\_name](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-events_transactions_summary_by_thread_by_event_name-tabl)
  * [events\_transactions\_summary\_by\_user\_by\_event\_name](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-events_transactions_summary_by_user_by_event_name-table)
  * [events\_transactions\_summary\_global\_by\_event\_name](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-events_transactions_summary_global_by_event_name-table)
  * [global\_status](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-global_status-table)
  * [global\_variables](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-global_status-tablee)
  * [memory\_summary\_by\_account\_by\_event\_name](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-memory_summary_by_account_by_event_name-table)
  * [memory\_summary\_by\_host\_by\_event\_name](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-memory_summary_by_host_by_event_name-table)
  * [memory\_summary\_by\_thread\_by\_event\_name](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-memory_summary_by_thread_by_event_name-table)
  * [memory\_summary\_by\_user\_by\_event\_name](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-memory_summary_by_user_by_event_name-table)
  * [memory\_summary\_global\_by\_event\_name](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-memory_summary_global_by_event_name-table)
  * [metadata\_locks](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-metadata_locks-table)
  * [prepared\_statements\_instances](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-prepared_statements_instances-table)
  * [replication\_applier\_configuration](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-replication_applier_configuration-table)
  * [replication\_applier\_status](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-replication_applier_status-table)
  * [replication\_applier\_status\_by\_coordinator](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-replication_applier_status_by_coordinator-table)
  * [replication\_applier\_status\_by\_worker](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-replication_applier_status_by_worker-table)
  * [replication\_connection\_configuration](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-replication_connection_configuration-table)
  * [session\_status](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-session_status-table)
  * \[session\_variables]\(https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-tables/performance-schema-session\_status-table
  * [status\_by\_account](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-status_by_account-table)
  * [status\_by\_host](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-status_by_host-table)
  * [status\_by\_thread](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-status_by_thread-table)
  * [status\_by\_user](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-status_by_user-table)
  * [table\_handles](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-table_handles-table)
  * [user\_variables\_by\_thread](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-user_variables_by_thread-table)
  * [variables\_by\_thread](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-user_variables_by_thread-table)

## Information Schema

MariaDB Enterprise Server 10.5 includes several [Information Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema) improvements:

* It adds the `GLOBAL_VALUE_PATH` column to the [information\_schema.SYSTEM\_VARIABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-system_variables-table) table, which can be used to determine which configuration file a variable's global value was read from.
* It adds new tables to monitor the internals of the thread pool on Linux:
  * [THREAD\_POOL\_GROUPS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_groups-table)
  * [THREAD\_POOL\_QUEUES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_queues-table)
  * [THREAD\_POOL\_STATS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_stats-table)
  * [THREAD\_POOL\_WAITS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_waits-table)
* It removes the [information\_schema.INNODB\_TABLESPACES\_SCRUBBING](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_tablespaces_scrubbing-table) table.
* It changes some other InnoDB-related [Information Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema) tables in minor ways.

## Thread Pool

MariaDB Enterprise Server 10.5 includes several thread pool improvements:

* It improves how it calculates the number of currently active threads, which can help prevent deadlocks.
* It improves performance under very bursty workloads by basing the thread creation rate and the throttling interval on the values of the [thread\_pool\_stall\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables) and [thread\_pool\_oversubscribe](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables) system variables.
* It adds new [Information Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema) tables to monitor the internals of the thread pool on Linux:
  * [THREAD\_POOL\_GROUPS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_groups-table)
  * [THREAD\_POOL\_QUEUES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_queues-table)
  * [THREAD\_POOL\_STATS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_stats-table)
  * [THREAD\_POOL\_WAITS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-thread_pool_waits-table)

## Protocol

MariaDB Enterprise Server 10.5 includes several protocol improvements:

* It adds protocol support for the new Data Type API.
* It adds protocol support for the [JSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/json) data type.
* It adds protocol support for the [GEOMETRY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/geometry/geometry-types) data type.

## XA Transactions

MariaDB Enterprise Server 10.5 includes some XA transaction improvements:

* It allows prepared XA transactions to be properly recovered after a client disconnects.

## Internals

MariaDB Enterprise Server 10.5 includes some internal improvements:

* Its internal regular expression library has been upgraded from PCRE to PCRE2.
* It adds support for a new Data Type API, so that plugins can define custom data types.

For a complete list of changes, see [MariaDB Enterprise Server 10.5.4-2 release notes](release-notes-for-mariadb-enterprise-server-10-5-4-2.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
