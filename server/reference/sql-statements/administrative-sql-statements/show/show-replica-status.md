# SHOW REPLICA STATUS

## Syntax

```sql
SHOW { REPLICA | SLAVE} ["connection_name"] STATUS [FOR CHANNEL "connection_name"]
```

or

```sql
SHOW ALL { REPLICAS | SLAVES } STATUS
```

## Description

This statement is to be run on a replica and provides status information on essential parameters of the [replica](../../../../ha-and-performance/standard-replication/replication-overview.md) threads.

{% tabs %}
{% tab title="Current" %}
This statement requires the [REPLICA MONITOR](../../account-management-sql-statements/grant.md#replica-monitor) privilege.
{% endtab %}

{% tab title="< 10.5.9" %}
This statement requires the [REPLICA MONITOR](../../account-management-sql-statements/grant.md#replica-monitor) privilege.
{% endtab %}

{% tab title="< 10.5.2" %}
This statement requires the [REPLICATION SLAVE ADMIN](../../account-management-sql-statements/grant.md#binlog-monitor) privilege.
{% endtab %}
{% endtabs %}

### Multi-Source

The `ALL` and `"connection_name"` options allow you to connect to [many primaries at the same time](../../../../ha-and-performance/standard-replication/multi-source-replication.md).

{% tabs %}
{% tab title="Current" %}
`ALL REPLICAS` gives you a list of all connections to the primary nodes.
{% endtab %}

{% tab title="< 10.5.1" %}
`ALL SLAVES` gives you a list of all connections to the primary nodes.
{% endtab %}
{% endtabs %}

The rows are sorted according to `Connection_name`.

If you specify a `connection_name`, you only get the information about that connection. If `connection_name` is not used, then the name set by `default_master_connection` is used. If the connection name doesn't exist you will get an error:`There is no master connection for 'xxx'`.

**MariaDB starting with** [**10.7.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1070-release-notes)

The `FOR CHANNEL` keyword was added for MySQL compatibility. This is identical to using the channel\_name directly after `SHOW SLAVE`.

### Column Descriptions

The order in which the columns appear depends on the MariaDB version. This means that extracting a column value is best done by comparing the field name instead of using a fixed offset into the row.

{% tabs %}
{% tab title="Current" %}
These columns can also be viewed/extracted from the [INFORMATION\_SCHEMA.SLAVE\_STATUS](../system-tables/information-schema/information-schema-tables/information-schema-slave_status-table.md) table.
{% endtab %}

{% tab title="< 11.6.0" %}
These columns cannot be viewed/extracted from the [INFORMATION\_SCHEMA.SLAVE\_STATUS](../system-tables/information-schema/information-schema-tables/information-schema-slave_status-table.md) table.
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Current" %}
**Connection\_name:** Name of the primary connection. Returned with SHOW ALL REPLICAS STATUS only.

**Slave\_SQL\_State:** State of SQL thread. Returned with SHOW ALL REPLICAS STATUSonly. See [Slave SQL Thread States](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-states/slave-sql-thread-states.md). Slave\_IO\_State: State of I/O thread. See [Slave I/O Thread States](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-states/replica-io-thread-states.md).
{% endtab %}

{% tab title="< 10.5.1" %}
**Connection\_name:** Name of the primary connection. Returned with SHOW ALL SLAVES STATUS only.

**Slave\_SQL\_State:** State of SQL thread. Returned with SHOW ALL SLAVES STATUS only. See [Slave SQL Thread States](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-states/slave-sql-thread-states.md). Slave\_IO\_State: State of I/O thread. See [Slave I/O Thread States](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-states/replica-io-thread-states.md).
{% endtab %}
{% endtabs %}

**Master\_host:** Master host that the replica is connected to.

**Master\_user:** Account user name being used to connect to the primary.

**Master\_port:** The port being used to connect to the primary.

**Connect\_Retry:** Time in seconds between retries to connect. The default is 60. The [CHANGE MASTER TO](../replication-statements/change-master-to.md) statement can set this. The [master-retry-count](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) option determines the maximum number of reconnection attempts.

**Master\_Log\_File:** Name of the primary [binary log](../../../../server-management/server-monitoring-logs/binary-log/) file that the I/O thread is currently reading from.

**Read\_Master\_Log\_Pos:** Position up to which the I/O thread has read in the current primary [binary log](../../../../server-management/server-monitoring-logs/binary-log/) file.

**Relay\_Log\_File:** Name of the relay log file that the SQL thread is currently processing.

**Relay\_Log\_Pos:** Position up to which the SQL thread has finished processing in the current relay log file.

**Relay\_Master\_Log\_File:** Name of the primary [binary log](../../../../server-management/server-monitoring-logs/binary-log/) file that contains the most recent event executed by the SQL thread.

**Slave\_IO\_Running:** Whether the replica I/O thread is running and connected (Yes), running but not connected to a primary (Connecting) or not running (No).

**Slave\_SQL\_Running:** Whether or not the SQL thread is running.

**Replicate\_Do\_DB:** Databases specified for replicating with the [replicate\_do\_db](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) option.

**Replicate\_Ignore\_DB:** Databases specified for ignoring with the [replicate\_ignore\_db](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) option.

**Replicate\_Do\_Table:** Tables specified for replicating with the [replicate\_do\_table](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) option.

**Replicate\_Ignore\_Table:** Tables specified for ignoring with the [replicate\_ignore\_table](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) option.

**Replicate\_Wild\_Do\_Table:** Tables specified for replicating with the [replicate\_wild\_do\_table](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) option.

**Replicate\_Wild\_Ignore\_Table:** Tables specified for ignoring with the [replicate\_wild\_ignore\_table](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) option.

**Last\_Errno:** Alias for Last\_SQL\_Errno (see below)

**Last\_Error:** Alias for Last\_SQL\_Error (see below)

**Skip\_Counter:** Number of events that a replica skips from the master, as recorded in the [sql\_slave\_skip\_counter](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) system variable.

**Exec\_Master\_Log\_Pos:** Position up to which the SQL thread has processed in the current master [binary log](../../../../server-management/server-monitoring-logs/binary-log/) file. Can be used to start a new replica from a current replica with the [CHANGE MASTER TO ... MASTER\_LOG\_POS](../replication-statements/change-master-to.md) option.

**Relay\_Log\_Space:** Total size of all relay log files combined.

**Until\_Condition:** One of four possible values: None, Master, Relay, or Gtid, depending on the respective [START SLAVE UNTIL](../replication-statements/start-replica.md) condition.

**Until\_Log\_File:** The MASTER\_LOG\_FILE value of the [START SLAVE UNTIL](../replication-statements/start-replica.md) condition.

**Until\_Log\_Pos:** The MASTER\_LOG\_POS value of the [START SLAVE UNTIL](../replication-statements/start-replica.md) condition.

**Master\_SSL\_Allowed:** Whether an SSL connection is permitted (Yes), not permitted (No) or permitted but without the replica having SSL support enabled (Ignored)

**Master\_SSL\_CA\_File:** The MASTER\_SSL\_CA option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md) statement.

**Master\_SSL\_CA\_Path:** The MASTER\_SSL\_CAPATH option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md) statement.

**Master\_SSL\_Cert:** The MASTER\_SSL\_CERT option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md) statement.

