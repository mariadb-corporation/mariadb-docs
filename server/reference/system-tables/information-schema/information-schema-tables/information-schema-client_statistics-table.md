---
description: >-
  The Information Schema CLIENT_STATISTICS table holds statistics about client
  connections, such as total connections, bytes sent/received, and command
  counts.
---

# Information Schema CLIENT\_STATISTICS Table

The [Information Schema](../) `CLIENT_STATISTICS` table holds statistics about client connections. This is part of the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature, which is not enabled by default.

It contains the following columns:

<table data-header-hidden="false" data-header-sticky><thead><tr><th>Field</th><th>Type</th><th>Notes</th></tr></thead><tbody><tr><td>CLIENT</td><td>VARCHAR(64)</td><td>The IP address or hostname the connection originated from.</td></tr><tr><td>TOTAL_CONNECTIONS</td><td>BIGINT(21)</td><td>The number of connections created for this client.</td></tr><tr><td>CONCURRENT_CONNECTIONS</td><td>BIGINT(21)</td><td>The number of concurrent connections for this client.</td></tr><tr><td>CONNECTED_TIME</td><td>BIGINT(21)</td><td>The cumulative number of seconds elapsed while there were connections from this client.</td></tr><tr><td>BUSY_TIME</td><td>DOUBLE</td><td>The cumulative number of seconds there was activity on connections from this client.</td></tr><tr><td>CPU_TIME</td><td>DOUBLE</td><td>The cumulative CPU time elapsed while servicing this client's connections. Note that this number may be wrong on SMP system if there was a CPU migration for the thread during the execution of the query.</td></tr><tr><td>BYTES_RECEIVED</td><td>BIGINT(21)</td><td>The number of bytes received from this client's connections.</td></tr><tr><td>BYTES_SENT</td><td>BIGINT(21)</td><td>The number of bytes sent to this client's connections.</td></tr><tr><td>BINLOG_BYTES_WRITTEN</td><td>BIGINT(21)</td><td>The number of bytes written to the <a href="../../../../server-management/server-monitoring-logs/binary-log/">binary log</a> from this client's connections.</td></tr><tr><td>ROWS_READ</td><td>BIGINT(21)</td><td>The number of rows read by this client's connections.</td></tr><tr><td>ROWS_SENT</td><td>BIGINT(21)</td><td>The number of rows sent by this client's connections.</td></tr><tr><td>ROWS_DELETED</td><td>BIGINT(21)</td><td>The number of rows deleted by this client's connections.</td></tr><tr><td>ROWS_INSERTED</td><td>BIGINT(21)</td><td>The number of rows inserted by this client's connections.</td></tr><tr><td>ROWS_UPDATED</td><td>BIGINT(21)</td><td>The number of rows updated by this client's connections.</td></tr><tr><td>KEY_READ_HITS</td><td>BIGINT(21)</td><td>From <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115">MariaDB 11.5</a></td></tr><tr><td>KEY_READ_MISSES</td><td>BIGINT(21)</td><td>From <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115">MariaDB 11.5</a></td></tr><tr><td>SELECT_COMMANDS</td><td>BIGINT(21)</td><td>The number of <a href="../../../sql-statements/data-manipulation/selecting-data/select.md">SELECT</a> commands executed from this client's connections.</td></tr><tr><td>UPDATE_COMMANDS</td><td>BIGINT(21)</td><td>The number of <a href="../../../sql-statements/data-manipulation/changing-deleting-data/update.md">UPDATE</a> commands executed from this client's connections.</td></tr><tr><td>OTHER_COMMANDS</td><td>BIGINT(21)</td><td>The number of other commands executed from this client's connections.</td></tr><tr><td>COMMIT_TRANSACTIONS</td><td>BIGINT(21)</td><td>The number of <a href="../../../sql-statements/transactions/commit.md">COMMIT</a> commands issued by this client's connections.</td></tr><tr><td>ROLLBACK_TRANSACTIONS</td><td>BIGINT(21)</td><td>The number of <a href="../../../sql-statements/transactions/rollback.md">ROLLBACK</a> commands issued by this client's connections.</td></tr><tr><td>DENIED_CONNECTIONS</td><td>BIGINT(21)</td><td>The number of connections denied to this client.</td></tr><tr><td>LOST_CONNECTIONS</td><td>BIGINT(21)</td><td>The number of this client's connections that were terminated uncleanly.</td></tr><tr><td>ACCESS_DENIED</td><td>BIGINT(21)</td><td>The number of times this client's connections issued commands that were denied.</td></tr><tr><td>EMPTY_QUERIES</td><td>BIGINT(21)</td><td>The number of times this client's connections sent queries that returned no results to the server.</td></tr><tr><td>TOTAL_SSL_CONNECTIONS</td><td>BIGINT(21)</td><td>The number of <a href="../../../../security/encryption/data-in-transit-encryption/secure-connections-overview.md">TLS connections</a> created for this client.</td></tr><tr><td>MAX_STATEMENT_TIME_EXCEEDED</td><td>BIGINT(21)</td><td>The number of times a statement was aborted, because it was executed longer than its <a href="../../../../ha-and-performance/optimization-and-tuning/query-optimizations/aborting-statements.md">MAX_STATEMENT_TIME</a> threshold.</td></tr></tbody></table>

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
