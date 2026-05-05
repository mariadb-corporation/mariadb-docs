---
description: >-
  Remove a node from a MariaDB Enterprise ColumnStore cluster by unlinking the
  server object from the MaxScale service using maxctrl or another REST
  client.
---

# Removing a Node

To remove a node from Enterprise ColumnStore, perform the following procedure.

## Unlinking from Service in MaxScale

The server object for the node must be unlinked from the service using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* Unlink the server object from the service using the `unlink service` command.
* As the first argument, provide the name of the service.
* As the second argument, provide the name of the server.

```bash
maxctrl unlink service \
   mcs_service \
   mcs3
```

## Checking the Service in MaxScale

To confirm that the server object was properly unlinked from the service, the service should be checked using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* Show the services using the `show services` command, like this:

```bash
maxctrl show services
```

## Unlinking from Monitor in MaxScale

The server object for the node must be unlinked from the monitor using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* Unlink a server object from the monitor using the `unlink monitor` command.
* As the first argument, provide the name of the monitor.
* As the second argument, provide the name of the server.

```bash
maxctrl unlink monitor \
   mcs_monitor \
   mcs3
```

## Checking the Monitor in MaxScale

To confirm that the server object was properly unlinked from the monitor, the monitor should be checked using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* Show the monitors using the `show monitors` command, like this:

```bash
maxctrl show monitors
```

## Removing the Server from MaxScale

The server object for the node must also be removed from MaxScale using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* Use [MaxCtrl](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/administrative-tools-for-mariadb-maxscale-maxctrl) or another supported REST client.
* Remove the server object using the `destroy server` command.
* As the first argument, provide the name for the server.

For example:

```bash
maxctrl destroy server \
   mcs3
```

## Checking the Server in MaxScale

To confirm that the server object was properly removed, the server objects should be checked using [MaxScale's REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api):

* Show the server objects using the `show servers` command, like this:

```bash
maxctrl show servers
```

## Stopping the Enterprise ColumnStore Services

The Enterprise Server. Enterprise ColumnStore, and CMAPI services can be stopped using the `systemctl` command.

Perform the following procedure on the node:

1.  Stop the MariaDB Enterprise Server service:

    ```bash
    sudo systemctl stop mariadb
    ```
2.  Stop the MariaDB Enterprise ColumnStore service:

    ```bash
    sudo systemctl stop mariadb-columnstore
    ```
3.  Stop the CMAPI service:

    ```bash
    sudo systemctl stop mariadb-columnstore-cmapi
    ```

## Removing the Node from Enterprise ColumnStore

The node must be removed from Enterprise ColumnStore using [CMAPI](../../reference/cmapi/):

* Remove the node using the [remove-node](../../reference/cmapi/node-delete.md) endpoint path.
* Use a [supported REST client](../../reference/cmapi/#clients), such as `curl` .
* Format the JSON output using `jq` for enhanced readability.
* Authenticate using the configured [API key](../../reference/cmapi/#authentication).
* Include the [required headers](../../reference/cmapi/#required-headers).

For example, if the primary node's host name is `mcs1` and the IP address for the node to remove is `192.0.2.3`:

*   In ES 10.5.10-7 and later:

    ```bash
    curl -k -s -X DELETE https://mcs1:8640/cmapi/0.4.0/cluster/node \
       --header 'Content-Type:application/json' \
       --header 'x-api-key:93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd' \
       --data '{"timeout":20, "node": "192.0.2.3"}' \
       | jq .
    ```
*   In ES 10.5.9-6 and earlier:

    ```bash
    curl -k -s -X PUT https://mcs1:8640/cmapi/0.4.0/cluster/remove-node \
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

## Checking the Enterprise ColumnStore Status

To confirm that the node was properly removed, the status of Enterprise ColumnStore should be checked using [CMAPI](../../reference/cmapi/):

* Check the status using the [status](../../reference/cmapi/status.md) endpoint path.

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
  "num_nodes": 2
}
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
