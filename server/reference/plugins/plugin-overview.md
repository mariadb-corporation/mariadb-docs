---
description: >-
  MariaDB supports loading plugins at startup or runtime to extend
  functionality, including storage engines, security features, and logging
  capabilities, without rebuilding the server.
---

# Plugin Overview

MariaDB supports the use of plugins, software components that may be added to the core software without having to rebuild the MariaDB server from source code. Plugins can be loaded at startup, or loaded and unloaded while the server is running, without interruption. Plugins are commonly used for adding desired storage engines, additional security requirements, logging special information about the server, or even small enhancements, such as a plugin to get a timestamp as an integer.

## Querying Plugin Information

There are a number of ways to see which plugins are currently active.

A server almost always has a large number of active plugins, because the server contains a large number of built-in plugins, which are active by default and cannot be uninstalled.

### Querying Plugin Information with `SHOW PLUGINS`

The [SHOW PLUGINS](../sql-statements/administrative-sql-statements/show/show-plugins.md) statement can be used to query information about all active plugins.

For example:

```sql
SHOW PLUGINS\G;
********************** 1. row **********************
   Name: binlog
 Status: ACTIVE
   Type: STORAGE ENGINE
Library: NULL
License: GPL
********************** 2. row **********************
   Name: mysql_native_password
 Status: ACTIVE
   Type: AUTHENTICATION
Library: NULL
License: GPL
********************** 3. row **********************
   Name: mysql_old_password
 Status: ACTIVE
   Type: AUTHENTICATION
Library: NULL
License: GPL
...
```

If a plugin's `Library` column has a `NULL` value, then the plugin is built-in, and it cannot be uninstalled.

### Querying Plugin Information with information\_schema.PLUGINS

The [information\_schema.PLUGINS](../system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md) table can be queried to get more detailed information about plugins.

For example:

```sql
SELECT * FROM information_schema.PLUGINS\G
...
*************************** 65. row ***************************
           PLUGIN_NAME: user_variables
        PLUGIN_VERSION: 1.0
         PLUGIN_STATUS: ACTIVE
           PLUGIN_TYPE: INFORMATION SCHEMA
   PLUGIN_TYPE_VERSION: 110600.0
        PLUGIN_LIBRARY: NULL
PLUGIN_LIBRARY_VERSION: NULL
         PLUGIN_AUTHOR: Sergey Vojtovich
    PLUGIN_DESCRIPTION: User-defined variables
        PLUGIN_LICENSE: GPL
           LOAD_OPTION: ON
       PLUGIN_MATURITY: Stable
   PLUGIN_AUTH_VERSION: 1.0
*************************** 66. row ***************************
           PLUGIN_NAME: wsrep_provider
        PLUGIN_VERSION: 1.0
         PLUGIN_STATUS: ACTIVE
           PLUGIN_TYPE: REPLICATION
   PLUGIN_TYPE_VERSION: 2.0
        PLUGIN_LIBRARY: NULL
PLUGIN_LIBRARY_VERSION: NULL
         PLUGIN_AUTHOR: Codership Oy
    PLUGIN_DESCRIPTION: Wsrep provider plugin
        PLUGIN_LICENSE: GPL
           LOAD_OPTION: ON
       PLUGIN_MATURITY: Alpha
   PLUGIN_AUTH_VERSION: 1.0
*************************** 67. row ***************************
           PLUGIN_NAME: THREAD_POOL_GROUPS
        PLUGIN_VERSION: 1.0
         PLUGIN_STATUS: ACTIVE
           PLUGIN_TYPE: INFORMATION SCHEMA
   PLUGIN_TYPE_VERSION: 110600.0
        PLUGIN_LIBRARY: NULL
PLUGIN_LIBRARY_VERSION: NULL
         PLUGIN_AUTHOR: Vladislav Vaintroub
    PLUGIN_DESCRIPTION: Provides information about threadpool groups.
        PLUGIN_LICENSE: GPL
           LOAD_OPTION: ON
       PLUGIN_MATURITY: Stable
   PLUGIN_AUTH_VERSION: 1.0
...
```

