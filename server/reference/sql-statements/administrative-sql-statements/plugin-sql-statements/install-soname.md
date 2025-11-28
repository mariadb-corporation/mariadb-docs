---
description: >-
  Load all plugins contained within a shared library file. This statement
  automatically discovers and installs every valid plugin found in the specified
  library.
---

# INSTALL SONAME

## Syntax

```sql
INSTALL SONAME 'plugin_library'
```

## Description

This statement is a variant of [INSTALL PLUGIN](install-plugin.md). It installs **all** [plugins](../../../plugins/) from a given `plugin_library`. See [INSTALL PLUGIN](install-plugin.md) for details.

`plugin_library` is the name of the shared library thatcontains the plugin code. The file name extension (forexample, `libmyplugin.so` or `libmyplugin.dll`) can be omitted (which makes the statement look the same on all architectures).

The shared library must be located in the plugin directory (that is,the directory named by the [plugin\_dir](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#plugin_dir) system variable). The library must be in the plugin directory itself, not in a subdirectory. Bydefault, `plugin_dir` is plugin directory under the directory named bythe `pkglibdir` configuration variable, but it can be changed by settingthe value of `plugin_dir` at server startup. For example, setits value in a `my.cnf` file:

```ini
[mariadbd]
plugin_dir=/path/to/plugin/directory
```

If the value of [plugin\_dir](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#plugin_dir) is a relative path name, it istaken to be relative to the MySQL base directory (the value of the `basedir`system variable).

`INSTALL SONAME` adds one or more lines to the `mysql.plugin` table thatdescribes the plugin. This table contains the plugin name and library filename.

`INSTALL SONAME` causes the server to readoption (`my.cnf`) files just as during server startup. This enables the plugin topick up any relevant options from those files. It is possible to add pluginoptions to an option file even before loading a plugin (if the loose prefix isused). It is also possible to uninstall a plugin, edit `my.cnf`, and install theplugin again. Restarting the plugin this way enables it to the new optionvalues without a server restart.

`INSTALL SONAME` also loads and initializes the plugin code tomake the plugin available for use. A plugin is initialized by executing itsinitialization function, which handles any setup that the plugin must performbefore it can be used.

To use `INSTALL SONAME`, you must have the [INSERT privilege](../../account-management-sql-statements/grant.md) for the `mysql.plugin` table.

At server startup, the server loads and initializes any plugin that islisted in the `mysql.plugin` table. This means that a plugin is installedwith `INSTALL SONAME` only once, not every time the serverstarts. Plugin loading at startup does not occur if the server is started withthe `--skip-grant-tables` option.

When the server shuts down, it executes the de-initialization functionfor each plugin that is loaded so that the plugin has a chance toperform any final cleanup.

If you need to load plugins for a single server startup when the`--skip-grant-tables` option is given (which tells the servernot to read system tables), use the`--plugin-load` [mariadbd option](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-plugin-load).

If you need to install only one plugin from a library, use the [INSTALL PLUGIN](install-plugin.md) statement.

## Examples

To load the [LOCALES plugin](../../../data-types/string-data-types/character-sets/internationalization-and-localization/locales-plugin.md) and all of its `information_schema` tables with one statement, use

```sql
INSTALL SONAME 'locales';
```

This statement can be used instead of `INSTALL PLUGIN` even when the library contains only one plugin:

```sql
INSTALL SONAME 'ha_sequence';
```

## See Also

* [List of Plugins](../../../plugins/information-on-plugins/list-of-plugins.md)
* [Plugin Overview](../../../plugins/plugin-overview.md)
* [SHOW PLUGINS](../show/show-plugins.md)
* [INSTALL PLUGIN](install-plugin.md)
* [UNINSTALL PLUGIN](uninstall-plugin.md)
* [UNINSTALL SONAME](uninstall-soname.md)
* [SHOW PLUGINS](../show/show-plugins.md)
* [INFORMATION\_SCHEMA.PLUGINS Table](../../../system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md)
* [mysql\_plugin](../../../../clients-and-utilities/legacy-clients-and-utilities/mysql_plugin.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
