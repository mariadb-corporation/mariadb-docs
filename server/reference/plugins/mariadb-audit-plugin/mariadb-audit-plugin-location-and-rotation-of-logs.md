---
description: >-
  Manage your audit log files effectively. Learn how to define the log file
  path, set size limits, and configure rotation strategies to prevent log files
  from consuming all available disk space.
---

# Audit Plugin Location and Rotation of Logs

Logs can be written to a separate file or to the system logs. If you prefer to have the logging separated from other system information, the value of the variable [server\_audit\_output\_type](mariadb-audit-plugin-options-and-system-variables.md#server_audit_output_type) should be set to `file`. Incidentally, `file` is the only option on Windows systems.

You can force a rotation by enabling the [server\_audit\_file\_rotate\_now](mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_rotate_now) variable like so:

```sql
SET GLOBAL server_audit_file_rotate_now = ON;
```

### Separate log files

In addition to setting `server_audit_output_type`, you will have to provide the file path and name of the audit file. This is set in the variable [server\_audit\_file\_path](mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_path). You can set the file size limit of the log file with the variable [server\_audit\_file\_rotate\_size.](mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_rotate_size)

So, if rotation is on and the log file has reached the size limit you set, a copy is created with a consecutive number as extension the original file will be truncated to be used for the auditing again. To limit the number of log files created, set the variable [server\_audit\_file\_rotations.](mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_rotations) You can force log file rotation by setting the variable [server\_audit\_file\_rotate\_now](mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_rotate_now) to a value of `ON`. When the number of files permitted is reached, the oldest file will be overwritten. Here is how those variables might be set in a [server configuration file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[mysqld]
...
server_audit_file_rotate_now=ON 
server_audit_file_rotate_size=1000000 
server_audit_file_rotations=5
...
```

### System logs

For security reasons, it's better sometimes to use the system logs instead of a local file owned by the `mysql` user. To do this, the value of [server\_audit\_output\_type](mariadb-audit-plugin-options-and-system-variables.md#server_audit_output_type) needs to be set to `syslog`. Advanced configurations, such as using a remote `syslogd` service, are part of the `syslogd` configuration.

The variables,[ server\_audit\_syslog\_ident](mariadb-audit-plugin-options-and-system-variables.md#server_audit_syslog_ident) and [server\_audit\_syslog\_info](mariadb-audit-plugin-options-and-system-variables.md#server_audit_syslog_info) can be used to identify a system log entry made by the audit plugin. If a remote `syslogd` service is used for several MariaDB servers, these same variables are also used to identify the MariaDB server.

Here is a system log entry taken from a server which had [server\_audit\_syslog\_ident](mariadb-audit-plugin-options-and-system-variables.md#server_audit_syslog_ident) set to the default value of `mysql­-server_auditing`, and [server\_audit\_syslog\_info](mariadb-audit-plugin-options-and-system-variables.md#server_audit_syslog_info) set to `<prod1>`.

```sql
Aug 717:19:58localhostmysql-­server_auditing: 
<prod1> localhost.localdomain,root,localhost,1,7, 
QUERY, mysql, 'SELECT * FROM user',0
```

Although the default values for [server\_audit\_syslog\_facility](mariadb-audit-plugin-options-and-system-variables.md#server_audit_syslog_facility) and [server\_audit\_syslog\_priority](mariadb-audit-plugin-options-and-system-variables.md#server_audit_syslog_priority) should be sufficient in most cases. They can be changed based on the definition in `syslog.h` for the functions `openlog()` and `syslog()`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
