# Server Status Variables

{% include "../../../.gitbook/includes/for-a-full-list-of-server-v....md" %}

Most status variables are described on this page, but some are described elsewhere:

* [Aria Status Variables](../../../server-usage/storage-engines/aria/aria-status-variables.md)
* [Galera Status Variables](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables)
* [InnoDB Status Variables](innodb-status-variables.md)
* [Mroonga Status Variables](../../../server-usage/storage-engines/mroonga/mroonga-status-variables.md)
* [MyRocks Status Variables](../../../server-usage/storage-engines/myrocks/myrocks-status-variables.md)
* [Performance Scheme Status Variables](../../../reference/sql-statements/administrative-sql-statements/system-tables/performance-schema/performance-schema-status-variables.md)
* [Replication and Binary Log Status Variables](../../standard-replication/replication-and-binary-log-status-variables.md)
* [S3 Storage Engine Status Variables](../../../server-usage/storage-engines/s3-storage-engine/s3-storage-engine-status-variables.md)
* [Server\_Audit Status Variables](../../../reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-status-variables.md)
* [Sphinx Status Variables](sphinx-status-variables.md)
* [Spider Status Variables](spider-status-variables.md)
* [TokuDB Status Variables](../../../server-usage/storage-engines/tokudb/tokudb-status-variables.md)

Use the [SHOW STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-status.md) statement to view status variables. This\
information also can be obtained using the [mariadb-admin extended-status](../../../clients-and-utilities/administrative-tools/mariadb-admin.md) command, or by querying the [Information Schema GLOBAL\_STATUS and SESSION\_STATUS](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/information-schema-global_status-and-session_status-tables.md) tables.

Issuing a [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) will reset many status variables to zero.

## List of Server Status Variables

#### `Aborted_clients`

