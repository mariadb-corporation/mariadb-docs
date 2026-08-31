# Step 3: Start and Configure MariaDB Enterprise Server on Replica Servers

## Overview

This page details step 3 of the 7-step procedure "[Deploy Primary/Replica Topology](./)".

This page starts and configures a MariaDB Enterprise Server 11.4 to operate as a replica server in MariaDB Replication.

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Stop the Enterprise Server Service

The installation process might have started the Enterprise Server service. The service should be stopped prior to making configuration changes.

On each Enterprise Server node, stop the MariaDB Enterprise Server service:

```bash
$ sudo systemctl stop mariadb
```

## Configure Enterprise Server

Enterprise Server nodes require that you set the following system variables and options:

<table><thead><tr><th width="231.7777099609375">System Variable/Option</th><th>Description</th></tr></thead><tbody><tr><td><a href="../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables">bind_address</a></td><td>The network socket Enterprise Server listens on for incoming TCP/IP client connections. On Debian or Ubuntu, this system variable must be set to override the 127.0.0.1 default configuration.</td></tr><tr><td><a href="../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin">log_bin</a></td><td>Enables binary logging and sets the name of the binlog file.</td></tr><tr><td><a href="../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#server_id">server_id</a></td><td>Unique numeric identifier for each Enterprise Server node.</td></tr></tbody></table>

MariaDB Enterprise Server also supports group commit.

### Parallel Replication

Writes to the primary server that are group committed or logged with a Global Transaction ID in different replication domains can be applied on the replica server using parallel threads to improve performance.

<table><thead><tr><th width="229.4073486328125">System Variable/Option</th><th>Description</th></tr></thead><tbody><tr><td><a href="../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_parallel_threads">slave_parallel_threads</a></td><td>Sets the number of threads the replica server uses to apply replication events in parallel. Use a non-zero value to enable Parallel Replication.</td></tr><tr><td><a href="../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_parallel_mode">slave_parallel_mode</a></td><td>Sets how the replica server applies replicated transactions.</td></tr></tbody></table>

### Example Configuration

On each Enterprise Server node, edit a configuration file and set these system variables and options:

```
[mariadb]
bind_address = 0.0.0.0
log_bin      = mariadb-bin.log
server_id    = 1
```

Set the server\_id option to a value that is unique for each Enterprise Server node.

## Initialize Replica Database

When deploying a new replica server to an existing system, back up the primary server and restore it on the replica server to initialize the database.

### Back up the Primary Server

Use [MariaDB Backup](../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md) to back up the primary server.

1. On the primary server, take a full backup:

```bash
$ sudo mariadb-backup --backup \
      --user=mariadb-backup_user \
      --password=mariadb-backup_passwd \
      --target-dir=/data/backup/replica_backup
```

Confirm successful completion of the backup operation.

2. On the primary server, prepare the backup:

```bash
$ sudo mariadb-backup --prepare \
      --target-dir=/data/backup/replica_backup
```

Confirm successful completion of the prepare operation.

### Restore the Backup to the Replica Server

1. **On the primary server**, copy the backup directory to each replica server:

```bash
$ sudo rsync -av /data/backup/replica_backup 192.0.2.11:/data/backup/
```

2. **On the replica server**, move the default [datadir](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables) to another location:

```bash
$ sudo mv /var/lib/mysql /var/lib/mysql_backup
```

3. **On the replica server**, use [MariaDB Backup](../../../server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview.md) to restore the backup to the [datadir](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir):

```bash
$ sudo mariadb-backup --copy-back \
   --target-dir=/data/backup/replica_backup
```

4. **On the replica server**, set the file permissions for the [datadir](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables):

```bash
$ sudo chown -R mysql:mysql /var/lib/mysql
```

## Start Replica Server

Start MariaDB Enterprise Server. If the Enterprise Server process is already running, restart it to apply the changes from the configuration file.

```bash
$ systemctl start mariadb
```

For additional information, see "[Starting and Stopping MariaDB](../../../server-management/starting-and-stopping-mariadb/)".

### Set the Global Transaction ID Position

If the replica server was restored from a backup of the primary, set the GTID position.

1. Get the GTID position that corresponds to the restored backup. This can be found in the xtrabackup\_binlong\_info file.

```bash
$ cat xtrabackup_binlog_info
mariadb-bin.000096 568 0-1-2001,1-2-5139
```

The GTID position from the above output is `0-1-2001,1-2-5139`.

2. Connect to the replica server:

```bash
$ sudo mariadb
```

Set the [gtid\_slave\_pos](../../../ha-and-performance/standard-replication/gtid.md#gtid_slave_pos) system variable to the GTID position:

```sql
SET GLOBAL gtid_slave_pos='0-1-2001,1-2-5139';
```

### Start Replication

1. Execute the CHANGE MASTER TO statement to configure the replica server to connect to the primary server at this position:

```sql
CHANGE MASTER TO
   MASTER_USER = "repl",
   MASTER_HOST = "192.0.2.10",
   MASTER_PASSWORD = "repl_passwd",
   MASTER_USE_GTID = slave_pos;
```

The above statement configures the replica server to connect to a primary server located at 192.0.2.10 using the repl user account. This account must first be configured on the primary server.

2. Use the [START REPLICA](../../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md) statement to start replication:

```sql
START REPLICA;
```

3. Use [SHOW REPLICA STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-replica-status.md) statement to confirm replication is running:

```sql
SHOW REPLICA STATUS\G

*************************** 1. row ***************************
                Slave_IO_State: Waiting for master to send event
                   Master_Host: 192.0.2.10
                   Master_User: repl
                   Master_Port: 3306
                 Connect_Retry: 60
               Master_Log_File: mariadb-bin.000001
           Read_Master_Log_Pos: 645
                Relay_Log_File: li282-189-relay-bin.000002
                 Relay_Log_Pos: 946
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
           Exec_Master_Log_Pos: 645
               Relay_Log_Space: 1259
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
              Master_Server_Id: 1
                Master_SSL_Crl:
            Master_SSL_Crlpath:
                    Using_Gtid: Slave_Pos
                   Gtid_IO_Pos: 0-1-2
       Replicate_Do_Domain_Ids:
   Replicate_Ignore_Domain_Ids:
                 Parallel_Mode: optimistic
                     SQL_Delay: 0
           SQL_Remaining_Delay: NULL
       Slave_SQL_Running_State: Slave has read all relay log; waiting for more updates
              Slave_DDL_Groups: 2
Slave_Non_Transactional_Groups: 0
    Slave_Transactional_Groups: 0
```

## Next Step

Navigation in the procedure "Deploy Primary/Replica Topology":

This page was step 3 of 7.

Next: Step 4: Test MariaDB Enterprise Server

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
