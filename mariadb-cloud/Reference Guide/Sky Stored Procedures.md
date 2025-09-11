# SkySQL Stored Procedures

## change_external_primary

Executes the [CHANGE MASTER TO](https://mariadb.com/kb/en/change-master-to/) statement to configure inbound replication from an external primary server based on binary log file and position.

```sql
CALL sky.change_external_primary(
   host VARCHAR(255),
   port INT,
   logfile TEXT,
   logpos LONG ,
   use_ssl_encryption BOOLEAN
);
```

```sql

-- Run_this_grant_on_your_external_primary                                                                      |
GRANT REPLICATION SLAVE ON *.* TO 'skysql_replication'@'%' IDENTIFIED BY '<password_hash>';                  |

```

## change_connect_retry

Sets the connection retry interval for the external replication master.

```sql
CALL change_connect_retry(connect_retry INT);
```

If the value is NULL, a default retry interval of 60 seconds will be used.

## change_external_primary_gtid

Executes the [CHANGE MASTER TO](https://mariadb.com/kb/en/change-master-to/) statement to configure inbound replication from an external primary server based on the provided GTID.

```sql
CALL sky.change_external_primary_gtid(
   host VARCHAR(255),
   port INT,
   gtid VARCHAR(60),
   use_ssl_encryption BOOLEAN
);
```

```sql
-- Run_this_grant_on_your_external_primary
GRANT REPLICATION SLAVE ON *.* TO 'skysql_replication'@'%' IDENTIFIED BY '<password_hash>';
```

## change_heartbeat_period

Sets the heartbeat period for the external replication master.

```sql
CALL change_heartbeat_period(heartbeat_period DECIMAL(10,3));
```

If the value is NULL, a default heartbeat period of 5 seconds will be used.

## change_replica_delay

Sets the replication delay for the external replication master.

```sql
CALL change_replica_delay(replica_delay INT);
```

If the value is NULL, a default delay of 1 second will be used.

## change_use_ssl_encryption

Toggles the SSL encryption setting for the external replication master.

```sql
CALL change_use_ssl_encryption(use_ssl_encryption BOOLEAN);
```

If the value is NULL, SSL encryption will be enabled by default.

## gtid_status

Provides a list of GTID-related [system variables](https://mariadb.com/kb/en/server-system-variables/).

```sql
CALL sky.gtid_status();
```

```sql
+-------------------+---------------------------+
| Variable_name     | Value                     |
+-------------------+---------------------------+
| gtid_binlog_pos   | 435700-435700-122         |
| gtid_binlog_state | 435700-435700-122         |
| gtid_current_pos  | 0-100-1,435700-435700-122 |
| gtid_slave_pos    | 0-100-1                   |
+-------------------+---------------------------+
```

## kill_session

Kills any non-root or non-SkySQL threads, similar to the [KILL](https://mariadb.com/kb/en/kill/) statement.

```sql
CALL sky.kill_session(IN thread BIGINT);
```

## replication_grants

Provides a [GRANT](https://mariadb.com/kb/en/grant/) statement to run on an external primary server when configuring inbound replication.

```sql
CALL sky.replication_grants();
```

```sql
-- Run_this_grant_on_your_external_primary
GRANT REPLICATION SLAVE ON *.* TO 'skysql_replication'@'%' IDENTIFIED BY '<password_hash>';
```

## replication_status

Executes the [SHOW REPLICA STATUS](https://mariadb.com/kb/en/show-replica-status/) statement to obtain the status of inbound replication.

```sql
CALL sky.replication_status()\G
```

- 
    
    ```
    *************************** 1. row ***************************
                    Slave_IO_State: Waiting for master to send event
                       Master_Host: mariadb1.example.com
                       Master_User: skysql_replication
                       Master_Port: 3306
                     Connect_Retry: 60
                   Master_Log_File: mariadb-bin.000001
               Read_Master_Log_Pos: 558
                    Relay_Log_File: mariadb-relay-bin.000002
                     Relay_Log_Pos: 674
             Relay_Master_Log_File: mariadb-bin.000001
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
               Exec_Master_Log_Pos: 558
                   Relay_Log_Space: 985
                   Until_Condition: None
                    Until_Log_File:
                     Until_Log_Pos: 0
                Master_SSL_Allowed: No
                Master_SSL_CA_File:
                Master_SSL_CA_Path:
                   Master_SSL_Cert:
                 Master_SSL_Cipher:
                    Master_SSL_Key:
             Seconds_Behind_Master: 0
     Master_SSL_Verify_Server_Cert: No
                     Last_IO_Errno: 0
                     Last_IO_Error:
                    Last_SQL_Errno: 0
                    Last_SQL_Error:
       Replicate_Ignore_Server_Ids:
                  Master_Server_Id: 100
                    Master_SSL_Crl:
                Master_SSL_Crlpath:
                        Using_Gtid: Slave_Pos
                       Gtid_IO_Pos: 0-100-1
           Replicate_Do_Domain_Ids:
       Replicate_Ignore_Domain_Ids:
                     Parallel_Mode: conservative
                         SQL_Delay: 0
               SQL_Remaining_Delay: NULL
           Slave_SQL_Running_State: Slave has read all relay log; waiting for more updates
                  Slave_DDL_Groups: 0
    Slave_Non_Transactional_Groups: 0
        Slave_Transactional_Groups: 0
    
    ```
    

## reset_replication

Executes the [RESET REPLICA](https://mariadb.com/kb/en/reset-replica/) statement to clear inbound replication configuration.

```sql
CALL sky.reset_replication();
```

```sql
+------------------------+
| Message                |
+------------------------+
| Replica has been reset |
+------------------------+
```

## set_master_ssl

Toggles the `MASTER_SSL` replication option using the [CHANGE MASTER TO](https://mariadb.com/kb/en/change-master-to/) statement.

```sql
CALL sky.set_master_ssl();
```

## skip_repl_error

This stored procedure can be used to ignore a transaction that is causing a replication error.

Executes the [STOP REPLICA](https://mariadb.com/kb/en/stop-replica/) statement, then sets the [sql_slave_skip_counter](https://mariadb.com/kb/en/replication-and-binary-log-system-variables/#sql_slave_skip_counter) system variable, and then executes the [START REPLICA](https://mariadb.com/kb/en/start-replica/) statement to skip a single transaction. Does not currently work with GTID.

```sql
CALL sky.skip_repl_error();
```

## start_replication

Executes the [START REPLICA](https://mariadb.com/kb/en/start-replica/) statement to start inbound replication from an external primary.

```sql
CALL sky.start_replication();
```

```sql
+----------------------------------------+
| Message                                |
+----------------------------------------+
| External replication running normally. |
+----------------------------------------+
```

## start_replication_until

Start the external replication until a specified relay log file and position. It checks if the replication threads are running and starts the replication if they are not. It also provides feedback on the replication status.

```sql
CALL start_replication_until(relay_log_file TEXT, relay_log_pos LONG);
```

## start_replication_until_gtid

Starts the external replication until the specified GTID position. It checks if the replication threads are running and starts the replication if they are not. It also provides feedback on the replication status.

```sql
CALL start_replication_until_gtid(master_gtid_pos TEXT);
```

## stop_replication

Executes the [STOP REPLICA](https://mariadb.com/kb/en/stop-replica/) statement to stop inbound replication from an external primary.

```sql
CALL sky.stop_replication();
```

```sql
+---------------------------------+
| Message                         |
+---------------------------------+
| Replication is down or disabled |
+---------------------------------+
```
