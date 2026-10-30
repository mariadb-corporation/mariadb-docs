---
description: >-
  Dump, load, copy, export and import data through the MariaDB MCP server,
  with background tasks a client follows and can cancel.
---

# Dump and Load Tools

<!--
  SYNCED: this page is maintained in mariadb-corporation/mariadb-shell, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-shell/).
  Make every change in mariadb-corporation/mariadb-shell. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

The `util` tools of the MCP server run the [dump](../utilities/dump-and-load/dump-utilities.md), [load](../utilities/dump-and-load/load-dump-utility.md), [copy](../utilities/dump-and-load/copy-utilities.md), [export and import](../utilities/table-export-and-import.md) utilities of MariaDB Shell on a connection opened with `db.connect`. These utilities run for minutes or hours, longer than an MCP client waits for a tool call to return, so each tool starts the work as a background **task** and returns its ID at once. The client then follows the task, and can cancel it.

The server provides these tools only when it provides the `db` group as well, and never in [multi-tenant mode](multi-tenant-mode.md).

## Tools

| Tool | Does | Arguments |
| --- | --- | --- |
| `util.dump_instance` | Runs `util.dump_instance()`. | `connection_id`, `output_url`, `options` |
| `util.dump_schemas` | Runs `util.dump_schemas()`. | `connection_id`, `schemas`, `output_url`, `options` |
| `util.dump_tables` | Runs `util.dump_tables()`. | `connection_id`, `schema`, `tables`, `output_url`, `options` |
| `util.export_table` | Runs `util.export_table()`. | `connection_id`, `table`, `output_url`, `options` |
| `util.load_dump` | Runs `util.load_dump()`. | `connection_id`, `url`, `options` |
| `util.import_table` | Runs `util.import_table()`. | `connection_id`, `urls` (a file or a list; names may contain `*` and `?`), `options` |
| `util.copy_instance` | Runs `util.copy_instance()`. | `connection_id`, `target_connection_id`, `options` |
| `util.copy_schemas` | Runs `util.copy_schemas()`. | `connection_id`, `schemas`, `target_connection_id`, `options` |
| `util.copy_tables` | Runs `util.copy_tables()`. | `connection_id`, `schema`, `tables`, `target_connection_id`, `options` |
| `util.get_task` | Returns the state of a task. | `task_id`, `since`, `wait_ms` |
| `util.list_tasks` | Lists the tasks of the client. | None |
| `util.cancel_task` | Stops a task. | `task_id` |

`options` holds the utility's own options, with their camelCase names, for example `{"threads": 8, "users": false}`. The tools set `showProgress` themselves, and refuse it, `session`, and `progressCallback` in `options`. The utility runs from MariaDB Shell's [command line](../using-mariadb-shell/command-line-integration.md), which can't pass some values on unchanged, so the tools refuse those too: a string that contains `\,`, `\"`, `\'`, or `\=`, and a name or path such as `2024`, `true`, or `-x` where the command line takes it without an option name. An option name must consist of letters, digits, `_`, and `-`. A copy takes no option that is a connection attribute, such as `host`, `port`, `user`, `password`, `socket`, or an `ssl-` or `ssh-` option, however it's spelled: its target is the connection that `target_connection_id` names, and the options can't change it.

Each start tool returns the task's ID and status:

```json
{"task_id": "4c0d0f0e-5a51-4a34-9c6e-0b8d2f3c1e77", "status": "running"}
```

## Following a Task

`util.get_task` returns the task's state:

| Field | Content |
| --- | --- |
| `status` | `pending`, `running`, `completed`, `failed`, or `cancelled`. |
| `title`, `kind` | What the task does, such as `Dump shop to /backups/shop` and `dump_schemas`. |
| `stages` | The stages of the utility so far, such as `Gathering information`, `Writing DDL`, and `Dumping data`, each with its status and, once finished, its duration in seconds. |
| `stage`, `progress` | The current stage and its progress: `current`, `total`, and `percent`. For a stage that moves data, also `throughput` (items per second), `eta_seconds`, and `items` (`bytes` or `rows`). |
| `messages` | What the utility printed after `since`, each with `seq`, `time`, `level` (such as `status`, `warning`, or `error`), and `text`. |
| `next_since` | The `since` for the next call, to get only new messages. Leave `since` out on the first call. |
| `result`, `error` | Once the task ended: what it produced, such as the dump's folder, or why it failed. |

With `wait_ms` (at most 30000), the call answers as soon as the task changes, for example at its next progress update, so a client need not poll in a tight loop. It answers at once when there are new messages or the task has ended:

```json
{"task_id": "4c0d0f0e-5a51-4a34-9c6e-0b8d2f3c1e77", "since": 12, "wait_ms": 30000}
```

Once `status` is `completed`, `failed`, or `cancelled`, the task doesn't change any more.

## Cancelling a Task

`util.cancel_task` interrupts the utility as Ctrl+C does when you run it in MariaDB Shell, and the task ends as `cancelled`. If the utility hasn't stopped 30 seconds later, its process is ended. A load that was cancelled [resumes where it stopped](../utilities/dump-and-load/load-dump-utility.md#resuming-an-interrupted-load) when you load the same dump again.

## How Tasks Run

* **A task runs in a MariaDB Shell process of its own,** connected to the server of the connection that `connection_id` names, with the same checks as a session that is [reopened after an idle period](security-and-session-handling.md#session-lifetime). The password goes to the process's standard input, never on its command line. The connection's own session stays free, so other tools can use it while the task runs, and the process ends with the MCP server.
* **A crash ends only the task's process.** The task then reports what happened. A load is started again, up to three times, and [resumes where it stopped](../utilities/dump-and-load/load-dump-utility.md#resuming-an-interrupted-load). A crashed dump, copy, export, or import fails, because starting it again wouldn't continue its work.
* **Tasks belong to the client that started them,** as [connections do](security-and-session-handling.md#connections-belong-to-the-client-that-opened-them). To another client, the task doesn't exist.
* **Limits:** a client can run four tasks at the same time. A finished task is kept for one hour, and the server keeps 100 finished tasks at most.
* **Paths** are checked against the [allowed directories](configuring-access.md#allowed-paths). A URL, and an object storage prefix given with `s3BucketName`, `osBucketName`, or `azureContainerName`, are passed to the utility unchecked.

<sub>_This page is licensed: GPLv2_</sub>
