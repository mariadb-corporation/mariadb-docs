# Audit Plugin Log Format

The audit plugin logs user access to MariaDB and its objects. The audit trail (i.e., audit log) is a set of records, written as a list of fields to a file in a plain‐text format. The fields in the log are separated by commas. The format used for the plugin's own log file is slightly different from the format used if it logs to the system log because it has its own standard format. The general format for the logging to the plugin's own file is defined like the following:

```ini
[timestamp],[serverhost],[username],[host],[connectionid],
[queryid],[operation],[database],[object],[retcode]
```

If the [server\_audit\_output\_type](mariadb-audit-plugin-options-and-system-variables.md) variable is set to `syslog` instead of the default, `file`, the audit log file format will be as follows:

```ini
[timestamp][syslog_host][syslog_ident]:[syslog_info][serverhost],[username],[host],
[connectionid],[queryid],[operation],[database],[object],[retcode]
```

| Item logged   | Description                                                                                                                                                                                                                                                                                                     |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| timestamp     | Time at which the event occurred. If syslog is used, the format is defined by syslogd.                                                                                                                                                                                                                          |
| syslog\_host  | Host from which the syslog entry was received.                                                                                                                                                                                                                                                                  |
| syslog\_ident | For identifying a system log entry, including the MariaDB server.                                                                                                                                                                                                                                               |
| syslog\_info  | For providing information for identifying a system log entry.                                                                                                                                                                                                                                                   |
| serverhost    | The MariaDB server host name.                                                                                                                                                                                                                                                                                   |
| username      | Connected user.                                                                                                                                                                                                                                                                                                 |
| host          | Host from which the user connected.                                                                                                                                                                                                                                                                             |
| connectionid  | Connection ID number for the related operation.                                                                                                                                                                                                                                                                 |
| queryid       | Query ID number, which can be used for finding the relational table events and related queries. For TABLE events, multiple lines will be added.                                                                                                                                                                 |
| operation     | Recorded action type: CONNECT, QUERY, READ, WRITE, CREATE, ALTER, RENAME, DROP.                                                                                                                                                                                                                                 |
| database      | Active database (as set by [USE](../../sql-statements/administrative-sql-statements/use-database.md)).                                                                                                                                                                                                          |
| object        | Executed query for QUERY events, or the table name in the case of TABLE events. From [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120), CONNECTION events also contain the tls version used, for example `TLSv1.3`. |
| retcode       | Return code of the logged operation.                                                                                                                                                                                                                                                                            |

Various events will result in different audit records. Some events will not return a value for some fields (e.g., when the active database is not set when connecting to the server).

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

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
