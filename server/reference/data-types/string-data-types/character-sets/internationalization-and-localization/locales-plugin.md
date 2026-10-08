---
description: >-
  The LOCALES plugin enables the INFORMATION_SCHEMA.LOCALES table and SHOW
  LOCALES statement, allowing users to view all locales compiled into the
  server.
---

# Locales Plugin

The `LOCALES` plugin creates the [LOCALES](../../../../system-tables/information-schema/information-schema-tables/information-schema-locales-table.md) table in the [INFORMATION\_SCHEMA](../../../../system-tables/information-schema/) database. The plugin also adds the [SHOW LOCALES](../../../../sql-statements/administrative-sql-statements/show/show-locales.md) statement.The table and statement can be queried to see all [locales](server-locale.md) that are compiled into the server.

## Installing the Plugin

Although the plugin's shared library is distributed with MariaDB by default, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.

The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing [INSTALL SONAME](../../../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../../../../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md). For example:

```sql
INSTALL SONAME 'locales';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the [--plugin-load](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or the [--plugin-load-add](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) options. This can be specified as a command-line argument to [mysqld](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```sql
[mariadb]
...
plugin_load_add = locales
```

## Uninstalling the Plugin

You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md). For example:

```sql
UNINSTALL SONAME 'locales';
```

If you installed the plugin by providing the [--plugin-load](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or the [--plugin-load-add](../../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) options in a relevant server [option group](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.

## Example

```sql
SELECT * FROM INFORMATION_SCHEMA.LOCALES;
+-----+-------+-------------------------------------+-----------------------+---------------------+---------------+--------------+------------------------+
| ID  | NAME  | DESCRIPTION                         | MAX_MONTH_NAME_LENGTH | MAX_DAY_NAME_LENGTH | DECIMAL_POINT | THOUSAND_SEP | ERROR_MESSAGE_LANGUAGE |
+-----+-------+-------------------------------------+-----------------------+---------------------+---------------+--------------+------------------------+
|   0 | en_US | English - United States             |                     9 |                   9 | .             | ,            | english                |
|   1 | en_GB | English - United Kingdom            |                     9 |                   9 | .             | ,            | english                |
|   2 | ja_JP | Japanese - Japan                    |                     3 |                   3 | .             | ,            | japanese               |
|   3 | sv_SE | Swedish - Sweden                    |                     9 |                   7 | ,             |              | swedish                |
|   4 | de_DE | German - Germany                    |                     9 |                  10 | ,             | .            | german                 |
|   5 | fr_FR | French - France                     |                     9 |                   8 | ,             |              | french                 |
|   6 | ar_AE | Arabic - United Arab Emirates       |                     6 |                   8 | .             | ,            | english                |
|   7 | ar_BH | Arabic - Bahrain                    |                     6 |                   8 | .             | ,            | english                |
|   8 | ar_JO | Arabic - Jordan                     |                    12 |                   8 | .             | ,            | english                |
...
| 106 | no_NO | Norwegian - Norway                  |                     9 |                   7 | ,             | .            | norwegian              |
| 107 | sv_FI | Swedish - Finland                   |                     9 |                   7 | ,             |              | swedish                |
| 108 | zh_HK | Chinese - Hong Kong SAR             |                     3 |                   3 | .             | ,            | english                |
| 109 | el_GR | Greek - Greece                      |                    11 |                   9 | ,             | .            | greek                  |
| 110 | rm_CH | Romansh - Switzerland               |                     9 |                   9 | ,             | .            | english                |
+-----+-------+-------------------------------------+-----------------------+---------------------+---------------+--------------+------------------------+
```

## Options

### `locales`

* Description: Controls how the server should treat the plugin when the server starts up.
  * Valid values are:
    * `OFF` - Disables the plugin without removing it from the [mysql.plugins](../../../../system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.
    * `ON` - Enables the plugin. If the plugin cannot be initialized, then the server still continues starting up, but the plugin will be disabled.
    * `FORCE` - Enables the plugin. If the plugin cannot be initialized, then the server fails to start with an error.
    * `FORCE_PLUS_PERMANENT` - Enables the plugin. If the plugin cannot be initialized, then the server fails to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../../../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../../../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running.
  * See [Plugin Overview: Configuring Plugin Activation at Server Startup](../../../../plugins/plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.
* Command line: `--locales=value`
* Data Type: `enumerated`
* Default Value: `ON`
* Valid Values: `OFF`, `ON`, `FORCE`, `FORCE_PLUS_PERMANENT`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
