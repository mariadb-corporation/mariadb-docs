---
description: >-
  Reference for the optional migrator tools of the mariadb-shell MCP server, which migrate a MySQL database to MariaDB.
---

# migrator Tools

The `migrator.*` tools migrate a MySQL database to MariaDB with the MySQL-to-MariaDB migration tooling. These tools are optional and aren't included in the count of 28 tools.

{% hint style="info" %}
The `migrator.*` tools are registered only when the migration tooling is installed, on Linux and macOS. Install it with the following command, then restart the MCP server:

```bash
mariadb-shell -- mcp setup --installMigrator
```

A server without the tooling advertises none of these tools.
{% endhint %}

## Overview

| Tool | Description |
| --- | --- |
| `migrator.set_config` | Writes `config/migration.yaml`. |
| `migrator.plan` | Resolves the list of steps and validates the configuration, without running anything. |
| `migrator.run` | Runs the migration. |
| `migrator.resume` | Continues a failed run from its `state.json`. |

## migrator.set_config

Writes `config/migration.yaml`.

| Argument | Description |
| --- | --- |
| `mode` | The migration mode. |
| `env` | The migration settings, naming configured connections only. |
| `merge` | Whether to merge into the existing configuration. Default: `False`. |

Only configured connections may be named, and passwords are refused.

## migrator.plan

Resolves the list of steps and validates the configuration, without running anything.

| Argument | Description |
| --- | --- |
| `mode` | The migration mode. |
| `out` | Optional. The output directory. |
| `timeout` | Seconds. Default: `3600`. |

## migrator.run

Runs the migration.

| Argument | Description |
| --- | --- |
| `mode` | The migration mode. |
| `out` | The output directory. Omit it for a new run. |
| `timeout` | Seconds. Default: `3600`. |

## migrator.resume

Continues a failed run from its `state.json`.

| Argument | Description |
| --- | --- |
| `mode` | The migration mode. |
| `out` | The output directory of the failed run. Required. |
| `timeout` | Seconds. Default: `3600`. |

## Avoiding a False Success

{% hint style="danger" %}
The migration orchestrator is safe to resume. If `out` points at a directory that already holds a `state.json`, the run reports every step as `SKIPPED`, exits with status 0, and migrates nothing. Omit `out` for every new migration, pass it only to `migrator.resume`, and check that every step reports `DONE`.
{% endhint %}
