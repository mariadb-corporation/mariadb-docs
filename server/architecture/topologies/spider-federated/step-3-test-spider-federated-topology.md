# Step 3: Test Spider Federated Topology

## Overview

This page details step 3 of the 3-step procedure "[Deploy Spider Federated Topology](./)".

This step tests MariaDB Enterprise Spider.

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Test Enterprise Server Service

Use Systemd to test whether the MariaDB Enterprise Server service is running.

This action is performed **on the Spider Node and Data Node**.

Check if the MariaDB Enterprise Server service is running by executing the following:

```bash
$ systemctl status mariadb
```

If the service is not running on any node, start the service by executing the following on that node:

```bash
$ sudo systemctl start mariadb
```

## Test Local Client Connections

Use MariaDB Client to test the local connection to the Enterprise Server node.

This action is performed on the Spider Node and Data Node:

```bash
$ sudo mariadb
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 38
Server version: 11.4.5-3-MariaDB-Enterprise MariaDB Enterprise Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

The sudo command is used here to connect to the Enterprise Server node using the `root@localhost` user account, which authenticates using the `unix_socket` authentication plugin. Other user accounts can be used by specifying the `--user` and `--password` command-line options.

## Test Data Node Client Connection

Use [mariadb Client](../../../clients-and-utilities/mariadb-client/) to test a client connection to the Data Node from the Spider Node using the Spider user.

This action is performed **on the Spider Node**:

```bash
$ mariadb \
   --host 192.0.2.2 \
   --user spider_user \
   --password
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 38
Server version: 11.4.5-3-MariaDB-Enterprise MariaDB Enterprise Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

The host and port of the Data Node can be provided using the `--host` and `--port` command-line options. The credentials for the Spider user can be provided using the `--user` and `--password` command-line options.

If the Spider user is unable to connect to the Data Node from the Spider Node, check the password for the Spider user account on the Data Node.

For additional information, see "[Create Spider User](step-2-configure-spider-node-and-data-node.md#create-spider-user)".

## Test Spider Storage Engine Plugin

Query the information\_schema.PLUGINS table to confirm that the Enterprise Spider storage engine is loaded.

This action is performed **on the Spider Node**.

Execute the following query:

```sql
SELECT PLUGIN_NAME, PLUGIN_STATUS
FROM information_schema.PLUGINS
WHERE PLUGIN_LIBRARY LIKE 'ha_spider%';

+--------------------------+---------------+
| PLUGIN_NAME              | PLUGIN_STATUS |
+--------------------------+---------------+
| SPIDER                   | ACTIVE        |
| SPIDER_ALLOC_MEM         | ACTIVE        |
| SPIDER_WRAPPER_PROTOCOLS | ACTIVE        |
+--------------------------+---------------+
```

The `PLUGIN_STATUS` column for each Spider-related plugin should contain `ACTIVE`.

For additional information, see "[Load the Spider Plugin](step-1-install-enterprise-spider.md#load-the-spider-plugin)".

## Test Write Operations

Write to the Spider Table using an [INSERT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement to test write operations.

This action is performed **on the Spider Node**.

Execute the following query:

```sql
INSERT INTO spider_hq_sales.invoices
   (branch_id, invoice_id, customer_id, invoice_date, invoice_total, payment_method)
VALUES (1, 4, 1, '2021-03-10 12:45:10', 3045.73, 'CREDIT_CARD');
```

## Test Read Operations

Read from the Spider Table using a [SELECT](../../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement to test read operations.

This action is performed **on the Spider Node**.

Execute the following query:

```sql
SELECT * FROM spider_hq_sales.invoices;

+-----------+------------+-------------+----------------------------+---------------+----------------+
| branch_id | invoice_id | customer_id | invoice_date               | invoice_total | payment_method |
+-----------+------------+-------------+----------------------------+---------------+----------------+
|         1 |          1 |           1 | 2020-05-10 12:35:10.000000 |       1087.23 | CREDIT_CARD    |
|         1 |          2 |           2 | 2020-05-10 14:17:32.000000 |       1508.57 | WIRE_TRANSFER  |
|         1 |          3 |           3 | 2020-05-10 14:25:16.000000 |        227.15 | CASH           |
|         1 |          4 |           1 | 2021-03-10 12:45:10.000000 |       3045.73 | CREDIT_CARD    |
+-----------+------------+-------------+----------------------------+---------------+----------------+
```

## Next Step

Navigation in the procedure "Deploy Spider Federated Topology".

This page was step 3 of 3.

This procedure is complete.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
