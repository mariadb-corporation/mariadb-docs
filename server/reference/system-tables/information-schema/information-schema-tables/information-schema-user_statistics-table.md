---
description: >-
  The Information Schema USER_STATISTICS table provides activity statistics for
  users, such as bytes sent and rows read, aiding in auditing.
---

# Information Schema USER\_STATISTICS Table

The [Information Schema](../) `USER_STATISTICS` table holds statistics about user activity. This is part of the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature, which is not enabled by default.

You can use this table to find out such things as which user is causing the most load and which users are being abusive. You can also use this table to measure how close to capacity the server may be.

It contains the following columns:

| Field                          | Type        | Notes                                                                                                                                                                                                                                                                                           |
| ------------------------------ | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| USER                           | varchar(48) | The username. The value '#mysql\_system\_user#' appears when there is no username (such as for the slave SQL thread).                                                                                                                                                                           |
| TOTAL\_CONNECTIONS             | int(11)     | The number of connections created for this user.                                                                                                                                                                                                                                                |
| CONCURRENT\_CONNECTIONS        | int(11)     | The number of concurrent connections for this user.                                                                                                                                                                                                                                             |
| CONNECTED\_TIME                | int(11)     | The cumulative number of seconds elapsed while there were connections from this user.                                                                                                                                                                                                           |
| BUSY\_TIME                     | double      | The cumulative number of seconds there was activity on connections from this user.                                                                                                                                                                                                              |
| CPU\_TIME                      | double      | The cumulative CPU time elapsed while servicing this user's connections.                                                                                                                                                                                                                        |
| BYTES\_RECEIVED                | bigint(21)  | The number of bytes received from this user's connections.                                                                                                                                                                                                                                      |
| BYTES\_SENT                    | bigint(21)  | The number of bytes sent to this user's connections.                                                                                                                                                                                                                                            |
| BINLOG\_BYTES\_WRITTEN         | bigint(21)  | The number of bytes written to the [binary log](../../../../server-management/server-monitoring-logs/binary-log/) from this user's connections.                                                                                                                                                 |
| ROWS\_READ                     | bigint(21)  | The number of rows read by this user's connections.                                                                                                                                                                                                                                             |
| ROWS\_SENT                     | bigint(21)  | The number of rows sent by this user's connections.                                                                                                                                                                                                                                             |
| ROWS\_DELETED                  | int(21)     | The number of rows deleted by this user's connections.                                                                                                                                                                                                                                          |
| ROWS\_INSERTED                 | bigint(21)  | The number of rows inserted by this user's connections.                                                                                                                                                                                                                                         |
| ROWS\_UPDATED                  | bigint(21)  | The number of rows updated by this user's connections.                                                                                                                                                                                                                                          |
| KEY\_READ\_HITS                | bigint(21)  | From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115)                                                                                                                               |
| KEY\_READ\_MISSES              | bigint(21)  | From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115)                                                                                                                               |
| SELECT\_COMMANDS               | bigint(21)  | The number of [SELECT](../../../sql-statements/data-manipulation/selecting-data/select.md) commands executed from this user's connections.                                                                                                                                                      |
| UPDATE\_COMMANDS               | bigint(21)  | The number of [UPDATE](../../../sql-statements/data-manipulation/changing-deleting-data/update.md) commands executed from this user's connections.                                                                                                                                              |
| OTHER\_COMMANDS                | bigint(21)  | The number of other commands executed from this user's connections.                                                                                                                                                                                                                             |
| COMMIT\_TRANSACTIONS           | bigint(21)  | The number committed transactions. Note that in autocommit mode every statement is a separate transaction.                                                                                                                                                                                      |
| ROLLBACK\_TRANSACTIONS         | bigint(21)  | The number of transactions that were rolled back.                                                                                                                                                                                                                                               |
| DENIED\_CONNECTIONS            | bigint(21)  | The number of connections denied to this user.                                                                                                                                                                                                                                                  |
| LOST\_CONNECTIONS              | bigint(21)  | The number of this user's connections that were terminated uncleanly.                                                                                                                                                                                                                           |
| ACCESS\_DENIED                 | bigint(21)  | The number of times this user's connections issued commands that were denied.                                                                                                                                                                                                                   |
| EMPTY\_QUERIES                 | bigint(21)  | The number of times this user's connections sent queries to the server that did not return data to the client (a per-user aggregate of the [empty\_queries](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#empty_queries) status variable). |
| TOTAL\_SSL\_CONNECTIONS        | bigint(21)  | The number of [TLS connections](../../../../security/securing-mariadb/encryption/data-in-transit-encryption/) created for this user.                                                                                                                                                            |
| MAX\_STATEMENT\_TIME\_EXCEEDED | bigint(21)  | The number of times a statement was aborted, because it was executed longer than its [MAX\_STATEMENT\_TIME](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/aborting-statements.md) threshold.                                                                       |

## Example

```sql
SELECT * FROM information_schema.USER_STATISTICS\G
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

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
