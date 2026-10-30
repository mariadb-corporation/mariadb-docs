---
description: >-
  Verify and load the MariaDB Enterprise Audit plugin, start audit logging, forbid its uninstallation, and understand its server startup behavior.
---

# Enterprise Audit Installation and Setup

## Install the Audit Plugin

MariaDB Enterprise Audit comes preinstalled with MariaDB Enterprise Server, so no manual installation is required.

To verify that the plugin is installed:

1. Locate your server’s plugin directory.
   * When MariaDB Enterprise Server is running, you can find the directory by checking the value of the `plugin_dir` system variable.

```sql
SHOW GLOBAL VARIABLES
   LIKE 'plugin_dir';
```

```sql
+---------------+--------------------------+
| Variable_name | Value                    |
+---------------+--------------------------+
| plugin_dir    | /usr/lib64/mysql/plugin/ |
+---------------+--------------------------+
```

2. Verify the `server_audit2.so` file—the shared library used by MariaDB Enterprise Audit—is present in your server’s plugin directory.

```bash
$ ls -l /usr/lib64/mysql/plugin/server_audit2.so
```

```bash
-rwxr-xr-x. 1 root root 70432 Jul 15 19:03 /usr/lib64/mysql/plugin/server_audit2.so
```

MariaDB Enterprise Audit is bundled with all MariaDB Enterprise Server distributions (binary tarball, DEB/RPM package tarball, and DEB/RPM packages). If you do not see the `server_audit2.so` file, verify that MariaDB Enterprise Server has been installed correctly.

## Load the Audit Plugin

MariaDB Enterprise Audit is enabled through the `mariadb-enterprise.cnf` configuration file, which is included by default with MariaDB Enterprise Server. This means manual loading is usually not required.

The `mariadb-enterprise.cnf` file activates MariaDB Enterprise Audit by configuring the `plugin-load-add` and `server-audit` options.

```ini
# -- Auditing - pre-load Plugin
plugin-load-add=server_audit
server_audit=FORCE_PLUS_PERMANENT
```

If your environment does not use `mariadb-enterprise.cnf`, you can enable MariaDB Enterprise Audit by adding the same options to your own configuration file.

### Confirm the Audit Plugin is Loaded

To verify that MariaDB Enterprise Audit is installed, check the `information_schema.PLUGINS` table.

```sql
SELECT PLUGIN_STATUS, PLUGIN_LIBRARY, PLUGIN_DESCRIPTION, LOAD_OPTION
FROM information_schema.PLUGINS
WHERE PLUGIN_NAME='SERVER_AUDIT'\G
```

```sql
*************************** 1. row ***************************
     PLUGIN_STATUS: ACTIVE
    PLUGIN_LIBRARY: server_audit2.so
PLUGIN_DESCRIPTION: MariaDB Enterprise Audit
       LOAD_OPTION: FORCE_PLUS_PERMANENT
```

MariaDB Enterprise Audit is enabled through the `mariadb-enterprise.cnf` configuration file, which is included by default in MariaDB Enterprise Server. If your results differ from the example output above, verify that the `mariadb-enterprise.cnf` file specifies the `plugin-load-add` and `server-audit` options.

## Start Audit Logging

When MariaDB Enterprise Audit is installed and loaded, audit logging does not begin automatically. You must explicitly start it, either from the shell or through SQL.

<table><thead><tr><th width="111">Interface</th><th width="207">Method</th><th>Benefits</th></tr></thead><tbody><tr><td>Shell</td><td><a href="#start-audit-logging-in-configuration-file">Configuration File</a></td><td>SQL access is not required SUPER privilege is not required Configuration file can be version controlled.</td></tr><tr><td>SQL</td><td><a href="#start-audit-logging-with-set-global">SET GLOBAL Statement</a></td><td>Server restart is not required.</td></tr></tbody></table>

### Start Audit Logging in Configuration File

