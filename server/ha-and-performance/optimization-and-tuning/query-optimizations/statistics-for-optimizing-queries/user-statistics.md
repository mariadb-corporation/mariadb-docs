# User Statistics

The User Statistics (userstat) plugin creates the [USER\_STATISTICS](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-user_statistics-table.md), [CLIENT\_STATISTICS](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-client_statistics-table.md), the [INDEX\_STATISTICS](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-index_statistics-table.md), and the [TABLE\_STATISTICS](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-table_statistics-table.md) tables in the [INFORMATION\_SCHEMA](../../../../reference/system-tables/information-schema/) database. As an alternative to these tables, the plugin also adds the [SHOW USER\_STATISTICS](../../../../reference/sql-statements/administrative-sql-statements/show/show-user-statistics.md), the [SHOW CLIENT\_STATISTICS](../../../../reference/sql-statements/administrative-sql-statements/show/show-client-statistics.md), the [SHOW INDEX\_STATISTICS](../../../../reference/sql-statements/administrative-sql-statements/show/show-index-statistics.md), and the [SHOW TABLE\_STATISTICS](../../../../reference/sql-statements/administrative-sql-statements/show/show-table-statistics.md) statements.

These tables and commands can be used to understand the server activity better and to identify the sources of your database's load.

The plugin also adds the [FLUSH USER\_STATISTICS](../../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md), [FLUSH CLIENT\_STATISTICS](../../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md), [FLUSH INDEX\_STATISTICS](../../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md), and [FLUSH TABLE\_STATISTICS](../../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) statements.

