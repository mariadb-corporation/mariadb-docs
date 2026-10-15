---
description: >-
  Reference for the rest tools of the mariadb-shell MCP server, which set up, start, stop, list, and delete MariaDB REST Daemon deployments.
---

# rest Tools

The `rest.*` tools set up and manage the MariaDB REST Daemon, `mariadb-restd`, which serves the REST services that are defined in a server's REST metadata. For how the agent defines REST services and endpoints, see [REST Endpoints with MariaDB REST Service](../features/rest-endpoints-with-mariadb-rest-service.md).

{% hint style="info" %}
The `rest.*` tools are available in MariaDB Shell releases later than 26.10.1. An MCP server from MariaDB Shell 26.10.1 or earlier doesn't offer them.
{% endhint %}

## Overview

| Tool | Description |
| --- | --- |
| `rest.configure_restd` | Sets up a REST Daemon for a server, and starts it. |
| `rest.start_restd` | Starts the daemon of a deployment. |
| `rest.stop_restd` | Stops the daemon of a deployment. |
| `rest.delete_restd_config` | Stops the daemon, drops the server account that the setup created for it, and deletes the deployment. |
| `rest.get_restd_status` | Lists the deployments, and whether each daemon is running. |

`rest.configure_restd` is offered only together with the `db.*` group, because it works on a connection from `db.connect`. A server in multi-tenant mode never offers the `rest.*` tools.

## Deployments

A deployment is a folder that holds a daemon's configuration, keyring, TLS certificate, and logs. Its location depends on the server that the daemon serves.

| Server | Deployment folder | Daemon port |
| --- | --- | --- |
| A sandbox instance | `<sandbox_dir>/<port>/mariadb-restd`, inside the instance's folder. | The first free port from 8443 up. |
| Any other server | `~/.mariadb-restd/<host>_<port>`. On Windows, `%APPDATA%\MariaDB\mariadb-restd\<host>_<port>`. | The first free port from 8443 up. |

The daemon serves HTTPS with a self-signed certificate, and logs to `log/mariadb-restd.log` in its deployment folder. It runs detached from the MCP server and keeps running after the MCP server ends.

A sandbox instance's daemon follows the instance: `sandbox.start` starts it, and `sandbox.stop`, `sandbox.kill`, and `sandbox.delete` stop it. See [sandbox Tools](sandbox-tools.md).

## rest.configure_restd

Sets up a REST Daemon for a server, and starts it.

