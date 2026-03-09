---
description: >-
  Understand the structure of audit log entries. This guide breaks down the
  fields in the log records, including timestamps, server IDs, user details, and
  the specific operations performed.
---

# Audit Plugin Log Format

The audit plugin logs user access to MariaDB and its objects. The audit trail (that is, the audit log) is a set of records, written as a list of fields to a file in a plain‐text format. The fields in the log are separated by commas. The format used for the plugin's own log file is slightly different from the format used if it logs to the system log because it has its own standard format.&#x20;

## Formal Specification

When the MariaDB Audit Plugin (v1) writes to a dedicated file, it uses a comma-separated (CSV) format. For tool developers, it is essential to map the `connectionid` to the server's global connection identifier to enable cross-log analysis.

Template: `<timestamp>,<serverhost>,<username>,<host>,<connectionid>,<queryid>,<operation>,<database>,<object>,<retcode>`

| Field | Component      | Data Type      | Standardized Name / Description                                                           |
| ----- | -------------- | -------------- | ----------------------------------------------------------------------------------------- |
| 1     | `timestamp`    | `DateTime`     | Formatted as `YYYYMMDD HH:MM:SS`.                                                         |
| 2     | `serverhost`   | `String`       | Hostname of the originating server.                                                       |
| 5     | `connectionid` | `Unsigned Int` | Standardized: Thread ID. Matches the `Thread ID` in Error, General, and Slow logs.        |
| 6     | `queryid`      | `Unsigned Int` | A unique identifier for the specific query, used to correlate `QUERY` and `TABLE` events. |
| 7     | `operation`    | `String`       | Action type (e.g., `CONNECT`, `QUERY`, `READ`, `WRITE`).                                  |
| 10    | `retcode`      | `Integer`      | Result code (`0` for success).                                                            |

### Audit Log Format with Syslog

If `server_audit_output_type` is set to `SYSLOG`, the standard CSV line is prefixed with syslog metadata: `<timestamp> <syslog_host> <syslog_ident>: <syslog_info> [Standard CSV Fields]`

Various events result in different audit records. Some events do not return a value for some fields (for instance, when the active database is not set when connecting to the server).

Below is a generic example of the output for connect events, with placeholders representing data. These are events in which a user connected, disconnected, or tried unsuccessfully to connect to the server.

```ini
[timestamp],[serverhost],[username],[host],[connectionid],0,CONNECT,[database],,0 
[timestamp],[serverhost],[username],[host],[connectionid],0,DISCONNECT,,,0 
[timestamp],[serverhost],[username],[host],[connectionid],0,FAILED_CONNECT,,,[retcode]
```

Here is the one audit record generated for each query event:

```ini
[timestamp],[serverhost],[username],[host],[connectionid],[queryid],QUERY,[database],[object], [retcode]
```

Below are generic examples of records that are entered in the audit log for each type of table event:

```ini
[timestamp],[serverhost],[username],[host],[connectionid],[queryid],CREATE,[database],[object], 
[timestamp],[serverhost],[username],[host],[connectionid],[queryid],READ,[database],[object], 
[timestamp],[serverhost],[username],[host],[connectionid],[queryid],WRITE,[database],[object], 
[timestamp],[serverhost],[username],[host],[connectionid],[queryid],ALTER,[database],[object], 
[timestamp],[serverhost],[username],[host],[connectionid],[queryid],RENAME,[database], 
[object_old]|[database_new].[object_new], 
[timestamp],[serverhost],[username],[host],[connectionid],[queryid],DROP,[database],[object],
```

Passwords are hidden in the log for certain types of queries. They are replaced with asterisks for `GRANT`, `CREATE USER`, `CREATE MASTER`, `CREATE SERVER`, and `ALTER SERVER` statements. Passwords, however, are not replaced for the `PASSWORD()` and `OLD_PASSWORD()` functions when they are used inside other SQL statements (i.e., `SET PASSWORD`).

{% tabs %}
{% tab title="Current" %}
For [Galera Cluster replication](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/high-availability/using-mariadb-replication-with-mariadb-galera-cluster/using-mariadb-replication-with-mariadb-galera-cluster-using-mariadb-replica) applier operations, audit log plugin logs events with a generic name of `<wsrep_applier>` .

This addresses an issue where the user was logged on the primary node, but stripped from other cluster nodes. See [MDEV-35511](https://jira.mariadb.org/browse/MDEV-35511) for details.
{% endtab %}

{% tab title="< 10.11.16" %}
For Galera Cluster replication applier operations, audit log plugin logs events without indicating what user initiates them.
{% endtab %}
{% endtabs %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
