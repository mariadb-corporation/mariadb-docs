---
description: >-
  Monitor the performance and status of the Audit Plugin. View variables that
  track the number of logged events and current settings to ensure the auditing
  system is functioning correctly.
---

# Audit Plugin Status Variables

There are a few status variables related to the [MariaDB Audit Plugin](./), once it has been [installed](mariadb-audit-plugin-installation.md). These variables can be displayed using the [SHOW STATUS](../../sql-statements/administrative-sql-statements/show/show-status.md) statement like so:

```sql
SHOW STATUS LIKE 'server_audit%';

+----------------------------+------------------+
| Variable_name              | Value            |
+----------------------------+------------------+
| Server_audit_active        | ON               |
| Server_audit_current_log   | server_audit.log |
| Server_audit_last_error    |                  |
| Server_audit_writes_failed | 0                |
+----------------------------+------------------+
```

### Status Variables

Below is a list of all status variables related to the Audit Plugin. These cannot be set: These are not to be confused with system variables, which can be set. See [Server Status Variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md) for a complete list of status variables that can be viewed with the [SHOW STATUS](../../sql-statements/administrative-sql-statements/show/show-status.md) statement. See also the [Full list of MariaDB options, system and status variables](../../full-list-of-mariadb-options-system-and-status-variables.md).

#### `Server_audit_active`

* Description: If the auditing is actually working. It gets the ON value when the logging is successfully started. Then it can get the OFF value if the logging was stopped or log records can't be properly stored due to file or syslog errors.
* Data Type: `boolean`

#### `Server_audit_current_log`

* Description: The name of the logfile or the SYSLOG parameters that are in current use.
* Data Type: `string`

#### `Server_audit_last_error`

* Description: If something went wrong with the logging here you can see the message.
* Data Type: `string`

#### `Server_audit_writes_failed`

* Description: The number of log records since last logging-start that weren't properly stored because of errors of any kind. The global value can be flushed by [FLUSH STATUS](../../sql-statements/administrative-sql-statements/flush-commands/).
* Data Type: `numeric`
* Default Value: `0`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
