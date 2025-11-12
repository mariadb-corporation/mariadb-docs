# MariaDB Enterprise Audit

## Overview

While application design specifications and database configurations may intend specific limitations to be placed around access to data, audit mechanisms help confirm the effectiveness of these controls.

MariaDB Enterprise Audit is a plugin that logs data access and database operations.

Audit mechanisms are most effective when they produce a manageable quantity of output. MariaDB Enterprise Audit includes advanced filtering features to enable narrowly defining which information is logged.

Where audit mechanisms may only be effective when control parameters can also be audited, MariaDB Enterprise Audit implements logging of configuration changes.

{% hint style="danger" %}
**Plugin Conflict (**[MENT-316](https://jira.mariadb.org/browse/MENT-316)**)**

The MariaDB Enterprise Audit plugin (`server_audit2.so`) is incompatible with the older server\_audit.so (`v1`) plugin. Running both can cause server instability or deadlocks.

_If you are a new user: You can continue reading._

_If you are migrating: You must remove the old `v1` plugin. Please go directly to the_ [_Upgrades_](mariadb-enterprise-audit.md#upgrades) _section for complete instructions._
{% endhint %}

## Configuration Overview

MariaDB Enterprise Audit is installed and loaded by default. If you are unsure whether it is loaded on your system, you can [confirm that the plugin is loaded](mariadb-enterprise-audit.md#confirm-the-audit-plugin-is-loaded).

To use MariaDB Enterprise Audit, the plugin must be configured:

* Administrators must define [Audit Filters](mariadb-enterprise-audit.md#audit-filters) to configure what MariaDB Enterprise Audit writes to the audit log.\
  MariaDB Enterprise Audit supports two types of Audit Filters:

| Audit Filter Type                                                        | Used For                                                                                         |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| [Default Audit Filter](mariadb-enterprise-audit.md#default-audit-filter) | The Default Audit Filter is used for any user account that is not assigned a Named Audit Filter. |
| [Named Audit Filters](mariadb-enterprise-audit.md#named-audit-filters)   | Named Audit Filters are assigned to specific user accounts.                                      |

Administrators can define Audit Filters to audit log activity using multiple types of filters:

| Filter Type                                                   | Used For                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Event Filters](mariadb-enterprise-audit.md#event-filters)    | Event Filters are used to enable or disable audit logging for specific types of operations performed by the user accounts assigned to the Audit Filter.                                                                                                                                                      |
| [Logging Filters](mariadb-enterprise-audit.md#logging-filter) | Logging Filters are used to enable or disable audit logging for the user accounts assigned to the Audit Filter.                                                                                                                                                                                              |
| [Object Filters](mariadb-enterprise-audit.md#object-filters)  | Object Filters are used to enable or disable audit logging for specific databases or tables accessed by the user accounts assigned to the Audit Filter. Support for Object Filters was added in MariaDB Enterprise Server 10.6. Support for Object Filters was backported to ES 10.4.21-13 and ES 10.5.12-8. |

Administrators must [start audit logging](mariadb-enterprise-audit.md#start-audit-logging).

## General Operation

MariaDB Enterprise Audit performs audit logging during typical operations of MariaDB Enterprise Server:

* When a user connects, fails to connect, or disconnects, MariaDB Enterprise Audit will write a message to the audit log if the Audit Filter specifies the specific type of [Connect Event](mariadb-enterprise-audit.md#connection-events).
* When a user executes a query, MariaDB Enterprise Audit will write a message to the audit log if the Audit Filter specifies the specific type of [Query Event](mariadb-enterprise-audit.md#query-events) and if the queried objects are not excluded by [Object Filters](mariadb-enterprise-audit.md#object-filters).
* When a query accesses a table, MariaDB Enterprise Audit will write a message to the audit log if the Audit Filter specifies the specific type of Table Event and if the table is not excluded by [Object Filters](mariadb-enterprise-audit.md#object-filters).
* When a query modifies the MariaDB Enterprise Audit configuration, MariaDB Enterprise Audit will write a message to the audit log if the Audit Filter specifies the [Audit Config Event](mariadb-enterprise-audit.md#audit-config-events).
* When a user's [Audit Filter](mariadb-enterprise-audit.md#logging-filter) contains a Logging Filter that disables audit logging, all audit logging for the user's activity will be skipped.

MariaDB Enterprise Audit writes audit log messages either to a dedicated [audit log file or to the system log (syslog)](mariadb-enterprise-audit.md#audit-log-destinations), depending on configuration.

Audit log messages that correspond to a query are logged when the query completes. If a query is executed in a transaction, the audit log messages that correspond to the query are logged when the individual query completes, not when the transaction completes. If the query fails, the audit log message is logged at time of failure.

## Audit Log Considerations

Care must be taken when logging data for audit to maintain alignment to business requirements. Concerns include:

* Queries should not be logged for tables containing Personally Identifiable Information (PII) or Sensitive PII (SPII) such as passwords, since audit log data is written unencrypted. Consider using [Object Filters](mariadb-enterprise-audit.md#object-filters) to exclude sensitive information from the audit log.
* Backup of audit data should be performed at least as frequently as database backups.
* Audit log data on database servers could be tampered with if the database server is compromised. Consider secure transmission of log data to a hardened and remote logging server.
* Where audit data is mission-critical, it should be subject to controls, data protection, data retention, and highly-available storage as are used for other mission-critical data.

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

\
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

<table><thead><tr><th width="111">Interface</th><th width="207">Method</th><th>Benefits</th></tr></thead><tbody><tr><td>Shell</td><td><a href="mariadb-enterprise-audit.md#start-audit-logging-in-configuration-file">Configuration File</a></td><td>SQL access is not required SUPER privilege is not required Configuration file can be version controlled.</td></tr><tr><td>SQL</td><td><a href="mariadb-enterprise-audit.md#start-audit-logging-with-set-global">SET GLOBAL Statement</a></td><td>Server restart is not required.</td></tr></tbody></table>

### Start Audit Logging in Configuration File

enable audit logging with MariaDB Enterprise Audit by setting the `server_audit_logging` system variable in a configuration file.\
Alternatively, you can enable it dynamically with `SET GLOBAL`, which does not require a server restart.

To configure in a file:\
1\. Set the `server_audit_logging` system variable in the configuration file.

```ini
[mariadb]
server_audit_logging = ON
```

2. Restart MariaDB Enterprise Server:

```bash
$ sudo systemctl restart mariadb
```

If the server does not start, review the [error log](mariadb-enterprise-audit.md#messages-in-mariadb-error-log) for details.

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

Audit logging with MariaDB Enterprise Audit can be started by setting the [server\_audit\_logging](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_logging) system variable with the [SET GLOBAL](../sql-statements/administrative-sql-statements/set-commands/set.md) statement, which requires the SUPER privilege.

1. Set the [server\_audit\_logging](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_logging) system variable with the [SET GLOBAL](../sql-statements/administrative-sql-statements/set-commands/set.md) statement:

```sql
SET GLOBAL server_audit_logging=ON;
```

2. Confirm that audit logging is started by querying the [Server\_audit\_active](mariadb-audit-plugin/mariadb-audit-plugin-status-variables.md#server_audit_active) status variable with the [SHOW GLOBAL STATUS](../sql-statements/administrative-sql-statements/show/show-status.md) statement:

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

Confirm that audit logging is started by querying the [Server\_audit\_active](mariadb-audit-plugin/mariadb-audit-plugin-status-variables.md#server_audit_active) status variable with the [SHOW GLOBAL STATUS](../sql-statements/administrative-sql-statements/show/show-status.md) statement:

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
SET GLOBAL server_audit_log_file=1
```

## Forbid Uninstallation

In a secure environment, MariaDB Enterprise Audit provides administrators with an audit trail of actions performed by users on the MariaDB Enterprise Server node. To protect the integrity of the audit trail, users should not be able to uninstall MariaDB Enterprise Audit. If the server-audit option is set to `FORCE_PLUS_PERMANENT`, MariaDB Enterprise Server will prevent MariaDB Enterprise Audit from being uninstalled:

```ini
server_audit=FORCE_PLUS_PERMANENT
```

When a user tries to uninstall MariaDB Enterprise Audit with the server-audit option set to FORCE\_PLUS\_PERMANENT, the operation fails with the ER\_PLUGIN\_IS\_PERMANENT error code:

```sql
UNINSTALL SONAME 'server_audit2';
```

```sql
ERROR 1702 (HY000): Plugin 'SERVER_AUDIT' is force_plus_permanent and can not be unloaded
```

{% hint style="info" %}
The `mariadb-enterprise.cnf` configuration file included by default in MariaDB Enterprise Server sets the server-audit option to `FORCE_PLUS_PERMANENT`. As a consequence, MariaDB Enterprise Server forbids MariaDB Enterprise Audit from being uninstalled by default.
{% endhint %}

If you do not use mariadb-enterprise.cnf in your environment, you can configure MariaDB Enterprise Audit to forbid uninstallation by setting the server-audit option in your configuration file.

### Confirm that Uninstallation is Forbidden

To confirm that MariaDB Enterprise Audit is configured to forbid uninstallation, query the [information\_schema.PLUGINS](../system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md) table:

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

For examples of error messages that can appear in the MariaDB error log during server startup, see [Messages in MariaDB Error Log](mariadb-enterprise-audit.md#messages-in-mariadb-error-log).

### Enterprise Audit Not Loaded

MariaDB Enterprise Server can startup and handle traffic even if MariaDB Enterprise Audit is not installed or loaded. However, the specific behavior can be configured.

When the server-audit option is set to `FORCE` or `FORCE_PLUS_PERMANENT`, MariaDB Enterprise Server will fail to start if MariaDB Enterprise Audit can't be loaded.

The mariadb-enterprise.cnf configuration file included by default in MariaDB Enterprise Server sets the server-audit option to `FORCE_PLUS_PERMANENT`. As a consequence, MariaDB Enterprise Server forbids MariaDB Enterprise Audit from being uninstalled by default.

### Invalid Filter Definitions

MariaDB Enterprise Audit attempts to load the [Audit Filters](mariadb-enterprise-audit.md#audit-filters) during startup.

When MariaDB Enterprise Audit encounters errors in the Audit Filter definitions, MariaDB Enterprise Server will still start and load MariaDB Enterprise Audit. In this situation, an error will be written to the MariaDB error log and all Events for all objects will be audit logged.

## Additional Points of Control

When enabled, MariaDB Enterprise Audit logs designated Events that occur on a running instance of MariaDB Enterprise Server.

Additional audit practices should be established to cover:

* Data backup controls.
* System-level controls, including authentication, file system, and process execution.
* Network-level controls.
* Monitoring systems, including [monitoring for audit logging](mariadb-enterprise-audit.md#confirm-audit-logging-is-started).
* Changes to user accounts (and the [mysql.global\_priv](../system-tables/the-mysql-database-tables/mysql-global_priv-table.md) system table), which can necessitate changes to Audit Filters.

## Audit Filters

Filters are JSON objects that specify what you want MariaDB Enterprise Audit to monitor.

There are two types of filters:

| Audit Filter Type                                                        | Description                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Default Audit Filter](mariadb-enterprise-audit.md#default-audit-filter) | The Default Audit Filter is used for all user accounts that are not assigned a Named Audit Filter. Only a single Default Audit Filter can be defined in the mysql.server\_audit\_filters system table, and it must be defined with the name default.                                                                                                                     |
| [Named Audit Filters](mariadb-enterprise-audit.md#named-audit-filters)   | Named Audit Filters must be assigned to specific user accounts. Many Named Audit Filters can be defined in the mysql.server\_audit\_filters system table, and they must be defined with unique names. A Named Audit Filter can be assigned to a user account by inserting the user account details and the filter name into the mysql.server\_audit\_users system table. |

## Default Audit Filter

The Default Audit Filter applies to all user accounts that do not have a specific Named Audit Filter assigned. Only one Default Audit Filter is allowed in the `mysql.server_audit_filters` system table, and it must be named `default`.

### Create a Default Audit Filter

If you want to create a Default Audit Filter, you need to insert the details into the `mysql.server_audit_filters` system table. The name for the Default Audit Filter must be default and the rule should be designed to meet your audit logging requirements.

To create a Default Audit Filter:

1. Confirm that a Default Audit Filter does not already exist:

```sql
SELECT * FROM mysql.server_audit_filters
    WHERE filtername = 'default';
```

2. If a Default Audit Filter already exists, remove it:

```sql
DELETE FROM mysql.server_audit_filters
    WHERE filtername = 'default';
```

3. Insert the details for the new Default Audit Filter into the mysql.server\_audit\_filters system table:

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES ('default',
      JSON_COMPACT(
         '{
            "connect_event":"ALL",
            "table_event":"WRITE"
         }'
      ));
```

This example Audit Filter configures audit logging for all Connection Events and Write Table Events.

The example passes the JSON object to the [JSON\_COMPACT()](../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.

4. Reload the Audit Filters by setting the server\_audit\_reload\_filters system variable to `ON`:

```sql
SET GLOBAL server_audit_reload_filters=ON;
```

### Disable Logging with the Default Filter

It is recommended to use the default filter to assure that any user is audited, also if not defined in the `mysql.server_audit_users` system table.

In some special cases you might want audits only to be enabled for the users in `mysql.server_audit_users`. In this case you should use the following default filter to disable logging for all other users.

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES (‘default’,
      JSON_COMPACT(
         ‘{
    “logging”: “OFF”
            }’
      ));
```

## Named Audit Filters

Named Audit Filters must be assigned to specific user accounts.

Multiple Named Audit Filters can be defined in the mysql.server\_audit\_filters system table, and they must be defined with unique names. A Named Audit Filter can be assigned to a user account by inserting the user account details and the filter name into the mysql.server\_audit\_users system table.

### Create a Named Audit Filter

To create a Named Audit Filter, insert a row with the Audit Filter's name and the rule into the `mysql.server_audit_filters` system table:

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES ('reporting',
      JSON_COMPACT(
         '{
            "connect_event": [
               "CONNECT",
               "DISCONNECT"
            ],
            "table_event":[
               "WRITE",
               "CREATE",
               "DROP",
               "RENAME",
               "ALTER"
            ]
         }'
      ));
```

This example Audit Filter is defined with the name reporting, and it configures audit logging for Connection Events and Disconnection Events and for several types of Table Events. This example Audit Filter can be useful for read-only users since it does not log table reads, but it does log table writes and schema changes which are illegitimate activities for a read-only user.

The example passes the JSON object to the `JSON_COMPACT`() function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.

For additional information on how to assign the Audit Filter to a user account, see "[Assign a Named Audit Filter](mariadb-enterprise-audit.md#assign-a-named-audit-filter)".

### Assign a Named Audit Filter

Named Audit Filters are only active when they are assigned to a specific user account.

To assign a Named Audit Filter to a user account:

1. Insert a row with the user account details and the Audit Filter's name into the `mysql.server_audit_users` system table:

```sql
INSERT INTO mysql.server_audit_users (host, user, filtername)
   VALUES ("%", "reader", "reporting");
```

This example statement assigns the reporting Audit Filter created in "[Create a Named Audit Filter](mariadb-enterprise-audit.md#create-a-named-audit-filter)" to the `reader@%` user account.

2. Reload the Audit Filters by setting the server\_audit\_reload\_filters system variable to `ON`:

```sql
SET GLOBAL server_audit_reload_filters=ON;
```

MariaDB Enterprise Audit does not track changes to user accounts. If you delete or rename a user account, the change doesn't cascade to the Audit Filter. The Audit Filters must be updated manually.

## System Tables for Audit Filters

There are two system tables for Audit Filters:

<table><thead><tr><th width="247">System Table</th><th>Description</th></tr></thead><tbody><tr><td>mysql.server_audit_filters</td><td>Audit Filter definitions with MariaDB Enterprise Audit</td></tr><tr><td>mysql.server_audit_users</td><td>Audit Filter assignments for user accounts with MariaDB Enterprise Audit.</td></tr></tbody></table>

### Query Audit Filters

You can query Audit Filters by querying the `mysql.server_audit_filters` system table.

The JSON objects can be made more human-readable by passing them to the [JSON\_DETAILED()](../sql-functions/special-functions/json-functions/json_detailed.md) or [JSON\_LOOSE()](../sql-functions/special-functions/json-functions/json_loose.md) functions:

```sql
SELECT filtername,
   JSON_DETAILED(rule)
FROM mysql.server_audit_filters\G
```

```json
*************************** 1. row ***************************
         filtername: reporting
JSON_DETAILED(rule): {
    "table_event":
    [
        "WRITE",
        "CREATE",
        "DROP",
        "RENAME",
        "ALTER",

        {
            "log_databases":
            [
                "production",
                "reporting"
            ]
        }
    ]
}
```

### Query User Assignments for Named Audit Filters

You can query user assignments for Named Audit Filters by joining the `mysql.server_audit_filters` and `mysql.server_audit_users` system tables.

The JSON objects can be made more human-readable by passing them to the [JSON\_DETAILED()](../sql-functions/special-functions/json-functions/json_detailed.md) or [JSON\_LOOSE()](../sql-functions/special-functions/json-functions/json_loose.md) functions:

```sql
SELECT sau.host, sau.user, saf.filtername,
   JSON_DETAILED(saf.rule)
FROM mysql.server_audit_filters saf
JOIN mysql.server_audit_users sau
   ON saf.filtername = sau.filtername
WHERE saf.filtername != 'default'\G
```

```json
*************************** 1. row ***************************
                   host: %
                   user: reader
             filtername: reporting
JSON_DETAILED(saf.rule): {
    "table_event":
    [
        "WRITE",
        "CREATE",
        "DROP",
        "RENAME",
        "ALTER",

        {
            "log_databases":
            [
                "production",
                "reporting"
            ]
        }
    ]
}
*************************** 2. row ***************************
                   host: %
                   user: writer
             filtername: reporting
JSON_DETAILED(saf.rule): {
    "table_event":
    [
        "WRITE",
        "CREATE",
        "DROP",
        "RENAME",
        "ALTER",

        {
            "log_databases":
            [
                "production",
                "reporting"
            ]
        }
    ]
}
```

### Reload Audit Filters and Assignments

MariaDB Enterprise Audit caches its Audit Filters to improve performance. When you change an Audit Filter or an Audit Filter assignment in the system tables, you need to reload the Audit Filters for the changes to take effect.

To reload Audit Filters, set the server\_audit\_reload\_filters system variable to ON with the [SET GLOBAL](../sql-statements/administrative-sql-statements/set-commands/set.md) statement, which requires the SUPER privilege:

```sql
SET GLOBAL server_audit_reload_filters=ON;
```

When you set the server\_audit\_reload\_filters system variable to ON, MariaDB Enterprise Audit reloads all Audit Filters and assignments to ensure that it is using the latest definitions. Afterward, it sets `server_audit_reload_filters` back to `OFF`.

For additional information on how to use the server\_audit\_reload\_filters system variable, see "[Default Audit Filter](mariadb-enterprise-audit.md#default-audit-filter)" and "[Named Audit Filters](mariadb-enterprise-audit.md#named-audit-filters)".

## Event Filters

MariaDB Enterprise Audit supports Event Filters in Audit Filters. Event Filters can be used to configure which Events you want to audit. Each Event refers to a different class of operation.

MariaDB Enterprise Audit defines multiple Event classes that can be used in Event Filters:

* [Audit Config Events](mariadb-enterprise-audit.md#audit-config-events)
* [Connect Events](mariadb-enterprise-audit.md#connection-events)
* [Query Events](mariadb-enterprise-audit.md#query-events)
* [Table Events](mariadb-enterprise-audit.md#table-events)

The Event classes are described in the sections below. Example audit logs for each Event class are shown in the sections below. For details about the audit log format, see [Audit Log Format](mariadb-enterprise-audit.md#audit-log-format).

### Audit Config Events

MariaDB Enterprise Audit implements Audit Config Events to help keep track of changes to the audit log configuration.

MariaDB Enterprise Audit logs Audit Config (AUDIT\_CONFIG) Events in the following situations:

* When one of MariaDB Enterprise Audit's system variables is changed with the [SET GLOBAL](../sql-statements/administrative-sql-statements/set-commands/set.md) statement, the change is logged.
* When the audit log file is rotated, it is logged.

In the following output, three audit configuration events (`AUDIT_CONFIG`) and one query event (`QUERY`) are shown:

```
20190622 02:10:21,localhost.localdomain,,,0,0,AUDIT_CONFIG,,file_path=server_audit.log,0
20190622 02:10:21,localhost.localdomain,,,0,0,AUDIT_CONFIG,,rotate_size=1000000,0
20190622 02:10:21,localhost.localdomain,,,0,0,AUDIT_CONFIG,,file_rotations=9,0
20190622 02:10:21,localhost.localdomain,root,localhost,8,7,QUERY,mysql,'set global server_audit_logging = on',0
```

{% hint style="success" %}
`AUDIT_CONFIG` events are always logged, so no configuration is required when [audit logging](mariadb-enterprise-audit.md#start-audit-logging) is started.
{% endhint %}

### Connection Events

MariaDB Enterprise Audit implements Connection Events to audit connection attempts, authentication failures, and user account changes that occur due to certain authentication plugins, such as pam.

MariaDB Enterprise Audit logs Connection Events in the following situations:

* When a user successfully connects, it is logged with the `CONNECT` Event sub-class.
* When a user disconnects, it is logged with the `DISCONNECT` Event sub-class.
* When a user fails to connect, it is logged with the `FAILED_CONNECT` Event sub-class.
* When an existing connection authenticates as a different user, it is logged with the `CHANGE_USER` Event sub-class.
* When an authentication plugin changes to a proxy user, it is logged with the `PROXY_CONNECT` Event sub-class.

In the following output, multiple sub-classes of connection events (`CONNECT`, `DISCONNECT`, `FAILED_CONNECT`) are shown:

```sql
20190710 00:05:30,localhost.localdomain,root, localhost,2,0,CONNECT,,,0
20190710 00:05:53,localhost.localdomain,root, localhost,2,0,DISCONNECT,,,0
20190710 00:06:28,localhost.localdomain,unknownuser,localhost,3,0,FAILED_CONNECT,,,1045
20190710 00:06:28,localhost.localdomain,unknownuser, localhost,3,0,DISCONNECT,,,0
```

An **event filter for connection events** can be added to an Audit filter with the `connect_event` key, which supports the following values:

| Value           | Description                                                                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| CONNECT         | Records when the user connects to MariaDB Enterprise Server                                                                                    |
| DISCONNECT      | Records when the user disconnects from MariaDB Enterprise Server                                                                               |
| FAILED\_CONNECT | Records when a user attempts to connect to MariaDB Enterprise Server, but the connection attempt fails due to authentication or similar issues |
| CHANGE\_USER    | Records when a user switches to a different user account                                                                                       |
| PROXY\_CONNECT  | Records proxy user connections. This Connection Event sub-class was added in ES10.4.17-10 and ES10.5.8-5.                                      |
| ALL             | Records all connection Events                                                                                                                  |

This query defines a [Named Audit Filter](mariadb-enterprise-audit.md#named-audit-filters) that specifies connection events:

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES ('connections',
      JSON_COMPACT(
         '{
            "connect_event": [
               "CONNECT",
               "DISCONNECT"
            ]
         }'
      ));
```

The example passes the JSON object to the [JSON\_COMPACT()](../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.

### Query Events

MariaDB Enterprise Audit implements Query Events to audit the execution of a specific subset of SQL statements.

MariaDB Enterprise Audit logs Query Events in the following situations:

* When a SQL statement is directly executed, it is logged with the `QUERY` event.

MariaDB Enterprise Audit does not log query events for SQL statements that are indirectly executed. For example, if an SQL statement is executed as part of a view, stored procedure, stored function, or trigger, the query will not be logged. If you want to audit all table accesses, including indirect table accesses, it is recommended to enable audit logging for [Table Events](mariadb-enterprise-audit.md#table-events) in addition to query events.

This query shows one query event:

```sql
20190710 02:21:07,localhost.localdomain,John,localhost,3,30,QUERY,db1,'SELECT * FROM services WHERE typeid IN (SELECT id FROM services_types WHERE name="consulting")',0
```

An **event filter for query events** can be added to an Audit Filter with the `query_event` key, which supports the following values:

| Value           | Description                                                                                                                                               |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DML             | Records any SQL statements in the Data Manipulation Language subset, including SELECT, INSERT, UPDATE, and DELETE statements.                             |
| DDL             | Records any SQL statements in the Data Definition Language subset, including CREATE TABLE and ALTER TABLE, as well as DROP TABLE and TRUNCATE operations. |
| DCL             | Records any SQL statements in the Data Control Language subset, including GRANT and REVOKE.                                                               |
| DML\_READ       | Records SELECT statements in the Data Manipulation Language subset.                                                                                       |
| DML\_WRITE      | Records any SQL statements for writes in the Data Manipulation Language subset, including INSERT, UPDATE, and DELETE statements.                          |
| DML\_NO\_SELECT | Alias for DML\_WRITE                                                                                                                                      |
| ALL             | Records any SQL statements run by the user.                                                                                                               |

For example, the following query defines a [Named Audit Filter](mariadb-enterprise-audit.md#named-audit-filters) that specifies Query Events:

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES (
       'queries',
       JSON_COMPACT(
          '{
              "query_event": [
                  "DML",
                  "DDL",
		  "DCL",
		  "DML_NO_SELECT",
		  "DML_WRITE",
		  "DML_READ",
		  "ALL"
              ]
          }'
       )
    );
```

The example passes the JSON object to the [JSON\_COMPACT()](../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.

{% tabs %}
{% tab title="Current" %}
MariaDB Enterprise Audit supports [Object Filters](mariadb-enterprise-audit.md#object-filters) for Query Events.
{% endtab %}

{% tab title="< 10.6 / 10.5.12 / 10.4.21" %}
MariaDB Enterprise Audit does **not** support [Object Filters](mariadb-enterprise-audit.md#object-filters) for Query Events.
{% endtab %}
{% endtabs %}

### Table Events

MariaDB Enterprise Audit implements Table Events to audit when a table is accessed or modified.

MariaDB Enterprise Audit logs Table Events in the following situations:

* When an operation reads from a table, it is logged with the `READ` Event sub-class.
* When an operation writes to a table, it is logged with the `WRITE` Event sub-class.
* When an operation creates a table, it is logged with the `CREATE` Event sub-class.
* When an operation drops a table, it is logged with the `DROP` Event sub-class.
* When an operation alters a table, it is logged with the `ALTER` Event sub-class.
* When an operation renames a table, it is logged with the `RENAME` Event sub-class.

Table Events are logged when a table is accessed or modified directly or indirectly by a query. They complement Query Events very well, because the [Query Event](mariadb-enterprise-audit.md#query-events) causes the raw query to be audit logged, and the Table Event causes all table operations to be audit logged. Both Query Events and Table Events are logged with the query ID, so each Table Event can easily be mapped to its corresponding Query Event. The combination of Query Events and Table Events can be useful when table operations can be hidden by views or triggers.

In the following example output, 6 sub-classes of Table Events are shown:

```sql
20190710 02:21:06,localhost.localdomain,John,localhost,3,25,CREATE,db1,services,
20190710 02:21:06,localhost.localdomain,John,localhost,3,27,READ,db1,services,
20190710 02:21:07,localhost.localdomain,John,localhost,3,29,WRITE,db1,services,
20190710 02:21:27,localhost.localdomain,John,localhost,3,35,ALTER,db1,services,
20190710 02:21:27,localhost.localdomain,John,localhost,3,36,RENAME,db1,services,db1,services_new
20190710 02:21:45,localhost.localdomain,John,localhost,3,38,DROP,db1,services_new,
```

When a query uses the `DELAYED` keyword, it is executed by a system user. In this case, any Table Event associated with the query is written to the audit log with the user set to `DELAYED`. However, the Query Event associated with the query is written to the audit log with the original user:

```sql
20190622 02:10:21,localhost.localdomain,root,localhost,8,5,QUERY,test,'INSERT DELAYED INTO t1 VALUES(1),(2),(3);',0
20190622 02:10:25,localhost.localdomain,root,localhost,2,2,WRITE,test,t1,
20190622 02:10:25,localhost,DELAYED,localhost,2,2,WRITE,test,t1,
```

When your application executes queries with the `DELAYED` keyword, it is recommended to enable audit logging for Query Events in addition to Table Events to ensure that the full details are logged.

If the query cache is enabled, `READ` Table Events may not be audit logged. If MariaDB Enterprise Audit detects that the query cache is enabled during startup, MariaDB Enterprise Audit writes the following message to the MariaDB error log:

```sql
2021-07-23  0:11:26 server_audit: Query cache is enabled with the TABLE events. Some table reads can be veiled.
```

An Event Filter for Table Events can be added to an Audit Filter with the `table_event` key, which supports the following values:

| Value  | Description                                                                                             |
| ------ | ------------------------------------------------------------------------------------------------------- |
| READ   | Records read operations run on table objects, such as from a `SELECT` statement or an `INSERT SELECT`   |
| WRITE  | Records write operations run on table objects, such as `INSERT` or `UPDATE` statements                  |
| CREATE | Records any creation operations run on table objects, such as from a `CREATE TABLE` or `CREATE SERVER`. |
| DROP   | Records any deletion operations run on table objects, such as `DELETE` or `DROP TABLE`.                 |
| ALTER  | Records any modifications made on table objects, such as `ALTER TABLE` or `ALTER USER`.                 |
| RENAME | Records any renaming operations run on table objects, such as `RENAME TABLE`                            |
| ALL    | Records all operations run on table objects                                                             |

For example, the following query defines a [Named Audit Filter](mariadb-enterprise-audit.md#named-audit-filters) that specifies Table Events:

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES (
       'tables',
       JSON_COMPACT(
           '{
              "table_event": [
                  "WRITE",
                  "CREATE",
                  "DROP",
                  "RENAME",
                  "ALTER"
              ]
           }'
       )
    );
```

The example passes the JSON object to the [JSON\_COMPACT()](../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.

{% tabs %}
{% tab title="Current" %}
MariaDB Enterprise Audit supports [Object Filters](mariadb-enterprise-audit.md#object-filters) for Table Events.
{% endtab %}

{% tab title="< 10.6 / 10.5.12 / 10.4.21" %}
MariaDB Enterprise Audit does **not** support [Object Filters](mariadb-enterprise-audit.md#object-filters) for Table Events.
{% endtab %}
{% endtabs %}

## Logging Filter

MariaDB Enterprise Audit supports a special Logging Filter that can be used in Audit Filters to enable or disable audit logging for any users that are assigned the Audit Filter.

The Logging Filter can be added to an Audit Filter with the logging key, which supports the following values:

| Value | Description                                  |
| ----- | -------------------------------------------- |
| ON    | Enables audit logging for this Audit Filter  |
| OFF   | Disables audit logging for this Audit Filter |

For example, the following query defines a [Default Audit Filter](mariadb-enterprise-audit.md#default-audit-filter) that enables logging for all Events for any user account without a [Named Audit Filter](mariadb-enterprise-audit.md#named-audit-filters):

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES (
       'default',
       JSON_COMPACT(
           '{
              "logging": "ON"
           }'
       )
    );
```

The example passes the JSON object to the [JSON\_COMPACT()](../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.

## Object Filters

{% hint style="info" %}
Object Filters are available from MariaDB 10.6, 10.5.12, and 10.4.21.
{% endhint %}

Object Filters allow Audit Filters to be limited to specific databases and/or tables. Object Filters can be specified at different scopes:

* An Object Filter can be specified for an entire Audit Filter
* An Object Filter can be specified for a single Event for the Audit Filter

### Object Filter Format

Object Filters are formatted as JSON objects, which are key-value pairs.

For Object Filters, the key in the key-value pair refers to the specific type of Object Filter. The following types of Object Filters are supported:

| Audit Log? | Object Filter Key | Description                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No         | ignore\_databases | When one or more databases are specified with the ignore\_databases Object Filter key, the specified databases will not be audit logged. The ignore\_databases Object Filter key is an alias for the ignore\_tables Object Filter key, with the table identifier set to the wildcard character (\*). The ignore\_databases Object Filter key cannot be specified in the same Object Filter as the log\_databases and log\_tables Object Filter keys. |
| No         | ignore\_tables    | When one or more tables are specified with the ignore\_tables Object Filter key, the specified tables will not be audit logged. Table names must be provided in the form database.table. Wildcard characters (\*) are allowed. The ignore\_tables Object Filter key cannot be specified in the same Object Filter as the log\_databases and log\_tables Object Filter keys.                                                                          |
| Yes        | log\_databases    | When one or more databases are specified with the log\_databases Object Filter key, the specified databases will be audit logged, and all other databases will not be audit logged. The log\_databases Object Filter key is an alias for the log\_tables Object Filter key, with the table identifier set to the wildcard character (`*`).                                                                                                           |
| Yes        | log\_tables       | When one or more databases are specified with the log\_tables Object Filter key, the specified tables will be audit logged, and all other tables will not be audit logged. Table names must be provided in the form database.table. Wildcard characters (`*`) are allowed.                                                                                                                                                                           |

The values in the key-value pair refer to iniobject names.

When the Object Filter only applies to one object, the object name can be specified as a string scalar value in the JSON object:

```json
{"object_filter_key": "object"}
```

When the Object Filter applies to multiple objects, the object names can be specified in a JSON array in the JSON object:

```json
{"object_filter_key": [ "object", "object" ]}
```

In the following example, the Object Filter is designed to audit log the production and reporting databases and to skip audit logging for all other databases and tables:

```json
{"log_tables": ["production.*", "reporting.*"]}
```

And in the following example, the Object Filter is designed to skip audit logging for the production.app\_log table:

```json
{"ignore_tables": "production.app_log"}
```

The Object Filter keys must be specified in different locations in the Audit Filter's JSON object, depending on the desired scope of the Object Filter. The following sections describe how to set Object Filters in more detail.

### Set Object Filters at Event Scope

An Object Filter can be specified for a single Event Filter within an Audit Filter.

Object Filters are supported by the following Events:

* [Query Events](mariadb-enterprise-audit.md#query-events)
* [Table Events](mariadb-enterprise-audit.md#table-events)

To create an Object Filter for a single Event Filter, specify the Object Filter's JSON object as part of the JSON object for the Event Filter.

The examples below pass the JSON object to the [JSON\_COMPACT()](../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.

In the following example, the reporting Audit Filter specifies an Event Filter for Table Events with an embedded Object Filter that includes all tables in the production and reporting databases:

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES (
       'reporting',
       JSON_COMPACT(
           '{
              "table_event": [
                  "WRITE",
                  "CREATE",
                  "DROP",
                  "RENAME",
                  "ALTER",
                  {
                     "log_tables": [
                        "production.*",
                        "reporting.*"
                     ]
                  }
              ]
           }'
       )
    );
```

### Set Object Filters at Audit Filter Scope

An Object Filter can be specified for an entire Audit Filter.

To create an Object Filter at Audit Filter scope, specify the Object Filter's JSON object as part of the root JSON object for the Audit Filter.

The examples below pass the JSON object to the [JSON\_COMPACT()](../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.

In the following example, the reporting Audit Filter specifies an Object Filter that includes all tables in the production and reporting databases:

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES (
       'reporting',
       JSON_COMPACT(
          '{
              "log_tables": [
                  "production.*",
                  "reporting.*"
              ]
          }'
       )
    );
```

When an Object Filter is specified at Audit Filter scope, it can contain embedded Event Filters. The following Event types support Object Filters:

* [Query Events](mariadb-enterprise-audit.md#query-events)
* [Table Events](mariadb-enterprise-audit.md#table-events)

In the following example, the reporting Audit Filter has been modified to include Event Filters on specific Query Event sub-classes and Table Event sub-classes:

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES (
       'reporting',
       JSON_COMPACT(
          '{
              "log_tables": [
                  "production.*",
                  "reporting.*",
                  {
                     "query_event": [
                         "DML",
                         "DDL"
                     ],
                     "table_event": [
                         "WRITE",
                         "CREATE",
                         "DROP",
                         "RENAME",
                         "ALTER"
                     ]
                  }
              ]
          }'
       )
    );
```

### Combine Object Filters at Audit Filter and Event Scope

When an Object Filter is specified at Audit Filter scope with embedded Event Filters, the embedded Event Filters can contain additional Object Filters. When you combine Object Filters at different levels, it is possible to combine Object Filters that are normally incompatible, like tables and ignore\_tables.

To create Object Filters at Audit Filter and Event Type scope, specify the JSON object for the Object Filter at Audit Filter scope as part of the root JSON object for the Audit Filter and specify the JSON object for the Object Filter at Event Type scope as part of the JSON object for the Event Filter.

The examples below pass the JSON object to the [JSON\_COMPACT()](../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.

In the following example, the reporting Audit Filter specifies an Event Filter for Table Events with an embedded Object Filter that includes all tables in the production and reporting databases, but it excludes Query Events that target specific tables that store Personally Identifiable Information (PII), so that the sensitive information does not appear in the audit log:

```sql
INSERT INTO mysql.server_audit_filters (filtername, rule)
   VALUES (
       'reporting',
       JSON_COMPACT(
          '{
              "log_tables": [
                  "production.*",
                  "reporting.*",
                  {
                     "table_event": [
                         "WRITE",
                         "CREATE",
                         "DROP",
                         "RENAME",
                         "ALTER"
                     ],
                     "query_event": [
                         "DML",
                         "DDL",
                         {
                             "ignore_tables": [
                                 "production.customer_profiles",
                                 "production.customer_addresses"
                             ]
                         }
                     ]
                  }
              ]
          }'
       )
    );
```

## Audit Log Destinations

MariaDB Enterprise Audit writes audit log messages either to a dedicated audit log file or to the system log (syslog), depending on configuration.

The audit log destination is configured with the [dit\_output\_type|server\_audit\_output\_type](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_au) system variable:

| Value                                                             | Description                                                |
| ----------------------------------------------------------------- | ---------------------------------------------------------- |
| [FILE](mariadb-enterprise-audit.md#audit-logging-to-file)         | Audit log messages are written to a dedicated file.        |
| [SYSLOG](mariadb-enterprise-audit.md#audit-logging-to-system-log) | Audit log messages are written to the system log (syslog). |

## Audit Logging to File

MariaDB Enterprise Audit writes audit log messages to a dedicated audit log file when the [dit\_output\_type|server\_audit\_output\_type](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_au) system variable is set to FILE.

### Audit Log Path

The path to the dedicated audit log file is configured with the [server\_audit\_file\_path](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_path) system variable. The path can be a relative or absolute path. If it is a relative path, then it will be relative to the [datadir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir). For example, to set the path to mariadb-enterprise-audit.log with the [SET GLOBAL](../sql-statements/administrative-sql-statements/set-commands/set.md) statement:

```sql
SET GLOBAL server_audit_file_path = 'mariadb-enterprise-audit.log'
```

When a system variable is dynamically changed with the [SET GLOBAL](../sql-statements/administrative-sql-statements/set-commands/set.md) statement, the change does not survive server restarts. To ensure that the new path is used when the server restarts, set the [server\_audit\_file\_path](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_path) system variable in a configuration file:

```ini
[mariadb]
server_audit_file_path=mariadb-enterprise-audit.log
```

### Audit Log Rotation

When MariaDB Enterprise Audit is configured to use the dedicated audit log file, it can rotate the file.

The file is rotated when its size exceeds the size specified by the [server\_audit\_file\_rotate\_size](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_rotate_size) system variable. For example, to set the maximum log size to 2 GB with the [SET GLOBAL](../sql-statements/administrative-sql-statements/set-commands/set.md) statement:

```sql
SET GLOBAL server_audit_file_rotate_size = 2 * (1024 * 1024 * 1024);
```

When a system variable is dynamically changed with the [SET GLOBAL](../sql-statements/administrative-sql-statements/set-commands/set.md) statement, the change does not survive server restarts. To ensure that the new file rotation size is used when the server restarts, set the [server\_audit\_file\_rotate\_size](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_rotate_size) system variable in a configuration file:

```ini
[mariadb]
...
server_audit_file_rotate_size=2147483648
```

The file can also be rotated manually by setting the [server\_audit\_file\_rotate\_now](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_rotate_now) system variable to ON. For example, to rotate the log with the [SET GLOBAL](../sql-statements/administrative-sql-statements/set-commands/set.md) statement:

```sql
SET GLOBAL server_audit_file_rotate_now = ON;
```

## Audit Logging to System Log

MariaDB Enterprise Audit writes audit log messages to the system log (syslog) when the [server\_audit\_output\_type](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_output_type) system variable is set to SYSLOG.

It can be very useful to configure audit logging to the syslog when your system's syslog is configured to securely transmit logs to a remote syslog server.

### System Log Parameters

Several syslog parameters can be changed for MariaDB Enterprise Audit by setting the following system variables:

* [server\_audit\_syslog\_facility](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_syslog_facility)
* [server\_audit\_syslog\_ident](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_syslog_ident)
* [server\_audit\_syslog\_info](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_syslog_info)
* [server\_audit\_syslog\_priority](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_syslog_priority)

## Audit Log Format

The audit log format for MariaDB Enterprise Audit depends on the [audit log destination](mariadb-enterprise-audit.md#audit-log-destinations).

### Audit Log Format with File

When MariaDB Enterprise Audit is configured to use a dedicated audit log file, it uses the following format for each line:

```
<timestamp>,<serverhost>,<username>,<host>,<connectionid>,<queryid>,<operation>,<database>,<object>,<retcode>
```

### Audit Log Format with Syslog

When MariaDB Enterprise Audit is configured to use the syslog, it uses the following format for each line:

```
<timestamp> <syslog_host> <syslog_ident>: <syslog_info> <serverhost>,<username>,<host>,<connectionid>,<queryid>,<operation>,<database>,<object>,<retcode>
```

## Messages in MariaDB Error Log

MariaDB Enterprise Audit writes messages to the MariaDB Error Log in various scenarios. Some of the scenarios and log messages are described below.

### Load Plugin

When MariaDB Enterprise Server loads the plugin for MariaDB Enterprise Audit, MariaDB Enterprise Audit writes the following message in the MariaDB error log:

```
2021-08-03 21:07:03 server_audit: MariaDB Audit Plugin version 2.0.3 STARTED.
```

For additional information, see "[Load the Audit Plugin](mariadb-enterprise-audit.md#load-the-audit-plugin)".

### Unload Plugin

When MariaDB Enterprise Server unloads the plugin for MariaDB Enterprise Audit, MariaDB Enterprise Audit writes the following message in the MariaDB error log:

```
2021-08-02 23:54:59 server_audit: STOPPED
```

The plugin is unloaded when MariaDB Enterprise Server is shutdown, so this message is most commonly written to the MariaDB error log during the shutdown process.

### Start Audit Logging to File

When audit logging is started and it is directed to a file, MariaDB Enterprise Audit writes the following message in the MariaDB error log:

{% code overflow="wrap" %}
```log
2021-08-03 21:39:42 server_audit: logging started to the file server_audit.log.
```
{% endcode %}

If a custom [audit log path](mariadb-enterprise-audit.md#audit-log-path) is configured, then the message will refer to the custom path.

For additional information, see "[Start Audit Logging](mariadb-enterprise-audit.md#start-audit-logging)" and "[Audit Logging to File](mariadb-enterprise-audit.md#audit-logging-to-file)".

### Start Audit Logging to Syslog

When audit logging is started and it is directed to syslog, MariaDB Enterprise Audit writes the following message in the MariaDB error log:

For additional information, see "[Start Audit Logging](mariadb-enterprise-audit.md#start-audit-logging)" and "[Audit Logging to Syslog](mariadb-enterprise-audit.md#audit-logging-to-system-log)".

```log
2021-08-03 22:02:45 server_audit: logging started to the syslog.
```

### Stop Audit Logging

When audit logging is stopped, MariaDB Enterprise Audit writes the following message in the MariaDB error log:

```log
2021-08-03 21:39:50 server_audit: logging was stopped.
```

### Change Audit Logging to File

When audit logging is changed to a file, MariaDB Enterprise Audit writes the following message in the MariaDB error log:

```log
2021-08-03 22:03:31 server_audit: Output was redirected to 'file'
```

For additional information, see "[Audit Logging to File](mariadb-enterprise-audit.md#audit-logging-to-file)".

### Change Audit Logging to Syslog

When audit logging is changed to syslog, MariaDB Enterprise Audit writes the following message in the MariaDB error log:

```log
2021-08-03 22:01:22 server_audit: Output was redirected to 'syslog'
```

For additional information, see "|[mariadb-enterprise-audit/#audit-logging-to-system-logAudit Logging to Syslog](mariadb-enterprise-audit.md#audit-logging-to-system-logAudit_Logging_to_Syslog)".

### Change File Name for Audit Logging

When the file name for audit logging is changed, MariaDB Enterprise Audit writes the following message in the MariaDB error log:

```log
2021-08-03 22:05:17 server_audit: Log file name was changed to 'mariadb-enterprise-audit.log'.
```

For additional information, see "[Audit Log Path](mariadb-enterprise-audit.md#audit-log-path)".

### Reload Invalid Audit Filters

When the Audit Filters are reloaded and one or more of the Audit Filters are invalid, MariaDB Enterprise Audit writes the following message in the MariaDB error log:

```sql
2021-08-03 21:51:55 server_audit: Unknown filter function tabels.
2021-08-03 21:51:55 server_audit: Can't parse filter's 'production' definition { "tabels": "production.*" }.
2021-08-03 21:51:55 server_audit: can't load filters - old filters are saved.
```

For additional information, see "[Reload Audit Filters and Assignments](mariadb-enterprise-audit.md#reload-audit-filters-and-assignments)".

### Conflict with the Query Cache

If the query cache is enabled, `READ` Table Events may not be audit logged. If MariaDB Enterprise Audit detects during startup that the query cache is enabled, MariaDB Enterprise Audit writes the following message to the MariaDB error log:

```log
2021-08-03 21:07:03 server_audit: Query cache is enabled with the TABLE events. Some table reads can be veiled.
```

## Upgrades

MariaDB Enterprise Audit is included with MariaDB Enterprise Server. Special consideration is needed when upgrading from MariaDB releases that include the MariaDB Audit Plugin, including MariaDB Community.

For details on how to upgrade from the MariaDB Audit Plugin to MariaDB Enterprise Audit, see the sections below.

{% hint style="danger" %}
**Migrating from MariaDB Audit Plugin (v1)**

MariaDB Enterprise Audit (`server_audit2.so`) is a different and incompatible plugin from the older MariaDB Audit Plugin (`v1`, `server_audit.so`) found in Community Server or older Enterprise Server versions.

The `v1` plugin is configured with server variables (e.g., `server_audit_events`).

The Enterprise (`v2`) plugin is configured with system tables (e.g., `mysql.server_audit_filters`).

You must uninstall the `v1` plugin before using the `v2` plugin, as running both can cause server instability or deadlocks ([MENT-545](https://jira.mariadb.org/browse/MENT-545)). The following sections guide you through the full migration process, starting with checking for and removing the old plugin.
{% endhint %}

### Check for and Uninstall the v1 Plugin

#### Confirm the MariaDB Audit Plugin is Loaded

To confirm that the MariaDB Audit plugin is loaded, query the [information\_schema.PLUGINS](mariadb-enterprise-audit.md#confirm-the-audit-plugin-is-loaded) table:

```sql
SELECT PLUGIN_STATUS, PLUGIN_LIBRARY, PLUGIN_DESCRIPTION
FROM information_schema.PLUGINS
WHERE PLUGIN_NAME='SERVER_AUDIT'\G
```

```
*************************** 1. row ***************************
     PLUGIN_STATUS: ACTIVE
    PLUGIN_LIBRARY: server_audit.so
PLUGIN_DESCRIPTION: Audit the server activity
```

If you see the output shown above, then the MariaDB Audit plugin is installed, and it must be uninstalled prior to performing the upgrade or migration. Follow the instructions in the section below.

If you do not see any rows in the output, then the MariaDB Audit plugin is not installed.

#### Determine Uninstallation Method

The MariaDB Audit plugin has multiple uninstallation methods. You must choose the uninstallation method that corresponds to how the plugin was installed on your system.

To determine the uninstallation method, query the [mysql.plugin](../system-tables/the-mysql-database-tables/mysql-plugin-table.md) system table:

```sql
SELECT *
FROM mysql.plugin
WHERE name = 'SERVER_AUDIT'\G
```

```
*************************** 1. row ***************************
name: SERVER_AUDIT
  dl: server_audit.so
```

If you see the output shown above, then the MariaDB Audit plugin can be uninstalled with [UNINSTALL SONAME](mariadb-enterprise-audit.md#uninstall-with-uninstall-soname).

If you do not see any rows in the output, then the MariaDB Audit plugin call be uninstalled by [editing the configuration file](mariadb-enterprise-audit.md#uninstall-with-configuration-file).

#### Uninstall with UNINSTALL SONAME

To uninstall the MariaDB Audit Plugin with [UNINSTALL SONAME](mariadb-enterprise-audit.md#uninstall-with-uninstall-soname):

{% stepper %}
{% step %}
Check the plugin load option by querying the [information\_schema.PLUGINS](../system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md) table:

```sql
SELECT PLUGIN_STATUS, PLUGIN_LIBRARY, PLUGIN_DESCRIPTION, LOAD_OPTION
FROM information_schema.PLUGINS
WHERE PLUGIN_NAME='SERVER_AUDIT'\G
```

```
*************************** 1. row ***************************
     PLUGIN_STATUS: ACTIVE
    PLUGIN_LIBRARY: server_audit.so
PLUGIN_DESCRIPTION: Audit the server activity
       LOAD_OPTION: FORCE_PLUS_PERMANENT
```
{% endstep %}

{% step %}
Check `LOAD_OPTION` column for `FORCE_PLUS_PERMANENT`

{% hint style="info" %}
If the `LOAD_OPTION` column does not contain the value `FORCE_PLUS_PERMANENT`, then you can skip to step 5, which executes the [UNINSTALL SONAME](mariadb-enterprise-audit.md#uninstall-with-uninstall-soname) statement.
{% endhint %}

If the `LOAD_OPTION` column contains the value `FORCE_PLUS_PERMANENT`, then check your configuration files for the server-audit option:

```bash
$ grep --extended-regexp --with-filename \
   'server[-_]audit[[:blank:]]*=' \
   /etc/mysql/my.cnf \
   /etc/mysql/mariadb.conf.d/*
```

{% code overflow="wrap" %}
```
/etc/mysql/mariadb.conf.d/enable-audit.cnf:server_audit=FORCE_PLUS_PERMANENT
```
{% endcode %}
{% endstep %}

{% step %}
If the server-audit option was found in a configuration file, then remove or comment the option out:

```toml
[mariadb]
# server_audit=FORCE_PLUS_PERMANENT
```
{% endstep %}

{% step %}
If the configuration file was changed, then restart the server:

```sql
$ sudo systemctl restart mariadb
```
{% endstep %}

{% step %}
Uninstall the plugin by executing the [UNINSTALL SONAME](mariadb-enterprise-audit.md#uninstall-with-uninstall-soname) statement:

```
UNINSTALL SONAME 'server_audit';
```
{% endstep %}

{% step %}
Confirm the plugin is uninstalled by querying the [mysql.plugin](../system-tables/the-mysql-database-tables/mysql-plugin-table.md) system table:

```sql
SELECT *
FROM mysql.plugin
WHERE name = 'SERVER_AUDIT'\G
```

If the query returns no results, then the plugin has been uninstalled.
{% endstep %}
{% endstepper %}

#### Uninstall with Configuration File

To uninstall the MariaDB Audit plugin with a configuration file:

{% stepper %}
{% step %}
Check your configuration files for the `plugin_load_add` option:

```bash
$ grep --extended-regexp --with-filename \
   'plugin[-_]load[-_]add[[:blank:]]*=[[:blank:]]*server_audit' \
   /etc/mysql/my.cnf \
   /etc/mysql/mariadb.conf.d/*
```

{% code overflow="wrap" %}
```bash
/etc/mysql/mariadb.conf.d/enable-audit.cnf:plugin_load_add=server_audit
```
{% endcode %}
{% endstep %}

{% step %}
Remove or comment out the plugin\_load\_add option from the configuration file:

```ini
[mariadb]
# plugin_load_add=server_audit
```
{% endstep %}
{% endstepper %}

### Migrate v1 Settings to Enterprise Audit (v2)

#### Update System Tables

After upgrading to MariaDB Enterprise Server, execute mariadb-upgrade to create the [System Tables for Audit Filters](mariadb-enterprise-audit.md#system-tables-for-audit-filters).

#### Migrate Audit Filters

The MariaDB Audit Plugin defines Audit Filters using the [server\_audit\_events system](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_events) system variable, but MariaDB Enterprise Audit defines Audit Filters using the mysql.server\_audit\_filters system table.

If you are upgrading from the MariaDB Audit Plugin to MariaDB Enterprise Audit, perform the following procedure:

{% stepper %}
{% step %}
Remove or comment out lines involving the [server\_audit\_events system](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_events) variable from the configuration file:

```toml
[mariadb]
...
# server_audit_events=CONNECT,QUERY
```
{% endstep %}

{% step %}
Insert a replacement Audit Filter into the `mysql.server_audit_filters` system table:

```sql
INSERT INTO mysql.server_audit_filters
   VALUES ('default',
      JSON_COMPACT(
         '{
            "connect_event": "ALL",
            "query_event": "ALL"
         }'
      ));
```

The example passes the JSON object to the [JSON\_COMPACT()](../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.
{% endstep %}
{% endstepper %}

#### Migrate Users

The MariaDB Audit Plugin enables or disable audit logging for specific user accounts using the [server\_audit\_incl\_users](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_incl_users) and [server\_audit\_excl\_users](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_excl_users) system variables, but MariaDB Enterprise Audit uses the mysql.server\_audit\_users system table.

If you are upgrading from the MariaDB Audit Plugin to MariaDB Enterprise Audit, perform the following procedure:

{% stepper %}
{% step %}
Edit configuration file

Remove or comment out lines involving the [server\_audit\_incl\_users](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_incl_users) and [server\_audit\_excl\_users](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_excl_users) system variables from the configuration file:

```ini
[mariadb]
...
# server_audit_incl_users = root,app
# server_audit_excl_users = backup_user,monitor_user
```
{% endstep %}

{% step %}
For the [server\_audit\_incl\_users](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_incl_users) system variable

For any user account previously mentioned in the [server\_audit\_incl\_users](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_incl_users) system variable, determine if the user account can use the [Default Audit Filter](mariadb-enterprise-audit.md#default-audit-filter) or if the user account requires a [Named Audit Filter](mariadb-enterprise-audit.md#named-audit-filters).

Insert the relevant Audit Filters into the `mysql.server_audit_filters` system table, and insert the user assignments into the `mysql.server_audit_users` system table:

```sql
INSERT INTO mysql.server_audit_filters
   VALUES
   ('default',
      JSON_COMPACT(
         '{
            "connect_event": [
               "CONNECT",
               "DISCONNECT"
            ],
            "query_event": [
               "DML",
               "DDL"
            ]
         }'
   )),
   ('root_filter',
      JSON_COMPACT(
         '{
            "logging": "ON"
         }'
   ));
INSERT INTO mysql.server_audit_users (host, user, filtername)
   VALUES ('%', 'root', 'root_filter');
```

The example passes the JSON object to the [JSON\_COMPACT()](../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.
{% endstep %}

{% step %}
For the [server\_audit\_excl\_users](https://mariadb.com/docs/server/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables#server_audit_excl_users) system variable

For any user account previously mentioned in the [server\_audit\_excl\_users](https://mariadb.com/docs/server/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables#server_audit_excl_users) system variable, create a [Named Audit Filter](https://mariadb.com/docs/server/reference/plugins/mariadb-enterprise-audit#named-audit-filters) that acts as an exclusion filter.

Insert the relevant Audit Filters into the `mysql.server_audit_filters` system table, and insert the user assignments into the `mysql.server_audit_users` system table:

```sql
INSERT INTO mysql.server_audit_filters
   VALUES ('exclusion_filter',
      JSON_COMPACT(
         '{
            "logging": "OFF"
         }'
      ));

INSERT INTO mysql.server_audit_users (host, user, filtername)
   VALUES
   ('%', 'backup_user', 'exclusion_filter'),
   ('%', 'monitor_user', 'exclusion_filter');
```
{% endstep %}
{% endstepper %}

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
