---
description: >-
  mariadb-plugin enables or disables MariaDB plugins from the command line
  while the server is offline, as an alternative to INSTALL PLUGIN and
  UNINSTALL PLUGIN.
---

# mariadb-plugin

`mariadb-plugin` is a tool for enabling or disabling [plugins](../../reference/plugins/).

The client was previously called `mysql_plugin`, and can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

It is a command line alternative to the [INSTALL PLUGIN](../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md) and [UNINSTALL PLUGIN](../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md) statements, and the `--plugin-load option` to [mariadbd](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md).

`mariadb-plugin` must be run while the server is offline, and works by adding or removing rows from the [mysql.plugin](../../reference/system-tables/the-mysql-database-tables/mysql-plugin-table.md) table.

`mariadb-plugin` basically has two use cases:

1. To add a plugin even before the first real server startup.
2. To remove a plugin that crashes the server on startup.

For the installation use case, adding a [plugin-load-add](../../reference/plugins/plugin-overview.md#installing-a-plugin-with-plugin-load-add) entry to `my.cnf` or in a separate include option file is a better alternative. In case of a plugin loaded via a `mysql.plugin` crashing the server, uninstalling the plugin with the help of `mariadb-plugin` can be the only viable action, though.

## Usage

```bash
mariadb-plugin [options] <plugin> ENABLE|DISABLE
```

`mariadb-plugin` expects to find a configuration file that indicates how to configure the plugins. The configuration file has, by default, the same name as the plugin, with an  `.ini` extension:

```bash
mariadb-plugin crazyplugins ENABLE
```

Here, `mariadb-plugin`  looks for a file called `crazyplugins.ini` :

```
crazyplugins
crazyplugin1
crazyplugin2
crazyplugin3
```

The first line should contain the name of the library object file, with no extension. The other lines list the names of the components. Each value should be on a separate line. The `#` character at the start of a line indicates a comment.

## Options

The following options can be specified on the command line, while some can be specified in the `[mysqld]` group of any option file. For options specified in a `[mysqld]` group, only the `--basedir`, `--datadir`, and `--plugin-dir` options can be used — the rest are ignored.

| Option                       | Description                                                                                     |
| ---------------------------- | ----------------------------------------------------------------------------------------------- |
| -b, --basedir=name           | The base directory for the server.                                                              |
| -d, --datadir=name           | The data directory for the server.                                                              |
| -?, --help                   | Display help and exit.                                                                          |
| -f, --my-print-defaults=name | Path to my\_print\_defaults executable. Example: /source/temp11/extra                           |
| -m, --mysqld=name            | Path to mysqld executable. Example: /sbin/temp1/mysql/bin                                       |
| -n, --no-defaults            | Do not read values from configuration file.                                                     |
| -p, --plugin-dir=name        | The plugin directory for the server.                                                            |
| -i, --plugin-ini=name        | Read plugin information from configuration file specified instead of from /\<plugin\_name>.ini. |
| -P, --print-defaults         | Show default values from configuration file.                                                    |
| -v, --verbose                | More verbose output; you can use this multiple times to get even more verbose output.           |
| -V, --version                | Output version information and exit.                                                            |

## See Also

* [List of Plugins](../../reference/plugins/information-on-plugins/list-of-plugins.md)
* [Plugin Overview](../../reference/plugins/plugin-overview.md)
* [INFORMATION\_SCHEMA.PLUGINS Table](../../reference/system-tables/information-schema/information-schema-tables/plugins-table-information-schema.md)
* [INSTALL PLUGIN](../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin.md)
* [INSTALL SONAME](../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-soname.md)
* [UNINSTALL PLUGIN](../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin.md)
* [UNINSTALL SONAME](../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
