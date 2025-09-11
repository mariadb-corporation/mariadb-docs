# Replicating data from MariaDB Cloud to external database

SkySQL customers can configure outbound replication from a Replicated Transactions service to a compatible MariaDB Server running elsewhere - could be your data center, self-managed MariaDB DB on the cloud or even other managed services like AWS RDS.

SkySQL uses stored procedures to configure replication to other MariaDB or MySQL database servers.

For additional information about the stored procedures used to configure replication with Replicated Transactions services, see [SkySQL Replication Helper Procedures for Replicated Transactions](<../Reference Guide/Sky Stored Procedures.md>)

## Requirements

To configure outbound replication from your Replicated Transactions service in SkySQL to an external replica server using MariaDB Server, the following requirements must be met:

* The external replica server must use a supported version of MariaDB Server, and the external replica server must use a version in the same or newer release series as the version used by the SkySQL service.
* When the SkySQL service uses **ES 10.6**, the following versions are supported for the external replica server:
  * MariaDB Server 10.6
* When the SkySQL service uses **ES 10.5**, the following versions are supported for the external replica server:
  * MariaDB Server 10.5
  * MariaDB Server 10.6
* When the SkySQL service uses **ES 10.4**, the following versions are supported for the external replica server:
  * MariaDB Server 10.4
  * MariaDB Server 10.5
  * MariaDB Server 10.6

## Create User for Outbound Replication

With the default database admin user provided, create an external\_replication user as seen below.

```sql
CREATE USER 'replication_user'@'%' IDENTIFIED BY 'bigs3cret';
GRANT REPLICATION SLAVE ON *.* TO ‘external_replication’@'hostname';
```

## Check User Account

**On the SkySQL service**, confirm that the new user has sufficient privileges by executing&#x20;

```sql
SHOW GRANTS FOR 'external_replication'@'%';
+-------------+
| Grants for external_replication@%                                                                                                              |
+-------------+
| GRANT REPLICATION SLAVE, SLAVE MONITOR ON *.* TO `external_replication`@`%` IDENTIFIED BY PASSWORD '*CCD3A959D6A004B9C3807B728BC2E55B67E10518' |
+-------------+
```

## Add External Replica to Allowlist

**On the SkySQL Customer Portal**, add the IP address of the external replica server to the SkySQL service's [allowlist](<../Security/Configuring Firewall.md>)

* Click ‘Manage’→ ‘Manage Allowlist’ to add the IP address to the allowed list.

{% hint style="info" %}
If your ‘external replica server’ is also running on SkySQL (say, for DR), you can find the outbound IP address from the ‘Details’ tab (select on the Service name on the dashboard, then click ‘Details’).
{% endhint %}

## Obtain GTID Position

**On the SkySQL service**, obtain the GTID position from which to start replication.

When you want to start replication from the most recent transaction, the current GTID position can be obtained by querying the value of the 'gtid\_current\_pos:

```sql
SHOW GLOBAL VARIABLES
   LIKE 'gtid_current_pos';
+------------------+-------------------+
| Variable_name    | Value             |
+------------------+-------------------+
| gtid_current_pos | 435700-435700-124 |
+------------------+-------------------+
```

## Configure GTID Position

**On the external replica server**, configure the GTID position from which to start replication.

The GTID position can be configured by setting the `gtid_slave_pos` variable:

```sql
SET GLOBAL gtid_slave_pos='435700-435700-124';
```

## Configure Replication

**On the external replica server**, configure replication using the connection parameters for your SkySQL service.

Replication can be configured using the `CHANGE MASTER TO` SQL statement:

```sql
CHANGE MASTER TO
   MASTER_HOST='FULLY_QUALIFIED_DOMAIN_NAME',
   MASTER_PORT=TCP_PORT,
   MASTER_USER='external_replication',
   MASTER_PASSWORD='my_password',
   MASTER_SSL=1,
   MASTER_SSL_CA='~/PATH_TO_PEM_FILE',
   MASTER_USE_GTID=slave_pos;
```

* Replace `FULLY_QUALIFIED_DOMAIN_NAME` with the Fully Qualified Domain Name of your service.
* Replace `TCP_PORT` with the read-write or read-only port of your service.
* Replace `~/PATH_TO_PEM_FILE` with the path to the certificate authority chain (.pem) file.

## Start Replication

**On the external replica server**, start replication.

Replication can be started using the `START REPLICA` SQL statement:

```sql
START REPLICA;
```

## Finally, Check Replication Status

**On the external replica server**, check replication status.

Replication status can be checked using the `SHOW REPLICA STATUS` SQL statement:

```sql
SHOW REPLICA STATUS \G

*************************** 1. row ***************************
                Slave_IO_State: Waiting for master to send event
                   Master_Host: my-service.mdb0002147.db.skysql.net
                   Master_User: external_replication
                   Master_Port: 5003
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
            Master_SSL_Allowed: Yes
            Master_SSL_CA_File: /var/lib/mysql/skysql_chain.pem
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
              Master_Server_Id: 435701
                Master_SSL_Crl: /var/lib/mysql/skysql_chain.pem
            Master_SSL_Crlpath:
                    Using_Gtid: Slave_Pos
                   Gtid_IO_Pos: 435700-435700-127
       Replicate_Do_Domain_Ids:
   Replicate_Ignore_Domain_Ids:
                 Parallel_Mode: optimistic
                     SQL_Delay: 0
           SQL_Remaining_Delay: NULL
       Slave_SQL_Running_State: Slave has read all relay log; waiting for more updates
              Slave_DDL_Groups: 0
Slave_Non_Transactional_Groups: 0
    Slave_Transactional_Groups: 0

```
