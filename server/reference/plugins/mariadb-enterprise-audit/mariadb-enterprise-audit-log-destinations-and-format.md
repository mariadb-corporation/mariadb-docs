---
description: >-
  Send MariaDB Enterprise Audit output to a file or to syslog, configure log path and rotation, and parse the audit log record format.
---

# Enterprise Audit Log Destinations and Format

## Audit Log Destinations

MariaDB Enterprise Audit writes audit log messages either to a dedicated audit log file or to the system log (syslog), depending on configuration.

The audit log destination is configured with the [server\_audit\_output\_type](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_output_type) system variable:

| Value                                                             | Description                                                |
| ----------------------------------------------------------------- | ---------------------------------------------------------- |
| [FILE](#audit-logging-to-file)         | Audit log messages are written to a dedicated file.        |
| [SYSLOG](#audit-logging-to-system-log) | Audit log messages are written to the system log (syslog). |

## Audit Logging to File

MariaDB Enterprise Audit writes audit log messages to a dedicated audit log file when the [server\_audit\_output\_type](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_output_type) system variable is set to FILE.

### Audit Log Path

The path to the dedicated audit log file is configured with the [server\_audit\_file\_path](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_path) system variable. The path can be a relative or absolute path. If it is a relative path, then it will be relative to the [datadir](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir). For example, to set the path to mariadb-enterprise-audit.log with the [SET GLOBAL](../../sql-statements/administrative-sql-statements/set-commands/set.md) statement:

```sql
SET GLOBAL server_audit_file_path = 'mariadb-enterprise-audit.log'
```

When a system variable is dynamically changed with the [SET GLOBAL](../../sql-statements/administrative-sql-statements/set-commands/set.md) statement, the change does not survive server restarts. To ensure that the new path is used when the server restarts, set the [server\_audit\_file\_path](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_path) system variable in a configuration file:

```ini
[mariadb]
server_audit_file_path=mariadb-enterprise-audit.log
```

### Audit Log Rotation

When MariaDB Enterprise Audit is configured to use the dedicated audit log file, it can rotate the file.

The file is rotated when its size exceeds the size specified by the [server\_audit\_file\_rotate\_size](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_rotate_size) system variable. For example, to set the maximum log size to 2 GB with the [SET GLOBAL](../../sql-statements/administrative-sql-statements/set-commands/set.md) statement:

```sql
SET GLOBAL server_audit_file_rotate_size = 2 * (1024 * 1024 * 1024);
```

When a system variable is dynamically changed with the [SET GLOBAL](../../sql-statements/administrative-sql-statements/set-commands/set.md) statement, the change does not survive server restarts. To ensure that the new file rotation size is used when the server restarts, set the [server\_audit\_file\_rotate\_size](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_rotate_size) system variable in a configuration file:

```ini
[mariadb]
server_audit_file_rotate_size=2147483648
```

The file can also be rotated manually by setting the [server\_audit\_file\_rotate\_now](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_rotate_now) system variable to `ON`. For example, to rotate the log with the [SET GLOBAL](../../sql-statements/administrative-sql-statements/set-commands/set.md) statement:

```sql
SET GLOBAL server_audit_file_rotate_now = ON;
```

## Audit Logging to System Log

MariaDB Enterprise Audit writes audit log messages to the system log (syslog) when the [server\_audit\_output\_type](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_output_type) system variable is set to SYSLOG.

It can be very useful to configure audit logging to the syslog when your system's syslog is configured to securely transmit logs to a remote syslog server.

### System Log Parameters

Several syslog parameters can be changed for MariaDB Enterprise Audit by setting the following system variables:

* [server\_audit\_syslog\_facility](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_syslog_facility)
* [server\_audit\_syslog\_ident](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_syslog_ident)
* [server\_audit\_syslog\_info](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_syslog_info)
* [server\_audit\_syslog\_priority](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_syslog_priority)

## Audit Log Format

The audit log format for MariaDB Enterprise Audit depends on the [audit log destination](#audit-log-destinations) and on the `server_audit_log_format` system variable. By default, records are written in a comma-separated (CSV) format. From MariaDB Enterprise Server 12.3.3-1, they can be written in [JSON format](#json-format) instead.

### Formal Specification

When MariaDB Enterprise Audit is configured to use a dedicated file and the CSV format, it records events in a comma-separated (CSV) format. For tool developers, it is critical to use standardized field mappings to correlate audit data with other server logs.

Template: `<timestamp>,<serverhost>,<username>,<host>:<port>,<connectionid>,<queryid>,<operation>,<database>,<object>,<retcode>`

| Field | Component      | Data Type      | Standardized Name / Description                                                                                                       |
| ----- | -------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | `timestamp`    | `DateTime`     | Formatted as `%Y%m%d %H:%i:%s` (the default), or [as described below](#milliseconds-precision-timestamps). |
| 2     | `serverhost`   | `String`       | The hostname of the server instance.                                                                                                  |
| 3     | `username`     | `String`       | The MariaDB user account triggering the event.                                                                                        |
| 4     | `host`:`port`  | `String`       | The client host from which the user connected, followed by a colon and the client's TCP port. The port is written as `unavailable` when the client did not connect over TCP/IP, such as over a Unix socket or a named pipe. The port was added in MariaDB Enterprise Server 12.3. |
| 5     | `connectionid` | `Unsigned Int` | Standardized: Thread ID. Matches the `Thread ID` in Error, General, and Slow logs.                                                    |
| 6     | `queryid`      | `Unsigned Int` | A unique identifier for the specific query. Used to link Query and Table events.                                                      |
| 7     | `operation`    | `String`       | The type of action (e.g., `CONNECT`, `QUERY`, `WRITE`).                                                                               |
| 8     | `database`     | `String`       | The name of the database being accessed.                                                                                              |
| 9     | `object`       | `String`       | The specific table or object involved in the operation. On [connection events](mariadb-enterprise-audit-filter-types.md#connection-events), from MariaDB Enterprise Server 12.3.3-1, this field holds the negotiated TLS version, such as `TLSv1.3`, and is empty when the connection is not encrypted. |
| 10    | `retcode`      | `Integer`      | The return code; `0` indicates success, non-zero indicates an error code.                                                             |

{% hint style="warning" %}
**Changed in MariaDB Enterprise Server 12.3**

These changes to the log format require updates to tools that parse the audit log:

* The `host` field now contains a colon and the client port.
* Connection events record the negotiated TLS version. From MariaDB Enterprise Server 12.3.3-1, it is in the `object` field and the record ends at `retcode`, matching the [MariaDB Audit Plugin](../mariadb-audit-plugin/mariadb-audit-plugin-log-format.md). In MariaDB Enterprise Server 12.3.3-0, it was a trailing eleventh field after `retcode`.
* `CHANGE_USER` records write the new user name in the `object` field, followed by the TLS version and then `retcode`, so they have eleven fields.
{% endhint %}

#### Milliseconds Precision Timestamps

Auditing regulations and standards require auditing logs with timestamps recording fractions of a second and timezone information. To fulfill this requirement, MariaDB Enterprise Audit uses the system log (syslog) via the [server\_audit\_output\_type](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_output_type) option, where the timestamp format is controlled by the syslog setting.&#x20;

To define the format of the timestamp:

* Configure `server_audit_output_type=file`.&#x20;
* Set the `server_audit_timestamp_format` system variable in a configuration file (it is read-only at runtime), changing its default of `%Y%m%d %H:%i:%s` (which assures compatibility) to something including milliseconds (`%f`) and time zone information (`%z`), like `%Y%m%dT%H:%i:%s.%f%z`.

This results in audit log entries like these:

{% code expandable="true" %}
```
# for server_audit_timestamp_format=%Y%m%dT%H:%i:%s.%f%z
20231207T13:14:28.000000+0100,mdbe106,root,localhost,4,0,CONNECT,,,0
20231207T13:14:32.481161+0100,mdbe106,root,localhost,4,0,DISCONNECT,,,0
```
{% endcode %}

### Value Mapping for Operations

To build accurate filters and parsers, the `<operation>` field corresponds to the following standardized event types:

| Operation        | Triggered By                                                |
| ---------------- | ----------------------------------------------------------- |
| `CONNECT`        | Successful user authentication and connection.              |
| `FAILED_CONNECT` | Authentication failures or denied access.                   |
| `DISCONNECT`     | Session termination.                                        |
| `QUERY`          | Direct execution of a SQL statement.                        |
| `READ`           | Table read access (e.g., `SELECT`).                         |
| `WRITE`          | Table modification (e.g., `INSERT`, `UPDATE`, `DELETE`).    |
| `AUDIT_CONFIG`   | Changes to audit settings via `SET GLOBAL` or log rotation. |

### Audit Log Format with Syslog

When configured to use `SYSLOG`, the standard CSV line is prefixed with syslog metadata: `<timestamp> <syslog_host> <syslog_ident>: <syslog_info> [Standard CSV Fields]`

The CSV fields have no timestamp of their own, because syslog records the time.

### JSON Format

{% hint style="info" %}
The JSON format is available from MariaDB Enterprise Server 12.3.3-1.
{% endhint %}

When the `server_audit_log_format` system variable is set to `JSON`, MariaDB Enterprise Audit writes each record as a JSON object on a single line. JSON format makes the audit log easier to process with log analysis tools, and it is supported for both [audit log destinations](#audit-log-destinations).

To switch to JSON format with the [SET GLOBAL](../../sql-statements/administrative-sql-statements/set-commands/set.md) statement:

```sql
SET GLOBAL server_audit_log_format = 'JSON';
```

To ensure that the JSON format is used when the server restarts, set the variable in a configuration file:

```ini
[mariadb]
server_audit_log_format=JSON
```

#### `server_audit_log_format`

* Description: The format of the audit log records. `CSV` writes the [comma-separated format](#formal-specification). `JSON` writes [one JSON object per record](#json-record-fields).
* Command line: `--server-audit-log-format=value`
* Scope: Global
* Dynamic: Yes
* Data type: `enum`
* Default value: `CSV`
* Valid values: `CSV`, `JSON`
* Introduced: MariaDB Enterprise Server 12.3.3-1

#### Changing the Format

If the format is changed while audit logging to a file is active, MariaDB Enterprise Audit [rotates the audit log file](#audit-log-rotation), so that a file never contains records in both formats, and the statement returns this warning:

```
Warning (Code 1): Changing server_audit_log_format while file logging is active has triggered an automatic log rotation.
```

The new file starts with `AUDIT_CONFIG` records, in the new format, for the file path, rotation settings, and the new value of `log_format`.

When audit logging to the system log, no rotation takes place. Records written after the change use the new format.

#### JSON Record Fields

Every JSON record starts with these fields:

| Field           | JSON Type | Description                                                                                                                                                                |
| --------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `timestamp`     | String    | The time of the event, formatted according to `server_audit_timestamp_format` (see [Milliseconds Precision Timestamps](#milliseconds-precision-timestamps)). Omitted when logging to the system log, because syslog records the time. |
| `serverhost`    | String    | The hostname of the server instance.                                                                                                                                       |
| `username`      | String    | The MariaDB user account triggering the event.                                                                                                                             |
| `host`          | String    | The client host from which the user connected.                                                                                                                             |
| `port`          | String    | The client's TCP port, or `unavailable` when the client did not connect over TCP/IP, such as over a Unix socket or a named pipe. The port is a string, not a number.  |
| `connection_id` | Number    | The thread ID. Matches the `Thread ID` in Error, General, and Slow logs.                                                                                                   |
| `query_id`      | Number    | A unique identifier for the specific query. Used to link Query and Table events. `0` for connection events.                                                                |
| `operation`     | String    | The type of action, such as `CONNECT`, `QUERY`, or `WRITE`.                                                                                                                 |

Which fields follow depends on the operation:

| Operation                                                    | Additional Fields                                                                                                                                                                                                                      |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `QUERY`                                                      | `database`, `query` (the statement text, with passwords masked as in the CSV format), `error` (the error code as a number; `0` means success)                                                                                                                              |
| `READ`, `WRITE`, `CREATE`, `ALTER`, `DROP`                   | `database`, `table`                                                                                                                                                                                                                    |
| `RENAME`                                                     | `database`, `table`, `new_database`, `new_table`                                                                                                                                                                                       |
| `CONNECT`, `FAILED_CONNECT`, `DISCONNECT`, `CHANGE_USER_DONE` | `database`, `tls_version` (the negotiated TLS version, such as `TLSv1.3`, or an empty string when the connection is not encrypted), `status` (the error code as a number; `0` means success)                                         |
| `CHANGE_USER`                                                | `database`, `info` (the new user name, enclosed in backticks), `tls_version`, `status`                                                                                                                                                  |
| `PROXY_CONNECT`                                              | `database`, `proxy_user`, `proxy_host`, `status`                                                                                                                                                                                      |
| `AUDIT_CONFIG`                                               | `database`, a field named after the changed setting (such as `logging` or `log_format`) holding its new value as a string, `status`                                                                                                    |

For example, a statement, the table it accessed, and a connection look like this:

```json
{"timestamp":"20261029 10:15:02","serverhost":"db1","username":"app","host":"192.0.2.10","port":"53412","connection_id":12,"query_id":0,"operation":"CONNECT","database":"sales","tls_version":"TLSv1.3","status":0}
{"timestamp":"20261029 10:15:03","serverhost":"db1","username":"app","host":"192.0.2.10","port":"53412","connection_id":12,"query_id":45,"operation":"READ","database":"sales","table":"orders"}
{"timestamp":"20261029 10:15:03","serverhost":"db1","username":"app","host":"192.0.2.10","port":"53412","connection_id":12,"query_id":45,"operation":"QUERY","database":"sales","query":"SELECT * FROM orders WHERE id = 7","error":0}
```

String values are escaped so that each record is valid JSON: double quotes and backslashes are escaped with a backslash, control characters such as newlines and tabs are written as escape sequences (for example `\n` or `\u0001`), and bytes that are not valid UTF-8 are written as `\u00XX`. A statement that spans several lines is therefore still written as a single line.

When logging to the system log, the syslog metadata prefix is the same as for the CSV format, followed by the JSON object: `<timestamp> <syslog_host> <syslog_ident>: <syslog_info> {JSON object}`

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