**Master\_SSL\_Cipher:** The MASTER\_SSL\_CIPHER option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md) statement.

**Master\_SSL\_Key:** The MASTER\_SSL\_KEY option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md) statement.

{% tabs %}
{% tab title="Current" %}
**Seconds\_Behind\_Master:** Difference between the timestamp logged on the master for the event that the replica is currently processing, and the current timestamp on the replica. Zero if the replica is not currently processing an event. With serial replication, seconds\_behind\_master is updated when the SQL thread begins executing a transaction. With [parallel replication](../../../../ha-and-performance/standard-replication/parallel-replication.md), seconds\_behind\_master is updated only after transactions commit. An exception is thrown on the parallel replica to additionally update `seconds_behind_master` when the first transaction received after idling is queued to a worker for execution, to provide a reliable initial value for the duration until a transaction commits.&#x20;

Additional behavior to be aware of:

1. `Seconds_Behind_Master` will update for ignored events, e.g. those skipped due to [sql\_slave\_skip\_counter](../replication-statements/set-global-sql_slave_skip_counter.md).&#x20;
2. On the serial replica, transactions with prior timestamps can update `Seconds_Behind_Master` such that it can go backwards, though this is not true for the parallel replica.&#x20;
3. When configured with [MASTER\_DELAY](../../../../ha-and-performance/standard-replication/delayed-replication.md), as a replicated transaction begins executing (i.e. on a serial or post-idle parallel replica), `Seconds_Behind_Master` will update before delaying, and while delaying occurs will grow to encompass the configured value.&#x20;
4. There is a known issue, tracked by [MDEV-17516](https://jira.mariadb.org/browse/MDEV-17516), such that `Seconds_Behind_Master` will initially present as 0 on replica restart until a replicated transaction begins executing, even if the last replica session was lagging behind when stopped.
{% endtab %}

{% tab title="< 10.11.12 / 10.10.3 / 10.9.5 / 10.8.7 / 10.6.12 / 10.5.19" %}
**Seconds\_Behind\_Master:** Difference between the timestamp logged on the master for the event that the replica is currently processing, and the current timestamp on the replica. Zero if the replica is not currently processing an event. With serial replication, seconds\_behind\_master is updated when the SQL thread begins executing a transaction. With [parallel replication](../../../../ha-and-performance/standard-replication/parallel-replication.md), seconds\_behind\_master is updated only after transactions commit.&#x20;

Additional behavior to be aware of:

1. `Seconds_Behind_Master` will update for ignored events, e.g. those skipped due to [sql\_slave\_skip\_counter](../replication-statements/set-global-sql_slave_skip_counter.md).&#x20;
2. On the serial replica, transactions with prior timestamps can update `Seconds_Behind_Master` such that it can go backwards, though this is not true for the parallel replica.&#x20;
3. When configured with [MASTER\_DELAY](../../../../ha-and-performance/standard-replication/delayed-replication.md), as a replicated transaction begins executing (i.e. on a serial or post-idle parallel replica), `Seconds_Behind_Master` will update before delaying, and while delaying occurs will grow to encompass the configured value.&#x20;
4. There is a known issue, tracked by [MDEV-17516](https://jira.mariadb.org/browse/MDEV-17516), such that `Seconds_Behind_Master` will initially present as 0 on replica restart until a replicated transaction begins executing, even if the last replica session was lagging behind when stopped.
{% endtab %}
{% endtabs %}

**Master\_SSL\_Verify\_Server\_Cert:** The MASTER\_SSL\_VERIFY\_SERVER\_CERT option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md) statement.

**Last\_IO\_Errno:** Error code of the most recent error that caused the I/O thread to stop (also recorded in the replica's error log). 0 means no error. [RESET SLAVE](../replication-statements/reset-replica.md) or [RESET MASTER](../replication-statements/reset-master.md) will reset this value.

**Last\_IO\_Error:** Error message of the most recent error that caused the I/O thread to stop (also recorded in the replica's error log). An empty string means no error. [RESET SLAVE](../replication-statements/reset-replica.md) or [RESET MASTER](../replication-statements/reset-master.md) will reset this value.

**Last\_SQL\_Errno:** Error code of the most recent error that caused the SQL thread to stop (also recorded in the replica's error log). 0 means no error. [RESET SLAVE](../replication-statements/reset-replica.md) or [RESET MASTER](../replication-statements/reset-master.md) will reset this value.

**Last\_SQL\_Error:** Error message of the most recent error that caused the SQL thread to stop (also recorded in the replica's error log). An empty string means no error. [RESET SLAVE](../replication-statements/reset-replica.md) or [RESET MASTER](../replication-statements/reset-master.md) will reset this value.

**Replicate\_Ignore\_Server\_Ids:** List of [server\_ids](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) that are currently being ignored for replication purposes, or an empty string for none, as specified in the IGNORE\_SERVER\_IDS option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md#ignore_server_ids) statement.

**Master\_Server\_Id:** The master's [server\_id](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) value.

**Master\_SSL\_Crl:** The MASTER\_SSL\_CRL option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md) statement.

**Master\_SSL\_Crlpath:** The MASTER\_SSL\_CRLPATH option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md) statement.

**Using\_Gtid:** Whether or not [global transaction ID's](../../../../ha-and-performance/standard-replication/gtid.md) are being used for replication (can be `No`, `Slave_Pos`, or `Current_Pos`).

**Gtid\_IO\_Pos:** Current [global transaction ID](../../../../ha-and-performance/standard-replication/gtid.md) value.

**Replicate\_Do\_Domain\_Ids:** List of [domain\_ids](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) that are currently being recognized for replication purposes, or an empty string for none, as specified in the `DO_DOMAIN_IDS` option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md#do_domain_ids) statement.

**Replicate\_Ignore\_Domain\_Ids:** List of [domain\_ids](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) that are currently being ignored for replication purposes, or an empty string for none, as specified in the `IGNORE_DOMAIN_IDS` option of the [CHANGE MASTER TO](../replication-statements/change-master-to.md#ignore_domain_ids) statement.

**Parallel\_Mode:** The [in-order parallel replication mode](../../../../ha-and-performance/standard-replication/parallel-replication.md#in-order-parallel-replication) as configured by the [`slave_parallel_mode`](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) system variable.

**SQL\_Delay:** Value specified by MASTER\_DELAY in [CHANGE MASTER](../replication-statements/change-master-to.md) (or 0 if none).

**SQL\_Remaining\_Delay:** When the replica is delaying the execution of an event due to `MASTER_DELAY`, this is the number of seconds of delay remaining before the event will be applied. Otherwise, the value is NULL.

**Slave\_SQL\_Running\_State:** The state of the SQL driver threads, same as in [SHOW PROCESSLIST](show-processlist.md). When the replica is delaying the execution of an event due to MASTER\_DELAY, this field displays: "Waiting until `MASTER_DELAY` seconds after master executed event".

**Slave\_DDL\_Groups:** This status variable counts the occurrence of DDL statements. This is a replica-side counter for optimistic parallel replication.

**Slave\_Non\_Transactional\_Groups:** This status variable counts the occurrence of non-transactional event groups. This is a replica-side counter for optimistic parallel replication.

**Slave\_Transactional\_Groups:** This status variable counts the occurrence of transactional event groups. This is a replica-side counter for optimistic parallel replication.

{% tabs %}
{% tab title="Current" %}
**Replicate\_Rewrite\_DB:** Databases specified for replicating and [rewriting](../../../../ha-and-performance/standard-replication/replication-filters.md#replicate_rewrite_db) with the [`replicate_rewrite_db`](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) system variable/option.
{% endtab %}

{% tab title="< 10.11" %}
**Replica\_Rewrite\_DB** is not available.
{% endtab %}
{% endtabs %}

**Retried\_transactions:** The number of times that replicating transactions have been retried due to temporary errors (e.g. deadlocks in parallel replication). Returned with `SHOW ALL SLAVES STATUS` only.

**Max\_relay\_log\_size:** Max [relay log](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) size for this connection. Returned with `SHOW ALL SLAVES STATUS` only.

**Executed\_log\_entries:** Number of binary log events that have been executed, irrespective of error outcome (i.e. if the event execution results in an error, this number will still increase). Returned with `SHOW ALL SLAVES STATUS` only.

**Slave\_received\_heartbeats:** Number of [Heartbeat Log Events](../../../../clients-and-utilities/server-client-software/client-libraries/clientserver-protocol/replication-protocol/heartbeat_log_event.md) that the slave has received. Note this counter does not reset when the slave is restarted; only when a new [CHANGE MASTER](../replication-statements/change-master-to.md) command has executed. Returned with `SHOW ALL SLAVES STATUS` only.

**Slave\_heartbeat\_period:** Configured (by [CHANGE MASTER TO MASTER\_HEARTBEAT\_PERIOD](../replication-statements/change-master-to.md#master_heartbeat_period)) interval in seconds between replication heartbeats. Returned with `SHOW ALL SLAVES STATUS` only.

**Gtid\_Slave\_Pos:** The value of the global variable [gtid\_slave\_pos](../../../../ha-and-performance/standard-replication/gtid.md#gtid_slave_pos), i.e. the GTID of the last event group replicated on a replica server, for each replication domain, as stored in the [gtid\_slave\_pos](../../../../ha-and-performance/standard-replication/gtid.md) system variable. Returned with `SHOW ALL SLAVES STATUS` only.

{% tabs %}
{% tab title="Current" %}
**Master\_last\_event\_time:** Timestamp of the last event read from the primary by the IO thread. NULL until the replica has started and the replica has read one query event from the primary that changes data.

**Slave\_last\_event\_time:** Primary timestamp of the last event committed on the replica. NULL until the replica has started and the replica has read one query event from the primary that changes data.

**Master\_Slave\_time\_diff:** The difference of the above two timestamps. NULL until the replica has started and the replica has read one query event from the primary that changes data.
{% endtab %}

{% tab title="< 11.6" %}
**Master\_last\_event\_time**, **Slave\_last\_event\_time**, and **Master\_Slave\_time\_diff** are not available.
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Current" %}
**Connects\_Tried:** The number of attempts done to connect to the primary. It starts from 0 with [*START* REPLICA](../replication-statements/start-replica.md) (but not [STOP REPLICA](../replication-statements/stop-replica.md)), [RESET REPLICA](../replication-statements/reset-replica.md) or [`CHANGE MASTER TO MASTER_RETRY_COUNT`][], and increments after each connection attempt until one succeeds or, after this reaches `Master_Retry_Count`, aborts the connection.

**Master\_Retry\_Count:** The limit to `Connects_Tried` as configured by [`CHANGE MASTER TO MASTER_RETRY_COUNT`][].

[`CHANGE MASTER TO MASTER_RETRY_COUNT`]: ../replication-statements/change-master-to.md#master_retry_count
{% endtab %}

{% tab title="< 12.0" %}
**Connects\_Tried:** and **Master\_Retry\_Count:** are not available.
If the Performance Schema is enabled, [`replication\_connection\_configuration`](../system-tables/performance-schema/performance-schema-tables/performance-schema-replication_connection_configuration-table.md) has `CONNECTION_RETRY_COUNT` available as an older alternative to `Master_Retry_Count`.
{% endtab %}
{% endtabs %}

## Examples

If you issue this statement using the [mariadb](../../../../clients-and-utilities/mariadb-client/) client, you can use a `\G` statement terminator rather than a semicolon to obtain a more readable vertical layout.

```sql
SHOW SLAVE STATUS\G
*************************** 1. row ***************************
                Slave_IO_State: Waiting for master to send event
                   Master_Host: db01.example.com
                   Master_User: replicant
                   Master_Port: 3306
                 Connect_Retry: 60
               Master_Log_File: mariadb-bin.000021
           Read_Master_Log_Pos: 17315
                Relay_Log_File: relay-bin.000042
                 Relay_Log_Pos: 17446
         Relay_Master_Log_File: mariadb-bin.000021
              Slave_IO_Running: Yes
             Slave_SQL_Running: Yes
               Replicate_Do_DB: 
           Replicate_Ignore_DB: 
            Replicate_Do_Table: 
        Replicate_Ignore_Table: 
       Replicate_Wild_Do_Table: 
   Replicate_Wild_Ignore_Table: 
                    Last_Errno: 0
                    Last_Error: 
                  Skip_Counter: 0
           Exec_Master_Log_Pos: 17146
               Relay_Log_Space: 17972
               Until_Condition: None
                Until_Log_File: 
                 Until_Log_Pos: 0
            Master_SSL_Allowed: Yes
            Master_SSL_CA_File: 
            Master_SSL_CA_Path: 
               Master_SSL_Cert: 
             Master_SSL_Cipher: 
                Master_SSL_Key: 
         Seconds_Behind_Master: 6
 Master_SSL_Verify_Server_Cert: No
                 Last_IO_Errno: 0
                 Last_IO_Error: 
                Last_SQL_Errno: 0
                Last_SQL_Error: 
   Replicate_Ignore_Server_Ids: 
              Master_Server_Id: 1
                Master_SSL_Crl: 
            Master_SSL_Crlpath: 
                    Using_Gtid: Slave_Pos
                   Gtid_IO_Pos: 0-1-2042
       Replicate_Do_Domain_Ids: 
   Replicate_Ignore_Domain_Ids: 
                 Parallel_Mode: optimistic
                     SQL_Delay: 0
           SQL_Remaining_Delay: NULL
       Slave_SQL_Running_State: Updating
              Slave_DDL_Groups: 1
Slave_Non_Transactional_Groups: 0
    Slave_Transactional_Groups: 2041
          Replicate_Rewrite_DB:
```

```sql
SHOW ALL SLAVES STATUS\G
*************************** 1. row ***************************
               Connection_name: 
               Slave_SQL_State: Updating
                Slave_IO_State: Waiting for master to send event
                   Master_Host: db01.example.com
                   Master_User: replicant
                   Master_Port: 3306
                 Connect_Retry: 60
               Master_Log_File: mariadb-bin.000021
           Read_Master_Log_Pos: 17315
                Relay_Log_File: relay-bin.000042
                 Relay_Log_Pos: 17446
         Relay_Master_Log_File: mariadb-bin.000021
              Slave_IO_Running: Yes
             Slave_SQL_Running: Yes
               Replicate_Do_DB: 
           Replicate_Ignore_DB: 
            Replicate_Do_Table: 
        Replicate_Ignore_Table: 
       Replicate_Wild_Do_Table: 
   Replicate_Wild_Ignore_Table: 
                    Last_Errno: 0
                    Last_Error: 
                  Skip_Counter: 0
           Exec_Master_Log_Pos: 17146
               Relay_Log_Space: 17972
               Until_Condition: None
                Until_Log_File: 
                 Until_Log_Pos: 0
            Master_SSL_Allowed: Yes
            Master_SSL_CA_File: 
            Master_SSL_CA_Path: 
               Master_SSL_Cert: 
             Master_SSL_Cipher: 
                Master_SSL_Key: 
         Seconds_Behind_Master: 6
 Master_SSL_Verify_Server_Cert: No
                 Last_IO_Errno: 0
                 Last_IO_Error: 
                Last_SQL_Errno: 0
                Last_SQL_Error: 
   Replicate_Ignore_Server_Ids: 
              Master_Server_Id: 1
                Master_SSL_Crl: 
            Master_SSL_Crlpath: 
                    Using_Gtid: Slave_Pos
                   Gtid_IO_Pos: 0-1-2042
       Replicate_Do_Domain_Ids: 
   Replicate_Ignore_Domain_Ids: 
                 Parallel_Mode: optimistic
                     SQL_Delay: 0
           SQL_Remaining_Delay: NULL
       Slave_SQL_Running_State: Updating
              Slave_DDL_Groups: 1
Slave_Non_Transactional_Groups: 0
    Slave_Transactional_Groups: 2041
          Replicate_Rewrite_DB: 
          Retried_transactions: 0
            Max_relay_log_size: 1073741824
          Executed_log_entries: 6330
     Slave_received_heartbeats: 0
        Slave_heartbeat_period: 60.000
                Gtid_Slave_Pos: 0-1-2041
        Master_last_event_time: 2024-12-12 06:53:52
         Slave_last_event_time: 2024-12-12 06:53:50
        Master_Slave_time_diff: 2
```

You can also access some of the variables directly from status variables:

```sql
SET @@default_master_connection="test" ;
show status like "%slave%"

Variable_name   Value
Com_show_slave_hosts    0
Com_show_slave_status   0
Com_start_all_slaves    0
Com_start_slave 0
Com_stop_all_slaves     0
Com_stop_slave  0
Rpl_semi_sync_slave_status      OFF
Slave_connections       0
Slave_heartbeat_period  1800.000
Slave_open_temp_tables  0
Slave_received_heartbeats       0
Slave_retried_transactions      0
Slave_running   OFF
Slaves_connected        0
Slaves_running  1
```

## See Also

* [MariaDB replication](../../../../ha-and-performance/standard-replication/)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
