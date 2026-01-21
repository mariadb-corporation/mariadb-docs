---
description: 'Step 5: Test MariaDB Enterprise Server'
---

# Step 5: Test MariaDB Enterprise Serverd

## Overview

This page details step 5 of the 9-step procedure "Deploy ColumnStore Object Storage Topology".

This step tests MariaDB Enterprise Server and MariaDB Enterprise ColumnStore.

{% include "../../../../../.gitbook/includes/the-instructions-were-teste....md" %}

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Test S3 Connection

MariaDB Enterprise ColumnStore 23.10 includes a `testS3Connection` command to test the S3 configuration, permissions, and connectivity.

This action is performed **on each Enterprise ColumnStore node**.

Test the S3 configuration by executing the following:

```bash
$ sudo testS3Connection
```

```
StorageManager[26887]: Using the config file found at /etc/columnstore/storagemanager.cnf
StorageManager[26887]: S3Storage: S3 connectivity & permissions are OK
S3 Storage Manager Configuration OK
```

If the `testS3Connection` command does not return `OK`, investigate the S3 configuration.

## Test Enterprise Server Service

Use Systemd to test whether the MariaDB Enterprise Server service is running.

This action is performed **on each Enterprise ColumnStore node**.

Check if the MariaDB Enterprise Server service is running by executing the following:

```bash
$ systemctl status mariadb
```

If the service is not running on any node, start the service by executing the following on that node:

```bash
$ sudo systemctl start mariadb
```

## Test Local Client Connections

Use [MariaDB Client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client) to test the local connection to the Enterprise Server node.

This action is performed on each Enterprise ColumnStore node:

```bash
$ sudo mariadb
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 38
Server version: 11.4.5-3-MariaDB-Enterprise MariaDB Enterprise Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

The `sudo` command is used here to connect to the Enterprise Server node using the root@localhost user account, which authenticates using the unix\_socket authentication plugin. Other user accounts can be used by specifying the --user and --password command-line options.

## Test ColumnStore Storage Engine Plugin

Query the [information\_schema.PLUGINS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/plugins-table-information-schema) table to confirm that the ColumnStore storage engine is loaded.

This action is performed on each Enterprise ColumnStore node.

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

### Test CMAPI Service

Use Systemd to test whether the CMAPI service is running.

This action is performed on each Enterprise ColumnStore node.

Check if the CMAPI service is running by executing the following:

```bash
$ systemctl status mariadb-columnstore-cmapi
```

If the service is not running on any node, start the service by executing the following on that node:

```bash
$ sudo systemctl start mariadb-columnstore-cmapi
```

## Test ColumnStore Status

Use CMAPI to request the ColumnStore status. The API key needs to be provided as part of the `X-API-key` HTML header.

This action is performed with the CMAPI service on the primary server.

Check the ColumnStore status using curl by executing the following:

```bash
$ curl -k -s https://mcs1:8640/cmapi/0.4.0/cluster/status \
   --header 'Content-Type:application/json' \
   --header 'x-api-key:93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd' \
   | jq .

{
  "timestamp": "2020-12-15 00:40:34.353574",
  "192.0.2.1": {
    "timestamp": "2020-12-15 00:40:34.362374",
    "uptime": 11467,
    "dbrm_mode": "master",
    "cluster_mode": "readwrite",
    "dbroots": [
      "1"
    ],
    "module_id": 1,
    "services": [
      {
        "name": "workernode",
        "pid": 19202
      },
      {
        "name": "controllernode",
        "pid": 19232
      },
      {
        "name": "PrimProc",
        "pid": 19254
      },
      {
        "name": "ExeMgr",
        "pid": 19292
      },
      {
        "name": "WriteEngine",
        "pid": 19316
      },
      {
        "name": "DMLProc",
        "pid": 19332
      },
      {
        "name": "DDLProc",
        "pid": 19366
      }
    ]
  },
  "192.0.2.2": {
    "timestamp": "2020-12-15 00:40:34.428554",
    "uptime": 11437,
    "dbrm_mode": "slave",
    "cluster_mode": "readonly",
    "dbroots": [
      "2"
    ],
    "module_id": 2,
    "services": [
      {
        "name": "workernode",
        "pid": 17789
      },
      {
        "name": "PrimProc",
        "pid": 17813
      },
      {
        "name": "ExeMgr",
        "pid": 17854
      },
      {
        "name": "WriteEngine",
        "pid": 17877
      }
    ]
  },
  "192.0.2.3": {
    "timestamp": "2020-12-15 00:40:34.428554",
    "uptime": 11437,
    "dbrm_mode": "slave",
    "cluster_mode": "readonly",
    "dbroots": [
      "2"
    ],
    "module_id": 2,
    "services": [
      {
        "name": "workernode",
        "pid": 17789
      },
      {
        "name": "PrimProc",
        "pid": 17813
      },
      {
        "name": "ExeMgr",
        "pid": 17854
      },
      {
        "name": "WriteEngine",
        "pid": 17877
      }
    ]
  },
  "num_nodes": 3
}
```

## Test DDL

Use MariaDB Client to test DDL.

1. On the primary server, use the MariaDB Client to connect to the node:

```bash
$ sudo mariadb
```

2. Create a test database and ColumnStore table:

```sql
CREATE DATABASE IF NOT EXISTS test;

CREATE TABLE IF NOT EXISTS test.contacts (
   first_name VARCHAR(50),
   last_name VARCHAR(50),
   email VARCHAR(100)
) ENGINE = ColumnStore;
```

3. On each replica server, use the MariaDB Client to connect to the node:

```bash
$ sudo mariadb
```

4. Confirm that the database and table exist:

```sql
SHOW CREATE TABLE test.contacts\G;
```

If the database or table do not exist on any node, then check the replication configuration.

## Test DML

Use MariaDB Client to test DML.

1. On the primary server, use the MariaDB Client to connect to the node:

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

3. On each replica server, use the MariaDB Client to connect to the node:

```bash
$ sudo mariadb
```

4. Execute a [SELECT](broken-reference/) query to retrieve the data:

```sql
SELECT * FROM test.contacts;

+------------+-----------+----------------------+
| first_name | last_name | email                |
+------------+-----------+----------------------+
| Kai        | Devi      | kai.devi@example.com |
| Lee        | Wang      | lee.wang@example.com |
+------------+-----------+----------------------+
```

If the data is not returned on any node, check the ColumnStore status and the storage configuration.

## Next Step

Navigation in the procedure 'Deploy ColumnStore Object Storage Topology".

This page was **step 5 of 9**.

[Next: Step 6: Install MariaDB MaxScale.](step-6-install-mariadb-maxscale.md)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
