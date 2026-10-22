---
description: >-
  Check the connection of GridGain MCP Server, and learn how it limits calls, what the audit log records, how to read its logs and exit codes, and how to fix common problems.
---

# Operating MCP Server

This page describes how to check the server, how it limits the calls, what it records, and how to fix common problems.

## Checking the Connection

Use the `--check` flag to test the settings and the connection without an assistant.
The server validates the settings, connects to the cluster, runs `SELECT 1`, prints one line of JSON, and exits.
It does not wait for input and does not start MCP.

```shell
GRIDGAIN_HOST=db.example.com:10800 java -jar gridgain-mcp-<version>.jar --check --retry-attempts=0
```

With the container image:

```shell
docker run --rm -e GRIDGAIN_HOST=db.example.com gridgain/mcp:<version> --check --retry-attempts=0
```

The output is the result of the `check_database_connection` tool and three more fields: `tls`, `mcpVersion`, and `javaVersion`.
It never contains the password.

```json
{"message":"GridGain cluster answered SELECT 1","elapsedMillis":12,"addresses":["db.example.com:10800"],"clusterVersion":"8.10.127#20261002-sha1:0123abcd","tls":false,"mcpVersion":"8.10.127","javaVersion":"17.0.12+7"}
```

The exit code shows the result:

| Code | Meaning |
| ---- | ------- |
| `0` | The cluster answered `SELECT 1`. |
| `1` | The check, the clean-up, or the report did not finish. There is no report. |
| `2` | The configuration is invalid. The reason is on standard error, and nothing is printed to standard output. |
| `3` | The check failed. The `code` field of the report is `TIMEOUT`, `CONNECTION_ERROR`, or `QUERY_ERROR`. |

The check repeats the connection attempts like the server does.
With the default settings, an unreachable cluster can take minutes to report, so use `--retry-attempts=0` to try only once.
The rate limit and the audit log do not apply to `--check`.

## Rate Limit

The server limits how often the assistant can call a tool.
This protects the cluster from an assistant that gets stuck in a loop.

Each tool has its own limit, `MCP_RATE_LIMIT_DEFAULT_PER_MINUTE` calls per minute, 100 by default.
Unused calls build up to the same number, so a short burst of calls is allowed, but a long series of calls is slowed down.
The limit applies to one running server and to each tool separately.
When the server restarts, all limits start fresh.

When a call is over the limit, the tool does not run.
The result is marked as an error and contains the following text:

```json
{"error":"Rate limit exceeded; retry after retryAfterMs","code":"RATE_LIMITED","retryAfterMs":600}
```

`retryAfterMs` is the time in milliseconds until the tool accepts the next call.
Calls to unknown tools and calls with invalid arguments are refused before the limit applies, and they do not count against it.

To turn the limit off, set `MCP_RATE_LIMIT_ENABLED=false`.

## Audit Log

The server writes one line of JSON to the audit log for every tool call that reaches a tool.
This includes the calls that the rate limit refuses.

```json
{"timestamp":"2026-10-09T10:15:30.123Z","user":"mcp_reader","tool":"check_database_connection","outcome":"error","durationMs":12}
```

| Field | Description |
| ----- | ----------- |
| `timestamp` | The start of the call, in UTC. |
| `user` | The user name that you configured. The field is missing if you did not set one. |
| `tool` | The name of the tool. |
| `outcome` | `ok`, `error` (the tool returned an error or failed), or `refused-rate-limit`. |
| `durationMs` | The duration of the call in milliseconds. |

The log never contains passwords, TLS secrets, or the rows of a result.
The SQL text of a query is not recorded.
Calls to unknown tools, calls with invalid arguments, and `--check` are not recorded.

The server writes the log in the background. If a write fails, the server reports it on standard error and does not fail the call.

### Location and Permissions

By default, the log is the file `~/.gridgain8/mcp/logs/audit.log`.
Use `MCP_AUDIT_LOG_PATH` to choose another file.

On systems that support POSIX permissions:

- The server creates missing folders with mode `0700` and the file with mode `0600`.
- The server restricts an existing file that is more open than `0600` to `0600`.
- The server does not start if the existing folder of the log belongs to another user. It also does not start if the folder is open to the group or to other users.

The log folder can be a symbolic link, but the log file cannot.
FAT file systems on Linux and all file systems on Windows do not support these checks, and the server does not check or change the permissions there.

The server exits with code 2 and an error message in the following cases:

- The path is empty or names no file.
- The file name contains any of the characters `% $ { } * ? [ ]`.
- The path starts with `~/`, and the system does not report a home folder for the user.
- The file cannot be opened for writing.

If the checks do not suit your system, set `MCP_AUDIT_LOG_PATH` to a suitable folder, or turn the log off with `MCP_AUDIT_ENABLED=false`.

