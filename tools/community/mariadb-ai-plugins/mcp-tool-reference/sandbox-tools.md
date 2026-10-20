---
description: >-
  Reference for the sandbox tools of the mariadb-shell MCP server, which list deployable MariaDB Server versions and deploy, start, stop, and delete local instances.
---

# sandbox Tools

The `sandbox.*` tools deploy and manage local MariaDB Server instances for development and testing. For an introduction, see [Sandbox Instances](../features/sandbox-instances.md).

## Overview

| Tool | Description |
| --- | --- |
| `sandbox.list_available_versions` | Lists the server versions `sandbox.deploy` can install. |
| `sandbox.deploy` | Creates and starts an instance, and registers its connection with the MCP server. |
| `sandbox.start` | Restarts an existing instance with its data intact. |
| `sandbox.stop` | Shuts an instance down gracefully. |
| `sandbox.kill` | Stops an instance forcefully. |
| `sandbox.delete` | Removes an instance. |
| `sandbox.vendor` | Returns the instance's vendor, `MariaDB` or `MySQL`. |
| `sandbox.version` | Returns the instance's server version. |

## sandbox.list_available_versions

Lists the server versions `sandbox.deploy` can install.

| Argument | Description |
| --- | --- |
| `series` | Optional. A series such as `11.8` or `11`. |

Without an argument, it lists the newest patch release of each series. With a series, it lists every release in that series. Only packages built for the current platform are listed, and every listed version can be deployed.

## sandbox.deploy

Creates and starts an instance, and registers its connection with the MCP server.

| Argument | Description |
| --- | --- |
| `port` | The instance's port. |
| `password` | The password for the instance's `root` user. A blank password produces a registered connection that is refused. |
| `sandbox_dir` | The sandbox directory. Must be in an allowed path. Leave empty for the default sandbox location. |
| `allow_root_from` | The host pattern for a remote `root` account. Default: `%`. An empty string skips creating the account. |
| `server_id` | The instance's `server_id`. |
| `ssl` | Whether to generate certificates and enable TLS. Default: `False`. `True` requires `openssl`. |
| `openssl_path` | The `openssl` executable, or its directory. |
| `server_version` | A version such as `11.8.9`, `11.8`, or `11`. Can't be combined with `mariadbd_path`. |
| `mariadbd_path` | The `mariadbd` binary, or its installation directory. |
| `mariadbd_options` | Additional options for the `[mysqld]` section, as `option=value` strings. |
| `timeout` | Seconds to wait for the instance to start. Default: `60`. |

Resolves a server from the `PATH`, then from already downloaded versions, then from the published index, so MariaDB Server doesn't need to be installed.

## sandbox.start

Restarts an existing instance with its data intact.

| Argument | Description |
| --- | --- |
| `port` | The instance's port. |
| `sandbox_dir` | The sandbox directory. Must be in an allowed path. Leave empty for the default sandbox location. |
| `mariadbd_path` | The `mariadbd` binary, or its installation directory. Required for a downloaded server. |
| `timeout` | Seconds to wait for the instance to start. Default: `60`. |

## sandbox.stop

Shuts an instance down gracefully.

| Argument | Description |
| --- | --- |
| `port` | The instance's port. |
| `sandbox_dir` | The sandbox directory. Must be in an allowed path. Leave empty for the default sandbox location. |
| `password` | The `root` password. Used on Windows to request the shutdown. |
| `timeout` | Seconds to wait for the instance to stop. Default: `60`. |

Can't stop an instance of a downloaded server, because it can't find the binary; use `sandbox.kill` for those.

## sandbox.kill

Stops an instance forcefully.

| Argument | Description |
| --- | --- |
| `port` | The instance's port. |
| `sandbox_dir` | The sandbox directory. Must be in an allowed path. Leave empty for the default sandbox location. |

The fallback when `sandbox.stop` doesn't work.

## sandbox.delete

Removes an instance.

| Argument | Description |
| --- | --- |
| `port` | The instance's port. |
| `sandbox_dir` | The sandbox directory. Must be in an allowed path. Leave empty for the default sandbox location. |

Refuses a running instance. Stop or kill it first.

## sandbox.vendor

Returns the instance's vendor, `MariaDB` or `MySQL`.

| Argument | Description |
| --- | --- |
| `port` | The instance's port. |
| `sandbox_dir` | The sandbox directory. Must be in an allowed path. Leave empty for the default sandbox location. |
| `mariadbd_path` | The `mariadbd` binary, or its installation directory. |

## sandbox.version

Returns the instance's server version.

| Argument | Description |
| --- | --- |
| `port` | The instance's port. |
| `sandbox_dir` | The sandbox directory. Must be in an allowed path. Leave empty for the default sandbox location. |
| `mariadbd_path` | The `mariadbd` binary, or its installation directory. |

## Common Failures

| Symptom | Cause |
| --- | --- |
| `sandbox.deploy` doesn't return. | The sandbox directory isn't on the allowed-paths list. |
| The deploy succeeds, but the connection is refused. | The password was blank. |
| The deploy fails on TLS. | `ssl` is `True` and `openssl` isn't installed. |
