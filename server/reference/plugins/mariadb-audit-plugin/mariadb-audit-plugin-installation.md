# MariaDB Audit Plugin - Installation

The `server_audit` plugin logs the server's activity. For each client session, it records who connected to the server (i.e., user name and host), what queries were executed, and which tables were accessed and server variables that were changed. This information is stored in a rotating log file or it may be sent to the local syslogd.

## Locating the Plugin

The `server_audit` plugin's shared library is included in MariaDB packages as the `server_audit.so` or `server_audit.dll` shared library on systems where it can be built.

The plugin must be located in the plugin directory, the directory containing all plugin libraries for MariaDB. The path to this directory is configured by the [plugin_dir](../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#plugin_dir) system variable. To see the value of this variable and thereby determine the file path of the plugin library, execute the following SQL statement:

```
SHOW GLOBAL VARIABLES LIKE 'plugin_dir';

+---------------+--------------------------+
| Variable_name | Value                    |
+---------------+--------------------------+
| plugin_dir    | /usr/lib64/mysql/plugin/ |
+---------------+--------------------------+
```

Check the directory returned at the filesystem level to make sure that you have a copy of the plugin library, `server_audit.so` or `server_audit.dll`, depending on your system. It's included in recent installations of MariaDB. If you do not have it, you should upgrade MariaDB.

## Installing the Plugin

Although the plugin's shared library is distributed with MariaDB by default, the plugin is not actually installed by MariaDB by default. There are two methods that can be used to install the plugin with MariaDB.

The first method can be used to install the plugin without restarting the server. You can install the plugin dynamically by executing [INSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md) or [INSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md). For example:

```
INSTALL SONAME 'server_audit';
```

The second method can be used to tell the server to load the plugin when it starts up. The plugin can be installed this way by providing the [--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or the [--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) options. This can be specified as a command-line argument to [mysqld](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or it can be specified in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). For example:

```
[mariadb]
...
plugin_load_add = server_audit
```

## Uninstalling the Plugin

You can uninstall the plugin dynamically by executing [UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md). For example:

```
UNINSTALL SONAME 'server_audit';
```

If you installed the plugin by providing the [--plugin-load](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) or the [--plugin-load-add](../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) options in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md), then those options should be removed to prevent the plugin from being loaded the next time the server is restarted.

## Prohibiting Uninstallation

The [UNINSTALL SONAME](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) or [UNINSTALL PLUGIN](../../sql-statements-and-structure/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) statements may be used to uninstall plugins. For the `server_audit` plugin, you might want to disable this capability. To prevent the plugin from being uninstalled, you could set the [server_audit](mariadb-audit-plugin-options-and-system-variables.md) option to `FORCE_PLUS_PERMANENT` in a relevant server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) after the plugin is loaded once:

```
[mariadb]
...
plugin_load_add = server_audit
server_audit=FORCE_PLUS_PERMANENT
```

Once you've added the option to the server's option file and restarted the server, the plugin can't be uninstalled. If someone tries to uninstall the audit plugin, then an error message will be returned. Below is an example of the error message:

```
UNINSTALL PLUGIN server_audit;

ERROR 1702 (HY000):
Plugin 'server_audit' is force_plus_permanent and can not be unloaded
```

For more information on `FORCE_PLUS_PERMANENT` and other option values for the [server_audit](mariadb-audit-plugin-options-and-system-variables.md) option, see [Plugin Overview: Configuring Plugin Activation at Server Startup](../plugin-overview.md#configuring-plugin-activation-at-server-startup) for more information.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
