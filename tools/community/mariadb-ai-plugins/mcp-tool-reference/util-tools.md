---
description: >-
  Reference for the util tools of the mariadb-shell MCP server, which dump, load, export, import, and copy data as background tasks.
---

# util Tools

The `util.*` tools run MariaDB Shell's dump, load, export, import, and copy utilities. Each utility runs as a background task, and the `util.get_task`, `util.list_tasks`, and `util.cancel_task` tools follow and stop the tasks.

{% hint style="info" %}
The `util.*` tools are available in MariaDB Shell 26.10.2 and later.
{% endhint %}

## Overview

| Tool | Description |
| --- | --- |
| `util.dump_instance` | Dumps the whole server to a directory. |
| `util.dump_schemas` | Dumps schemas to a directory. |
| `util.dump_tables` | Dumps tables and views of a schema to a directory. |
| `util.export_table` | Exports the rows of a table to a file. |
| `util.load_dump` | Loads a dump into a server. |
| `util.import_table` | Imports files into a table. |
| `util.copy_instance` | Copies the whole server to another server. |
| `util.copy_schemas` | Copies schemas to another server. |
| `util.copy_tables` | Copies tables of a schema to another server. |
| `util.get_task` | Returns the state of a task. |
| `util.list_tasks` | Lists the tasks of the client. |
| `util.cancel_task` | Stops a running task. |

The `util.*` tools are offered only together with the `db.*` group, because every utility works on a connection from `db.connect`. A server in multi-tenant mode never offers them.

The agent uses these tools instead of running `mariadb-dump` or piping its output into another client. The plugins' CLI guard blocks a `mariadb-dump` command that is piped into a client, and names the `util.copy_*` tools instead.

## Background Tasks

The dump, load, export, import, and copy tools start the utility and return at once, with the following fields.

| Field | Description |
| --- | --- |
| `task_id` | The ID to pass to `util.get_task` and `util.cancel_task`. |
| `status` | The task's status when the call returns. |

A task's status is `pending`, `running`, `completed`, `failed`, or `cancelled`. A finished task is kept for one hour, and the server keeps at most 100 finished tasks. A client can run at most four tasks at once, because a dump or load opens a session for each of its threads.

Each task runs the utility in a MariaDB Shell process of its own. That process logs in with the URI and the stored password of the connection that `connection_id` names, and receives the password on standard input, not on its command line. The task doesn't use the connection itself, so the connection stays available for other tools while the task runs. The MCP server finds the shell binary that it runs in itself, or `mariadb-shell` on the `PATH`.

When the MCP server ends, it stops the tasks that are still running.

## Options and Paths

Each tool takes an `options` argument with the options of the shell utility, named in camelCase, for example `{"threads": 8, "ddlOnly": true}`. For the options of each utility, see the MariaDB Shell documentation.

The tools set the following options themselves and refuse them in `options`.

* `session`
* `progressCallback`
* `showProgress`
* `outputUrl`, for `util.dump_schemas` and `util.dump_tables` only. Use the `output_url` argument.