* Description: Number of aborted client connections. This can be due to the client not calling mysql\_close() before exiting, the client sleeping without issuing a request to the server for more seconds than specified by [wait\_timeout](server-system-variables.md#wait_timeout) or [interactive\_timeout](server-system-variables.md#interactive_timeout), or by the client program ending in the midst of transferring data. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md#flush-status).
* Scope: Global
* Data Type: `numeric`

#### `Aborted_connects`

* Description: Number of failed server connection attempts. This can be due to a client using an incorrect password, a client not having privileges to connect to a database, a connection packet not containing the correct information, or if it takes more than [connect\_timeout](server-system-variables.md#connect_timeout) seconds to get a connect packet. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md#flush-status).
* Scope: Global
* Data Type: `numeric`

#### `Aborted_connects_preauth`

* Description: Number of connection attempts that were aborted prior to authentication (regardless of whether or not an error occured).
* Scope: Global
* Data Type: `numeric`

#### `Access_denied_errors`

* Description: Number of access denied errors. For details on when this is incremented, see [Incrementing of the access\_denied\_errors status variable](../../../security/user-account-management/incrementing-of-the-access_denied_errors-status-variable.md).
* Scope: Global
* Data Type: `numeric`

#### `Acl_column_grants`

* Description: Number of column permissions granted (rows in the [mysql.columns\_priv table](../../../reference/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-columns_priv-table.md)).
* Scope: Global
* Data Type: `numeric`

#### `Acl_database_grants`

* Description: Number of database permissions granted (rows in the [mysql.db table](../../../reference/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-db-table.md)).
* Scope: Global
* Data Type: `numeric`

#### `Acl_function_grants`

* Description: Number of function permissions granted (rows in the [mysql.procs\_priv table](../../../reference/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-procs_priv-table.md) with a routine type of `FUNCTION`).
* Scope: Global
* Data Type: `numeric`

#### `Acl_package_body_grants`

* Description:
* Scope: Global
* Data Type: `numeric`

#### `Acl_package_spec_grants`

* Description:
* Scope: Global
* Data Type: `numeric`

#### `Acl_procedure_grants`

* Description: Number of procedure permissions granted (rows in the [mysql.procs\_priv table](../../../reference/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-procs_priv-table.md) with a routine type of `PROCEDURE`).
* Scope: Global
* Data Type: `numeric`

#### `Acl_proxy_users`

* Description: Number of proxy permissions granted (rows in the [mysql.proxies\_priv table](../../../reference/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-proxies_priv-table.md)).
* Scope: Global
* Data Type: `numeric`

#### `Acl_role_grants`

* Description: Number of role permissions granted (rows in the [mysql.roles\_mapping table](../../../reference/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-roles_mapping-table.md)).
* Scope: Global
* Data Type: `numeric`

#### `Acl_roles`

* Description: Number of roles (rows in the [mysql.user table](../../../reference/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-user-table.md) where `is_role='Y'`).
* Scope: Global
* Data Type: `numeric`

#### `Acl_table_grants`

* Description: Number of table permissions granted (rows in the [mysql.tables\_priv table](../../../reference/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-tables_priv-table.md)).
* Scope: Global
* Data Type: `numeric`

#### `Acl_users`

* Description: Number of users (rows in the [mysql.user table](../../../reference/sql-statements/administrative-sql-statements/system-tables/the-mysql-database-tables/mysql-user-table.md) where `is_role='N'`).
* Scope: Global
* Data Type: `numeric`

#### `Busy_time`

* Description: Cumulative time in seconds of activity on connections. Part of [User Statistics](../query-optimizations/statistics-for-optimizing-queries/user-statistics.md). Requires the [userstat](../query-optimizations/statistics-for-optimizing-queries/user-statistics.md#userstat) system variable to be set in order to be recorded.
* Scope: Global
* Data Type: `numeric`

#### `Bytes_received`

* Description: Total bytes received from all clients.
* Scope: Global
* Data Type: `numeric`

#### `Bytes_sent`

* Description: Total bytes sent to all clients.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_admin_commands`

* Description: Number of admin commands executed. These include table dumps, change users, binary log dumps, shutdowns, pings and debugs.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_alter_db`

* Description: Number of [ALTER DATABASE](../../../reference/sql-statements/data-definition/alter/alter-database.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_alter_db_upgrade`

* Description: Number of [ALTER DATABASE ... UPGRADE](../../../reference/sql-statements/data-definition/alter/alter-database.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_alter_event`

* Description: Number of [ALTER EVENT](../../../server-usage/triggers-events/event-scheduler/alter-event.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_alter_function`

* Description: Number of [ALTER FUNCTION](../../../reference/sql-statements/data-definition/alter/alter-function.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_alter_procedure`

* Description: Number of [ALTER PROCEDURE](../../../server-usage/stored-routines/stored-procedures/alter-procedure.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_alter_sequence`

* Description: Number of [ALTER SEQUENCE](../../../reference/sql-structure/sequences/alter-sequence.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_alter_server`

* Description: Number of [ALTER SERVER](../../../reference/sql-statements/data-definition/alter/alter-server.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_alter_table`

* Description: Number of [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_alter_tablespace`

* Description: Number of [ALTER TABLESPACE](../../../reference/sql-statements/data-definition/alter/alter-tablespace.md) commands executed (unsupported by MariaDB).
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 10.7.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1070-release-notes)

#### `Com_alter_user`

* Description: Number of [ALTER USER](../../../reference/sql-statements/account-management-sql-statements/alter-user.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_analyze`

* Description: Number of [ANALYZE](../../../reference/sql-statements/table-statements/analyze-table.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_assign_to_keycache`

* Description: Number of assign to keycache commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_backup`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 10.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1041-release-notes)

#### `Com_backup_lock`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 10.4.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1042-release-notes)

#### `Com_backup_table`

* Description: Removed in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5). In older versions, Com\_backup\_table contains the number of [BACKUP TABLE](../../../reference/sql-statements/table-statements/obsolete-table-commands/backup-table-removed.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

#### `Com_begin`

* Description: Number of [BEGIN](../../../reference/sql-statements/programmatic-compound-statements/begin-end.md) or [START TRANSACTION](../../../reference/sql-statements/transactions/start-transaction.md) statements executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_binlog`

* Description: Number of [BINLOG](../../../reference/sql-statements/administrative-sql-statements/binlog.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_call_procedure`

* Description: Number of [CALL](../../../reference/sql-statements/stored-routine-statements/call.md) procedure\_name statements executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_change_db`

* Description: Number of [USE](../../../reference/sql-statements/administrative-sql-statements/use-database.md) database\_name commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_check`

* Description: Number of [CHECK TABLE](../../../reference/sql-statements/table-statements/check-table.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_checksum`

* Description: Number of [CHECKSUM TABLE](../../../reference/sql-statements/table-statements/checksum-table.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_commit`

* Description: Number of [COMMIT](../../../reference/sql-statements/transactions/commit.md) commands executed. Differs from [Handler\_commit](server-status-variables.md#handler_commit), which counts internal commit statements.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_compound_sql`

* Description: Number of [compund](../../../reference/sql-statements/programmatic-compound-statements/) sql statements.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_create_db`

* Description: Number of [CREATE DATABASE](../../../reference/sql-statements/data-definition/create/create-database.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_create_event`

* Description: Number of [CREATE EVENT](../../../reference/sql-statements/data-definition/create/create-event.md) commands executed. Differs from [Executed\_events](server-status-variables.md#executed_events) in that it is incremented when the CREATE EVENT is run, and not when the event executes.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_create_function`

* Description: Number of [CREATE FUNCTION](../../../reference/sql-statements/data-definition/create/create-function.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_create_index`

* Description: Number of [CREATE INDEX](../../../reference/sql-statements/data-definition/create/create-index.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_create_package`

* Description:
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_create_package_body`

* Description:
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_create_procedure`

* Description: Number of [CREATE PROCEDURE](../../../server-usage/stored-routines/stored-procedures/create-procedure.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_create_role`

* Description: Number of [CREATE ROLE](../../../reference/sql-statements/account-management-sql-statements/create-role.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_create_sequence`

* Description: Number of [CREATE SEQUENCE](../../../reference/sql-structure/sequences/create-sequence.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_create_server`

* Description: Number of [CREATE SERVER](../../../reference/sql-statements/data-definition/create/create-server.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_create_table`

* Description: Number of [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_create_temporary_table`

* Description: Number of [CREATE TEMPORARY TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_create_trigger`

* Description: Number of [CREATE TRIGGER](../../../server-usage/triggers-events/triggers/create-trigger.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_create_udf`

* Description: Number of [CREATE UDF](../../../server-usage/user-defined-functions/create-function-udf.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_create_user`

* Description: Number of [CREATE USER](../../../reference/sql-statements/account-management-sql-statements/create-user.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_create_view`

* Description: Number of [CREATE VIEW](../../../server-usage/views/create-view.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_dealloc_sql`

* Description: Number of [DEALLOCATE](../../../reference/sql-statements/prepared-statements/deallocate-drop-prepare.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_delete`

* Description: Number of [DELETE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) commands executed. Differs from [Handler\_delete](server-status-variables.md#handler_delete), which counts the number of times rows have been deleted from tables.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_delete_multi`

* Description: Number of multi-table [DELETE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_do`

* Description: Number of [DO](../../../reference/sql-statements/stored-routine-statements/do.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_drop_db`

* Description: Number of [DROP DATABASE](../../../reference/sql-statements/data-definition/drop/drop-database.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_drop_event`

* Description: Number of [DROP EVENT](../../../reference/sql-statements/data-definition/drop/drop-event.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_drop_function`

* Description: Number of [DROP FUNCTION](../../../server-usage/stored-routines/stored-functions/drop-function.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_drop_index`

* Description: Number of [DROP INDEX](../../../reference/sql-statements/data-definition/drop/drop-index.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_drop_package`

* Description:
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_drop_package_body`

* Description:
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_drop_procedure`

* Description: Number of [DROP PROCEDURE](../../../server-usage/stored-routines/stored-procedures/drop-procedure.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_drop_role`

* Description: Number of [DROP ROLE](../../../reference/sql-statements/account-management-sql-statements/drop-role.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_drop_sequence`

* Description: Number of [DROP SEQUENCE](../../../reference/sql-structure/sequences/drop-sequence.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_drop_server`

* Description: Number of [DROP SERVER](../../../reference/sql-statements/data-definition/drop/drop-server.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_drop_table`

* Description: Number of [DROP TABLE](../../../reference/sql-statements/data-definition/drop/drop-table.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_drop_temporary_table`

* Description: Number of [DROP TEMPORARY TABLE](../../../reference/sql-statements/data-definition/drop/drop-table.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_drop_trigger`

* Description: Number of [DROP TRIGGER](../../../reference/sql-statements/data-definition/drop/drop-trigger.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_drop_user`

* Description: Number of [DROP USER](../../../reference/sql-statements/account-management-sql-statements/drop-user.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_drop_view`

* Description: Number of [DROP VIEW](../../../server-usage/views/drop-view.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_empty_query`

* Description: Number of queries to the server that do not produce SQL queries. An SQL query simply returning no results does not increment `Com_empty_query` - see [Empty\_queries](server-status-variables.md#empty_queries) instead. An example of an empty query sent to the server is `mariadb --comments -e '-- sql comment'`
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_execute_immediate`

* Description: Number of [EXECUTE IMMEDIATE](../../../reference/sql-statements/prepared-statements/execute-immediate.md) statements executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_execute_sql`

* Description: Number of [EXECUTE](../../../reference/sql-statements/prepared-statements/execute-statement.md) statements executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_flush`

* Description: Number of [FLUSH](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) commands executed. This differs from [Flush\_commands](server-status-variables.md#flush_commands), which also counts internal server flush requests.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_get_diagnostics`

* Description: Number of [GET DIAGNOSTICS](../../../reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-diagnostics/get-diagnostics.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_grant`

* Description: Number of [GRANT](../../../reference/sql-statements/account-management-sql-statements/grant.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_grant_role`

* Description: Number of [GRANT](../../../reference/sql-statements/account-management-sql-statements/grant.md#roles) role commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_ha_close`

* Description: Number of [HANDLER](../../../reference/sql-structure/nosql/handler/handler-commands.md) table\_name CLOSE commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_ha_open`

* Description: Number of [HANDLER](../../../reference/sql-structure/nosql/handler/handler-commands.md) table\_name OPEN commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_ha_read`

* Description: Number of [HANDLER](../../../reference/sql-structure/nosql/handler/handler-commands.md) table\_name READ commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_help`

* Description: Number of [HELP](../../../reference/sql-statements/administrative-sql-statements/help-command.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_insert`

* Description: Number of [INSERT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_insert_select`

* Description: Number of [INSERT ... SELECT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-select.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_install_plugin`

* Description: Number of [INSTALL PLUGIN](../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_kill`

* Description: Number of [KILL](../../../reference/sql-statements/administrative-sql-statements/kill.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_load`

* Description: Number of LOAD commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_load_master_data`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

#### `Com_load_master_table`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

#### `Com_multi`

* Description:
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_lock_tables`

* Description: Number of \[lock-tables|LOCK TABLES]] commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_optimize`

* Description: Number of [OPTIMIZE](../optimizing-tables/optimize-table.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_preload_keys`

* Description:
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_prepare_sql`

* Description: Number of [PREPARE](../../../reference/sql-statements/prepared-statements/prepare-statement.md) statements executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_purge`

* Description: Number of [PURGE](../../../reference/sql-statements/administrative-sql-statements/purge-binary-logs.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_purge_before_date`

* Description: Number of [PURGE BEFORE](../../../reference/sql-statements/administrative-sql-statements/purge-binary-logs.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_release_savepoint`

* Description: Number of [RELEASE SAVEPOINT](../../../reference/sql-statements/transactions/savepoint.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_rename_table`

* Description: Number of [RENAME TABLE](../../../reference/sql-statements/data-definition/rename-table.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_rename_user`

* Description: Number of [RENAME USER](../../../reference/sql-statements/account-management-sql-statements/rename-user.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_repair`

* Description: Number of [REPAIR TABLE](../../../reference/sql-statements/table-statements/repair-table.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_replace`

* Description: Number of [REPLACE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/replace.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_replace_select`

* Description: Number of [REPLACE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/replace.md) ... [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_reset`

* Description: Number of [RESET](../../../reference/sql-statements/administrative-sql-statements/reset.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_resignal`

* Description: Number of [RESIGNAL](../../../reference/sql-statements/programmatic-compound-statements/resignal.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_restore_table`

* Description: Removed in [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5). In older versions, Com\_restore\_table contains the number of [RESTORE TABLE](../../../reference/sql-statements/table-statements/obsolete-table-commands/restore-table-removed.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

#### `Com_revoke`

* Description: Number of [REVOKE](../../../reference/sql-statements/account-management-sql-statements/revoke.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_revoke_all`

* Description: Number of [REVOKE ALL](../../../reference/sql-statements/account-management-sql-statements/revoke.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_revoke_grant`

* Description: Number of [REVOKE](../../../reference/sql-statements/account-management-sql-statements/revoke.md#roles) role commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_rollback`

* Description: Number of [ROLLBACK](../../../reference/sql-statements/transactions/rollback.md) commands executed. Differs from [Handler\_rollback](server-status-variables.md#handler_rollback), which is the number of transaction rollback requests given to a storage engine.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_rollback_to_savepoint`

* Description: Number of [ROLLBACK ... TO SAVEPOINT](../../../reference/sql-statements/transactions/rollback.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_savepoint`

* Description: Number of [SAVEPOINT](../../../reference/sql-statements/transactions/savepoint.md) commands executed. Differs from [Handler\_savepoint](server-status-variables.md#handler_savepoint), which is the number of transaction savepoint creation requests.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_select`

* Description: Number of [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) commands executed. Also includes queries that make use of the [query cache](../buffers-caches-and-threads/query-cache.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_set_option`

* Description: Number of [SET OPTION](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_signal`

* Description: Number of [SIGNAL](../../../reference/sql-statements/programmatic-compound-statements/signal.md) statements executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_authors`

* Description: Number of [SHOW AUTHORS](../../../reference/sql-statements/administrative-sql-statements/show/show-authors.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_binlog_events`

* Description: Number of [SHOW BINLOG EVENTS](../../../reference/sql-statements/administrative-sql-statements/show/show-binlog-events.md) statements executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_binlogs`

* Description: Number of [SHOW BINARY LOGS](../../../reference/sql-statements/administrative-sql-statements/show/show-binary-logs.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_charsets`

* Description: Number of [SHOW CHARACTER SET](../../../reference/sql-statements/administrative-sql-statements/show/show-character-set.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_client_statistics`

* Description: Number of [SHOW CLIENT STATISTICS](../../../reference/sql-statements/administrative-sql-statements/show/show-client-statistics.md) commands executed. Removed in [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes) when that statement was replaced by the generic [SHOW information\_schema\_table](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/).
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes)

#### `Com_show_collations`

* Description: Number of [SHOW COLLATION](../../../reference/sql-statements/administrative-sql-statements/show/show-collation.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_column_types`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

#### `Com_show_contributors`

* Description: Number of [SHOW CONTRIBUTORS](../../../reference/sql-statements/administrative-sql-statements/show/show-contributors.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_create_db`

* Description: Number of [SHOW CREATE DATABASE](../../../reference/sql-statements/administrative-sql-statements/show/show-create-database.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_create_event`

* Description: Number of [SHOW CREATE EVENT](../../../reference/sql-statements/administrative-sql-statements/show/show-create-event.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_create_func`

* Description: Number of [SHOW CREATE FUNCTION](../../../reference/sql-statements/administrative-sql-statements/show/show-create-function.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_create_package`

* Description:
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_create_package_body`

* Description:
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_create_proc`

* Description: Number of [SHOW CREATE PROCEDURE](../../../reference/sql-statements/administrative-sql-statements/show/show-create-procedure.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_create_table`

* Description: Number of [SHOW CREATE TABLE](../../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_create_trigger`

* Description: Number of [SHOW CREATE TRIGGER](../../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_create_user`

* Description: Number of [SHOW CREATE USER](../../../reference/sql-statements/administrative-sql-statements/show/show-create-user.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_databases`

* Description: Number of [SHOW DATABASES](../../../reference/sql-statements/administrative-sql-statements/show/show-databases.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_engine_logs`

* Description: Number of [SHOW ENGINE LOGS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_engine_mutex`

* Description: Number of [SHOW ENGINE MUTEX](../../../reference/sql-statements/administrative-sql-statements/show/show-engine.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_engine_status`

* Description: Number of [SHOW ENGINE STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_events`

* Description: Number of [SHOW EVENTS](../../../reference/sql-statements/administrative-sql-statements/show/show-events.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_errors`

* Description: Number of [SHOW ERRORS](../../../reference/sql-statements/administrative-sql-statements/show/show-errors.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_explain`

* Description: Number of [SHOW EXPLAIN](../../../reference/sql-statements/administrative-sql-statements/show/show-explain.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_fields`

* Description: Number of [SHOW COLUMNS](../../../reference/sql-statements/administrative-sql-statements/show/show-columns.md) or SHOW FIELDS commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_function_status`

* Description: Number of [SHOW FUNCTION STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-function-status.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_generic`

* Description: Number of generic [SHOW](../../../reference/sql-statements/administrative-sql-statements/show/) commands executed, such as [SHOW INDEX\_STATISTICS](../../../reference/sql-statements/administrative-sql-statements/show/show-index-statistics.md) and [SHOW TABLE\_STATISTICS](../../../reference/sql-statements/administrative-sql-statements/show/show-table-statistics.md)
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_grants`

* Description: Number of [SHOW GRANTS](../../../reference/sql-statements/administrative-sql-statements/show/show-grants.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_keys`

* Description: Number of [SHOW INDEX](../../../reference/sql-statements/administrative-sql-statements/show/show-index.md) or SHOW KEYS commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_index_statistics`

* Description: Number of [SHOW INDEX\_STATISTICS](../../../reference/sql-statements/administrative-sql-statements/show/show-index-statistics.md) commands executed. Removed in [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes) when that statement was replaced by the generic [SHOW information\_schema\_table](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/).
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes)

#### `Com_show_open_tables`

* Description: Number of [SHOW OPEN TABLES](../../../reference/sql-statements/administrative-sql-statements/show/show-open-tables.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_package_status`

* Description:
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_package_body_status`

* Description:
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_plugins`

* Description: Number of [SHOW PLUGINS](../../../reference/sql-statements/administrative-sql-statements/show/show-plugins.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_privileges`

* Description: Number of [SHOW PRIVILEGES](../../../reference/sql-statements/administrative-sql-statements/show/show-privileges.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_procedure_status`

* Description: Number of [SHOW PROCEDURE STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-procedure-status.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_processlist`

* Description: Number of [SHOW PROCESSLIST](../../../reference/sql-statements/administrative-sql-statements/show/show-processlist.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_profile`

* Description: Number of [SHOW PROFILE](../../../reference/sql-statements/administrative-sql-statements/show/show-profile.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_profiles`

* Description: Number of [SHOW PROFILES](../../../reference/sql-statements/administrative-sql-statements/show/show-profiles.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_relaylog_events`

* Description: Number of [SHOW RELAYLOG EVENTS](../../../reference/sql-statements/administrative-sql-statements/show/show-relaylog-events.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_status`

* Description: Number of [SHOW STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-status.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`st

#### `Com_show_storage_engines`

* Description: Number of [SHOW STORAGE ENGINES](../../../reference/sql-statements/administrative-sql-statements/show/show-engines.md) - or `SHOW ENGINES` - commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_table_statistics`

* Description: Number of [SHOW TABLE STATISTICS](../../../reference/sql-statements/administrative-sql-statements/show/show-table-statistics.md) commands executed. Removed in [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes) when that statement was replaced by the generic [SHOW information\_schema\_table](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/).
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes)

#### `Com_show_table_status`

* Description: Number of [SHOW TABLE STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-table-status.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_tables`

* Description: Number of [SHOW TABLES](../../../reference/sql-statements/administrative-sql-statements/show/show-tables.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_triggers`

* Description: Number of [SHOW TRIGGERS](../../../reference/sql-statements/administrative-sql-statements/show/show-triggers.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_user_statistics`

* Description: Number of [SHOW USER STATISTICS](../../../reference/sql-statements/administrative-sql-statements/show/show-user-statistics.md) commands executed. Removed in [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes) when that statement was replaced by the generic [SHOW information\_schema\_table](../../../reference/sql-statements/administrative-sql-statements/system-tables/information-schema/information-schema-tables/).
* Scope: Global, Session
* Data Type: `numeric`
* Removed: [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes)

#### `Com_show_variable`

* Description: Number of [SHOW VARIABLES](../../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_show_warnings`

* Description: Number of [SHOW WARNINGS](../../../reference/sql-statements/administrative-sql-statements/show/show-warnings.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_shutdown`

* Description: Number of [SHUTDOWN](../../../reference/sql-statements/administrative-sql-statements/shutdown.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_stmt_close`

* Description: Number of [prepared statements](../../../reference/sql-statements/prepared-statements/) closed ([deallocated or dropped](../../../reference/sql-statements/prepared-statements/deallocate-drop-prepare.md)).
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_stmt_execute`

* Description: Number of [prepared statements](../../../reference/sql-statements/prepared-statements/) [executed](../../../reference/sql-statements/prepared-statements/execute-statement.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_stmt_fetch`

* Description: Number of [prepared statements](../../../reference/sql-statements/prepared-statements/) fetched.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_stmt_prepare`

* Description: Number of [prepared statements](../../../reference/sql-statements/prepared-statements/) [prepared](../../../reference/sql-statements/prepared-statements/prepare-statement.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_stmt_reprepare`

* Description: Number of [prepared statements](../../../reference/sql-statements/prepared-statements/) reprepared.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_stmt_reset`

* Description: Number of [prepared statements](../../../reference/sql-statements/prepared-statements/) where the data of a prepared statement which was accumulated in chunks by sending long data has been reset.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_stmt_send_long_data`

* Description: Number of [prepared statements](../../../reference/sql-statements/prepared-statements/) where the parameter data has been sent in chunks (long data).
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_truncate`

* Description: Number of [TRUNCATE](../../../reference/sql-functions/numeric-functions/truncate.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_uninstall_plugin`

* Description: Number of [UNINSTALL PLUGIN](../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_unlock_tables`

* Description: Number of [UNLOCK TABLES](../../../reference/sql-statements/transactions/lock-tables.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_update`

* Description: Number of [UPDATE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_update_multi`

* Description: Number of multi-table [UPDATE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_xa_commit`

* Description: Number of XA statements committed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_xa_end`

* Description: Number of XA statements ended.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_xa_prepare`

* Description: Number of XA statements prepared.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_xa_recover`

* Description: Number of XA RECOVER statements executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_xa_rollback`

* Description: Number of XA statements rolled back.
* Scope: Global, Session
* Data Type: `numeric`

#### `Com_xa_start`

* Description: Number of XA statements started.
* Scope: Global, Session
* Data Type: `numeric`

#### `Compression`

* Description: Whether client-server traffic is compressed.
* Scope: Session
* Data Type: `boolean`

#### `Connection_errors_accept`

* Description: Number of errors that occurred during calls to accept() on the listening port. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global
* Data Type: `numeric`

#### `Connection_errors_internal`

* Description: Number of refused connections due to internal server errors, for example out of memory errors, or failed thread starts. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global
* Data Type: `numeric`

#### `Connection_errors_max_connections`

* Description: Number of refused connections due to the [max\_connections](server-system-variables.md#max_connections) limit being reached. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global
* Data Type: `numeric`

#### `Connection_errors_peer_address`

* Description: Number of errors while searching for the connecting client IP address. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global
* Data Type: `numeric`

#### `Connection_errors_select`

* Description: Number of errors during calls to select() or poll() on the listening port. The client would not necessarily have been rejected in these cases. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global
* Data Type: `numeric`

#### `Connection_errors_tcpwrap`

* Description: Number of connections the libwrap library refused. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global
* Data Type: `numeric`

#### `Connections`

* Description: Number of connection attempts (both successful and unsuccessful)
* Scope: Global
* Data Type: `numeric`

#### `Cpu_time`

* Description: Total CPU time used. Part of [User Statistics](../query-optimizations/statistics-for-optimizing-queries/user-statistics.md). Requires the [userstat](../query-optimizations/statistics-for-optimizing-queries/user-statistics.md#userstat) system variable to be set in order to be recorded.
* Scope: Global, Session
* Data Type: `numeric`

#### `Created_tmp_disk_tables`

* Description: Number of on-disk temporary tables created.
* Scope: Global, Session
* Data Type: `numeric`

#### `Created_tmp_files`

* Description: Number of temporary files created. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global
* Data Type: `numeric`

#### `Created_tmp_tables`

* Description: Number of in-memory temporary tables created.
* Scope: Global
* Data Type: `numeric`

#### `Delayed_errors`

* Description: Number of errors which occurred while doing [INSERT DELAYED](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md). The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global
* Data Type: `numeric`

#### `Delayed_insert_threads`

* Description: Number of [INSERT DELAYED](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md) threads.
* Scope: Global
* Data Type: `numeric`

#### `Delayed_writes`

* Description: Number of [INSERT DELAYED](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md) rows written. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global
* Data Type: `numeric`

#### `Delete_scan`

* Description: Number of [DELETE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md)s that required a full table scan.
* Scope: Global
* Data Type: `numeric`

#### `Empty_queries`

* Description: Number of queries returning no results. Note this is not the same as [Com\_empty\_query](server-status-variables.md#com_empty_query).
* Scope: Global, Session
* Data Type: `numeric`

#### `Executed_events`

* Description: Number of times events created with [CREATE EVENT](../../../reference/sql-statements/data-definition/create/create-event.md) have executed. This differs from [Com\_create\_event](server-status-variables.md#com_create_event) in that it is only incremented when the event has run, not when it executes.
* Scope: Global, Session
* Data Type: `numeric`

#### `Executed_triggers`

* Description: Number of times triggers created with [CREATE TRIGGER](../../../server-usage/triggers-events/triggers/create-trigger.md) have executed. This differs from [Com\_create\_trigger](server-status-variables.md#com_create_trigger) in that it is only incremented when the trigger has run, not when it executes.
* Scope: Global, Session
* Data Type: `numeric`

#### `Feature_application_time_periods`

* Description: Number of times a table created with [periods](../../../reference/sql-statements/data-definition/create/create-table.md#periods) has been opened.
* Scope: Global, Session
* Data Type: `numeric`

#### `Feature_check_constraint`

* Description: Number of times [constraints](../../../reference/sql-statements/data-definition/constraint.md) were checked. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global, Session
* Data Type: `numeric`

#### `Feature_custom_aggregate_functions`

* Description: Number of queries which make use of [custom aggregate functions](../../../server-usage/stored-routines/stored-functions/stored-aggregate-functions.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Feature_delay_key_write`

* Description: Number of tables opened that are using [delay\_key\_write](server-system-variables.md#delay_key_write). The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global, Session
* Data Type: `numeric`

#### `Feature_dynamic_columns`

* Description: Number of times the [COLUMN\_CREATE()](../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_create.md) function was used.
* Scope: Global, Session
* Data Type: `numeric`

#### `Feature_fulltext`

* Description: Number of times the [MATCH … AGAINST()](../../../reference/sql-functions/string-functions/match-against.md) function was used.
* Scope: Global, Session
* Data Type: `numeric`

#### `Feature_gis`

* Description: Number of times a table with a any of the [geometry](../../../reference/sql-structure/geometry/geometry-types.md) columns was opened.
* Scope: Global, Session
* Data Type: `numeric`

#### `Feature_insert_returning`

* Description:
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1050-release-notes)

#### `Feature_invisible_columns`

* Description: Number of invisible columns in all opened tables.
* Scope: Global, Session
* Data Type: `numeric`

#### `Feature_json`

* Description: Number of times JSON functionality has been used, such as one of the [JSON functions](../../../reference/sql-functions/special-functions/json-functions/). Does not include the [CONNECT engine JSON type](../../../server-usage/storage-engines/connect/connect-table-types/connect-json-table-type.md), or [EXPLAIN/ANALYZE FORMAT=JSON](../../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/analyze-statement.md#analyze-formatjson).
* Scope: Global, Session
* Data Type: `numeric`

#### `Feature_locale`

* Description: Number of times the [@@lc\_messages](server-system-variables.md#lc_messages) variable was assigned into.
* Scope: Global, Session
* Data Type: `numeric`

#### `Feature_subquery`

* Description: Number of subqueries (excluding subqueries in the FROM clause) used.
* Scope: Global, Session
* Data Type: `numeric`

#### `Feature_system_versioning`

* Description: Number of times [system versioning](../../../reference/sql-structure/temporal-tables/system-versioned-tables.md) functionality has been used (opening a table WITH SYSTEM VERSIONING).
* Scope: Global, Session
* Data Type: `numeric`

#### `Feature_timezone`

* Description: Number of times an explicit timezone (excluding [UTC](../../../reference/data-types/string-data-types/character-sets/internationalization-and-localization/coordinated-universal-time.md) and SYSTEM) was specified.
* Scope: Global, Session
* Data Type: `numeric`

#### `Feature_trigger`

* Description: Number of triggers loaded.
* Scope: Global, Session
* Data Type: `numeric`

#### `Feature_window_functions`

* Description: Number of times [window functions](../../../reference/sql-functions/special-functions/window-functions/) were used.
* Scope: Global, Session
* Data Type: `numeric`

#### `Feature_xml`

* Description: Number of times XML functions ([EXTRACTVALUE()](../../../reference/sql-functions/string-functions/extractvalue.md) and [UPDATEXML()](../../../reference/sql-functions/string-functions/updatexml.md)) were used.
* Scope: Global, Session
* Data Type: `numeric`

#### `Flush_commands`

* Description: Number of [FLUSH](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) statements executed, as well as due to internal server flush requests. This differs from [Com\_flush](server-status-variables.md#com_flush), which simply counts FLUSH statements, not internal server flush operations.
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1051-release-notes)

#### `Handler_commit`

* Description: Number of internal [COMMIT](../../../reference/sql-statements/transactions/commit.md) requests. Differs from [Com\_commit](server-status-variables.md#com_commit), which counts the number of [COMMIT](../../../reference/sql-statements/transactions/commit.md) statements executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_delete`

* Description: Number of times rows have been deleted from tables. Differs from [Com\_delete](server-status-variables.md#com_delete), which counts [DELETE](../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) statements.
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_discover`

* Description: Discovery is when the server asks the NDBCLUSTER storage engine if it knows about a table with a given name. Handler\_discover indicates the number of times that tables have been discovered in this way.
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_external_lock`

* Description: Incremented for each call to the external\_lock() function, which generally occurs at the beginning and end of access to a table instance.
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_icp_attempts`

* Description: Number of times pushed index condition was checked. The smaller the ratio of Handler\_icp\_attempts to [Handler\_icp\_match](server-status-variables.md#handler_icp_match) the better the filtering. See [Index Condition Pushdown](../query-optimizations/index-condition-pushdown.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_icp_match`

* Description: Number of times pushed index condition was matched. The smaller the ratio of [Handler\_icp\_attempts](server-status-variables.md#handler_icp_attempts) to Handler\_icp\_match the better the filtering. See [Index Condition Pushdown](../query-optimizations/index-condition-pushdown.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_mrr_init`

* Description: Counts how many MRR (multi-range read) scans were performed. See [Multi Range Read optimization](../mariadb-internal-optimizations/multi-range-read-optimization.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_mrr_key_refills`

* Description: Number of times key buffer was refilled (not counting the initial fill). A non-zero value indicates there wasn't enough memory to do key sort-and-sweep passes in one go. See [Multi Range Read optimization](../mariadb-internal-optimizations/multi-range-read-optimization.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_mrr_rowid_refills`

* Description: Number of times rowid buffer was refilled (not counting the initial fill). A non-zero value indicates there wasn't enough memory to do rowid sort-and-sweep passes in one go. See [Multi Range Read optimization](../mariadb-internal-optimizations/multi-range-read-optimization.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_prepare`

* Description: Number of two-phase commit prepares.
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_read_first`

* Description: Number of requests to read the first row from an index. A high value indicates many full index scans, e.g. `SELECT a FROM table_name` where `a` is an indexed column.
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_read_key`

* Description: Number of row read requests based on an index value. A high value indicates indexes are regularly being used, which is usually positive.
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_read_last`

* Description: Number of requests to read the last row from an index. [ORDER BY DESC](../../../reference/sql-statements/data-manipulation/selecting-data/order-by.md) results in a last-key request followed by several previous-key requests.
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_read_next`

* Description: Number of requests to read the next row from an index (in order). Increments when doing an index scan or querying an index column with a range constraint.
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_read_prev`

* Description: Number of requests to read the previous row from an index (in order). Mostly used with [ORDER BY DESC](../../../reference/sql-statements/data-manipulation/selecting-data/select.md#order-by).
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_read_retry`

* Description: Number of read retrys triggered by semi\_consistent\_read (InnoDB feature).
* Scope: Global
* Data Type: `numeric`

#### `Handler_read_rnd`

* Description: Number of requests to read a row based on its position. If this value is high, you may not be using joins that don't use indexes properly, or be doing many full table scans.
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_read_rnd_deleted`

* Description: Number of requests to delete a row based on its position.
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_read_rnd_next`

* Description: Number of requests to read the next row. A large number of these may indicate many table scans and improperly used indexes.
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_rollback`

* Description: Number of transaction rollback requests given to a storage engine. Differs from [Com\_rollback](server-status-variables.md#com_rollback), which is the number of [ROLLBACK](../../../reference/sql-statements/transactions/rollback.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_savepoint`

* Description: Number of transaction savepoint creation requests. Differs from [Com\_savepoint](server-status-variables.md#com_savepoint) which is the number of [SAVEPOINT](../../../reference/sql-statements/transactions/savepoint.md) commands executed.
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_savepoint_rollback`

* Description: Number of requests to rollback to a transaction [savepoint](../../../reference/sql-statements/transactions/savepoint.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_tmp_delete`

* Description: Number of requests to delete a row in a temporary table.
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_tmp_update`

* Description: Number of requests to update a row to a temporary table.
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_tmp_write`

* Description: Number of requests to write a row to a temporary table.
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_update`

* Description: Number of requests to update a row in a table. Since [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5), this no longer counts temporary tables - see [Handler\_tmp\_update](server-status-variables.md#handler_tmp_update).
* Scope: Global, Session
* Data Type: `numeric`

#### `Handler_write`

* Description: Number of requests to write a row to a table. Since [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5), this no longer counts temporary tables - see [Handler\_tmp\_write](server-status-variables.md#handler_tmp_write).
* Scope: Global, Session
* Data Type: `numeric`

#### `Key_blocks_not_flushed`

* Description: Number of key cache blocks which have been modified but not flushed to disk.
* Scope: Global
* Data Type: `numeric`

#### `Key_blocks_unused`

* Description: Number of unused key cache blocks.
* Scope: Global
* Data Type: `numeric`

#### `Key_blocks_used`

* Description: Max number of key cache blocks which have been used simultaneously.
* Scope: Global
* Data Type: `numeric`

#### `Key_blocks_warm`

* Description: Number of key cache blocks in the warm list.
* Scope: Global
* Data Type: `numeric`

#### `Key_read_requests`

* Description: Number of key cache block read requests. See [Optimizing key\_buffer\_size](optimizing-key_buffer_size.md).
* Scope: Global
* Data Type: `numeric`

#### `Key_reads`

* Description: Number of physical index block reads. See [Optimizing key\_buffer\_size](optimizing-key_buffer_size.md).
* Scope: Global
* Data Type: `numeric`

#### `Key_write_requests`

* Description: Number of requests to write a block to the key cache.
* Scope: Global
* Data Type: `numeric`

#### `Key_writes`

* Description: Number of key cache block write requests
* Scope: Global
* Data Type: `numeric`

#### `Last_query_cost`

* Description: The most recent query optimizer query cost calculation. Can not be calculated for complex queries, such as subqueries or UNION. It will be set to 0 for complex queries.
* Scope: Session
* Data Type: `numeric`

#### `Maria_*`

* Description: When the Maria storage engine was renamed Aria, the Maria variables existing at the time were renamed at the same time. See [Aria Server Status Variables](../../../server-usage/storage-engines/aria/aria-status-variables.md).

#### `Max_memory_used`

* Description: The maximum memory allocation used by the current connection.
* Scope: Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.6.21](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-21-release-notes)

#### `Max_statement_time_exceeded`

* Description: Number of queries that exceeded the execution time specified by [max\_statement\_time](server-system-variables.md#max_statement_time). See [Aborting statements that take longer than a certain time to execute](../query-optimizations/aborting-statements.md).
* Data Type: `numeric`

#### `Max_tmp_space_used`

* Description: Maximum temporary space used. See [Limiting Size of Created Disk Temporary Files and Tables Overview](../../../security/limiting-size-of-created-disk-temporary-files-and-tables/limiting-size-of-created-disk-temporary-files-and-tables-overview.md)
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115)

#### `Max_used_connections`

* Description: Max number of connections ever open at the same time. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Max_used_connections_time`

* Description: The time at which the last change of [max\_used\_connections](server-status-variables.md#max_used_connections) occured. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `datetime`
* Introduced: [MariaDB 11.0.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-2-release-notes), [MariaDB 11.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-1-release-notes)

#### `Memory_used`

* Description: Global or per-connection memory usage, in bytes. This includes all per-connection memory allocations, but excludes global allocations such as the key\_buffer, innodb\_buffer\_pool etc.
* Scope: Global, Session
* Data Type: `numeric`

#### `Memory_used_initial`

* Description: Amount of memory that was used when the server started to service the user connections.
* Scope: Global
* Data Type: `numeric`

#### `Not_flushed_delayed_rows`

* Description: Number of [INSERT DELAYED](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-delayed.md) rows waiting to be written.
* Scope: Global
* Data Type: `numeric`

#### `Open_files`

* Description: Number of regular files currently opened by the server. Does not include sockets or pipes, or storage engines using internal functions.
* Scope: Global
* Data Type: `numeric`

#### `Open_streams`

* Description: Number of currently opened streams, usually log files.
* Scope: Global
* Data Type: `numeric`

#### `Open_table_definitions`

* Description: Number of currently cached .frm files.
* Scope: Global
* Data Type: `numeric`

#### `Open_tables`

* Description: Number of currently opened tables, excluding temporary tables.
* Scope: Global, Session
* Data Type: `numeric`

#### `Opened_files`

* Description: Number of files the server has opened.
* Scope: Global
* Data Type: `numeric`

#### `Opened_plugin_libraries`

* Description: Number of shared libraries that the server has opened to load [plugins](../../../reference/plugins/).
* Scope: Global
* Data Type: `numeric`

#### `Opened_table_definitions`

* Description: Number of .frm files that have been cached.
* Scope: Global, Session
* Data Type: `numeric`

#### `Opened_tables`

* Description: Number of tables the server has opened.
* Scope: Global, Session
* Data Type: `numeric`

#### `Opened_views`

* Description: Number of views the server has opened.
* Scope: Global, Session
* Data Type: `numeric`

#### `Prepared_stmt_count`

* Description: Current number of prepared statements.
* Scope: Global
* Data Type: `numeric`

#### `Qcache_free_blocks`

* Description: Number of free [query cache](../buffers-caches-and-threads/query-cache.md) memory blocks.
* Scope: Global
* Data Type: `numeric`

#### `Qcache_free_memory`

* Description: Amount of free [query cache](../buffers-caches-and-threads/query-cache.md) memory.
* Scope: Global
* Data Type: `numeric`

#### `Qcache_hits`

* Description: Number of requests served by the [query cache](../buffers-caches-and-threads/query-cache.md). The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global
* Data Type: `numeric`

#### `Qcache_inserts`

* Description: Number of queries ever cached in the [query cache](../buffers-caches-and-threads/query-cache.md). The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global
* Data Type: `numeric`

#### `Qcache_lowmem_prunes`

* Description: Number of pruning operations performed to remove old results to make space for new results in the [query cache](../buffers-caches-and-threads/query-cache.md). The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global
* Data Type: `numeric`

#### `Qcache_not_cached`

* Description: Number of queries that are uncacheable by the [query cache](../buffers-caches-and-threads/query-cache.md), or use SQL\_NO\_CACHE. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global
* Data Type: `numeric`

#### `Qcache_queries_in_cache`

* Description: Number of queries currently cached by the [query cache](../buffers-caches-and-threads/query-cache.md).
* Scope: Global
* Data Type: `numeric`

#### `Qcache_total_blocks`

* Description: Number of blocks used by the [query cache](../buffers-caches-and-threads/query-cache.md).
* Scope: Global
* Data Type: `numeric`

#### `Queries`

* Description: Number of statements executed by the server, excluding COM\_PING and COM\_STATISTICS. Differs from [Questions](server-status-variables.md#questions) in that it also counts statements executed within [stored programs](../../../server-usage/stored-routines/).
* Scope: Global, Session
* Data Type: `numeric`

#### `Query_time`

* Description: Cumulative time in seconds, with microsecond precision, of running queries.
* Scope: Global,Session
* Data Type: `numeric`
* Introduced: [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/what-is-mariadb-114)

#### `Questions`

* Description: Number of statements executed by the server, excluding COM\_PING, COM\_STATISTICS, COM\_STMT\_PREPARE, COM\_STMT\_CLOSE, and COM\_STMT\_RESET statements. Differs from [Queries](server-status-variables.md#queries) in that it doesn't count statements executed within [stored programs](../../../server-usage/stored-routines/).
* Scope: Global, Session
* Data Type: `numeric`

#### `Resultset_metadata_skipped`

* Description: Number of times sending the metadata has been skipped. Metadata is not resent if metadata does not change between prepare and execute of prepared statement, or between executes.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1060-release-notes)

#### `Rows_read`

* Description: Number of requests to read a row (excluding temporary tables).
* Scope: Global, Session
* Data Type: `numeric`

#### `Rows_sent`

* Description:
* Scope: Global, Session
* Data Type: `numeric`

#### `Rows_tmp_read`

* Description: Number of requests to read a row in a temporary table.
* Scope: Global, Session
* Data Type: `numeric`

#### `Select_full_join`

* Description: Number of joins which did not use an index. If not zero, you may need to check table indexes.
* Scope: Global, Session
* Data Type: `numeric`

#### `Select_full_range_join`

* Description: Number of joins which used a range search of the first table.
* Scope: Global, Session
* Data Type: `numeric`

#### `Select_range`

* Description: Number of joins which used a range on the first table.
* Scope: Global, Session
* Data Type: `numeric`

#### `Select_range_check`

* Description: Number of joins without keys that check for key usage after each row. If not zero, you may need to check table indexes.
* Scope: Global, Session
* Data Type: `numeric`

#### `Select_scan`

* Description: Number of joins which used a full scan of the first table.
* Scope: Global, Session
* Data Type: `numeric`

#### `Slow_launch_threads`

* Description: Number of threads which took longer than [slow\_launch\_time](server-system-variables.md#slow_launch_time) to create. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global, Session
* Data Type: `numeric`

#### `Slow_queries`

* Description: Number of queries which took longer than [long\_query\_time](server-system-variables.md#long_query_time) to run. The [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/) does not need to be active for this to be recorded.
* Scope: Global, Session
* Data Type: `numeric`

#### `Sort_merge_passes`

* Description: Number of merge passes performed by the sort algorithm. If too high, you may need to look at improving your query indexes, or increasing the [sort\_buffer\_size](server-system-variables.md#sort_buffer_size).
* Scope: Global, Session
* Data Type: `numeric`

#### `Sort_priority_queue_sorts`

* Description: The number of times that sorting was done through a priority queue. (The total number of times sorting was done is a sum [Sort\_range](server-status-variables.md#sort_range) and [Sort\_scan](server-status-variables.md#sort_scan)). See [filesort with small LIMIT optimization](../query-optimizations/filesort-with-small-limit-optimization.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Sort_range`

* Description: Number of sorts which used a range.
* Scope: Global, Session
* Data Type: `numeric`

#### `Sort_rows`

* Description: Number of rows sorted.
* Scope: Global, Session
* Data Type: `numeric`

#### `Sort_scan`

* Description: Number of sorts which used a full table scan.
* Scope: Global, Session
* Data Type: `numeric`

#### `Subquery_cache_hit`

* Description: Counter for all [subquery cache](../query-optimizations/subquery-optimizations/subquery-cache.md) hits. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global, Session
* Data Type: `numeric`

#### `Subquery_cache_miss`

* Description: Counter for all [subquery cache](../query-optimizations/subquery-optimizations/subquery-cache.md) misses. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global, Session
* Data Type: `numeric`

#### `Syncs`

* Description: Number of times my\_sync() has been called, or the number of times the server has had to force data to disk. Covers the [binary log](../../../server-management/server-monitoring-logs/binary-log/), .frm creation (if these\
  operations are configured to sync) and some storage engines ([Archive](../../../server-usage/storage-engines/archive.md),[CSV](../../../server-usage/storage-engines/csv/), [Aria](../../../server-usage/storage-engines/aria/)), but not [XtraDB/InnoDB](../../../server-usage/storage-engines/innodb/)).
* Scope: Global, Session
* Data Type: `numeric`

#### `Table_locks_immediate`

* Description: Number of table locks which were completed immediately. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global
* Data Type: `numeric`

#### `Table_locks_waited`

* Description: Number of table locks which had to wait. Indicates table lock contention. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global
* Data Type: `numeric`

#### `Table_open_cache_active_instances`

* Description: Number of active instances for open tables cache lookups.
* Scope:
* Data Type: `numeric`

#### `Table_open_cache_hits`

* Description: Number of hits for open tables cache lookups.
* Scope:
* Data Type: `numeric`

#### `Table_open_cache_misses`

* Description: Number of misses for open tables cache lookups.
* Scope:
* Data Type: `numeric`

#### `Table_open_cache_overflows`

* Description: Number of overflows for open tables cache lookups.
* Scope:
* Data Type: `numeric`

#### `Tc_log_max_pages_used`

* Description: Max number of pages used by the memory-mapped file-based [transaction coordinator log](../../../server-management/server-monitoring-logs/transaction-coordinator-log/). The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global
* Data Type: `numeric`

#### `Tc_log_page_size`

* Description: Page size of the memory-mapped file-based [transaction coordinator log](../../../server-management/server-monitoring-logs/transaction-coordinator-log/).
* Scope: Global
* Data Type: `numeric`

#### `Tc_log_page_waits`

* Description: Number of times a two-phase commit was forced to wait for a free memory-mapped file-based [transaction coordinator log](../../../server-management/server-monitoring-logs/transaction-coordinator-log/) page. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/).
* Scope: Global
* Data Type: `numeric`

#### `Threads_cached`

* Description: Number of threads cached in the thread cache. This value will be zero if the [thread pool](../buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb.md) is in use.
* Scope: Global
* Data Type: `numeric`

#### `Threads_connected`

* Description: Number of clients connected to the server. See [Handling Too Many Connections](handling-too-many-connections.md). The `Threads_connected` name is inaccurate when the [thread pool](../buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb.md) is in use, since each client connection does not correspond to a dedicated thread in that case.
* Scope: Global
* Data Type: `numeric`

#### `Threads_created`

* Description: Number of threads created to respond to client connections. If too large, look at increasing [thread\_cache\_size](server-system-variables.md#thread_cache_size).
* Scope: Global
* Data Type: `numeric`

#### `Threads_running`

* Description: Number of client connections that are actively running a command, and not just sleeping while waiting to receive the next command to execute. Some internal system threads also count towards this status variable if they would show up in the output of the [SHOW PROCESSLIST](../../../reference/sql-statements/administrative-sql-statements/show/show-processlist.md) statement.
  * In [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1032-release-notes) and before, a global counter was updated each time a client connection dispatched a command. In these versions, the global and session status variable are always the same value.
  * In [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes) and later, the global counter has been removed as a performance improvement. Instead, when the global status variable is queried, it is calculated dynamically by essentially adding up all the running client connections as they would appear in [SHOW PROCESSLIST](../../../reference/sql-statements/administrative-sql-statements/show/show-processlist.md)  output. A client connection is only considered to be running if its thread [COMMAND](../buffers-caches-and-threads/thread-command-values.md) value is not equal to `Sleep`. When the session status variable is queried, it always returns `1`.
* Scope: Global
* Data Type: `numeric`

#### `Tmp_space_used`

* Description: Temporary space used. See [Limiting Size of Created Disk Temporary Files and Tables Overview](../../../security/limiting-size-of-created-disk-temporary-files-and-tables/limiting-size-of-created-disk-temporary-files-and-tables-overview.md)
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115)

#### `Update_scan`

* Description: Number of updates that required a full table scan.
* Scope: Global
* Data Type: `numeric`

#### `Uptime`

* Description: Number of seconds the server has been running.
* Scope: Global
* Data Type: `numeric`

#### `Uptime_since_flush_status`

* Description: Number of seconds since the last [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
