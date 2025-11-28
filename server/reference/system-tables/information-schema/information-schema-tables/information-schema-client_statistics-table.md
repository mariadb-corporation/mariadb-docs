---
description: >-
  The Information Schema CLIENT_STATISTICS table holds statistics about client
  connections, such as total connections, bytes sent/received, and command
  counts.
---

# Information Schema CLIENT\_STATISTICS Table

The [Information Schema](../) `CLIENT_STATISTICS` table holds statistics about client connections. This is part of the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature, which is not enabled by default.

It contains the following columns:

| Field                          | Type        | Notes                                                                                                                                                                                                                     |
| ------------------------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CLIENT                         | VARCHAR(64) | The IP address or hostname the connection originated from.                                                                                                                                                                |
| TOTAL\_CONNECTIONS             | BIGINT(21)  | The number of connections created for this client.                                                                                                                                                                        |
| CONCURRENT\_CONNECTIONS        | BIGINT(21)  | The number of concurrent connections for this client.                                                                                                                                                                     |
| CONNECTED\_TIME                | BIGINT(21)  | The cumulative number of seconds elapsed while there were connections from this client.                                                                                                                                   |
| BUSY\_TIME                     | DOUBLE      | The cumulative number of seconds there was activity on connections from this client.                                                                                                                                      |
| CPU\_TIME                      | DOUBLE      | The cumulative CPU time elapsed while servicing this client's connections. Note that this number may be wrong on SMP system if there was a CPU migration for the thread during the execution of the query.                |
| BYTES\_RECEIVED                | BIGINT(21)  | The number of bytes received from this client's connections.                                                                                                                                                              |
| BYTES\_SENT                    | BIGINT(21)  | The number of bytes sent to this client's connections.                                                                                                                                                                    |
| BINLOG\_BYTES\_WRITTEN         | BIGINT(21)  | The number of bytes written to the [binary log](../../../../server-management/server-monitoring-logs/binary-log/) from this client's connections.                                                                         |
| ROWS\_READ                     | BIGINT(21)  | The number of rows read by this client's connections.                                                                                                                                                                     |
| ROWS\_SENT                     | BIGINT(21)  | The number of rows sent by this client's connections.                                                                                                                                                                     |
| ROWS\_DELETED                  | BIGINT(21)  | The number of rows deleted by this client's connections.                                                                                                                                                                  |
| ROWS\_INSERTED                 | BIGINT(21)  | The number of rows inserted by this client's connections.                                                                                                                                                                 |
| ROWS\_UPDATED                  | BIGINT(21)  | The number of rows updated by this client's connections.                                                                                                                                                                  |
| KEY\_READ\_HITS                | BIGINT(21)  | From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115)                                                         |
| KEY\_READ\_MISSES              | BIGINT(21)  | From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115)                                                         |
| SELECT\_COMMANDS               | BIGINT(21)  | The number of [SELECT](../../../sql-statements/data-manipulation/selecting-data/select.md) commands executed from this client's connections.                                                                              |
| UPDATE\_COMMANDS               | BIGINT(21)  | The number of [UPDATE](../../../sql-statements/data-manipulation/changing-deleting-data/update.md) commands executed from this client's connections.                                                                      |
| OTHER\_COMMANDS                | BIGINT(21)  | The number of other commands executed from this client's connections.                                                                                                                                                     |
| COMMIT\_TRANSACTIONS           | BIGINT(21)  | The number of [COMMIT](../../../sql-statements/transactions/commit.md) commands issued by this client's connections.                                                                                                      |
| ROLLBACK\_TRANSACTIONS         | BIGINT(21)  | The number of [ROLLBACK](../../../sql-statements/transactions/rollback.md) commands issued by this client's connections.                                                                                                  |
| DENIED\_CONNECTIONS            | BIGINT(21)  | The number of connections denied to this client.                                                                                                                                                                          |
| LOST\_CONNECTIONS              | BIGINT(21)  | The number of this client's connections that were terminated uncleanly.                                                                                                                                                   |
| ACCESS\_DENIED                 | BIGINT(21)  | The number of times this client's connections issued commands that were denied.                                                                                                                                           |
| EMPTY\_QUERIES                 | BIGINT(21)  | The number of times this client's connections sent queries that returned no results to the server.                                                                                                                        |
| TOTAL\_SSL\_CONNECTIONS        | BIGINT(21)  | The number of [TLS connections](../../../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md) created for this client.                                                      |
| MAX\_STATEMENT\_TIME\_EXCEEDED | BIGINT(21)  | The number of times a statement was aborted, because it was executed longer than its [MAX\_STATEMENT\_TIME](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/aborting-statements.md) threshold. |

#### Example

```sql
SELECT * FROM information_schema.CLIENT_STATISTICS\G
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
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
