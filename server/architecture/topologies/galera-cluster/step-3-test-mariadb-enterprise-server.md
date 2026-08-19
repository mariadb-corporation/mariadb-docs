# Step 3: Test MariaDB Enterprise Server

## Overview

This page details step 3 of the 6-step procedure "[Deploy Galera Cluster Topology](./)".

This step tests MariaDB Enterprise Server.

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Test Enterprise Server Service

Use Systemd to test whether the MariaDB Enterprise Server service is running.

This action is performed on each Enterprise Cluster node.

Check if the MariaDB Enterprise Server service is running by executing the following:

```bash
$ systemctl status mariadb
```

If the service is not running on any node, start the service by executing the following on that node:

```bash
$ sudo systemctl start mariadb
```

## Test Local Client Connections

Use [MariaDB Client](../../../clients-and-utilities/mariadb-client/) to test the local connection to the Enterprise Server node.

This action is performed on each Enterprise Cluster node:

```bash
$ sudo mariadb

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 38
Server version: 11.4.5-3-MariaDB-Enterprise MariaDB Enterprise Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

The sudo command is used here to connect to the Enterprise Server node using the `root@localhost` user account, which authenticates using the `unix_socket` authentication plugin. Other user accounts can be used by specifying the --user and --password command-line options.

## Test Cluster Status

MariaDB Enterprise Cluster is operational when the cluster has a Primary Component. Query the [wsrep\_cluster\_status](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_cluster_status) status variable with SHOW GLOBAL STATUS to confirm that each node belongs to the Primary Component.

This action is performed on each Enterprise Cluster node.

Check the cluster status by executing the following:

```sql
SHOW GLOBAL STATUS LIKE 'wsrep_cluster_status';

+----------------------+---------+
| Variable_name        | Value   |
+----------------------+---------+
| wsrep_cluster_status | Primary |
+----------------------+---------+
```

If the Value column does not contain Primary on any node, then the node is not part of the Primary Component. Investigate network connectivity between the node and the nodes in the Primary Component.

## Test Cluster Size

MariaDB Enterprise Cluster maintains a count of the cluster size. Query the [wsrep\_cluster\_size](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_cluster_size) status variable with SHOW GLOBAL STATUS to confirm the number of nodes currently in the cluster.

This action is performed on each Enterprise Cluster node.

Check the cluster size by executing the following:

```sql
SHOW GLOBAL STATUS LIKE 'wsrep_cluster_size';

+--------------------+---------+
| Variable_name      | Value   |
+--------------------+---------+
| wsrep_cluster_size |       3 |
+--------------------+---------+
```

If the Value column does not contain the expected number of nodes, then some nodes might not be in the cluster. Check the value of the [wsrep\_cluster\_address](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_cluster_address) on each node to confirm that all nodes are in the same cluster.

## Test DDL

Use MariaDB Client to test DDL.

1. On a single Enterprise Cluster node, use the MariaDB Client to connect to the node:

```bash
$ sudo mariadb
```

Create a test database and InnoDB table:

```sql
CREATE DATABASE IF NOT EXISTS test;

CREATE TABLE test.contacts (
   id INT PRIMARY KEY AUTO_INCREMENT,
   first_name VARCHAR(50),
   last_name VARCHAR(50),
   email VARCHAR(100)
);
```

3. On each other Enterprise Cluster node, use the MariaDB Client to connect to the node:

```bash
$ sudo mariadb
```

4. Confirm that the database and table exist:

```sql
SHOW CREATE TABLE test.contacts\G;
```

If the database or table do not exist on any node, then check that:

The nodes are in the Primary Component of the same cluster.

The wsrep\_osu\_method system variable is not set to RSU.

## Test DML

Use MariaDB Client to test DML.

1. On a single Enterprise Cluster node, use the MariaDB Client to connect to the node:

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

3. On each other Enterprise Cluster node, use the MariaDB Client to connect to the node:

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

If the data is not returned on any node, then check that:

* The nodes are in the Primary Component of the same cluster.
* The table uses the InnoDB storage engine.
* The wsrep\_on system variable is set to ON.

## Next Step

Navigation in the procedure "Deploy Galera Cluster Topology":

This page was step 3 of 6.

Next: Step 4: Install MariaDB MaxScale

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
