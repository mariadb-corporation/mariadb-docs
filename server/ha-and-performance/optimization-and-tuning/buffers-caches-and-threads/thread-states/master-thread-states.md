# Master Thread States

This article documents thread states that are related to [replication](../../../standard-replication/replication-overview.md) master threads. These correspond to the `STATE` values listed by the [SHOW PROCESSLIST](../../../../reference/sql-statements/administrative-sql-statements/show/show-processlist.md) statement or in the [Information Schema PROCESSLIST Table](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) as well as the `PROCESSLIST_STATE` value listed in the [Performance Schema threads Table](../../../../reference/system-tables/performance-schema/performance-schema-tables/performance-schema-threads-table.md).

| Value                                                                 | Description                                                                                                                                             |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Finished reading one binlog; switching to next binlog                 | After completing one [binary log](../../../../server-management/server-monitoring-logs/binary-log/), the next is being opened for sending to the slave. |
| Master has sent all binlog to slave; waiting for binlog to be updated | All events have been read from the binary logs and sent to the slave. Now waiting for the binary log to be updated with new events.                     |
| Sending binlog event to slave                                         | An event has been read from the [binary log](../../../../server-management/server-monitoring-logs/binary-log/),  and is now being sent to the slave.    |
| Waiting to finalize termination                                       | State that only occurs very briefly while the thread is terminating.                                                                                    |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
