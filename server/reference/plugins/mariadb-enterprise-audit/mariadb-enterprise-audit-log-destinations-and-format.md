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

The audit log format for MariaDB Enterprise Audit depends on the [audit log destination](#audit-log-destinations).

### Formal Specification

When MariaDB Enterprise Audit is configured to use a dedicated file, it records events in a comma-separated (CSV) format. For tool developers, it is critical to use standardized field mappings to correlate audit data with other server logs.

Template: `<timestamp>,<serverhost>,<username>,<host>:<port>,<connectionid>,<queryid>,<operation>,<database>,<object>,<retcode>,<tlsversion>`

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
| 9     | `object`       | `String`       | The specific table or object involved in the operation.                                                                               |
| 10    | `retcode`      | `Integer`      | The return code; `0` indicates success, non-zero indicates an error code.                                                             |
| 11    | `tlsversion`   | `String`       | The TLS version negotiated for the connection, such as `TLSv1.3`. Present only on [connection events](mariadb-enterprise-audit-filter-types.md#connection-events), and empty when the connection is not encrypted. Added in MariaDB Enterprise Server 12.3. |

{% hint style="warning" %}
**Changed in MariaDB Enterprise Server 12.3**

Two changes to the log format require updates to tools that parse the audit log:

* The `host` field now contains a colon and the client port.
* Connection event records carry an eleventh field. Records for all other operations still end at `retcode`.
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

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