A local path in `output_url`, `url`, or `urls`, and in the `progressFile`, `ociConfigFile`, `s3ConfigFile`, `s3CredentialsFile`, and `azureConfigFile` options, must be in an allowed path. See [Security Model](../security-model.md#paths). A path with wildcards is checked at its directory. A URL with a scheme other than `file://`, such as an `https://` URL, isn't a local path and isn't checked. When the `s3BucketName`, `osBucketName`, or `azureContainerName` option is set, `output_url`, `url`, and `urls` are prefixes in object storage and aren't checked either.

## util.dump_instance

Dumps the whole server to a directory.

| Argument | Description |
| --- | --- |
| `connection_id` | A connection ID returned by `db.connect`, for the server to dump. |
| `output_url` | The directory to write the dump to. It must not exist, or must be empty. |
| `options` | Optional. The options of the utility, such as `{"threads": 8, "users": false, "excludeSchemas": ["test"]}`. |

When the task completes, its `result` holds `output_url`.

## util.dump_schemas

Dumps schemas to a directory.

| Argument | Description |
| --- | --- |
| `connection_id` | A connection ID returned by `db.connect`. |
| `schemas` | The names of the schemas to dump. |
| `output_url` | The directory to write the dump to. It must not exist, or must be empty. |
| `options` | Optional. The options of the utility, such as `{"threads": 8, "ddlOnly": true}`. |

When the task completes, its `result` holds `output_url`.

## util.dump_tables

Dumps tables and views of a schema to a directory.

| Argument | Description |
| --- | --- |
| `connection_id` | A connection ID returned by `db.connect`. |
| `schema` | The schema that the tables are in. |
| `tables` | The names of the tables and views to dump. To dump all of them, pass an empty list and `{"all": true}` in `options`. |
| `output_url` | The directory to write the dump to. It must not exist, or must be empty. |
| `options` | Optional. The options of the utility, such as `{"where": {"shop.orders": "id > 1000"}}`. |

When the task completes, its `result` holds `output_url`.

## util.export_table

Exports the rows of a table to a file.

| Argument | Description |
| --- | --- |
| `connection_id` | A connection ID returned by `db.connect`. |
| `table` | The table, as `table` or `schema.table`. |
| `output_url` | The file to write. |
| `options` | Optional. The options of the utility, such as `{"dialect": "csv", "where": "id > 10"}`. |

When the task completes, its `result` holds `output_url`.

## util.load_dump

Loads a dump into a server. The server must have `local_infile` enabled.

| Argument | Description |
| --- | --- |
| `connection_id` | A connection ID returned by `db.connect`, for the server to load into. |
| `url` | The directory of a dump made with `util.dump_instance`, `util.dump_schemas`, or `util.dump_tables`. |
| `options` | Optional. The options of the utility, such as `{"schema": "copy_of_shop", "loadUsers": false, "dropExistingObjects": true}`. |

The load records its progress in a progress file, which is kept with the dump by default. If the shell process of the task crashes, the MCP server starts the load again from the progress file, up to three more times. A load that is stopped with `util.cancel_task` resumes where it stopped when the same dump is loaded again. A load from an `https://` URL, or with `progressFile` set to an empty string, has no progress file and isn't resumed.

When the task completes, its `result` holds `url`.

## util.import_table

Imports files into a table. The table must exist, and the server must have `local_infile` enabled.

| Argument | Description |
| --- | --- |
| `connection_id` | A connection ID returned by `db.connect`. |
| `urls` | A file, or a list of files, to import. File names can contain the wildcards `*` and `?`. |
| `options` | Optional. The options of the utility, such as `{"schema": "shop", "table": "orders", "dialect": "csv-unix", "skipRows": 1}`. |

When the task completes, its `result` holds `urls`, as a list.

## util.copy_instance

Copies the whole server to another server. The copy dumps from the source and loads into the target at the same time, and writes no files. The target must have `local_infile` enabled.

| Argument | Description |
| --- | --- |
| `connection_id` | A connection ID returned by `db.connect`, for the source server. |
| `target_connection_id` | A connection ID returned by `db.connect`, for the target server. It must be a different server. |
| `options` | Optional. The options of the utility, such as `{"users": false, "threads": 8}`. |

When the task completes, its `result` holds `target_connection_id`.

## util.copy_schemas

Copies schemas to another server. The copy dumps from the source and loads into the target at the same time, and writes no files. The target must have `local_infile` enabled.

| Argument | Description |
| --- | --- |
| `connection_id` | A connection ID returned by `db.connect`, for the source server. |
| `schemas` | The names of the schemas to copy. |
| `target_connection_id` | A connection ID returned by `db.connect`, for the target server. It must be a different server. |
| `options` | Optional. The options of the utility, such as `{"ddlOnly": true}`. |

When the task completes, its `result` holds `target_connection_id`.

## util.copy_tables

Copies tables of a schema to another server. The copy dumps from the source and loads into the target at the same time, and writes no files. The target must have `local_infile` enabled.

| Argument | Description |
| --- | --- |
| `connection_id` | A connection ID returned by `db.connect`, for the source server. |
| `schema` | The schema that the tables are in. |
| `tables` | The names of the tables and views to copy. |
| `target_connection_id` | A connection ID returned by `db.connect`, for the target server. It must be a different server. |
| `options` | Optional. The options of the utility. To load the tables into another schema, pass `{"schema": "<name>"}`. |

When the task completes, its `result` holds `target_connection_id`.

## util.get_task

Returns the state of a task.

| Argument | Description |
| --- | --- |
| `task_id` | The task ID that a `util.*` tool returned. |
| `since` | Optional. The `next_since` value of the previous call, to get only the messages printed after it. Default: `0`, which returns all the messages that are kept. |
| `wait_ms` | Optional. The number of milliseconds to wait for a change before the tool returns, at most 30000. The tool returns early when a message arrives or the task finishes. Default: `0`, which returns at once. |

Returns the following fields.

| Field | Description |
| --- | --- |
| `task_id` | The task ID. |
| `kind` | The utility, such as `dump_schemas`. |
| `title` | A short description of the task, such as `Dump shop to /backups/shop`. |
| `connection_id` | The connection that the task runs on. |
| `status` | `pending`, `running`, `completed`, `failed`, or `cancelled`. |
| `cancel_requested` | Whether `util.cancel_task` was called for the task. |
| `created_at`, `started_at`, `finished_at` | When the task was created, started, and finished, in ISO 8601 format and UTC. |
| `stage` | The stage that the utility is in. |
| `progress` | The progress of the current stage, with `current`, `total`, and `percent`, and `throughput`, `eta_seconds`, and `items` where the stage measures them. |
| `stages` | The stages that the utility has reached so far, each with its `name`, `status`, and duration in `seconds`. |
| `messages` | The messages after `since`. Each has a `seq`, `time`, `level`, and `text`. |
| `messages_dropped` | The number of messages after `since` that are no longer kept. A task keeps its last 2000 messages. |
| `next_since` | The value to pass as `since` in the next call. |
| `result` | When the task completed, what it produced, as described for each tool. |
| `error` | When the task failed, the error. |

## util.list_tasks

Lists the tasks of the client that are still kept. The tool takes no arguments.

Returns one entry for each task, with the fields that `util.get_task` returns, except `messages` and `messages_dropped`.

## util.cancel_task

Stops a running task. The utility is interrupted as if by Ctrl+C, and the task then ends as `cancelled`.

| Argument | Description |
| --- | --- |
| `task_id` | The task ID that a `util.*` tool returned. |

Returns the task's state, as `util.get_task` returns it, without `messages` and `messages_dropped`.

## Common Failures

| Symptom | Cause |
| --- | --- |
| The MCP server offers no `util.*` tools. | The server doesn't serve the `db.*` group, runs in multi-tenant mode, or is from a MariaDB Shell release earlier than 26.10.2. |
| A tool reports that the MariaDB Shell binary wasn't found. | The MCP server can't find a shell to run the task in. Put `mariadb-shell` on the `PATH`. |
| A tool reports that four tasks are already running. | The client has reached its limit of running tasks. Wait for a task to finish, or stop one with `util.cancel_task`. |
| A tool refuses an option. | The option is one that the tool sets itself. See [Options and Paths](#options-and-paths). |
| A load, import, or copy fails because of `local_infile`. | The server that the data goes into has `local_infile` disabled. |
| A dump fails because the output directory isn't empty. | `output_url` names a directory that already holds files. Use a new directory. |