If a plugin's `PLUGIN_LIBRARY` column has the `NULL` value, the plugin is built-in and cannot be uninstalled.

### Querying Plugin Information with `mysql.plugin`

The [mysql.plugin](../system-tables/the-mysql-database-tables/mysql-plugin-table.md) table can be queried to get information about installed plugins.

This table only contains information about plugins that have been installed via the following methods:

* The [INSTALL SONAME](../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) statement.
* The [INSTALL PLUGIN](../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md) statement.
* The [mariadb-plugin](../../clients-and-utilities/administrative-tools/mariadb-plugin.md) utility.

This table does not contain information about:

* Built-in plugins.
* Plugins loaded with the [--plugin-load-add](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add) option.
* Plugins loaded with the [--plugin-load](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) option.

This table only contains enough information to reload the plugin when the server is restarted, which means it only contains the plugin name and the plugin library.

For example:

```sql
SELECT * FROM mysql.plugin;

+------+------------+
| name | dl         |
+------+------------+
| PBXT | libpbxt.so |
+------+------------+
```

## Installing a Plugin

There are three primary ways to install a plugin:

* A plugin can be installed dynamically with an SQL statement.
* A plugin can be installed with a [mariadbd](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) option, but it requires a server restart.
* A plugin can be installed with the [mariadb-plugin](../../clients-and-utilities/administrative-tools/mariadb-plugin.md) utility, while the server is completely offline.

When you are installing a plugin, you also have to ensure that:

* The server's plugin directory is properly configured, and the plugin's library is in the plugin directory.
* The server's minimum plugin maturity is properly configured, and the plugin is mature enough to be installed.

### Installing a Plugin Dynamically

