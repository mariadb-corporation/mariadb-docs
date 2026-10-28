---
description: >-
  Check the connection of GridGain MCP Server, and learn how it limits calls, what the audit log records, how to read its logs and exit codes, and how to fix common problems.
---

# Operating MCP Server

An MCP host starts GridGain MCP Server in the background, so you do not watch it run.
To check and monitor the server, use the connection check, the audit log, the server log, and the exit codes.
The server also limits how often the assistant can call each tool.

## Checking the Connection

The `--check` flag tests the settings and the connection without an assistant.
The server validates the settings, connects to the cluster, runs `SELECT 1`, prints one line of JSON, and exits.
It does not wait for input and does not start MCP.

To check the connection with the JAR file:

```shell
GRIDGAIN_HOST=db.example.com:10800 java -jar gridgain-mcp-<version>.jar --check --retry-attempts=0
```

To check the connection with the container image:

```shell
docker run --rm -e GRIDGAIN_HOST=db.example.com gridgain/mcp:<version> --check --retry-attempts=0
```

The check repeats the connection attempts like the server does.
With the default settings, an unreachable cluster can take minutes to report, so use `--retry-attempts=0` to try only once.
The rate limit and the audit log do not apply to `--check`.

### Check Report

The report is the result of the `check_database_connection` tool with three more fields: `tls`, `mcpVersion`, and `javaVersion`.
It never contains the password.

```json
{"message":"GridGain cluster answered SELECT 1","elapsedMillis":12,"addresses":["db.example.com:10800"],"clusterVersion":"8.10.0#20261002-sha1:0123abcd","tls":false,"mcpVersion":"8.10.0","javaVersion":"17.0.12+7"}
```

The exit code of the check shows the result:

| Code | Meaning |
| ---- | ------- |
| `0` | The cluster answered `SELECT 1`. |
| `1` | The check, the cleanup, or the report did not finish. There is no report. |
| `2` | The configuration is invalid. The reason is on standard error, and nothing is printed to standard output. |
| `3` | The check failed. The `code` field of the report is `TIMEOUT`, `CONNECTION_ERROR`, or `QUERY_ERROR`. |

## Rate Limit

The rate limit protects the cluster from an assistant that calls a tool in a loop.
By default, each tool allows 100 calls per minute. You set the number with `MCP_RATE_LIMIT_DEFAULT_PER_MINUTE`.

The limit works as follows:

- Each tool has its own limit.
- Unused calls build up to the same number. A short burst of calls is allowed, but a long series of calls is slowed down.
- The limit applies to one running server. When the server restarts, all limits start fresh.
- Calls to unknown tools and calls with invalid arguments are refused before the limit applies. They do not count against it.

When a call is over the limit, the tool does not run.
The result is marked as an error and has only text, with no structured content:

```json
{"error":"Rate limit exceeded; retry after retryAfterMs","code":"RATE_LIMITED","retryAfterMs":600}
```

The message says `retryAfterMs` literally. This is the exact text, not a bug.
The `retryAfterMs` field holds the time in milliseconds until the tool accepts the next call.

To turn the limit off, set `MCP_RATE_LIMIT_ENABLED=false`.

## Audit Log

The audit log records the tool calls of the assistant, so you can review what the assistant did on the cluster.
The log is on by default. To turn it off, set `MCP_AUDIT_ENABLED=false`.

### Log Entries

The server writes one line of JSON for every tool call that reaches a tool.
This includes the calls that the rate limit refuses.

```json
{"timestamp":"2026-10-09T10:15:30.123Z","user":"mcp_reader","tool":"check_database_connection","outcome":"error","durationMs":12}
```

| Field | Description |
| ----- | ----------- |
| `timestamp` | The start of the call, in UTC. |
| `user` | The user name that you configured. The field is missing if you did not set one. |
| `tool` | The name of the tool. |
| `outcome` | `ok`, `error` (the tool returned an error or failed, or the host cancelled the call), or `refused-rate-limit`. |
| `durationMs` | The duration of the call in milliseconds. |

The log does not record the following:

- Passwords, TLS secrets, or the rows of a result.
- The SQL text of a query.
- Calls to unknown tools and calls with invalid arguments.
- The `--check` run.

The server writes the log in the background. If a write fails, the server reports it on standard error and does not fail the call.
If 1,024 entries are already waiting to be written, or the log is closing, the server drops the entry.
It reports the number of dropped entries on standard error.

### Location and Permissions

By default, the log is the file `~/.gridgain8/mcp/logs/audit.log`.
To choose another file, set `MCP_AUDIT_LOG_PATH`.

On systems that support POSIX permissions, the server protects the log:

- It creates missing folders with mode `0700` and the file with mode `0600`.
- It restricts an existing file that is more open than `0600` to `0600`.
- It does not start if the log folder belongs to another user, or if the folder is open to the group or to other users.

The log folder can be a symbolic link, but the log file cannot.

The server skips these checks on file systems without POSIX attributes, such as FAT on Linux and all file systems on Windows.
It does not change the permissions there.
On mounts such as exFAT or SMB, the server checks the permissions that the mount options report.

The server exits with code `2` and an error message in the following cases:

- The path is empty or names no file.
- The file name contains any of the characters `% $ { } * ? [ ]`.
- The path starts with `~/`, and the system does not report a home folder for the user.
- The file cannot be opened for writing.
- The log folder belongs to another user, or is open to the group or to other users.
- The log file is a symbolic link.

