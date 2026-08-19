# Step 4: Test MariaDB Enterprise Server

## Overview

This page details step 4 of the 4-step procedure "[Deploy HTAP Topology](./)".

This step tests Enterprise ColumnStore.

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Test S3 Connection

MariaDB Enterprise ColumnStore includes a `testS3Connection` command to test the S3 configuration, permissions, and connectivity.

Test the S3 configuration by executing the following:

```bash
$ sudo testS3Connection
```

```
StorageManager[26887]: Using the config file found at /etc/columnstore/storagemanager.cnf
StorageManager[26887]: S3Storage: S3 connectivity & permissions are OK
S3 Storage Manager Configuration OK
```

If the testS3Connection command does not return OK, investigate the S3 configuration.

## Test Enterprise Server Service

Use Systemd to test whether the MariaDB Enterprise Server service is running.

Check if the MariaDB Enterprise Server service is running by executing the following:

```bash
$ systemctl status mariadb
```

If the service is not running, start the service by executing the following:

```bash
$ sudo systemctl start mariadb
```

## Test Local Client Connections

Use MariaDB Client to test the local connection to the Enterprise Server node:

```bash
$ sudo mariadb
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 38
Server version: MariaDB-Enterprise MariaDB Enterprise Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

The sudo command is used here to connect to the Enterprise Server node using the root@localhost user account, which authenticates using the unix\_socket authentication plugin. Other user accounts can be used by specifying the --user and --password command-line options.

## Test ColumnStore Storage Engine Plugin

Query the [information\_schema.PLUGINS](../../../reference/system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md) table to confirm that the ColumnStore storage engine is loaded.

Execute the following query:

```sql
SELECT PLUGIN_NAME, PLUGIN_STATUS
FROM information_schema.PLUGINS
WHERE PLUGIN_LIBRARY LIKE 'ha_columnstore%';

+---------------------+---------------+
| PLUGIN_NAME         | PLUGIN_STATUS |
+---------------------+---------------+
| Columnstore         | ACTIVE        |
| COLUMNSTORE_COLUMNS | ACTIVE        |
| COLUMNSTORE_TABLES  | ACTIVE        |
| COLUMNSTORE_FILES   | ACTIVE        |
| COLUMNSTORE_EXTENTS | ACTIVE        |
+---------------------+---------------+
```

The `PLUGIN_STATUS` column for each ColumnStore-related plugin should contain ACTIVE.

## Test Replication Status

Use the [SHOW REPLICA STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-replica-status.md) statement to check the status of MariaDB Replication:

```sql
SHOW REPLICA STATUS\G

*************************** 1. row ***************************
                Slave_IO_State: Waiting for master to send event
                   Master_Host: localhost
                   Master_User: repl
                   Master_Port: 3306
                 Connect_Retry: 60
               Master_Log_File: mariadb-bin.000002
           Read_Master_Log_Pos: 695
                Relay_Log_File: mysqld-relay-bin.000002
                 Relay_Log_Pos: 996
         Relay_Master_Log_File: mariadb-bin.000002
              Slave_IO_Running: Yes
             Slave_SQL_Running: Yes
               Replicate_Do_DB:
           Replicate_Ignore_DB:
            Replicate_Do_Table:
        Replicate_Ignore_Table:
       Replicate_Wild_Do_Table: columnstore_db.htap%
   Replicate_Wild_Ignore_Table:
                    Last_Errno: 0
                    Last_Error:
                  Skip_Counter: 0
           Exec_Master_Log_Pos: 695
               Relay_Log_Space: 1306
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
                   Gtid_IO_Pos: 0-1-7
       Replicate_Do_Domain_Ids:
   Replicate_Ignore_Domain_Ids:
                 Parallel_Mode: optimistic
                     SQL_Delay: 0
           SQL_Remaining_Delay: NULL
       Slave_SQL_Running_State: Slave has read all relay log; waiting for more updates
              Slave_DDL_Groups: 1
Slave_Non_Transactional_Groups: 0
    Slave_Transactional_Groups: 1
```

## Test ColumnStore Table Creation

1. Create a test database, if it does not exist:

```sql
CREATE DATABASE IF NOT EXISTS test;
```

2. Create a ColumnStore table:

```sql
CREATE TABLE IF NOT EXISTS test.contacts (
   first_name VARCHAR(50),
   last_name VARCHAR(50),
   email VARCHAR(100)
) ENGINE=ColumnStore;
```

3. Add sample data into the table:

```sql
INSERT INTO test.contacts (first_name, last_name, email)
   VALUES
   ("Kai", "Devi", "kai.devi@example.com"),
   ("Lee", "Wang", "lee.wang@example.com");
