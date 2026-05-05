---
description: >-
  CMAPI is the REST API for administering MariaDB Enterprise ColumnStore in
  multi-node topologies, accessed with curl or any standard REST client and
  authenticated via x-api-key.
---

# CMAPI

**CMAPI** is a REST API for administering MariaDB Enterprise ColumnStore in multi-node topologies.

Reference material is available for MariaDB Enterprise ColumnStore.

MariaDB Enterprise ColumnStore is included with MariaDB Enterprise Server.

## Clients

CMAPI is a REST API, so it should be compatible with most standard REST clients.

CMAPI examples throughout the documentation use `curl` as the REST client. The examples also pipe the JSON output to `jq` for enhanced readability.

## Endpoint

The endpoint for CMAPI contains the hostname and port for the primary node running Enterprise ColumnStore, `/cmapi/`, the CMAPI API version (`0.4.0`), and a action-specific endpoint path.

Example: `https://mcs1:8640/cmapi/0.4.0/cluster/node`

## Endpoint Paths

| Endpoint Path           | Method   | Action                                                |
| ----------------------- | -------- | ----------------------------------------------------- |
| [mode-set](mode-set.md) | `PUT`    | Sets all ColumnStore nodes to read-only or read-write |
| [node](node-delete.md)  | `DELETE` | Removes a ColumnStore node                            |
| [node](node-put.md)     | `PUT`    | Adds a ColumnStore node                               |
| [shutdown](shutdown.md) | `PUT`    | Shuts down ColumnStore on all nodes                   |
| [start](start.md)       | `PUT`    | Starts ColumnStore on all nodes                       |
| [status](status.md)     | `GET`    | Checks the status of ColumnStore                      |

Method and required data vary by CMAPI endpoint path.

## Required Headers

| Header         | Description                                                                           |
| -------------- | ------------------------------------------------------------------------------------- |
| `Content-Type` | Set to `application/json`                                                             |
| `x-api-key`    | Set to the API key configured for CMAPI. Calls using the incorrect keys are rejected. |

## Authentication

Authentication is performed via an API key, which performs the role of a shared secret. The API key is passed to the API using the `x-api-key` header.

The API key is stored in `/etc/columnstore/cmapi_server.conf`.

### Generate an API Key

The API key is a shared secret that can be used to add nodes to multi-node Enterprise ColumnStore. The API key can be any string, but it is recommended to use a long, random string. The API key should be stored securely and kept confidential.

For example, to create a random 256-bit API key using `openssl rand`:

```bash
openssl rand -hex 32
93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd
```

### Set the API Key