The MariaDB implementation of this plugin is based on the [userstatv2 patch](https://www.percona.com/docs/wiki/patches:userstatv2) from Percona and Ourdelta. The original code comes from Google (Mark Callaghan's team) with additional work from Percona, Ourdelta, and Weldon Whipple. The MariaDB implementation provides the same functionality as the userstatv2 patch but a lot of changes have been made to make it faster and to better fit the MariaDB infrastructure.

## How it Works

The `userstat` plugin works by keeping several hash tables in memory. All variables are incremented while the query is running. At the end of each statement the global values are updated.

## Enabling the Plugin

By default statistics are not collected. This is to ensure that statistics collection does not cause any extra load on the server unless desired.

Set the [userstat=ON](user-statistics.md#userstat) system variable in a relevant server [option group](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) to enable the plugin. For example:

```
[mariadb]
...
userstat = 1
```

The value can also be changed dynamically. For example:

```sql
SET GLOBAL userstat=1;
```

## Using the Plugin

### Using the Information Schema Table

The `userstat` plugin creates the [USER\_STATISTICS](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-user_statistics-table.md), [CLIENT\_STATISTICS](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-client_statistics-table.md), the [INDEX\_STATISTICS](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-index_statistics-table.md), and the [TABLE\_STATISTICS](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-table_statistics-table.md) tables in the [INFORMATION\_SCHEMA](../../../../reference/system-tables/information-schema/) database.

```sql
SELECT * FROM INFORMATION_SCHEMA.USER_STATISTICS\G
*************************** 1. row ***************************
                  USER: root
     TOTAL_CONNECTIONS: 1
CONCURRENT_CONNECTIONS: 0
        CONNECTED_TIME: 297
             BUSY_TIME: 0.001725
              CPU_TIME: 0.001982
        BYTES_RECEIVED: 388
            BYTES_SENT: 2327
  BINLOG_BYTES_WRITTEN: 0
             ROWS_READ: 0
             ROWS_SENT: 12
          ROWS_DELETED: 0
         ROWS_INSERTED: 13
          ROWS_UPDATED: 0
       SELECT_COMMANDS: 4
       UPDATE_COMMANDS: 0
        OTHER_COMMANDS: 3
   COMMIT_TRANSACTIONS: 0
 ROLLBACK_TRANSACTIONS: 0
    DENIED_CONNECTIONS: 0
      LOST_CONNECTIONS: 0
         ACCESS_DENIED: 0
         EMPTY_QUERIES: 1
```

```sql
SELECT * FROM INFORMATION_SCHEMA.CLIENT_STATISTICS\G
*************************** 1. row ***************************
                CLIENT: localhost
     TOTAL_CONNECTIONS: 3
CONCURRENT_CONNECTIONS: 0
        CONNECTED_TIME: 4883
             BUSY_TIME: 0.009722
              CPU_TIME: 0.0102131
        BYTES_RECEIVED: 841
            BYTES_SENT: 13897
  BINLOG_BYTES_WRITTEN: 0
             ROWS_READ: 0
             ROWS_SENT: 214
          ROWS_DELETED: 0
         ROWS_INSERTED: 207
          ROWS_UPDATED: 0
       SELECT_COMMANDS: 10
       UPDATE_COMMANDS: 0
        OTHER_COMMANDS: 13
   COMMIT_TRANSACTIONS: 0
 ROLLBACK_TRANSACTIONS: 0
    DENIED_CONNECTIONS: 0
      LOST_CONNECTIONS: 0
         ACCESS_DENIED: 0
         EMPTY_QUERIES: 1
1 row in set (0.00 sec)
```

```sql
SELECT * FROM INFORMATION_SCHEMA.INDEX_STATISTICS WHERE TABLE_NAME = "author";
+--------------+------------+------------+-----------+
| TABLE_SCHEMA | TABLE_NAME | INDEX_NAME | ROWS_READ |
+--------------+------------+------------+-----------+
| books        | author     | by_name    |        15 |
+--------------+------------+------------+-----------+
```

```sql
SELECT * FROM INFORMATION_SCHEMA.TABLE_STATISTICS WHERE TABLE_NAME='user';
+--------------+------------+-----------+--------------+------------------------+
| TABLE_SCHEMA | TABLE_NAME | ROWS_READ | ROWS_CHANGED | ROWS_CHANGED_X_INDEXES |
+--------------+------------+-----------+--------------+------------------------+
| mysql        | user       |         5 |            2 |                      2 |
+--------------+------------+-----------+--------------+------------------------+
```

### Using the SHOW Statements

As an alternative to the [INFORMATION\_SCHEMA](../../../../reference/system-tables/information-schema/) tables, the `userstat` plugin also adds the [SHOW USER\_STATISTICS](../../../../reference/sql-statements/administrative-sql-statements/show/show-user-statistics.md), the [SHOW CLIENT\_STATISTICS](../../../../reference/sql-statements/administrative-sql-statements/show/show-client-statistics.md), the [SHOW INDEX\_STATISTICS](../../../../reference/sql-statements/administrative-sql-statements/show/show-index-statistics.md), and the [SHOW TABLE\_STATISTICS](../../../../reference/sql-statements/administrative-sql-statements/show/show-table-statistics.md) statements.

These commands are another way to display the information stored in the information schema tables. WHERE clauses are accepted. LIKE clauses are accepted but ignored.

```sql
SHOW USER_STATISTICS
SHOW CLIENT_STATISTICS
SHOW INDEX_STATISTICS
SHOW TABLE_STATISTICS
```

### Flushing Plugin Data

The `userstat` plugin also adds the [FLUSH USER\_STATISTICS](../../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md), [FLUSH CLIENT\_STATISTICS](../../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md), [FLUSH INDEX\_STATISTICS](../../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md), and [FLUSH TABLE\_STATISTICS](../../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) statements, which discard the information stored in the specified information schema table.

```sql
FLUSH USER_STATISTICS
FLUSH CLIENT_STATISTICS
FLUSH INDEX_STATISTICS
FLUSH TABLE_STATISTICS
```

## Versions

### USER\_STATISTICS

| Version | Status | Introduced                                                                                                   |
| ------- | ------ | ------------------------------------------------------------------------------------------------------------ |
| 2.0     | Stable | [MariaDB 10.1.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.18) |
| 2.0     | Gamma  | [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.1)   |

### CLIENT\_STATISTICS

| Version | Status | Introduced                                                                                                   |
| ------- | ------ | ------------------------------------------------------------------------------------------------------------ |
| 2.0     | Stable | [MariaDB 10.1.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.13) |
| 2.0     | Gamma  | [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.1)   |

### INDEX\_STATISTICS

| Version | Status | Introduced                                                                                                   |
| ------- | ------ | ------------------------------------------------------------------------------------------------------------ |
| 2.0     | Stable | [MariaDB 10.1.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.13) |
| 2.0     | Gamma  | [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.1)   |

### TABLE\_STATISTICS

| Version | Status | Introduced                                                                                                   |
| ------- | ------ | ------------------------------------------------------------------------------------------------------------ |
| 2.0     | Stable | [MariaDB 10.1.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.18) |
| 2.0     | Gamma  | [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.1)   |

## System Variables

### `userstat`

* Description: If set to `1`, user statistics will be activated.
* Command line: `--userstat=1`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

## Status Variables

User Statistics introduced a number of new status variables:

* [access\_denied\_errors](../../system-variables/server-status-variables.md#access_denied_errors)
* [binlog\_bytes\_written](../../system-variables/server-status-variables.md#binlog_bytes_written)
* [busy\_time](../../system-variables/server-status-variables.md#busy_time) (requires [userstat](user-statistics.md#userstat) to be set to be recorded)
* [cpu\_time](../../system-variables/server-status-variables.md#cpu_time) (requires [userstat](user-statistics.md#userstat) to be set to be recorded)
* [empty\_queries](../../system-variables/server-status-variables.md#empty_queries)
* [rows\_read](../../system-variables/server-status-variables.md#rows_read)
* [rows\_sent](../../system-variables/server-status-variables.md#rows_sent)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