When the server restarts on the same day (UTC), it continues in the same file.
Several servers can write to the same file, so a program that reads the log should skip empty lines.

### Rotation

The server starts a new file when the day changes (UTC) and before a line would make the file larger than `MCP_AUDIT_MAX_FILE_SIZE_MB`.
It renames the old file to `<name>.<yyyy-MM-dd>.<n>`, where the date is the day of the last line and `n` counts from 1.
Then it compresses the file to `<name>.<yyyy-MM-dd>.<n>.gz`.
On a day without calls, nothing is rotated. The next call rotates the old file.

At every rotation, the server deletes the rotated files that are older than `MCP_AUDIT_RETENTION_DAYS`.
The server keeps the current day and that number of days before it.
The server deletes only the files in the log folder whose names follow the rotated pattern.

If a rotation fails, the server reports it and continues in the current file.
It tries again on the next day, or after another `MCP_AUDIT_MAX_FILE_SIZE_MB`.

{% hint style="warning" %}
Several servers can share one log file, but this has limits.
After a rotation by another server, a server reopens the new file before its next line.
A line that it writes at this moment can be lost.
On Windows, servers that share a file lose lines at every rotation.
If every line matters, give each server its own `MCP_AUDIT_LOG_PATH`. On Windows, always do so.
{% endhint %}

## Server Log

The server writes its own messages to standard error.
By default, it records warnings and errors.
The log replaces the password and the store passwords with `***`.
Standard output carries the protocol, and the server writes nothing else there.

To get more detail, add a Log4j2 configuration file next to the default one.
The following example adds a file `debug.xml`, which contains only `<Root level="debug"/>`:

```shell
LOG4J_CONFIGURATION_FILE=classpath:log4j2.xml,/path/to/debug.xml
```

## Exit Codes

The assistant ends the session by closing the standard input of the server.
The server answers the requests that it has already read within 5 seconds and exits.

| Code | Meaning |
| ---- | ------- |
| `0` | Every response was written. |
| `1` | The session ended in another way. The reason is on standard error. The host may have stopped reading the output, or sent a line that is damaged or too large. |
| `2` | The configuration was rejected before the server started. |

## Troubleshooting

| Problem | What to do |
| ------- | ---------- |
| The container stops at once. | Start it with `-i`. Without it, the standard input is empty, and the server exits. |
| `NoClassDefFoundError` at start. | The `libs` folder is not next to the JAR file. Move them together, or use the single JAR from the `standalone` folder. |
| The JAR file does not load. | The Java version is older than 17. Install Java 17 or later. |
| The server exits with code 2. | Read the message on standard error. It names the setting and the reason, such as an unknown flag, a value out of range, or a store that does not open. |
| `CONNECTION_ERROR` from a container, and the cluster runs on your machine. | `localhost` inside the container is the container. See [Reaching the Cluster From a Container](installation.md#reaching-the-cluster-from-a-container). |
| `CONNECTION_ERROR`, and the credentials are wrong. | The cluster rejected them. The server does not repeat the attempt. Check `GRIDGAIN_USERNAME` and `GRIDGAIN_PASSWORD`. |
| `CONNECTION_ERROR` with TLS. | Check `GRIDGAIN_SSL_MODE`. A TLS client that connects to a node without TLS waits for the connection timeout. A security plugin can also reject a connection in a way that looks like an unreachable host, so the server repeats the attempt. |
| Every call takes minutes before it fails. | The server is repeating the connection attempts. Lower `MCP_RETRY_ATTEMPTS`, or use `--check --retry-attempts=0` to find the cause. |
| `TIMEOUT` for a query. | The query ran longer than `MCP_OPERATION_TIMEOUT`. Narrow the query or increase the timeout. |
| `AUTHORIZATION` | The account lacks a permission. See [Preparing a Cluster Account](security.md#preparing-a-cluster-account). |
| `REJECTED` | The statement is not a single `SELECT`. Read the `reason` field and see [Running Queries](tools-and-resources.md#running-queries). |
| `RATE_LIMITED` | The assistant calls a tool too often. Wait for `retryAfterMs`, or raise `MCP_RATE_LIMIT_DEFAULT_PER_MINUTE`. |
| `BUSY` | Too many calls are waiting. Wait and try again, or raise `MCP_MAX_CONCURRENT_QUERIES`. |
| The result is cut (`truncated` is `true`). | Narrow the query with `WHERE` or `LIMIT`. To get more data, raise `MCP_MAX_ROWS` or `MCP_MAX_RESPONSE_BYTES`. |
| A join returns fewer rows than expected. | Distributed joins are not enabled, and the tables may not be colocated. Read the `gridgain://sql-dialect` resource. |
| The server does not start because of the audit log. | The folder of the log is open to other users, belongs to another user, or is not writable. See [Location and Permissions](#location-and-permissions). |
