# GRANT

## Syntax

```bnf
GRANT
    priv_type [(column_list)]
      [, priv_type [(column_list)]] ...
    ON [object_type] priv_level
    TO user_specification [ user_options ...] | role_name

user_specification:
  username [authentication_option]
  | PUBLIC
authentication_option:
  IDENTIFIED BY 'password' 
  | IDENTIFIED BY PASSWORD 'password_hash'
  | IDENTIFIED {VIA|WITH} authentication_rule [OR authentication_rule  ...]

authentication_rule:
    authentication_plugin
  | authentication_plugin {USING|AS} 'authentication_string'
  | authentication_plugin {USING|AS} PASSWORD('password')

GRANT PROXY ON username
    TO user_specification [, user_specification ...]
    [WITH GRANT OPTION]

GRANT rolename TO grantee [, grantee ...]
    [WITH ADMIN OPTION]

grantee:
    rolename
    username [authentication_option]

user_options:
    [REQUIRE {NONE | tls_option [[AND] tls_option] ...}]
    [WITH with_option [with_option] ...]

object_type:
    TABLE
  | FUNCTION
  | PROCEDURE
  | PACKAGE
  | PACKAGE BODY

priv_level:
    *
  | *.*
  | db_name.*
  | db_name.tbl_name
  | tbl_name
  | db_name.routine_name

with_option:
    GRANT OPTION
  | resource_option

resource_option:
  MAX_QUERIES_PER_HOUR count
  | MAX_UPDATES_PER_HOUR count
  | MAX_CONNECTIONS_PER_HOUR count
  | MAX_USER_CONNECTIONS count
  | MAX_STATEMENT_TIME time

tls_option:
  SSL 
  | X509
  | CIPHER 'cipher'
  | ISSUER 'issuer'
  | SUBJECT 'subject'
```

## Description

