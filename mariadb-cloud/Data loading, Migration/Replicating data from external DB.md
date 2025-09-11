# Replicating Data from an External Database to SkySQL

MariaDB SkySQL customers can configure inbound replication from both **MySQL** and **MariaDB** to a compatible MariaDB running in SkySQL. This guide will walk you through setting up replication for both MySQL and MariaDB as the source databases.

For additional information about the stored procedures used to configure replication with Replicated Transactions services, see [SkySQL Replication Helper Procedures for Replicated Transactions](https://docs.skysql.com/Reference%20Guide/Sky%20Stored%20Procedures/).

## Requirements

1. **For MySQL** :
   * Replication must be configured using the binary log file and position (GTID is not supported).
2. **For MariaDB**:
   * GTID-based replication can be used instead of binary log for complex replication setups.

Ensure that the external primary server is compatible with the version of MariaDB used in SkySQL.

## Step 1: Obtain the Log File and Position

### MySQL:

If using MySQL, obtain the binary log file and position from which to start replication. This can be retrieved from a logical dump or `xtrabackup_binlog_info` file.\
If the source database is idle, use the `SHOW MASTER STATUS` statement to get the current binary log file and position:

```sql
SHOW MASTER STATUS;
```

### MariaDB:

For MariaDB, replication can be done using GTID. Obtain the GTID position using the `@@current_gtid_pos` variable:

```sql
SELECT @@current_gtid_pos;
```

## Step 2: Configure the Log File and Position

### For MySQL (Binary Log Position Based)

Configure the binary log file and position on the SkySQL service using the following stored procedure:

```sql
CALL sky.change_external_primary('mysql1.example.com', 3306, 'mysql-bin.000001', 154, false);
```

This procedure can be referenced in the official documentation:\
[sky.change\_external\_primary()](https://docs.skysql.com/Reference%20Guide/Sky%20Stored%20Procedures/#change_external_primary)

This will return a `GRANT` statement that needs to be executed on the external MySQL server:

```sql
GRANT REPLICATION SLAVE ON *.* TO 'skysql_replication'@'%' IDENTIFIED BY '<password_hash>';
```

For MariaDB (GTID Based) if preferred refer to [sky.change\_external\_primary\_gtid()](https://docs.skysql.com/Reference%20Guide/Sky%20Stored%20Procedures/#change_external_primary_gtid)

## Step 3: Start Replication

Once the configuration is complete, start replication on the SkySQL service using the following command:

```sql
CALL sky.start_replication();
```

This will return a confirmation message such as:

```sql
+----------------------------------------+
| Message                                |
+----------------------------------------+
| External replication running normally. |
+----------------------------------------+
```

You can find the documentation for this procedure [here](<../Reference Guide/Sky Stored Procedures.md#start_replication>).

## Step 4: Check Replication Status

To verify the status of replication, you can run the following stored procedure on SkySQL:

```sql
CALL sky.replication_status()\G;
```

The output will provide detailed information about the replication process, including the position of the replication logs and the state of the slave threads. An example output is shown below:

```sql
*************************** 1. row ***************************
                Slave_IO_State: Waiting for master to send event
                   Master_Host: mariadb1.example.com
                   Master_User: skysql_replication
                   Master_Port: 3306
                 Connect_Retry: 60
               Master_Log_File: mysql-bin.000001
           Read_Master_Log_Pos: 462
                Relay_Log_File: mariadb-relay-bin.000002
                 Relay_Log_Pos: 665
         Relay_Master_Log_File: mysql-bin.000001
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
           Exec_Master_Log_Pos: 462
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
              Master_Server_Id: 200
                Master_SSL_Crl:
            Master_SSL_Crlpath:
                    Using_Gtid: No
                   Gtid_IO_Pos:
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

You can reference the replication status procedure [here](<../Reference Guide/Sky Stored Procedures.md#replication_status>).\


## Compatibility Notes

* **For MySQL**: Only binary log-based replication is supported; GTID is not available.
* **For MariaDB**: GTID-based replication can be used.

### Supported MariaDB Versions for Replication

Ensure that the external primary server uses a supported version of MariaDB, which must be the same or older than the SkySQL service version.

* **For SkySQL using ES 10.6**:
  * MariaDB Server 10.2, 10.3, 10.4, 10.5, 10.6
* **For SkySQL using ES 10.5**:
  * MariaDB Server 10.2, 10.3, 10.4, 10.5
* **For SkySQL using ES 10.4**:
  * MariaDB Server 10.2, 10.3, 10.4