```

4. Read data from table:

```sql
SELECT * FROM test.contacts;

+------------+-----------+----------------------+
| first_name | last_name | email                |
+------------+-----------+----------------------+
| Kai        | Devi      | kai.devi@example.com |
| Lee        | Wang      | lee.wang@example.com |
+------------+-----------+----------------------+
```

## Test Cross Engine Join

1. Create an InnoDB table:

```sql
CREATE TABLE test.addresses (
   email VARCHAR(100),
   street_address VARCHAR(255),
   city VARCHAR(100),
   state_code VARCHAR(2)
) ENGINE = InnoDB;
```

2. Add data to the table:

```sql
INSERT INTO test.addresses (email, street_address, city, state_code)
   VALUES
   ("kai.devi@example.com", "1660 Amphibious Blvd.", "Redwood City", "CA"),
   ("lee.wang@example.com", "32620 Little Blvd", "Redwood City", "CA");
```

3. Perform a cross-engine join:

```sql
SELECT name AS "Name", addr AS "Address"
FROM (SELECT CONCAT(first_name, " ", last_name) AS name,
   email FROM test.contacts) AS contacts
INNER JOIN (SELECT CONCAT(street_address, ", ", city, ", ", state_code) AS addr,
   email FROM test.addresses) AS addr
WHERE  contacts.email = addr.email;

+----------+-----------------------------------------+
| Name     | Address                                 |
+----------+-----------------------------------------+
| Kai Devi | 1660 Amphibious Blvd., Redwood City, CA |
| Lee Wang | 32620 Little Blvd, Redwood City, CA     |
+----------+-----------------------------------------+
```

## Test HTAP Replication

1. Connect to the server using [MariaDB Client](../../../clients-and-utilities/mariadb-client/) using the root@localhost user account:

```bash
$ sudo mariadb
```

2. Create the databases for the InnoDB and ColumnStore tables using the CREATE DATABASE statement:

```sql
CREATE DATABASE columnstore_db;

CREATE DATABASE innodb_db;
```

3. Create the InnoDB versions of the HTAP tables using the CREATE TABLE statement:

```sql
USE innodb_db;

CREATE TABLE htap_test1 (
   id INT
) ENGINE = InnoDB;

CREATE TABLE htap_test2 (
   id INT
) ENGINE = InnoDB;
```

4. Confirm that the tables were replicated using the SHOW TABLES statement:

```sql
SHOW TABLES FROM columnstore_db;

+--------------------------+
| Tables_in_columnstore_db |
+--------------------------+
| htap_test1               |
| htap_test2               |
+--------------------------+
```

5. The replication initially creates empty InnoDB tables, which need to be transformed into ColumnStore tables and which need to be populated with the initial copy of the data:

```sql
DROP TABLE IF EXISTS columnstore_db.htap_test1;

CREATE TABLE columnstore_db.htap_test1
ENGINE=COLUMNSTORE
SELECT * FROM innodb_db.htap_test1;

DROP TABLE IF EXISTS columnstore_db.htap_test2;

CREATE TABLE columnstore_db.htap_test2
ENGINE=COLUMNSTORE
SELECT * FROM innodb_db.htap_test2;
```

6. Insert data into the InnoDB versions of the HTAP tables using the [INSERT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement:

```sql
USE innodb_db;

INSERT INTO htap_test1
VALUES (100);

INSERT INTO htap_test2
VALUES (200);
```

7. Confirm that the data was replicated using the [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement:

```sql
SELECT * FROM columnstore_db.htap_test1;

+------+
| id   |
+------+
|  100 |
+------+

SELECT * FROM columnstore_db.htap_test2;

+------+
| id   |
+------+
|  200 |
+------+
```

8. Create an InnoDB table that will not be replicated:

```sql
USE innodb_db;
CREATE TABLE transactional_test1 (
   id INT
) ENGINE = InnoDB;
```

9. Confirm that the table was not replicated:

```sql
SHOW TABLES FROM columnstore_db LIKE 'transactional_%';

Empty set (0.02 sec)
```

10. Create a ColumnStore table that will not be replicated:

```sql
USE columnstore_db;
CREATE TABLE analytical_test1 (
   id INT
) ENGINE = ColumnStore;
```

11. Confirm that the table was not replicated:

```sql
SHOW TABLES FROM innodb_db LIKE 'analytical_%';

Empty set (0.02 sec)
```

## Next Step

Navigation in the procedure "Deploy HTAP Topology".\
This page was step 4 of 4.

This procedure is complete.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
