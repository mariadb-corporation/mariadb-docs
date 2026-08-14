---
description: Adding a Node to MariaDB ColumnStore
---

# Adding a Node

To add a new node to ColumnStore, perform the following procedure.

## Deploying ColumnStore

Before you can add a node to ColumnStore, confirm that the ColumnStore software has been deployed on the node in the desired topology.

For additional information, see "[Topologies](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies)".

## Backing Up MariaDB Data Directory on the Primary Server

Before the new node can be added, its MariaDB data directory must be consistent with the Primary Server. To ensure that it is consistent, take a backup of the Primary Server:

The instructions below show how to perform a backup using [MariaDB Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup).

1.  On the Primary Server, take a full backup:

    ```bash
    sudo mariadb-backup --backup \
          --user=mariabackup_user \
          --password=mariabackup_passwd \
          --target-dir=/data/backup/replica_backup
    ```

    Confirm successful completion of the backup operation.
2.  On the Primary Server, prepare the backup:

    ```bash
    sudo mariadb-backup --prepare \
          --target-dir=/data/backup/replica_backup
    ```

    Confirm successful completion of the prepare operation.

## Restoring the Backup on the New Node

To make the new node consistent with the Primary Server, restore the new backup on the new node:

1.  On the Primary Server, copy the backup to the new node:

    ```bash
    sudo rsync -av /data/backup/replica_backup 192.0.2.3:/data/backup/
    ```
2.  On the new node, restore the backup using [MariaDB Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup).

    ```bash
    sudo mariadb-backup --copy-back \
       --target-dir=/data/backup/replica_backup
    ```
3.  On the new node, fix the file permissions of the restored backup:

    ```bash
    sudo chown -R mysql:mysql /var/lib/mysql
    ```

## Starting the Enterprise ColumnStore Services

The Enterprise Server. Enterprise ColumnStore, and CMAPI services can be started using the `systemctl` command. In case the services were started during the installation process, use the restart command.

Perform the following procedure on the new node:

1.  Start and enable the MariaDB Enterprise Server service, so that it starts automatically upon reboot:

    ```bash
    sudo systemctl restart mariadb
    sudo systemctl enable mariadb
    ```
2.  Start and disable the MariaDB Enterprise ColumnStore service, so that it does not start automatically upon reboot:

    ```bash
    sudo systemctl restart mariadb-columnstore
    sudo systemctl disable mariadb-columnstore
    ```

    Note

    The Enterprise ColumnStore service should not be enabled in a multi-node deployment. The Enterprise ColumnStore service will be started as-needed by the CMAPI service, so it does not require starting automatically upon reboot.
3.  Start and enable the CMAPI service, so that it starts automatically upon reboot:

    ```bash
    sudo systemctl restart mariadb-columnstore-cmapi
    sudo systemctl enable mariadb-columnstore-cmapi
    ```

## Configuring MariaDB Replication

MariaDB Enterprise ColumnStore requires MariaDB Replication, which must be configured.

1.  Get the GTID position that corresponds to the restored backup.

    If the backup was taken with [MariaDB Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup), this position will be located in `xtrabackup_binlog_info`:

    ```bash
    cat xtrabackup_binlog_info
    mariadb-bin.000096 568 0-1-2001,1-2-5139
    ```

    The GTID position from the above output is `0-1-2001,1-2-5139`.
2.  Connect to the Replica Server using [MariaDB Client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client) using the `root@localhost` user account:

    ```bash
    sudo mariadb
    ```
3.  Set the [gtid\_slave\_pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_slave_pos) system variable to the GTID position:

    ```sql
    SET GLOBAL gtid_slave_pos='0-1-2001,1-2-5139';
    ```
4.  Execute the [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to) statement to configure the new node to connect to the Primary Server at this position:

    ```sql
    CHANGE MASTER TO
       MASTER_USER = "repl",
       MASTER_HOST = "192.0.2.1",
       MASTER_PASSWORD = "repl_passwd",
       MASTER_USE_GTID=slave_pos;
    ```

    The above statement configures the Replica Server to connect to a Primary Server located at `192.0.2.1` using the `repl` user account.