The `GRANT` statement allows you to grant privileges or [roles](grant.md#roles) to accounts. To use `GRANT`, you must have the `GRANT OPTION` privilege, and you must have the privileges that you are granting.

Use the [REVOKE](revoke.md) statement to revoke privileges granted with the `GRANT` statement.

Use the [SHOW GRANTS](../administrative-sql-statements/show/show-grants.md) statement to determine what privileges an account has.

### Account Names

For `GRANT` statements, account names are specified as the `username` argument in the same way as they are for [CREATE USER](create-user.md) statements. See [account names](create-user.md#account-names) from the `CREATE USER` page for details on how account names are specified.

### Implicit Account Creation

The `GRANT` statement also allows you to implicitly create accounts in some cases.

If the account does not yet exist, then `GRANT` can implicitly create it. To implicitly create an account with `GRANT`, a user is required to have the same privileges that would be required to explicitly create the account with the `CREATE USER` statement.

If the `NO_AUTO_CREATE_USER` [SQL\_MODE](../../../server-management/variables-and-modes/sql-mode.md) is set, then accounts can only be created if authentication information is specified, or with a [CREATE USER](create-user.md) statement. If no authentication information is provided, `GRANT` will produce an error when the specified account does not exist, for example:

```sql
SHOW VARIABLES LIKE '%sql_mode%' ;
```

<pre><code><strong>+---------------+--------------------------------------------+
</strong>| Variable_name | Value                                      |
+---------------+--------------------------------------------+
| sql_mode      | NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+---------------+--------------------------------------------+
</code></pre>

```sql
GRANT USAGE ON *.* TO 'user123'@'%' IDENTIFIED BY '';
```

```
ERROR 1133 (28000): Can't find any matching row in the user table
```

```sql
GRANT USAGE ON *.* TO 'user123'@'%' 
  IDENTIFIED VIA PAM using 'mariadb' require ssl ;
Query OK, 0 rows affected (0.00 sec)
```

```sql
SELECT host, user FROM mysql.user WHERE user='user123' ;
```

```
+------+----------+
| host | user     |
+------+----------+
| %    | user123 |
+------+----------+
```

## Privilege Levels

Privileges can be set globally, for an entire database, for a table or routine, or for individual columns in a table. Certain privileges can only be set at certain levels.

Global privileges do not take effect immediately and are only applied to connections created after the `GRANT` statement was executed.

* [Global privileges priv\_type](grant.md#global-privileges) are granted using `*.*` for priv\_level. Global privileges include privileges to administer the database and manage user accounts, as well as privileges for all tables, functions, and procedures. Global privileges are stored in [mysql.global\_priv table](../../system-tables/the-mysql-database-tables/mysql-global_priv-table.md).
* [Database privileges priv\_type](grant.md#database-privileges) are granted using `db_name.*` for priv\_level, or using just `*` to use the [current database](../administrative-sql-statements/use-database.md#description). Database privileges include privileges to create tables and functions, as well as privileges for all tables, functions, and procedures in the database. Database privileges are stored in the [mysql.db table](../../system-tables/the-mysql-database-tables/mysql-db-table.md).
* [Table privileges priv\_type](grant.md#table-privileges) are granted using `db_name.tbl_name`for priv\_level, or using just `tbl_name` to specify a table in the current database. The `TABLE` keyword is optional. Table privileges include the ability to select and change data in the table. Certain table privileges can be granted for individual columns.
* [Column privileges priv\_type](grant.md#column-privileges) are granted by specifying a table for priv\_level and providing a column list after the privilege type. They allow you to control exactly which columns in a table users can select and change.
* [Function privileges priv\_type](grant.md#function-privileges) are granted using `FUNCTION db_name.routine_name` for priv\_level, or using just `FUNCTION routine_name` to specify a function in the current database.
* [Procedure privileges priv\_type](grant.md#procedure-privileges) are granted using `PROCEDURE db_name.routine_name` for priv\_level, or using just `PROCEDURE routine_name` to specify a procedure in the current database.

### The `USAGE` Privilege

The `USAGE` privilege grants no real privileges. The [SHOW GRANTS](../administrative-sql-statements/show/show-grants.md) statement will show a global `USAGE` privilege for a newly-created user. You can use `USAGE` with the `GRANT` statement to change options like `GRANT OPTION`and `MAX_USER_CONNECTIONS` without changing any account privileges.

### The `ALL PRIVILEGES` Privilege

The `ALL PRIVILEGES` privilege grants all available privileges. Granting all privileges only affects the given privilege level. For example, granting all privileges on a table does not grant any privileges on the database or globally.

Using `ALL PRIVILEGES` does not grant the special `GRANT OPTION` privilege.

You can use `ALL` instead of `ALL PRIVILEGES`.

### The `GRANT OPTION` Privilege

Use the `WITH GRANT OPTION` clause to give users the ability to grant privileges to other users at the given privilege level. Users with the `GRANT OPTION` privilege can only grant privileges they have. They cannot grant privileges at a higher privilege level than they have the `GRANT OPTION` privilege.

The `GRANT OPTION` privilege cannot be set for individual columns. If you use `WITH GRANT OPTION` when specifying [column privileges](grant.md#column-privileges), the `GRANT OPTION` privilege will be granted for the entire table.

Using the `WITH GRANT OPTION` clause is equivalent to listing `GRANT OPTION` as a privilege.

### Global Privileges

The following table lists the privileges that can be granted globally. You can also grant all database, table, and function privileges globally. When granted globally, these privileges apply to all databases, tables, or functions, including those created later.

To set a global privilege, use `*.*` for _priv\_level_.

#### **BINLOG ADMIN**

{% tabs %}
{% tab title="Current" %}
Enables administration of the [binary log](../../../server-management/server-monitoring-logs/binary-log/), including the [PURGE BINARY LOGS](../administrative-sql-statements/purge-binary-logs.md) statement and setting the system variables:

* [binlog\_annotate\_row\_events](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_annotate_row_events)
* [binlog\_cache\_size](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_cache_size)
* [binlog\_commit\_wait\_count](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_commit_wait_count)
* [binlog\_commit\_wait\_usec](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_commit_wait_usec)
* [binlog\_direct\_non\_transactional\_updates](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_direct_non_transactional_updates)
* [binlog\_expire\_logs\_seconds](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_expire_logs_seconds)
* [binlog\_file\_cache\_size](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_file_cache_size)
* [binlog\_format](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format)
* [binlog\_row\_image](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_row_image)
* [binlog\_row\_metadata](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_row_metadata)
* [binlog\_stmt\_cache\_size](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_stmt_cache_size)
* [expire\_logs\_days](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#expire_logs_days)
* [log\_bin\_compress](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin_compress)
* [log\_bin\_compress\_min\_len](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin_compress_min_len)
* [log\_bin\_trust\_function\_creators](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin_trust_function_creators)
* [max\_binlog\_cache\_size](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#max_binlog_cache_size)
* [max\_binlog\_size](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#max_binlog_size)
* [max\_binlog\_stmt\_cache\_size](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#max_binlog_stmt_cache_size)
* [sql\_log\_bin](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#sql_log_bin) and
* [sync\_binlog](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#sync_binlog).
{% endtab %}

{% tab title="< 10.5" %}
BINLOG ADMIN isn't available.
{% endtab %}
{% endtabs %}

#### **BINLOG MONITOR**

{% tabs %}
{% tab title="Current" %}
New name for [REPLICATION CLIENT](grant.md#replication-client). `REPLICATION CLIENT` can still be used, though.
{% endtab %}

{% tab title="< 10.5" %}
Use [REPLICATION CLIENT](grant.md#replication-client) instead. [SHOW REPLICA STATUS](../administrative-sql-statements/show/show-replica-status.md) isn't included in this privilege, and [REPLICA MONITOR](grant.md#replica-monitor) is required.
{% endtab %}
{% endtabs %}

Permits running SHOW commands related to the [binary log](../../../server-management/server-monitoring-logs/binary-log/), in particular the [SHOW BINLOG STATUS](../administrative-sql-statements/show/show-binlog-status.md) and [SHOW BINARY LOGS](../administrative-sql-statements/show/show-binary-logs.md) statements.

#### **BINLOG REPLAY**

{% tabs %}
{% tab title="Current" %}
Enables replaying the binary log with the [BINLOG](../administrative-sql-statements/binlog.md) statement (generated by [mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/)), executing [SET timestamp](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#timestamp) when [secure\_timestamp](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#secure_timestamp) is set to `replication`, and setting the session values of system variables usually included in BINLOG output, in particular:

* [gtid\_domain\_id](../../../ha-and-performance/standard-replication/gtid.md#gtid_domain_id)
* [gtid\_seq\_no](../../../ha-and-performance/standard-replication/gtid.md#gtid_seq_no)
* [pseudo\_thread\_id](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#pseudo_thread_id)
* [server\_id](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#server_id).
{% endtab %}

{% tab title="< 10.5" %}
`BINLOG REPLAY` isn't available.
{% endtab %}
{% endtabs %}

#### **CONNECTION ADMIN**

Enables administering connection resource limit options. This includes ignoring the limits specified by [max\_user\_connections](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_user_connections) and [max\_password\_errors](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_password_errors), and allowing one extra connection over [max\_connections](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_connections)

The statements specified in [init\_connect](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#init_connect) are not executed, [killing connections and queries](../administrative-sql-statements/kill.md) owned by other users is permitted. The following connection-related system variables can be changed:

* [connect\_timeout](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#connect_timeout)
* [disconnect\_on\_expired\_password](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#disconnect_on_expired_password)
* [extra\_max\_connections](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#extra_max_connections)
* [init\_connect](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#init_connect)
* [max\_connections](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_connections)
* [max\_connect\_errors](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_connect_errors)
* [max\_password\_errors](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_password_errors)
* [proxy\_protocol\_networks](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#proxy_protocol_networks)
* [secure\_auth](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#secure_auth)
* [slow\_launch\_time](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#slow_launch_time)
* [thread\_pool\_exact\_stats](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_exact_stats)
* [thread\_pool\_dedicated\_listener](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_dedicated_listener)
* [thread\_pool\_idle\_timeout](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_idle_timeout)
* [thread\_pool\_max\_threads](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_max_threads)
* [thread\_pool\_min\_threads](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_min_threads)
* [thread\_pool\_oversubscribe](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_oversubscribe)
* [thread\_pool\_prio\_kickup\_timer](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_prio_kickup_timer)
* [thread\_pool\_priority](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_priority)
* [thread\_pool\_size](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_size), and
* [thread\_pool\_stall\_limit](../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md#thread_pool_stall_limit).

#### **CREATE USER**

Create a user using the [CREATE USER](create-user.md) statement, or implicitly create a user with the `GRANT` statement.

#### **FEDERATED ADMIN**

{% tabs %}
{% tab title="Current" %}
Execute [CREATE SERVER](../data-definition/create/create-server.md), [ALTER SERVER](../data-definition/alter/alter-server.md), and [DROP SERVER](../data-definition/drop/drop-server.md) statements.
{% endtab %}

{% tab title="< 10.5" %}
`FEDERATED ADMIN` is not available.
{% endtab %}
{% endtabs %}

#### **FILE**

Read and write files on the server, using statements like [LOAD DATA INFILE](../data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) or functions like [LOAD\_FILE()](../../sql-functions/string-functions/load_file.md). Also needed to create [CONNECT](../../../server-usage/storage-engines/connect/) outward tables. MariaDB server must have the permissions to access those files.

#### **GRANT OPTION**

Grant global privileges. You can only grant privileges that you have.

#### **PROCESS**

Show information about the active processes, for example via [SHOW PROCESSLIST](../administrative-sql-statements/show/show-processlist.md) or [mariadb-admin processlist](../../../clients-and-utilities/administrative-tools/mariadb-admin.md). If you have the PROCESS privilege, you can see all threads. Otherwise, you can see only your own threads (that is, threads associated with the MariaDB account that you are using).

#### **READ\_ONLY ADMIN**

{% tabs %}
{% tab title="Current" %}
User ignores the [read\_only](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#read_only) system variable, and can perform write operations even when the `read_only` option is active.

The `READ_ONLY ADMIN` privilege has been removed from [SUPER](grant.md#super). The benefit of this is that one can remove the READ\_ONLY ADMIN privilege from all users and ensure that no one can make any changes on any non-temporary tables. This is useful on replicas when one wants to ensure that the replica is kept identical to the primary.
{% endtab %}

{% tab title="< 10.11" %}
User ignores the [read\_only](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#read_only) system variable, and can perform write operations even when the `read_only` option is active.

The `READ_ONLY ADMIN` privilege is included in [SUPER](grant.md#super).
{% endtab %}

{% tab title="< 10.5" %}
`READ\_ONLY ADMIN` isn't available.
{% endtab %}
{% endtabs %}

#### **RELOAD**

Execute [FLUSH](../administrative-sql-statements/flush-commands/flush.md) statements or equivalent [mariadb-admin](../../../clients-and-utilities/administrative-tools/mariadb-admin.md) commands.

#### **REPLICATION CLIENT**

{% tabs %}
{% tab title="Current" %}
Execute [SHOW MASTER STATUS](../administrative-sql-statements/show/show-binlog-status.md) and [SHOW BINARY LOGS](../administrative-sql-statements/show/show-binary-logs.md) informative statements. Renamed to [BINLOG MONITOR](grant.md#binlog-monitor) (but still supported as an alias for compatibility reasons).
{% endtab %}

{% tab title="< 10.5" %}
Execute [SHOW MASTER STATUS](../administrative-sql-statements/show/show-binlog-status.md) and [SHOW BINARY LOGS](../administrative-sql-statements/show/show-binary-logs.md) informative statements. [SHOW SLAVE STATUS](../administrative-sql-statements/show/show-replica-status.md) is part of [REPLICATION CLIENT](grant.md#replication-client).
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Current" %}
Execute [SHOW MASTER STATUS](../administrative-sql-statements/show/show-binlog-status.md) and [SHOW BINARY LOGS](../administrative-sql-statements/show/show-binary-logs.md) informative statements. Using [BINLOG MONITOR](grant.md#binlog-monitor) instead is still supported as an alias.
{% endtab %}

{% tab title="< 10.6" %}
Execute [SHOW MASTER STATUS](../administrative-sql-statements/show/show-binlog-status.md) and [SHOW BINARY LOGS](../administrative-sql-statements/show/show-binary-logs.md) informative statements. Renamed to [BINLOG MONITOR](grant.md#binlog-monitor) in [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes) (but still supported as an alias for compatibility reasons). [SHOW SLAVE STATUS](../administrative-sql-statements/show/show-replica-status.md) was part of [REPLICATION CLIENT](grant.md#replication-client) prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105).
{% endtab %}
{% endtabs %}

#### **REPLICATION MASTER ADMIN**

{% tabs %}
{% tab title="Current" %}
Permits administration of primary servers, including the [SHOW REPLICA HOSTS](../administrative-sql-statements/show/show-replica-hosts.md) statement, and setting the [gtid\_binlog\_state](../../../ha-and-performance/standard-replication/gtid.md#gtid_binlog_state), [gtid\_domain\_id](../../../ha-and-performance/standard-replication/gtid.md#gtid_domain_id), [master\_verify\_checksum](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#master_verify_checksum) and [server\_id](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#server_id) system variables.
{% endtab %}

{% tab title="< 10.5" %}
**`REPLICATION MASTER ADMIN` is not available.**
{% endtab %}
{% endtabs %}

#### **REPLICA MONITOR**

{% tabs %}
{% tab title="Current" %}
Permit [SHOW REPLICA STATUS](../administrative-sql-statements/show/show-replica-status.md) and [SHOW RELAYLOG EVENTS](../administrative-sql-statements/show/show-relaylog-events.md).

See _Reasoning_ tab as to why this was implemented.
{% endtab %}

{% tab title="Reasoning" %}
When a user would upgrade from an older major release to a [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105) minor release prior to [MariaDB 10.5.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1059-release-notes), certain user accounts would lose capabilities. For example, a user account that had the REPLICATION CLIENT privilege in older major releases could run [SHOW REPLICA STATUS](../administrative-sql-statements/show/show-replica-status.md), but after upgrading to a [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105) minor release prior to [MariaDB 10.5.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1059-release-notes), they could no longer run [SHOW REPLICA STATUS](../administrative-sql-statements/show/show-replica-status.md), because that statement was changed to require the REPLICATION REPLICA ADMIN privilege.

This issue is fixed in [MariaDB 10.5.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1059-release-notes) with this new privilege, which now grants the user the ability to execute `SHOW [ALL] (SLAVE | REPLICA) STATUS`.

When a database is upgraded from an older major release to MariaDB Server 10.5.9 or later, any user accounts with the `REPLICATION CLIENT` or `REPLICATION SLAVE` privileges will automatically be granted the new `REPLICA MONITOR` privilege. The privilege fix occurs when the server is started up, not when mariadb-upgrade is performed.

However, when a database is upgraded from an early 10.5 minor release to 10.5.9 and later, the user will have to fix any user account privileges manually.
{% endtab %}

{% tab title="< 10.5.9" %}
`REPLICA MONITOR` is not available.
{% endtab %}
{% endtabs %}

#### **REPLICATION REPLICA**

{% tabs %}
{% tab title="Current" %}
Synonym for [REPLICATION SLAVE](grant.md#replication-slave).
{% endtab %}

{% tab title="< 10.5" %}
**`REPLICATION REPLICA` is not available.**
{% endtab %}
{% endtabs %}

#### **REPLICATION SLAVE**

{% tabs %}
{% tab title="Current" %}
Accounts used by replica servers on the primary need this privilege. This is needed to get the updates made on the master. [REPLICATION REPLICA](grant.md#replication-replica) is an alias for `REPLICATION SLAVE`.
{% endtab %}

{% tab title="< 10.5" %}
Accounts used by replica servers on the primary need this privilege. This is needed to get the updates made on the master.
{% endtab %}
{% endtabs %}

#### **REPLICATION SLAVE ADMIN**

{% tabs %}
{% tab title="Current" %}
Permits administering replica servers, including [START REPLICA/SLAVE](../administrative-sql-statements/replication-statements/start-replica.md), [STOP REPLICA/SLAVE](../administrative-sql-statements/replication-statements/stop-replica.md), [CHANGE MASTER](../administrative-sql-statements/replication-statements/change-master-to.md), [SHOW REPLICA/SLAVE STATUS](../administrative-sql-statements/show/show-replica-status.md), [SHOW RELAYLOG EVENTS](../administrative-sql-statements/show/show-relaylog-events.md) statements, replaying the binary log with the [BINLOG](../administrative-sql-statements/binlog.md) statement (generated by [mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/)), and setting the system variables:

* [gtid\_cleanup\_batch\_size](../../../ha-and-performance/standard-replication/gtid.md#gtid_cleanup_batch_size)
* [gtid\_ignore\_duplicates](../../../ha-and-performance/standard-replication/gtid.md#gtid_ignore_duplicates)
* [gtid\_pos\_auto\_engines](../../../ha-and-performance/standard-replication/gtid.md#gtid_pos_auto_engines)
* [gtid\_slave\_pos](../../../ha-and-performance/standard-replication/gtid.md#gtid_slave_pos)
* [gtid\_strict\_mode](../../../ha-and-performance/standard-replication/gtid.md#gtid_strict_mode)
* [init\_slave](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#init_slave)
* [read\_binlog\_speed\_limit](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#read_binlog_speed_limit)
* [relay\_log\_purge](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#relay_log_purge)
* [relay\_log\_recovery](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#relay_log_recovery)
* [replicate\_do\_db](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#replicate_do_db)
* [replicate\_do\_table](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#replicate_do_table)
* [replicate\_events\_marked\_for\_skip](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#replicate_events_marked_for_skip)
* [replicate\_ignore\_db](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#replicate_ignore_db)
* [replicate\_ignore\_table](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#replicate_ignore_table)
* [replicate\_wild\_do\_table](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#replicate_wild_do_table)
* [replicate\_wild\_ignore\_table](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#replicate_wild_ignore_table)
* [slave\_compressed\_protocol](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_compressed_protocol)
* [slave\_ddl\_exec\_mode](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_ddl_exec_mode)
* [slave\_domain\_parallel\_threads](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_domain_parallel_threads)
* [slave\_exec\_mode](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_exec_mode)
* [slave\_max\_allowed\_packet](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_max_allowed_packet)
* [slave\_net\_timeout](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_net_timeout)
* [slave\_parallel\_max\_queued](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_parallel_max_queued)
* [slave\_parallel\_mode](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_parallel_mode)
* [slave\_parallel\_threads](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_parallel_threads)
* [slave\_parallel\_workers](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_parallel_workers)
* [slave\_run\_triggers\_for\_rbr](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_run_triggers_for_rbr)
* [slave\_sql\_verify\_checksum](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_sql_verify_checksum)
* [slave\_transaction\_retry\_interval](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_transaction_retry_interval)
* [slave\_type\_conversions](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_type_conversions)
* [sync\_master\_info](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#sync_master_info)
* [sync\_relay\_log](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#sync_relay_log), and
* [sync\_relay\_log\_info](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#sync_relay_log_info).
{% endtab %}

{% tab title="< 10.5" %}
`REPLICATION SLAVE ADMIN` is not available.
{% endtab %}
{% endtabs %}

#### **SET USER**

{% tabs %}
{% tab title="Current" %}
Enables setting the `DEFINER` when creating [triggers](../../../server-usage/triggers-events/triggers/), [views](../../../server-usage/views/), [stored functions](../../../server-usage/stored-routines/stored-functions/) and [stored procedures](../../../server-usage/stored-routines/stored-procedures/).
{% endtab %}

{% tab title="< 10.5" %}
SET USER isn't available.
{% endtab %}
{% endtabs %}

#### **SHOW DATABASES**

List all databases using the [SHOW DATABASES](../administrative-sql-statements/show/show-databases.md) statement. Without the `SHOW DATABASES` privilege, you can still issue the `SHOW DATABASES` statement, but it will only list databases containing tables on which you have privileges.

#### **SHUTDOWN**

Shut down the server using [SHUTDOWN](../administrative-sql-statements/shutdown.md) or the [mariadb-admin shutdown](../../../clients-and-utilities/administrative-tools/mariadb-admin.md) command.

#### **SUPER**

Execute superuser statements: [CHANGE MASTER TO](../administrative-sql-statements/replication-statements/change-master-to.md), [KILL](../administrative-sql-statements/kill.md) (users who do not have this privilege can only `KILL` their own threads), [PURGE LOGS](../administrative-sql-statements/purge-binary-logs.md), [SET global system variables](../administrative-sql-statements/set-commands/set.md), or the [mariadb-admin debug](../../../clients-and-utilities/administrative-tools/mariadb-admin.md) command. Also, this permission allows the user to write data even if the [read\_only](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#read_only) startup option is set, enable or disable logging, enable or disable replication on replica, specify a `DEFINER` for statements that support that clause, connect once reaching the `MAX_CONNECTIONS`. If a statement has been specified for the [init-connect](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#init_connect) [mariadbd](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) option, that command will not be executed when a user with `SUPER` privileges connects to the server.

{% tabs %}
{% tab title="Current" %}
The SUPER privilege has been split into multiple smaller privileges to allow for more fine-grained privileges ([MDEV-21743](https://jira.mariadb.org/browse/MDEV-21743)). The privileges are:

* [SET USER](grant.md#set-user)
* [FEDERATED ADMIN](grant.md#federated-admin)
* [CONNECTION ADMIN](grant.md#connection-admin)
* [REPLICATION SLAVE ADMIN](grant.md#replication-slave-admin)
* [BINLOG ADMIN](grant.md#binlog-admin)
* [BINLOG REPLAY](grant.md#binlog-replay)
* [REPLICA MONITOR](grant.md#replica-monitor)
* [BINLOG MONITOR](grant.md#binlog-monitor)
* [REPLICATION MASTER ADMIN](grant.md#replication-master-admin)
* [READ\_ONLY ADMIN](grant.md#read_only-admin)

These grants are no longer a part of SUPER and need to be granted separately.

The [READ\_ONLY ADMIN](grant.md#read_only-admin) privilege has been removed from `SUPER`. The benefit of this is that one can remove the READ\_ONLY ADMIN privilege from all users and ensure that no one can make any changes on any non-temporary tables. This is useful on replicas when one wants to ensure that the replica is kept identical to the primary ([MDEV-29596](https://jira.mariadb.org/browse/MDEV-29596)).
{% endtab %}

{% tab title="< 11.0.1" %}
The SUPER privilege has been split into multiple smaller privileges to allow for more fine-grained privileges ([MDEV-21743](https://jira.mariadb.org/browse/MDEV-21743)). The privileges are:

* [SET USER](grant.md#set-user)
* [FEDERATED ADMIN](grant.md#federated-admin)
* [CONNECTION ADMIN](grant.md#connection-admin)
* [REPLICATION SLAVE ADMIN](grant.md#replication-slave-admin)
* [BINLOG ADMIN](grant.md#binlog-admin)
* [BINLOG REPLAY](grant.md#binlog-replay)
* [REPLICA MONITOR](grant.md#replica-monitor)
* [BINLOG MONITOR](grant.md#binlog-monitor)
* [REPLICATION MASTER ADMIN](grant.md#replication-master-admin)
* [READ\_ONLY ADMIN](grant.md#read_only-admin)

These grants are part of SUPER and don't need to be granted separately.
{% endtab %}

{% tab title="< 10.5" %}
Use the SUPER privilege.
{% endtab %}
{% endtabs %}

### Database Privileges

The following table lists the privileges that can be granted at the database level. You can also grant all table and function privileges at the database level. Table and function privileges on a database apply to all tables or functions in that database, including those created later.

To set a privilege for a database, specify the database using`db_name.*` for _priv\_level_, or just use `*` to specify the current. database.

<table><thead><tr><th width="236.5184326171875">Privilege</th><th>Description</th></tr></thead><tbody><tr><td>CREATE</td><td>Create a database using the <a href="../data-definition/create/create-database.md">CREATE DATABASE</a> statement, when the privilege is granted for a database. You can grant the CREATE privilege on databases that do not yet exist. This also grants the CREATE privilege on all tables in the database.</td></tr><tr><td>CREATE ROUTINE</td><td>Create Stored Programs using the <a href="../../../server-usage/stored-routines/stored-procedures/create-procedure.md">CREATE PROCEDURE</a> and <a href="../data-definition/create/create-function.md">CREATE FUNCTION</a> statements.</td></tr><tr><td>CREATE TEMPORARY TABLES</td><td>Create temporary tables with the <a href="../data-definition/create/create-table.md">CREATE TEMPORARY TABLE</a> statement. This privilege enable writing and dropping those temporary tables</td></tr><tr><td>DROP</td><td>Drop a database using the <a href="../data-definition/drop/drop-database.md">DROP DATABASE</a> statement, when the privilege is granted for a database. This also grants the DROP privilege on all tables in the database.</td></tr><tr><td>EVENT</td><td>Create, drop and alter EVENTs.</td></tr><tr><td>GRANT OPTION</td><td>Grant database privileges. You can only grant privileges that you have.</td></tr><tr><td>LOCK TABLES</td><td>Acquire explicit locks using the <a href="../transactions/lock-tables.md">LOCK TABLES</a> statement; you also need to have the SELECT privilege on a table, in order to lock it.</td></tr><tr><td>SHOW CREATE ROUTINE</td><td>Permit viewing the SHOW CREATE definition statement of a routine, for example <a href="../administrative-sql-statements/show/show-create-function.md">SHOW CREATE FUNCTION</a>, even if not the routine owner. From <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes">MariaDB 11.3.0</a>.</td></tr></tbody></table>

### Table Privileges

<table><thead><tr><th width="257.851806640625">Privilege</th><th>Description</th></tr></thead><tbody><tr><td>ALTER</td><td>Change the structure of an existing table using the <a href="../data-definition/alter/alter-table/">ALTER TABLE</a> statement.</td></tr><tr><td>CREATE</td><td>Create a table using the <a href="../data-definition/create/create-table.md">CREATE TABLE</a> statement. You can grant the CREATE privilege on tables that do not yet exist.</td></tr><tr><td>CREATE VIEW</td><td>Create a view using the <a href="../../../server-usage/views/create-view.md">CREATE_VIEW</a> statement.</td></tr><tr><td>DELETE</td><td>Remove rows from a table using the <a href="../data-manipulation/changing-deleting-data/delete.md">DELETE</a> statement.</td></tr><tr><td>DELETE HISTORY</td><td>Remove <a href="../../sql-structure/temporal-tables/system-versioned-tables.md">historical rows</a> from a table using the <a href="../data-manipulation/changing-deleting-data/delete.md">DELETE HISTORY</a> statement. Displays as DELETE VERSIONING ROWS when running SHOW PRIVILEGES until <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes">MariaDB 10.5.2</a> (<a href="https://jira.mariadb.org/browse/MDEV-20382">MDEV-20382</a>). If a user has the SUPER privilege but not this privilege, running <a href="../../../clients-and-utilities/deployment-tools/mariadb-upgrade.md">mariadb-upgrade</a> will grant this privilege as well.</td></tr><tr><td>DROP</td><td>Drop a table using the <a href="../data-definition/drop/drop-table.md">DROP TABLE</a> statement or a view using the <a href="../../../server-usage/views/drop-view.md">DROP VIEW</a> statement. Also required to execute the <a href="../table-statements/truncate-table.md">TRUNCATE TABLE</a> statement.</td></tr><tr><td>GRANT OPTION</td><td>Grant table privileges. You can only grant privileges that you have.</td></tr><tr><td>INDEX</td><td>Create an index on a table using the <a href="../data-definition/create/create-index.md">CREATE INDEX</a> statement. Without the INDEX privilege, you can still create indexes when creating a table using the <a href="../data-definition/create/create-table.md">CREATE TABLE</a> statement if the you have the CREATE privilege, and you can create indexes using the <a href="../data-definition/alter/alter-table/">ALTER TABLE</a> statement if you have the ALTER privilege.</td></tr><tr><td>INSERT</td><td>Add rows to a table using the <a href="../data-manipulation/inserting-loading-data/insert.md">INSERT</a> statement. The INSERT privilege can also be set on individual columns; see <a href="grant.md#column-privileges">Column Privileges</a> below for details.</td></tr><tr><td>REFERENCES</td><td>Unused.</td></tr><tr><td>SELECT</td><td>Read data from a table using the <a href="../data-manipulation/selecting-data/select.md">SELECT</a> statement. The SELECT privilege can also be set on individual columns; see <a href="grant.md#column-privileges">Column Privileges</a> below for details.</td></tr><tr><td>SHOW VIEW</td><td>Show the <a href="../../../server-usage/views/create-view.md">CREATE VIEW</a> statement to create a view using the <a href="../administrative-sql-statements/show/show-create-view.md">SHOW CREATE VIEW</a> statement.</td></tr><tr><td>TRIGGER</td><td>Required to run the <a href="../../../server-usage/triggers-events/triggers/create-trigger.md">CREATE TRIGGER</a>, <a href="../data-definition/drop/drop-trigger.md">DROP TRIGGER</a>, and <a href="../administrative-sql-statements/show/show-create-trigger.md">SHOW CREATE TRIGGER</a> statements. When another user activates a trigger (running INSERT, UPDATE, or DELETE statements on the associated table), for the trigger to execute, the user that defined the trigger should have the TRIGGER privilege for the table. The user running the INSERT, UPDATE, or DELETE statements on the table is not required to have the TRIGGER privilege.</td></tr><tr><td>UPDATE</td><td>Update existing rows in a table using the <a href="../data-manipulation/changing-deleting-data/update.md">UPDATE</a> statement. UPDATE statements usually include a WHERE clause to update only certain rows. You must have SELECT privileges on the table or the appropriate columns for the WHERE clause. The UPDATE privilege can also be set on individual columns; see <a href="grant.md#column-privileges">Column Privileges</a> below for details.</td></tr></tbody></table>

### Column Privileges

Some table privileges can be set for individual columns of a table. To use column privileges, specify the table explicitly and provide a list of column names after the privilege type. For example, the following statement would allow the user to read the names and positions of employees, but not other information from the same table, such as salaries.

```sql
GRANT SELECT (name, position) ON Employee TO 'jeffrey'@'localhost';
```

<table><thead><tr><th width="249.5555419921875">Privilege</th><th>Description</th></tr></thead><tbody><tr><td>INSERT (column_list)</td><td>Add rows specifying values in columns using the <a href="../data-manipulation/inserting-loading-data/insert.md">INSERT</a> statement. If you only have column-level <code>INSERT</code> privileges, you must specify the columns you are setting in the <code>INSERT</code> statement. All other columns will be set to their default values, or <code>NULL</code>.</td></tr><tr><td>REFERENCES (column_list)</td><td>Unused.</td></tr><tr><td>SELECT (column_list)</td><td>Read values in columns using the <a href="../data-manipulation/selecting-data/select.md">SELECT</a> statement. You cannot access or query any columns for which you do not have <code>SELECT</code> privileges, including in <code>WHERE</code>, <code>ON</code>, <code>GROUP BY</code>, and <code>ORDER BY</code> clauses.</td></tr><tr><td>UPDATE (column_list)</td><td>Update values in columns of existing rows using the <a href="../data-manipulation/changing-deleting-data/update.md">UPDATE</a> statement. <code>UPDATE</code> statements usually include a <code>WHERE</code> clause to update only certain rows. You must have <code>SELECT</code> privileges on the table or the appropriate columns for the <code>WHERE</code> clause.</td></tr></tbody></table>

### Function Privileges

<table><thead><tr><th width="212.81475830078125">Privilege</th><th>Description</th></tr></thead><tbody><tr><td>ALTER ROUTINE</td><td>Change the characteristics of a stored function using the <a href="../data-definition/alter/alter-function.md">ALTER FUNCTION</a> statement.</td></tr><tr><td>EXECUTE</td><td>Use a stored function. You need <code>SELECT</code> privileges for any tables or columns accessed by the function.</td></tr><tr><td>GRANT OPTION</td><td>Grant function privileges. You can only grant privileges that you have.</td></tr></tbody></table>

### Procedure Privileges

| Privilege     | Description                                                                                                                                                                                                                                                                                         |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ALTER ROUTINE | Change the characteristics of a stored procedure using the [ALTER PROCEDURE](../../../server-usage/stored-routines/stored-procedures/alter-procedure.md) statement.                                                                                                                                 |
| EXECUTE       | Execute a [stored procedure](../../../server-usage/stored-routines/stored-procedures/) using the [CALL](../stored-routine-statements/call.md) statement. The privilege to call a procedure may allow you to perform actions you wouldn't otherwise be able to do, such as insert rows into a table. |
| GRANT OPTION  | Grant procedure privileges. You can only grant privileges that you have.                                                                                                                                                                                                                            |

```sql
GRANT EXECUTE ON PROCEDURE mysql.create_db TO maintainer;
```

### Proxy Privileges

| Privilege | Description                                 |
| --------- | ------------------------------------------- |
| PROXY     | Permits one user to be a proxy for another. |

The `PROXY` privilege allows one user to proxy as another user, which means their privileges change to that of the proxy user, and the [CURRENT\_USER()](../../sql-functions/secondary-functions/information-functions/current_user.md) function returns the user name of the proxy user.

The `PROXY` privilege only works with authentication plugins that support it. The default [mysql\_native\_password](../../plugins/authentication-plugins/authentication-plugin-mysql_native_password.md) authentication plugin does not support proxy users.

The [pam](../../plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md) authentication plugin is the only plugin included with MariaDB that currently supports proxy users. The `PROXY` privilege is commonly used with the [pam](../../plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md) authentication plugin to enable [user and group mapping with PAM](../../plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/user-and-group-mapping-with-pam.md).

For example, to grant the `PROXY` privilege to an [anonymous account](create-user.md#anonymous-accounts) that authenticates with the [pam](../../plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md) authentication plugin, you could execute the following:

```sql
CREATE USER 'dba'@'%' IDENTIFIED BY 'strongpassword';
GRANT ALL PRIVILEGES ON *.* TO 'dba'@'%' ;

CREATE USER ''@'%' IDENTIFIED VIA pam USING 'mariadb';
GRANT PROXY ON 'dba'@'%' TO ''@'%';
```

A user account can only grant the `PROXY` privilege for a specific user account if the granter also has the `PROXY` privilege for that specific user account, and if that privilege is defined `WITH GRANT OPTION`. For example, the following example fails because the granter does not have the `PROXY` privilege for that specific user account at all:

```sql
SELECT USER(), CURRENT_USER();
```

```
+-----------------+-----------------+
| USER()          | CURRENT_USER()  |
+-----------------+-----------------+
| alice@localhost | alice@localhost |
+-----------------+-----------------+
```

```sql
SHOW GRANTS
```

```
+-----------------------------------------------------------------------------------------------------------------------+
| Grants for alice@localhost                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------+
| GRANT ALL PRIVILEGES ON *.* TO 'alice'@'localhost' IDENTIFIED BY PASSWORD '*2470C0C06DEE42FD1618BB99005ADCA2EC9D1E19' |
+-----------------------------------------------------------------------------------------------------------------------+
```

```sql
GRANT PROXY ON 'dba'@'localhost' TO 'bob'@'localhost';
ERROR 1698 (28000): Access denied for user 'alice'@'localhost'
```

And the following example fails because the granter does have the `PROXY` privilege for that specific user account, but it is not defined `WITH GRANT OPTION`:

```sql
SELECT USER(), CURRENT_USER();
```

```
+-----------------+-----------------+
| USER()          | CURRENT_USER()  |
+-----------------+-----------------+
| alice@localhost | alice@localhost |
+-----------------+-----------------+
```

```sql
SHOW GRANTS;
```

<pre><code><strong>+-----------------------------------------------------------------------------------------------------------------------+
</strong>| Grants for alice@localhost                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------+
| GRANT ALL PRIVILEGES ON *.* TO 'alice'@'localhost' IDENTIFIED BY PASSWORD '*2470C0C06DEE42FD1618BB99005ADCA2EC9D1E19' |
| GRANT PROXY ON 'dba'@'localhost' TO 'alice'@'localhost'                                                               |
+-----------------------------------------------------------------------------------------------------------------------+
</code></pre>

```sql
GRANT PROXY ON 'dba'@'localhost' TO 'bob'@'localhost';
ERROR 1698 (28000): Access denied for user 'alice'@'localhost'
```

But the following example succeeds because the granter does have the `PROXY` privilege for that specific user account, and it is defined `WITH GRANT OPTION`:

```sql
SELECT USER(), CURRENT_USER();
```

```
+-----------------+-----------------+
| USER()          | CURRENT_USER()  |
+-----------------+-----------------+
| alice@localhost | alice@localhost |
+-----------------+-----------------+
```

```sql
SHOW GRANTS;
```

```
+-----------------------------------------------------------------------------------------------------------------------------------------+
| Grants for alice@localhost                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------+
| GRANT ALL PRIVILEGES ON *.* TO 'alice'@'localhost' IDENTIFIED BY PASSWORD '*2470C0C06DEE42FD1618BB99005ADCA2EC9D1E19' WITH GRANT OPTION |
| GRANT PROXY ON 'dba'@'localhost' TO 'alice'@'localhost' WITH GRANT OPTION                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------+
```

```sql
GRANT PROXY ON 'dba'@'localhost' TO 'bob'@'localhost';
```

A user account can grant the `PROXY` privilege for any other user account if the granter has the `PROXY` privilege for the `''@'%'` anonymous user account, like this:

```sql
GRANT PROXY ON ''@'%' TO 'dba'@'localhost' WITH GRANT OPTION;
```

For example, the following example succeeds because the user can grant the `PROXY` privilege for any other user account:

```sql
SELECT USER(), CURRENT_USER();
```

```
+-----------------+-----------------+
| USER()          | CURRENT_USER()  |
+-----------------+-----------------+
| alice@localhost | alice@localhost |
+-----------------+-----------------+
```

```sql
SHOW GRANTS;
```

```
+-----------------------------------------------------------------------------------------------------------------------------------------+
| Grants for alice@localhost                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------+
| GRANT ALL PRIVILEGES ON *.* TO 'alice'@'localhost' IDENTIFIED BY PASSWORD '*2470C0C06DEE42FD1618BB99005ADCA2EC9D1E19' WITH GRANT OPTION |
| GRANT PROXY ON ''@'%' TO 'alice'@'localhost' WITH GRANT OPTION                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------+
```

```sql
GRANT PROXY ON 'app1_dba'@'localhost' TO 'bob'@'localhost';
Query OK, 0 rows affected (0.004 sec)
```

```sql
GRANT PROXY ON 'app2_dba'@'localhost' TO 'carol'@'localhost';
Query OK, 0 rows affected (0.004 sec)
```

The default `root` user accounts created by [mariadb-install-db](../../../clients-and-utilities/deployment-tools/mariadb-install-db.md) have this privilege. For example:

```sql
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
GRANT PROXY ON ''@'%' TO 'root'@'localhost' WITH GRANT OPTION;
```

This allows the default `root` user accounts to grant the `PROXY` privilege for any other user account, and it also allows the default `root` user accounts to grant others the privilege to do the same.

## Authentication Options

The authentication options for the `GRANT` statement are the same as those for the [CREATE USER](create-user.md) statement.

### IDENTIFIED BY 'password'

The optional `IDENTIFIED BY` clause can be used to provide an account with a password. The password should be specified in plain text. It will be hashed by the [PASSWORD](../../sql-functions/secondary-functions/encryption-hashing-and-compression-functions/password.md) function prior to being stored.

For example, if our password is `mariadb`, then we can create the user with:

```sql
GRANT USAGE ON *.* TO foo2@test IDENTIFIED BY 'mariadb';
```

If you do not specify a password with the `IDENTIFIED BY` clause, the user will be able to connect without a password. A blank password is not a wildcard to match any password. The user must connect without providing a password if no password is set.

If the user account already exists and if you provide the `IDENTIFIED BY` clause, then the user's password will be changed. You must have the privileges needed for the [SET PASSWORD](set-password.md) statement to change a user's password with `GRANT`.

The only [authentication plugins](../../plugins/authentication-plugins/) that this clause supports are [mysql\_native\_password](../../plugins/authentication-plugins/authentication-plugin-mysql_native_password.md) and [mysql\_old\_password](../../plugins/authentication-plugins/authentication-plugin-mysql_old_password.md).

### IDENTIFIED BY PASSWORD 'password\_hash'

The optional `IDENTIFIED BY PASSWORD` clause can be used to provide an account with a password that has already been hashed. The password should be specified as a hash that was provided by the [PASSWORD](../../sql-functions/secondary-functions/encryption-hashing-and-compression-functions/password.md) function. It will be stored as-is.

For example, if our password is `mariadb`, then we can find the hash with:

```sql
SELECT PASSWORD('mariadb');
```

```
+-------------------------------------------+
| PASSWORD('mariadb')                       |
+-------------------------------------------+
| *54958E764CE10E50764C2EECBB71D01F08549980 |
+-------------------------------------------+
1 row in set (0.00 sec)
```

And then we can create a user with the hash:

```sql
GRANT USAGE ON *.* TO foo2@test IDENTIFIED BY 
  PASSWORD '*54958E764CE10E50764C2EECBB71D01F08549980';
```

If you do not specify a password with the `IDENTIFIED BY` clause, the user will be able to connect without a password. A blank password is not a wildcard to match any password. The user must connect without providing a password if no password is set.

If the user account already exists and if you provide the `IDENTIFIED BY` clause, then the user's password will be changed. You must have the privileges needed for the [SET PASSWORD](set-password.md) tastatement to change a user's password with `GRANT`.

The only [authentication plugins](../../plugins/authentication-plugins/) that this clause supports are [mysql\_native\_password](../../plugins/authentication-plugins/authentication-plugin-mysql_native_password.md) and [mysql\_old\_password](../../plugins/authentication-plugins/authentication-plugin-mysql_old_password.md).

### IDENTIFIED {VIA|WITH} authentication\_plugin

The optional `IDENTIFIED VIA authentication_plugin` allows you to specify that the account should be authenticated by a specific [authentication plugin](../../plugins/authentication-plugins/). The plugin name must be an active authentication plugin as per [SHOW PLUGINS](../administrative-sql-statements/show/show-plugins.md). If it doesn't show up in that output, then you will need to install it with [INSTALL PLUGIN](../administrative-sql-statements/plugin-sql-statements/install-plugin.md) or [INSTALL SONAME](../administrative-sql-statements/plugin-sql-statements/install-soname.md).

For example, this could be used with the [PAM authentication plugin](../../plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md):

```sql
GRANT USAGE ON *.* TO foo2@test IDENTIFIED VIA pam;
```

Some authentication plugins allow additional arguments to be specified after a `USING` or `AS` keyword. For example, the [PAM authentication plugin](../../plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md) accepts a [service name](../../plugins/authentication-plugins/authentication-with-pluggable-authentication-modules-pam/authentication-plugin-pam.md#configuring-the-pam-service):

```sql
GRANT USAGE ON *.* TO foo2@test IDENTIFIED VIA pam USING 'mariadb';
```

The exact meaning of the additional argument would depend on the specific authentication plugin.

The `USING` or `AS` keyword can also be used to provide a plain-text password to a plugin if it's provided as an argument to the [PASSWORD()](../../sql-functions/secondary-functions/encryption-hashing-and-compression-functions/password.md) function. This is only valid for [authentication plugins](../../plugins/authentication-plugins/) that have implemented a hook for the [PASSWORD()](../../sql-functions/secondary-functions/encryption-hashing-and-compression-functions/password.md) function. For example, the [ed25519](../../plugins/authentication-plugins/authentication-plugin-ed25519.md) authentication plugin supports this:

```sql
CREATE USER safe@'%' IDENTIFIED VIA ed25519 
  USING PASSWORD('secret');
```

One can specify many authentication plugins, they all work as alternative ways of authenticating a user:

```sql
CREATE USER safe@'%' IDENTIFIED VIA ed25519 
  USING PASSWORD('secret') OR unix_socket;
```

By default, when you create a user without specifying an authentication plugin, MariaDB uses the [mysql\_native\_password](../../plugins/authentication-plugins/authentication-plugin-mysql_native_password.md) plugin.

## Resource Limit Options

It is possible to set per-account limits for certain server resources. The following table shows the values that can be set per account:

| Limit Type                  | Decription                                                                                                                                                                                                                      |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MAX\_QUERIES\_PER\_HOUR     | Number of statements that the account can issue per hour (including updates)                                                                                                                                                    |
| MAX\_UPDATES\_PER\_HOUR     | Number of updates (not queries) that the account can issue per hour                                                                                                                                                             |
| MAX\_CONNECTIONS\_PER\_HOUR | Number of connections that the account can start per hour                                                                                                                                                                       |
| MAX\_USER\_CONNECTIONS      | Number of simultaneous connections that can be accepted from the same account; if it is 0, max\_connections will be used instead; if max\_connections is 0, there is no limit for this account's simultaneous connections.      |
| MAX\_STATEMENT\_TIME        | Timeout, in seconds, for statements executed by the user. See also [Aborting Statements that Exceed a Certain Time to Execute](../../../ha-and-performance/optimization-and-tuning/query-optimizations/aborting-statements.md). |

If any of these limits are set to `0`, then there is no limit for that resource for that user.

To set resource limits for an account, if you do not want to change that account's privileges, you can issue a `GRANT` statement with the `USAGE` privilege, which has no meaning. The statement can name some or all limit types, in any order.

Here is an example showing how to set resource limits:

```sql
GRANT USAGE ON *.* TO 'someone'@'localhost' WITH
    MAX_USER_CONNECTIONS 0
    MAX_QUERIES_PER_HOUR 200;
```

The resources are tracked per account, which means `'user'@'server'`; not per user name or per connection.

The count can be reset for all users using [FLUSH USER\_RESOURCES](../administrative-sql-statements/flush-commands/flush.md), [FLUSH PRIVILEGES](../administrative-sql-statements/flush-commands/flush.md) or [mariadb-admin reload](../../../clients-and-utilities/administrative-tools/mariadb-admin.md).

{% tabs %}
{% tab title="Current" %}
Users with the `CONNECTION ADMIN` privilege or the `SUPER` privilege are not restricted by `max_user_connections` or `max_password_errors` , and they are allowed one additional connection when `max_connections` is reached.
{% endtab %}

{% tab title="< 10.5" %}
Users with the `CONNECTION ADMIN` privilege or the `SUPER` privilege are restricted by `max_user_connections` or `max_password_errors` , and they are not allowed one additional connection when `max_connections` is reached.
{% endtab %}
{% endtabs %}

Per account resource limits are stored in the [user](../../system-tables/the-mysql-database-tables/mysql-user-table.md) table, in the [mysql](../../system-tables/the-mysql-database-tables/) database. Columns used for resources limits are named `max_questions`, `max_updates`, `max_connections` (for `MAX_CONNECTIONS_PER_HOUR`), and `max_user_connections` (for `MAX_USER_CONNECTIONS`).

## TLS Options

By default, MariaDB transmits data between the server and clients without encrypting it. This is generally acceptable when the server and client run on the same host or in networks where security is guaranteed through other means. However, in cases where the server and client exist on separate networks or they are in a high-risk network, the lack of encryption does introduce security concerns as a malicious actor could potentially eavesdrop on the traffic as it is sent over the network between them.

To mitigate this concern, MariaDB allows you to encrypt data in transit between the server and clients using the Transport Layer Security (TLS) protocol. TLS was formerly known as Secure Socket Layer (SSL), but strictly speaking the SSL protocol is a predecessor to TLS and, that version of the protocol is now considered insecure. The documentation still uses the term SSL often and for compatibility reasons TLS-related server system and status variables still use the prefix ssl\_, but internally, MariaDB only supports its secure successors.

See [Secure Connections Overview](../../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md) for more information about how to determine whether your MariaDB server has TLS support.

You can set certain TLS-related restrictions for specific user accounts. For instance, you might use this with user accounts that require access to sensitive data while sending it across networks that you do not control. These restrictions can be enabled for a user account with the [CREATE USER](create-user.md), [ALTER USER](alter-user.md), or [GRANT](grant.md) statements. The following options are available:

<table><thead><tr><th width="234.1480712890625">Option</th><th>Description</th></tr></thead><tbody><tr><td>REQUIRE NONE</td><td>TLS is not required for this account, but can still be used.</td></tr><tr><td>REQUIRE SSL</td><td>The account must use TLS, but no valid X509 certificate is required. This option cannot be combined with other TLS options.</td></tr><tr><td>REQUIRE X509</td><td>The account must use TLS and must have a valid X509 certificate. This option implies REQUIRE SSL. This option cannot be combined with other TLS options.</td></tr><tr><td>REQUIRE ISSUER 'issuer'</td><td>The account must use TLS and must have a valid X509 certificate. Also, the Certificate Authority must be the one specified via the string issuer. This option implies REQUIRE X509. This option can be combined with the SUBJECT, and CIPHER options in any order.</td></tr><tr><td>REQUIRE SUBJECT 'subject'</td><td>The account must use TLS and must have a valid X509 certificate. Also, the certificate's Subject must be the one specified via the string subject. This option implies REQUIRE X509. This option can be combined with the ISSUER, and CIPHER options in any order.</td></tr><tr><td>REQUIRE CIPHER 'cipher'</td><td>The account must use TLS, but no valid X509 certificate is required. Also, the encryption used for the connection must use a specific cipher method specified in the string cipher. This option implies REQUIRE SSL. This option can be combined with the ISSUER, and SUBJECT options in any order.</td></tr></tbody></table>

The `REQUIRE` keyword must be used only once for all specified options, and the `AND` keyword can be used to separate individual options, but it is not required.

For example, you can create a user account that requires these TLS options with the following:

```sql
GRANT USAGE ON *.* TO 'alice'@'%'
  REQUIRE SUBJECT '/CN=alice/O=My Dom, Inc./C=US/ST=Oregon/L=Portland'
  AND ISSUER '/C=FI/ST=Somewhere/L=City/ O=Some Company/CN=Peter Parker/emailAddress=p.parker@marvel.com'
  AND CIPHER 'SHA-DES-CBC3-EDH-RSA';
```

If any of these options are set for a specific user account, then any client who tries to connect with that user account will have to be configured to connect with TLS.

See [Securing Connections for Client and Server](../../../security/securing-mariadb/encryption/data-in-transit-encryption/securing-connections-for-client-and-server.md) for information on how to enable TLS on the client and server.

## Roles

```sql
GRANT role TO grantee [, grantee ... ]
[ WITH ADMIN OPTION ]

grantee:
    rolename
    username [authentication_option]
```

The `GRANT` statement is also used to grant the use of a [role](../../../security/user-account-management/roles/) to one or more users or other roles. In order to be able to grant a role, the grantor doing so must have permission to do so (see `WITH ADMIN` in the [CREATE ROLE](create-role.md) article).

Specifying the `WITH ADMIN OPTION` permits the grantee to in turn grant the role to another.

For example, the following commands show how to grant the same role to a couple different users.

```sql
GRANT journalist TO hulda;

GRANT journalist TO berengar WITH ADMIN OPTION;
```

If a user has been granted a role, they do not automatically obtain all permissions associated with that role. These permissions are only in use when the user activates the role with the [SET ROLE](set-role.md) statement.

{% hint style="warning" %}
Be careful to avoid conflicting role and user names. In case of a conflict, the role name takes precedence, as shown in the following example. The `GRANT` statement assigns privileges to the role, not to the user:
{% endhint %}

```sql
CREATE USER alice IDENTIFIED BY 'password';
CREATE ROLE alice;
GRANT select, insert on db.* TO alice;
```

## TO PUBLIC

{% tabs %}
{% tab title="Current" %}
[blog post](https://mariadb.org/grant-to-public-in-mariadb/)
{% endtab %}

{% tab title="< 10.11.0" %}
TO PUBLIC is unavailable.
{% endtab %}
{% endtabs %}

### Syntax

```sql
GRANT <privilege> ON <DATABASE>.<object> TO PUBLIC;
REVOKE <privilege> ON <DATABASE>.<object> FROM PUBLIC;
```

`GRANT ... TO PUBLIC` grants privileges to all users with access to the server. The privileges also apply to users created after the privileges are granted. This can be useful when one only wants to state once that all users need to have a certain set of privileges.\
When running [SHOW GRANTS](../administrative-sql-statements/show/show-grants.md), a user will also see all privileges inherited from PUBLIC. [SHOW GRANTS FOR PUBLIC](../administrative-sql-statements/show/show-grants.md#for-public) will only show TO PUBLIC grants.

## Grant Examples

### Granting Root-like Privileges

You can create a user that has privileges similar to the default `root` accounts by executing the following:

```sql
CREATE USER 'alexander'@'localhost';
GRANT ALL PRIVILEGES ON  *.* TO 'alexander'@'localhost' WITH GRANT OPTION;
```

## See Also

* [Troubleshooting Connection Issues](../../../mariadb-quickstart-guides/mariadb-connection-troubleshooting-guide.md)
* [Authentication from MariaDB 10.4](../../../security/user-account-management/authentication-from-mariadb-10-4.md)
* [--skip-grant-tables](../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) allows you to start MariaDB without `GRANT`. This is useful if you lost your root password.
* [CREATE USER](create-user.md)
* [ALTER USER](alter-user.md)
* [DROP USER](drop-user.md)
* [SET PASSWORD](set-password.md)
* [SHOW CREATE USER](../administrative-sql-statements/show/show-create-user.md)
* [mysql.global\_priv table](../../system-tables/the-mysql-database-tables/mysql-global_priv-table.md)
* [mysql.user table](../../system-tables/the-mysql-database-tables/mysql-user-table.md)
* [Password Validation Plugins](../../plugins/password-validation-plugins/) - permits the setting of basic criteria for passwords
* [Authentication Plugins](../../plugins/authentication-plugins/) - allow various authentication methods to be used, and new ones to be developed.

{% include "../../../.gitbook/includes/license-gplv2-fill-help-tables.md" %}

{% @marketo/form formId="4316" %}