Enable audit logging with MariaDB Enterprise Audit by setting the `server_audit_logging` system variable in a configuration file. Alternatively, enable it dynamically with `SET GLOBAL`, which does not require a server restart.

To configure in a file:

1. Set the `server_audit_logging` system variable in the configuration file.

```ini
[mariadb]
server_audit_logging = ON
```

2. Restart MariaDB Enterprise Server:

```bash
$ sudo systemctl restart mariadb
```

If the server does not start, review the [error log](mariadb-enterprise-audit-error-log-messages.md) for details.

3. To confirm that audit logging is running, check the value of the `Server_audit_active` status variable using the `SHOW GLOBAL STATUS` statement.

```sql
SHOW GLOBAL STATUS
   LIKE 'Server_audit_active';
```

```sql
+---------------------+-------+
| Variable_name       | Value |
+---------------------+-------+
| Server_audit_active | ON    |
+---------------------+-------+
```

### Start Audit Logging with SET GLOBAL

Audit logging with MariaDB Enterprise Audit can be started by setting the [server\_audit\_logging](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_logging) system variable with the [SET GLOBAL](../../sql-statements/administrative-sql-statements/set-commands/set.md) statement, which requires the SUPER privilege.

1. Set the [server\_audit\_logging](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_logging) system variable with the [SET GLOBAL](../../sql-statements/administrative-sql-statements/set-commands/set.md) statement:

```sql
SET GLOBAL server_audit_logging=ON;
```