5.  Start replication using the START SLAVE command:

    ```sql
    START SLAVE;
    ```

    The above statement configures the new node to connect to the Primary Server to retrieve new binary log events and replicate them into the local database.

## Adding the Node to Enterprise ColumnStore

The new node must be added to Enterprise ColumnStore using [CMAPI](../../reference/cmapi/):

* Add the node using the [add-node](../../reference/cmapi/node-put.md) endpoint path
* Use a [supported REST client](../../reference/cmapi/#clients), such as `curl`
* Format the JSON output using `jq` for enhanced readability
* Authenticate using the configured [API key](../../reference/cmapi/#authentication)
* Include the [required headers](../../reference/cmapi/#required-headers)

For example, if the primary node's host name is `mcs1` and the new node's IP address is `192.0.2.3`:

*   In ES 10.5.10-7 and later:

    ```bash
    curl -k -s -X PUT https://mcs1:8640/cmapi/0.4.0/cluster/node \
       --header 'Content-Type:application/json' \
       --header 'x-api-key:93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd' \
       --data '{"timeout":20, "node": "192.0.2.3"}' \
       | jq .
    ```
*   In ES 10.5.9-6 and earlier:

    ```bash
    curl -k -s -X PUT https://mcs1:8640/cmapi/0.4.0/cluster/add-node \
       --header 'Content-Type:application/json' \
       --header 'x-api-key:93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd' \
       --data '{"timeout":20, "node": "192.0.2.3"}' \
       | jq .
    ```

Example output:

```json
{
  "timestamp": "2020-10-28 00:39:14.672142",
  "node_id": "192.0.2.3"
}
```

## Checking Enterprise ColumnStore Status

To confirm that the node was properly added, the status of Enterprise ColumnStore should be checked using [CMAPI](../../reference/cmapi/):

* Check the status using the [status](../../reference/cmapi/status.md) endpoint path

For example, if the primary node's host name is `mcs1`:

```bash
curl -k -s https://mcs1:8640/cmapi/0.4.0/cluster/status \
   --header 'Content-Type:application/json' \
   --header 'x-api-key:93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd' \
   | jq .
```

Example output:

```json
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

## Adding a Server to MaxScale

A server object for the new node must also be added to MaxScale using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* Use [MaxCtrl](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/administrative-tools-for-mariadb-maxscale-maxctrl) or another supported REST client
* Add the server object using the `create server` command
* As the first argument, provide a name for the server
* As the second argument, provide the IP address for the node

For example:

```bash
maxctrl create server \
   mcs3 \
   192.0.2.3
```

## Verifying the Server in MaxScale

To confirm that the server object was properly added, the server objects should be checked using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* Show the server objects using the `show servers` command

For example:

```bash
maxctrl show servers
```

## Linking to Monitor in MaxScale

The server object for the new node must be linked to the monitor using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* Link a server object to the monitor using the `link monitor` command
* As the first argument, provide the name of the monitor
* As the second argument, provide the name of the server

```bash
maxctrl link monitor \
   mcs_monitor \
   mcs3
```

## Checking the Monitor in MaxScale

To confirm that the server object was properly linked to the monitor, the monitor should be checked using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* Show the monitors using the `show monitors` command

For example:

```bash
maxctrl show monitors
```

## Linking to Service in MaxScale

The server object for the new node must be linked to the service using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* Link the server object to the service using the `link service` command
* As the first argument, provide the name of the service
* As the second argument, provide the name of the server

```bash
maxctrl link service \
   mcs_service \
   mcs3
```

## Checking the Service in MaxScale

To confirm that the server object was properly linked to the service, the service should be checked using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* Show the services using the `show services` command

For example:

```bash
maxctrl show services
```

## Checking the Replication Status with MaxScale

MaxScale is capable of checking the status of [MariaDB Replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication) using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* List the servers using the `list servers` command

For example:

```bash
maxctrl list servers
```

If the new node is properly replicating, then the `State` column will show `Slave, Running`.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
