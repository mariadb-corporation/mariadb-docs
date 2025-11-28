---
description: >-
  Configure the Audit Plugin to suit your monitoring requirements. Learn how to
  enable logging, select specific event types to record, and exclude specific
  users from the audit trail.
---

# Audit Plugin Configuration

After the audit plugin has been installed and loaded, there will be some new global variables within MariaDB. These can be used to configure many components, limits, and methods related to auditing the server. You may set these variables related to the logs, such as their location, size limits, rotation parameters, and method of logging information. You may also set what information is logged, such connects, disconnects, and failed attempts to connect. You can also have the audit plugin log queries, read and write access to tables. So as not to overload your logs, the audit plugin can be configured based on lists of users. You can include or exclude the activities of specific users in the logs.

To see a list of [audit plugin-related variables](mariadb-audit-plugin-options-and-system-variables.md) on the server and their values, execute the follow while connected to the server:

{% tabs %}
{% tab title="Current" %}
```sql
SHOW GLOBAL VARIABLES LIKE 'server_audit%';
+-------------------------------+-----------------------+
| Variable_name                 | Value                 |
+-------------------------------+-----------------------+
| server_audit_events           |                       |
| server_audit_excl_users       |                       |
| server_audit_file_buffer_size | 0                     |
| server_audit_file_path        | server_audit.log      |
| server_audit_file_rotate_now  | OFF                   |
| server_audit_file_rotate_size | 1000000               |
| server_audit_file_rotations   | 9                     |
| server_audit_incl_users       |                       |
| server_audit_logging          | OFF                   |
| server_audit_mode             | 0                     |
| server_audit_output_type      | file                  |
| server_audit_query_log_limit  | 1024                  |
| server_audit_sync_log_file    | OFF                   |
| server_audit_syslog_facility  | LOG_USER              |
| server_audit_syslog_ident     | mysql-server_auditing |
| server_audit_syslog_info      |                       |
| server_audit_syslog_priority  | LOG_INFO              |
+-------------------------------+-----------------------+
17 rows in set (0.003 sec)
```
{% endtab %}

{% tab title="< 12.1" %}
```sql
SHOW GLOBAL VARIABLES LIKE 'server_audit%';

+-------------------------------+-----------------------+
| Variable_name                 | Value                 |
+-------------------------------+-----------------------+
| server_audit_events           | CONNECT,QUERY,TABLE   |
| server_audit_excl_users       |                       |
| server_audit_file_path        | server_audit.log      |
| server_audit_file_rotate_now  | OFF                   |
| server_audit_file_rotate_size | 1000000               |
| server_audit_file_rotations   | 9                     |
| server_audit_incl_users       |                       |
| server_audit_logging          | ON                    |
| server_audit_mode             | 0                     |
| server_audit_output_type      | file                  |
| server_audit_query_log_limit  | 1024                  |
| server_audit_syslog_facility  | LOG_USER              |
| server_audit_syslog_ident     | mysql-server_auditing |
| server_audit_syslog_info      |                       |
| server_audit_syslog_priority  | LOG_INFO              |
+-------------------------------+-----------------------+
```
{% endtab %}
{% endtabs %}

The values of these variables can be changed by an administrator with the `SUPER` privilege, using the [SET](../../sql-statements/administrative-sql-statements/set-commands/set.md) statement. Below is an example of how to disable audit logging:

```sql
SET GLOBAL server_audit_logging=OFF;
```

Although it is possible to change all of the variables shown above, some of them may be reset when the server restarts. Therefore, you may want set them in the configuration file (e.g., `/etc/my.cnf.d/server.cnf`) to ensure the values are the same after a restart:

```ini
[server]
... 
server_audit_logging=OFF 
…
```

For the reason given in the paragraph above, you would not generally set variables related to the auditing plugin using the `SET` statement. However, you might do so to test settings before making them more permanent. Since one cannot always restart the server, you would use the `SET` statement to change immediately the variables and then include the same settings in the configuration file so that the variables are set again as you prefer when the server is restarted.

#### Configuring Logs and Setting Other Variables

Of all of the server variables you can set, you may want to set initially the [server\_audit\_events](mariadb-audit-plugin-options-and-system-variables.md) variable to tell the Audit Plugin which events to log. The [Log Settings documentation page](mariadb-audit-plugin-log-settings.md) describes in detail the choices you have and provides examples of log entries related to them.

You can see a detailed list of system variables related to the MariaDB Audit Plugin on the [System Variables documentation page](mariadb-audit-plugin-options-and-system-variables.md). Status variables related to the Audit Plugin are listed and explained on the [Status Variables documentation page](mariadb-audit-plugin-status-variables.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