To set the API key for the first time, provide the desired API key when you add the first node using the [node](http://localhost:8000/docs/columnstore/ref/cmapi/add-node/) PUT command. Since Enterprise ColumnStore does not yet have an API key, CMAPI will write the first API key it receives to `/etc/columnstore/cmapi_server.conf`.

For example, if the primary server's host name is `mcs1` and its IP address is `192.0.2.1`, the following command will add the primary server to Enterprise ColumnStore and write the provided API key to the node's CMAPI configuration file:

```bash
curl -k -s -X PUT https://mcs1:8640/cmapi/0.4.0/cluster/node \
   --header 'Content-Type:application/json' \
   --header 'x-api-key:93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd' \
   --data '{"timeout":120, "node": "192.0.2.1"}' \
   | jq .
```

### Change the API Key

To change the API key in multi-node Enterprise ColumnStore, change it in the CMAPI configuration file on each node located at `/etc/columnstore/cmapi_server.conf`. The CMAPI server must be restarted on each node for the changes to be applied.

Restart the CMAPI server by running the following command on each node:

```bash
sudo systemctl restart mariadb-columnstore-cmapi
```

## Bash Aliases

{% hint style="info" %}
Bash aliases are available starting with Enterprise ColumnStore 5.5.2.
{% endhint %}

These aliases are available if your `bash` shell is configured to source the `columnstoreAlias` shell script.

These aliases execute `curl` and `jq`, so both programs must be installed on the system.

These aliases automatically retrieve the IP address for the primary node using the [mcsGetConfig](http://localhost:8000/docs/columnstore/ref/col/cli/mcsGetConfig/) command. The aliases automatically retrieve the API key by reading `/etc/columnstore/cmapi_server.conf`.

Available aliases:

| Alias        | Endpoint                | Action                                   |
| ------------ | ----------------------- | ---------------------------------------- |
| mcsReadOnly  | [mode-set](mode-set.md) | Sets all ColumnStore nodes to read-only  |
| mcsReadWrite | [mode-set](mode-set.md) | Sets all ColumnStore nodes to read/write |
| mcsShutdown  | [shutdown](shutdown.md) | Shuts down ColumnStore on all nodes      |
| mcsStart     | [start](start.md)       | Starts ColumnStore on all nodes          |
| mcsStatus    | [status](status.md)     | Checks the status of ColumnStore         |

## CMAPI Service Management

The `systemctl` command is used to start and stop the CMAPI service.

| Operation            | Command                                       |
| -------------------- | --------------------------------------------- |
| Status               | `systemctl status mariadb-columnstore-cmapi`  |
| Start                | `systemctl start mariadb-columnstore-cmapi`   |
| Stop                 | `systemctl stop mariadb-columnstore-cmapi`    |
| Restart              | `systemctl restart mariadb-columnstore-cmapi` |
| Enable startup       | `systemctl enable mariadb-columnstore-cmapi`  |
| Disable startup      | `systemctl disable mariadb-columnstore-cmapi` |
| View systemd journal | `journalctl -u mariadb-columnstore-cmapi`     |

## Configuration

The CMAPI configuration file is located at `/etc/columnstore/cmapi_server.conf`.

To change the configuration:

* Modify the configuration file on each node
*   Restart the CMAPI server on each node:

    > ```bash
    > sudo systemctl restart mariadb-columnstore-cmapi
    > ```

### Configure Failover

Starting with CMAPI 6.4.1, the `auto_failover` option can be set to `True` or `False` in the `[application]` section:

```ini
[application]
auto_failover = False
```

* The default value of the `auto_failover` option is `True`.
* The `auto_failover` option should be set to `False` when [non-shared local storage](../../architecture/columnstore-storage-architecture.md#storage-options) is used.

## Logging

Starting with Enterprise ColumnStore 5.5.2, the [CMAPI logs](http://localhost:8000/docs/columnstore/ref/col/logging/cmapi/) can be found at `/var/log/mariadb/columnstore/cmapi_server.log`.

In previous versions, CMAPI's log messages can be viewed in the `systemd` journal:

```bash
sudo journalctl -u mariadb-columnstore-cmapi
```

## CMAPI Responses

CMAPI responds to client requests with standard HTTP response messages.

### Status Line

The first part of the standard HTTP response message is the status line. To determine if your request was successful, check the status code and the reason phrase from the status line.

| **Status Code**  | **Reason Phrase** | **Outcome**                                              |
| ---------------- | ----------------- | -------------------------------------------------------- |
| `200`            | `OK`              | Successful                                               |
| `200 < x < 300`  | Varies            | Possibly successful                                      |
| `300 <= x < 400` | Varies            | Request redirected                                       |
| `400 <= x < 500` | Varies            | Client-side error Check endpoint, API key, and JSON data |
| `500 <= x < 600` | Varies            | Server-side error Contact support                        |

{% hint style="info" %}
Consult the [HTTP standard](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) to see the full list of status codes and their descriptions.
{% endhint %}

### Headers

The second part of the standard HTTP response message is the HTTP headers. To determine what kind of message body is in the response message, check the `Content-Type` header field.

| **Outcome** | `Content-Type`                        |
| ----------- | ------------------------------------- |
| Success     | `application/json`                    |
| Failure     | Undefined Depends on specific failure |

### Body

The final part of the standard HTTP response message is the body.

| **Outcome** | **Body**                              |
| ----------- | ------------------------------------- |
| Success     | JSON Data                             |
| Failure     | Undefined Depends on specific failure |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