A plugin can be installed dynamically by executing either the [INSTALL SONAME](../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or the [INSTALL PLUGIN](../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md) statement.

If a plugin is installed with one of these statements, a record will be added to the [mysql.plugins](../system-tables/the-mysql-database-tables/mysql-plugin-table.md) table for the plugin. This means that the plugin will automatically be loaded every time the server restarts, unless specifically uninstalled or deactivated.

#### Installing a Plugin with `INSTALL SONAME`

You can install a plugin dynamically by executing the [INSTALL SONAME](../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) statement. [INSTALL SONAME](../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) installs all plugins from the given plugin library. This could be required for some plugin libraries.

For example, to install all plugins in the `server_audit` plugin library (which is currently only the [server\_audit](mariadb-audit-plugin/) audit plugin), you could execute the following:

```sql
INSTALL SONAME 'server_audit';
```

#### Installing a Plugin with `INSTALL PLUGIN`

You can install a plugin dynamically by executing the [INSTALL PLUGIN](../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md) statement. [INSTALL PLUGIN](../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md) installs a single plugin from the given plugin library.

For example, to install the [server\_audit](mariadb-audit-plugin/) audit plugin from the `server_audit` plugin library, you could execute the following:

```sql
INSTALL PLUGIN server_audit SONAME 'server_audit';
```

### Installing a Plugin with Plugin Load Options

A plugin can be installed with a [mariadbd](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) option by providing either the [--plugin-load-add](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add) or the [--plugin-load](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) option.

If a plugin is installed with one of these options, then a record will **not** be added to the [mysql.plugins](../system-tables/the-mysql-database-tables/mysql-plugin-table.md) table for the plugin. This means that if the server is restarted without the same option set, then the plugin will **not** automatically be loaded.

#### Installing a Plugin with `--plugin-load-add`

You can install a plugin with the [--plugin-load-add](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add) option by specifying the option as a command-line argument to [mariadbd](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or by specifying the option in a relevant server [option group](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md).

The `--plugin-load-add` option uses the following format:

* Plugins can be specified in the format `name=library`, where `name` is the plugin name and `library` is the plugin library. This format installs a single plugin from the given plugin library.
* Plugins can also be specified in the format `library`, where `library` is the plugin library. This format installs all plugins from the given plugin library.
* Multiple plugins can be specified by separating them with semicolons.

For example, to install all plugins in the `server_audit` plugin library (which is currently only the [server\_audit](mariadb-audit-plugin/) audit plugin) and also the [ed25519](authentication-plugins/authentication-plugin-ed25519.md) authentication plugin from the `auth_ed25519` plugin library, you could set the option to the following values on the command-line:

```bash
$ mariadbd --user=mysql --plugin-load-add='server_audit' --plugin-load-add='ed25519=auth_ed25519'
```

You could also set the option to the same values in an [option file](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[mariadb]
...
plugin_load_add = server_audit
plugin_load_add = ed25519=auth_ed25519
```

Special care must be taken when specifying both the [--plugin-load](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) option and the [--plugin-load-add](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add) option together. The `--plugin-load` option resets the plugin load list, and this can cause unexpected problems if you are not aware. The `--plugin-load-add` option does **not** reset the plugin load list, so it is much safer to use. See [Specifying Multiple Plugin Load Options](plugin-overview.md#specifying-multiple-plugin-load-options) for more information.

#### Installing a Plugin with `--plugin-load`

You can install a plugin with the [--plugin-load](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) option by specifying the option as a command-line argument to [mariadbd](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or by specifying the option in a relevant server [option group](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md).

The `--plugin-load` option uses the following format:

* Plugins can be specified in the format `name=library`, where `name` is the plugin name and `library` is the plugin library. This format installs a single plugin from the given plugin library.
* Plugins can also be specified in the format `library`, where `library` is the plugin library. This format installs all plugins from the given plugin library.
* Multiple plugins can be specified by separating them with semicolons.

For example, to install all plugins in the `server_audit` plugin library (which is currently only the [server\_audit](mariadb-audit-plugin/) audit plugin) and also the [ed25519](authentication-plugins/authentication-plugin-ed25519.md) authentication plugin from the `auth_ed25519` plugin library, you could set the option to the following values on the command-line:

```bash
$ mariadbd --user=mysql --plugin-load='server_audit;ed25519=auth_ed25519'
```

You could also set the option to the same values in an [option file](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[mariadb]
...
plugin_load = server_audit;ed25519=auth_ed25519
```

Special care must be taken when specifying the `--plugin-load` option multiple times, or when specifying both the --plugin-load option and the `--plugin-load-add` option together. The `--plugin-load` option resets the plugin load list, and this can cause unexpected problems if you are not aware. The `--plugin-load-add` option does **not** reset the plugin load list, so it is much safer to use. See [Specifying Multiple Plugin Load Options](plugin-overview.md#specifying-multiple-plugin-load-options) for more information.

#### Specifying Multiple Plugin Load Options

Special care must be taken when specifying the `--plugin-load` option multiple times, or when specifying both the `--plugin-load` option and the -`-plugin-load-add` option. The `--plugin-load` option resets the plugin load list, and this can cause unexpected problems if you are not aware. The `--plugin-load-add` option does **not** reset the plugin load list, so it is much safer to use.

This can have the following consequences:

* If the `--plugin-load` option is specified multiple times, then only the last instance will have any effect. For example, in the following case, the first instance of the option is reset:

```ini
[mariadb]
...
plugin_load = server_audit
plugin_load = ed25519=auth_ed25519
```

* If the --plugin-load option is specified after the `--plugin-load-add` option, then it will also reset the changes made by that option. For example, in the following case, the `--plugin-load-add` option does not do anything, because the subsequent `--plugin-load` option resets the plugin load list:

```ini
[mariadb]
...
plugin_load_add = server_audit
plugin_load = ed25519=auth_ed25519
```

* In contrast, if the `--plugin-load` option is specified before the `--plugin-load-add` option, then it will work fine, because the `--plugin-load-add` option does not reset the plugin load list. For example, in the following case, both plugins are properly loaded:

```ini
[mariadb]
...
plugin_load = server_audit
plugin_load_add = ed25519=auth_ed25519
```

### Installing a Plugin with mariadb-plugin

A plugin can be installed with the [mariadb-plugin](../../clients-and-utilities/administrative-tools/mariadb-plugin.md) utility if the server is completely offline.

The syntax is:

```sql
mariadb-plugin [options] <plugin> ENABLE|DISABLE
```

For example, to install the [server\_audit](mariadb-audit-plugin/) audit plugin, you could execute the following:

```sql
mariadb-plugin server_audit ENABLE
```

If a plugin is installed with this utility, a record will be added to the [mysql.plugins](../system-tables/the-mysql-database-tables/mysql-plugin-table.md) table for the plugin. This means that the plugin will automatically be loaded every time the server restarts, unless specifically uninstalled or deactivated.

### Configuring the Plugin Directory

When a plugin is being installed, the server looks for the plugin's library in the server's plugin directory. This directory is configured by the `plugin_dir` system variable. This can be specified as a command-line argument to [mariadbd](../../server-management/starting-and-stopping-mariadb/mariadbd.md) or it can be specified in a relevant server [option group](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[mariadb]
...
plugin_dir = /usr/lib64/mysql/plugin
```

### Configuring the Minimum Plugin Maturity

When a plugin is being installed, the server compares the plugin's maturity level against the server's minimum allowed plugin maturity. This can help prevent users from using unstable plugins on production servers. This minimum plugin maturity is configured by the [plugin\_maturity](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#plugin_maturity) system variable. This can be specified as a command-line argument to [mariadbd](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

```ini
[mariadb]
...
plugin_maturity = stable
```

### Configuring Plugin Activation at Server Startup

A plugin will be loaded by default when the server starts if:

* The plugin was installed with the [INSTALL SONAME](../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) statement.
* The plugin was installed with the [INSTALL PLUGIN](../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md) statement.
* The plugin was installed with the [mariadb-plugin](../../clients-and-utilities/administrative-tools/mariadb-plugin.md) utility.
* The server is configured to load the plugin with the [--plugin-load-add](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load-add) option.
* The server is configured to load the plugin with the [--plugin-load](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load) option.

This behavior can be changed with special options that take the form `--plugin-name`. For example, for the [server\_audit](mariadb-audit-plugin/) audit plugin, the special option is called [--server-audit](mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md).

The possible values for these special options are:

| Option Value           | Description                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OFF                    | Disables the plugin without removing it from the [mysql.plugins](../system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.                                                                                                                                                                                                                                                                                 |
| ON                     | Enables the plugin. If the plugin cannot be initialized, then the server will still continue starting up, but the plugin will be disabled.                                                                                                                                                                                                                                                                                |
| FORCE                  | Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error.                                                                                                                                                                                                                                                                                                                |
| FORCE\_PLUS\_PERMANENT | Enables the plugin. If the plugin cannot be initialized, then the server will fail to start with an error. In addition, the plugin cannot be uninstalled with [UNINSTALL SONAME](../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) while the server is running. |

A plugin's status can be found by looking at the `PLUGIN_STATUS` column of the [information\_schema.PLUGINS](../system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md) table.

## Uninstalling Plugins

Plugins that are found in the mysql.plugin table, that is those that were installed with [INSTALL SONAME](../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md), [INSTALL PLUGIN](../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md) or [mariadb-plugin](../../clients-and-utilities/administrative-tools/mariadb-plugin.md) can be uninstalled in one of two ways:

* The [UNINSTALL SONAME](../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or the [UNINSTALL PLUGIN](../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) statement while the server is running
* With [mariadb-plugin](../../clients-and-utilities/administrative-tools/mariadb-plugin.md) while the server is offline.

Plugins that were enabled as a `--plugin-load` option do not need to be uninstalled. If `--plugin-load` is omitted the next time the server starts, or the plugin is not listed as one of the `--plugin-load` entries, the plugin will not be loaded.

[UNINSTALL PLUGIN](../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) uninstalls a single installed plugin, while [UNINSTALL SONAME](../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) uninstalls all plugins belonging to a given library.

## See Also

* [List of Plugins](information-on-plugins/list-of-plugins.md)
* [INSTALL PLUGIN](../sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md)
* [INSTALL SONAME](../sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md)
* [UNINSTALL PLUGIN](../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)
* [UNINSTALL SONAME](../sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)
* [SHOW PLUGINS](../sql-statements/administrative-sql-statements/show/show-plugins.md)
* [INFORMATION\_SCHEMA.PLUGINS Table](../system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md)
* [mariadb-plugin](../../clients-and-utilities/administrative-tools/mariadb-plugin.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