| Argument | Description |
| --- | --- |
| `connection_id` | A connection ID returned by `db.connect`. See the privileges below. |
| `password` | Optional. The password of the connection's account. Default: the password stored for the connection. |
| `sandbox_port` | Optional. The port of the sandbox instance that the connection is to. Pass it for a sandbox instance's daemon. |
| `sandbox_dir` | Optional. The sandbox directory. Must be in an allowed path. Leave empty for the default sandbox location. |
| `port` | Optional. The port that the daemon serves HTTPS on. Default: as described in [Deployments](#deployments). |
| `metadata_schema` | Optional. The REST metadata schema that the daemon serves. Required only when the server has more than one. |
| `restd_path` | Optional. The `mariadb-restd` executable, or its directory. Must be in an allowed path. |

The tool performs these steps in order:

1. Connects with the password, to check that it works.
2. Selects the REST metadata schema. A server with one metadata schema uses it. A server with several requires `metadata_schema`. On a server with none, the tool runs `CONFIGURE REST METADATA` to create `mariadb_rest_service`, or the schema named in `metadata_schema`.
3. Looks for `mariadb-restd` on the `PATH`, in `~/.local/bin`, and among the releases in `~/.local/share/mariadb-restd/<version>` (`%LOCALAPPDATA%\Programs\mariadb-restd\<version>` on Windows). If it finds none, it asks you to confirm, and then downloads and installs the latest release with the REST Daemon's install script.
4. Checks that the account has the privileges the setup needs.
5. Runs `mariadb-restd --setup`, which registers the daemon in the REST metadata, creates a server account for it, and writes the deployment folder. The password is passed on standard input, not on the command line.
6. Starts the daemon, and waits until it listens on its port.

The connection's account needs the following privileges. On a server without REST metadata, it also needs the privileges to create the metadata schema.

* `CREATE USER` with the `GRANT OPTION`.
* `SELECT`, `INSERT`, and `UPDATE` on the metadata schema.
* The metadata schema's `meta_provider` and `data_provider` roles `WITH ADMIN OPTION`.

The tool refuses to set up a second deployment in the same folder. Delete the existing one with `rest.delete_restd_config` first.

Returns the deployment's status, as `rest.get_restd_status` reports it, with two more fields.

| Field | Description |
| --- | --- |
| `installed` | Whether the tool installed `mariadb-restd` for this deployment. |
| `setup_output` | The output of `mariadb-restd --setup`. |

## rest.start_restd

Starts the daemon of a deployment. Does nothing when the daemon is already running.

| Argument | Description |
| --- | --- |
| `directory` | The deployment folder, as `rest.get_restd_status` lists it. A listed folder needs no allowed path; any other must be in one. |
| `restd_path` | Optional. The `mariadb-restd` executable, or its directory. Must be in an allowed path. Default: found in the places that `rest.configure_restd` searches. |

Returns the deployment's status, as `rest.get_restd_status` reports it. The daemon keeps running after the MCP server ends.

## rest.stop_restd

Stops the daemon of a deployment. Does nothing when the daemon is already stopped.

| Argument | Description |
| --- | --- |
| `directory` | The deployment folder, as `rest.get_restd_status` lists it. A listed folder needs no allowed path; any other must be in one. |

A daemon that doesn't stop within 30 seconds is killed. Returns the deployment's status, as `rest.get_restd_status` reports it.

## rest.delete_restd_config

Stops the daemon, drops the server account that the setup created for it, and deletes the deployment.

| Argument | Description |
| --- | --- |
| `directory` | The deployment folder, as `rest.get_restd_status` lists it. A listed folder needs no allowed path; any other must be in one. |
| `connection_id` | A connection ID returned by `db.connect`, for a connection to the deployment's server. Required unless `drop_accounts` is `False`. |
| `drop_accounts` | Whether to drop the daemon's server account and its registration in the `rest_daemon` table of the REST metadata. Default: `True`. Pass `False` to delete only the folder, for example when the server no longer exists. |

Only accounts that the setup generated are dropped. If the registration can't be deleted, the tool still deletes the folder and says so in its message.

## rest.get_restd_status

Lists the deployments of the sandbox instances in the default sandbox location and the deployments for other servers. The tool takes no arguments.

Returns one entry for each deployment, with the following fields.

| Field | Description |
| --- | --- |
| `directory` | The deployment folder. |
| `host` | The host of the server that the daemon serves. |
| `server_port` | The port of that server. |
| `port` | The port that the daemon listens on. |
| `url` | The daemon's URL, such as `https://localhost:8443`. |
| `status` | `running` or `stopped`. |
| `pid` | The daemon's process ID. `None` when the daemon is stopped. |
| `log_path` | The daemon's log file. |
| `metadata_schema` | The REST metadata schema that the daemon serves. |
| `connection_uri` | The URI of the connection that the deployment was set up with. |
| `sandbox_port` | The port of the sandbox instance. `None` for a deployment for another server. |

## Common Failures

| Symptom | Cause |
| --- | --- |
| `rest.configure_restd` reports several REST metadata schemas. | The server has more than one. Pass `metadata_schema`. |
| `rest.configure_restd` reports that `mariadb-restd` wasn't found and wasn't installed. | The installation wasn't confirmed, or the agent doesn't support confirmation requests. Install `mariadb-restd`, or pass `restd_path`. |
| `rest.configure_restd` reports what the account lacks. | The connection's account is missing a privilege the setup needs. Grant it, or use another connection. |
| `rest.configure_restd` reports an existing deployment. | The folder already holds one. Delete it with `rest.delete_restd_config` first. |
| A client refuses the daemon's certificate. | The certificate is self-signed. |