2. Confirm that audit logging is started by querying the [Server\_audit\_active](../mariadb-audit-plugin/mariadb-audit-plugin-status-variables.md#server_audit_active) status variable with the [SHOW GLOBAL STATUS](../../sql-statements/administrative-sql-statements/show/show-status.md) statement:

```sql
SHOW GLOBAL STATUS
   LIKE 'Server_audit_active';
```

```sql
+---------------------+-------+
| Variable_name       | Value |
+---------------------+-------+
| Server_audit_active | ON    |
+---------------------+-------+
```

When you modify a system variable dynamically using the `SET GLOBAL` statement, the change is not preserved after a server restart. To ensure audit logging automatically starts with the server, also configure the `server_audit_logging` system variable in a configuration file.

```ini
[mariadb]
server_audit_logging = ON
```

### Confirm Audit Logging is Started

Confirm that audit logging is started by querying the [Server\_audit\_active](../mariadb-audit-plugin/mariadb-audit-plugin-status-variables.md#server_audit_active) status variable with the [SHOW GLOBAL STATUS](../../sql-statements/administrative-sql-statements/show/show-status.md) statement:

```sql
SHOW GLOBAL STATUS
   LIKE 'Server_audit_active';
```

```sql
+---------------------+-------+
| Variable_name       | Value |
+---------------------+-------+
| Server_audit_active | ON    |
+---------------------+-------+
```

### Audit Logging Buffer Writes

{% hint style="info" %}
Buffer writes are available from MariaDB Enterprise Server 11.8.
{% endhint %}

Audit log buffering is controlled by these variables:

* `server_audit_file_buffer_size` — This defines the size of the buffer. The default value is `0`, meaning there's no buffering at all. Setting non-zero value enables the buffering with the buffer of the specified size aligned by `8192`. The maximum value is `65536`.
* `server_audit_sync_log_file` — This flushes the buffer to the log file. While the log record is in the buffer, it cannot be seen in the log file. If there aren't many events to log, the time before records can be observed can be significant. You can issue this statement to force writing the buffer to the file, making sure not to miss recent records:

```sql
SET GLOBAL server_audit_sync_log_file=1;
```

## Forbid Uninstallation

In a secure environment, MariaDB Enterprise Audit provides administrators with an audit trail of actions performed by users on the MariaDB Enterprise Server node. To protect the integrity of the audit trail, users should not be able to uninstall MariaDB Enterprise Audit. If the server-audit option is set to `FORCE_PLUS_PERMANENT`, MariaDB Enterprise Server will prevent MariaDB Enterprise Audit from being uninstalled:

```ini
server_audit=FORCE_PLUS_PERMANENT
```

When a user tries to uninstall MariaDB Enterprise Audit with the server-audit option set to `FORCE_PLUS_PERMANENT`, the operation fails with the `ER_PLUGIN_IS_PERMANENT` error code:

```sql
UNINSTALL SONAME 'server_audit2';
```

```sql
ERROR 1702 (HY000): Plugin 'SERVER_AUDIT' is force_plus_permanent and can not be unloaded
```

{% hint style="info" %}
The `mariadb-enterprise.cnf` configuration file included by default in MariaDB Enterprise Server sets the server-audit option to `FORCE_PLUS_PERMANENT`. As a consequence, MariaDB Enterprise Server forbids MariaDB Enterprise Audit from being uninstalled by default.
{% endhint %}

If you do not use `mariadb-enterprise.cnf` in your environment, you can configure MariaDB Enterprise Audit to forbid uninstallation by setting the server-audit option in your configuration file.

### Confirm that Uninstallation is Forbidden

To confirm that MariaDB Enterprise Audit is configured to forbid uninstallation, query the [information\_schema.PLUGINS](../../system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md) table:

```sql
SELECT PLUGIN_STATUS, PLUGIN_LIBRARY, PLUGIN_DESCRIPTION, LOAD_OPTION
FROM information_schema.PLUGINS
WHERE PLUGIN_NAME='SERVER_AUDIT'\G
```

```sql
*************************** 1. row ***************************
     PLUGIN_STATUS: ACTIVE
    PLUGIN_LIBRARY: server_audit2.so
PLUGIN_DESCRIPTION: MariaDB Enterprise Audit
       LOAD_OPTION: FORCE_PLUS_PERMANENT
```

If your output does not match the example output shown above, confirm that the `mariadb-enterprise.cnf` configuration file sets the server-audit option to `FORCE_PLUS_PERMANENT`.

## Server Startup Behavior

Some specific server startup behavior is described in the sections below.

For examples of error messages that can appear in the MariaDB error log during server startup, see [Messages in MariaDB Error Log](mariadb-enterprise-audit-error-log-messages.md).

### Enterprise Audit Not Loaded

MariaDB Enterprise Server can startup and handle traffic even if MariaDB Enterprise Audit is not installed or loaded. However, the specific behavior can be configured.

When the server-audit option is set to `FORCE` or `FORCE_PLUS_PERMANENT`, MariaDB Enterprise Server will fail to start if MariaDB Enterprise Audit can't be loaded.

The mariadb-enterprise.cnf configuration file included by default in MariaDB Enterprise Server sets the server-audit option to `FORCE_PLUS_PERMANENT`. As a consequence, MariaDB Enterprise Server forbids MariaDB Enterprise Audit from being uninstalled by default.

### Invalid Filter Definitions

MariaDB Enterprise Audit attempts to load the [Audit Filters](mariadb-enterprise-audit-filters.md) during startup.

When MariaDB Enterprise Audit encounters errors in the Audit Filter definitions, MariaDB Enterprise Server will still start and load MariaDB Enterprise Audit. In this situation, an error will be written to the MariaDB error log and all Events for all objects will be audit logged.

## Additional Points of Control

When enabled, MariaDB Enterprise Audit logs designated Events that occur on a running instance of MariaDB Enterprise Server.

Additional audit practices should be established to cover:

* Data backup controls.
* System-level controls, including authentication, file system, and process execution.
* Network-level controls.
* Monitoring systems, including [monitoring for audit logging](#confirm-audit-logging-is-started).
* Changes to user accounts (and the [mysql.global\_priv](../../system-tables/the-mysql-database-tables/mysql-global_priv-table.md) system table), which can necessitate changes to Audit Filters.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
