---
description: >-
  Uninstall the v1 MariaDB Audit Plugin and migrate its settings, filters, and user lists to MariaDB Enterprise Audit (v2).
---

# Upgrading to Enterprise Audit

MariaDB Enterprise Audit is included with MariaDB Enterprise Server. Special consideration is needed when upgrading from MariaDB releases that include the MariaDB Audit Plugin, including MariaDB Community.

For details on how to upgrade from the MariaDB Audit Plugin to MariaDB Enterprise Audit, see the sections below.

{% hint style="warning" %}
**Before upgrading the package**: Remove the v1 plugin **and** every `server_audit_*` variable setting from your configuration files *before* running `apt upgrade` (or your platform's equivalent). The new Enterprise Server does not recognize the v1 variables and will fail to start if they remain. Follow the [pre-upgrade cleanup steps](#check-for-and-uninstall-the-v1-plugin) below.
{% endhint %}

{% hint style="danger" %}
**Migrating from MariaDB Audit Plugin (v1)**

MariaDB Enterprise Audit (`server_audit2.so`) is a different and incompatible plugin from the older MariaDB Audit Plugin (`v1`, `server_audit.so`) found in Community Server or older Enterprise Server versions.

The `v1` plugin is configured with server variables (e.g., `server_audit_events`).

The Enterprise (`v2`) plugin is configured with system tables (e.g., `mysql.server_audit_filters`).

You must uninstall the `v1` plugin before using the `v2` plugin, as running both can cause server instability or deadlocks ([MENT-545](https://jira.mariadb.org/browse/MENT-545)). The following sections guide you through the full migration process, starting with checking for and removing the old plugin.
{% endhint %}

## Check for and Uninstall the v1 Plugin

### Confirm the MariaDB Audit Plugin is Loaded

To confirm that the MariaDB Audit plugin is loaded, query the [information\_schema.PLUGINS](mariadb-enterprise-audit-installation.md#confirm-the-audit-plugin-is-loaded) table:

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

### Determine Uninstallation Method

The MariaDB Audit plugin has multiple uninstallation methods. You must choose the uninstallation method that corresponds to how the plugin was installed on your system.

To determine the uninstallation method, query the [mysql.plugin](../../system-tables/the-mysql-database-tables/mysql-plugin-table.md) system table:

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

If you see the output shown above, then the MariaDB Audit plugin can be uninstalled with [UNINSTALL SONAME](#uninstall-with-uninstall-soname).

If you do not see any rows in the output, then the MariaDB Audit plugin can be uninstalled by [editing the configuration file](#uninstall-with-configuration-file).

### Uninstall with UNINSTALL SONAME

To uninstall the MariaDB Audit Plugin with [UNINSTALL SONAME](#uninstall-with-uninstall-soname):

{% stepper %}
{% step %}
Check the plugin load option by querying the [information\_schema.PLUGINS](../../system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md) table:

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
If the `LOAD_OPTION` column does not contain the value `FORCE_PLUS_PERMANENT`, then you can skip to step 5, which executes the [UNINSTALL SONAME](#uninstall-with-uninstall-soname) statement.
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
Uninstall the plugin by executing the [UNINSTALL SONAME](#uninstall-with-uninstall-soname) statement:

```
UNINSTALL SONAME 'server_audit';
```
{% endstep %}

{% step %}
Confirm the plugin is uninstalled by querying the [mysql.plugin](../../system-tables/the-mysql-database-tables/mysql-plugin-table.md) system table:

```sql
SELECT *
FROM mysql.plugin
WHERE name = 'SERVER_AUDIT'\G
```

If the query returns no results, then the plugin has been uninstalled.
{% endstep %}
{% endstepper %}

### Uninstall with Configuration File

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

### Remove v1 Variable Settings

After uninstalling the plugin, also remove every `server_audit_*` system variable from your configuration files. If any of these settings remain, the new Enterprise Server will fail to start because it does not recognize them.

```bash
$ grep --extended-regexp --with-filename \
   'server_audit[_a-z]*[[:blank:]]*=' \
   /etc/mysql/my.cnf \
   /etc/mysql/mariadb.conf.d/*
```

Comment out or delete every matching line. Common variables include `server_audit_events`, `server_audit_logging`, `server_audit_incl_users`, `server_audit_excl_users`, `server_audit_file_path`, `server_audit_output_type`, `server_audit_query_log_limit`, and `server_audit_file_rotate_size`.

## Migrate v1 Settings to Enterprise Audit (v2)

### Update System Tables

After upgrading to MariaDB Enterprise Server, execute `mariadb-upgrade` to create the [System Tables for Audit Filters](mariadb-enterprise-audit-filters.md#system-tables-for-audit-filters).

{% hint style="info" %}
If `mariadb-upgrade` reports that the installation is already up to date — for example, when upgrading from Community Server 10.6 to Enterprise Server 10.6 — the audit-filter system tables will not be created. In that case, run [`mariadb-upgrade --force`](../../../clients-and-utilities/deployment-tools/mariadb-upgrade.md#f-force) to force the upgrade scripts to run anyway. See [mariadb-upgrade](../../../clients-and-utilities/deployment-tools/mariadb-upgrade.md) for the full behaviour.
{% endhint %}

### Migrate Audit Filters

The MariaDB Audit Plugin defines Audit Filters using the [server\_audit\_events system](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_events) system variable, but MariaDB Enterprise Audit defines Audit Filters using the mysql.server\_audit\_filters system table.

If you are upgrading from the MariaDB Audit Plugin to MariaDB Enterprise Audit, perform the following procedure:

{% stepper %}
{% step %}
Remove or comment out lines involving the [server\_audit\_events system](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_events) variable from the configuration file:

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

The example passes the JSON object to the [JSON\_COMPACT()](../../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.
{% endstep %}
{% endstepper %}

### Migrate Users

The MariaDB Audit Plugin enables or disable audit logging for specific user accounts using the [server\_audit\_incl\_users](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_incl_users) and [server\_audit\_excl\_users](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_excl_users) system variables, but MariaDB Enterprise Audit uses the mysql.server\_audit\_users system table.

If you are upgrading from the MariaDB Audit Plugin to MariaDB Enterprise Audit, perform the following procedure:

{% stepper %}
{% step %}
Edit configuration file

Remove or comment out lines involving the [server\_audit\_incl\_users](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_incl_users) and [server\_audit\_excl\_users](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_excl_users) system variables from the configuration file:

```ini
[mariadb]
...
# server_audit_incl_users = root,app
# server_audit_excl_users = backup_user,monitor_user
```
{% endstep %}

{% step %}
For the [server\_audit\_incl\_users](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_incl_users) system variable

For any user account previously mentioned in the [server\_audit\_incl\_users](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_incl_users) system variable, determine if the user account can use the [Default Audit Filter](mariadb-enterprise-audit-filters.md#default-audit-filter) or if the user account requires a [Named Audit Filter](mariadb-enterprise-audit-filters.md#named-audit-filters).

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

The example passes the JSON object to the [JSON\_COMPACT()](../../sql-functions/special-functions/json-functions/json_compact.md) function, so that the JSON object is compacted prior to being inserted into the system table. This step is recommended, but not required.
{% endstep %}

{% step %}
For the [server\_audit\_excl\_users](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_excl_users) system variable

For any user account previously mentioned in the [server\_audit\_excl\_users](../mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_excl_users) system variable, create a [Named Audit Filter](mariadb-enterprise-audit-filters.md#named-audit-filters) that acts as an exclusion filter.

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

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
