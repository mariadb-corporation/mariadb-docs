# Step 4: Test MariaDB Enterprise Server

## Overview

This page details step 4 of the 7-step procedure "[Deploy Primary/Replica Topology](./)".

This step tests MariaDB Enterprise Server

Several actions require connection to MariaDB Enterprise Server. A command-line client (mariadb) was included with your ES installation. These instructions describe connection via Unix domain socket. Alternatively, a different client and connection method could be used.

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Test Enterprise Server Service

Use Systemd to test whether the MariaDB Enterprise Server service is running.

This action is performed **on each Enterprise Server node**.

Check if the MariaDB Enterprise Server service is running by executing the following:

```bash
$ systemctl status mariadb
```

If the service is not running on any node, start the service by executing the following on that node:

```bash
$ sudo systemctl start mariadb
```

## Test Local Client Connections

Use [mariadb Client](../../../clients-and-utilities/mariadb-client/) to test the local connection to the Enterprise Server node.

This action is performed **on each Enterprise Server node**:

```bash
$ sudo mariadb
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 38
Server version: 11.4.5-3-MariaDB-Enterprise MariaDB Enterprise Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

The sudo command is used here to connect to the Enterprise Server node using the root@localhost user account, which authenticates using the [unix\_socket](../../../reference/plugins/authentication-plugins/authentication-plugin-unix-socket.md) authentication plugin. Other user accounts can be used by specifying the `--user` and `--password` command-line options.

## Test Replica Status

Use [SHOW REPLICA STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-replica-status.md) to check that replication is running properly on the replica servers.

This action is performed **on each replica server**.

Execute the following:

```sql
SHOW REPLICA STATUS\G

*************************** 1. row ***************************
                Slave_IO_State: Waiting for master to send event
                   Master_Host: 192.0.2.1
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

If `Slave_IO_Running` column is not `Yes` on any replica server, then check:

* The network connectivity between the replica server and the primary server
* The `Last_IO_Error` column for details on any errors

If `Slave_SQL_Running` column is not Yes on any replica server, then check:

* The GTID position in [gtid\_slave\_pos](../../../ha-and-performance/standard-replication/gtid.md#gtid_slave_pos)
* The `Last_SQL_Error` column for details on any errors

If both columns are not `Yes` on any replica server, then check:

* The replication configuration on the replica server.

If you need to make any corrections, the slave threads can be restarted with [START REPLICA](../../../reference/sql-statements/administrative-sql-statements/replication-statements/start-replica.md).

## Test DDL

Use [mariadb Client](../../../clients-and-utilities/mariadb-client/) to test DDL.

1. **On the primary server**, use the [mariadb Client](../../../clients-and-utilities/mariadb-client/) to connect to the node:

```bash
$ sudo mariadb
```

2. Create a test database and table:

```sql
CREATE DATABASE IF NOT EXISTS test;

CREATE TABLE test.contacts (
   id INT PRIMARY KEY AUTO_INCREMENT,
   first_name VARCHAR(50),
   last_name VARCHAR(50),
   email VARCHAR(100)
);
```

3. **On each replica server**, use the [mariadb Client](../../../clients-and-utilities/mariadb-client/) to connect to the node:

```bash
$ sudo mariadb
```

4. Confirm that the database and table exist:

```sql
SHOW CREATE TABLE test.contacts\G;
```

If the database or table do not exist on any node, then check the replication status on the node.

## Test DML

Use [mariadb Client](../../../clients-and-utilities/mariadb-client/) to test DML.

1. **On the primary server**, use the MariaDB Client to connect to the node:

```bash
$ sudo mariadb
```

2. Insert sample data into the table created in the DDL test:

```sql
INSERT INTO test.contacts (first_name, last_name, email)
   VALUES
   ("Kai", "Devi", "kai.devi@example.com"),
   ("Lee", "Wang", "lee.wang@example.com");
```

3. **On each replica server**, use the [mariadb Client](../../../clients-and-utilities/mariadb-client/) to connect to the node:

```bash
$ sudo mariadb
```

4. Execute a [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) query to retrieve the data:

```sql
SELECT * FROM test.contacts;

+----+------------+-----------+----------------------+
| id | first_name | last_name | email                |
+----+------------+-----------+----------------------+
| 1  | Kai        | Devi      | kai.devi@example.com |
| 2  | Lee        | Wang      | lee.wang@example.com |
+----+------------+-----------+----------------------+
```

If the data is not returned on any node, then check the replication status on the node.

## Next Step

Navigation in the procedure "Deploy Primary/Replica Topology":

This page was step 4 of 7.

Next: Step 5: Install MariaDB MaxScale

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