The server does not open the audit log with `--check`, so these checks do not run there.
If the checks do not suit your system, set `MCP_AUDIT_LOG_PATH` to a suitable folder, or turn the log off.

### Rotation

The server starts a new log file when the day changes (UTC), and before a line would make the file larger than `MCP_AUDIT_MAX_FILE_SIZE_MB`.
It renames the old file to `<name>.<yyyy-MM-dd>.<n>`, where the date is the day of the last line and `n` counts from 1.
Then it compresses the file to `<name>.<yyyy-MM-dd>.<n>.gz`.

On a day without calls, nothing is rotated. The next call rotates the old file.
When the server restarts on the same day (UTC), it continues in the same file.

At every rotation, the server deletes the rotated files that are older than `MCP_AUDIT_RETENTION_DAYS`.
It keeps the current day and that number of days before it.
It deletes only the files in the log folder whose names follow the rotated pattern.

If a rotation fails, the server reports it and continues in the current file.
It tries again on the next day, or after another `MCP_AUDIT_MAX_FILE_SIZE_MB`.
If the server stops during a rotation, it skips the compression and the cleanup until the next rotation.

### Sharing a Log File

Several servers can write to the same log file.
A program that reads a shared log should skip empty lines.

{% hint style="warning" %}
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

To get more detail, add a Log4j2 configuration file next to the default one, such as `debug.xml`:

```shell
LOG4J_CONFIGURATION_FILE=classpath:log4j2.xml,/path/to/debug.xml
```

The following `debug.xml` sets the root log level and uses the appender of the default configuration:

```xml
<Configuration>
    <Loggers>
        <Root level="debug"/>
    </Loggers>
</Configuration>
```

{% hint style="warning" %}
The default appender masks the passwords. If your configuration defines its own appender, the server log shows the passwords in plain text.
{% endhint %}

## Session Exit Codes

The assistant ends a session by closing the server's standard input.
The server answers the requests that it has already read within 5 seconds and exits with one of the following codes:

| Code | Meaning |
| ---- | ------- |
| `0` | Every response was written. |
| `1` | The session ended in another way. The reason is on standard error. The host may have stopped reading the output, or sent a line that is damaged or too large. |
| `2` | The configuration was rejected before the server started. |

For the exit codes of `--check`, see [Check Report](#check-report).

## Troubleshooting

Find the error code or the symptom in the first column.
For the meaning of each error code, see [Query Errors](tools-and-resources.md#query-errors).

| Problem | What to do |
| ------- | ---------- |
| The container stops at once. | Start it with `-i`. Without it, the standard input is empty, and the server exits. |
| `NoClassDefFoundError` at start. | The `libs` folder is not next to the JAR file. Move them together, or use the single JAR from the `standalone` folder. |
| The JAR file does not load. | The Java version is older than 17. Install Java 17 or later. |
| The server exits with code 2. | Read the message on standard error. It names the setting and the reason, such as an unknown flag, a value out of range, or a store that does not open. |
| `CONNECTION_ERROR` from a container, and the cluster runs on your machine. | `localhost` inside the container is the container. See [Reaching the Cluster From a Container](installation.md#reaching-the-cluster-from-a-container). |
| `CONNECTION_ERROR`, and the credentials are wrong. | The cluster rejected them. The server does not repeat the attempt. Check `GRIDGAIN_USERNAME` and `GRIDGAIN_PASSWORD`. |
| `CONNECTION_ERROR` with TLS. | Check that `GRIDGAIN_SSL_MODE` matches the cluster. A mismatch can look like an unreachable cluster. A security plugin can also reject a connection in a way that looks like an unreachable host, so the server repeats the attempt. |
| Every call takes minutes before it fails. | The server is repeating the connection attempts. Lower `MCP_RETRY_ATTEMPTS`, or use `--check --retry-attempts=0` to find the cause. |
| `TIMEOUT` for a query. | The query ran longer than `MCP_OPERATION_TIMEOUT`, or the call waited too long for a free worker. Narrow the query, increase the timeout, or raise `MCP_MAX_CONCURRENT_QUERIES`. |
| `AUTHORIZATION` | The account lacks a permission. See [Preparing a Cluster Account](security.md#preparing-a-cluster-account). |
| `REJECTED` | The statement is not a single `SELECT`. Read the `reason` field and see [Statement Check](tools-and-resources.md#statement-check). |
| `RATE_LIMITED` | The assistant calls a tool too often. Wait for `retryAfterMs`, or raise `MCP_RATE_LIMIT_DEFAULT_PER_MINUTE`. |
| `BUSY` | Too many calls are waiting. Wait and try again, or raise `MCP_MAX_CONCURRENT_QUERIES`. |
| The result is truncated (`truncated` is `true`). | Narrow the query with `WHERE` or `LIMIT`. To get more data, raise `MCP_MAX_ROWS` or `MCP_MAX_RESPONSE_BYTES`. |
| A join returns fewer rows than expected. | Distributed joins are not enabled, and the tables may not be colocated. Read the `gridgain://sql-dialect` resource. |
| The server does not start because of the audit log. | The log folder is open to other users, belongs to another user, or is not writable. See [Location and Permissions](#location-and-permissions). |
